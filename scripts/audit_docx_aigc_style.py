from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
}

W = "{" + NS["w"] + "}"
M = "{" + NS["m"] + "}"


def qn(prefix: str, name: str) -> str:
    return "{" + NS[prefix] + "}" + name


def attr_val(el: ET.Element | None, name: str = "val") -> str:
    if el is None:
        return ""
    return el.attrib.get(qn("w", name), "")


def node_text(el: ET.Element) -> str:
    parts: list[str] = []
    for t in el.iter(qn("w", "t")):
        parts.append(t.text or "")
    return "".join(parts)


def has_desc(el: ET.Element, tag: str) -> bool:
    return el.find(".//" + tag) is not None


def para_style(p: ET.Element) -> str:
    return attr_val(p.find("./w:pPr/w:pStyle", NS))


def para_jc(p: ET.Element) -> str:
    return attr_val(p.find("./w:pPr/w:jc", NS))


def para_ind(p: ET.Element) -> dict[str, str]:
    ind = p.find("./w:pPr/w:ind", NS)
    if ind is None:
        return {}
    out: dict[str, str] = {}
    for key in ("firstLine", "hanging", "left", "right"):
        value = ind.attrib.get(qn("w", key))
        if value:
            out[key] = value
    return out


def short(s: str, n: int = 96) -> str:
    s = re.sub(r"\s+", " ", s.strip())
    return s if len(s) <= n else s[: n - 1] + "…"


def load_doc_xml(docx: Path) -> tuple[ET.Element, dict[str, str]]:
    with zipfile.ZipFile(docx) as zf:
        names = set(zf.namelist())
        required = [
            "[Content_Types].xml",
            "word/document.xml",
            "word/styles.xml",
            "word/_rels/document.xml.rels",
        ]
        missing = [name for name in required if name not in names]
        if missing:
            raise RuntimeError(f"missing core parts: {missing}")
        xml = zf.read("word/document.xml")
        root = ET.fromstring(xml)
        style_map: dict[str, str] = {}
        try:
            styles_root = ET.fromstring(zf.read("word/styles.xml"))
            for style in styles_root.findall(".//w:style", NS):
                sid = style.attrib.get(qn("w", "styleId"), "")
                name = attr_val(style.find("./w:name", NS))
                if sid:
                    style_map[sid] = name
        except Exception:
            pass
    return root, style_map


def get_body_blocks(root: ET.Element) -> list[dict]:
    body = root.find(".//w:body", NS)
    if body is None:
        return []
    blocks: list[dict] = []
    para_index = 0
    table_index = 0
    for child in list(body):
        if child.tag == qn("w", "p"):
            text = node_text(child)
            blocks.append(
                {
                    "kind": "p",
                    "index": para_index,
                    "element": child,
                    "text": text,
                    "style": para_style(child),
                    "jc": para_jc(child),
                    "ind": para_ind(child),
                    "has_omath": has_desc(child, qn("m", "oMath")),
                    "has_omath_para": has_desc(child, qn("m", "oMathPara")),
                    "manual_breaks": len(child.findall(".//w:br", NS)),
                    "tabs": len(child.findall(".//w:tab", NS)),
                }
            )
            para_index += 1
        elif child.tag == qn("w", "tbl"):
            table_index += 1
            blocks.append(
                {
                    "kind": "tbl",
                    "index": table_index,
                    "element": child,
                    "text": short(node_text(child), 160),
                }
            )
    return blocks


def section_text_width(root: ET.Element) -> int | None:
    sect = root.find(".//w:body/w:sectPr", NS)
    if sect is None:
        return None
    pg = sect.find("./w:pgSz", NS)
    mar = sect.find("./w:pgMar", NS)
    if pg is None or mar is None:
        return None
    try:
        width = int(pg.attrib.get(qn("w", "w"), "0"))
        left = int(mar.attrib.get(qn("w", "left"), "0"))
        right = int(mar.attrib.get(qn("w", "right"), "0"))
    except ValueError:
        return None
    return width - left - right


