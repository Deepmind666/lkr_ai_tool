# lkr_ai_tool

Portable AI workbench for document editing, editable slides, figures, diagrams,
project memory, and code-context handoff across machines.

This repository is intentionally project-neutral. Put project-specific rules in a
profile or local `AGENTS.md`, then let this repo carry the reusable methods,
templates, and tool choices.

## GitHub

Repository: <https://github.com/Deepmind666/lkr_ai_tool>

Clone it with:

```powershell
git clone https://github.com/Deepmind666/lkr_ai_tool.git
```

## What This Repo Is For

- Give a new GPT/agent enough context to work without re-learning your habits.
- Keep document, figure, PPT, and experiment handoffs reproducible.
- Separate local document work from server-side code and experiment work.
- Preserve editable sources instead of only storing screenshots or flattened
  images.
- Record tool decisions so the stack can migrate to another computer.

## Recommended Layout

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

## First Things To Read

1. `docs/usage_for_other_gpts.md`
2. `docs/migration_playbook.md`
3. `docs/tool_catalog.md`
4. `docs/token_saving_and_context_indexing.md`
5. `docs/editable_ppt_workflow.md`
6. `docs/gpt_image_2_tips.md`
7. `docs/local_experience.md`
8. `docs/codewiki_playbook.md` when generating a repository wiki.

## Current Bias

This kit is optimized for:

- DOCX/WPS/Word formatting safety.
- Editable PPTX generation and revision.
- Research-style charts and diagrams.
- AI image generation as a visual asset source, not as a substitute for
  editable slides.
- Codebase context packaging for another coding GPT or server agent.
- Optional CodeWiki-style repository wiki generation for source-only onboarding
  snapshots.
- Token-efficient codebase retrieval through MCP/search before broad file reads.

## Skill Catalog

Each directory under `skills/` is a standalone agent skill. This catalog explains the main purpose of every skill in the repository.

### Writing, Thesis, And Research

| Skill | Main function | Use when |
|---|---|---|
| `academic-research` | Literature search, paper triage, focused reading, citation hygiene, and review-style synthesis without fabricated references. | Looking up papers, comparing related work, extracting claims from PDFs, or preparing BibTeX/citation evidence. |
| `edit-article` | Revises article drafts for structure, clarity, flow, and readability while preserving the author's intended meaning. | Improving essays, reports, sections, introductions, conclusions, or long-form prose. |
| `ieee-network-paper-writer` | Writes, revises, and reviews IEEE/ACM networking manuscripts with claim-evidence discipline and reproducibility checks. | Preparing systems/networking paper sections, reviewer responses, figure/table audits, or technical positioning. |
| `moe-thesis-academic-polish` | Polishes Chinese MoE/ASTRA-sim thesis drafts around the input-chain logic with low-AIGC academic prose. | Revising the MoE workload simulation thesis, especially background, methodology, experiments, and figure captions. |
| `nature-data` | Produces Nature-ready data availability statements, repository plans, dataset citations, and FAIR metadata. | Preparing Data Availability, code/data release notes, or journal submission data statements. |
| `nature-paper2ppt` | Converts a paper, preprint, or PDF into a Nature-style Chinese PPTX with selected figures and speaker notes. | Making academic presentation decks from a manuscript or preprint. |
| `nature-polishing` | Polishes, restructures, or translates academic prose into concise Nature-leaning English. | Improving high-impact journal style, abstracts, significance statements, or rebuttal language. |
| `thesis-aigc-revision` | Audits and revises Chinese thesis prose to reduce generic AI-like writing while preserving DOCX formatting. | Checking for empty slogans, weak grounding, repeated transitions, missing citations, and DOCX-safe revisions. |

### Figures, Documents, And Presentations

| Skill | Main function | Use when |
|---|---|---|
| `docx-format-guard` | Protects Word/WPS document formatting, references, tables, fields, and layout during edits. | Editing `.docx` files where page layout, captions, references, or table formatting must not break. |
| `editable-ppt-builder` | Builds or revises editable PPTX decks with native text, shapes, icons, tables, charts, and assets. | Creating presentation slides that remain editable instead of flattened images. |
| `figure-pipeline` | Creates reproducible charts, diagrams, and manuscript figures with data, source, exports, and manifests. | Building paper figure packs where every figure must be reproducible from CSV/NPZ/scripts. |
| `gpt-image-2-workflow` | Uses OpenAI `gpt-image-2` for document/PPT visual assets while keeping labels and layout editable. | Generating bitmap illustrations, covers, or visual backgrounds for documents and slides. |
| `nature-figure` | Submission-grade high-impact journal figure workflow with Python/R plotting, export, and QA rules. | Making polished multi-panel scientific plots for Nature-style or top-tier manuscript figures. |

### Codebase Intelligence, Context, And Memory

