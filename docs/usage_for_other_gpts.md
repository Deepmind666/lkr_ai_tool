# Instructions For Other GPT/Agent Sessions

This repository is a reusable workbench. It is not the project itself. Before
editing anything, identify the active project and load that project's rules.

## Start Here

1. Read the target project's `AGENTS.md` or equivalent rule file.
2. Read the latest session handoff note.
3. Identify the exact source file, output file, and requested scope.
4. Make the smallest useful change.
5. Verify the result with the checks appropriate to the file type.

## Non-Negotiable Habits

- Never overwrite the only working copy of a user document.
- Preserve manually adjusted formatting unless a concrete error is verified.
- Keep editable sources for figures, diagrams, and slides.
- Do not turn editable PPT content into one full-slide screenshot.
- Do not trust a tool summary when source files or tests can be inspected.
- Record skipped checks and why.
- Keep private documents, datasets, and reports out of public repos.

## For DOCX / WPS / Word Work

- Copy the source file to a named output file before large edits.
- Inspect highlights, comments, fields, bookmarks, references, tables, and styles
  before rewriting.
- Use structural checks after editing.
- If a document has formal cross-references, preserve them as fields or links
  rather than plain text.
- If a table has custom formatting, inspect current XML/visual state before
  touching it.

## For PPT Work

- Build slides from editable text boxes, shapes, icons, charts, and images.
- Use generated images as backgrounds or visual assets, not as flattened slides.
- Keep the source prompt, raw image, edited image, and final PPTX together.
- Verify in PowerPoint or WPS that text and shapes remain editable.

## For Figures And Diagrams

- Keep raw data, script/source, exported SVG/PDF/PNG, and manifest together.
- Prefer vector exports for review and high-DPI PNG for office compatibility.
- Make chart labels editable in the chart source, not baked into a screenshot.
- Store `.drawio`, `.mmd`, or `.d2` next to exported images.

## For Code And Experiments

- Use code indexing tools only as navigation aids.
- For large repos, prefer Claude Context/Serena/GitNexus/Repomix or `rg`
  before broad file reads.
- Verify claims against source files and tests.
- Record repo commit, command, data path, and output path.
- Separate local document work from server-side experiment work.

## For Token Economy

- Start from the latest handoff note instead of asking the user to restate
  stable rules.
- Search first, then read small slices.
- Keep only final facts, paths, checks, and risks in memory.
- Do not paste long logs, whole source files, or long paper excerpts when a
  path plus summary is enough.

## Session Closeout

Before ending, update a handoff note with:

- files changed,
- checks passed,
- checks skipped,
- unresolved risks,
- next concrete task.
