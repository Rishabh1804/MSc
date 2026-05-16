# DES-001 Learning Log

## 2026-05-14 — Topic 1 UI vs UX

### What was studied

- Difference between UI and UX
- Source comparison across Figma, NN/g, IxDF, and UXDT
- Further-reading ladder using heuristics, UX Honeycomb, GOV.UK user needs, and W3C accessibility framing

### What changed in understanding

UI is the visible and interactive interface layer. UX is the broader task journey and trust experience. In a data-review tool, UX includes credibility and uncertainty signalling, not only ease of use.

### Repository outputs created

- `docs/design-foundations.html`
- `docs/design-foundations-app/`
- `design/foundations/ui-vs-ux-further-reading.md`
- `design/checklists/master-browser-design-checklist.md`

### Open work

- Execute Topic 1 exercises
- Record lab results
- Complete quiz
- Submit and grade DES-001

---

## 2026-05-14 — Lab 01 UI vs UX Browser Audit executed

### What was executed

Lab 01 was executed against:

```text
docs/destination-master-browser-v1.html
```

The lab converted Topic 1 from reading evidence into applied coursework evidence.

### Exercises completed

- Exercise A: UI inventory
- Exercise B: UX journey map
- Exercise C: Nielsen heuristic mini-audit
- Exercise D: UX Honeycomb score

### Key finding

The browser already supports a basic QA/review workflow through search, filters, stats, warnings, cards, metadata, and chips. However, the reviewer journey is incomplete because v1 lacks reset, sort, table mode, full-record inspection, active-filter summary, and repeated trust signalling in deeper contexts.

### Repository outputs created

- `design/foundations/topic-01-ui-vs-ux-exercise-results.md`
- `courses/des-001-design-foundations/submissions/lab-01-ui-vs-ux-browser-audit-results.md`
- updated `courses/des-001-design-foundations/competency-map.md`

### What changed in understanding

The main v1 issue is not aesthetics. It is workflow completion and trust preservation. v1.1 should improve the review sequence:

```text
browse → narrow → compare → inspect → recover → leave with correct trust level
```

### Next action

Update the grade report and decide whether to implement Destination Master Browser v1.1 immediately or continue with DES-001 Topic 2 first.

---

## 2026-05-14 — Grade report completed after Lab 01

### What was graded

The current DES-001 state after Topic 1 and Lab 01 was graded against:

- `assignments/rubrics/design-foundations-rubric.md`
- `courses/des-001-design-foundations/grading-policy.md`

### Result

```text
82 / 100 — Excellent by DES-001 rubric; Distinction by course grading policy
```

### Feedback summary

Topic 1 is strong because it includes multi-source reading, source comparison, further-reading extension, applied lab execution, checklist implications, and a formal submission trail.

The result is provisional rather than final because the remaining DES-001 topics are not yet deeply digested and the modular dashboard still needs live visual verification.

### Decision

Proceed to DES-001 Topic 2 before implementing Destination Master Browser v1.1.

### Reason

Topic 2 will improve component-level UI decisions. Topic 3 will improve UX journey and task-flow decisions. Browser v1.1 should be implemented after the design vocabulary is stronger.

### Repository outputs updated

- `courses/des-001-design-foundations/feedback/DES-001-grade-report-v1.md`
- `courses/des-001-design-foundations/revisions/DES-001-revision-plan-v1.md`
- `courses/des-001-design-foundations/competency-map.md`

### Next action

Start DES-001 Topic 2 — What is UI design.

---

## 2026-05-16 — Topic 2 started: What is UI design

### What was scaffolded

Topic 2 artifacts created in the same shape as Topic 1:

- `lectures/lecture-02-what-is-ui-design.md` — UI design as a discipline; element vocabulary (controls, containers, navigation, data display, feedback, editorial); nine standard component states; affordance / signifier / feedback (Norman); consistency as load reducer; application to the Destination Master Browser.
- `readings/topic-02-what-is-ui-design-reading-pack.md` — five required sources (Material Design, Apple HIG, IBM Carbon, GOV.UK Design System, Don Norman) plus five extension sources (Refactoring UI, NN/g pattern articles, Atomic Design, Smashing Magazine pattern essays, WCAG / ARIA Authoring Practices). Seven reading questions plus an extraction target.
- `quizzes/quiz-02-what-is-ui-design.md` and `quizzes/quiz-02-what-is-ui-design-answer-key.md` — ten questions covering definition, vocabulary, states, affordance/signifier/feedback, container selection (card vs table vs drawer vs modal), filter-UI choice, empty-state design, and a design-decision gate. Answer key includes worked examples grounded in the Destination Master Browser.
- `labs/lab-02-ui-design-component-inventory.md` — six-step lab that produces a component catalogue, state-coverage matrix, affordance audit, container-selection rules, filter-UI rules, and a consolidated rule sheet (`design/foundations/ui-design-component-rules.md`) that becomes the input for Browser v1.1.

