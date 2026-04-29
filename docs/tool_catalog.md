# Tool Catalog

Reviewed on 2026-04-29. Star counts are only freshness signals; always verify a
tool against the exact task before adopting it.

## High-Value Shortlist

| Area | Tool | Why keep it |
| --- | --- | --- |
| Code graph | GitNexus | Builds a code knowledge graph and helps agents inspect dependencies. |
| Code snapshot | Repomix | Packs selected repo files into an AI-friendly context bundle. |
| Semantic code work | Serena | MCP-style semantic retrieval and editing for larger codebases. |
| Terminal coding | Aider | Strong CLI pair-programming workflow for Git repositories. |
| IDE agents | Cline, Roo Code | Useful when an IDE agent needs to edit and run code locally. |
| Agent memory | Graphiti, mem0 | Candidate long-term memory layers; self-host if data is sensitive. |
| Editable PPT | ppt-master | AI-to-editable-PPTX direction; worth testing for draft decks. |
| PPT generation | PptxGenJS, python-pptx, pptx-automizer | Programmatic editable PowerPoint generation and template automation. |
| Diagrams | draw.io desktop, Mermaid, D2, Penrose | Versionable diagram sources plus polished exports. |
| Experiment figures | marimo, Matplotlib, SciencePlots, Seaborn, Altair, Plotly | Reproducible charts and notebooks. |

## Code Knowledge And Server-Side Context

### GitNexus

- Repo: https://github.com/abhigyanpatwari/GitNexus
- Observed stars: about 33k on 2026-04-29.
- Fit: code knowledge graph exploration and Graph RAG over a GitHub repo or ZIP.
- Use when: another GPT needs function dependencies, call relationships, or
  repo structure before editing code.
- Keep in mind: the graph is a navigation aid, not proof. Claims still need
  direct file and test verification.

### Repomix

- Repo: https://github.com/yamadashy/repomix
- Observed stars: about 24k on 2026-04-29.
- Fit: compact AI-ready snapshots of selected repository files.
- Use when: a server repo must be handed to another GPT without copying raw
  data, generated outputs, or private files.
- Suggested rule: pack only source, configs, docs, and small examples.

### Serena

- Repo: https://github.com/oraios/serena
- Observed stars: about 23.6k on 2026-04-29.
- Fit: semantic code retrieval/editing through MCP.
- Use when: the codebase is too large for direct context and symbol-level
  navigation matters.

### Aider

- Repo: https://github.com/Aider-AI/aider
- Observed stars: about 44k on 2026-04-29.
- Fit: terminal-first AI pair programming with Git-aware patches.
- Use when: a server-side coding GPT should make small, reviewable commits.

### Cline And Roo Code

- Cline: https://github.com/cline/cline
- Roo Code: https://github.com/RooCodeInc/Roo-Code
- Fit: IDE-based autonomous coding workflows.
- Use when: the machine has the full dev environment and the task benefits from
  visible file navigation, terminals, and iterative test runs.

### Sourcebot

- Repo: https://github.com/sourcebot-dev/sourcebot
- Observed stars: about 3.3k on 2026-04-29.
- Fit: self-hosted code search for humans and agents.
- Use when: several projects or agents need repeatable code search.

## Memory And Handoff

### Local Markdown Memory

- Fit: default starting point.
- Use files such as `templates/session_memory.md`,
  `templates/figure_manifest.md`, and project-specific `AGENTS.md`.
- Advantage: transparent, Git-friendly, easy for any GPT to read.

### Graphiti

- Repo: https://github.com/getzep/graphiti
- Fit: temporal knowledge graph memory.
- Use when: the project needs versioned facts, decision history, and changing
  relationships.
- Caution: prefer self-hosting for private documents.

### mem0

- Repo: https://github.com/mem0ai/mem0
- Fit: long-term agent memory.
- Use when: preferences and project state need to persist across sessions.
- Caution: check storage location and privacy before using it with drafts or
  private reports.

### Microsoft GraphRAG

