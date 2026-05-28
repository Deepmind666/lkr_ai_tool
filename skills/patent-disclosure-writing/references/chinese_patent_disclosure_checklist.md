# Chinese Patent Disclosure Checklist

This checklist captures practical lessons for drafting Chinese patent technical disclosures that resemble formal patent documents while remaining useful for agent review.

## 1. Invention Boundary

Before writing, state the invention as a chain:

`technical input -> conversion rule -> intermediate data structure -> executable/output form -> measurable technical effect`

For system/simulation/software cases, the protectable invention is usually not "we analyze data" or "we improve evaluation", but a reproducible conversion mechanism, data structure, execution graph, scheduling method, storage method, verification method, or interface adaptation method.

Ask:

- What is the nearest existing system already able to do?
- What exactly does it not produce, preserve, or distinguish?
- Which minimal combination of steps makes the missing effect appear?
- Which parts are core and which are implementation preferences?

## 2. Prior-Art Comparison

A comparison category must have support. Use papers, patents, tool documentation, or source code. Do not invent an "average method" category without a source basis.

Use this structure:

1. Category A: what it does.
2. What data granularity or execution state it preserves.
3. What it fails to convert, distinguish, or output.
4. Why that failure matters technically.

In the disclosure body, avoid turning this into a literature review. Write:

> 现有一类方案能够基于执行轨迹、依赖图或集合通信接口进行集群仿真...

In a separate comparison list or oral report, it is acceptable to name concrete systems such as ASTRA-sim, Chakra, AICB, SimAI, or specific patent publication numbers.

Keep reference roles separate:

- "对比方案": closest prior art used to explain difference.
- "参考写作格式": patents used for style, numbering, drawing, and formula conventions.
- "技术支撑材料": thesis, code, experiments, logs, implementation notes.
- "评审意见": external comments used to improve clarity.

## 3. Protection Points

A protection point must be a technical means, preferably with a rule or structure.

Good:

- "根据 token 源执行进程和被选专家所在执行进程累加生成逐对端通信字节矩阵。"
- "构造分发通信节点、多个专家计算节点、同步依赖节点和返回通信节点，使热点专家等待进入执行依赖图。"

Weak:

- "提高仿真准确性。"
- "更好地分析 MoE 负载。"
- "支持动态负载。"

Recommended hierarchy:

1. Independent claim: stable core chain.
2. Dependent claims: input variants, formulas, matrix conservation, node granularity, communication variants, local/remote traffic handling, simulator compatibility, metrics.
3. System/device/storage-medium claims: mirror the method but keep module functions tied to the core technical effects.

## 4. Claims

Independent claims should not be only a business goal or an abstract workflow. They should include enough transformation rules to distinguish from conventional processing.

Typical method-claim skeleton:

1. obtaining concrete inputs;
2. transforming them by a specified rule;
3. generating an intermediate technical structure;
4. constructing execution/communication/dependency data;
5. outputting a file, control plan, simulation input, or device action.

Avoid overloading the independent claim with every refinement. If a feature is useful but optional, move it to a dependent claim.

Check for conflicts:

- If a feature appears as necessary in claim 1, do not later write it as optional in a dependent claim.
- Symbols in claims must match the specification.
- Every formula and term in claims must be supported by the specification.

## 5. Specification Style

Formal Chinese patent prose favors compact technical description:

- "本发明涉及..." for technical field.
- "现有一类方案..." for background.
- "为实现上述目的，本发明提供..." for summary.
- "在一个实施例中..." for variants.
- "其中..." after formulas and variables.
- "上述..." for references to prior described elements.

Avoid:

- report-like words: "本文认为"、"我们"、"本次调研"、"投稿版";
- thesis-like framing: "研究意义重大"、"本文贡献如下";
- AI filler: "深度"、"高水平"、"显著" unless backed by exact data;
- legal overpromise: "不会有错漏"、"必然授权"、"提交通过概率高".

## 6. Paragraph Numbers And Step Numbers

`[0001]` paragraph numbers are common in published CN patents and formal agent drafts. For an internal technical disclosure, they are optional. If the user is sending the document to an agent or supervisor, do not force-add `[0001]` unless requested.

`S101`、`S102` method steps are useful when:

- there is a method flowchart;
- the implementation section describes a sequence;
- later drawings or paragraphs need concise references.

Write method steps as separate short paragraphs when possible:

> S101，获取...
>
> S102，生成...

## 7. Formulas

Formula presentation should resemble formal CN patents:

- Important formulas are single-line display formulas, usually starting near the normal left text indent, not thesis-style centered unless the template requires it.
- The line before introduces the formula with "满足"、"如下" or "可以表示为".
- The following paragraph starts with "其中，" and explains variables.
- Inline symbols such as `T_s`、`src(t)`、`D[s,l,i,j]` should be real math objects or consistently formatted symbols when editing DOCX.
- Do not leave raw LaTeX such as `\sum`、`_`、`^`、`$...$` in Word deliverables.
- Render/export the document and visually inspect formulas. XML text extraction is not enough.

If Word display equations appear visually centered when left indentation is required, use a left-aligned paragraph with two full-width spaces before the formula object instead of relying on first-line indent alone.

## 8. Drawings

Formal patent drawings should be functional, not decorative.

Rules:

- black-and-white or grayscale;
- clear module numbers such as 101, 102, 103;
- straight connectors where possible;
- no crossing lines unless unavoidable;
- no curved or ornamental connectors in ordinary system/flow diagrams;
- labels do not touch borders;
- arrows meet box edges cleanly without gaps or penetration;
- figures are referenced in the specification and described by their number.

Good figure set for method/system cases:

1. system/module diagram;
2. method flowchart with S101-style steps;
3. key execution dependency diagram;
4. data-structure or matrix-generation diagram;
5. optional example/effect diagram.

Do not use screenshots or colorful research charts as patent drawings unless the user explicitly needs a technical-effect figure. If an effect figure is used, describe the experimental conditions conservatively.

## 9. DOCX And Layout QA

Before delivery:

- confirm the final path and timestamp;
- ensure the title and filename do not include "draft", "submission version", "投稿版", or unclear temporary words unless requested;
- render/export to PDF or PNG;
- inspect title, claims, formulas, background-to-summary transition, drawings, tables, and page breaks;
- confirm formulas are not raw text;
- confirm drawings have no overlapped labels or line penetration;
- confirm no accidental blue font, broken fields, comments, or hidden placeholder text remain.

If the user has the file open in Word/WPS, explain that they may be seeing an in-memory copy or cache after overwrite.

## 10. Reporting To Non-Patent Readers

When helping the user report a patent, do not recite the whole document. Use:

1. writing logic: the technical gap and conversion chain;
2. comparison schemes: supported categories and representative sources;
3. protection points: core independent features and optional dependent features;
4. risks: which features may be challenged as conventional and how the claims/specification support them.

For WeChat-style reporting, use formal but plain language. Avoid "老师" inside documents, but in a user-facing chat draft it may be acceptable if the user is writing to a supervisor.
