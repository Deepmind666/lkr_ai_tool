# Patent Writing Style Rules

Use these rules when drafting or revising Chinese patent disclosures in any technical field. The purpose is to produce a document that reads like a serious patent technical disclosure, not a paper, meeting note, product brochure, or AI-generated report.

## 1. Style Mode

Choose the writing mode before drafting.

**University-review style** is suitable when the document will be read by a supervisor, research group, university IP office, or patent agent after academic review. It should emphasize:

- clear technical mechanism;
- invention boundary and technical chain;
- formulas, variables, examples, drawings, and implementation detail;
- concise comparison with existing technical categories;
- enough support for claims, without excessive product marketing.

**Enterprise-review style** is suitable when internal company reviewers care about product value and implementation. It should additionally emphasize:

- product or platform scenario;
- deployable modules, devices, systems, storage media, and interfaces;
- input/output objects that a real system can collect, generate, store, transmit, or execute;
- measurable technical effects such as resource use, latency, scheduling quality, reliability, throughput, or deployment cost.

Do not force enterprise product language into a university-style disclosure unless the user asks for it. Do not leave a software invention as a pure algorithm if the review concern is system/device protectability.

## 2. Technical Chain

Every draft should be reducible to:

`technical problem -> technical input -> processing rule -> intermediate structure -> output/execution object -> technical effect`

The chain must be specific to the current field. Do not copy MoE terms into unrelated fields. Build the vocabulary from source materials, implementation documents, papers, patents, and user-confirmed terms.

Strong chain examples:

- sensor signal -> filtering rule -> feature sequence -> fault-state determination -> equipment control instruction -> lower false alarm or faster diagnosis;
- user request and cluster state -> scheduling rule -> priority queue and resource map -> task placement result -> lower waiting time or higher utilization;
- route trace and deployment mapping -> load matrix and communication matrix -> executable simulation trace -> deployment-plan comparison before real cluster testing.

Weak chains:

- collect data -> analyze data -> improve performance;
- use AI -> make prediction -> optimize system;
- generate report -> support evaluation.

## 3. Titles

Use standard Chinese patent title patterns:

- `一种……方法及系统`
- `一种……方法、装置、设备及存储介质`
- `一种……系统、平台及装置`
- `一种……生成方法及电子设备`

Avoid:

- `系统实现` as a title ending;
- `评估方法` when the invention is actually trace generation, scheduling, control, conversion, or simulation input generation;
- overly long titles that put every feature into the title;
- temporary words such as `投稿版`、`最终版`、`可提交版`.

The title should name the protected technical object, not the research process. Prefer a title that covers both method and system when software or platform implementation matters.

## 4. Protection Points

Use 3 to 5 protection points for discussion with supervisors or reviewers. Too many points dilute the invention. Too few points may hide the technical chain.

Each protection point should have:

1. a method/system title;
2. a technical problem or prior simplified handling;
3. concrete processing rule;
4. generated technical object;
5. effect that follows from the rule.

Good title patterns:

- `一种基于……的……生成方法`
- `一种将……转换为……的方法`
- `一种面向……的……轨迹生成方法`
- `一种用于……的系统或装置`

Do not make up impressive but unclear phrases. If a phrase is not common in the field, define it or replace it with a readable expression.

## 5. Prior-Art Comparison

A comparison scheme needs a source: patent, paper, tool document, code, or product manual. Do not invent a prior-art category merely because it is rhetorically convenient.

In the disclosure body, name the technical category rather than listing many source names:

- `现有一类方案基于静态执行图进行仿真……`
- `现有一类方案按照层级总计算量描述工作负载……`
- `现有一类方案能够生成工作负载，但其输出对象难以直接表示……`

In a separate research list, report, or appendix, record concrete source names, patent numbers, links, PDF filenames, and the exact role of each source.

Do not mix:

- prior-art comparison sources;
- patents used only for writing style;
- thesis/code/project documents used as internal technical support;
- reviewer comments.

## 6. Patent Prose

Use formal but readable wording.

Preferred:

- `本发明涉及……`
- `为解决上述问题，本发明提供……`
- `在一个实施例中……`
- `进一步地……`
- `其中，……`
- `由此，……`
- `上述……`

Avoid report or AI-style expressions:

- `口径`
- `深度调研`
- `高度模仿`
- `高水平`
- `不会有错漏`
- `提交通过概率`
- `本次任务`
- `我们认为`
- `研究意义重大`

Avoid unclear verbs unless the object is specified:

- `结合` without saying which data structures are associated;
- `压缩` unless a compression operation really exists;
- `细粒度生成` because granularity is usually a description level, not the generated object;
- `可保留` when the feature is actually generated, written, represented, or recorded.

Use contrast carefully. `区别于`、`相较于`、`采用……时难以……` are acceptable, but do not mechanically repeat the same sentence pattern.

## 7. Claims

Independent claims should protect the smallest stable technical combination that creates the effect. Do not overload claim 1 with every implementation detail.

Dependent claims should hold:

- input variants;
- optional formulas;
- data structure refinements;
- module or node granularity;
- exception handling;
- compatibility formats;
- validation or conservation checks;
- output metrics;
- device/system/storage-medium implementation.

Check before delivery:

- if a feature is necessary in claim 1, do not write it later as merely optional;
- every claim term appears in the specification;
- every formula symbol is defined once and used consistently;
- system claims are not a mechanical list of modules; module functions should map to technical effects.

## 8. Formulas

For formal DOCX files, formulas must be Word/WPS equation objects or rendered equation objects. Do not leave raw LaTeX.

Patent-like formula layout:

1. introduce the formula with `满足`、`如下`、`可以表示为`;
2. put the formula on a separate line, normally near the left text indent according to the template;
3. start the next paragraph with `其中，` and define variables;
4. keep inline symbols visually consistent.

If a reference patent or user template uses left-aligned equations, do not center formulas unless the template requires it.

## 9. Drawings

Drawings must support claim interpretation.

Rules:

- black-and-white or grayscale;
- straight connectors unless a special topology requires otherwise;
- no crossing lines where a simple layout can avoid them;
- arrows meet box edges without gaps or penetration;
- labels do not touch borders;
- number modules or steps consistently, such as 101, 102 or S101, S102;
- each drawing is referenced and explained in the specification.

For method inventions, use a method flowchart. For system inventions, use a module diagram. For execution or scheduling inventions, include a dependency, timing, queue, state, or data-structure diagram when it helps identify the invention.

## 10. Word Formatting

Follow the user's template first. If no template is given:

- keep Chinese body font consistent, commonly SimSun or equivalent;
- avoid accidental blue font, comments, field codes, placeholders, and mixed font sizes;
- keep tables simple, readable, and necessary;
- avoid a final page with only a few orphan lines by modestly tightening earlier spacing or wording;
- render/export to PDF or page images and inspect visually before delivery.

For documents modeled after formal Chinese patents, `[0001]` paragraph numbering is common but not mandatory for a technical disclosure unless requested. `S101` step numbering should correspond to a flowchart and actual method sequence.

## 11. Self-Audit Questions

Before final delivery, answer internally:

- Does the title match the actual protected object?
- Are the protection points limited and coherent?
- Does each protection point state a technical means, not only a result?
- Are comparison schemes supported by sources?
- Are invented terms removed or defined?
- Can a patent agent map the text to claims, embodiments, and drawings?
- Can a technical reviewer recognize the product, system, device, data structure, or execution object?
- Are formulas, figures, and Word layout visually acceptable?
