---
name: moe-thesis-academic-polish
description: Polish and audit Chinese MoE/ASTRA-sim thesis drafts, DOCX chapters, abstracts, related work, formulas, figures, tables, algorithms, experiments, and conclusions while preserving the simulation-platform input-chain boundary and strict Word/WPS formatting.
---

# MoE Thesis Academic Polish

Use this skill for the thesis "面向 MoE 推理的动态负载建模与仿真评估研究" and its supporting technical documents. This is not generic proofreading. The work must stay centered on simulation-platform workload inputs: routing trace statistics, dynamic workload generation, Chakra ET conversion, ASTRA-sim entry validation, and bounded experimental interpretation.

## Core Positioning

Treat the contribution as a simulation input layer, not a new MoE model, serving runtime, ASTRA-sim kernel rewrite, or real-hardware throughput predictor.

The stable argument chain is:

1. Distributed inference simulation reduces physical-cluster experiment cost, but simulation conclusions depend on whether workload inputs preserve the dynamic states that affect execution.
2. In MoE inference, Top-K routing makes token-to-expert mappings input-dependent.
3. Under expert parallelism, routing variation becomes expert micro-batch imbalance, Rank compute-time differences, and peer-wise All-to-Allv communication differences.
4. If inputs keep only layer FLOPs, average traffic, or uniform All-to-All, hot experts, overloaded Ranks, and source-to-destination byte differences are removed before simulation.
5. The thesis builds a chain from routing trace statistics to workload generation and then to Chakra ET, so MoE routing structure can enter ASTRA-sim 2.0.
6. Experiments evaluate statistical fidelity, conversion correctness, and simulator-entry executability. They do not claim absolute hardware throughput, online QPS, or a complete serving optimization algorithm.

## Writing Style

Each paragraph should have one job. Use the pattern: observation or conflict -> mechanism -> consequence for simulation workload inputs. The first sentence should state the paragraph's core claim; the following sentences must serve that claim.

Follow the user's preferred Chapter 1 style:

- Start from simulation platforms and workload inputs, not from broad AI history.
- Preserve the accepted logic: simulation replaces expensive cluster experiments; dense Transformer inputs are relatively stable under fixed model, parallel strategy, and sequence length; MoE breaks that stability through input-dependent routing.
- Do not replace a clear user sentence with a harder but less natural sentence. If the user's wording already carries the argument, only polish grammar, term consistency, and technical precision.
- Avoid "disclaimer performance": do not repeatedly write "本文不讨论...". State the positive research object first, then add one compact boundary sentence only where misreading is likely.
- Avoid AI-like filler: "具有重要意义", "显著提升", "充分证明", "无缝", "高可靠", "取得良好效果", "由此可见", "提供坚实基础", "深刻揭示".
- Avoid rejected or unclear terms in prose: "expert selection trace", "通信重边", "模型侧专家集合", "专家访问序列", "数据移动角度", "byte_list", "外推", "口径", unexplained "输入口径".
- Prefer concrete expressions: "路由轨迹", "每层 token 实际命中的专家集合", "专家负载矩阵", "专家到 Rank 的映射", "各 Rank 承载的专家 token 数", "源 Rank 到目标 Rank 的发送字节数", "逐对端发送字节量", "仿真设置".
- Before accepting a paragraph, ask whether its first sentence is actually
  supported by the rest of the paragraph. If the body drifts into model history,
  serving runtime, or broad AI background, rewrite it back to the simulation
  input problem.
- Match the user's preferred 1.1 style: first state the simulation-platform
  requirement, then explain the MoE mechanism, then name what the input file must
  preserve. Do not add ornate phrasing when a shorter technical sentence is
  clearer.

## Chapter Roles