### What changed in understanding

UI design is decision work: choosing the right element for the right task, in the right state, with honest feedback. Visual design is a sub-skill within UI design — a polished colour palette does not redeem a wrong container choice. The Topic 1 finding ("v1 lacks workflow completion and trust preservation") now has a Topic 2 path forward: a rule-driven rebuild of the components themselves.

### Open work

- Complete Topic 2 deep reading (five required sources)
- Produce source-comparison notes
- Execute Lab 02 against the v1 browser
- Submit Lab 02 results and update `design/checklists/master-browser-design-checklist.md`
- Answer Quiz 02 without the answer key, then self-mark

### Next action

Begin Topic 2 deep reading. Lab 02 cannot start until the readings produce the source-comparison notes and the extraction target.

---

## 2026-05-16 — Topic 2 deep reading executed

### What was studied

The five required sources from the Topic 2 reading pack: Material Design 3 (foundations + components), Apple Human Interface Guidelines (foundations + components), IBM Carbon (component patterns + usage guidelines), GOV.UK Design System (components + patterns), Don Norman (DOET — affordances, signifiers, feedback). The reading produced source-by-source notes, a structured source comparison, CodeMike interpretation, browser application, anti-patterns, implementation implications, a checklist update, and three reusable design capabilities.

### What changed in understanding

UI design is the work of *choosing pattern → choosing container → choosing elements → specifying all nine states → verifying affordance/signifier/feedback for each interactive → defending against a "when not to use" gate*. Visual treatment is downstream of those decisions. The five sources differ less on definition than on emphasis — modality (Material permissive vs HIG/Carbon/GOV.UK restrictive), data-table prominence (Carbon first-class vs others light), and "when not to use" discipline (GOV.UK explicit vs others implicit) — and those emphasis differences map directly onto v1.1 design choices. The single biggest reframing: the unit of design is the *pattern* (master-detail with faceted search) not the component, and once the pattern is named most component choices follow.

### Repository outputs created

