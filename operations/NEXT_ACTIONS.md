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
| 3 | Verify v1.1 GitHub Pages render at canonical URL | User / Browser | todo | Open `https://rishabh1804.github.io/MSc/destination-master-browser.html` after deployment delay. Then verify the v1.0 archive renders at `…/destination-master-browser-v1.0.html`. Both URLs were updated 2026-05-16 by the v1.1 ship. |
| 4 | Implement Destination Master Browser v1.1 | Assistant / CodeMike | **done** | Landed across two PRs (#10 core + this PR polish/walk-through). Canonical at `docs/destination-master-browser.html`; v1 archived at `-v1.0.html`. Full 13-gate Playwright walk-through: **15/15 pass** with zero console errors. Capability transfer recorded in `operations/TRANSFER_LOG.md` (Transfer 1); SKILL_MAP UI/UX skill promoted to level 5; six CAPABILITIES rows promoted to maturity 4. |
| 5 | Design master enrichment strategy | Assistant / GitHub connector | todo | Define fields and rules before scoring |
| 6 | Start destination scoring v1 | Assistant / GitHub connector | deferred | After enrichment strategy exists |
| 7 | DES-001 grade report v3 | Assistant / CodeMike | doing | Cumulative DES-001 grade after Topics 1–6 (the three-topic push closure). Lives at `feedback/DES-001-grade-report-v3.md`. Includes HCD compliance verdict from Topic 5 + Gestalt compliance verdict from Topic 6 + scope-incompleteness adjustment scaled down from −6 toward 0 as 6/12 topics now closed. Ships in this same PR. |
| 8 | Browser v1.1.x polish PR — Lab 06 visual-treatment fixes | Assistant / CodeMike | todo | Five v1.1.x fixes from Lab 06 prioritised list: (1) elevate verification signal in card meta-grid + table column [closes F-GES-1 + F-GES-2]; (2) separate view-toggle from narrowing-controls [F-GES-4]; (3) strengthen active-filter summary separation [F-GES-6]; (4) distinguish sortable column headers [F-GES-3]; (5a) separate search from selects [F-GES-5 visual half]. Plus the caution-chip divider Trade-off → Pass upgrade. Capture before/after screenshots for each fix and attach them to `design/foundations/topic-06-gestalt-audit.md` retroactively (per Lyra missed-opportunity on PR #18). |
| 9 | Recruit Sponsor Reviewer for v1.2 | User / Assistant | todo | Closes Lab 05 F-PRIN-1 + F-EVAL-1 + Lab 06 Fix #5b grammar-unification deferral. Two labs depend on a person who isn't yet recruited. Track here so the dependency is visible. |
| 10 | Browser v1.2 implementation PR | Assistant / CodeMike | deferred | Inherits three labs' worth of work: Lab 04 Loop 1 (batch-promote-confirm modal anatomy + four U-CONF acceptance criteria); Lab 05 prioritised HCD list (6 items led by Sponsor Reviewer recruitment + systems-context + inclusion requirements); Lab 06 Fix #5b (search-vs-select grammar unification pending Sponsor Reviewer input). Sequence carefully across the three labs. |
| 11 | Audit 2 trigger — Gestalt + HCD re-audit after v1.2 ships | Assistant / Lyra | deferred | Per audit doc honest limitations: future Audit 2 should compare against Audit 1's findings to verify the v1.2 closures actually closed the v1.1 violations. Triggers after the v1.2 implementation PR ships. |
| 12 | DES-001 Topics 7–12 | Assistant / CodeMike | deferred | The remaining six DES-001 topics (Fitts' law / Button states / Typography / Color theory / Web design / grid layout / Design systems) per the execution plan. **Currently STOPPED per the ratified three-topic-push goal — do not start without an explicit user instruction.** |

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
