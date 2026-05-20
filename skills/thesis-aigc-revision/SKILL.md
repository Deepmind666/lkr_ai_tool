---
name: thesis-aigc-revision
description: Audit and revise Chinese thesis prose to reduce AI-like generic writing by adding technical grounding, improving citation placement, and preserving DOCX formatting.
---

# Thesis AIGC Revision

Use this skill for Chinese thesis drafts when the user asks for AIGC-rate
checks, AI-like prose cleanup, or thesis paragraph revision.

## Workflow

1. Preserve the source file. For `.docx` work, copy to a new named output before
   major edits unless the user explicitly says to edit the current file.
2. If the user provides a third-party detector report, parse that report first
   and turn it into a concrete paragraph checklist. Do not rewrite unflagged
   sections mechanically.
3. Start with the detector's high-risk sections. For this MoE thesis, the usual
   high-risk sections are Chinese abstract, English abstract, Chapter 1,
   Chapter 3, Chapter 5, Chapter 6 explanation paragraphs, and Chapter 7.
4. Revise by adding concrete grounding:
   - data source, variable, equation, table, figure, script, check, or measured
     result;
   - citations at the end of the exact clause or sentence they support;
   - paragraph logic that moves from observation to mechanism to consequence.
5. Rerun local style/AIGC triage if available, then run DOCX format checks.
6. Do not promise official detector results. Local scripts are triage; the
   user's detector/report is the final judge.

## MoE Thesis Override

For `面向MoE推理的动态负载建模与仿真评估研究.docx`, these rules override generic
paper-writing habits:

- Do not write abstract text as a chapter roadmap. The abstract must not contain
  "第六章", "第 6 章", "本文第几章", "本章", or similar section-navigation phrases.
- The Chinese abstract should be substantial, close to one page, and written as:
  problem -> method -> simulation chain -> results/contribution. Do not shorten
  it just to reduce AIGC risk.
- The Chinese abstract note `注：本设计（论文）选题类型为自选题目。` must be the
  last visible text line on the Chinese abstract page. If it moves to a blank
  page, the edit has failed.
- English `Key words:` must stay on the English abstract page and keep the
  template label/capitalization. Do not let it become an orphan page.
- Keep technical words exact: routing Trace, token, expert, Rank, Top-K,
  inter-token lift, intra-token lift, peer-wise All-to-Allv, Chakra ET,
  ASTRA-sim, Converter, RTX 5090.
- Preferred technical chain: routing Trace -> expert load matrix -> Rank compute
  time -> peer-wise All-to-Allv bytes -> Chakra ET DAG -> ASTRA-sim
  parsing/running.

## Revision Rules

- Do not perform mechanical synonym replacement.
- Avoid generic thesis phrases such as "具有重要意义", "充分证明",
  "显著提升", "有效解决", "完整闭环", "赋能", "抓手", "无缝映射",
  "前置能力", and "综上所述" unless a concrete measurement or transition
  requires them.
- Do not stack many references at the end of a paragraph. Avoid forms such as
  `[3]、[4]、[5]`, `[12][13]`, `[45-53]`, or `[45]-[53]` as a substitute for
  explanation. Split the sentence and tie each citation to the specific system,
  paper, or claim it supports.
- Put citations at the end of the exact clause or sentence they support, not in
  the middle of an unsupported claim.
- Keep boundaries concrete. Prefer "该实验检查 X" over repeated disclaimers.
- When editing DOCX files, preserve existing cross-references, bookmarks,
  captions, table alignment, formulas, and user-adjusted formatting.

## Section-Specific Guidance

- Abstract: no chapter names, no roadmap prose, no generic conclusion. State the
  simulation-input problem, the data and model object, the generation method,
  the Chakra/ASTRA-sim conversion chain, and the measured result type.
- Introduction: do not write broad AI background for its own sake. Move from
  MoE routing variation to expert parallelism to simulator input mismatch.
- Related work: explain why each cited system matters for this thesis. Do not
  use broad reference ranges as a literature dump.
- Method chapters: replace "framework/module/effectiveness" claims with input,
  output, invariant, variable, and validation check.
- Experiment prose: every figure/table needs a reason before it and a compact
  interpretation after it. Name the metric and what it validates.
- Conclusion: summarize concrete contributions and limitations. Do not use
  empty slogans or overclaim real serving/QPS performance.

## DOCX Safety For AIGC Rewrites

- Never rewrite Chinese DOCX paragraphs through PowerShell here-strings. They
  can corrupt Chinese text into `????`. Save a UTF-8 Python script with
  `apply_patch`, set `PYTHONIOENCODING=utf-8`, then write a DOCX copy or the
  active WPS document.
- If the document is open in WPS, filesystem overwrite may fail while the user
  still sees the old in-memory document. For final delivery, modify through the
  active `KWPS.Application` document and call `Save()`, or ask the user to close
  the file before writing.
- For front matter, WPS visual export is the verification target. LibreOffice is
  useful for fast checks but is not enough for abstract notes, keywords, TOC,
  page numbers, or page breaks.
- AIGC cleanup is not complete until format checks still pass: citation
  superscript/jumpability, ordinary-table leading spaces/indents, algorithm
  alignment, forbidden terms, formula residue, and rendered blank-like pages.
- Before saying a DOCX edit is done, render/export and visually inspect at least
  the cover/front matter, Chinese abstract, English abstract, first TOC page,
  edited chapter pages, and conclusion pages. Text extraction is not enough.

## Delivery Gate

Before delivery, report these checks or explicitly state why one was skipped:

- high-risk AIGC sections revised;
- forbidden generic phrase scan;
- citation range/list/stack scan;
- citation superscript and jumpability;
- Chinese abstract note page position;
- English `Key words:` page position;
- ordinary table leading spaces and indents;
- algorithm-table alignment and indentation;
- formula residue and broken field text;
- rendered blank-like pages.

## 2026-05-20 Detector Lessons

- When the overall AIGC score is close to the threshold, do not keep polishing
  safe sections. Parse the report and edit only the highlighted sections. In
  report `(28)`, the remaining risk was English Abstract, local Chapter 1
  organization prose, and one Chapter 6 hardware-side evidence paragraph.
- English abstract rewrites must stay concrete and source-specific: name the
  workload file, Qwen1.5-MoE-A2.7B, Top-K expert ids, routing probabilities,
  inter-token lift, intra-token lift, expert-to-Rank placement, peer-wise
  All-to-Allv, Chakra ET, and RTX 5090 boundary evidence. Avoid generic phrases
  such as "important contribution", "comprehensive framework", or "significant
  improvement".
- Do not reduce AIGC by shortening the Chinese abstract below the user's target
  layout. Preserve the page layout and the final-note position first.
