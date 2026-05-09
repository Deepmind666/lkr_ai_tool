# lkr_ai_tool

`lkr_ai_tool` 是一个可迁移的 AI 工作台，主要用于论文写作、Word 文档编辑、可编辑 PPT 制作、论文图表生成、项目记忆、代码库理解和跨机器交接。

这个仓库刻意保持项目中立。具体项目的规则应该放在项目自己的 `AGENTS.md`、profile 或本地说明文件里；本仓库只保存可复用的方法、模板、脚本、skill 和工具选择。

## GitHub

仓库地址：<https://github.com/Deepmind666/lkr_ai_tool>

克隆命令：

```powershell
git clone https://github.com/Deepmind666/lkr_ai_tool.git
```

## 这个仓库用来做什么

- 让新的 GPT、Codex、Claude 或其它 agent 快速理解你的常用工作方式。
- 保存可复用的论文写作、图表绘制、PPT 制作、文档排版和代码理解流程。
- 把本地文档工作和服务器端代码、实验工作区分开，避免互相污染。
- 尽量保留可编辑源文件，而不是只保存截图或不可编辑图片。
- 记录工具选择和操作规范，方便以后迁移到另一台电脑或另一个 agent。

## 推荐目录结构

```text
lkr_ai_tool/
  AGENTS.md
  config/
  docs/
  profiles/
  scripts/
  skills/
  templates/
```

## 建议优先阅读

1. `docs/usage_for_other_gpts.md`
2. `docs/migration_playbook.md`
3. `docs/tool_catalog.md`
4. `docs/token_saving_and_context_indexing.md`
5. `docs/editable_ppt_workflow.md`
6. `docs/gpt_image_2_tips.md`
7. `docs/local_experience.md`
8. `docs/codewiki_playbook.md`，用于生成代码库 wiki 或架构文档。

## 当前定位

这个工具箱重点服务以下场景：

- DOCX/WPS/Word 格式安全编辑。
- 可编辑 PPTX 的生成和修改。
- 学术论文图表、流程图和示意图生成。
- 把 AI 生成图片作为视觉素材，而不是替代可编辑幻灯片。
- 为其它 coding GPT 或服务器 agent 打包代码库上下文。
- 可选使用 CodeWiki 风格工具生成代码库 onboarding wiki。
- 通过 MCP、搜索、索引和文件清单减少 token 消耗。

## Skill 目录

`skills/` 下面的每个目录都是一个可独立调用的 agent skill。下面按用途说明每个 skill 的主要功能和适用场景。

### 写作、论文与文献研究

| Skill | 主要功能 | 适用场景 |
|---|---|---|
| `academic-research` | 做文献检索、论文筛选、精读、引用核查和综述式总结，避免编造文献。 | 查论文、比较 related work、从 PDF 中提取证据、准备 BibTeX 或引用依据。 |
| `edit-article` | 修改文章结构、表达、逻辑和可读性，同时保留作者原意。 | 修改论文段落、报告、说明文、引言、结论或长文草稿。 |
| `ieee-network-paper-writer` | 按 IEEE/ACM 网络与系统论文风格写作、修改和审查，强调论点-证据对应和可复现性。 | 写系统/网络论文、审查实验叙述、修改图表说明、准备 rebuttal 或技术定位。 |
| `moe-thesis-academic-polish` | 面向 MoE/ASTRA-sim 毕业论文的中文学术润色，突出输入链路、仿真链路和低 AIGC 表达。 | 修改 MoE 工作负载仿真论文的背景、方法、实验、图注和结论。 |
| `nature-data` | 生成 Nature 风格的数据可用性声明、仓库发布计划、数据引用和 FAIR 元数据。 | 准备 Data Availability、代码/数据开源说明或投稿材料。 |
| `nature-paper2ppt` | 从论文、预印本或 PDF 生成 Nature 风格中文 PPTX，包含精选图表和讲稿。 | 把论文快速转成答辩、组会或汇报 PPT。 |
| `nature-polishing` | 将学术文本润色、重组或翻译成更接近 Nature 系列的简洁英文。 | 修改摘要、重要性陈述、引言、结果段或 rebuttal 英文。 |
| `thesis-aigc-revision` | 审查并降低中文论文中的 AI 味，补充具体对象、证据和引用，同时保护 DOCX 格式。 | 检查空泛套话、重复转折、证据不足、引用缺失和 DOCX 安全修改。 |

### 图表、文档与 PPT

| Skill | 主要功能 | 适用场景 |
|---|---|---|
| `docx-format-guard` | 保护 Word/WPS 文档的样式、题注、交叉引用、表格、域和页面布局。 | 修改 `.docx` 时必须保证格式、编号、图表题注和引用不被破坏。 |
| `editable-ppt-builder` | 生成或修改可编辑 PPTX，优先使用原生文本、形状、图标、表格和图表。 | 制作答辩 PPT、汇报 PPT、论文展示 PPT，且后续还要手动编辑。 |
| `figure-pipeline` | 建立可复现图表流程，保留数据、脚本、导出文件和 manifest。 | 为论文生成 PDF/SVG/PNG 图表包，并保证能从 CSV/NPZ 一键重画。 |
| `gpt-image-2-workflow` | 使用 OpenAI `gpt-image-2` 生成文档或 PPT 视觉素材，同时保持文字和布局可编辑。 | 生成封面图、插画、背景图、示意素材或视觉草图。 |
| `nature-figure` | 面向 Nature/高水平期刊的多子图绘制流程，包含 Python/R 绘图、导出和 QA。 | 制作投稿级多面板科研图、审查配色/字号/版面、导出高质量矢量图。 |

