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

### Transfer 3 — DES-001 Lab 04 Loop 1 → Browser v1.2 batch-promote-confirm modal

**Date:** 2026-05-18

**Source capability:** All five DES-001-derived Topics 4 / 5 / 6 audit-and-loop capabilities now applied to a real implementation (CAPABILITIES.md rows at maturity 4):
- Design-thinking loop template (8-step) — Lab 04 Loop 1 worked example
- Three-constraint triage frame — Candidate B chosen via comparative reasoning
- UX acceptance-criterion form — U-CONF-1..4 landed in `ux-acceptance-criteria.md` by the Sponsor Reviewer framework PR
- Master-detail-with-faceted-search pattern card — modal is the right container per Topic 2 §3.5
- Trust-signal four-depth specification — confirm-modal adds the 4th depth (banner + drawer + card + **confirm-modal**)

**Target project:** Destination Master Browser v1.2 — adds the batch-promote feature against the v1.1 reference dataset. First Topic-4-loop output to ship as a real implementation. Implements the modal anatomy specified at `design/foundations/topic-04-design-thinking-loop.md` §6 + §State machine.

**Problem solved:** v1.1 ships read-only (browse, filter, inspect). The reviewer cannot act on the data within the tool. Lab 04 Loop 1 specified the *first* destructive action — batch-promote-to-Planner — with a two-stage confirm modal that honours the asymmetric-cost framing (cost of wrong promotion >> cost of cancelling). v1.2 implements that spec.

**Artifact transferred:**
- `docs/destination-master-browser.html` — v1.2 batch-promote-confirm feature added (table select column + select-all-visible + batch action bar + confirm modal + success toast + state management for selected and promoted ids)
- Per-criterion walkthrough at `curriculum/courses/des-001-design-foundations/verification/v1.2-walkthrough/walkthrough-conf.js` (10/10 pass on U-CONF-1..4 + setup + confirm-path + console)
- Verification report at `.../v1.2-walkthrough/v1.2-walkthrough-verification-2026-05-18.md` (per-criterion verdict table; implementation notes; state-machine compliance; honest limitations)
- Modal-open + modal-after-confirm screenshots (`walkthrough-modal-open.png`, `walkthrough-modal-after-confirm.png`)

**Evidence:**
- **U-CONF-1**: modal title reflects count ("Confirm: promote 3 records to Planner"); list shows record names + IDs; overflow handled for N > 25 (tested in code; walkthrough tested with N=3)
- **U-CONF-2**: Cancel default-focused; Esc cancels; overlay-click cancels; all three paths single-interaction (verified by walkthrough)
- **U-CONF-3**: `role="dialog"` + `aria-modal="true"` + `aria-labelledby` + `aria-describedby` (verified)
- **U-CONF-4**: focus trap cycles between Cancel and Confirm only; focus restoration to the batch-promote button on close (verified)
- **v1.1 regression check**: 19/19 walk-through pass — zero behaviour regression from the v1.2 additions
- **Console**: zero errors / pageerrors / requestfailed across the full v1.2 walkthrough

**Outcome:**
- The first Topic-4-loop output has shipped as a real implementation (Loop 1 → real code → walkthrough-verified)
- v1.2 has its first destructive action with the safety affordances Lab 04 Loop 1's asymmetric-cost framing requires (two-stage confirm; default-focused cancel; multiple cancel paths; in-flight protection via disabled-confirm)
- The trust-signal four-depth specification (Topic 2 §6.2) now has all four depths shipped: banner + drawer + card + confirm-modal
- The Topic 4 loop discipline (design-thinking-loop → user-need form → triage → prototype-spec → test-spec → real implementation → walkthrough) is now demonstrably end-to-end. Future loops can follow the same pattern.

**Limitations:**
- **No real Planner backend.** The promotion is session-scoped (in-memory state change). A real backend integration is a separate scope item; the current implementation is a *behaviour test* for the modal anatomy, not a production promotion path.
- **Screen-reader actual usability untested.** ARIA attributes are present and walkthrough-verified, but Sponsor Reviewer's accessibility-need persona is the only test that confirms the announcements are useful. Queued for first Sponsor Reviewer session per the brief.
- **N > 25 overflow path code-tested only.** Walkthrough used N=3.
- **No error state in the modal state machine.** Lab 04 §State machine specifies `done | error` as the third state; v1.2's implementation has only `done` because there is no real backend that can fail. v1.3 with a real backend would add the error state with retry + report-issue actions.
- **Mobile / touch / narrow-viewport untested.** Desktop-shaped feature; Lab 05 inclusion-lens findings name these as deferred to v2.x.

**Next action:**
1. Mark `NEXT_ACTIONS.md` priority 10 status `done` after this PR merges
2. Sponsor Reviewer recruitment (priority 9) — first session can now test the modal anatomy against U-CONF-1..4 with a real reviewer
3. Audit 2 trigger (priority 11) — re-audit v1.2 against Lab 06's six findings + Lab 05's prioritised list once a real Sponsor Reviewer session has happened

### Transfer 4 — Design-discipline calibration-cycle methodology → Data-engineering workstream

**Date:** 2026-05-18

