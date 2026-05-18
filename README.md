# lkr_ai_tool

`lkr_ai_tool` 是一个面向科研写作、文档编辑、图表制作、代码理解和项目交接的 AI 工具箱。它将常用的工作流程整理为可复用的 skill、脚本、模板和说明文档，方便在不同电脑、不同项目和不同 AI 助手之间迁移。

仓库地址：<https://github.com/Deepmind666/lkr_ai_tool>

## 项目定位

本仓库不是某一个项目的源码，也不存放私有论文、原始数据或大型实验结果。它更像一个可复用的工作方法库，适合用于：

- 论文、报告、毕业设计和投稿材料的写作与润色。
- Word/WPS/DOCX 文档的安全修改和格式保护。
- 可编辑 PPT、论文图表、流程图和示意图制作。
- 大型代码库的结构理解、上下文压缩和跨会话交接。
- 为 Codex、Claude、ChatGPT 或其它 AI 助手提供统一的工作规范。

项目专属规则应放在具体项目的 `AGENTS.md`、profile 或本地说明文件中。本仓库只保留通用方法、模板和工具配置。

## 快速使用

```powershell
git clone https://github.com/Deepmind666/lkr_ai_tool.git
cd lkr_ai_tool
```

建议先阅读以下文档：

1. `docs/usage_for_other_gpts.md`
2. `docs/migration_playbook.md`
3. `docs/tool_catalog.md`
4. `docs/token_saving_and_context_indexing.md`
5. `docs/editable_ppt_workflow.md`
6. `docs/gpt_image_2_tips.md`
7. `docs/local_experience.md`
8. `docs/codewiki_playbook.md`

## 目录结构

```text
lkr_ai_tool/
  AGENTS.md                 # 通用协作约定
  config/                   # 工具配置示例
  docs/                     # 使用说明和工作流文档
  profiles/                 # 项目 profile 模板
  scripts/                  # 可复用脚本
  skills/                   # AI 助手可调用的工作流 skill
  templates/                # 文档、PPT、图表等模板
```

## 核心能力

- 文档处理：降低 DOCX/WPS/Word 修改时的格式风险。
- 学术写作：支持论文润色、文献检索、图注撰写和低 AIGC 风格修改。
- 图表生产：保留数据、脚本、导出图和 manifest，便于复现。
- PPT 制作：优先生成可编辑的 PPTX，而不是不可修改的截图。
- 代码理解：通过索引、wiki、检索和上下文压缩理解大型仓库。
- 项目交接：保存关键决策、实验状态、后续任务和恢复信息。

## Skill 索引

`skills/` 下的每个目录对应一个可复用 skill。下表按用途列出主要功能。

### 写作、论文与文献研究

| Skill | 主要功能 | 典型用途 |
|---|---|---|
| `deep-research` | 13-agent 深度研究 pipeline。7 种模式：full / quick / paper-review / lit-review / fact-check / Socratic 引导 / systematic review (PRISMA 含 meta-analysis)。 | 研究问题构建、系统性文献检索、跨源核查、风险偏倚评估、APA 7.0 报告。源自 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.x。 |
| `academic-paper` | 12-agent 论文写作 pipeline。10 种模式（full/plan/outline/revision/abstract/lit-review/format-convert/citation-check 等），支持 6 种论文类型、5 种引用格式、双语摘要、LaTeX/DOCX/PDF 输出。含 Style Calibration、Writing Quality Check、anti-leakage protocol。 | 全文起草、章节规划、修订意见解析、AI 使用披露、写作质量检查。 |
| `academic-paper-reviewer` | 多视角同行评审：5 名独立 reviewer（EIC + 3 peer + Devil's Advocate），含 0-100 评分 rubrics、复审验证、Socratic 引导、calibration 模式。 | 论文同行评审、方法论聚焦审查、re-review、reviewer 校准。 |
| `academic-pipeline` | 10-stage 研究全流程编排：research → write → integrity check → review → revise → re-review → re-revise → final integrity → finalize。统一调度 deep-research / academic-paper / academic-paper-reviewer。 | 端到端论文工作流，含 Material Passport、claim 验证、可选 cross-model 完整性核查。 |
| `academic-research-legacy` | 早期单文件版本：文献检索、论文筛选、精读、引用核查和综述式总结（无 fabricated reference）。 | 已被上面 4 个 skill 取代，保留备查。 |
| `edit-article` | 改善文章结构、表达、逻辑和可读性。 | 修改论文段落、报告、说明文、引言、结论或长文草稿。 |
| `ieee-network-paper-writer` | 面向 IEEE/ACM 网络与系统论文的写作、修改和审查。 | 强化论点-证据对应、实验叙述、图表说明和 reproducibility。 |
| `moe-thesis-academic-polish` | 面向 MoE/ASTRA-sim 毕业论文的中文学术润色。 | 修改 MoE 工作负载仿真论文的背景、方法、实验和图注。 |
| `nature-data` | 生成 Nature 风格的数据可用性声明和 FAIR 元数据。 | 准备 Data Availability、数据引用和代码/数据开源说明。 |
| `nature-paper2ppt` | 从论文或 PDF 生成 Nature 风格中文 PPTX。 | 制作答辩、组会、论文汇报或投稿展示 PPT。 |
| `nature-polishing` | 将学术文本润色、重组或翻译为更接近 Nature 风格的英文。 | 修改摘要、引言、结果段、重要性陈述或 rebuttal。 |
| `thesis-aigc-revision` | 审查并降低中文论文中的 AI 味，同时保护 DOCX 格式。 | 处理空泛套话、重复表达、证据不足、引用缺失等问题。 |

### 图表、文档与 PPT

