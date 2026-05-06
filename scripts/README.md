# Scripts

Utility scripts in this folder should be portable and conservative. Prefer
inspection and reporting over broad automatic rewrites.

## Available

- `audit_docx_aigc_style.py`: audits a `.docx` thesis draft for AI-like prose
  risks, citation-density issues, weak technical anchoring, unrendered LaTeX-like
  text, and table formatting problems. It prints JSON to stdout.
- `check_docx_structure.ps1`: checks DOCX package integrity, highlights,
  reference bookmarks, citation superscript formatting, and algorithm/table
  alignment patterns.

Example:

```powershell
python scripts/audit_docx_aigc_style.py "D:\path\thesis.docx" > qa_aigc_audit.json
```

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/check_docx_structure.ps1 -DocxPath "D:\path\document.docx"
```