| Skill | Main function | Use when |
|---|---|---|
| `codewiki-repo-documentation` | Uses CodeWiki or similar AI wiki generators to create scoped repository architecture documentation. | Building onboarding maps or codebase wiki pages while excluding private data and generated artifacts. |
| `context-economy` | Reduces token waste through retrieval, indexing, manifests, compact handoffs, and targeted file reads. | Working in large repos, long papers, repeated sessions, or any task where context size is becoming expensive. |
| `gitnexus-codebase-intelligence` | Indexes, queries, and summarizes large codebases with GitNexus, Repomix, Serena, Sourcebot, or similar tools. | Understanding large repositories without dumping too many files into the chat. |
| `obsidian-vault` | Searches, creates, and maintains Obsidian notes with wikilinks and index notes. | Managing personal or project knowledge in an Obsidian vault. |
| `project-memory-handoff` | Maintains portable handoff memory for project state across machines and agent sessions. | Saving current decisions, experiment state, next actions, and recovery notes for future sessions. |

### Engineering Workflow

| Skill | Main function | Use when |
|---|---|---|
| `diagnose` | Runs a disciplined debug loop: reproduce, minimize, hypothesize, instrument, fix, and regression-test. | Debugging failures, performance regressions, flaky behavior, or unclear root causes. |
| `git-guardrails-claude-code` | Configures Claude Code hooks to block dangerous git commands and protect the working tree. | Setting up safer AI-agent coding environments with git command guardrails. |
| `improve-codebase-architecture` | Finds refactoring and architecture-deepening opportunities using domain docs and ADRs. | Auditing a codebase for better module boundaries, abstractions, and maintainability. |
| `karpathy-guidelines` | Applies coding guardrails that avoid common LLM overengineering and require verification. | Implementing or reviewing code where simplicity, correctness, and tests matter. |
| `migrate-to-shoehorn` | Migrates TypeScript tests from `as` type assertions to `@total-typescript/shoehorn`. | Cleaning up type-test code that currently relies on unsafe `as` casts. |
| `pua` | Persistent Unblocking Assistant workflow that prevents giving up, looping, or claiming completion without evidence. | Handling hard tasks that require sustained execution, explicit blockers, and concrete proof of progress. |
| `setup-pre-commit` | Sets up Husky pre-commit hooks with lint-staged, typecheck, tests, and related checks. | Adding local quality gates to a JavaScript/TypeScript repository. |
| `tdd` | Test-driven development loop with red, green, refactor discipline. | Adding features or fixes where tests should define behavior before implementation. |

### Planning And Issue Management

| Skill | Main function | Use when |
|---|---|---|
| `grill-me` | Stress-tests a plan or design by asking hard questions until the assumptions are clear. | You want a plan challenged before implementation. |
| `grill-with-docs` | Challenges a plan against existing domain docs and updates CONTEXT/ADR notes inline. | You want critique grounded in project documentation, not generic opinions. |
| `setup-matt-pocock-skills` | Configures `AGENTS`/`CLAUDE` and `docs/agents` for issue tracker, triage, and domain context workflows. | Bootstrapping a repo for agent-friendly issue and context management. |
| `to-issues` | Breaks a plan, PRD, or specification into independently grabbable implementation issues. | Turning a roadmap into issue-sized units of work. |
| `to-prd` | Converts the current conversation context into a PRD and publishes it to an issue tracker. | Capturing requirements, acceptance criteria, and scope from a discussion. |
| `triage` | Triage issues through a state machine and role-based workflow. | Sorting and refining issue queues before implementation. |
| `zoom-out` | Forces a higher-level summary of context, direction, risks, and next decisions. | The session is too detailed and needs strategic orientation. |

### Skill And Repo Utilities

| Skill | Main function | Use when |
|---|---|---|
| `caveman` | Ultra-compressed terse communication mode that saves tokens while preserving technical accuracy. | You want very short, direct, low-token agent replies. |
| `codex-performance-maintenance` | Diagnoses and reduces Codex desktop slowness from large sessions, logs, caches, stale worktrees, or local processes. | Codex becomes slow to open, type, render, scroll, or run local checks. |
| `scaffold-exercises` | Creates exercise directory structures with sections, problems, solutions, and explainers. | Building course or tutorial exercise packs. |
| `write-a-skill` | Creates new agent skills with proper structure, progressive disclosure, resources, and examples. | Adding a new reusable workflow to this toolbox. |

## Repository Rules

- Do not commit private full drafts, raw datasets, local reports, or generated
  experiment dumps.
- Keep source files next to exports: `.drawio` with `.svg` or `.png`, chart
  scripts with generated plots, PPTX sources with any images used inside them.
- Prefer editable/native artifacts over screenshots.
- When a rule is project-specific, store it in that project profile rather than
  hard-coding it into the shared tool kit.

## Project Profiles

Use `profiles/project_profile_template.md` to create one small profile per
project. A profile should record file safety rules, preferred tools, source data
locations, and project-specific formatting constraints.

## GitHub Remote

Current remote: <https://github.com/Deepmind666/lkr_ai_tool.git>

Recommended update flow:

```powershell
git pull --ff-only
git status -sb
```
