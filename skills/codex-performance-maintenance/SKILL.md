---
name: codex-performance-maintenance
description: Diagnose and safely reduce Codex desktop slowness caused by oversized sessions, sqlite logs, temporary caches, stale worktrees, or long-running local processes on Windows. Use when Codex startup, rendering, typing, scrolling, or document/PDF checks become slow.
---

# Codex Performance Maintenance

Use this skill when Codex Desktop becomes slow to start, render, type, scroll,
or run local document checks. The goal is to reduce local state bloat without
damaging active sessions, settings, skills, plugins, or user work.

## Safety Rules

- Treat `~\.codex` as live application state. Do not delete files blindly.
- Never move `logs_2.sqlite`, `logs_2.sqlite-wal`, or `logs_2.sqlite-shm`
  while any Codex process is running.
- Never move a session rollout whose `LastWriteTime` is current or appears to
  belong to the active conversation.
- Prefer archiving over deletion. Keep a report and a restore path.
- If a thread is very large, create a compact handoff note and continue in a
  fresh thread instead of trying to keep the large chat as permanent memory.
- For document-heavy work, check WPS/Word and background dev-server processes;
  do not kill user-visible applications unless the user explicitly asks.

## Quick Workflow

1. Inspect `~\.codex\sessions`, `~\.codex\.tmp`, `logs_2.sqlite*`, and active
   Codex/WPS/Word/Node processes.
2. Archive old large session rollout files that are not active.
3. Create or update a project handoff note for the current task.
4. Run the bundled maintenance script in dry-run mode.
5. If Codex is still running, tell the user to close Codex before applying
   log rotation and cache moves.
6. After Codex is closed, run the script with `-Apply`.
7. Reopen Codex and verify that sqlite logs and temporary caches were recreated
   at small sizes.

## Commands

Use PowerShell on Windows. Run from any directory.

```powershell
$codexRoot = Join-Path $env:USERPROFILE ".codex"
Get-ChildItem -LiteralPath $codexRoot -Force | Select-Object Name,Mode,LastWriteTime
Get-ChildItem -LiteralPath (Join-Path $codexRoot "sessions") -Recurse -File -Force |
  Sort-Object Length -Descending |
  Select-Object -First 12 FullName,@{Name="MB";Expression={[math]::Round($_.Length/1MB,2)}},LastWriteTime
Get-Process | Where-Object { $_.ProcessName -match "codex|wps|WINWORD|node" } |
  Sort-Object CPU -Descending |
  Select-Object -First 20 ProcessName,Id,CPU,WorkingSet64
```

Run the bundled script in dry-run mode first:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".\scripts\codex_maintenance.ps1"
```

Run with `-Apply` only after Codex has fully exited:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".\scripts\codex_maintenance.ps1" -Apply
```

## Handoff Pattern

For long-running thesis, codebase, or document tasks, create a short handoff
file before leaving a large thread. Include:

- current goal and non-negotiable rules;
- latest working files and files to avoid;
- commands or scripts already run;
- checks that passed;
- remaining risks and next actions.

Start the next thread from that handoff file. Treat chats as execution context,
handoff files as working memory, and archives as history.

## What To Report

Report only high-signal facts:

- the repository or project path inspected;
- current sizes of sessions, `.tmp`, and `logs_2.sqlite*`;
- how much was archived and where it was moved;
- whether Codex was running during the check;
- the exact command to run after closing Codex;
- any remaining active large sessions that should be handled by a fresh thread.

