# Token Saving And Context Indexing

Reviewed on 2026-04-30.

## Local Downloads

The following upstream projects were cloned locally for inspection:

- `third_party/claude-context`
  - Upstream: https://github.com/zilliztech/claude-context
  - Local commit checked: `3675469 feat: deduplicate overlapping search results (#333)`
- `third_party/pua`
  - Upstream: https://github.com/tanweai/pua
  - Local commit checked: `34cf090 fix: use Glob discovery for protocol file paths in P7/P9/P10 agents`

`third_party/` is intentionally gitignored. Keep upstream clones local; store
only distilled notes, templates, and clean skills in this repo.

## Claude Context

Claude Context is an MCP server for semantic code search. It indexes a codebase
with embeddings and stores chunks in Milvus/Zilliz, then exposes tools such as:

- `index_codebase`
- `search_code`
- `get_indexing_status`
- `clear_index`

Why it saves tokens: an agent can search the indexed repository and load only
relevant chunks instead of repeatedly reading broad folders. The "40% token
saving" claim should be treated as workload-dependent, not guaranteed.

Use it for server-side code repositories and large unfamiliar projects. For
small one-file document edits, `rg` and direct file reads are cheaper.

## Current Machine Status

- Node.js is available.
- `pnpm` is not installed.
- PowerShell blocks direct `npm.ps1`; use `npx.cmd`/`npm.cmd` or configure MCP
  on the server shell.
- This Codex API session does not currently expose a `claude-context` MCP server,
  so it cannot be hot-used in this conversation. It can be used after adding MCP
  config and restarting Codex CLI/server Codex.

## Codex MCP Config

Create or edit `~/.codex/config.toml` on the server:

```toml
[mcp_servers.claude-context]
command = "npx"
args = ["@zilliz/claude-context-mcp@latest"]
env = {
  "EMBEDDING_PROVIDER" = "OpenAI",
  "OPENAI_API_KEY" = "YOUR_OPENAI_API_KEY",
  "EMBEDDING_MODEL" = "text-embedding-3-small",
  "MILVUS_ADDRESS" = "YOUR_ZILLIZ_OR_MILVUS_ENDPOINT",
  "MILVUS_TOKEN" = "YOUR_ZILLIZ_OR_MILVUS_TOKEN"
}
startup_timeout_ms = 20000
```

Optional local-private mode:

```toml
[mcp_servers.claude-context]
command = "npx"
args = ["@zilliz/claude-context-mcp@latest"]
env = {
  "EMBEDDING_PROVIDER" = "Ollama",
  "OLLAMA_HOST" = "http://127.0.0.1:11434",
  "OLLAMA_MODEL" = "nomic-embed-text",
  "MILVUS_ADDRESS" = "127.0.0.1:19530",
  "MILVUS_TOKEN" = ""
}
startup_timeout_ms = 20000
```

After restart, in the target repo ask Codex:

```text
Index this codebase.
Check the indexing status.
Search this codebase for: <specific behavior or function>.
```

Use the same absolute repo path every time. Claude Context keys codebases by
absolute path, so symlinks or second clones create separate indexes.

## Recommended Token Discipline

1. Start with project rules and the latest handoff note.
2. Use `rg`, Claude Context, Serena, GitNexus, or Repomix to find candidate
   files.
3. Read only the smallest necessary slice.
4. Verify by source/test/render/log, not by retrieval summary.
5. End with a compact handoff: changed files, checks, risks, next task.

## Clean PUA Skill

The upstream PUA project has useful persistence mechanics but a noisy style.
This repo keeps a clean version in:

`skills/pua/SKILL.md`

It is renamed semantically as **Persistent Unblocking Assistant**. It preserves:

- act-before-asking,
- failure inventory,
- materially different hypotheses,
- verification before completion,
- structured handoff when still blocked.

It removes:

- insults,
- shame/threat language,
- corporate role-play,
- long motivational monologues.
