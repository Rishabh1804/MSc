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
| 1 | Pull latest repo in Termux | User / Termux | done | Completed for clean validation |
| 2 | Run normalized backlog validator | User / Termux | done | Clean report produced |
| 3 | Commit regenerated validation report | User / Termux | done | Clean validation pushed |
| 4 | Verify clean validation report from GitHub | Assistant / GitHub connector | done | Invalid counts are zero |
| 5 | Create master schema | Assistant / GitHub connector | done | `datasets/reference/destinations_master_v2_schema.md` |
| 6 | Create master promotion script | Assistant / GitHub connector | done | `src/codemike/data/destination_master_promotion.py` |
| 7 | Generate master dataset | User / Termux | done | `datasets/reference/destinations_master_v2.csv` generated and verified |
| 8 | Create master validation utility | Assistant / GitHub connector | done | `src/codemike/data/destination_master_validation.py` |
| 9 | Run master validation report | User / Termux | todo | Generate computed report |
| 10 | Create master HTML browser | Assistant / GitHub connector | todo | GitHub Pages review layer |
| 11 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After master browser exists |

## Current Blocking Item

```text
Run destination_master_validation.py in Termux
```

The master validation script now exists:

```text
src/codemike/data/destination_master_validation.py
```

It should generate:

```text
reports/evidence/destination-master-v2-validation-report.md
```

## Next Termux Command Block

Run:

```bash
cd ~/projects/MSc
git pull
python src/codemike/data/destination_master_validation.py
git status
git add reports/evidence/destination-master-v2-validation-report.md
git commit -m "Generate destinations master v2 validation report"
git push
```

Expected clean readiness:

```text
master_structurally_valid_not_planner_ready
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
