---
name: codewiki-repo-documentation
description: Use CodeWiki or similar AI wiki generators to create scoped repository architecture documentation, onboarding maps, and codebase handoff notes while excluding private data, generated artifacts, and caches.
---

# CodeWiki Repo Documentation

Use this skill when the user asks to evaluate, configure, or run CodeWiki for a
repository. CodeWiki is for durable architecture documentation, not routine
small edits.

## Decision Rule

Use CodeWiki when the task needs an onboarding wiki, architecture map, or module
guide for a medium or large repo. Do not use it for a narrow code question that
`rg`, direct file reads, GitNexus, Serena, or Repomix can answer faster.

## Required Guardrails

Before running CodeWiki:

1. Confirm the target path is one Git repository or a small source-only subset.
2. Exclude data, caches, generated outputs, model weights, archives, logs, and
   secrets.
3. Record the source commit, command, model/provider, and output path.
4. Verify any important CodeWiki claim by reading the source file directly.

Read `docs/codewiki_playbook.md` for the exclusion list and workflow.

## Output Contract

If committing CodeWiki output, include:

- a short README with the command and source commit;
- generated wiki pages under a project-local docs folder;
- no raw datasets, experiment dumps, `.npz`, `.et`, model weights, cache files,
  or private drafts.

For active coding work, prefer keeping generated wiki output untracked and use
it only as navigation.
