---
name: thesis-aigc-revision
description: Audit and revise Chinese thesis prose to reduce AI-like generic writing by adding technical grounding, improving citation placement, and preserving DOCX formatting.
---

# Thesis AIGC Revision

Use this skill for Chinese thesis drafts when the user asks for AIGC-rate
checks, AI-like prose cleanup, or thesis paragraph revision.

## Workflow

1. Preserve the source file. For `.docx` work, copy to a new named output before
   editing.
2. Run the local audit script:

   ```powershell
   python scripts/audit_docx_aigc_style.py "D:\path\thesis.docx" > qa_aigc_audit.json
   ```

3. Start with `aigc.top_findings`. Prioritize paragraphs flagged for citation
   density, unsupported strong claims, long generic prose, or weak technical
   anchors.
4. Revise by adding concrete evidence:
   - technical objects, variables, data sources, equations, checks, or figure
     interpretations;
   - citations placed beside the exact paper, system, or factual claim;
   - paragraph logic that moves from observation to mechanism to consequence.
5. Do not promise official detector results or detector bypass. The local score
   is only a writing-risk triage signal.
6. Rerun the audit after editing. Check that `phrase_counts` and
   `top_findings` decreased, then run any relevant DOCX format checks.

## Revision Rules

- Do not perform mechanical synonym replacement.
- Avoid generic thesis phrases such as "has important significance",
  "experiments fully prove", "significantly improves", and "seamlessly maps"
  unless measurements support them.
- Do not stack many references at the end of a paragraph. Tie references to
  specific claims.
- Keep boundaries concrete. Prefer "this experiment checks X" over repeated
  disclaimers about what the work does not do.
- When editing DOCX files, preserve existing cross-references, bookmarks,
  captions, table alignment, and user-adjusted formatting.
