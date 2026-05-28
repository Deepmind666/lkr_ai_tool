---
name: patent-disclosure-writing
description: Draft, revise, and audit Chinese patent technical disclosures and application-style Word documents, including prior-art comparison, protection-point distillation, claims, formal patent prose, formulas, drawings, and DOCX layout QA. Use when the user mentions 专利、技术交底书、权利要求、保护点、对比方案、附图、专利格式、CNIPA, or patent disclosure drafting/revision.
---

# Patent Disclosure Writing

Use this skill for Chinese invention patent disclosure work. The target is a document that a patent agent, supervisor, or technical lead can review without first asking for basic structure, evidence, formatting, or invention-boundary fixes.

For DOCX work, also load `docx-format-guard`. For literature or patent lookup, verify current facts with web or local PDFs and keep source files traceable.

Before drafting or revising a substantive patent document, read `references/chinese_patent_disclosure_checklist.md`. When the user is preparing a disclosure for a supervisor, patent agent, enterprise review, or a new technical field, also read `references/patent_writing_style_rules.md`.

## Workflow

1. **Orient the matter**: identify the latest working DOCX, source materials, target title, invention boundary, and whether this is a new draft or an iteration. In iteration mode, continue from the current disclosure rather than restarting from broad mining.
2. **Separate source roles**: distinguish (a) prior art used for comparison, (b) patents used only for writing/style reference, (c) project papers/thesis/code used as technical support, and (d) informal review comments. Do not mix these roles in the same table or folder label.
3. **Choose the review style**: use the university-review style when the audience needs technical completeness, mechanism clarity, formulas, drawings, and claim support; use the enterprise-review style when the audience emphasizes product scenario, deployable modules, system/device claims, and measurable engineering value.
4. **Define the real invention**: compress the case into a technical chain: input data -> transformation rule -> intermediate structure -> execution/output -> technical effect. Protection points must be concrete technical means, not wishes such as "improve accuracy".
5. **Build comparison logic**: write prior-art categories only when supported by patents, papers, tools, or code. In the disclosure body, use patent-style categories such as "现有一类方案..." instead of over-citing tool names; keep named sources in the research list or report.
6. **Draft claims by hierarchy**: independent claim protects the smallest stable combination that creates the effect. Dependent claims hold optional features, engineering variants, file formats, checks, compatibility paths, and implementation refinements.
7. **Write in formal patent prose**: prefer "本发明实施例..."、"在一个实施例中..."、"进一步地..."、"其中..." and avoid thesis-like commentary, report tone, AI filler, and unverifiable praise.
8. **Treat formulas and drawings as legal support**: formulas must be real Word/WPS math objects or clearly rendered objects, not raw LaTeX. Drawings must be black-and-white, numbered, readable, and referenced by the text.
9. **Render before delivery**: for Word deliverables, render/export and visually inspect key pages: title, claims, background-to-summary transition, formulas, drawings, tables, and page breaks. Fix until defects are gone.

## Document Structure

Default Chinese disclosure/application-style order:

1. 摘要
2. 权利要求书
3. 说明书：技术领域、背景技术、发明内容、附图说明、具体实施方式
4. 附图

`[0001]` paragraph numbers are common in published patents and agent-finalized application text, but they are not mandatory in a technical disclosure sent to an agent. `S101`-style method steps are useful when they correspond to a flowchart and should be used for method inventions.

## Writing Guardrails

- Do not name a file or heading "投稿版" unless the user explicitly asks. Formal files should use `{专利标题}_技术交底书`.
- Do not use informal roles such as "老师" inside deliverables. Use "审阅人"、"申请人"、"发明人"、"技术评审意见" when needed.
- Avoid terms that read like AI reports: "口径"、"深度调研"、"高度模仿"、"显著提升"、"高水平"、"不会有错漏"、"提交通过概率". Use "实验条件"、"验证性实施例"、"技术效果"、"写作格式参考" instead.
- Background technology should not sound like a paper survey. It should state the closest categories, their technical capabilities, their missing feature, and why the missing feature matters.
- Protection points should be explainable in one sentence each and traceable to claim language, specification paragraphs, and drawings.
- If a feature is optional or weakly supported by project materials, place it in dependent claims or embodiments, not as the core independent claim.

## Load When Needed

For a full drafting or audit pass, read [references/chinese_patent_disclosure_checklist.md](references/chinese_patent_disclosure_checklist.md).

For cross-domain writing style, university/enterprise review differences, title/protection-point wording, and banned weak expressions, read [references/patent_writing_style_rules.md](references/patent_writing_style_rules.md).
