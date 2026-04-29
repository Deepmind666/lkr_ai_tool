# Editable PPT Workflow

Goal: produce PPTX files where text, icons, shapes, tables, and charts can still
be edited in PowerPoint or WPS.

## Principle

A slide is editable when the important content is represented as native slide
objects:

- text boxes,
- shapes,
- lines and arrows,
- icons or SVGs,
- tables,
- charts,
- grouped objects,
- separately inserted images.

A full-slide screenshot is only acceptable for a temporary preview.

## Recommended Tool Choices

### Manual / Visual Editing

- PowerPoint or WPS for final adjustment.
- draw.io desktop for diagrams exported as SVG/PNG while keeping `.drawio`
  source.
- Built-in icon libraries or SVG icon sets for scalable symbols.

### AI-To-PPT Drafting

- `ppt-master`: promising because it targets natively editable PPTX from
  documents.
- Test before trusting: open the output and check whether objects are real text,
  shapes, charts, and tables.

### Programmatic PPTX

- `PptxGenJS`: best when JavaScript layout generation is convenient.
- `python-pptx`: best when data and chart pipelines are already in Python.
- `pptx-automizer`: best when reusing and filling an existing template deck.

## Slide Build Order

1. Decide slide purpose and one-sentence takeaway.
2. Sketch layout with native boxes, not images.
3. Add editable title, labels, and callouts.
4. Add chart/table as native object when possible.
5. Add generated image or diagram export only where it adds visual value.
6. Check editability in PowerPoint/WPS.
7. Export PDF only as a delivery copy, never as the source.

## For Research And Technical Decks

- Keep charts reproducible from data.
- Keep figure captions and slide claims close to the source data.
- Prefer plain, stable layout over decorative backgrounds.
- Use one visual hierarchy: title, evidence, takeaway.
- Keep generated images out of charts and equations.

## Asset Folder Pattern

```text
slides/
  YYYYMMDD_deck_name/
    deck.pptx
    deck.pdf
    assets/
      images/
      icons/
      diagrams/
    sources/
      charts/
      prompts/
      drawio/
    manifest.json
```

## Editability Checklist

- [ ] Slide title is editable text.
- [ ] Body text is editable text.
- [ ] Icons can be scaled without blur.
- [ ] Diagrams have source files.
- [ ] Charts have source data or script.
- [ ] Generated images are separate assets, not the entire slide.
- [ ] PPTX opens correctly in PowerPoint/WPS.
- [ ] PDF export is only a delivery artifact.