- Repo: https://github.com/microsoft/graphrag
- Fit: graph-based retrieval over document collections.
- Use when: many background documents need structured retrieval rather than
  one-off keyword search.

## Editable PPT And Presentation Work

### ppt-master

- Repo: https://github.com/hugohe3/ppt-master
- Observed stars: about 9.4k on 2026-04-29.
- Fit: AI generation of natively editable PPTX from documents.
- Why it matters: it explicitly targets real PowerPoint shapes rather than
  flattened slide images.
- Test plan: try it on one small deck, then inspect whether text boxes, icons,
  tables, and charts remain editable in PowerPoint/WPS.

### PptxGenJS

- Repo: https://github.com/gitbrent/PptxGenJS
- Observed stars: about 5.1k on 2026-04-29.
- Fit: JavaScript generation of editable PowerPoint files.
- Use when: a deck can be described as data, layout boxes, text, shapes, images,
  tables, and charts.

### python-pptx

- Repo: https://github.com/scanny/python-pptx
- Observed stars: about 3.3k on 2026-04-29.
- Fit: Python creation and modification of Open XML PowerPoint files.
- Use when: chart/data pipelines are already Python-based.

### pptx-automizer

- Repo: https://github.com/singerla/pptx-automizer
- Fit: template-based PPTX automation and slide reuse.
- Use when: you have a strong master deck and want to fill or rearrange slides
  while preserving theme and editable elements.

## Image Generation For Documents And PPT

### OpenAI gpt-image-2

- Official docs: https://developers.openai.com/api/docs/models/gpt-image-2
- Fit: high-quality image generation and editing.
- Important current limitation from official docs: transparent backgrounds are
  not supported yet.
- Use when: you need a background, object render, texture, visual metaphor,
  product-style mockup, or illustration source.
- Do not use it for: precise Chinese/English slide text, final chart labels, or
  dense tables. Put those into PPT as editable text and shapes.

## Diagrams

### draw.io desktop

- Repo: https://github.com/jgraph/drawio-desktop
- Fit: polished editable architecture diagrams, workflow diagrams, and DAGs.
- Rule: keep `.drawio` as source, export SVG or PNG only as delivery formats.

### Mermaid

- Repo: https://github.com/mermaid-js/mermaid
- Fit: quick versionable flowcharts, sequence diagrams, and state diagrams.
- Rule: good for drafts and documentation; polish in draw.io when final visual
  quality matters.

### D2

- Repo: https://github.com/terrastruct/d2
- Fit: clean text-based architecture and dataflow diagrams.
- Rule: use for stable layout drafts; export SVG for review.

### Penrose

- Repo: https://github.com/penrose/penrose
- Fit: notation-driven mathematical and conceptual diagrams.
- Rule: optional, valuable when a figure is closer to a formal concept diagram
  than a simple flowchart.

## Charts And Experiment Figures

### marimo

- Repo: https://github.com/marimo-team/marimo
- Fit: Git-friendly reactive Python notebooks.
- Use when: a figure notebook should remain reviewable as plain Python.

### Matplotlib + SciencePlots

- Matplotlib: https://github.com/matplotlib/matplotlib
- SciencePlots: https://github.com/garrettj403/SciencePlots
- Fit: publication-style static charts.
- Rule: export vector formats for source review and high-DPI PNG for WPS/Word
  compatibility.

### Seaborn, Altair, Plotly

- Seaborn: https://github.com/mwaskom/seaborn
- Altair: https://github.com/vega/altair
- Plotly: https://github.com/plotly/plotly.py
- Fit: exploration, statistical charts, and interactive analysis.
- Rule: final paper/report figures should still pass through a consistent style
  and export pipeline.

## Adoption Order

1. Keep local Markdown memory and this repository structure immediately.
2. Use draw.io, Matplotlib/SciencePlots, and editable PPT workflows for current
   document work.
3. Add Repomix to the server machine for AI handoff.
4. Test GitNexus or Serena on one real code repo before standardizing.
5. Evaluate Graphiti or mem0 only after privacy and self-hosting choices are
   clear.

