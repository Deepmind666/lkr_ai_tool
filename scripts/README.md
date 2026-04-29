# Scripts

Utility scripts in this folder should be portable and conservative. Prefer
inspection and reporting over broad automatic rewrites.

## Available

- `check_docx_structure.ps1`: checks DOCX package integrity, highlights,
  reference bookmarks, citation superscript formatting, and algorithm/table
  alignment patterns.

Example:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/check_docx_structure.ps1 -DocxPath "D:\path\document.docx"
```