- Abstract: State the simulation-input problem first, then method and validation. Use readable objects such as "计算节点" before introducing "Rank" if the abstract would otherwise become opaque. The Chinese abstract can be close to one page when the user asks for a fuller version, but it must remain dense, technical, and free of generic claims.
- Chapter 1: Establish the problem. Related work should compare input granularity and explain what each line solves, what it misses, and how the thesis inherits the gap.
- Chapter 2: Explain only the foundations needed for Chapters 4 and 5: MoE, Top-K routing, routing trace, expert parallelism, Rank, expert-to-Rank mapping, dispatch/combine, All-to-Allv, peer-wise byte matrix, Chakra ET, and AICB/AIOB.
- Chapter 3: Define interfaces: inputs, outputs, constraints, and checks.
- Chapter 4: Present modeling logic. Explain why marginal distribution, inter-token lift, intra-token lift, Sinkhorn-Knopp balancing, and autoregressive Top-K sampling are needed.
- Chapter 5: Present semantic-preserving conversion by compute invariants, communication invariants, and DAG-dependency invariants.
- Chapter 6: Organize results around statistical structure, generator fidelity, and Converter correctness/executability. Every figure/table should answer one of these.
- Chapter 7: Close with interface contributions, limitations, and future work. Do not repeat the abstract.

## Related Work Logic

Do not list papers one by one. For each category, write:

1. What problem this category solves.
2. What input granularity or system state it preserves.
3. What it still does not convert into executable simulation events.
4. How the thesis uses that gap.

Prioritize simulation platforms and execution traces, then serving-state simulators as boundary evidence, and MoE routing/system work as the source of dynamic workload structure. vLLM, DistServe, Splitwise, Sarathi-Serve, KVCache, and Prefill/Decode may be mentioned only as evidence that dynamic state affects critical paths; they must not replace the thesis main line.

When citing `Patterns behind Chaos`, use it only to support that large-scale MoE routing traces contain expert activation imbalance, adjacent-token correlation, and same-token co-selection. Do not invent broader claims such as "expert access sequences determine data movement".

Place citations at the end of the clause or sentence that contains the supported
claim. Avoid long citation dumps such as `[11-14,21-23]`, `[3]、[4]、[5]`, or a
range used as a substitute for explanation. Split the prose into concrete
claims and attach the relevant citation to each claim. When editing DOCX, use
jumpable Word/WPS cross-references and superscript citation display.

## Terminology

Use terms consistently:

- "混合专家模型（Mixture-of-Experts, MoE）" at first mention, then "MoE".
- "Top-K", not "Top-k" or "Top-k".
- "token" in body text unless the user explicitly chooses "Token" for a caption or title.
- "路由轨迹（routing trace）" at first mention, then "路由轨迹".
- "位序空间" for sorted-frequency rank space; reserve "Rank" for distributed devices/logical processes.
- Use "计算节点（Rank）" at first reader-facing mention if "Rank" would be hard to read alone. Later use "Rank" or "计算节点" according to local readability.
- "逐对端" for peer-wise; "逐对端发送字节量" for the communication field in prose. Do not write `byte_list` in the thesis body.
- "All-to-Allv", not "All2Allv", "All2All", or "alltoallv".
- "Chakra ET 转换器" or "转换器"; avoid unexplained "Converter" in Chinese prose unless naming code.
- "提升比" for lift; do not write "PMI 式提升".
- "专家放置" or "专家到 Rank 的映射" for expert placement.

Use symbols consistently:

- `L`: number of layers.
- `E`: number of experts.
- `K`: Top-K value. Do not write lowercase `k` in denominators if the symbol table uses `K`.
- `T`: token count in real traces.
- `N`: token count in online generation.
- `R`: number of Ranks/NPUs.
- `W[l,e]`: generated dynamic load matrix.
- Avoid using `N` as total expert count in Chapter 5.

## Formula And Algorithm Checks

Formula correctness is a writing deliverable, not a cosmetic detail.

