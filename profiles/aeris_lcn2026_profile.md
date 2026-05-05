# AERIS LCN 2026 Paper Profile

Use this profile with `skills/ieee-network-paper-writer` for the AERIS wireless
sensor network routing paper.

## Stable Story Line

The paper should present AERIS as a simple, rule-based, auditable,
reliability-first WSN routing design for heterogeneous and unstable channel
conditions. It should not present AERIS as a globally dominant routing protocol.

Recommended one-sentence story:

> AERIS improves delivery over classical WSN baselines in harsh heterogeneous
> channel regimes by adding context-adaptive local forwarding and
> Gateway-assisted uplinks, but this reliability is bought with concentrated
> relay burden, early first-node death, and a deployment boundary once stronger
> collection-tree/RPL-style baselines are considered.

## Non-Negotiable Claim Boundaries

- Do not claim AERIS is universally best.
- Do not claim AERIS replaces CTP, RPL, ORPL, ORW, or TSCH-based LLN stacks.
- Do not describe simplified CTP/RPL-MRHOF baselines as full
  standards-compliant stacks.
- Do not overstate Skeleton as a major gain carrier in the audited
  configuration; it is mostly reserve/dormant.
- Do not use the strict-physics Python stress layer as canonical protocol
  ranking evidence.
- Do not edit a user hand-copied `.bib` or a hand-drawn flowchart unless the
  user explicitly asks.

## Evidence Layers

Keep these roles separate in text, captions, and response to reviewers:

1. **Classical NS-3 audit.**
   AERIS vs LEACH, PEGASIS, HEED, and TEEN. This is the primary fairness anchor
   for classical WSN baselines. Current claim: AERIS ranks first in 21 of 28
   cells and top-two in all 28 cells against these classical baselines.

2. **Expanded seven-protocol boundary sweep.**
   Adds simplified CTP and RPL-MRHOF-style collection baselines. This is
   deployment-boundary evidence, not a replacement for the classical audit.
   It bounds the claim: collection-tree/RPL-style behavior reduces or removes
   AERIS's advantage outside selected regimes, especially benign office-like
   settings.

3. **NS-3 ablation.**
   Full AERIS vs no-Gateway, no-CAS, and no-CH-score variants. Use it to explain
   mechanism attribution. Gateway is the main gain carrier; CAS is conditional;
   CH scoring is near-neutral in the publication configuration.

4. **Strict-physics adapted stress layer.**
   Python stress simulator with adapted LEACH/HEED/TEEN relay support. Use it as
   collision/channel stress evidence only. It is not canonical ranking evidence.

5. **Mechanism and trade-off study.**
   Gateway uplink PDR, CAS behavior, Skeleton usage, first-node death, lifetime,
   hop count, and energy explain why AERIS works and what it costs.

## Core Mechanism Interpretation

- **Gateway:** main measured delivery gain, especially in harsh factory and
  suburban settings.
- **CAS:** useful when local detours remain viable; can be environment-dependent.
- **CH scoring:** near-neutral in the current publication configuration.
- **Skeleton:** reserve fallback; mostly dormant under audited settings.
- **Trade-off:** AERIS buys PDR by concentrating forwarding work on critical
  relay roles. This explains early first-node death and shorter lifetime.

## Known Reviewer Risks

Treat these as high-priority risks when reviewing or rewriting:

- Fixed coefficients and thresholds need provenance. If no sensitivity analysis
  is available, state they are a fixed heuristic publication configuration.
- Idealized MAC/channel assumptions limit external validity. Do not imply full
  802.15.4, TSCH, CSMA-CA, or capture-effect realism unless implemented.
- TEEN is event-triggered; PDR expected over all expected reports can be viewed
  as unfavorable. Discuss energy/lifetime and denominator sensitivity.
- Simplified CTP/RPL-MRHOF baselines are useful boundary baselines but not full
  LLN stacks with all control behavior.
- Table-level pooled results must say they are pooled across environments and
  should not be generalized to all scales unless the data support it.
- If a figure is changed, verify that panel titles, caption, formula definition,
  and section text all use the same baseline set and denominator.

## Local AERIS Paths

Main project root:

```text
C:\AERIS-WSN-Protocol
```

Current Overleaf package:

```text
C:\AERIS-WSN-Protocol\LCN26_AERIS_overleaf
```

Common current files:

```text
LCN26_AERIS_overleaf\aeris_lcn2026.tex
LCN26_AERIS_overleaf\aeris_lcn2026.pdf
LCN26_AERIS_overleaf\ref.bib
LCN26_AERIS_overleaf\figures\
LCN26_AERIS_overleaf\figure_data\
```

Use the repository's current figure manifest or data folders to map each figure
to source data before making reproducibility claims. If a path is missing, search
the project rather than inventing a replacement.

## Preferred Review Output

For a deep review, output:

1. Difference from the previous draft, if a previous draft is supplied.
2. P0/P1/P2 findings with exact page, section, figure, table, or file references.
3. Technical loopholes that a strict LCN reviewer can attack.
4. Minimal deadline-safe edits.
5. A realistic accept/reject risk score, without flattering the author.
