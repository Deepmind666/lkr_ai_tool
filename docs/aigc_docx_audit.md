# DOCX AIGC Style Audit

`scripts/audit_docx_aigc_style.py` is a local heuristic checker for Chinese
thesis drafts in `.docx` format. It does not replace an official AIGC detector.
Its purpose is to find paragraphs that tend to look machine-written because
they are generic, citation-dense, weakly anchored in technical objects, or full
of unsupported strong claims.

## Run

```powershell
python scripts/audit_docx_aigc_style.py "D:\path\thesis.docx" > qa_aigc_audit.json
```

The script emits JSON to stdout. Useful fields:

- `aigc.risk_rate`: heuristic share of body text flagged for revision.
- `aigc.risk_chars`: flagged characters before references/acknowledgements.
- `aigc.phrase_counts`: repeated high-risk phrases.
- `aigc.top_findings`: paragraphs to revise first.
- `tables`: table formatting checks, including leading cell spaces and hidden
  paragraph indents.
- `counts`: DOCX package counts for math, highlights, bookmarks, and fields.

## How To Interpret

Treat the score as a triage signal, not a detector score. A high-risk paragraph
usually needs one of these repairs:

- Replace generic claims with concrete mechanisms, variables, data, or checks.
- Move citations next to the exact system or claim they support.
- Split long citation lists into smaller paragraphs with a clear comparison
  dimension.
- Avoid unsupported phrases such as "significant improvement", "fully proves",
  "seamless", or "highly reliable" unless the document gives measurements.
- Keep scope statements short and substantive; avoid repeated disclaimers.

After revising, rerun the script and inspect `top_findings` rather than chasing
the numeric score alone.
