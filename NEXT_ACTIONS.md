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
| 6 | Create master promotion script | Assistant / GitHub connector | todo | `src/codemike/data/destination_master_promotion.py` |
| 7 | Generate master dataset | User / Termux | todo | `datasets/reference/destinations_master_v2.csv` |
| 8 | Validate master dataset | Assistant + User | todo | Add validator/report |
| 9 | Create master HTML browser | Assistant / GitHub connector | todo | GitHub Pages review layer |
| 10 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After master dataset exists |

## Current Blocking Item

```text
Master promotion script
```

The normalized backlog is clean and the master schema exists. The next blocker is creating:

```text
src/codemike/data/destination_master_promotion.py
```

It should generate:

```text
datasets/reference/destinations_master_v2.csv
reports/evidence/destination-master-v2-promotion-report.md
```

## Next Termux Command Block

No command yet. First create the promotion script.

After the script exists, expected command will be:

```bash
cd ~/projects/MSc
git pull
python src/codemike/data/destination_master_promotion.py
git status
git add datasets/reference/destinations_master_v2.csv reports/evidence/destination-master-v2-promotion-report.md
git commit -m "Generate destinations master v2 dataset"
git push
```

## Master Schema Summary

Created:

```text
datasets/reference/destinations_master_v2_schema.md
```

The master schema unifies:

- 134 seed rows
- 225 normalized candidate rows
- stable `DST2-*` IDs
- source lineage
- destination scale
- type/vibe/trip-style/context/caution fields
- promotion status
- verification status
- source confidence placeholders
- Planner-readiness placeholders

## Deferred Later Actions

| Action | Reason for deferral |
|---|---|
| Final PDF report | Better after master dataset and browser exist |
| Formal portfolio pack | Better after scoring module exists |
| PWA layer | Better after data model stabilises |
| Verified travel facts | Requires source verification workflow and possibly current web research |
