---
name: thesis-aigc-revision
description: Audit and revise Chinese thesis prose to reduce AI-like generic writing by adding technical grounding, improving citation placement, and preserving DOCX formatting.
---

# Thesis AIGC Revision

Use this skill for Chinese thesis drafts when the user asks for AIGC-rate
checks, AI-like prose cleanup, or thesis paragraph revision.

## Workflow

1. Preserve the source file. For `.docx` work, copy to a new named output before
   editing.
2. Run the local audit script when available:

   ```powershell
   python scripts/audit_docx_aigc_style.py "D:\path\thesis.docx" > qa_aigc_audit.json
   ```

3. If the user provides a third-party detector report, parse that report first
   and create a concrete paragraph checklist. Do not rewrite unflagged sections
   mechanically.
4. Start with `aigc.top_findings` or the detector's high-risk sections. Prioritize paragraphs flagged for citation
   density, unsupported strong claims, long generic prose, or weak technical
   anchors.
5. Revise by adding concrete evidence:
   - technical objects, variables, data sources, equations, checks, or figure
     interpretations;
   - citations placed at the end of the exact clause or sentence that contains
     the supported paper, system, or factual claim;
   - paragraph logic that moves from observation to mechanism to consequence.
6. Do not promise official detector results or detector bypass. The local score
   is only a writing-risk triage signal.
7. Rerun the audit after editing. Check that `phrase_counts` and
   `top_findings` decreased, then run any relevant DOCX format checks.

## Revision Rules

- Do not perform mechanical synonym replacement.
- Avoid generic thesis phrases such as "has important significance",
  "experiments fully prove", "significantly improves", and "seamlessly maps"
  unless measurements support them.
- Do not stack many references at the end of a paragraph. Avoid forms such as
  `[3]、[4]、[5]` or broad ranges used as a substitute for explanation. Split the
  sentence and tie each citation to the specific system, paper, or claim it
  supports.
- Keep boundaries concrete. Prefer "this experiment checks X" over repeated
  disclaimers about what the work does not do.
- When editing DOCX files, preserve existing cross-references, bookmarks,
  captions, table alignment, and user-adjusted formatting.

## MoE Thesis High-Risk Sections

For the MoE/ASTRA-sim thesis, AIGC reports have repeatedly flagged the same
places. Handle them first:

- Chinese abstract and English abstract: keep them short, concrete, and
  readable. Start from the simulation-input problem, then method, then
  validation. Avoid abstract-only terms that readers cannot decode.
- Chapter summaries, 1.3/1.4 organization text, and Chapter 7: avoid parallel
  list prose. Mention the actual chain: routing Trace -> expert load matrix ->
  Rank expert compute time -> peer-wise All-to-Allv sent bytes -> Chakra ET DAG
  -> ASTRA-sim parsing/running.
- Chapter 3 and Chapter 5: replace generic "framework", "module", "mapping",
  and "effectiveness" claims with input, processing, output, invariant, and
  check.
- Experiment prose: each figure/table needs motivation before it and a compact
  interpretation after it. Do not write "the result is good" without naming the
  metric and what it validates.

## MoE Thesis Hard Wording Rules

- Keep accepted technical vocabulary: MoE, Top-K, token, expert, Rank, NPU,
  routing Trace, inter-token lift, intra-token lift, dispatch/combine,
  peer-wise, All-to-Allv, Chakra ET, ASTRA-sim, Converter.
- Avoid wording the user has rejected: `byte_list`, `口径`, `外推`, `通信重边`,
  `模型侧专家集合`, `专家访问序列`, `数据移动角度`, `expert selection trace`,
  `无缝`, `高可靠`, `充分证明`, `显著提升`.
- Do not use "not X but Y" disclaimers throughout the thesis. State the positive
  research object first; add one compact boundary sentence only where a reader
  could confuse input-chain validation with real serving/QPS prediction.
- For throughput, QPS, congestion-sensitive estimates, or RTX 5090 tests, write
  exactly what was measured. Do not imply real cluster throughput or online
  serving performance unless the experiment actually measures it.

## DOCX Safety For AIGC Rewrites

- Never rewrite Chinese DOCX paragraphs through PowerShell here-strings. They
  can corrupt Chinese text into `????`. Save a UTF-8 Python script with
  `apply_patch`, set `PYTHONIOENCODING=utf-8`, then write a new DOCX copy.
- If the document is open in WPS, filesystem overwrite may fail while the user
  still sees the old in-memory document. For final formatting or AIGC delivery,
  modify through the active `KWPS.Application` document and call `Save()`, or
  ask the user to close the file before writing.
- For front matter, WPS visual export is the verification target. Do not rely
  on LibreOffice-only pagination for abstract notes, keywords, TOC, page
  numbers, or page breaks.
- AIGC cleanup is not complete until format checks still pass: citation
  superscript/jumpability, ordinary-table leading spaces/indents, algorithm
  alignment, forbidden terms, formula residue, and rendered blank-like pages.
- Do not promise "AIGC < 5%" from local heuristics. Say which high-risk report
  sections were revised and that the official detector must be rerun.
