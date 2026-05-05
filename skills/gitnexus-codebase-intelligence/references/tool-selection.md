# Large Codebase Tool Selection

Use this reference when choosing between repository-intelligence tools.

| Tool | Best Use | Local Setup Status | Main Risk |
| --- | --- | --- | --- |
| GitNexus | Local code graph, MCP exploration, symbol context, impact analysis | Installed as `gitnexus.cmd`; MCP can be configured in Codex | Index freshness, startup cost, and occasional version-specific analyzer failures |
| Repomix | Pack a repo into one AI-friendly snapshot for handoff or review | Installed as `repomix.cmd` | Oversharing generated files or secrets |
| Serena | LSP-style semantic navigation and code editing | Evaluate per project before installing | Requires language-server setup and can be heavier |
| Sourcebot | Self-hosted multi-repo code search for teams | Not enabled by default | Service maintenance and indexing overhead |
| CodeGraphContext | MCP server backed by graph retrieval for large codebases | Not enabled by default | Usually needs graph/database setup |
| Claude Context | Semantic/vector retrieval over indexed repos | Not enabled by default | Remote/vector storage and privacy choices |
| Gitingest | Quick public repository text digest | Use only for public repos or throwaway snapshots | Not suitable for private exact-source verification |

Recommended default on Windows Codex:

1. Use `rg` and direct reads for small tasks.
2. Use GitNexus when a repository needs graph-aware exploration.
3. Use Repomix when another agent or machine needs a compact source artifact.
4. Add heavier services only when repeated large-codebase work justifies their background cost.

If `gitnexus analyze` exits without a useful error, first verify the version with `gitnexus.cmd --version`. In the current Windows/Node.js 24 environment, `gitnexus@1.6.4-rc.66` succeeded where `1.6.3` did not.

Source notes:

- GitNexus: https://github.com/abhigyanpatwari/GitNexus
- Repomix: https://github.com/yamadashy/repomix
- Serena: https://github.com/oraios/serena
- Sourcebot: https://github.com/sourcebot-dev/sourcebot
- CodeGraphContext: https://codegraphcontext.github.io/
- Gitingest: https://github.com/cyclotruc/gitingest
