# Local Experience Notes

These are practical rules learned from document, PPT, and figure work. Keep this
file short and factual so another GPT can apply it quickly.

## Document Work

- Make a named copy before touching an important DOCX.
- Inspect the current document state before applying a script; older templates
  can silently undo user formatting.
- Cross-references should remain fields or hyperlinks when the document requires
  jumpable references.
- Citation appearance can be affected by hidden run properties such as
  superscript, character position, scaling, or fit-text settings.
- Table cells often fail because of invisible paragraph indentation or leading
  spaces, not only visible alignment.
- For WPS/Word compatibility, verify both file structure and visual rendering
  when possible.

## Algorithm And Table Blocks

- Do not assume algorithm blocks should be centered. Check the target document's
  sample format.
- Keep algorithm title, input, output, stages, and line numbers as structured
  content when the format requires it.
- Tables should be checked for paragraph indentation, cell vertical alignment,
  and border style together.

## Figure Work

- A final figure should have a source. Examples: `.py`, `.drawio`, `.mmd`, `.d2`,
  `.xlsx`, or `.pptx`.
- Export both editable/vector review formats and office-compatible PNG when
  needed.
- Do not let a generated image model draw exact chart labels or equations.
- Keep visual style consistent across a paper/report/deck: font, line width,
  colors, marker sizes, and caption wording.

## PPT Work

- PPT slides should be editable unless the user explicitly asks for a flattened
  poster or image.
- Use AI images as assets or backgrounds. Add text, labels, arrows, and charts
  inside PPT.
- When generating decks programmatically, verify editability after opening the
  output in PowerPoint/WPS.
- Keep the PPTX source even when exporting a PDF for submission.

## Handoff Work

- A good handoff gives exact paths, exact changed files, checks passed, checks
  skipped, and next task.
- Avoid long chat summaries. Use factual, file-oriented notes.
- Separate stable project rules from one-off task notes.

