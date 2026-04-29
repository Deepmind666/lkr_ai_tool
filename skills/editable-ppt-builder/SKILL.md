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

## Workflow

1. Define each slide's purpose and one-sentence takeaway.
2. Build layout with native editable objects.
3. Insert images only as assets or backgrounds.
4. Keep chart data/scripts and diagram sources beside the deck.
5. Open or render the deck to verify layout and editability when feasible.
6. Export PDF only as a delivery copy.

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