def audit_tables(root: ET.Element) -> list[dict]:
    tables = []
    for i, tbl in enumerate(root.findall(".//w:body/w:tbl", NS), start=1):
        tbl_pr = tbl.find("./w:tblPr", NS)
        tbl_w = tbl_pr.find("./w:tblW", NS) if tbl_pr is not None else None
        tbl_ind = tbl_pr.find("./w:tblInd", NS) if tbl_pr is not None else None
        jc = tbl_pr.find("./w:jc", NS) if tbl_pr is not None else None
        grid_sum = 0
        for col in tbl.findall("./w:tblGrid/w:gridCol", NS):
            try:
                grid_sum += int(col.attrib.get(qn("w", "w"), "0"))
            except ValueError:
                pass
        leading = 0
        non_center_p = 0
        non_center_v = 0
        ind_count = 0
        fixed_heights = 0
        at_least_heights = 0
        for tr in tbl.findall(".//w:tr", NS):
            h_rule = tr.find("./w:trPr/w:trHeight", NS)
            rule = h_rule.attrib.get(qn("w", "hRule"), "") if h_rule is not None else ""
            if rule == "exact":
                fixed_heights += 1
            elif rule == "atLeast":
                at_least_heights += 1
            for tc in tr.findall("./w:tc", NS):
                v_align = attr_val(tc.find("./w:tcPr/w:vAlign", NS))
                if v_align and v_align != "center":
                    non_center_v += 1
                elif not v_align:
                    non_center_v += 1
                for p in tc.findall("./w:p", NS):
                    txt = node_text(p)
                    if txt.startswith((" ", "\u3000", "\t")):
                        leading += 1
                    if para_ind(p):
                        ind_count += 1
                    if para_jc(p) != "center":
                        non_center_p += 1
        tables.append(
            {
                "table": i,
                "tblW": tbl_w.attrib.get(qn("w", "w"), "") if tbl_w is not None else "",
                "tblW_type": tbl_w.attrib.get(qn("w", "type"), "") if tbl_w is not None else "",
                "grid_sum": grid_sum,
                "tblInd": tbl_ind.attrib.get(qn("w", "w"), "") if tbl_ind is not None else "",
                "jc": attr_val(jc),
                "leading_cells": leading,
                "cell_indents": ind_count,
                "non_center_paras": non_center_p,
                "non_center_vAlign": non_center_v,
                "fixed_row_heights": fixed_heights,
                "atLeast_row_heights": at_least_heights,
            }
        )
    return tables


LATEX_PATTERNS = {
    "latex_commands": re.compile(r"\\[A-Za-z]+"),
    "dollar_math": re.compile(r"\$[^$]+\$"),
    "paren_math": re.compile(r"\\\(|\\\)|\\\[|\\\]"),
    "begin_end": re.compile(r"\\(?:begin|end)\{"),
    "raw_frac": re.compile(r"\\frac|\\dfrac|\\tfrac"),
    "raw_supsub": re.compile(r"(?<![A-Za-z0-9])[_^][A-Za-z0-9{]"),
}


def audit_latex(paragraphs: list[dict]) -> dict:
    hits: dict[str, list[dict]] = {k: [] for k in LATEX_PATTERNS}
    underscore = []
    special_counter = Counter()
    for p in paragraphs:
        text = p["text"]
        if not text:
            continue
        for ch in "\\${}^":
            if ch in text:
                special_counter[ch] += text.count(ch)
        if "_" in text:
            contexts = []
            for m in re.finditer("_", text):
                contexts.append(short(text[max(0, m.start() - 28) : m.start() + 42], 90))
            underscore.append({"index": p["index"], "style": p["style"], "text": short(text, 120), "contexts": contexts[:4]})
        for name, pat in LATEX_PATTERNS.items():
            if pat.search(text):
                hits[name].append({"index": p["index"], "style": p["style"], "text": short(text, 140)})
    return {
        "pattern_hits": {k: v for k, v in hits.items() if v},
        "underscore_paragraphs": underscore,
        "special_counter": dict(special_counter),
    }


def audit_paragraphs(blocks: list[dict]) -> dict:
    paragraphs = [b for b in blocks if b["kind"] == "p"]
    empty = []
    long_paras = []
    visible_issues = []
    formula_layout = []
    caption_like = []
    for pos, p in enumerate(paragraphs):
        text = p["text"]
        stripped = text.strip()
        before = short(paragraphs[pos - 1]["text"], 60) if pos > 0 else ""
        after = short(paragraphs[pos + 1]["text"], 60) if pos + 1 < len(paragraphs) else ""
        if not stripped:
            empty.append({"index": p["index"], "style": p["style"], "before": before, "after": after})
        if len(stripped) > 520:
            long_paras.append({"index": p["index"], "style": p["style"], "chars": len(stripped), "text": short(stripped, 150)})
        if text and (text.startswith((" ", "\u3000", "\t")) or p["manual_breaks"] or p["tabs"]):
            visible_issues.append(
                {
                    "index": p["index"],
                    "style": p["style"],
                    "leading": text[:4],
                    "manual_breaks": p["manual_breaks"],
                    "tabs": p["tabs"],
                    "text": short(text, 130),
                }
            )
        if p["has_omath"] or p["has_omath_para"]:
            formula_layout.append(
                {
                    "index": p["index"],
                    "style": p["style"],
                    "chars": len(stripped),
                    "has_omath": p["has_omath"],
                    "has_omath_para": p["has_omath_para"],
                    "text": short(stripped, 140),
                }
            )
        if re.match(r"^[图表]\s*\d+(?:\.\d+)+", stripped):
            caption_like.append({"index": p["index"], "style": p["style"], "text": short(stripped, 150)})
    return {
        "empty_count": len(empty),
        "empty_samples": empty[:40],
        "long_paragraphs": long_paras,
        "visible_para_issues": visible_issues,
        "formula_layout": formula_layout,
        "caption_like": caption_like,
    }


