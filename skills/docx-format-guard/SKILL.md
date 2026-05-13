---
name: docx-format-guard
description: Guard important DOCX/WPS/Word documents by preserving formatting, references, tables, algorithms, fields, and user-edited layout during edits.
---

# DOCX Format Guard

Use this skill before and after editing important DOCX files, especially thesis documents that already contain manually adjusted Word/WPS formatting.

## Workflow

1. Identify the latest source DOCX.
2. Copy it to a new named output file before major edits.
3. Inspect existing formatting before editing:
   - highlights and comments;
   - REF fields, bookmarks, hyperlinks, and cross-references;
   - reference list numbering;
   - ordinary tables, symbol tables, and algorithm/pseudocode tables;
   - figure captions and image anchors;
   - manually adjusted cover, abstract, TOC, algorithms, and front matter.
4. Classify the object before applying a global fix. Do not treat every table as the same kind of table.
5. Edit only the requested scope.
6. Verify after editing:
   - DOCX package opens as a zip;
   - core Word XML parts exist;
   - fields or hyperlinks were not flattened unexpectedly;
   - ordinary table indentation/alignment did not drift;
   - algorithm formatting was not normalized as an ordinary centered table;
   - important captions and references still render correctly.

## Rules

- Never overwrite the user's only working copy.
- Preserve manually adjusted formatting unless a concrete error is verified.
- Do not convert formal cross-references to plain text when jumpable references are required.
- Check hidden paragraph/run properties when text appears visually wrong.
- Do not use Word/WPS automation for slow whole-document loops unless necessary.

## References

- Bibliography entries must follow first appearance order in the main text unless the user explicitly freezes a different order.
- Do not add a GitHub repository as a separate bibliography entry when the same tool/system already has a formal paper, arXiv preprint, proceedings paper, or technical report cited in the thesis.
- The GitHub de-duplication rule must not be used to delete unrelated references. Before delivering any bibliography edit, diff the bibliography against the previous working version. Preserve non-duplicate papers, reports, surveys, web pages, and repositories unless the user explicitly approves deletion.
- Jumpability is mandatory. Figure/table/equation `REF` fields must include the `\h` switch or equivalent internal hyperlink.
- Bibliography citations such as `[1]` must be superscript and must link to the matching bibliography entry bookmark, for example `[10]` -> `BibRef010`.
- Final citation checks must report `citation_hyperlink_missing=0`, `citation_bad_anchor=0`, and `citation_not_superscript=0`, or explicitly list every remaining exception.

## Fonts

- Chinese body text should preserve the thesis template, normally Songti for body and Heiti for headings.
- English letters and Arabic numerals in the body, captions, references, and ordinary tables must explicitly use Times New Roman unless the user's current template gives a more specific exception.
- Final font checks should report `latin_font_not_TNR=0` for the edited scope, or explain each deliberate exception.

## Ordinary Tables

Ordinary tables include comparison tables, result tables, ablation tables, symbol explanation tables, and configuration tables.

- Table cells must not contain leading half-width spaces, full-width spaces, tabs, non-breaking spaces, first-line indents, left indents, hanging indents, or inherited body indentation.
- Do not rely only on literal text scans. WPS/Word may render inherited paragraph-style indentation inside table cells even when the cell text has no leading spaces and no direct `w:ind`.
- For ordinary table-cell paragraphs, explicitly override indentation with zero `w:ind` values.
- Ordinary table cells should be horizontally centered and vertically centered unless the user's current table style deliberately uses a different alignment.
- Ordinary thesis tables should use the required table font and size, commonly five-point Chinese text with Times New Roman for English/numbers.
- Ordinary table checks must report:
  - `ordinary_table_leading_cells=0`
  - `ordinary_table_cell_indents=0`
  - `ordinary_table_non_center_paras=0`
  - `ordinary_table_non_center_vAlign=0`
  - `ordinary_table_bad_size=0`
  - `ordinary_table_bad_latin_font=0`

## Algorithm Tables

Algorithm tables are not ordinary data tables. They often contain pseudocode, input/output declarations, stages, line numbers, comments, and code-like expressions.

- Never run a whole-document "center every table paragraph" fix without excluding algorithm/pseudocode tables.
- If a table caption starts with "算法" or the table contains algorithm markers such as "输入", "输出", "阶段", "for", "while", "if", "else", "return", line numbers, or code-like statements, audit it as an algorithm table first.
- Do not force algorithm bodies, pseudocode lines, input/output lines, phase labels, or line-number columns to horizontal center.
- Preserve or restore the user's algorithm style:
  - title/caption handled separately;
  - input/output and pseudocode body left aligned or in the user's existing alignment;
  - line numbers stable and readable;
  - no extra cell leading spaces;
  - no accidental body-text first-line indent;
  - top/bottom rules consistent with surrounding algorithm blocks.
- Algorithm tables may keep mixed alignment: line numbers can be centered, pseudocode can be left aligned, and headers can follow the user's existing style.
- Algorithm font hierarchy should be preserved. Do not shrink, center, or normalize algorithms through ordinary-table scripts.
- Algorithm checks must be reported separately from ordinary table checks. Do not claim `non_center_paras=0` as success if that number was obtained by incorrectly centering algorithm pseudocode.

## Delivery Gate

Before delivering any edited DOCX, run separate audits for:

- package validity;
- citation superscript and jumpability;
- Latin font assignment;
- ordinary table indentation/alignment/font;
- algorithm-table indentation/alignment/font;
- figure/table captions;
- highlights and comments if the task touches review marks.

If any gate is not zero or intentionally skipped, say so in the final answer.
