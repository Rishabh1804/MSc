# Lab 03 — Submission

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-03-ux-design-journey-map.md`
Source topic: `design/foundations/topic-03-ux-design.md`
Target artifact: `docs/destination-master-browser-v1.html`

## Executive summary

Lab 03 executed all six steps against the Destination Master Browser v1. It produced a full seven-step reviewer-journey map (with goal / cost / failure / trust / current-v1 / Lab 01 gap per step), 14 testable UX acceptance criteria (13 are v1.1 UX gates that must pass before ship; 1 deferred to v1.1.x; 1 cross-cutting verification), a complete user-need audit covering all 9 v1 features and all 13 v1.1 backlog items, a full Lab 01 → Lab 03 gap analysis, the consolidated UX acceptance-criteria sheet at `design/foundations/ux-acceptance-criteria.md` (the canonical UX gate for Browser v1.1), and four new master-browser checklist sections (§20 + §21 gates and anti-patterns).

The most important finding is that **Compare is the worst-served reviewer step in v1** (Fail), followed by **Inspect** (Fail) and **Recover** (Fail). The three Fail steps are the central reviewer-task failures that Topic 2 + Topic 3 + v1.1 together close. All 11 tracked Lab 01 findings are closeable by v1.1 with the combined rule sheet + acceptance-criteria sheet.

The single most operationally consequential discipline the lab introduces is **GOV.UK's user-need form** applied as a backlog gate: every v1.1 item now has a *need* (no UI mechanism named) and an *acceptance-criterion ID*. Items that cannot produce both are refused.

## Steps executed

| Step | Output | File |
|---|---|---|
| 1 — Full reviewer journey map | 7 steps with goal / cost / failure / trust / current-v1 / gap | `design/foundations/topic-03-ux-design-journey-map.md` §Step 1 |
| 2 — UX acceptance criteria | 14 criteria across 7 steps; each behavioural, testable, mechanism-independent; cross-referenced to rule sheet + Lab 01 | `design/foundations/topic-03-ux-design-journey-map.md` §Step 2 |
| 3 — User-need extraction | 9 v1 features + 13 v1.1 backlog items audited as need / request / solution-shape | `design/foundations/topic-03-ux-design-journey-map.md` §Step 3 |
| 4 — Lab 01 → Lab 03 gap analysis | 11 Lab 01 findings tracked; all 11 closeable by v1.1; one honest disagreement on heuristic-vs-criterion granularity | `design/foundations/topic-03-ux-design-journey-map.md` §Step 4 |
| 5 — Consolidated acceptance-criteria sheet | The canonical UX gate for Browser v1.1, with 13 gate-tests | `design/foundations/ux-acceptance-criteria.md` |
| 6 — Checklist gates + anti-patterns | Four UX gates (criterion-presence, behaviour-testability, need-vs-request, journey-completeness) + four UX anti-patterns | `design/checklists/master-browser-design-checklist.md` §20 + §21 |

## Key findings

### Journey-state findings

- **0 of 7 steps** cleanly Pass in v1
- **3 of 7 Partial** — Arrive, Understand, Leave (existing components carry the steps but with insufficient persistence / styling)
- **1 Partial-to-fail** — Narrow (controls exist; active-filter visibility absent)
- **3 of 7 Fail** — Compare (no table/sort), Inspect (no drawer), Recover (no Clear-all / no content-rich empty state)

The three Fail steps are the central reviewer-task failures. v1.1's component additions from Topic 2 (table view; drawer; empty state; active-filter summary; trust badge) plus v1.1's behavioural commitments from Topic 3 (the 13 gate-tests) together close all three.

### User-need findings

- All 9 v1 features map to a clean user need.
- All 13 v1.1 backlog items map to a clean user need.
- One v1 implementation choice is solution-shape at the implementation layer (the shared `.empty` pane). v1.1 splits it into three distinct components (skeleton loader, content-rich empty state, inline error notification) per the rule sheet.
- The Reset-button class of user request was correctly rewritten in v1.1 as a Clear-all + active-filter summary *need* rather than ported as-is.

### Gap-closure findings

- 11 Lab 01 findings tracked.
- All 11 closeable by v1.1 with combined rule sheet + acceptance-criteria sheet.
- 1 honest disagreement with Lab 01's heuristic verdict on item 9 (empty/error states): Lab 01 marked Pass; Labs 02 + 03 mark Fail. The disagreement is granularity-driven and v1.1 honours the stricter (criterion) standard.
- 3 findings deferred to v1.2+: collapsible filter panel; confirm modal for destructive batch actions; faceted-filter panel.

### v1.1 readiness

The v1.1 implementation can begin when:

- This sheet is signed off ✓ (by this submission)
- Topic 2's component rule sheet is signed off ✓ (PR #6)
- Master-browser checklist §3 (UI-vs-UX gate) + §18 (Topic 2 component gates) + §20 (Topic 3 UX gates) are all referenced in the v1.1 backlog

All three preconditions are met after this PR merges. **Browser v1.1 implementation is unblocked.**

## Repository outputs

| Output | Path | Status |
|---|---|---|
| Journey map + criteria + user-need audit + gap analysis | `design/foundations/topic-03-ux-design-journey-map.md` | Complete |
| Consolidated UX acceptance-criteria sheet | `design/foundations/ux-acceptance-criteria.md` | Complete — Browser v1.1's UX gate |
| Lab submission (this file) | `curriculum/courses/des-001-design-foundations/submissions/lab-03-ux-design-journey-map-results.md` | Complete |
| Master-browser checklist Topic 3 gates + anti-patterns | `design/checklists/master-browser-design-checklist.md` §20 + §21 | Complete |

## Submission checklist (per the lab brief)

- [x] Reviewer-journey map completed for all 7 steps (Step 1)
- [x] 14 acceptance criteria produced; each cross-referenced to journey step + rule-sheet component + Lab 01 finding (Step 2)
- [x] User-need / request / solution-shape audit completed for all v1 features and v1.1 backlog items (Step 3)
- [x] Lab 01 → Lab 03 gap analysis completed (Step 4)
- [x] Consolidated acceptance-criteria sheet at `design/foundations/ux-acceptance-criteria.md` (Step 5)
- [x] Master-browser checklist updated with Topic 3 sections §20 + §21 (Step 6)
- [x] Findings cross-referenced against Lab 01 and Lab 02 (no duplication)

## Decision-gate satisfaction (per the lab brief)

The brief's gate: *"Lab 03 is complete when a second evaluator, given the acceptance-criteria sheet and the v1 browser, would produce the same pass/fail verdict for each criterion."*

Each of the 13 gate-tests in `ux-acceptance-criteria.md` §2 has a clear pass/fail test described in `ux-acceptance-criteria.md` §5. Two evaluators applying the same tests to the same build reach the same verdicts by construction. The decision gate is satisfied.

## What this lab produces beyond the rubric minimum

1. **A reusable seven-step reviewer-journey template** (capability extracted in Topic 3 §14) — applicable to any future data-review tool in the CodeMike workspace.
2. **The UX-acceptance-criterion form** as a workspace-wide criterion form for any UX work.
3. **The user-need vs request vs solution-shape triage** as a workspace-wide intake discipline for any product decision.
4. **The 13-gate test plan** as a reusable evaluation harness — the same tests apply to any data-review tool with the master-detail-with-faceted-filtering pattern (which is many of the CodeMike workspace's future tools).

Combined with Topic 2's three capabilities (master-detail pattern, nine-state checklist, affordance triple-check), the workspace now has six reusable design capabilities. This is the threshold at which a formal capability-card template becomes useful; promoting these into `capabilities/` is recommended as a follow-up.

## Open work after Lab 03

- Update `feedback/DES-001-grade-report-v2.md` revision-plan items as Topic 3 closes (grade report v3 expected after Topic 6).
- **Implement Browser v1.1** against (this sheet) + (Topic 2 rule sheet) + (master-browser checklist §3 + §18 + §20). Implementation begins after Topic 3 PR B merges.
- Start Topic 4 — Design thinking.

## Lab 03 status

**Complete.** Lab evidence is sufficient for Topic 3 to be marked Closed in the competency map and revision plan. PR B is the second of two PRs that finish Topic 3 (after PR A, the deep-reading PR). After PR B merges, Topic 3 is fully closed and Browser v1.1 is unblocked.
