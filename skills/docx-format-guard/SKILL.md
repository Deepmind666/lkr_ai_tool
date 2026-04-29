---
name: docx-format-guard
description: Guard important DOCX/WPS/Word documents by preserving formatting, references, tables, fields, and user-edited layout during edits.
---

# DOCX Format Guard

Use this skill before and after editing important DOCX files.

## Workflow

1. Identify the latest source DOCX.
2. Copy it to a new named output file before major edits.
3. Inspect existing formatting before editing:
   - highlights,
   - comments,
   - fields and cross-references,
   - bookmarks and hyperlinks,
   - reference lists,
   - tables,
   - figure captions,
   - manually adjusted sections.
4. Edit only the requested scope.
5. Verify after editing:
   - DOCX package opens as a zip,
   - core Word XML parts exist,
   - fields or hyperlinks were not flattened unexpectedly,
   - table indentation and alignment did not drift,
   - important captions and references still render correctly.

## Rules

- Never overwrite the user's only working copy.
- Preserve manually adjusted formatting unless a concrete error is verified.
- Do not convert formal cross-references to plain text when jumpable references
  are required.
- Check hidden paragraph/run properties when text appears visually wrong.
- Do not use Word/WPS automation for slow whole-document loops unless necessary.

