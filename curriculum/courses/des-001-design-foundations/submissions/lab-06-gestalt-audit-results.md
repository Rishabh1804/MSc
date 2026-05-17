# Lab 06 — Submission

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-06-gestalt-audit.md`
Source topic: `design/foundations/topic-06-gestalt.md`
Audit output: `design/foundations/topic-06-gestalt-audit.md`
Target artifact: Destination Master Browser v1.1 (post-PR #12) at `docs/destination-master-browser.html`

## Executive summary

Lab 06 ran a full Gestalt audit against v1.1, evaluating six screen regions (cards, table, toolbar, active-filter summary, banners stack, drawer) against the six core Gestalt principles (proximity, similarity, continuity, closure, common region, common fate). The audit produced a per-region per-principle verdict matrix, explicit conflict adjudication for four cross-principle conflicts, a density-vs-grouping audit, and a six-item prioritised v1.1.x / v1.2 fix list ordered by leverage.

**Overall verdict**: v1.1 is *Gestalt-substantial*. Two regions (banners stack + drawer) are exemplary; the other four have a small consistent pattern of findings, all closable with visual-treatment-only changes. Five of six fixes tag as v1.1.x; one tags as v1.2 (an optional grammar-unification deepening). No fix requires a Topic 2 component-rule change — the rule sheet already specifies the four-depth trust signal; the findings are *implementations* of an existing rule, not new rules.

The single most operationally important finding: **the trust badge is correctly elevated at four depths (banner, card top-right, drawer, confirm-modal) per the Topic 2 rule sheet, but the verification *text* is duplicated inside the card meta-grid and the table column at equivalent visual weight to non-trust fields, partially undoing the badge's elevation via similarity-collapse**. Fix #1 closes both occurrences with a single visual-treatment change.

## Steps executed

| Step | Output | File / section |
|---|---|---|
| 1 — Pick audit regions | Six regions selected with justification + four exclusions named | Audit doc §Step 1 |
| 2 — Per-region per-principle audit | 36 cells graded across six regions (22 Pass, 5 Trade-off, 7 Violation, 4 N/A) | Audit doc §Step 2 |
| 3 — Conflict adjudication | Four cross-principle conflicts adjudicated (R1 caution-chips; R3 view-toggle; R3 search-vs-selects; R4 summary-vs-toolbar); 0 left unresolved | Audit doc §Step 3 |
| 4 — Density-vs-grouping audit | Per-region density audit + audit-level meta-finding (F-GES-7) when substitution silently collapses | Audit doc §Step 4 |
| 5 — Findings + prioritised fix list | 6 distinct findings (F-GES-1..6) + 1 meta-finding (F-GES-7); 6-item leverage-ranked fix list (5 v1.1.x + 1 v1.2) | Audit doc §Step 5 |
| 6 — Master-browser checklist appendix | §29 + §30 + §31 appended to `master-browser-design-checklist.md` | Audit doc §Step 6 + checklist file |

## Key findings

### Region-level findings

- **F-GES-1 (R1 Cards, Similarity)**: "Verification" cell inside meta-grid uses the same styling as Scale/Region/Type cells around it — false-negative trust signal. Source: NN/g diagnostic discipline.
- **F-GES-2 (R2 Table, Similarity)**: "Verification" column (col 6) uses the same plain text styling as non-trust columns — same root cause as F-GES-1 at table scale across all 359 rows. Source: NN/g.
- **F-GES-3 (R2 Table, Similarity sub-audit)**: Sortable column headers don't visually signal interactivity; similarity to non-sortable headers creates false-negative interactivity grouping. Source: NN/g named-violation discipline.
- **F-GES-4 (R3 Toolbar, Proximity + Common region)**: View-toggle button-group is included in the toolbar's narrowing-controls common region despite being a different category (view-mode switch, not narrowing). Source: IxDF + NN/g.
- **F-GES-5 (R3 Toolbar, Similarity)**: Search input + filter selects share input-styling but have different interaction grammars (search live-updates; selects commit-on-change) — false-positive similarity grouping over interaction grammar. Source: NN/g + Smashing task-driven adjudication.
- **F-GES-6 (R4 Active-filter summary, Proximity + Common region)**: Summary bleeds into toolbar via proximity + weak tint differential despite similarity correctly separating chip styling. Source: IxDF.

### Audit-level meta-finding

- **F-GES-7 (Cross-cutting, Density-vs-grouping)**: Three of six regions (R3, R4, plus borderline R1) compromise on whitespace. R1's substitution is explicit (acceptable); R3's substitution over-groups (counts as F-GES-4 + F-GES-5); R4's substitution is too weak (counts as F-GES-6). The pattern is structural, not three isolated bugs. Source: Smashing density-vs-grouping framing + Topic 6 deep-reading doc §10 anti-pattern 1.

### Strengths

- **R5 (banner + header + stats stack)** — every principle Pass; no findings. Cleanest region in v1.1.
- **R6 (drawer)** — five Pass + one Trade-off with explicit closure-completion compensation.
- **R2 (table)** — proximity, continuity, closure, common region, common fate all Pass; only F-GES-2 (verification column) + F-GES-3 (sortable headers) are findings.
- **PR #12's result-count flash animation** — clean common-fate signal applied to both R2 and R4; meaningful motion used correctly (not decorative).
- **Trust-badge similarity across four depths** (banner → card top-right → drawer-trust → confirm-modal) — Gestalt-similarity working correctly across contexts; honours the Topic 2 four-depth trust signal specification.
- **Audit-shape itself** surfaced a cross-cutting pattern (verification false-negative at both card + table scale via similarity collapse) and a structural conflict (toolbar over-grouping) that introspection alone would have missed without the per-region per-principle matrix.

## Prioritised v1.1.x / v1.2 fix list

| # | Action | Closes | Tag |
|---:|---|---|---|
| 1 | Visually elevate verification signal in card meta-grid + table column (use trust-badge component or coloured tint instead of plain text) | F-GES-1 + F-GES-2 | v1.1.x |
| 2 | Visually separate toolbar's view-toggle from narrowing-controls (extra gap + optional vertical divider) | F-GES-4 | v1.1.x |
| 3 | Strengthen active-filter summary visual separation from toolbar (24px gap or stronger tint) | F-GES-6 | v1.1.x |
| 4 | Visually distinguish sortable column headers from non-sortable (icon, weight, hover affordance) | F-GES-3 | v1.1.x |
| 5a | Visually separate search from selects in toolbar | F-GES-5 (visual half) | v1.1.x |
| 5b | Unify search vs select grammar (selects live-update too) — defer to Sponsor Reviewer input | F-GES-5 (behaviour half) | v1.2 |
| 6 | Add small visual divider before caution chips in card-chips row | R1 caution-chip Trade-off → Pass upgrade | v1.1.x |

Items 1–4 + 5a + 6 close all six findings + upgrade one Trade-off at v1.1.x scope. Item 5b is the only v1.2-tagged work; it's optional pending real-reviewer feedback.

## Repository outputs

| Output | Path | Status |
|---|---|---|
| Full Gestalt audit (Steps 1–6 evidence) | `design/foundations/topic-06-gestalt-audit.md` | Complete |
| Lab submission (this file) | `submissions/lab-06-gestalt-audit-results.md` | Complete |
| Master-browser checklist Topic 6 gates + anti-patterns + canonical pointer | `design/checklists/master-browser-design-checklist.md` §29 + §30 + §31 | Complete |

## Submission checklist (per the lab brief)

- [x] Audit-region list with exclusion rationale (Step 1) — six regions audited, four excluded with one-line reasons
- [x] Per-region per-principle audit matrix (Step 2) — 36 cells across 6 regions × 6 principles
- [x] Conflict adjudication per region (Step 3) — four conflicts adjudicated, zero left unresolved
- [x] Density-vs-grouping audit (Step 4) — every region audited; F-GES-7 meta-finding captures the structural pattern
- [x] Findings + prioritised fix list (v1.1.x / v1.2 tags) (Step 5) — 6 findings; 6-item leverage-ranked list (5 v1.1.x + 1 v1.2 + 1 Trade-off upgrade)
- [x] Master-browser checklist Topic 6 section appended (Step 6) — §29 + §30 + §31

## Decision-gate satisfaction (per the lab brief)

The brief's gate (Lab 06 §"Decision gate before closing the lab"):

> Lab 06 is complete when:
> 1. Every chosen region has been audited against every relevant principle
> 2. Every Trade-off cell names a compensating signal
> 3. Every Violation has a fix in the prioritised list
> 4. Every conflict is adjudicated, not left unresolved
> 5. The prioritised fix list tags each item as v1.1.x or v1.2

All five conditions satisfied:

1. ✓ 6 regions × 6 principles = 36 cells; every relevant cell graded (4 N/A documented)
2. ✓ All 5 Trade-off cells name a compensating signal (R1 proximity → sub-section visual structure; R1 caution-chip → similarity colour wins; R3 common-region → soft tint with named over-grouping side-effect; R4 common-region → tint with named weakness; R6 closure → closure-completion across three borders)
3. ✓ All 6 distinct violations (F-GES-1..6) have a fix; the audit-level meta-finding F-GES-7 is closed by the fixes for its component findings
4. ✓ Four conflicts adjudicated (R1 caution-chip; R3 view-toggle; R3 search-vs-selects; R4 summary-vs-toolbar); zero left unresolved
5. ✓ Six-item prioritised list explicitly tags each as v1.1.x or v1.2

Decision-gate satisfied.

## What this lab produces beyond the rubric minimum

- A **Gestalt audit template** as a reusable workspace asset — region selection rules + per-principle matrix + conflict adjudication + density-vs-grouping audit + leverage-ranked fix list with v1.1.x / v1.2 tagging
- A **violation taxonomy** (false-positive grouping / false-negative grouping / unresolved principle conflict) as a diagnostic vocabulary applicable to any UI design review
- A **density-vs-grouping audit pattern** applicable to any information-dense interface, not just data-review tools
- A **leverage-scoring rubric** for prioritising fixes: (findings closed) × (journey steps served) × (cost-of-implementation inverse). Items 1–3 in the prioritised list demonstrate the scoring.
- A documented **cross-audit consistency check**: the four-depth trust signal from Topic 2 §6.2 is verified intact by the Lab 06 audit (Strengths list) — Topic 2 and Topic 6 cross-validate.

## Honest limitations (audit doc §"What this audit does NOT do")

- No human-grade perceptual testing — the Topic 6 analogue of Topic 5's Sponsor Reviewer gap
- No quantitative perceptual measurement (eye-tracking / attention-heat-maps)
- No motion-disabled audit (`prefers-reduced-motion: reduce` reviewers lose the common-fate signal)
- No mobile / narrow-viewport audit — desktop-shaped findings only
- No cross-version regression check against v1.0 (archived); future Audit 2 should compare against Audit 1

Naming these explicitly is HCD-compliant (Topic 5 §11 anti-pattern 1) and matches the Topic 6 discipline (deep-reading doc §10 — silent collapse is the failure mode; explicit naming is acceptable).

## Inheritance into v1.2

The v1.2 backlog now inherits work from three labs:

- Lab 04 Loop 1 (batch-promote-confirm modal anatomy + four U-CONF acceptance criteria)
- Lab 05 prioritised HCD list (6 items: Sponsor Reviewer + U-CONF landing + systems-context + inclusion requirements + screen-reader test + heuristic re-audit)
- **Lab 06 prioritised list (this submission)**: 5 v1.1.x items + 1 v1.2 grammar-unification item

The v1.2 implementation PR will need to sequence carefully across all three labs' worth of work. The Gestalt v1.1.x items can ship first (visual-treatment-only) without waiting for Sponsor Reviewer recruitment.

## Open work after Lab 06

- **End-of-Topic-6 closure** per the ratified three-topic push (Topics 4 → 5 → 6):
  1. Lyra + Aurelius graded reviews on this PR (PR B) — review-and-grade-only pattern per established protocol
  2. Merge PR A (Topic 6 reading) + PR B (this Lab 06)
  3. Catch up Aurelius governance debt accumulated across Topics 4 + 5 + 6 (SKILL_MAP, CAPABILITIES, PROJECT_LOG × 3 closure entries, NEXT_ACTIONS)
  4. **Grade report v3** at `feedback/DES-001-grade-report-v3.md` — cumulative DES-001 grade after Topics 1–6, including HCD compliance verdict (Topic 5) + Gestalt compliance verdict (Topic 6) + scope-incompleteness adjustment scaled down (6 of 12 topics now closed)
  5. **STOP** per ratified three-topic push goal

## Lab 06 status

**Complete.** Lab evidence is sufficient for Topic 6 to be marked Closed. PR B (this submission) closes Topic 6. After PR A + PR B merge, the three-topic push terminates with grade report v3 as the final closure deliverable.
