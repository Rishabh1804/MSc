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

