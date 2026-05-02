# Literature Comparison Table Template

One file per topic / decision, not per paper. Use this after reading 5-15
papers from `templates/literature_note.md` to force a side-by-side view before
writing prose.

---

## Topic

State the question in one sentence, and the decision this comparison informs.

## Scope Filter

- Included papers must satisfy:
- Excluded because:
- Date window:
- Venue filter (if any):

## Dimensions

List the 5-10 columns that matter. Typical choices:

- Problem setting
- Core method
- Data / benchmark
- Headline metric
- Compute / scale
- Assumptions / failure modes
- Code or artefacts released
- Load-bearing for our project? (yes / partial / no)

Drop dimensions that do not actually discriminate between papers.

## Table

| Cite key | Year | Setting | Method (1 line) | Dataset / Benchmark | Headline metric | Scale | Assumption / failure mode | Code? | Load-bearing? | Source (table / fig / sec) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

Every cell must be traceable. If a cell is "unknown", write `unknown` and
explain in the notes rather than leaving it blank.

## Cross-Paper Observations

- What is consistent across all methods:
- Where claims disagree:
- Where numbers are not comparable (different splits, metrics, prompts):
- Which assumption, if broken, invalidates most of the column:

## Implication For The Current Project

- Methods worth prototyping:
- Methods worth citing but not adopting:
- Gaps our work would fill:
- Risks if we adopt the leading method blindly:

## Follow-Up Reading Queue

- Papers added after building this table:
- Questions that were not answerable from the current set:

## Status

- [ ] First pass (abstracts + tables)
- [ ] Second pass (methods section read)
- [ ] Numbers cross-checked against original PDFs
- [ ] Used to draft related work / methodology section
