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
| 2 | Create master HTML browser | Assistant / GitHub connector | done | `docs/destination-master-browser-v1.html` |
| 3 | Verify GitHub Pages browser | User / Browser | todo | Open Pages URL after deployment delay |
| 4 | **Implement Destination Master Browser v1.1** | Assistant / CodeMike | **todo** | DES-001 Topic 2 component rule sheet (`design/foundations/ui-design-component-rules.md`) + Topic 3 UX acceptance-criteria sheet (`design/foundations/ux-acceptance-criteria.md`) + master-browser checklist §3 + §18 + §20. All gates signed off in DES-001 grade report v2. |
| 5 | Design master enrichment strategy | Assistant / GitHub connector | todo | Define fields and rules before scoring |
| 6 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After enrichment strategy exists |

## Current Blocking Item

```text
Verify destination-master-browser-v1.html on GitHub Pages
```

Open:

```text
https://rishabh1804.github.io/MSc/destination-master-browser-v1.html
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
docs/destination-master-browser-v1.html
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
