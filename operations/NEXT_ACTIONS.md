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
| 1 | Master validation report clean | User + Assistant | done | `master_structurally_valid_not_planner_ready` |
| 2 | Create master HTML browser | Assistant / GitHub connector | done | `docs/destination-master-browser.html` |
| 3 | Verify GitHub Pages browser | User / Browser | todo | Open Pages URL after deployment delay |
| 4 | **Implement Destination Master Browser v1.1** | Assistant / CodeMike | **doing** | Core implementation landed at `docs/destination-master-browser.html` (canonical); v1 archived to `docs/destination-master-browser-v1.0.html`. Playwright smoke test passes 26/26 checks. Full 13-gate walk-through verification + screenshots + TRANSFER_LOG entry pending in PR B (polish + verification). |
| 5 | Design master enrichment strategy | Assistant / GitHub connector | todo | Define fields and rules before scoring |
| 6 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After enrichment strategy exists |

## Current Blocking Item

```text
Verify destination-master-browser.html on GitHub Pages
```

Open:

```text
https://rishabh1804.github.io/MSc/destination-master-browser.html
```

Also available from:

```text
https://rishabh1804.github.io/MSc/
```

## Current Master Dataset Summary

Created:

```text
datasets/reference/destinations_master_v2.csv
reports/evidence/destination-master-v2-promotion-report.md
reports/evidence/destination-master-v2-validation-report.md
docs/destination-master-browser.html
```

Master validation:

```text
Rows checked: 359
Invalid location types: 0
Invalid vibe tags: 0
Readiness: master_structurally_valid_not_planner_ready
```

## Next Design Step

Create a master enrichment strategy before scoring:

```text
datasets/reference/destination_master_enrichment_strategy.md
```

It should define:

- enrichment fields
- origin-fit dimensions
- infant/family suitability dimensions
- travel fatigue dimensions
- planning complexity dimensions
- medical access confidence
- verification/source requirements
- manual-review rules
- what remains blocked from Planner-ready status

## Deferred Later Actions

| Action | Reason for deferral |
|---|---|
| Final PDF report | Better after master browser and enrichment strategy exist |
| Formal portfolio pack | Better after scoring module exists |
| PWA layer | Better after data model stabilises |
| Verified travel facts | Requires source verification workflow and possibly current web research |
