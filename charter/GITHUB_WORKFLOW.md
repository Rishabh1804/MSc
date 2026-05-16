# GitHub Workflow Standard

This file defines how to reduce GitHub confirmation friction and keep history readable.

## Problem

Using one GitHub connector write per file creates too many confirmation prompts, too many small commits, and a messy project history.

## Standard workflow

Use one phase-level batch commit whenever possible.

Examples:

| Work type | Preferred commit style |
|---|---|
| Add a course skeleton | One commit with all course skeleton files |
| Execute a lab | One commit with result file + submission update + tracker updates |
| Grade an assignment | One commit with grade report + revision plan + tracker updates |
| Refactor dashboard modules | One commit or one PR with all related file changes |

## Preferred change unit

A commit should represent a meaningful academic or project step, not a single file.

Good commit examples:

```text
DES-001: execute Lab 01 browser audit
DES-001: grade Topic 1 milestone
Repo: add structure and workflow standards
```

Weak commit examples:

```text
Add README
Update README
Add another file
Fix link
```

## Reducing confirmation prompts

For future repository writes:

1. Plan the full phase first.
2. Bundle related file changes into one batch operation where possible.
3. Use a branch and pull request for larger refactors.
4. Keep generated output separate from source files.
5. Avoid exploratory writes; inspect first, then write once.

## Branch rule

For risky changes, use a branch:

```text
chore/repo-structure-cleanup
course/des-001-topic-02
feature/destination-browser-v1-1
```

Then open a PR instead of writing directly to `main`.

## Current recommendation

Use `main` for small course evidence updates. Use branches/PRs for:

- moving files
- deleting files
- replacing dashboard architecture
- large browser implementation changes
- changing repository structure

## Confirmation reality

The ChatGPT GitHub connector may still ask for confirmation for write operations. The best way to reduce friction is not to eliminate confirmation entirely, but to reduce the number of write operations by batching related changes into fewer commits.
