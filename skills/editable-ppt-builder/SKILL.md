---
name: editable-ppt-builder
description: Build and revise PowerPoint/WPS decks as editable PPTX files with native text, shapes, icons, tables, charts, and separately stored image assets.
---

# Editable PPT Builder

Use this skill whenever the requested output is a PPT/PPTX deck or slide.

## Core Rule

Important slide content must stay editable. Use native text boxes, shapes, icons,
tables, and charts. Do not flatten an entire slide into one image unless the user
explicitly asks for a poster-like export.

## Revising An Existing Research Deck

When a user supplies a PPTX as the required style reference, treat that file as
the visual contract rather than as a source of approximate inspiration. Before
editing, inspect the current filename, slide count, target slides, existing
speaker notes, and the layout of the affected pages. Do not infer the current
state from an older deck, render, or remembered path.

- Edit only the slides and elements the user identifies. Preserve the theme,
  masters, layouts, fonts, page numbering, and untouched sections.
- Never overwrite a user-submitted baseline deck. Save the revised deck as a
  separate file unless in-place editing is explicitly requested.
- When replacing a chart, reproduce the approved chart grammar: chart type,
  category order, labels, colors, axes, annotations, and legend treatment. Do
  not add average lines, extra subplots, alternate colors, or decorative marks
  unless requested.
- Keep a separately inspectable source table or plotting script for every
  data-driven figure; it is the authority for the plotted values.

## Research Data And Chart Rules

For experimental figures, calculate values from the authoritative CSV, JSON,
or raw measurement files before drawing. State internally whether a number is a
single-point value, a group average, or a global average; never substitute one
for another in a chart or summary table.

- Verify the requested point count and category ordering against the source
  rows before exporting. For grouped charts, write the group/order mapping next
  to the data so each bar remains auditable.
- If a plot compares measured and simulated quantities, retain their source
  columns and the exact error formula. Label formula estimates, simulator
  outputs, and hardware measurements as distinct evidence layers.
- Public hardware specifications used as simulation inputs are parameters, not
  measurements. Record the source, parameter value, topology, and latency
  assumption beside the figure or in its reproducibility note.
- Do not claim that a figure reflects a new run until its data source, run
  directory, and figure output have all been checked in the current task.

## Speaker Notes

Treat speaker notes as concise presentation support, not a second report.
Explain the meaning of an important chart or formula, include only technical
detail that helps the speaker answer likely questions, and avoid repeating the
visible conclusion verbatim. Respect the user's requested note style. Do not
insert generic `[Sources]` blocks when the user asks for concise notes or
explicitly requests their removal.

## Rendering And Delivery Gate

Before delivery, render the complete revised deck and inspect every slide, not
only the changed page. Check for clipped or wrapped text, misalignment, font
fallback, chart-label overlap, invisible objects, and unintended edits to
untouched slides. Inspect speaker notes separately after the final save.

- For Chinese SVG figures, embed glyphs as paths (for example, Matplotlib
  `svg.fonttype="path"`) or otherwise verify that the target viewer renders
  the selected CJK font correctly. A valid-looking PNG does not prove that the
  SVG is usable.
- Deliver the PPTX plus direct paths to the final figures and their data tables
  or scripts, so the recipient can check the numbers without extracting the
  deck.

## Workflow

1. Identify whether this is a new deck or a revision of an existing deck; for
   revisions, inspect the actual baseline before changing anything.
2. Define each affected slide's purpose and one-sentence takeaway.
3. Recalculate any chart values from the authoritative data source, then retain
   the data table or script beside the deck.
4. Build or update layout with native editable objects.
5. Insert images only as assets or backgrounds.
6. Render the final deck, inspect every slide and the final notes, and correct
   visual or data inconsistencies.
7. Export PDF only as a delivery copy.

## Tool Selection

- Use PowerPoint/WPS for final manual polish.
- Use PptxGenJS for JavaScript-driven decks.
- Use python-pptx for Python/data-driven decks.
- Use pptx-automizer when filling or rearranging a template deck.
- Test ppt-master on small decks before trusting it for formal output.

## Checks

- Title and body text are editable.
- Icons and diagrams scale cleanly.
- Charts have source data or scripts.
- Generated images are separate files.
- PPTX opens correctly in PowerPoint/WPS.
- Target-slide edits preserve the supplied deck's visual system and do not alter
  unrelated slides.
- Chart labels, bar ordering, and displayed aggregates match the authoritative
  data source and requested definition.
- Rendered PNG/PDF and any delivered SVG show Chinese text correctly.
- Final speaker notes follow the requested level of detail and do not include
  unwanted generic source blocks.

