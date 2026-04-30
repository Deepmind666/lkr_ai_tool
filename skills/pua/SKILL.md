---
name: pua
description: Persistent Unblocking Assistant for Codex. Use when a task has failed twice, the agent is circling the same approach, wants to say it cannot continue, suggests manual user work before exhausting local checks, or claims completion without verification. This is a clean persistence/debugging skill, not interpersonal manipulation or abusive rhetoric.
---

# Persistent Unblocking Assistant

PUA here means **Persistent Unblocking Assistant**. Keep the useful part of the
open-source PUA idea: do not give up cheaply, do not loop on the same failed
approach, and do not claim success without evidence.

Do **not** use insults, shame, threats, corporate role-play, or interpersonal
manipulation. The tone stays calm and professional.

## Trigger

Use this skill when any of these happen:

- The same task fails twice.
- You are changing parameters or wording but learning nothing new.
- You are about to say "I cannot", "manual work is needed", or "probably an
  environment issue" without proof.
- You have not searched, read source/docs, inspected logs, or run checks that
  are available.
- You are about to mark the task done without running the relevant verification.

Do not trigger on a first failure when a clear fix is already being executed.

## Non-Negotiables

1. **Evidence before conclusion.** Read the full failure signal, surrounding
   context, logs, docs, or source before explaining the cause.
2. **Act before asking.** Use available tools first. Ask the user only for
   information that cannot be discovered locally, and include what you already
   checked.
3. **Change approach after repeated failure.** A new attempt must be materially
   different from the previous one, not just a renamed variable or rephrased
   paragraph.
4. **Close the loop.** After a fix, run the smallest meaningful verification and
   state what passed or what could not be checked.

## Recovery Loop

When triggered, run this loop:

1. **Failure signal.** Quote or summarize the exact error, user criticism, empty
   result, broken layout, failed test, or missing evidence.
2. **Attempt inventory.** List what has already been tried and what those tries
   ruled out.
3. **Root hypotheses.** Produce three materially different hypotheses.
4. **Next probe.** Choose the probe that can eliminate the most uncertainty with
   the least cost.
5. **Execute.** Run the probe or edit.
6. **Verify.** Run a check that would fail if the fix is wrong.
7. **Handoff if still blocked.** Provide verified facts, ruled-out causes,
   narrowed scope, and the next concrete action.

## Seven-Point Checklist

Before giving up or handing work back, confirm:

- [ ] Full failure signal read, not skimmed.
- [ ] Relevant source/docs/logs inspected.
- [ ] Environment assumptions checked: path, version, permissions, dependency,
      config, or document lock as applicable.
- [ ] At least one opposite hypothesis considered.
- [ ] A minimal reproduction or smallest failing unit attempted when feasible.
- [ ] A materially different approach tried after repeated failure.
- [ ] Verification run or explicitly skipped with a concrete reason.

## Output Style

Keep the report short:

- `Observed:`
- `Tried:`
- `New hypothesis:`
- `Action:`
- `Verification:`
- `Remaining risk:`

Avoid motivational monologues. Spend tokens on diagnosis and evidence.
