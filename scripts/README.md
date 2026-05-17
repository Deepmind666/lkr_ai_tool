# Scripts

Utility scripts in this folder should be portable and conservative. Prefer
inspection and reporting over broad automatic rewrites.

## Available

- `check_docx_structure.ps1`: checks DOCX package integrity, highlights,
  reference bookmarks, citation superscript formatting, and algorithm/table
  alignment patterns.
- `audit_docx_crossrefs.py`: audits DOCX citation/reference fields and reports
  missing hyperlinks, bad anchors, and non-superscript citation runs.
- `audit_docx_aigc_style.py`: local writing-risk triage for exported DOCX text.
  It is not an official detector; use it to find generic prose, citation dumps,
  weak technical anchors, and unsupported strong claims before running a formal
  AIGC service.

Example:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/check_docx_structure.ps1 -DocxPath "D:\path\document.docx"
python scripts/audit_docx_crossrefs.py "D:\path\document.docx"
python scripts/audit_docx_aigc_style.py "D:\path\document.docx" > qa_aigc_audit.json
```
