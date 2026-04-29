# lkr_ai_tool

Portable AI workbench for document editing, editable slides, figures, diagrams,
project memory, and code-context handoff across machines.

This repository is intentionally project-neutral. Put project-specific rules in a
profile or local `AGENTS.md`, then let this repo carry the reusable methods,
templates, and tool choices.

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
4. `docs/editable_ppt_workflow.md`
5. `docs/gpt_image_2_tips.md`
6. `docs/local_experience.md`

## Current Bias

This kit is optimized for:

- DOCX/WPS/Word formatting safety.
- Editable PPTX generation and revision.
- Research-style charts and diagrams.
- AI image generation as a visual asset source, not as a substitute for
  editable slides.
- Codebase context packaging for another coding GPT or server agent.

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

Planned remote:

```text
https://github.com/Deepmind666/lkr_ai_tool.git
```

After local files are ready, initialize and push with:

```powershell
git init
git branch -M main
git remote add origin https://github.com/Deepmind666/lkr_ai_tool.git
git add .
git commit -m "Initialize lkr_ai_tool workbench"
git push -u origin main
```
