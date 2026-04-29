---
name: figure-pipeline
description: Create reproducible charts, diagrams, and document figures while preserving editable sources and export manifests.
---

# Figure Pipeline

Use this skill when creating or revising charts, diagrams, technical figures, or
report illustrations.

## Required Artifacts

Keep these together:

- raw or processed data,
- plotting or diagram source,
- exported SVG/PDF/PNG,
- short manifest,
- caption or slide text.

## Charts

Preferred stack:

- Python,
- pandas / numpy,
- Matplotlib,
- SciencePlots,
- optional Seaborn / Altair / Plotly,
- optional marimo for notebooks.

Rules:

- Use consistent size, font, line width, marker size, and palette.
- Export vector format for review and high-DPI PNG for office compatibility.
- Record whether values are measured, simulated, estimated, or illustrative.

## Diagrams

Preferred stack:

- Mermaid or D2 for text-first drafts,
- draw.io desktop for final polishing,
- SVG/PNG export for documents and slides.

Rules:

- Keep `.mmd`, `.d2`, or `.drawio` source files.
- Use generated images only as assets, not as the only source of a technical
  diagram.
- Make direction, grouping, and dependency semantics explicit.

