# Project Profiles

Profiles store project-specific rules that should not be baked into the shared
tool kit.

Use `project_profile_template.md` as the starting point for each project.

Recommended naming:

```text
profiles/
  project_name.profile.md
```

Do not commit private paths, account details, or sensitive project content to a
public profile. Keep those in the target project's local `AGENTS.md` or private
handoff notes.

## Shared behavioral profiles

`karpathy-guidelines.md` — Karpathy LLM coding 行为守则（4 节：Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution）。来源 `https://github.com/forrestchang/andrej-karpathy-skills` 仓库根目录的 `CLAUDE.md`。在 Claude Code 项目里用 `@karpathy-guidelines.md` import；Codex 侧已落到 `~/.codex/memories/karpathy-guidelines.md`。同正文也作为 `skills/karpathy-guidelines/SKILL.md` 提供按需加载形态。