- Check formulas against the surrounding text and symbol table before changing prose.
- Scan for unrendered or half-rendered LaTeX: raw `\alpha`, `\beta`, `_`, `^`, `$...$`, `<=`, `>=`, duplicated variables such as `qTqT`, `LTLT`, and WPS messages such as "错误！未定义书签".
- Do not leave orphan equation objects glued to the beginning of prose, such as a stray `S_t` before "设..." or a copied symbol before "表示...".
- Equation numbering must be visible, stable, and not dependent on broken REF fields. After field updates, exported PDF must not contain "错误！未定义书签".
- If a formula was manually reconstructed, make it a real Word/WPS math object when possible; avoid plain text formulas that look inconsistent with surrounding equations.
- Algorithm tables should follow the user's thesis style: title, input, output, phases, line numbers or stable steps, top/bottom rules, readable pseudocode. Algorithm titles are left aligned in the current thesis template; pseudocode body is not centered.

## Figure, Table, And Layout Rules

When editing a DOCX thesis, load `docx-format-guard` together with this skill.

- The Chinese abstract note must stay on the Chinese abstract page near the
  last line: `注：本设计（论文）选题类型为自选题目。`. Do not place it on a
  separate blank page. Do not use large paragraph spacing that only works in
  LibreOffice; validate through WPS export.
- Classify tables before formatting. Ordinary data/comparison/result/symbol tables and algorithm tables have different alignment rules.
- Ordinary tables: remove leading spaces, full-width spaces, tabs, non-breaking spaces, first-line indents, left indents, hanging indents, and inherited body indentation. Cells should be horizontally and vertically centered unless the user's current template deliberately differs.
- Algorithm tables: do not run a global "center all table paragraphs" fix. Preserve left-aligned title/input/output/pseudocode according to the user's template.
- Table 2.1 and algorithm tables are high-risk objects. Inspect them visually after any broad table operation.
- Do not leave legacy or mixed-purpose tables. If a table combines validation coverage, congestion examples, and old matrix settings without a clear caption and local narrative, split it, rewrite it, or remove the stale part.
- Figure captions go below figures; table captions go above tables. Captions must match the nearby prose and the actual figure content.
- A figure cannot stand alone as a full page without a local explanation unless the thesis template explicitly requires it. Add a compact motivation before or interpretation after large figures.
- When replacing figures, verify: caption, body reference, image size, aspect ratio, page break, and whether the figure is still the correct technical figure from the source document or figure folder.
- Do not put old Chakra/overall-scheme figures into the wrong chapter. The Chapter 3 overall-scheme figure, Chapter 5 Chakra/DAG figures, and Chapter 4 generation-flow figures have different roles.
- For awkward vertical figure layouts, consider a left-right composite if the comparison is naturally side-by-side.
- Large figures need a local narrative. Do not leave two figures glued together
  without a paragraph explaining what the first establishes and what the second
  adds.
- Figure source must be checked against the technical source document and the
  current figure folder. If the user has replaced an AI-generated Chakra/DAG or
  overall-scheme figure, do not reinsert the obsolete one.
- For tables, "no two leading spaces" is a hard blocker. Inspect literal leading
  whitespace and hidden Word indentation (`w:ind`) in every cell, then verify by
  rendering. This rule also applies when the current task only edits prose but
  the final deliverable is a DOCX.

## Experiment Writing

Keep the evaluation boundary explicit and positive. The experiments validate the input chain, not real hardware throughput.

Use these research questions unless the thesis already has stronger equivalents:

- RQ1: Do real routing traces contain dynamic structures that must enter simulation inputs, including expert long tails, inter-token correlation, and intra-token co-selection?
- RQ2: Does the dynamic workload generator reproduce these structures while satisfying Top-K conservation and expert de-duplication?
- RQ3: Does the Chakra ET Converter rewrite dynamic workloads into ASTRA-sim 2.0 executable compute, communication, and DAG events?

For each figure/table, write a short motivation before it and a compact interpretation after it. Avoid "图中可以看出"; state what the measurement means for workload inputs.

