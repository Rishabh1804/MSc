# TRANSFER_LOG.md — CodeMike Transfer Log

This file records capability transfers from the MSc workspace into other projects.

## Transfer Principle

CodeMike is not finished when he learns something. CodeMike is finished when the skill can improve a real project.

## Transfer Protocol

1. Identify target project need.
2. Check `SKILL_MAP.md` and `CAPABILITIES.md`.
3. Build or validate the method in MSc.
4. Package the result as a pattern, module, or implementation note.
5. Apply it to the target project.
6. Record the transfer here.

## Transfer Entry Template

Entries use the form `### Transfer N — <source capability> → <target project>` so the register reads as a numbered sequence; the body covers the same eight fields as the original template.

```md
### Transfer N — <source capability> → <target project>

**Date:** YYYY-MM-DD

**Source capability:** which SKILL_MAP / CAPABILITIES rows are being transferred

**Target project:** the receiving project + one-line context

**Problem solved:** what gap in the target project the transfer closes

**Artifact transferred:** the concrete file / build / module that landed

**Evidence:** verification artifacts (test results, screenshots, PR links)

**Outcome:** what is true now that wasn't true before

**Limitations:** what this transfer does *not* cover; what is intentionally deferred

**Next action:** the smallest next step that this transfer unblocks
```

## Transfer Register

### Transfer 1 — DES-001 design discipline → Destination Master Browser v1.1

**Date:** 2026-05-16

**Source capability:** All six DES-001-derived design capabilities (CAPABILITIES.md rows promoted from maturity 3 → 4 as part of this transfer):
- Master-detail-with-faceted-search pattern card
- Nine-state interactive checklist
- Affordance-signifier-feedback triple-check
- Seven-step reviewer-journey template
- UX acceptance-criterion form
- User-need vs request vs solution-shape triage

Plus the workspace-level UI/UX design skill (SKILL_MAP.md, promoted level 4 → 5).

