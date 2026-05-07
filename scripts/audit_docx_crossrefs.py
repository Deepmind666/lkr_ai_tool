#!/usr/bin/env python
"""Audit Word DOCX cross-reference fields.

This script distinguishes bibliography citation formatting from Word-native
cross references. It reports field counts (`REF`, `PAGEREF`, `SEQ`, etc.) and
lists visible figure/table/equation references that appear to be static text.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}


FIELD_RE = re.compile(r"\b(TOC|REF|PAGEREF|NOTEREF|SEQ|HYPERLINK)\b", re.I)
VISIBLE_REF_RE = re.compile(
    r"(?P<kind>图|表)\s*(?P<num>\d+(?:\.\d+)+)|"
    r"(?P<formula>式|公式)\s*[（(]?\s*(?P<fnum>\d+(?:[.-]\d+)+)\s*[）)]?"
)
CAPTION_RE = re.compile(r"^\s*(图|表)\s*\d+(?:\.\d+)+\s+")


def _text_of(el: etree._Element) -> str:
    return "".join(el.xpath(".//w:t/text()", namespaces=NS))


def _field_texts(root: etree._Element) -> list[str]:
    texts: list[str] = []
    for node in root.xpath(".//w:instrText", namespaces=NS):
        if node.text:
            texts.append(node.text)
    for node in root.xpath(".//w:fldSimple", namespaces=NS):
        instr = node.get(f"{{{NS['w']}}}instr")
        if instr:
            texts.append(instr)
    return texts


def _paragraph_style_id(p: etree._Element) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


def _static_text_of_paragraph(p: etree._Element) -> str:
    """Return paragraph text excluding Word field instructions/results.

    Field results are visible in Word, so a naive text scan would still see
    "图 6.1" after it has been converted to a REF field. For cross-reference
    auditing, we only want text that remains static outside field results.
    """

    parts: list[str] = []
    in_field = False
    for child in p.iter():
        tag = etree.QName(child).localname
        if tag == "fldChar":
            fld_type = child.get(f"{{{NS['w']}}}fldCharType")
            if fld_type == "begin":
                in_field = True
            elif fld_type == "end":
                in_field = False
            continue
        if tag == "instrText":
            continue
        if tag == "t" and not in_field:
            parts.append(child.text or "")
    return "".join(parts)


def audit_docx(path: Path) -> dict:
    with ZipFile(path) as z:
        document_xml = z.read("word/document.xml")

    root = etree.fromstring(document_xml)
    body = root.find("w:body", NS)
    if body is None:
        raise RuntimeError("word/document.xml has no w:body")

    field_counter: Counter[str] = Counter()
    field_texts = _field_texts(root)
    for instr in field_texts:
        match = FIELD_RE.search(instr)
        if match:
            field_counter[match.group(1).upper()] += 1

    hyperlink_anchor_count = len(root.xpath(".//w:hyperlink[@w:anchor]", namespaces=NS))
    bookmark_count = len(root.xpath(".//w:bookmarkStart", namespaces=NS))

    visible_refs: list[dict] = []
    captions: list[dict] = []
    in_references = False

    paragraphs = body.xpath(".//w:p", namespaces=NS)
    for idx, p in enumerate(paragraphs):
        text = _text_of(p).strip()
        if not text:
            continue

        style_id = _paragraph_style_id(p)
        if text in {"参考文献", "References", "致谢"}:
            in_references = True

        is_caption = bool(CAPTION_RE.match(text)) and style_id in {
            "-caption",
            "-caption1",
            "Caption",
        }
        if is_caption:
            captions.append({"paragraph": idx, "text": text[:160], "style": style_id})
            continue

        if in_references:
            continue

        static_text = _static_text_of_paragraph(p)
        for match in VISIBLE_REF_RE.finditer(static_text):
            value = match.group(0)
            visible_refs.append(
                {
                    "paragraph": idx,
                    "text": text[:220],
                    "reference": value,
                    "style": style_id,
                }
            )

    warnings: list[str] = []
    if visible_refs and field_counter["REF"] == 0:
        warnings.append(
            "Detected visible figure/table/equation references, but no Word REF fields. "
            "These references are likely static text, not jumpable cross-references."
        )
    if captions and field_counter["SEQ"] == 0:
        warnings.append(
            "Detected figure/table captions, but no Word SEQ caption fields. "
            "Caption numbers are likely static text."
        )

    return {
        "path": str(path),
        "field_counts": dict(field_counter),
        "instr_text_total": len(field_texts),
        "hyperlink_anchor_count": hyperlink_anchor_count,
        "bookmark_count": bookmark_count,
        "caption_count": len(captions),
        "visible_reference_count": len(visible_refs),
        "warnings": warnings,
        "sample_visible_references": visible_refs[:80],
        "sample_captions": captions[:80],
    }


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args(argv)

    report = audit_docx(args.docx)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text, encoding="utf-8")
    print(text)
    return 1 if report["warnings"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
