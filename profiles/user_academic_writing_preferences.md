# User Academic Writing Preferences

Use this profile with academic writing, paper review, figure design, and
submission-package work.

## Review Stance

- Be strict and concrete. The user prefers direct reviewer-style criticism over
  reassurance.
- Lead with risks and contradictions, then summarize improvements.
- Use severity labels:
  - `P0`: fatal contradiction, unreproducible artifact, wrong data mapping, or
    likely rejection trigger.
  - `P1`: misleading claim, missing method/setup detail, baseline fairness risk,
    or serious layout issue.
  - `P2`: style, polish, or minor formatting issue.

## Writing Logic

- Build the paper around a clear story line.
- Do not pile up results without explaining the role of each evidence layer.
- Keep claims tied to exact data, metrics, denominators, and figure/table IDs.
- Avoid universal-best language unless the evidence truly supports it.
- If a limitation is real and cannot be fixed before deadline, state it clearly
  and narrow the claim.

## Method Expectations

- Method sections should include enough equations, variables, thresholds, and
  fallback rules for reproducibility.
- Avoid long dry method prose without mathematical structure.
- Move pure parameter-setting details to experiment setup unless they define the
  algorithm itself.
- If weights are hand-selected or heuristic, say so. Do not imply optimization
  or sensitivity analysis that was not performed.

## Figure Preferences

- Prefer compact, publication-style figures.
- Avoid unnecessary two-column figures and large multi-row layouts.
- Avoid too many heatmaps; use bars, margin plots, CDFs, boxplots, or small
  multiples when clearer.
- If lines overlap, change the plot type rather than defending the line chart.
- Use a coherent color system and make the proposed method visually identifiable.
- Use Times-like fonts for academic paper figures.
- Keep subfigure titles/labels centered when using centered subfigure design.
- Captions must explain abbreviations, sample counts, denominators, and whether
  the plotted value is absolute, pooled, mean, or delta.

## Layout Preferences

- Follow the venue template exactly for table and caption alignment.
- Do not let a table and a figure stick together without explanatory prose.
- Avoid large blank regions and isolated tiny blocks on a page.
- When the user says "8 pages excluding references", count body pages separately
  from references.
- In thesis DOCX front matter, the Chinese abstract note must be on the Chinese
  abstract page near the last line, not on a separate blank page. Validate this
  in WPS, not only in LibreOffice.
- In ordinary table cells, never leave literal leading spaces or inherited
  first-line indentation. This is a blocking formatting issue.
- Algorithm table titles and pseudocode follow the user's template; do not
  globally center algorithm-table text.
- Citation references should appear at the sentence or clause end. Avoid
  citation dumps such as `[3]、[4]、[5]` unless the user explicitly requests that
  style.

## File and Artifact Safety

- Do not modify a user hand-copied bibliography unless explicitly asked.
- Do not modify a user hand-drawn flowchart unless explicitly asked.
- Before pushing or handing off, ensure the PDF, source, figures, data, scripts,
  and submission package/zip are synchronized.
- Provide exact paths and pull instructions when another AI will review the work.
