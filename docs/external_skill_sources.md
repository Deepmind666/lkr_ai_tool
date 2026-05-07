# External Skill Sources

Reviewed on 2026-05-05. License notes added 2026-05-06.

This repo now keeps local copies of selected third-party agent skills so the
same workflow can be restored on a new Claude Code or Codex machine without
re-discovering the source repos.

## Installed Sources

| Source | License | Installed skill paths | Notes |
| --- | --- | --- | --- |
| https://github.com/forrestchang/andrej-karpathy-skills | Repo has no top-level LICENSE; the upstream `SKILL.md` declares `license: MIT` in its frontmatter, which we preserve verbatim in the mirrored copy. | `skills/karpathy-guidelines` | The user-provided singular URL `forrestchang/andrej-karpathy-skill` returned 404; the active repo is plural. The same body is also mirrored to `profiles/karpathy-guidelines.md` so it can be `@`-imported into a `CLAUDE.md`. |
| https://github.com/mattpocock/skills | MIT | `skills/diagnose`, `skills/grill-with-docs`, `skills/improve-codebase-architecture`, `skills/setup-matt-pocock-skills`, `skills/tdd`, `skills/to-issues`, `skills/to-prd`, `skills/triage`, `skills/zoom-out`, `skills/git-guardrails-claude-code`, `skills/migrate-to-shoehorn`, `skills/scaffold-exercises`, `skills/setup-pre-commit`, `skills/edit-article`, `skills/obsidian-vault`, `skills/caveman`, `skills/grill-me`, `skills/write-a-skill` | Installed the current non-deprecated skills from the repo. Deprecated skills were intentionally skipped. |

## Local Agent Targets

The same set was installed to:

- `C:\Users\deepmind666\.codex\skills`
- `C:\Users\deepmind666\.claude\skills`
- `D:\毕业论文\毕业论文\lkr_ai_tool\skills`

No `C:\Users\deepmind666\.cortex` directory was present on 2026-05-05. In this
setup note, "cortex" is treated as the local Codex configuration unless the user
later confirms a separate Cortex tool directory.

## Usage Notes

- Restart Codex and Claude Code after installing or updating skills.
- For coding tasks, load `karpathy-guidelines` when the work risks hidden
  assumptions, overengineering, broad edits, or vague success criteria.
- For Matt Pocock engineering workflows, run `setup-matt-pocock-skills` once per
  code repo before relying on `to-issues`, `to-prd`, `triage`, `diagnose`,
  `tdd`, `improve-codebase-architecture`, or `zoom-out`.
- Treat external skills as reusable workflow assets. Project-specific thesis
  rules still belong in the target project's `AGENTS.md` or private memory.