Treat wall cycles, congestion-aware estimates, no-congestion baselines, slowdown, and smoke checks as unified-simulation proxy indicators. Do not frame them as RTX 5090 performance, real cluster latency, throughput, or QPS.

Generator performance profiling should be discussed carefully: if Sinkhorn-Knopp is matrix-level preprocessing, do not claim it runs for every token. Explain whether the main cost comes from autoregressive sampling, validation, file writing, or simulator entry checks.

## Reference Hygiene

Bibliography order should follow first appearance in the main text unless the user freezes another order.

Do not list a GitHub repository as a separate reference when the thesis already cites a formal paper, arXiv preprint, proceedings paper, or technical report for the same tool/system. This rule is not permission to shrink the bibliography. Only remove repository entries that are true duplicates of formal references, or entries the user explicitly approves for deletion. If a GitHub repository, web page, report, survey, or preprint has no formal-paper replacement in the thesis, preserve it and keep or restore its in-text citation.

## DOCX Delivery Gate

Before delivering any edited thesis DOCX:

1. Copy the current file to a new named version.
2. Preserve user-adjusted cover, abstract, TOC, tables, captions, references, highlighted text, and manually adjusted layout unless a concrete error is verified.
3. Inspect highlights, comments, REF fields, bookmarks, citation fields, reference numbering, table alignment, figure captions, and algorithms.
4. Prefer targeted OpenXML edits over whole-document style rewrites.
5. Export to PDF through WPS/Word and inspect rendered pages for broken formulas, wrong font/size, blank pages, image/caption mismatch, table overflow, and broken fields. WPS export is mandatory when the user edits or reviews in WPS.
6. Run structural checks and report them separately:
   - package validity;
   - citation superscript and jumpability;
   - forbidden terms;
   - ordinary table leading spaces/indent/alignment/vertical alignment;
   - algorithm title/body alignment;
   - formula broken-field strings;
   - Chinese abstract note page placement;
   - blank-like pages in rendered PDF.

Never claim a DOCX is fixed only from XML/text extraction. Rendered visual QA is mandatory when figures, formulas, algorithms, or tables are touched.

If WPS/Word export fails through `Word.Application` but the DOCX package audit
passes, try `KWPS.Application` before declaring the file corrupted. When using
scripts to rewrite Chinese text, use UTF-8 Python files rather than PowerShell
here-strings, which can corrupt Chinese text into `????`.

## External AIGC Report Workflow

When the user provides an AIGC report zip, do not rewrite the whole chapter.
Extract the report, list the exact flagged paragraphs, and revise only those
paragraphs. For citation-heavy paragraphs, preserve existing REF/PAGEREF field
runs and edit only surrounding text runs; otherwise cross-references may lose
jumpability.

For the current MoE thesis, recent high-risk sections were English Abstract,
the 1.2.4 boundary paragraph cluster, Chapter 6 data-scope paragraphs, and the
Chapter 7 conversion summary. The Chinese abstract was not always the hotspot:
check the report before changing it. Keep paragraph count and page layout stable
unless the user explicitly asks to change length.

If the target DOCX is open in WPS and the filesystem copy/write fails, do not
keep editing a stale temporary copy. Either use the active `KWPS.Application`
document object and `Save()`, or ask the user to close the file before writing.

## Final Scan

Before final response, scan the edited scope for:

- rejected terms: `byte_list`, "通信重边", "模型侧专家集合", "专家访问序列", "数据移动角度", "expert selection trace", "外推", "口径", "无缝", "高可靠", `Orders in Chaos`;
- old terminology: "Rank空间", "PMI", "All2Allv", "Top-k", "Chakra Converter";
- broken fields: "错误！未定义书签";
- unrendered formula residue: raw LaTeX, duplicated symbols, lowercase `k` where `K` is required;
- unsupported claims that imply real hardware prediction;
- figure/table captions without local motivation and interpretation.