- `design/foundations/topic-02-what-is-ui-design.md` — 13-section deep-reading doc covering topic definition, source list with type classification, source-by-source notes, source comparison, CodeMike interpretation, browser application (with a per-decision sourcing table and a four-depth trust-signal specification), anti-patterns, implementation implications (10-item v1.1 backlog), further reading, checklist updates, three reusable CodeMike design capabilities, source-set reflection, and open work.
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-02-what-is-ui-design-answers.md` — ten worked answers cross-checked against the answer key, with self-mark notes.
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` — eight Topic 2 viva questions appended.
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-answers.md` — eight Topic 2 viva answers appended, each with an examiner-push follow-up.
- `docs/design-foundations-app/data.js` — Topic 2 module flipped from `todo` to `done`; sources expanded from three to six (five required + the extension link); full notes object replacing `PENDING_NOTES`.

### Key finding

The Destination Master Browser is — in Carbon's pattern vocabulary — a *master-detail data-review tool with faceted filtering*. That phrase, once spoken, fixes most v1.1 decisions: **table by default (cards as secondary), drawer for detail (never modal), filter chips + dropdowns + search for narrowing, content-rich empty state, skeleton loading, inline error notification, and a four-depth trust signal (top banner + list row + drawer header + confirm-modal)**. The v1 build was designed component-by-component; v1.1 should be designed pattern-first.

### Open work after Topic 2 reading

- Execute Lab 02 against `docs/destination-master-browser-v1.html`.
- Produce `design/foundations/topic-02-ui-design-component-inventory.md` (catalogue + state matrix + affordance audit).
- Produce `design/foundations/ui-design-component-rules.md` (the consolidated rule sheet — Browser v1.1's input).
- Update `design/checklists/master-browser-design-checklist.md` with the six new gates listed in §10 of the deep-reading doc.
- Open Topic 2 Execution PR B (Lab 02 + rule sheet).

### Next action

Open Topic 2 Execution PR A (this commit set), then start Lab 02 on a fresh branch for PR B.

---

## 2026-05-16 — Lab 02 executed (Topic 2 closed)

### What was executed

All six steps of Lab 02 against `docs/destination-master-browser-v1.html` (671 lines). The lab converted Topic 2's reading evidence into applied coursework evidence at the component level.

### Exercises completed

- **Step 1 — Component catalogue**: 20 patterns inventoried as present in v1 (controls / containers / data display / feedback / editorial / navigation), plus 12 patterns inventoried as missing but expected by Topic 2's named pattern fit (table, drawer, active-filter summary, Clear-all, card/table toggle, sortable headers, sticky header, skeleton loader, inline notification, confirm modal — deferred, focus rings, active-state on selects).
- **Step 2 — State coverage matrix**: every present pattern × nine standard states. Three HIGH-severity findings (control states missing across P3–P8; loading/empty/error sharing one component; record-card has no clickable state) and four MEDIUM-severity findings (stats-banner zero-narrative; side-panel loading; metadata missing-field handling; chips empty state).
- **Step 3 — Affordance / signifier / feedback audit**: per-pattern audit on Norman's three questions. Three cross-cutting findings: F1 active-state on filter controls; F2 trust-signal depth; F3 three feedback states sharing one component.
- **Step 4 — Container-selection rules**: card / table / list / drawer / modal each with when-to-use + when-not-to-use + sources + browser application. Decision tree included.
- **Step 5 — Filter-UI rules**: search input / filter chip / dropdown / faceted panel each with decision criteria. Active-filter summary is mandatory regardless of filter pattern in use.
- **Step 6 — Consolidated rule sheet**: full per-component rule table at `design/foundations/ui-design-component-rules.md` (signed off as Browser v1.1's input).

### Key findings

1. **Pattern resolution**: the Destination Master Browser is a *master-detail data-review tool with faceted filtering* (Carbon vocabulary). v1 commits to that pattern partially (has master, missing detail; has filtering, missing summary + recovery). v1.1 must close the partial commitment.
2. **Default view changes**: table becomes the default; cards become the secondary view via a toggle. The cards-vs-table debate from Lab 01 is resolved.
3. **Modality stays out of v1.1**: detail uses a drawer; modals are reserved for v1.2+ destructive batch actions.
4. **Trust-signal specification**: one trust-badge component, seven states (`verified`, `unverified`, `planner-ready`, `blocked`, `missing-fields`, `conflict`, `unassigned`), four depths (top banner + list row + drawer header + future confirm-modal). Colour palette deferred to Topic 10 — until then, colour + icon + text, never colour alone.

### Repository outputs created

- `design/foundations/topic-02-ui-design-component-inventory.md` — Lab 02 Steps 1–3.
- `design/foundations/ui-design-component-rules.md` — Lab 02 Steps 4–6 (consolidated rule sheet).
- `curriculum/courses/des-001-design-foundations/submissions/lab-02-ui-design-component-inventory-results.md` — formal lab submission with executive summary, key findings, and decision-gate satisfaction.
- `design/checklists/master-browser-design-checklist.md` §18 (six Topic 2 gates) + §19 (canonical rule-sheet pointer).

### What changed in understanding

Lab 01's "workflow completion + trust preservation" framing was correct but high-level. Lab 02 turns it into 18 concrete v1.1 changes (10 from the Topic 2 backlog + 8 component-rule refinements). The pattern-first framing — name the pattern, then the components follow — is the structural insight Topic 2 contributes to Browser v1.1.

### Topic 2 status

**Closed.** Both PR A (deep reading + source comparison + quiz + viva + data.js) and PR B (this entry's lab work + rule sheet + checklist gates + submission) are complete.

### Next action

Start DES-001 Topic 3 — UX design. Browser v1.1 implementation is gated on Topic 3 producing the reviewer-journey + UX-acceptance-criteria companion to the Topic 2 component rule sheet.

---

## 2026-05-16 — Topic 3 scaffolded + deep reading executed (PR A)

### What was scaffolded and executed

Topic 3 artifacts created in the Topic 1/Topic 2 shape, plus the deep reading executed in the same PR (no separate scaffold-only PR this time — the Topic 2 pattern was established enough to combine):

Scaffolding:

- `lectures/lecture-03-ux-design.md` — UX design as a discipline (research / modelling / design / evaluation); the four canonical activities and their artifacts; user-need vs request vs solution-shape; the seven-step reviewer journey with goal / cost / failure-mode / trust-check per step; UX acceptance-criterion form.
- `readings/topic-03-ux-design-reading-pack.md` — five required sources (Norman, NN/g, IDEO, GOV.UK Service Manual, IxDF) + five extension sources (Goodwin, Young, Morville Honeycomb, Patton, ISO 9241-210). Eight reading questions + extraction target + linked extension at `design/foundations/ux-acceptance-criteria.md`.
- `quizzes/quiz-03-ux-design.md` and `quizzes/quiz-03-ux-design-answer-key.md` — ten questions covering definition, the four activities, user-need classification, the seven journey steps, acceptance-criterion form, heuristic-vs-criterion comparison, GOV.UK discipline, why both Topic 2 and Topic 3 sheets are required, anti-patterns, design-decision gate.
- `labs/lab-03-ux-design-journey-map.md` — six-step lab brief that produces the journey map, the acceptance-criteria sheet, the user-need audit, the Lab 01 → Lab 03 gap analysis, and the master-browser checklist Topic 3 section.

Deep reading executed:

- `design/foundations/topic-03-ux-design.md` — 16-section deep-reading doc covering topic definition, the four canonical activities, source list with type classification, source-by-source notes, structured source comparison, user-need framework with three browser examples, the seven-step reviewer journey with goal/cost/failure/trust per step, UX acceptance-criterion form with three worked examples, CodeMike interpretation, browser application (with per-decision sourcing and v1.1 UX gates), four anti-patterns, ten-item v1.1 implementation impact, three reusable CodeMike design capabilities, source-set reflection, and open work.

Topic 3 quiz answers (ten worked answers, self-marked against the key).

Topic 3 viva questions (eight) + answers (eight, each with examiner-push follow-up) appended to the existing viva files.

Dashboard module updated: `docs/design-foundations-app/data.js` Topic 3 flipped from `todo` to `done`. Six sources attached (Norman, NN/g, IDEO, GOV.UK, IxDF, plus the CodeMike deep-reading-doc link). Full notes object mirroring Topic 1 and Topic 2 structure. Playwright re-verified post-change: 12 modules render, zero console errors, three of twelve now show `done` status.

### What changed in understanding

UX design is the discipline that turns user understanding into testable behavioural criteria the UI must produce. The single most important corrective the topic introduces — sourced primarily from GOV.UK — is the *user-need form*: `As a [user], I need [outcome], so that [goal]` with **no UI mechanism named**. This catches the entire class of solution-shape thinking ("users need a sort dropdown", "users need a reset button") that locks the design before the underlying outcome is researched.

The Destination Master Browser's reviewer journey has seven steps (arrive / understand / narrow / compare / inspect / recover / leave), each with goal / cost / failure / trust. The trust-check column is the journey-level operationalisation of Topic 2's four-depth trust signal. The Compare step is the most cognitively expensive (≤ 60s budget for the first comparison pass) and is the step v1's cards-only view fails — Topic 2's table mode is the fix.

### Open work after Topic 3 reading

- Execute Lab 03 against the v1 browser.
- Produce `design/foundations/topic-03-ux-design-journey-map.md` (lab Steps 1–4 evidence).
- Produce `design/foundations/ux-acceptance-criteria.md` (lab Step 5 — Browser v1.1's UX gate, companion to Topic 2's component rule sheet).
- Append Topic 3 section to `design/checklists/master-browser-design-checklist.md` (lab Step 6 — four UX gates + four UX anti-patterns).
- Open Topic 3 Execution PR B (lab + acceptance-criteria sheet + checklist gates + Topic 3 closure).

### Next action

Open Topic 3 Execution PR A (this commit set), then start Lab 03 on a fresh branch for PR B.

---

## 2026-05-16 — Lab 03 executed (Topic 3 closed)

### What was executed

All six steps of Lab 03 against `docs/destination-master-browser-v1.html` (671 lines). The lab converted Topic 3's reading evidence into applied coursework evidence at the journey level.

### Exercises completed

- **Step 1 — Full reviewer journey map**: 7 steps with goal (in GOV.UK user-need form) / cost budget / failure mode / trust check / current-v1 state / Lab 01 gap. Verdicts: 0 of 7 cleanly Pass; 3 Partial (Arrive, Understand, Leave); 1 Partial-to-fail (Narrow); 3 Fail (Compare, Inspect, Recover).
- **Step 2 — UX acceptance criteria**: 12 behavioural, testable, mechanism-independent criteria across the 7 steps. Each cross-referenced to its Topic 2 rule-sheet component(s) and the Lab 01 finding it closes.
- **Step 3 — User-need extraction**: 9 v1 features + 13 v1.1 backlog items audited as need / request / solution-shape. All produce a clean user need in GOV.UK form. One v1 implementation choice (shared `.empty` pane for loading/empty/error) flagged as solution-shape at the implementation layer; v1.1 splits it.
- **Step 4 — Lab 01 → Lab 03 gap analysis**: 11 Lab 01 findings tracked. All 11 closeable by v1.1 with combined rule sheet + acceptance-criteria sheet. One honest disagreement with Lab 01's heuristic verdict on item 9 (empty/error states marked Pass at heuristic granularity, Fail at criterion granularity — v1.1 honours the stricter standard).
- **Step 5 — Consolidated UX acceptance-criteria sheet**: `design/foundations/ux-acceptance-criteria.md` — 12 criteria, 13 gate-tests (1 cross-cutting), 12 of the 13 marked as v1.1 UX gates that must pass before ship. Per-criterion test plan included.
- **Step 6 — Master-browser checklist Topic 3 section**: §20 (four UX gates: criterion-presence, behaviour-testability, need-vs-request, journey-completeness); §21 (four UX anti-patterns: happy-path-only, request-vs-need, skip-evaluation, ignore-trust-at-depth); §22 (canonical pointer to the acceptance-criteria sheet).

### Key findings

1. **Browser v1.1 is now unblocked.** Topic 2 (component rule sheet) + Topic 3 (UX acceptance-criteria sheet) + master-browser checklist §3 + §18 + §20 form the complete v1.1 specification. The ratified execution plan's gate 1 (v1.1 implementation between Lab 03 close and Topic 4 open) is now reachable.
2. **Three Fail steps in v1**: Compare (no table/sort), Inspect (no drawer), Recover (no Clear-all / no content-rich empty state). v1.1's component + behavioural commitments close all three.
3. **All 11 tracked Lab 01 findings** are closeable by v1.1 — the heuristic-level findings translate into criterion-level closures.
4. **The 13-gate test plan** is reusable: it can be applied to any future data-review tool with the master-detail-with-faceted-filtering pattern.

### Repository outputs created

- `design/foundations/topic-03-ux-design-journey-map.md` — Lab 03 Steps 1–4.
- `design/foundations/ux-acceptance-criteria.md` — Lab 03 Step 5 consolidated sheet (Browser v1.1's UX gate).
- `curriculum/courses/des-001-design-foundations/submissions/lab-03-ux-design-journey-map-results.md` — formal lab submission.
- `design/checklists/master-browser-design-checklist.md` §20 + §21 + §22 — Topic 3 gates, anti-patterns, and canonical pointer.

### What changed in understanding

Lab 01's heuristic-level findings ("workflow completion + trust preservation") translate cleanly into Topic 3's criterion-level closures, but at a different granularity. Heuristic audits and acceptance criteria are complementary evaluation tools, not equivalents. The criterion approach is more reproducible (two evaluators reach the same verdict); the heuristic approach catches things the criteria forgot to name. Both have a role.

The most operationally consequential discipline Topic 3 introduces is the user-need audit as a backlog gate. Every v1.1 item now has a *need* (no UI mechanism named) and an *acceptance-criterion ID*. Items that cannot produce both are refused. This is the GOV.UK posture made operational.

### Topic 3 status

**Closed.** Both PR A (deep reading + source comparison + quiz + viva + data.js) and PR B (this entry's lab work + acceptance-criteria sheet + checklist gates + submission) are complete.

### Next action

**Implement Browser v1.1** against the consolidated specification: Topic 2 rule sheet + Topic 3 acceptance-criteria sheet + master-browser checklist §3 + §18 + §20.