**Target project:** Destination Master Browser — internal QA review tool for the 359-row `destinations_master_v2.csv` reference dataset (the workspace's first applied data-review tool).

**Problem solved:** v1 was a card-only browser with no inspection, no recovery affordance, no sortable comparison, and only a shallow trust signal. Lab 01 identified the workflow + trust-preservation gap heuristically; Lab 02 + Lab 03 specified the gap at component-rule and acceptance-criterion levels. v1.1 implements the spec.

**Artifact transferred:**
- `docs/destination-master-browser.html` (canonical v1.1 build, ~1180 lines)
- v1 archived at `docs/destination-master-browser-v1.0.html` for historical evidence
- Two PRs landed (#10 — core implementation; this PR — polish + walk-through + governance promotion)

**Evidence:**
- `curriculum/courses/des-001-design-foundations/verification/v1.1-core/` — PR A Playwright smoke-test screenshots (26/26 checks)
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/` — full 13-gate walk-through (15/15 pass including the cross-cutting CONSOLE check) + four screenshots (table / cards / empty / drawer) + raw JSON results + the verification report itself
- `design/foundations/ui-design-component-rules.md` — the component rule sheet implemented
- `design/foundations/ux-acceptance-criteria.md` — the UX acceptance-criteria sheet whose 13 gates were verified
- Lyra + Aurelius PR-review evidence on PRs #10 and (this PR)

**Outcome:**
- Every one of the 13 v1.1 UX gates passes the Playwright walk-through.
- All seven reviewer-journey steps move from PARTIAL/FAIL (in v1) to PASS (in v1.1).
- All 11 Lab 01 findings tracked in the Lab 03 gap analysis are closed.
- All five Lyra observations on PR #10 (ARIA describedby, focus restoration, count-flash animation, CSV URL override, taxonomy-drift warn) are addressed in this PR.
- Zero console errors / pageerrors / requestfailed during the full walk-through.
- The Destination Master Browser is no longer "structurally valid but not Planner-ready" *and* "design-foundationless". It is now structurally valid + design-foundation-grounded.

**Limitations:**
- Production GitHub Pages render not yet verified — operational check (NEXT_ACTIONS.md priority 3), separate from this transfer.
- Trust-badge colour palette uses neutral colours; the dedicated accessible palette comes from Topic 10 (Color theory), deferred to a future Browser v1.2.
- Confirm-modal for destructive batch actions is intentionally deferred to v1.2+ (no destructive actions in v1.1 scope, per the rule sheet's modality rule).
- Faceted filter panel is intentionally deferred to v1.2 if reviewer feedback shows the chip-row + dropdown combination is insufficient.
- The CSV-fetch URL hits `raw.githubusercontent.com` by default; the `?csv=` query-param override (added in this PR) supports staging / offline workflows without code changes.

**Next action:**
1. Mark `NEXT_ACTIONS.md` priority 4 as `done` (this PR closes it).
2. User to verify the production GitHub Pages render (priority 3) when convenient.
3. Start DES-001 Topic 4 (Design thinking) per the ratified execution plan §3.
4. When 3–4 more design transfers accumulate, promote the six capabilities from register rows to formal capability cards under `capabilities/` (template at the bottom of `operations/CAPABILITIES.md`).

### Transfer 2 — DES-001 Lab 06 Gestalt audit → Browser v1.1.x polish PR

**Date:** 2026-05-17

**Source capability:** All five DES-001 Topics 4 + 5 + 6 audit-derived capabilities (CAPABILITIES.md rows added at maturity 4 as part of the three-topic-push closure):
- Gestalt audit template (Steps 1–6)
- Gestalt violation taxonomy (false-positive / false-negative / unresolved conflict)
- Density-vs-grouping audit pattern
- HCD audit template (Steps 1–7)
- HCD self-audit gate (four cells)

Plus the workspace-level design-discipline meta-skill (SKILL_MAP.md row added).

**Target project:** Destination Master Browser v1.1.x polish — the next implementation cycle on `docs/destination-master-browser.html`, scoped to the Lab 06 prioritised v1.1.x fix list (visual-treatment-only changes that close 6 Gestalt findings without changing component rules).

**Problem solved:** v1.1 ships with 6 Gestalt findings (F-GES-1..6) the Lab 06 audit surfaced. Five of the six fixes are visual-treatment-only (v1.1.x scope); they close findings whose root causes the audit-shape made visible (silarity-collapse around the verification text; toolbar over-grouping; active-filter summary bleed; sortable-header affordance; search-vs-select grammar separation). The transfer is the audit's prioritised fix list moving from `design/foundations/topic-06-gestalt-audit.md` into the next polish PR's scope.

**Artifact transferred (planned):**
- `docs/destination-master-browser.html` (v1.1.x build — updated visual treatment on six regions)
- Per-fix before/after screenshots attached to `design/foundations/topic-06-gestalt-audit.md` retroactively (per Lyra missed-opportunity on PR #18)
- Anticipated leverage scores computed per fix (per Lyra missed-opportunity)

**Evidence (to be produced by the polish PR):**
- Lab 06 prioritised fix list as the input
- Updated `docs/destination-master-browser.html` with the six visual-treatment changes
- Annotated before/after screenshots in the audit doc
- v1.1.x walk-through re-verified (existing 19-gate Playwright walk-through should continue to pass; no regression)

**Outcome (planned):**
- All 6 Gestalt findings closed at v1.1.x scope (F-GES-1 + F-GES-2 closed by Fix #1; F-GES-3 by Fix #4; F-GES-4 by Fix #2; F-GES-5 visual half by Fix #5a; F-GES-6 by Fix #3)
- R1 caution-chip Trade-off upgraded to Pass by Fix #6
- Audit doc gains empirical (screenshot) grounding
- Fix #5b grammar-unification deferred to v1.2 pending Sponsor Reviewer input

**Limitations:**
- The polish PR is not yet started; this entry pre-records the transfer per the Aurelius missed-opportunity that flagged Lab-06-fix-list-as-transfer-payload as a missed governance step
- Fix #5b stays in v1.2 scope and is *not* part of this transfer
- Audit 2 trigger (NEXT_ACTIONS priority 11) is the verification step that closes this transfer after v1.2 ships

**Next action:**
1. Start the v1.1.x polish PR (NEXT_ACTIONS priority 8) implementing the six fixes
2. Capture before/after screenshots per fix as evidence
3. Attach screenshots + computed leverage scores to the audit doc retroactively
4. Re-verify the existing 19-gate walk-through (no regression)
5. Update this Transfer 2 entry's "Outcome" section with the actual results once shipped

**Outcome (shipped 2026-05-18):**

All six fixes shipped in the v1.1.x polish PR. Visual-treatment-only — zero behavioural changes. 19/19 walk-through pass on polished build (no regression). All six Gestalt findings (F-GES-1 through F-GES-6) closed at v1.1.x scope except F-GES-5's behaviour half (Fix #5b, deferred to v1.2 pending Sponsor Reviewer). R1 caution-chip Trade-off upgraded to Pass via the divider (Fix #6). Audit doc now has empirical (screenshot) grounding via the addendum's five after-screenshots + computed leverage scores per fix. Lyra missed-opportunities from PR #18 (no screenshots; no leverage scores) both closed.
