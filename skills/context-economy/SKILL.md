---
name: context-economy
description: Reduce token waste in Codex/agent sessions by using retrieval, indexing, file manifests, and compact handoff notes. Use when working with large codebases, long papers, repeated document sessions, Claude Context, Repomix, GitNexus, Serena, MCP search, or any request to save context/tokens.
---

# Context Economy

Goal: spend context on evidence and decisions, not repeated discovery.

## Operating Rules

1. **Search before reading.** Use semantic search, `rg`, symbol search, or a file
   manifest before opening large files.
2. **Read slices, not folders.** Open the exact function, section, table, or XML
   node needed for the current decision.
3. **Cache stable facts.** Put project rules, file paths, figure sources, command
   recipes, and unresolved risks in a handoff note instead of re-explaining them
   every session.
4. **Separate retrieval from proof.** Retrieval tools find candidates; source
   files, tests, renders, or logs prove claims.
5. **Compress after decisions.** Keep only final facts, changed files, checks,
   and next tasks. Drop failed speculation unless it prevents repeating a trap.

## Large Codebase Workflow

1. Index or pack only the target repo, not the whole machine.
2. Ask a narrow query first, such as "where is routing trace converted to
   All-to-Allv bytes" rather than "explain the repo".
3. Read retrieved files directly and verify line-level behavior.
4. Edit only after the relevant ownership boundary is clear.
5. Update the handoff with paths and checks.

## Recommended Tools

- **Claude Context MCP**: hybrid semantic search over indexed codebases.
- **Repomix**: compact source bundle for another agent when MCP is unavailable.
- **GitNexus/Serena**: graph or symbol navigation for dependency questions.
- **Local Markdown handoff**: cheapest persistent memory.

## Claude Context Notes

Claude Context helps by indexing a codebase into Milvus/Zilliz and returning
only relevant chunks through MCP. It is useful for server-side code work. It is
not a replacement for tests, source inspection, or project rules.

Use it when:

- the repo is too large to inspect file-by-file,
- you need semantic lookup across unfamiliar code,
- multiple agents repeatedly ask the same codebase questions.

Avoid it when:

- the task is a one-file edit,
- secrets or private drafts would be indexed into an unapproved remote vector DB,
- MCP is unavailable and a simple `rg` is enough.

## Token Budget Checklist

- [ ] Did I use search/index before loading large files?
- [ ] Did I avoid pasting long source or article text into the response?
- [ ] Did I write a compact handoff for facts that will recur?
- [ ] Did I remove stale or duplicate context from the next prompt?