**Source capability:** The cross-topic *audit-shape* discipline accumulated through DES-001 Topics 4 / 5 / 6 (CAPABILITIES rows at maturity 4), generalised one rung higher as the calibration-cycle pattern: spec → ship → calibration → policy revision, with artifacts at each step and the prior step's output retained as the diff baseline.

Specifically:
- Audit-shape as a workspace standard (cross-topic) — the Steps 1–N skeleton (artifact + framework → per-dimension matrix → findings + leverage-ranked list)
- Gestalt audit template + HCD audit template — both running the same *cycle* on a real artifact and surfacing durable findings rather than silent tweaks
- HCD self-audit gate (four cells) — name what would falsify the design, not just what the design is
- User-need vs request vs solution-shape triage — distinguishing category-level problems from parameter problems

**Target project:** The MSc destination-enrichment data-engineering workstream — first time the workspace runs the calibration cycle on a *data* artifact rather than a UI artifact. Promotes Big Data Analytics + Data Engineering from scaffolded (level 0) to active-development (level 2) per `operations/SKILL_MAP.md`.

**Problem solved:** Before this transfer the data-engineering workstream had no shipped methodology for *how* the workspace would convert "a strategy doc that ran end-to-end against real data" into "a policy revision that supersedes the strategy doc" without silently rewriting history or rolling back the v1 artifact. The design-discipline audit-cycle answered the question: ship the spec, capture the calibration findings as durable text alongside the original, revise the policy when category signals warrant a category rethink, preserve the prior artifact as the heuristic baseline. The pattern is the bridge.

**Artifact transferred:**
- `datasets/reference/destination_master_enrichment_strategy.md` — §18 calibration findings section added 2026-05-18 (with the original §§0–17 preserved unchanged); §19 policy transition added (~140 lines); §19.6 architecture resolution added
- `src/codemike/data/destination_master_enrichment_v1.py` — preserved as the v0 heuristic baseline, will be renamed `destination_master_enrichment_v0_heuristic.py` in P21
- `operations/CAPABILITIES.md` — calibration-cycle capability row added at maturity 2 (this PR)
- `operations/EXPERIMENTS.md` — EXP-003 entry for the E1 v1.0 ship as a worked experiment (this PR)
- `operations/DECISIONS.md` — two entries (§19 policy + §19.6 architecture) (this PR)
- `operations/SKILL_MAP.md` — Big Data Analytics + Data Engineering promoted from level 0 to level 2 (this PR)
- `charter/TOOLING.md` — free-tier source candidates pre-approved (this PR)

**Evidence:**
- Four-commit destination-enrichment cycle on the same branch: strategy v1 (P5) → E1 v1.0 ship (P15) → §18 calibration findings → §19 + §19.6 policy revision (PR #26)
- E1 v1.0 validator clean (`enriched_structurally_valid_not_planner_ready`); 359 rows; three manual-review queues; deterministic re-run confirmed
- Calibration findings are durable text in §18, not silent edits to §§0–17 — the audit-trail is preserved
- v1.0 artifacts retained per §19.2; not deleted, not rolled back
- Lyra + Aurelius graded reviews on PR #26 (93/100 + 91/100); both reviews durable on the PR

**Outcome:**
- The data-engineering workstream now has a shipped methodology, not just a target outcome. P20 (v2 strategy doc) inherits the pattern: it supersedes v1's §§0–17 with no-assumption + live-data + two-tier architecture (§19 + §19.6), it does so as a new document (`destination_master_enrichment_strategy_v2.md`), and v1 stays on file as the heuristic baseline. Future enrichment cycles can follow the same pattern.
- Big Data Analytics + Data Engineering skill rows in SKILL_MAP move from level 0 (Not started) to level 2 (Example reproduced) — the v1.0 cycle is the reproduced example.
- The CodeMike operating loop's *Improve* step has its first worked example outside the UI domain — the loop is now demonstrably cross-domain.
- The audit-shape-as-workspace-standard capability now has cross-domain evidence (UI audits + data-engineering policy cycle running the same skeleton).

**Limitations:**
- Single worked example. The capability sits at maturity 2 (prototype evidence) because the cycle has run once. P20 (v2 strategy doc) is the planned second worked example; success there promotes the capability to maturity 3 (reusable pattern).
- The transfer is *into* an MSc-internal workstream, not *out to* another project (Codex, SproutLab, future Planner). Cross-Province transfer is queued for after P21 ships — at that point the v2 source-backed pipeline becomes a candidate for Planner's enrichment service.
- The transfer pre-dates the §6 persona-spec formalization workstream (handoff §6 / §10) — calibration-cycle pattern was authored in the informal-persona era. Forward versions of this capability should reference the formal CodeMike + Aurelius specs once they land in Codex.
- Source-cited derivation is the *goal* of v2; v0 heuristic baseline does not satisfy the no-assumption rule and is named explicitly as the rejected pattern per §19.2.

**Next action:**
1. Land this governance-debt PR before P20 substance begins (handoff §5)
2. Open P20 work on a fresh branch — v2 strategy doc + per-field tier assignments + source coverage matrix (handoff §4.2) as the prerequisite
3. After P20 ships, evaluate the capability for promotion to maturity 3 (reusable pattern); second worked example unblocks the promotion
4. After P21 ships, evaluate cross-Province transfer candidacy (Planner's enrichment service)