### 代码库理解、上下文与记忆

| Skill | 主要功能 | 适用场景 |
|---|---|---|
| `codewiki-repo-documentation` | 使用 CodeWiki 或类似工具生成代码库架构文档和 onboarding wiki。 | 给大型仓库生成结构说明，同时排除私有数据、实验产物和生成文件。 |
| `context-economy` | 通过检索、索引、文件清单和压缩交接降低 token 消耗。 | 处理大型代码库、长论文、多轮文档任务或上下文成本过高的任务。 |
| `gitnexus-codebase-intelligence` | 用 GitNexus、Repomix、Serena、Sourcebot 等工具索引、查询和总结大型代码库。 | 不想把大量源码直接塞进对话，但又需要准确理解仓库结构。 |
| `obsidian-vault` | 搜索、创建和管理 Obsidian 笔记，支持 wikilink 和索引笔记。 | 管理个人知识库、项目笔记、阅读记录或长期研究材料。 |
| `project-memory-handoff` | 维护可跨机器、跨 agent 复用的项目交接记忆。 | 保存当前决策、实验状态、下一步计划、恢复信息和长期上下文。 |

### 工程开发流程

| Skill | 主要功能 | 适用场景 |
|---|---|---|
| `diagnose` | 按复现、最小化、假设、插桩、修复、回归测试的流程排查问题。 | 调试失败、性能退化、偶发 bug 或根因不清的问题。 |
| `git-guardrails-claude-code` | 配置 Claude Code hook，拦截危险 git 命令，保护工作区。 | 搭建更安全的 AI agent 编码环境，防止误删或误回滚。 |
| `improve-codebase-architecture` | 基于领域文档和 ADR 查找代码架构改进点。 | 审查模块边界、抽象层次、可维护性和重构机会。 |
| `karpathy-guidelines` | 应用简洁、可验证、不过度设计的编码准则，减少 LLM 常见工程问题。 | 实现或审查代码时，需要避免复杂化并强调测试验证。 |
| `migrate-to-shoehorn` | 将 TypeScript 测试中的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。 | 清理依赖不安全 `as` cast 的类型测试代码。 |
| `pua` | Persistent Unblocking Assistant 工作流，避免 agent 过早放弃、原地循环或无证据宣布完成。 | 处理困难任务，需要持续推进、明确阻塞点并给出进展证据。 |
| `setup-pre-commit` | 配置 Husky pre-commit hook，接入 lint-staged、typecheck 和测试。 | 给 JavaScript/TypeScript 仓库增加本地提交前质量门禁。 |
| `tdd` | 按 red-green-refactor 的测试驱动开发流程工作。 | 新增功能或修复 bug 时，希望先用测试定义行为。 |

### 规划、需求与 Issue 管理

| Skill | 主要功能 | 适用场景 |
|---|---|---|
| `grill-me` | 用尖锐问题压力测试方案或设计，逼清楚关键假设。 | 实施前想让计划被认真质疑，避免盲区。 |
| `grill-with-docs` | 基于已有领域文档挑战方案，并把结论更新到 CONTEXT/ADR。 | 希望批判来自项目文档和真实约束，而不是泛泛而谈。 |
| `setup-matt-pocock-skills` | 配置 `AGENTS`/`CLAUDE` 和 `docs/agents`，支持 issue tracker、triage 和领域上下文工作流。 | 为仓库建立更适合 agent 协作的问题管理和上下文结构。 |
| `to-issues` | 把计划、PRD 或规格拆成可独立领取的 issue。 | 将路线图拆成明确、可执行、可分配的开发任务。 |
| `to-prd` | 把当前对话上下文整理成 PRD，并发布到 issue tracker。 | 从讨论中沉淀需求、验收标准和范围边界。 |
| `triage` | 用状态机和角色分工流程整理 issue。 | 对问题池进行分类、澄清、排优先级和进入实现。 |
| `zoom-out` | 强制 agent 跳出细节，给出更高层的背景、方向、风险和决策点。 | 当前会话过细、过乱，需要重新建立全局视角。 |

### Skill 与仓库工具

| Skill | 主要功能 | 适用场景 |
|---|---|---|
| `caveman` | 极简短回复模式，在保证技术准确的前提下尽量节省 token。 | 只需要非常短、直接、低 token 的 agent 回复。 |
| `codex-performance-maintenance` | 排查并降低 Codex 桌面端卡顿，包括大 session、日志、缓存、旧进程和工作区问题。 | Codex 打开、输入、渲染、滚动或本地检查变慢。 |
| `scaffold-exercises` | 创建练习目录结构，包含章节、题目、答案和讲解。 | 搭建课程、教程或训练题库。 |
| `write-a-skill` | 创建新的 agent skill，并保证结构、渐进披露、资源和示例完整。 | 给这个工具箱新增可复用工作流。 |

## 仓库规则

- 不要提交私有完整论文、原始数据集、本地报告或大型生成实验产物。
- 图表和导出物要尽量保留源文件，例如 `.drawio` 配 `.svg`/`.png`，绘图脚本配生成图片，PPTX 配套使用到的图片。
- 优先保存可编辑、可复现的源文件，不要只保存截图。
- 项目专属规则应该放在对应 project profile，不要硬编码进这个通用工具箱。

## 项目 Profile

使用 `profiles/project_profile_template.md` 为每个项目创建一个简短 profile。profile 应记录文件安全规则、推荐工具、源数据位置和项目专属格式要求。

## GitHub 远端

当前远端：<https://github.com/Deepmind666/lkr_ai_tool.git>

推荐更新流程：

```powershell
git pull --ff-only
git status -sb
```
