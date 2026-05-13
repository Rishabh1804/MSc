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
| 1 | Pull latest repo in Termux | User / Termux | todo | Needed after taxonomy cleanup commits |
| 2 | Run normalized backlog validator | User / Termux | todo | `python src/codemike/data/destination_normalized_validation.py` |
| 3 | Commit regenerated validation report | User / Termux | todo | Expected clean result after taxonomy update |
| 4 | Verify clean validation report from GitHub | Assistant / GitHub connector | todo | Confirm invalid counts are zero |
| 5 | Create master schema | Assistant / GitHub connector | todo | `datasets/reference/destinations_master_v2_schema.md` |
| 6 | Create master promotion script | Assistant / GitHub connector | todo | `src/codemike/data/destination_master_promotion.py` |
| 7 | Generate master dataset | User / Termux | todo | `datasets/reference/destinations_master_v2.csv` |
| 8 | Validate master dataset | Assistant + User | todo | Add validator/report |
| 9 | Create master HTML browser | Assistant / GitHub connector | todo | GitHub Pages review layer |
| 10 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After master dataset exists |

## Current Blocking Item

```text
Clean normalized backlog validation report
```

The taxonomy and validator have been updated to accept the final six concepts:

```text
culture_town
lake_hill_station
mountain_resort
monastery
rain
rock_carving
```

A rerun should produce:

```text
Invalid normalized destination types: 0
Invalid normalized vibe tags: 0
Readiness: clean_enough_for_master_promotion_design
```

## Termux Command Block

Run from repo root:

```bash
cd ~/projects/MSc
git pull
python src/codemike/data/destination_normalized_validation.py
git status
git add reports/evidence/destination-normalized-backlog-validation-v1.md
git commit -m "Regenerate clean normalized destination backlog validation report"
git push
```

If `git commit` says there is nothing to commit, run `git push` anyway and report the output.

## Next Design Step After Clean Validation

Create:

```text
datasets/reference/destinations_master_v2_schema.md
```

The master schema should unify:

- 134 seed rows
- 225 normalized candidate rows
- stable destination IDs
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
