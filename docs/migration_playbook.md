# Migration Playbook

This playbook moves the same AI-assisted workflow to another computer, another
project, or another GPT/agent session.

## What Belongs In This Public Repo

Keep:

- reusable skills,
- tool reviews,
- templates,
- scripts that inspect or validate files,
- workflow notes,
- generic project profiles.

Do not keep:

- private DOCX/PPTX drafts,
- raw datasets,
- generated experiment dumps,
- account tokens,
- private reports,
- WPS/Word temporary files,
- copied third-party paid assets.

## Minimal Setup On A New Machine

1. Clone `https://github.com/Deepmind666/lkr_ai_tool.git`.
2. Read `docs/usage_for_other_gpts.md`.
3. Copy the relevant files from `skills/` into the local agent skill directory
   if the agent supports local skills.
4. Create or copy a project-specific `AGENTS.md` in the target project.
5. Create a fresh `templates/session_memory.md` entry before major work starts.
6. Install only the tools needed for that machine's role.

## Machine Roles

### Local Document Machine

Primary work:

- DOCX/WPS/Word editing.
- OpenXML structural checks.
- Editable PPTX creation and revision.
- draw.io, D2, or Mermaid diagram drafting.
- Chart styling and final figure export.

Recommended tools:

- Word or WPS.
- draw.io desktop.
- D2 or Mermaid CLI.
- Python with `matplotlib`, `SciencePlots`, `pandas`, and `numpy`.
- Optional: marimo for figure notebooks.
- Optional: PptxGenJS, python-pptx, pptx-automizer, or ppt-master for editable
  slide generation.

### Server / Code / Experiment Machine

Primary work:

- code editing,
- experiment execution,
- large result generation,
- AI-ready codebase handoff,
- chart data export.

Recommended tools:

- GitNexus or Serena for code graph and semantic navigation.
- Repomix for compact repo snapshots.
- Aider, Cline, or Roo Code for coding workflows.
- Sourcebot if the codebase becomes large.
- marimo or plain Python scripts for reproducible analysis.

## Data And Figure Handoff Contract

Use a directory like:

```text
results/
  YYYYMMDD_project_task/
    data/
      *.csv
      *.json
    plots/
      *.svg
      *.png
    sources/
      *.py
      *.ipynb
      *.mmd
      *.d2
      *.drawio
    manifest.json
    README.md
```

Every `manifest.json` should record:

- date,
- machine,
- project,
- source repo and commit,
- command or script used,
- input data path,
- generated output path,
- model or dataset if relevant,
- random seed if relevant,
- whether the numbers are measured, simulated, estimated, or illustrative.

## Handoff To Another GPT

Give the next GPT:

- the target project `AGENTS.md`,
- `docs/usage_for_other_gpts.md`,
- latest `templates/session_memory.md` entry,
- exact file paths,
- exact source data or figure directory,
- one concrete task,
- known risks and things it must not touch.

Do not ask a new GPT to infer project rules from a long chat transcript. Give it
the rules and the current state as files.

