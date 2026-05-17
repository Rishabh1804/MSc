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
docs/destination-master-browser-v1.0.html
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

- Execute Lab 02 against `docs/destination-master-browser-v1.0.html`.
- Produce `design/foundations/topic-02-ui-design-component-inventory.md` (catalogue + state matrix + affordance audit).
- Produce `design/foundations/ui-design-component-rules.md` (the consolidated rule sheet — Browser v1.1's input).
- Update `design/checklists/master-browser-design-checklist.md` with the six new gates listed in §10 of the deep-reading doc.
- Open Topic 2 Execution PR B (Lab 02 + rule sheet).

### Next action

Open Topic 2 Execution PR A (this commit set), then start Lab 02 on a fresh branch for PR B.

---

## 2026-05-16 — Lab 02 executed (Topic 2 closed)

### What was executed

All six steps of Lab 02 against `docs/destination-master-browser-v1.0.html` (671 lines). The lab converted Topic 2's reading evidence into applied coursework evidence at the component level.

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

All six steps of Lab 03 against `docs/destination-master-browser-v1.0.html` (671 lines). The lab converted Topic 3's reading evidence into applied coursework evidence at the journey level.

### Exercises completed

- **Step 1 — Full reviewer journey map**: 7 steps with goal (in GOV.UK user-need form) / cost budget / failure mode / trust check / current-v1 state / Lab 01 gap. Verdicts: 0 of 7 cleanly Pass; 3 Partial (Arrive, Understand, Leave); 1 Partial-to-fail (Narrow); 3 Fail (Compare, Inspect, Recover).
- **Step 2 — UX acceptance criteria**: 12 behavioural, testable, mechanism-independent criteria across the 7 steps. Each cross-referenced to its Topic 2 rule-sheet component(s) and the Lab 01 finding it closes.
- **Step 3 — User-need extraction**: 9 v1 features + 13 v1.1 backlog items audited as need / request / solution-shape. All produce a clean user need in GOV.UK form. One v1 implementation choice (shared `.empty` pane for loading/empty/error) flagged as solution-shape at the implementation layer; v1.1 splits it.
- **Step 4 — Lab 01 → Lab 03 gap analysis**: 11 Lab 01 findings tracked. All 11 closeable by v1.1 with combined rule sheet + acceptance-criteria sheet. One honest disagreement with Lab 01's heuristic verdict on item 9 (empty/error states marked Pass at heuristic granularity, Fail at criterion granularity — v1.1 honours the stricter standard).
- **Step 5 — Consolidated UX acceptance-criteria sheet**: `design/foundations/ux-acceptance-criteria.md` — 14 criteria total; 13 are v1.1 UX gates (must pass before ship); 1 deferred to v1.1.x (U-INS-3 Prev/Next in drawer); 1 cross-cutting verification (U-LEA-1). Per-criterion test plan included.
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

---

## 2026-05-17 — Topic 4 scaffolded + deep reading executed (PR A)

### What was scaffolded and executed

Topic 4 (Design thinking) artifacts created in the Topic 3 shape (scaffold + deep reading + quiz + viva + data.js + tracking all in one PR per the established pattern).

Scaffolding:
- `lectures/lecture-04-design-thinking.md` — design thinking as iterative process; d.school 5-stage / IBM 3-activity / NN/g 5-stage mappings; Tim Brown's three constraints; iterative-non-linear discipline; common failure modes; application to the browser.
- `readings/topic-04-design-thinking-reading-pack.md` — four required sources (d.school Bootleg, IBM Design Thinking, Brown HBR + *Change by Design*, NN/g *Design Thinking 101*) + five extension sources (IDEO Field Guide chapters, Liedtka HBR, Goodwin scenarios+personas, Norman *Useful Myth* critique, GOV.UK Service Manual Discovery). Eight reading questions + extraction target + linked extension at `design/foundations/topic-04-design-thinking-loop.md` (Lab 04 PR B output).
- `quizzes/quiz-04-design-thinking.md` and `quiz-04-design-thinking-answer-key.md` — ten questions covering definition, stage-mappings, three-constraint triage, iteration jumps, evidence-per-stage rule, Norman critique, user-need vs POV statement, single-person-workspace anti-patterns, Topic 4-vs-Topic 3 routing, design-decision gate before exiting Ideate.
- `labs/lab-04-design-thinking-loop.md` — eight-step lab brief: pick pain-point + reject two alternatives, Empathize (3-perspective synthesis), Define (POV + HMW; rewrite twice), Ideate (≥ 3 meaningfully different), triage by three constraints, Prototype (cheap form), Test specification (with falsification criteria), loop result + decision.

Deep reading executed:
- `design/foundations/topic-04-design-thinking.md` — 16-section deep-reading doc: topic definition (+ non-definition), the 5-stage canonical + IBM/NN/g compressions with mapping table, source list + type classification, source-by-source notes (what each teaches / under-emphasises / strongest takeaway), structured source comparison (agreement + emphasis-difference + per-source omissions), three-constraint triage frame with browser-applied table, iterative/non-linear discipline (jump table: healthy vs evidence-skipping), Norman *Useful Myth* critique + how each other source responds, CodeMike interpretation (Topic 4 vs Topic 3 routing), application to v1.2 backlog, five anti-patterns (single-person specifics), implementation implications, three reusable CodeMike capabilities, source-set reflection, open work.

Topic 4 quiz answers (ten worked answers, self-marked against the key).
Topic 4 viva questions (eight) + answers (eight, each with examiner-push follow-up) appended.

Dashboard module: `docs/design-foundations-app/data.js` Topic 4 promoted from stub to full module entry with status `done`. Sources expanded from 0 to 5 (four required + extension link). Full notes object mirroring Topic 1/2/3 structure. Playwright re-verified: 12 modules render, zero console errors, four of twelve now `done`.

### What changed in understanding

Design thinking is *process discipline*, not creativity or workshop attendance. The four required sources have different centres of gravity (d.school operational, IBM organisational, Brown strategic, NN/g epistemic) and a single-source stop costs differently per source. The most operationally important corrective is the *evidence-per-stage* rule (NN/g) combined with the *three-constraint triage* (Brown) — together they distinguish design thinking from design-by-opinion at every stage. The Norman *Useful Myth* critique sharpens the discipline by naming what it must defend against (branding hazard, domain-expertise hazard) — sources that ignore the critique end up overselling.

For DES-001 specifically: Topic 4 sits *upstream* of Topic 3. The decision tree is — if the problem is well-framed (user-need writable + tested success answerable + criterion measurable), skip to Topic 3 criteria-writing; if not, run a Topic 4 loop first. Three v1.2 candidates from Lab 03's gap analysis (collapsible filter panel, confirm modal for destructive batch actions, faceted filter panel) need Topic 4 loops first because their underlying problems are not yet well-framed.

### Open work after Topic 4 reading

- Execute Lab 04 against ONE chosen v1.2 pain-point (Lab 04 PR B)
- Produce `design/foundations/topic-04-design-thinking-loop.md` (full loop with evidence per stage)
- Submit `submissions/lab-04-design-thinking-loop-results.md`
- Append Topic 4 §23 + §24 to `design/checklists/master-browser-design-checklist.md`
- Move on to Topic 5 (HCD) per the ratified three-topic push (Topics 4 → 5 → 6 ending in grade report v3)

### Next action

Open Topic 4 PR A (this commit set), then start Lab 04 on a fresh branch for PR B.

---

## 2026-05-17 — Lab 04 executed (Topic 4 closed)

### What was executed

All eight steps of Lab 04 against the **batch-promote-with-confirm** v1.2-candidate pain-point (chosen from Lab 03's three deferred items; collapsible-filter and faceted-panel rejected for Loop 1 with reasons recorded).

### Loop output highlights

- **Empathize**: three-persona synthesis (first-time / power / accessibility-need) converged on a non-obvious shared requirement: *the modal must work for any-N batches from the start*. Designing for the "interesting" case (large batch) and bolting on the small-batch case is the trap Loop 1 avoided.
- **Define**: POV statement rewritten three times; final form locks **asymmetric cost** as the design constraint (cost of a wrong promotion >> cost of an interruption to a correct one).
- **Ideate**: four meaningfully different candidates (inline-preview-toast / two-stage modal / approval-step / eliminate batch).
- **Triage**: all four × Tim Brown's three constraints with sourced cells. Candidate B (two-stage confirm modal with named records) chosen with explicit comparative reasoning vs A (viability concern), C (better long-term but needs Topic 5-level workflow redesign), D (solves wrong problem by removing the user need).
- **Prototype**: ASCII modal anatomy + three-state machine + accessibility commitments (focus trap, focus restoration, Esc cancels, default-focused Cancel, aria-labelledby/describedby).
- **Test specification**: three personas × five testable metrics + six falsification criteria that would trigger Loop 2.
- **Decision**: Ship Candidate B to v1.2 backlog with Topic 3 handoff (four `U-CONF-*` criteria) + Topic 2 component-rules note + falsification criteria as the v1.2 test plan.

### Key findings

1. **Asymmetric cost as the design constraint** for destructive actions. The right modal-design optimises for catching wrong actions, not for minimising friction on correct ones.
2. **Three-persona synthesis is a workable solo-workspace substitute** for facilitated empathy work. It doesn't replace real Sponsor-Reviewer testing (Loop 2 input), but it produces honest Empathize evidence.
3. **The best long-term answer was not the chosen candidate.** Candidate C (approval-step) would be better if the workflow itself moved toward an approval-stage model — but it requires Topic 5-level workflow rework. Choosing the shippable-now over the better-but-needs-rework option is the kind of explicit *shortest-path* decision Brown's triage forces.
4. **Three new reusable design capabilities extracted** (three-persona synthesis pattern; asymmetric-cost framing; Topic 4 → Topic 3 handoff format). Combined with the three from the deep-reading doc, the workspace now has fifteen reusable design capabilities at maturity ≥ 3.

### Repository outputs created

- `design/foundations/topic-04-design-thinking-loop.md` — Loop 1 evidence (Steps 1–8)
- `curriculum/courses/des-001-design-foundations/submissions/lab-04-design-thinking-loop-results.md` — formal lab submission
- `design/checklists/master-browser-design-checklist.md` §23 (four gates) + §24 (five anti-patterns) + §25 (canonical loop-output pointer)

### What changed in understanding

Lab 04 turned design thinking from a *process to read about* into a *process to run*. The eight-step worked example produces a concrete v1.2-backlog item with acceptance criteria, component rules, and falsification criteria — exactly the handoff Topic 4 deep-reading doc §10 specified. The discipline is now operational, not theoretical.

The single most important meta-finding: **Loop 1's three-persona substitute for real empathy work is honest but limited**. Loop 2, when it runs, needs at least one real Sponsor Reviewer to test against the six falsification criteria. The discipline isn't complete until that happens.

### Topic 4 status

**Closed.** Both PR A (deep reading + scaffold + quiz + viva + data.js) and PR B (this entry's Lab 04 + loop output + checklist gates + submission) are complete.

### Next action

Start **DES-001 Topic 5 — Human-centred design** per the ratified three-topic push (Topics 4 → 5 → 6 ending in grade report v3).

---

## 2026-05-17 — Topic 5 scaffolded + deep reading executed (PR A)

### What was scaffolded and executed

Topic 5 (Human-centred design) artifacts created in the Topic 4 shape (scaffold + deep reading + quiz + viva + data.js + tracking all in one PR).

Scaffolding: lecture-05, reading-pack-topic-05, quiz-05 + answer key, lab-05.

Deep reading executed:
- `design/foundations/topic-05-hcd.md` — 16-section deep-reading doc: topic definition (HCD as standards-grade lifecycle); four ISO 9241-210 activities with per-activity artifacts; six ISO principles with single-person-workspace translation table; W3C accessibility/usability/inclusion triad; source list (ISO, Norman, IDEO, W3C + 6 extension); source-by-source notes; structured source comparison; Norman *HCD Considered Harmful?* critique + per-source responses; canonical hierarchy (HCD umbrella over Topics 2/3/4) with artifact-to-activity mapping; application to v1.1 (anticipated gaps); four anti-patterns for solo workspaces; implementation implications for v1.2 + grade-report v3; further reading; reusable capabilities; source-set reflection; open work.

Topic 5 quiz answers (ten worked answers, self-marked).
Topic 5 viva questions (eight) + answers (eight, each with examiner-push follow-up) appended.

Dashboard module: `docs/design-foundations-app/data.js` Topic 5 promoted from stub to full module entry. Five sources attached. Full notes object. Playwright re-verified: 12 modules render, zero console errors, five of twelve now `done`.

### What changed in understanding

HCD is the *standards-grade lifecycle* that wraps every other design discipline. Its value isn't new artifacts; it's the *audit-shape* — every Topic 2/3/4 artifact maps to at least one ISO 9241-210 activity, and missing activities become visible. The Norman critique (HCD over-centres the individual user, missing systems thinking) is addressed structurally by doing Activity 1 (Context of use) properly: context-of-use IS systems-thinking when done well.

For DES-001 specifically: HCD is the umbrella over Topics 2 (UI components), 3 (UX criteria + journey), and 4 (design-thinking loop). Lab 05 will audit v1.1 against the lifecycle. Anticipated gaps: human-grade evaluation absent; systems-level context-of-use incomplete; inclusion lens fail (English-only, desktop-only, monocultural).

### Open work after Topic 5 reading

- Execute Lab 05 HCD audit (PR B)
- Produce `design/foundations/topic-05-hcd-audit.md`
- Submit `submissions/lab-05-hcd-audit-results.md`
- Append Topic 5 §26 + §27 + §28 to `design/checklists/master-browser-design-checklist.md`
- Move on to Topic 6 (Gestalt) — final topic in the three-topic push

### Next action

Open Topic 5 PR A (this commit set), then start Lab 05 on a fresh branch for PR B.

---

## 2026-05-17 — Lab 05 executed (Topic 5 closed)

### What was executed

Full HCD audit (Audit 1) of v1.1 + Lab 04 Loop 1 against ISO 9241-210's four activities, six principles, and the W3C accessibility/usability/inclusion triad. Seven findings identified; six-item prioritised v1.2 HCD list produced.

### Verdict summary

| Dimension | Result |
|---|---|
| Four ISO activities | All audited with evidence |
| Six ISO principles | 2 Pass, 3 Partial, 1 Fail |
| W3C triad | 1 Pass (Usability), 1 Partial (Accessibility), 1 Fail (Inclusion) |
| Findings | 7 (4 High, 2 Medium, 1 lower) |
| v1.2 HCD list | 6-item prioritised list, ordered by leverage |

**Overall**: v1.1 is *HCD-substantial but incomplete*. The audit-shape is intact; machine-grade discipline is strong. The Fail (Principle 2: Users involved throughout) and four High-severity findings are all closable in v1.2 with Sponsor Reviewer recruitment + four targeted specification efforts.

### Key findings

- **F-CTX-1 (High)**: Systems-level context-of-use under-documented. The downstream Planner consumer + lateral handoff + regulatory layers are not yet designed objects. Norman's *HCD Considered Harmful?* critique applies.
- **F-REQ-1 (Medium)**: Lab 04 §8 U-CONF-1..4 criteria in prose but not landed in `ux-acceptance-criteria.md`.
- **F-REQ-2 (High)**: Inclusion-lens user requirements entirely absent from the canonical criteria sheet.
- **F-EVAL-1 (High)**: Human-grade evaluation is absent — only the machine-grade 19-gate walkthrough exists.
- **F-PRIN-1 (High)**: Principle 2 (Users involved throughout) is the only outright Fail; Sponsor Reviewer recruitment becomes a v1.2 prerequisite.
- **F-W3C-1 (High)**: Inclusion lens fails on five sub-dimensions (language, bandwidth, device, cultural context, terminology).

### Prioritised v1.2 HCD list

1. Recruit at least one Sponsor Reviewer (closes F-EVAL-1, F-PRIN-1)
2. Land U-CONF-1..4 in `ux-acceptance-criteria.md` (closes F-REQ-1)
3. Produce systems-context-of-use document (closes F-CTX-1)
4. Specify inclusion-lens requirements (closes F-REQ-2, F-W3C-1)
5. Include screen-reader test in Sponsor Reviewer recruitment (upgrades Accessibility lens)
6. Re-audit v1.1 at heuristic-grade with post-Topics-2-5 discipline (closes F-EVAL-2)

### Repository outputs created

- `design/foundations/topic-05-hcd-audit.md` — Audit 1 (Steps 1–7 evidence; capability extraction)
- `curriculum/courses/des-001-design-foundations/submissions/lab-05-hcd-audit-results.md` — formal lab submission
- `design/checklists/master-browser-design-checklist.md` §26 + §27 + §28 (Topic 5 gates + anti-patterns + canonical pointer)

### What changed in understanding

The audit-shape itself is the most operationally important discipline Topic 5 introduces. Before the audit, *we did HCD* was unverifiable; after, the four activities + six principles + W3C triad are a checklist. Items that can be passed off as "the design is good" are surfaced as concrete gaps (F-CTX-1, F-REQ-2, F-EVAL-1, F-W3C-1) with specific closure paths.

The single most important meta-finding: *honest naming of limitations is the discipline*. v1.1 isn't HCD-failing because it has gaps; it's HCD-substantial because the gaps are named, prioritised, and queued for closure. Pretending the gaps don't exist is the non-compliance failure mode.

### Topic 5 status

**Closed.** Both PR A (deep reading + scaffold + quiz + viva + data.js) and PR B (this entry's Lab 05 + audit + checklist gates + submission) are complete.

### Next action

Start **DES-001 Topic 6 — Gestalt principles** — the final topic in the ratified three-topic push (Topics 4 → 5 → 6 ending in grade report v3).

---

## 2026-05-17 — Topic 6 PR A scaffolded + deep reading complete

### What was executed

Topic 6 (Gestalt principles) reading + scaffold landed on branch `claude/des-001-topic-06-reading`:

- Lecture (`lectures/lecture-06-gestalt-principles.md`) — Gestalt as perceptual constraints (not aesthetic rules); Prägnanz + six core principles with UI consequences; canonical hierarchy extension (Topic 6 sits underneath Topic 2)
- Reading pack (`readings/topic-06-gestalt-principles-reading-pack.md`) — 4 required sources (Wertheimer/Koffka/Köhler via secondary; IxDF; NN/g; Smashing) + 5 extensions
- Quiz + answer key + worked answers (`quizzes/quiz-06-gestalt-principles*.md`) — 10 questions including definition, Prägnanz, six principles, violation, conflict adjudication, hierarchy, critique, scope defence, anti-pattern, design-decision gate
- Lab 06 brief (`labs/lab-06-gestalt-audit.md`) — six-step audit (regions → per-principle matrix → conflict adjudication → density audit → findings + prioritised v1.1.x/v1.2 fix list → checklist §29/§30/§31)
- 15-section deep-reading doc (`design/foundations/topic-06-gestalt.md`) — topic definition, Prägnanz + corollary, source list + per-source notes, source comparison, violation taxonomy (false-positive / false-negative / unresolved conflict), perceptual-constraint vs aesthetic-rule critique, canonical hierarchy extension (Gestalt underneath Topic 2), browser application with six anticipated violations, three anti-patterns, implementation implications
- Eight Topic 6 viva questions + answers (`viva/DES-001-viva-questions.md` + `-answers.md`) — each with examiner-push follow-up
- Dashboard module flipped from `partial` (stub) to `done` (`docs/design-foundations-app/data.js`) — 12 modules, 6 done, 6 todo; Cipher verified zero errors

### Verdict summary

| Dimension | Result |
|---|---|
| Required sources read | 4/4 (Wertheimer/Koffka/Köhler via secondary; IxDF; NN/g; Smashing) |
| Extension sources noted | 5/5 (Rutledge, Refactoring UI, Tufte, Goldstein, Krug) |
| Six principles documented with browser-specific example | 6/6 |
| Source comparison (agreement + difference-by-emphasis + per-source omissions) | Complete (§5) |
| Violation taxonomy | 3 sub-types defined (§6) |
| Critique engagement | Complete (§7 — perceptual constraint vs aesthetic rule) |
| Canonical hierarchy extension | Complete (§8 — Gestalt underneath Topic 2) |
| Browser application | Complete (§9 — six audit regions + six anticipated violations) |
| Anti-patterns specific to data-review tools | 3 documented (§10) |
| Lecture | Complete |
| Quiz + key + worked answers | Complete |
| Lab brief | Complete |
| Viva questions + answers (with examiner-push) | 8 / 8 |
| Dashboard module promoted | Complete |
| Cipher verification (`/tmp/verify-canonical.js`) | 12 modules, 0 errors |

### What changed in understanding

The single most operationally important discipline Topic 6 introduces is the *perceptual constraint vs aesthetic rule* distinction. The style reading lets designers override the principles on taste ("use whitespace generously" is unfalsifiable); the constraint reading forces every visual choice to defend itself against what the visual system *will* do ("we used 16px between unrelated controls and 4px within related ones, defending the proximity signal for the toolbar's narrowing-controls group" is falsifiable). The constraint framing is what makes Lab 06's audit possible at all — without it, "feels off" is the strongest finding language available.

Second meta-finding: Gestalt sits *underneath* Topic 2, not alongside. A design can be Topic-2-compliant (right components, right states, right modality) and still Gestalt-violating (wrong perceived grouping). The two audits run different tests and produce different fix lists; keeping them distinct preserves both audit-shapes.

Third meta-finding: principle conflicts are adjudicated *by user task*, not by a fixed principle hierarchy. The same proximity-vs-similarity conflict can resolve in opposite directions depending on whether the task is "treat these as one group" or "distinguish these categories". Smashing is the only required source that publishes this rule explicitly, and it's the most operationally important piece of guidance for the dense regions of the v1.1 browser.

### Topic 6 PR A status

**Complete and ready to push.** Six files written + tracking files updated + Cipher verified. PR #17 will be cut as draft against `main`.

### Next action

Execute **Lab 06 — Gestalt audit of v1.1** (Topic 6 PR B) on a fresh branch. After Lab 06 closes, the three-topic push terminates and grade report v3 (cumulative DES-001 grade after Topics 1–6) is the final closure deliverable.

---

## 2026-05-17 — Lab 06 executed (Topic 6 closed)

### What was executed

Full Gestalt audit (Audit 1) of v1.1 against the six core principles (proximity, similarity, continuity, closure, common region, common fate) across six screen regions (cards, table, toolbar, active-filter summary, banners stack, drawer). Six findings identified plus one audit-level meta-finding; six-item prioritised v1.1.x / v1.2 fix list produced.

### Verdict summary

| Dimension | Result |
|---|---|
| Audited regions | 6 / 6 |
| Principle-cells graded | 36 (6 regions × 6 principles) |
| Pass cells | 22 |
| Trade-off cells (with named compensation) | 5 |
| Violation cells (findings) | 7 |
| N/A cells | 4 |
| Findings (consolidated, distinct) | 6 (F-GES-1..6) plus 1 meta-finding (F-GES-7) |
| Strengths | 6 (R5 banners + R6 drawer + 4 cross-cutting) |
| Conflicts adjudicated | 4 (R1 caution-chips; R3 view-toggle; R3 search-vs-selects; R4 summary-vs-toolbar) — zero left unresolved |
| Prioritised fix list | 6 items (5 v1.1.x + 1 v1.2) |
| Decision-gate satisfaction | All 5 Lab 06 decision-gate conditions met |

**Overall**: v1.1 is *Gestalt-substantial*. Two regions (R5 + R6) are exemplary; the other four have a small consistent pattern of findings, all closable with visual-treatment-only changes. Five of six fixes tag as v1.1.x; one (search-vs-select grammar unification) tags as v1.2 pending Sponsor Reviewer input. No fix requires a Topic 2 component-rule change.

### Key findings

- **F-GES-1 + F-GES-2 (High leverage)**: Verification *text* duplicated inside card meta-grid + table column at equivalent visual weight to non-trust fields — partially undoing the trust badge's elevation via similarity-collapse. Single visual-treatment fix closes both occurrences across both views.
- **F-GES-3 (R2 Table)**: Sortable column headers don't visually signal interactivity; similarity to non-sortable headers creates false-negative interactivity grouping. The `aria-sort` accessibility work is correct but lacks a visual counterpart.
- **F-GES-4 + F-GES-5 (R3 Toolbar)**: Two false-positive groupings in the toolbar — view-toggle incorrectly included in narrowing-controls common-region (F-GES-4); search + selects share styling but have different interaction grammars (live-update vs commit-on-change) — F-GES-5 confirms the primary anticipated violation from the deep-reading doc §9.2.
- **F-GES-6 (R4 Active-filter summary)**: Summary bleeds into toolbar via proximity + weak tint differential.
- **F-GES-7 (Cross-cutting meta-finding)**: Three of six regions silently collapse on whitespace; pattern is structural, not three isolated bugs. Closed by fixes for the component findings.

### Repository outputs created

- `design/foundations/topic-06-gestalt-audit.md` — Audit 1 (Steps 1–6 evidence; reusable capabilities; honest limitations)
- `curriculum/courses/des-001-design-foundations/submissions/lab-06-gestalt-audit-results.md` — formal lab submission
- `design/checklists/master-browser-design-checklist.md` §29 + §30 + §31 (Topic 6 Gestalt gates + anti-patterns + canonical pointer)

### What changed in understanding

The audit-shape's most operationally important contribution is the *cross-cutting pattern surfacing*. Three observations would have read as separate small issues under introspection alone: "verification text in cards looks plain", "verification column in table looks plain", "trust badge elevation feels partial". The per-region per-principle matrix instead surfaced them as a *single root cause*: similarity-collapse against the four-depth trust signal specification. One visual-treatment fix closes the pattern wherever it appears.

Second meta-finding: the audit *cross-validated Topic 2's specifications*. The four-depth trust signal (Topic 2 §6.2) is correctly implemented in three of four depths (banner + drawer + confirm-modal) and in the *badge* element of cards + table. The findings are about the *duplicate verification text*, not the badge itself — meaning the Topic 2 rule is right; the implementation is partially under-honouring it. Without the Gestalt audit, this nuance would have been invisible.

Third meta-finding: principle conflicts can be adjudicated even when v1.1 hasn't explicitly resolved them. The R1 caution-chip case is currently a "soft" win for similarity (colour distinction does most of the work); the audit names it as Trade-off rather than Violation but flags the upgrade (visual divider) as a Pass-promotion item. The discipline is to be explicit about which adjudications are full vs partial — and the matrix forces that explicitness.

### Topic 6 status

**Closed.** Both PR A (deep reading + scaffold + quiz + viva + data.js) and PR B (this entry's Lab 06 + audit + checklist gates + submission) are complete. The three-topic push (Topics 4 → 5 → 6) is one closure-cycle away from terminating with grade report v3.

### Next action

**End-of-Topic-6 closure** per the ratified three-topic push:

1. Lyra + Aurelius graded reviews on PR B (review-and-grade-only pattern)
2. Merge PR A + PR B
3. Catch up Aurelius governance debt accumulated across Topics 4 + 5 + 6 (SKILL_MAP, CAPABILITIES, PROJECT_LOG × 3, NEXT_ACTIONS)
4. Write **grade report v3** at `feedback/DES-001-grade-report-v3.md` — cumulative DES-001 grade after Topics 1–6 (HCD compliance from Topic 5 + Gestalt compliance from Topic 6 + scope-incompleteness adjustment scaled down from −6 toward 0 as 6 / 12 topics now closed)
5. **STOP** per ratified three-topic push goal

