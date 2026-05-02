---
name: academic-research
description: Run literature search, paper triage, focused reading, citation hygiene, and review-style synthesis without fabricating references. Use when a task involves arXiv/Google Scholar/Semantic Scholar lookups, BibTeX/Zotero handling, reading a PDF for a specific claim, comparing N papers on a topic, drafting a related-work section, or any moment an agent might be tempted to invent a citation.
---

# Academic Research

Use this skill whenever the task is to find, read, compare, or cite scholarly
sources. The single hardest rule: **no invented references, no invented page
numbers, no invented authors**.

## Hard Rules

- Every cited fact carries a verifiable source: DOI, arXiv ID, venue + year, or
  a stable URL. No source, no claim.
- An agent may not generate a BibTeX entry from memory. Pull it from the
  publisher, arXiv, or Semantic Scholar API, then keep the raw response.
- Distinguish primary papers from secondary surveys/blogs/tweets. Quote primary
  for methods and numbers; secondary only for context.
- Do not paraphrase a paper that has not actually been opened. "Likely says X"
  is not a finding.
- When summarising a number from a paper, record table/figure/section so the
  next reader can re-check.

## Workflow

1. **Frame the question.** One sentence, with the decision it informs and the
   acceptable evidence type (benchmark numbers? proof? survey?).
2. **Discover candidates.** Search 2-3 sources, not just one. Save raw query
   strings.
3. **Triage by abstract.** Drop anything that does not match the question. Keep
   reasons for drops; they are useful when the user pushes back.
4. **Read with a goal.** Open a PDF for a specific claim, table, or section,
   not "to summarise". Capture page/figure numbers as you go.
5. **Note in a structured form.** Use `templates/literature_note.md` so notes
   are comparable across papers.
6. **Synthesize across papers.** Build a comparison table before writing prose.
   Rows = papers, columns = the dimensions that matter for the decision. Use
   `templates/literature_comparison_table.md`.
7. **Cite cleanly.** Export BibTeX from the source of truth, not the LLM.

## Recommended Tool Stack

Discovery:

- arXiv (preprints, latest work).
- Semantic Scholar (graph: citations, references, influence).
- Google Scholar (broad coverage, alerts).
- Connected Papers / Inciteful / Litmaps (neighbourhood expansion from a seed).
- OpenReview (open peer review for ICLR/NeurIPS/etc.).

PDFs and reading:

- Zotero (library, tags, annotations, citation export).
- Better BibTeX for Zotero (stable cite keys, auto-export).
- SumatraPDF or local viewer for fast skim with margin notes elsewhere.

Notes and synthesis:

- Markdown notes per paper, plus one comparison table per topic.
- Obsidian or plain Markdown vault if cross-linking helps.
- A single `references.bib` per project, generated/exported, not hand-typed.

LLM assistance:

- OK: extract structure, suggest related work, rewrite a sentence, sanity-check
  a paraphrase against the original PDF text.
- Not OK: produce citations, fill in numeric results, summarise a paper that
  has not been opened.

## Anti-Patterns

- Pasting a long PDF into the chat and asking for a verdict; instead, search
  for the relevant section first.
- Letting the model produce a "References" list at the end of a draft; build
  the bibliography from the manager, then check every cite-key resolves.
- Treating Connected Papers / similar tools as evidence. They are navigation;
  proof is in the paper.
- Citing arXiv versions when the published venue version exists and matters
  for the claim.

## Output Hygiene

- For any deliverable that contains citations, also produce: a `.bib` file, a
  list of every cite-key used, and a one-line note per key explaining why it
  was cited where it was cited.
- If a claim cannot be backed by a primary source after search, mark it as
  "unverified" in the draft instead of softening the wording.
