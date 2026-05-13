# NEXT_ACTIONS.md — CodeMike Operational Queue

This file tracks the current operational queue for CodeMike. It is intentionally practical and action-oriented.

## Status Legend

| Status | Meaning |
|---|---|
| `todo` | Not started |
| `doing` | In progress |
| `blocked` | Waiting on another step/tool/user action |
| `done` | Completed |
| `deferred` | Intentionally later |

## Immediate Actions

| Priority | Action | Owner/Mode | Status | Notes |
|---:|---|---|---|---|
| 1 | Pull latest repo in Termux | User / Termux | todo | Needed after seed compatibility cleanup |
| 2 | Run master validation report | User / Termux | todo | Regenerate computed report |
| 3 | Commit regenerated master validation report | User / Termux | todo | Should show clean structural readiness |
| 4 | Verify clean master validation from GitHub | Assistant / GitHub connector | todo | Confirm invalid counts are zero |
| 5 | Create master HTML browser | Assistant / GitHub connector | todo | GitHub Pages review layer |
| 6 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After master browser exists |

## Current Blocking Item

```text
Regenerate destination-master-v2-validation-report.md after seed compatibility cleanup
```

The master validator and tag dictionary now accept the legacy seed concepts that appeared in the original seed dataset.

## Next Termux Command Block

Run:

```bash
cd ~/projects/MSc
git pull
python src/codemike/data/destination_master_validation.py
git status
git add reports/evidence/destination-master-v2-validation-report.md
git commit -m "Regenerate clean destinations master v2 validation report"
git push
```

Expected clean readiness:

```text
master_structurally_valid_not_planner_ready
```

Expected invalid counts:

```text
Invalid location types: 0
Invalid vibe tags: 0
```

## Current Master Dataset Summary

Created:

```text
datasets/reference/destinations_master_v2.csv
reports/evidence/destination-master-v2-promotion-report.md
```

Promotion result:

```text
Seed rows read: 134
Normalized candidate rows read: 225
Master rows written: 359
Duplicate name-country keys flagged: 0
Duplicate name-state keys flagged: 0
```

## Deferred Later Actions

| Action | Reason for deferral |
|---|---|
| Final PDF report | Better after master dataset and browser exist |
| Formal portfolio pack | Better after scoring module exists |
| PWA layer | Better after data model stabilises |
| Verified travel facts | Requires source verification workflow and possibly current web research |
