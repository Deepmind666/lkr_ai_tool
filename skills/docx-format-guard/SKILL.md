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
- Table cells must never contain leading spaces, full-width spaces, tabs, non-breaking spaces, first-line indents, left indents, hanging indents, or inherited body indentation. Before delivering any edited DOCX, clean and verify all table cells, even if the current request was mainly textual.
- Do not rely only on literal text scans. WPS/Word may render inherited paragraph-style indentation inside table cells even when the cell text has no leading spaces and no direct `w:ind`. If a cell can inherit body first-line indentation, explicitly override it with zero left/right/firstLine/hanging indentation for every table-cell paragraph.
- Table delivery gate: literal leading whitespace must be zero, nonzero table-cell indentation must be zero, inherited indentation must be explicitly overridden with zero `w:ind`, all table-cell paragraphs must be horizontally centered, and all cells must be vertically centered. If the user reports visible "空两格", treat it as a blocker even when literal-space checks pass.
- Reference delivery gate: bibliography entries must follow first appearance order in the main text. The unique citation sequence before the bibliography must be `[1], [2], ... [N]`, and the bibliography must contain exactly `N` numbered entries unless appendices explicitly cite additional sources.
- Do not add a GitHub repository as a separate bibliography entry when the same tool/system already has a formal paper, arXiv preprint, proceedings paper, or technical report cited in the thesis. Keep the paper citation and remove the repository entry, unless the text explicitly cites implementation details that are unavailable in the paper. Examples: cite the AIConfigurator arXiv paper instead of the AIConfigurator GitHub repository; cite the AICB paper instead of the AICB GitHub repository.
- Jumpability is mandatory, not optional. Figure/table/equation `REF` fields must include the `\h` switch or an equivalent internal hyperlink. Bibliography citations such as `[1]` must be superscript and must link to the matching bibliography entry bookmark, for example `[10]` -> `BibRef010`. Final checks must report `citation_hyperlink_missing=0`, `citation_bad_anchor=0`, and `citation_not_superscript=0`.