AI_PATTERNS = [
    ("strong_claim", r"显著|极大|深刻|充分证明|充分说明|完整证明|全面证明|完全解决|精准预测|精确预测|高可靠|确证|无缝|重要意义|坚实基础|良好效果|创新性提出"),
    ("template_transition", r"需要强调的是|值得注意的是|由此可见|综上所述|总的来说|与此同时|在一定程度上|可以看出|如图所示|实验结果表明"),
    ("authorial_generic", r"本文认为|本文主要|本文首先|然后|最后|进一步说明|进一步验证|相关研究|相关工作"),
    ("boundary_terms", r"口径|外推"),
    ("contrast_template", r"不是[^。；]{0,35}而是|不仅[^。；]{0,45}而且"),
]

TECH_ANCHORS = [
    "MoE",
    "Top-K",
    "token",
    "expert",
    "rank",
    "All-to-Allv",
    "Chakra",
    "ASTRA",
    "DAG",
    "routing",
    "Trace",
    "selected_experts",
    "expert-to-rank",
    "byte_list",
    "dispatch",
    "combine",
    "Sinkhorn",
    "Zipf",
    "NPU",
    "AICB",
    "AIOB",
    "KVCache",
    "Prefill",
    "Decode",
]


def is_body_candidate(text: str, style: str) -> bool:
    stripped = text.strip()
    if len(stripped) < 28:
        return False
    if re.match(r"^(图|表)\s*\d+(?:\.\d+)+", stripped):
        return False
    if re.match(r"^\d+(?:\.\d+)*\s+", stripped):
        return False
    if stripped.startswith(("参考文献", "致谢", "附录")):
        return False
    if style and ("Title" in style or "Heading" in style):
        return False
    return True


def audit_aigc(paragraphs: list[dict]) -> dict:
    rows = []
    total_chars = 0
    risk_chars = 0
    phrase_counts = Counter()
    stop_index = None
    for p in paragraphs:
        stripped = p["text"].strip()
        if stripped.startswith("参考文献") or stripped == "致谢":
            stop_index = p["index"]
            break
    for p in paragraphs:
        if stop_index is not None and p["index"] >= stop_index:
            continue
        text = p["text"].strip()
        if not is_body_candidate(text, p["style"]):
            continue
        chars = len(re.sub(r"\s+", "", text))
        total_chars += chars
        score = 0
        reasons = []
        for label, pat in AI_PATTERNS:
            matches = sorted(set(re.findall(pat, text)))
            if matches:
                weight = 3 if label in {"strong_claim", "boundary_terms"} else 2
                score += weight * min(3, len(matches))
                reasons.append(f"{label}: {'、'.join(matches[:6])}")
                for m in matches:
                    phrase_counts[m] += 1
        anchors = [a for a in TECH_ANCHORS if a in text]
        if len(anchors) == 0 and chars >= 120:
            score += 2
            reasons.append("长段落但技术锚点不足")
        if len(re.findall(r"\[\d+(?:[-,]\d+)*\]", text)) >= 4:
            score += 1
            reasons.append("引用密度偏高，需确认不是段尾堆引用")
        if re.search(r"不属于本文评价对象|不能解释为|不用于预测|评价范围", text):
            score = max(0, score - 1)
        if score:
            risk_chars += chars
            rows.append(
                {
                    "index": p["index"],
                    "style": p["style"],
                    "chars": chars,
                    "score": score,
                    "anchors": anchors[:8],
                    "reasons": reasons,
                    "text": short(text, 220),
                }
            )
    rows.sort(key=lambda x: (-x["score"], -x["chars"], x["index"]))
    return {
        "body_chars": total_chars,
        "risk_chars": risk_chars,
        "risk_rate": round(risk_chars / total_chars, 4) if total_chars else None,
        "phrase_counts": phrase_counts.most_common(),
        "top_findings": rows[:45],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("docx", type=Path)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    root, style_map = load_doc_xml(args.docx)
    blocks = get_body_blocks(root)
    paragraphs = [b for b in blocks if b["kind"] == "p"]
    tables = audit_tables(root)
    report = {
        "source": str(args.docx),
        "source_size": args.docx.stat().st_size,
        "paragraph_count": len(paragraphs),
        "table_count": len(tables),
        "text_width_twips": section_text_width(root),
        "counts": {
            "oMath": len(root.findall(".//m:oMath", NS)),
            "oMathPara": len(root.findall(".//m:oMathPara", NS)),
            "REF": len(re.findall(r"\bREF\b", ET.tostring(root, encoding="unicode"))),
            "PAGEREF": len(re.findall(r"\bPAGEREF\b", ET.tostring(root, encoding="unicode"))),
            "bookmarkStart": len(root.findall(".//w:bookmarkStart", NS)),
            "highlight": len(root.findall(".//w:highlight", NS)),
        },
        "latex": audit_latex(paragraphs),
        "paragraphs": audit_paragraphs(blocks),
        "tables": tables,
        "aigc": audit_aigc(paragraphs),
        "style_map_sample": {k: style_map[k] for k in sorted(style_map)[:20]},
    }
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.write_text(text, encoding="utf-8")
    sys.stdout.buffer.write(text.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
