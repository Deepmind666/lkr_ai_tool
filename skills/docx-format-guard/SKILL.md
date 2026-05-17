---
name: docx-format-guard
description: Guard important DOCX/WPS/Word documents by preserving formatting, references, tables, algorithms, formulas, fields, and user-edited layout during edits.
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
   - formula objects and equation numbers;
   - figure captions and image anchors;
   - manually adjusted cover, abstract, TOC, algorithms, and front matter.
4. Classify the object before applying a global fix. Do not treat every table as the same kind of table.
5. Edit only the requested scope.
6. Verify after editing:
   - DOCX package opens as a zip;
   - core Word XML parts exist;
   - fields or hyperlinks were not flattened unexpectedly;
   - formulas did not become raw text or broken REF output;
   - ordinary table indentation/alignment did not drift;
   - algorithm formatting was not normalized as an ordinary centered table;
   - important captions and references still render correctly.

## General Rules

- Never overwrite the user's only working copy.
- Preserve manually adjusted formatting unless a concrete error is verified.
- Do not convert formal cross-references to plain text when jumpable references are required.
- Check hidden paragraph/run properties when text appears visually wrong.
- Do not use Word/WPS automation for slow whole-document loops unless necessary.
- Always render or export to PDF and inspect the pages visually when formulas, figures, tables, algorithms, captions, or page breaks are touched.

## References

- Bibliography entries should follow first appearance order in the main text unless the user explicitly freezes a different order.
- Do not add a GitHub repository as a separate bibliography entry when the same tool/system already has a formal paper, arXiv preprint, proceedings paper, or technical report cited in the thesis.
- The GitHub de-duplication rule must not be used to delete unrelated references. Before delivering any bibliography edit, diff the bibliography against the previous working version. Preserve non-duplicate papers, reports, surveys, web pages, and repositories unless the user explicitly approves deletion.
- Jumpability is mandatory. Figure/table/equation `REF` fields must include the `\h` switch or an equivalent internal hyperlink.
- Bibliography citations such as `[1]` must be superscript and must link to the matching bibliography entry bookmark, for example `[10]` -> `BibRef010`.
- WPS may encode citation links as field-code `HYPERLINK \l "BibRefNNN"` rather than `w:hyperlink`. Count both forms before claiming links are missing.
- Final citation checks must report `citation_hyperlink_missing=0`, `citation_bad_anchor=0`, and `citation_not_superscript=0`, or explicitly list every remaining exception.

## Fonts

- Chinese body text should preserve the thesis template, normally Songti for body and Heiti for headings.
- English letters and Arabic numerals in body text, captions, references, ordinary tables, and algorithm tables must explicitly use Times New Roman unless the user's current template gives a more specific exception.
- Final font checks should report `latin_font_not_TNR=0` for the edited scope, or explain each deliberate exception.

## Ordinary Tables

Ordinary tables include comparison tables, result tables, ablation tables, symbol explanation tables, and configuration tables.

- Table cells must not contain leading half-width spaces, full-width spaces, tabs, non-breaking spaces, first-line indents, left indents, hanging indents, or inherited body indentation.
- Do not rely only on literal text scans. WPS/Word may render inherited paragraph-style indentation inside table cells even when the cell text has no leading spaces and no direct `w:ind`.
- For ordinary table-cell paragraphs, explicitly override indentation with zero `w:ind` values.
- Ordinary table cells should be horizontally centered and vertically centered unless the user's current table style deliberately uses a different alignment.
- Ordinary thesis tables should use the required table font and size, commonly five-point Chinese text with Times New Roman for English/numbers.
- Remove stale or mixed-purpose tables that combine unrelated claims without a clear caption, local narrative, and current data source.
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
- If a table caption starts with "算法" or the table contains algorithm markers such as "输入", "输出", "阶段", `for`, `while`, `if`, `else`, `return`, line numbers, or code-like statements, audit it as an algorithm table first.
- In the current MoE thesis template, algorithm titles are left aligned. Do not right-align them.
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

## Formula And Field Checks

- Scan edited formulas and nearby prose for raw LaTeX residue, duplicated symbols, and broken field output.
- High-risk patterns include `\alpha`, `\beta`, `$...$`, `_`, `^`, `<=`, `>=`, `≤≤`, duplicated variables such as `qTqT` or `LTLT`, and WPS strings such as "错误！未定义书签".
- Do not leave orphan math objects glued to prose. A formula object before "设..." or "表示..." usually means a copied symbol was left behind.
- Equation numbers should remain visible and stable after field update.
- Prefer real Word/WPS math objects for displayed equations. Avoid plain text formulas if neighboring equations use OMML/Equation objects.
- After WPS/Word field updates, exported PDF must not contain "错误！未定义书签".

## Figures And Page Layout

- Figure captions go below figures; table captions go above tables.
- Check the figure source against the intended chapter role. Do not keep an obsolete AI-generated figure when the source technical document provides the correct overall scheme or Chakra/DAG figure.
- After replacing or resizing a figure, verify caption, body reference, visible size, aspect ratio, page break, and neighboring explanatory paragraph.
- A figure should not occupy a whole page with no interpretation unless the template explicitly requires it. Add a compact motivation before it or interpretation after it.
- For comparison figures, prefer a left-right composition when the user has rejected vertical stacking.
- Detect blank pages through rendered PDF text and visual inspection, not only through DOCX paragraph counts.
- For thesis delivery, a page containing only one orphan line before a forced
  chapter break is a blocking layout error. Render to PNG, compute low-content
  pages, inspect them, and fix the preceding paragraph or page break instead of
  delivering a near-blank page.
- On Windows/WPS setups, if `Word.Application` reports a false "file may be
  corrupted" error on a package-valid DOCX, try `KWPS.Application` for export
  before assuming the file is broken.

## Delivery Gate

Before delivering any edited DOCX, run separate audits for:

- package validity;
- citation superscript and jumpability;
- Latin font assignment;
- ordinary table indentation/alignment/font;
- algorithm-table indentation/alignment/font;
- formula broken fields and raw LaTeX residue;
- figure/table captions and page breaks;
- blank-like rendered pages;
- highlights and comments if the task touches review marks.

If any gate is not zero or intentionally skipped, say so in the final answer.

For the MoE thesis, do not deliver until the final report includes these
zero-blocker checks: citation links/superscript, ordinary-table leading spaces
and indents, algorithm-table leading spaces and indents, forbidden wording,
formula residue, and rendered blank-like pages.
