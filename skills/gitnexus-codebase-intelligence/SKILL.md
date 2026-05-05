---
name: gitnexus-codebase-intelligence
description: Use when Codex must understand, index, query, or summarize a large codebase with GitNexus, Repomix, Serena, Sourcebot, CodeGraphContext, Gitingest, Claude Context, MCP search, or similar repository-intelligence tools while keeping context small and verifying claims against source files.
---

# GitNexus Codebase Intelligence

Use this skill to choose the lightest codebase-intelligence tool that answers the current question without flooding context. Retrieval tools find candidates; source files, tests, traces, and logs prove claims.

## Tool Choice

Prefer tools in this order unless the user asks for a specific one:

1. `rg`, file manifests, and direct source reads for small or narrow tasks.
2. GitNexus for local repository graph, symbol context, impact analysis, and MCP-backed exploration.
3. Repomix for portable repository snapshots, handoff files, or sharing a compact source bundle with another agent.
4. Serena or other LSP-backed tools when symbol-level editing and language-server semantics matter.
5. Sourcebot, CodeGraphContext, Claude Context, or vector/graph services only when the repository set is large enough to justify a service, index, or database.
6. Gitingest for quick public GitHub snapshots, not for private local work or claims requiring exact line verification.

For detailed tradeoffs and source notes, read `references/tool-selection.md`.

## GitNexus Workflow

1. Confirm the target path is a Git repository and that large binary, dataset, cache, and generated folders are excluded by `.gitignore` or tool configuration.
2. Run `gitnexus analyze <repo-path>` before relying on GitNexus results. Use `gitnexus analyze --force <repo-path>` only when the index is stale or dependencies changed substantially.
3. Use narrow queries: ask where a behavior is implemented, what calls a symbol, or what may break if a file changes. Avoid vague prompts such as "explain the whole repo".
4. Read the returned source files directly before editing or reporting conclusions.
5. Keep `.gitnexus/` untracked unless the project explicitly wants to version index artifacts.
6. If GitNexus MCP is unavailable, fall back to `gitnexus query`, `gitnexus context`, `gitnexus impact`, `rg`, and direct file reads.

Useful commands:

```powershell
gitnexus.cmd analyze .
gitnexus.cmd list
gitnexus.cmd status
gitnexus.cmd query "where is routing trace converted to All-to-Allv bytes"
gitnexus.cmd context <symbol>
gitnexus.cmd impact <symbol-or-file>
```

## Repomix Workflow

Use Repomix when an agent needs a compact repository artifact rather than a live graph.

```powershell
repomix.cmd . --style markdown --output .\repomix-output.md --top-files-len 20
repomix.cmd . --token-count-tree 200 --output .\repomix-output.xml
```

Do not commit `repomix-output.*` unless the user explicitly wants a handoff artifact in the repository.

## Verification Rules

- Do not claim "the codebase does X" from an index hit alone; cite or inspect the exact file/function.
- Do not index the whole machine. Index only the target repo or an explicitly named repo group.
- Do not run heavyweight services for one-file edits.
- Do not include secrets, private drafts, generated datasets, build caches, virtual environments, or node modules in repository packs.
- For architecture reports, list the retrieval tool used, the indexed path, and the direct files inspected.

