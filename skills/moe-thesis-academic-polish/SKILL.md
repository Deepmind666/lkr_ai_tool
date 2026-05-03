---
name: moe-thesis-academic-polish
description: Polish Chinese MoE/ASTRA-sim thesis drafts, DOCX chapters, abstracts, related work, experiments, and conclusions when the work must stay centered on simulation-platform input chains, expert-parallel MoE dynamic workload modeling, Chakra ET conversion, ASTRA-sim entry validation, and low-AIGC academic prose.
---

# MoE Thesis Academic Polish

Use this skill to revise Chinese undergraduate or graduate thesis prose on MoE inference simulation. The target is not generic polishing. Keep the paper centered on the simulation-platform input problem: routing trace statistics, parametric dynamic workload generation, Chakra ET conversion, and ASTRA-sim executable input.

## Core Positioning

Treat the thesis contribution as an input layer for simulation platforms, not as a new MoE model, a serving runtime, or an ASTRA-sim kernel rewrite.

Use this hierarchy throughout the document:

1. Distributed inference simulators evaluate systems cheaply, but their conclusions depend on whether workload inputs preserve key dynamic states.
2. In MoE inference, Top-K routing makes token-to-expert mappings input-dependent.
3. Under expert parallelism, routing variation becomes expert-to-rank load skew, rank-level compute imbalance, and peer-wise All-to-Allv traffic skew.
4. If the input chain keeps only layer FLOPs, average traffic, or uniform All-to-All, hot experts, slow ranks, and heavy communication edges are averaged out before simulation begins.
5. The thesis builds a trace-statistics to workload-generation to Chakra ET conversion chain so MoE routing semantics can enter ASTRA-sim 2.0.
6. Experiments evaluate statistical fidelity, conversion correctness, and entry executability; they do not predict absolute hardware throughput, QPS, or online serving performance.

## Chapter Roles

- Abstract: State the simulation-input gap first, then compress method and validation. Keep data scale and key verification anchors if already present, but avoid turning the abstract into an experiment log.
- Chapter 1: Establish the problem. Related work must compare input granularity and explain what each line solves, what it misses, and how the thesis inherits the gap.
- Chapter 2: Explain only the technical foundations needed for Chapters 4 and 5: MoE, Top-K routing, routing trace, expert parallelism, rank, expert-to-rank mapping, dispatch/combine, All-to-Allv, peer-wise byte matrix, Chakra ET, and AICB/AIOB.
- Chapter 3: Define interfaces. Make inputs, outputs, constraints, and checks explicit.
- Chapter 4: Present modeling logic. Explain why marginal distribution, inter-token lift, intra-token lift, Sinkhorn-Knopp balancing, and autoregressive Top-K sampling are needed.
- Chapter 5: Present semantic-preserving conversion. Organize by compute invariants, communication invariants, and DAG-dependency invariants.
- Chapter 6: Organize around RQ1/RQ2/RQ3. Every result should answer statistical structure, generator fidelity, or Converter correctness/executability.
- Chapter 7: Close the loop with interface contributions and research boundaries. Do not repeat the abstract.

## Paragraph Rewrite Rules

Each paragraph should have one job. Prefer the pattern "observation or conflict -> mechanism -> consequence for the simulation input chain".

Replace generic claims with concrete objects:

- weak: "该方法具有重要意义。"
- stronger: "该转换保留了rank级计算时间和逐对端All-to-Allv字节量，使路由偏斜在进入ASTRA-sim前不会被平均通信量抹平。"

Keep claims tied to data, equations, checks, or explicit boundaries. Avoid unsupported adjectives such as "有效", "显著", "充分", "可靠", "重要" unless a specific measurement supports them.

Do not overuse "本文". Avoid dense "不是……而是……" constructions. Do not use conversational phrases such as "看不到", "卡住", "很直接", or "装饰性标签".

## Related Work Logic

Do not list papers one by one. For each category, write:

1. What problem this category solves.
2. What input granularity or system state it preserves.
3. What it still does not convert into executable simulation events.
4. How the thesis uses that gap.

Prioritize work on simulation platforms and execution traces, then serving-state simulators only as boundary evidence, and MoE routing/system work as the source of dynamic workload structure. Do not let KVCache, PD separation, model architecture history, or runtime optimization become the main line unless the user explicitly asks for that scope.

Place citations close to the system, paper, or factual claim they support. Avoid long citation dumps such as `[11-14,21-23]`. Use jumpable Word/WPS cross-references when editing DOCX thesis files.

## Terminology

Use terms consistently:

- "混合专家模型（Mixture-of-Experts, MoE）" at first mention, then "MoE".
- "Top-K", not "Top-k".
- "token" in body text.
- "路由轨迹（routing trace）" at first mention, then "路由轨迹".
- "位序空间" for sorted-frequency rank space; reserve "rank" for distributed devices or logical processes.
- "逐对端" for "peer-wise".
- "All-to-Allv", not "All2Allv" or "alltoallv".
- "Chakra ET转换器" or "转换器", not mixed Converter names.
- "提升比" for lift; do not write "PMI式提升".
- "专家放置" for expert placement.

Use symbols consistently when revising formulas:

- `L`: number of layers.
- `E`: number of experts.
- `K`: Top-K value.
- `T`: token count in real traces.
- `N`: token count in online generation.
- `R`: number of ranks or NPUs.
- `W[l,e]`: generated dynamic load matrix.
- Avoid using `N` as total expert count in Chapter 5.

## Experiment Writing

Keep the evaluation boundary explicit. The experiments validate the input chain, not real hardware throughput.

Use these research questions unless the thesis already has a stronger equivalent:

- RQ1: Do real routing traces contain dynamic structures that must enter simulation inputs, including expert long tails, inter-token correlation, and intra-token co-selection?
- RQ2: Does the dynamic workload generator reproduce these structures while satisfying Top-K conservation and expert de-duplication?
- RQ3: Does the Chakra ET Converter rewrite dynamic workloads into ASTRA-sim 2.0 executable compute, communication, and DAG events?

For each figure or table, add a short motivation before it and a compact interpretation after it. Do not write "图中可以看出"; state what the measurement means for workload inputs.

Treat slowdown, wall cycles, congestion-aware estimates, and no-congestion baselines as unified-simulation proxy indicators. Do not frame them as RTX 5090 performance, real cluster latency, throughput, or QPS.

## DOCX Safety

Before editing a DOCX thesis:

1. Copy the current file to a new named version.
2. Preserve user-adjusted cover, abstract, TOC, tables, captions, references, and highlighted locations unless a concrete error is verified.
3. Inspect existing highlights, REF fields, bookmarks, reference numbering, table alignment, figure captions, and algorithms.
4. Prefer targeted OpenXML edits over whole-document style rewrites.
5. After edits, run structural checks for package validity, highlight residue, REF/bookmark integrity, citation superscripts, table alignment, and algorithm formatting.
6. Export to PDF and inspect rendered pages for small-text anomalies, title drift, broken tables, large blank pages, and misplaced captions.

Never flatten formal cross-references to plain text when the target document requires jumpable references.

## Final Checks

Before delivering, scan for:

- old terminology: "Rank空间", "PMI", "All2Allv", "Top-k", "MoE 层", "Chakra Converter";
- AI-like phrasing: "具有重要意义", "能够有效", "进一步说明", "显著提升", "充分证明", "很好地", "极大地", "由此可见";
- claims that imply real hardware prediction;
- chapter openings or summaries that drift away from the simulation-platform input chain;
- formula variables without complete explanations;
- figure/table captions without motivation and interpretation.
