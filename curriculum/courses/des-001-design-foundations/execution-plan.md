# DES-001 Execution Plan

Status: draft — awaiting scope and sequencing decisions before execution starts.

This plan turns the 12-topic assignment brief into a concrete execution order with per-topic source lists, effort estimates, and decision gates. It does **not** start executing topics — that begins after the four decisions in §1 are locked.

The plan is grounded in the four documents that already exist:

- `curriculum/assignments/DES-001-design-foundations-study-dashboard.md` — the brief
- `curriculum/assignments/rubrics/design-foundations-rubric.md` — the grading rubric
- `curriculum/courses/des-001-design-foundations/feedback/DES-001-grade-report-v1.md` — the provisional grade and open revision items
- `curriculum/courses/des-001-design-foundations/competency-map.md` — what is done vs pending

---

## 1. Decisions required before execution

Four decisions shape the rest of the plan. Each is listed with the trade-off and a recommendation.

### 1.1 Scope: 12 topics, or freeze at N for interim submission?

The brief lists 12 topics. The grade report (item 4 of "Required revisions") explicitly asks: *"Decide whether DES-001 scope requires all 12 topics before final grading."*

| Option | What it means | Trade-off |
|---|---|---|
| **A. All 12 topics** | Full benchmark eligibility per §12 of the brief. ~60–80h of focused work after Topic 1. | Highest grade ceiling. Calendar risk: Browser v1.1 waits longer. |
| **B. Freeze at Topic 6** | Submit DES-001 v1 after Topics 1–6 (UI vs UX, UI design, UX design, Design thinking, HCD, Gestalt). Topics 7–12 deferred to DES-002 or a v2 of DES-001. | Faster path to a graded Excellent. Cannot be promoted to **Benchmark** under §12 ("transferability to future CodeMike work") because half the foundation language is missing. |
| **C. Freeze at Topic 3** | Just enough to inform Browser v1.1 (UI vs UX, UI design, UX design). | Pragmatic. Grade likely Good rather than Excellent. Cannot be benchmark. |

**Recommendation: A (all 12).** Topic 1 graded provisional 82/100. The rubric's Benchmark band requires breadth as well as depth. Cutting the scope now caps the grade. The brief was set up with benchmark eligibility in mind; don't trade that away unless the calendar forces it.

### 1.2 Sequencing: scaffold-all then execute, or scaffold-then-execute per topic?

| Option | What it means | Trade-off |
|---|---|---|
| **A. Per topic** (current pattern) | Scaffold Topic N → execute Topic N → close → scaffold Topic N+1. What Topics 1 and 2 did. | Each topic produces real evidence before the next one opens. Learning compounds. Slower to "look complete". |
| **B. Scaffold all first** | Write lecture + reading pack + quiz + lab brief for all 12 topics, then execute. | Whole curriculum visible at once. Risk: scaffolds drift from the actual reading because they're written before the sources are read. |

**Recommendation: A (per topic).** The Topic 1 pattern works. Scaffolds-before-reading risks the lecture asserting things the sources don't support — exactly the failure mode the rubric punishes.

### 1.3 When to implement Destination Master Browser v1.1?

The Topic 1 grade report decision was *"proceed to Topic 2 first, then implement v1.1 after at least Topics 2 and 3 are complete."* That decision still holds, but it's worth re-confirming now that Topic 2 is scaffolded.

| Option | What it means | Trade-off |
|---|---|---|
| **A. After Topic 3 (current decision)** | Lab 02 produces the component rule sheet; Lab 03 produces the journey-and-task-flow rules. v1.1 follows both. | Component decisions and journey decisions both informed. Browser improvement comes early enough to validate the rules. |
| **B. After Topic 6** | Wait until Gestalt is also in the toolkit. | Grouping and visual-hierarchy rules also available. Calendar cost. |
| **C. After all 12** | Defer until DES-001 is fully submitted. | Maximally informed. Browser stays at v1 for the duration of DES-001. |

**Recommendation: A (after Topic 3).** Diminishing returns past Topic 3 for v1.1's stated scope (workflow completion and trust preservation). Topics 4–12 inform v1.2 and beyond.

### 1.4 Dashboard artifact naming

The brief names `docs/design-foundations.html`. The current submission points to `docs/design-foundations-v2.html`. They diverge.

