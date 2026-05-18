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
| 8 | Browser v1.1.x polish PR — Lab 06 visual-treatment fixes | Assistant / CodeMike | **done** | All six v1.1.x fixes shipped in the v1.1.x polish PR: Fix #1 verif-pill (closes F-GES-1 + F-GES-2); Fix #2 view-toggle separator (F-GES-4); Fix #3 active-filter summary tint (F-GES-6); Fix #4 sortable-header ↕ glyph (F-GES-3); Fix #5a search-vs-selects separator (F-GES-5 visual half); Fix #6 caution-chip divider (R1 Trade-off → Pass). After-screenshots + computed leverage scores landed in `design/foundations/topic-06-gestalt-audit.md` audit addendum. Zero walk-through regression (19/19 pass). Fix #5b stays deferred to v1.2 (see priority 10). |
| 9 | Recruit Sponsor Reviewer for v1.2 | Rishabh / Assistant | doing | **Framework landed**: `design/foundations/sponsor-reviewer-brief.md` defines profile + 3-hour session shape (orient / two scoped tasks / structured debrief) + feedback-format + closure mapping. Rishabh decides recruitment source (internal network / Codex network / paid hire / self-as-Sponsor fallback). U-CONF-1..4 acceptance criteria now landed in `ux-acceptance-criteria.md` per the brief's evaluation targets — closes Lab 05 F-REQ-1. Open work: first recruitment ask + first session. |
| 10 | Browser v1.2 implementation PR (batch-promote-confirm subset) | Assistant / CodeMike | **done** (subset) | Lab 04 Loop 1 batch-promote-confirm modal shipped to `docs/destination-master-browser.html`. U-CONF-1..4 walkthrough 10/10 pass. v1.1 walkthrough 19/19 pass (zero regression). Transfer 3 recorded. Open: the other v1.2 inheritance items (Lab 05 systems-context-of-use doc + inclusion-lens requirements + Lab 06 Fix #5b grammar unification) remain *deferred* pending Sponsor Reviewer (priority 9) — they're not part of this PR's scope. |
| 11 | Audit 2 trigger — Gestalt + HCD re-audit after v1.2 ships | Assistant / Lyra | deferred | Per audit doc honest limitations: future Audit 2 should compare against Audit 1's findings to verify the v1.2 closures actually closed the v1.1 violations. Triggers after the v1.2 implementation PR ships. |
| 12 | F-MOB-2 mobile table layout — horizontal-scroll on narrow viewports | Assistant / CodeMike | deferred | The 8-column records table + new v1.2 select-checkbox column = 9 columns. On ~360px mobile viewports the table overflows horizontally; reviewer must scroll right to see what they're selecting then scroll left to find the batch action bar. Surfaced 2026-05-18 by real-device user screenshots. Structural fix is mobile-friendly table layout (collapsing-to-cards / horizontal-scroll-container with sticky first column / responsive column hide) — v2.x scope per Lab 05 inclusion-lens F-W3C-1 (device sub-dimension). Cosmetic workaround: switch to Cards view on mobile (no multi-select there). |
| 13 | F-MOB-5 mobile-viewport variant for capture-fixes.js / walkthrough scripts | Assistant / CodeMike | deferred | Provisional rule landed in `topic-06-gestalt-audit.md` Audit Addendum 2 + `operations/FAILURE_LOG.md` (Unicode-glyph failure): every visual-treatment change with a CSS-content-character OR position:absolute change gets a mobile-viewport screenshot before merge. Implementation: extend `verification/v1.1.x-polish/capture-fixes.js` with a `viewport=360x640` variant; same for future polish PRs. Defer until the next polish PR cycle is in scope. |
| 14 | DES-001 Topics 7–12 | Assistant / CodeMike | deferred | The remaining six DES-001 topics (Fitts' law / Button states / Typography / Color theory / Web design / grid layout / Design systems) per the execution plan. **Currently STOPPED per the ratified three-topic-push goal — do not start without an explicit user instruction.** |

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