| Skill | 主要功能 | 典型用途 |
|---|---|---|
| `docx-format-guard` | 保护 Word/WPS 文档的样式、题注、交叉引用、表格和页面布局。 | 修改 `.docx` 时避免破坏编号、引用、题注和版式。 |
| `editable-ppt-builder` | 生成或修改可编辑 PPTX。 | 制作包含原生文本、形状、图标、表格和图表的演示文稿。 |
| `figure-pipeline` | 建立可复现的图表生产流程。 | 生成包含数据、脚本、PDF/SVG/PNG 和 manifest 的论文图表包。 |
| `gpt-image-2-workflow` | 使用 OpenAI `gpt-image-2` 生成视觉素材，并保留文字和布局可编辑性。 | 生成封面图、插画、背景图、示意素材或 PPT 视觉草图。 |
| `nature-figure` | 面向高水平期刊的多子图绘制、导出和质量检查流程。 | 制作投稿级科研图，检查配色、字号、线宽、版面和导出格式。 |

### 代码库理解、上下文与记忆

| Skill | 主要功能 | 典型用途 |
|---|---|---|
| `codewiki-repo-documentation` | 使用 CodeWiki 或类似工具生成代码库架构文档。 | 为大型仓库生成 onboarding wiki，并排除私有数据和生成产物。 |
| `context-economy` | 通过检索、索引、文件清单和压缩交接降低上下文成本。 | 处理大型代码库、长论文、多轮文档任务或长会话。 |
| `gitnexus-codebase-intelligence` | 使用 GitNexus、Repomix、Serena、Sourcebot 等工具理解大型代码库。 | 建立仓库索引、查询模块关系、生成结构摘要。 |
| `obsidian-vault` | 管理 Obsidian 笔记、wikilink 和索引笔记。 | 维护个人知识库、项目笔记、阅读记录和长期研究材料。 |
| `project-memory-handoff` | 保存跨机器、跨会话的项目交接信息。 | 记录当前决策、实验状态、后续任务和恢复路径。 |

### 工程开发流程

| Skill | 主要功能 | 典型用途 |
|---|---|---|
| `diagnose` | 按复现、最小化、假设、插桩、修复、回归测试的流程排查问题。 | 调试失败、性能退化、偶发 bug 或根因不清的问题。 |
| `git-guardrails-claude-code` | 配置 Claude Code hook，拦截危险 git 命令。 | 防止误删、误回滚和破坏工作区。 |
| `improve-codebase-architecture` | 基于领域文档和 ADR 寻找架构改进点。 | 审查模块边界、抽象层次、可维护性和重构机会。 |
| `karpathy-guidelines` | 应用简洁、可验证、不过度设计的编码准则。 | 减少 LLM 常见工程问题，强调可运行验证。 |
| `migrate-to-shoehorn` | 将 TypeScript 测试中的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。 | 清理依赖不安全 `as` cast 的类型测试代码。 |
| `pua` | Persistent Unblocking Assistant 工作流。 | 避免任务过早放弃、原地循环或无证据宣布完成。 |
| `setup-pre-commit` | 配置 Husky pre-commit hook、lint-staged、typecheck 和测试。 | 为 JavaScript/TypeScript 仓库增加本地提交前质量门禁。 |
| `tdd` | 测试驱动开发流程。 | 通过 red-green-refactor 新增功能或修复 bug。 |

### 规划、需求与 Issue 管理

| Skill | 主要功能 | 典型用途 |
|---|---|---|
| `grill-me` | 用高强度问题审视方案或设计。 | 在实施前暴露假设、风险和不清楚的边界。 |
| `grill-with-docs` | 基于已有领域文档挑战方案，并更新 CONTEXT/ADR。 | 让方案审查建立在项目文档和真实约束之上。 |
| `setup-matt-pocock-skills` | 配置 `AGENTS`/`CLAUDE` 和 `docs/agents`。 | 建立适合 agent 协作的问题管理和上下文结构。 |
| `to-issues` | 将计划、PRD 或规格拆成可独立领取的 issue。 | 把路线图拆成明确、可执行、可分配的开发任务。 |
| `to-prd` | 将讨论内容整理成 PRD。 | 沉淀需求、验收标准和范围边界。 |
| `triage` | 用状态机和角色分工流程整理 issue。 | 对问题池进行分类、澄清、排优先级和进入实现。 |
| `zoom-out` | 从细节中抽离，重新整理背景、方向、风险和决策点。 | 会话过细或过乱时恢复全局视角。 |

### Skill 与仓库工具

| Skill | 主要功能 | 典型用途 |
|---|---|---|
| `caveman` | 极简回复模式，在保证技术准确的前提下降低 token 消耗。 | 需要非常短、直接、低 token 的回复风格。 |
| `codex-performance-maintenance` | 排查和缓解 Codex 桌面端卡顿。 | 处理大 session、日志、缓存、旧进程或工作区导致的性能问题。 |
| `scaffold-exercises` | 创建练习目录结构。 | 搭建课程、教程或训练题库，包含章节、题目、答案和讲解。 |
| `write-a-skill` | 创建新的 agent skill。 | 为工具箱新增结构完整、可复用的工作流。 |

## 维护约定

- 不提交私有完整论文、原始数据集、本地报告或大型实验产物。
- 图表和导出物应尽量保留源文件，例如 `.drawio`、绘图脚本、CSV/NPZ 数据和 PPTX 原始文件。
- 优先保存可编辑、可复现的材料，避免只保留截图。
- 项目专属规则放入对应项目的 profile，不写入通用工具箱。
- 新增 skill 时，应同时补充用途说明、触发条件和必要示例。

## 更新方式

```powershell
git pull --ff-only
git status -sb
```