| Option | What it means | Trade-off |
|---|---|---|
| **A. Rename v2 → canonical** | Move `docs/design-foundations-v2.html` to `docs/design-foundations.html`. Update submission file, learning log, and grade report references. | Matches the brief. One rename, three or four reference updates. Cleanest outcome. |
| **B. Keep `v2` and update the brief** | Brief becomes "primary artifact: `docs/design-foundations-v2.html`". | Avoids rename in `docs/`. Brief change is the kind of paperwork edit that gets re-litigated later. |
| **C. Build a new `docs/design-foundations.html`** | Treat `v2` as scratch, build the canonical artifact fresh from the brief's §7 feature list. | Maximum cleanliness. Costliest in time. Throws away the modular v2 architecture. |

**Recommendation: A (rename v2 → canonical).** v2's modular architecture is already verified at the repository level (per the grade report). Renaming costs one PR; rebuilding costs days.

---

## 2. Per-topic plan

Each row gives sources, type classification (P = primary/high-authority, A = applied, X = cross-check), estimated effort in focused hours, and lab outline.

Topics 1 and 2 are listed for completeness. Topic 1 is done. Topic 2 is scaffolded (lecture, reading pack, quiz, lab brief shipped in PR #3) — the row reflects remaining execution effort.

### Topic 1 — UI vs UX ✓ done

Status: graded provisional 82/100. Open: quiz answers, viva answers, visual verification of v2.

### Topic 2 — What is UI design (scaffolded, in progress)

Sources already chosen in `readings/topic-02-what-is-ui-design-reading-pack.md`:

| Source | Type |
|---|---|
| Material Design — Foundations & Components | A |
| Apple HIG — Components | A |
| IBM Carbon — Component patterns | A |
| GOV.UK Design System — Components | A |
| Don Norman — affordances/signifiers chapter | P |
| Refactoring UI; NN/g pattern articles; Atomic Design; Smashing pattern essays; WCAG/ARIA APG | X (extension ladder) |

Effort remaining: **8–10h** (reading + source comparison + Lab 02 execution + rule sheet).
Lab output: `design/foundations/ui-design-component-rules.md` — the input to Browser v1.1.

### Topic 3 — UX design

| Source | Type |
|---|---|
| Don Norman — *The Design of Everyday Things* (intro + UX definition) | P |
| NN/g — Definition of User Experience (already used in Topic 1, extended here) | P |
| IDEO — *Field Guide to Human-Centered Design* (UX chapter) | A |
| GOV.UK Service Manual — User research and journey mapping | A |
| Interaction Design Foundation — UX foundations course summary | X |

Effort: **8–10h**.
Lab outline: full reviewer journey map for the Destination Master Browser with UX acceptance criteria; gap analysis against the Lab 01 journey map (which was heuristic-led).
Lab output: `design/foundations/topic-03-ux-design-journey.md` and acceptance-criteria sheet that becomes Browser v1.1's UX gate.

### Topic 4 — Design thinking

| Source | Type |
|---|---|
| Stanford d.school — Design Thinking Bootleg / process guide | P |
| IBM Design Thinking — Loop framework | A |
| Tim Brown — *Change by Design* / HBR article | P |
| NN/g — "Design Thinking 101" | X |

Effort: **5–7h**.
Lab outline: run one design-thinking loop (empathize → define → ideate → prototype → test) on a single browser pain point identified in Lab 01.
Lab output: `design/foundations/topic-04-design-thinking-loop.md`.

### Topic 5 — Human-centered design

| Source | Type |
|---|---|
| ISO 9241-210 — Human-centred design for interactive systems (summary) | P |
| Don Norman — HCD essays (NN/g) | P |
| IDEO HCD field guide (overlap with Topic 4; different chapters) | A |
| W3C — Accessibility, usability, and inclusion | X |

Effort: **5–7h**.
Lab outline: HCD audit of the browser — who is the user, what is the context of use, what are the requirements, what does evaluation look like? Cross-check against ISO 9241-210's four activities.
Lab output: `design/foundations/topic-05-hcd-audit.md`.

### Topic 6 — Gestalt principles

| Source | Type |
|---|---|
| Wertheimer / Koffka / Köhler — original Gestalt principles (via authoritative secondary source) | P |
| Interaction Design Foundation — Gestalt principles | A |
| NN/g — Gestalt principles in UI | A |
| Andy Rutledge / Smashing — Gestalt in interface examples | X |

Effort: **4–5h**.
Lab outline: re-audit the browser cards and stats banner for proximity, similarity, continuity, closure, common region, common fate; mark each Gestalt violation against a v1.1 fix.
Lab output: `design/foundations/topic-06-gestalt-audit.md`.

### Topic 7 — Fitts' law

| Source | Type |
|---|---|
| Fitts (1954) — original paper, abstract and summary | P |
| Bruce Tognazzini — "A Quiz Designed to Give You Fitts" | A |
| NN/g — Fitts' law in interface design | A |
| Kent Bye / A List Apart — applied web design articles | X |

Effort: **3–4h** (well-defined, narrow).
Lab outline: measure target sizes and distances in the browser; flag any clickable < 24px or hard-to-reach combinations; produce a target-size rule for v1.1.
Lab output: `design/foundations/topic-07-fitts-law-targets.md`.

### Topic 8 — Button states

| Source | Type |
|---|---|
| Material Design — button states | A |
| Apple HIG — control states | A |
| W3C ARIA Authoring Practices — interactive states | P |
| NN/g — state design for forms and buttons | X |

Effort: **3–4h** (overlaps with Topic 2's state matrix; this topic is the depth pass).
Lab outline: extend the Lab 02 state-coverage matrix to *every* interactive in the browser, not just patterns. Produce missing-state implementation tickets.
Lab output: `design/foundations/topic-08-button-states.md`.

### Topic 9 — Typography

| Source | Type |
|---|---|
| Robert Bringhurst — *The Elements of Typographic Style* (foundational chapters) | P |
| Matthew Butterick — *Practical Typography* | A |
| Material Design — Typography system | A |
| WebAIM — Typography accessibility | X |

Effort: **6–8h**.
Lab outline: type audit of the browser — scale, line-length, line-height, hierarchy, accessible minimums; produce a type token sheet.
Lab output: `design/foundations/topic-09-typography-tokens.md`.

### Topic 10 — Color theory

| Source | Type |
|---|---|
| Johannes Itten / Josef Albers — color theory foundations (via summary) | P |
| Material Design — color system + tonal palettes | A |
| WebAIM — contrast and accessible color | A |
| Schoger & Wathan — *Refactoring UI* color chapter | X |

Effort: **6–8h**.
Lab outline: color audit + accessible palette; encode "verified / unverified / planner-ready / blocked" in a small, principled palette.
Lab output: `design/foundations/topic-10-color-tokens.md`.

### Topic 11 — Web design / grid layout

| Source | Type |
|---|---|
| Josef Müller-Brockmann — *Grid Systems in Graphic Design* (chapters on grid construction) | P |
| MDN — CSS Grid + Flexbox reference | A |
| Material Design — Layout (responsive grid, breakpoints, 8pt) | A |
| Smashing Magazine — responsive grids in production | X |

Effort: **5–7h**.
Lab outline: grid audit of the browser; define a column system, breakpoint set, and a card-to-table transition rule that works on the chosen grid.
Lab output: `design/foundations/topic-11-grid-layout.md`.

### Topic 12 — Design systems

| Source | Type |
|---|---|
| Brad Frost — *Atomic Design* | P |
| Nathan Curtis — design system articles (EightShapes) | P |
| Material / Apple HIG / IBM Carbon / GOV.UK DS — comparative read | A |
| Figma — design tokens specification | X |

Effort: **6–8h**.
Lab outline: stitch Lab 02 (component rules), Lab 09 (type), Lab 10 (color), Lab 11 (grid) into a single CodeMike design-system v0 — tokens, atoms, molecules, organisms.
Lab output: `design/foundations/codemike-design-system-v0.md`.

---

## 3. Recommended execution order

This order interleaves topic execution with the gates already locked in §1:

```text
1.   Close Topic 1 revisions (quiz answers, viva answers, v2 visual verification)
2.   Execute Topic 2 (reading → source comparison → Lab 02 → rule sheet)
3.   Execute Topic 3 (reading → source comparison → Lab 03 → journey map + UX gate)
     ──── Gate: implement Destination Master Browser v1.1 here ────
4.   Execute Topic 4 (Design thinking)
5.   Execute Topic 5 (HCD)
6.   Execute Topic 6 (Gestalt)
     ──── Gate: interim grade report v2 ────
7.   Execute Topic 7 (Fitts' law)
8.   Execute Topic 8 (Button states)
9.   Execute Topic 9 (Typography)
10.  Execute Topic 10 (Color theory)
11.  Execute Topic 11 (Web design / grid layout)
12.  Execute Topic 12 (Design systems) — stitches the previous topics into a v0 design system
     ──── Gate: final dashboard build at docs/design-foundations.html ────
13.  Final synthesis + readiness statement + submission-v1 + final grade report
     ──── Gate: benchmark promotion review ────
```

Total estimated effort after Topic 1 close-out: **~60–80h focused work**, spread across however many calendar weeks the user wants.

## 4. Per-step deliverables (so each step is "done"-able)

For each topic, "done" means all of the following exist and are linked from the dashboard:

1. `lectures/lecture-NN-*.md` ✱
2. `readings/topic-NN-*-reading-pack.md` ✱
3. `design/foundations/topic-NN-*.md` — the deep-reading + source-comparison + browser-application doc (the rubric's evidence)
4. `labs/lab-NN-*.md` ✱
5. `submissions/lab-NN-*-results.md` — the executed lab evidence
6. `quizzes/quiz-NN-*.md` + `-answer-key.md` + `-answers.md` ✱
7. `viva/viva-NN-*.md` — three viva-style questions with answers
8. `learning-log.md` entry for the topic
9. `competency-map.md` rows flipped to Complete
10. Dashboard row in `docs/design-foundations.html` updated

✱ The Topic 2 PR shipped items 1, 2, 4, and 6 (minus the `-answers.md`). The remaining items are the execution work.

## 5. Dashboard reconciliation (one-time)

Independent of topic execution. Should land before Topic 3 ships so all subsequent topics point at the canonical artifact.

Steps:

1. `git mv docs/design-foundations-v2.html docs/design-foundations.html`
2. Update references in:
   - `curriculum/courses/des-001-design-foundations/submissions/DES-001-submission.md`
   - `curriculum/courses/des-001-design-foundations/learning-log.md`
   - `curriculum/courses/des-001-design-foundations/feedback/DES-001-grade-report-v1.md`
   - `curriculum/courses/des-001-design-foundations/revisions/DES-001-revision-plan-v1.md`
   - `design/foundations/*` files that mention v2
3. Live visual verification (the open item from the grade report) is done against the canonical filename, not v2.

## 6. Decision gates — when to pause

The plan has three pauses where a human decision is the right next step rather than more execution:

- **Gate 1 (after Topic 3):** confirm v1.1 implementation scope. The Lab 02 + Lab 03 outputs should make v1.1's component and journey changes obvious. If they don't, the rules are under-specified — fix the rules before building.
- **Gate 2 (after Topic 6):** interim grade report v2. Halfway through scope is a natural marking point. If the grade is below the Topic 1 baseline, something has slipped and Topics 7–12 shouldn't start until the cause is found.
- **Gate 3 (after Topic 12):** final dashboard build + readiness statement + final grade. Benchmark promotion is a separate decision after the final grade, per §13 of the brief.

## 7. Risks called out up front

- **Source drift.** Some primary sources (Wertheimer, Itten, Albers, Bringhurst, Müller-Brockmann) are books. Reading "via authoritative secondary source" is faster but the rubric's primary-source requirement softens. Mitigation: name the secondary source explicitly and quote the primary where possible.
- **Topic overlap.** Topics 2 / 8 (states) and Topics 9 / 10 / 11 / 12 (visual / system) overlap by design. Mitigation: each later topic must add depth, not duplicate; that's enforced by the per-topic "what is new vs Topic N-1" section in the deep-reading doc.
- **Lab execution backlog.** It is tempting to scaffold ahead and let labs slip. Topic 1 only graded 82 because the lab was executed. Mitigation: §1.2's "per-topic" sequencing — no scaffolding Topic N+1 while Topic N's lab is unexecuted.

## 8. What this plan does NOT do

- It does not write Topic 2's source-comparison notes — that is the first execution step.
- It does not run Lab 02.
- It does not implement Browser v1.1.
- It does not change scope on its own — §1's four decisions need explicit confirmation first.

When the user confirms (or amends) §1's decisions, the next action is: close Topic 1 revisions, then execute Topic 2.
