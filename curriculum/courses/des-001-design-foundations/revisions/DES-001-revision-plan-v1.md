# DES-001 Revision Plan v1

Status: Active after grade report

## Revision trigger

Grade report v1 assigned the current Topic 1 + Lab 01 milestone:

```text
82 / 100 — Excellent / Distinction provisional
```

DES-001 remains open because only Topic 1 has been completed in full. The remaining topics are scaffolded.

## Required revisions before final DES-001 submission

1. ~~Complete live visual verification of `docs/design-foundations.html`.~~ **Closed 2026-05-16.** Playwright verification passed all six promotion-rule conditions documented in `docs/design-foundations-app/README.md`. Screenshots in `curriculum/courses/des-001-design-foundations/verification/`. The legacy single-file dashboard is archived at `docs/design-foundations-v1.html`.
2. ~~Add Topic 1 quiz answers.~~ **Closed 2026-05-16.** See `quizzes/quiz-01-ui-vs-ux-answers.md`.
3. ~~Add Topic 1 viva answers.~~ **Closed 2026-05-16.** See `viva/DES-001-viva-answers.md`.
4. ~~Continue Topic 2 — What is UI design — with the same course pattern.~~ **Closed 2026-05-16.** Topic 2 fully digested across two PRs: PR A produced the deep-reading doc + source comparison + quiz answers + viva answers + data.js update; PR B produced Lab 02 (component inventory + state matrix + affordance audit) + the consolidated rule sheet at `design/foundations/ui-design-component-rules.md` + six new gates in the master-browser checklist (§18) + the canonical rule-sheet pointer (§19).
5. Continue Topic 3 — UX design — before implementing Browser v1.1.
6. Keep Lab 01 recommendations as formal v1.1 design gates. (Topic 2's rule sheet supersedes them at the component level while preserving the workflow-completion and trust-preservation framing.)

## Stretch revisions

1. Add a dashboard link to the Lab 01 results.
2. Add a dashboard link to the grade report.
3. Create a portfolio case study from Topic 1 and Lab 01.
4. Add automated topic-completion validation for source types, exercise evidence, and submission links.
5. Convert Topic 1 principles into reusable CodeMike design principles for data-review tools.

## Decision from grade report

Proceed to DES-001 Topic 2 before implementing Destination Master Browser v1.1.

Rationale:

- Lab 01 already identifies the workflow gaps.
- Topic 2 will improve component-level UI decisions.
- Topic 3 will improve UX journey and task-flow decisions.
- Browser v1.1 should be implemented after stronger UI and UX vocabulary is available.

Recommended sequence:

```text
Topic 2 — What is UI design
Topic 3 — UX design
Destination Master Browser v1.1 implementation
```

## Revision log

| Date | Change | Reason |
|---|---|---|
| 2026-05-14 | Created revision shell | Prepare grading and revision workflow |
| 2026-05-14 | Activated revision plan after grade report | Lab 01 complete and provisional grade assigned |
| 2026-05-16 | Ratified 12-topic scope + per-topic sequencing + v1.1-after-Topic-3 + dashboard rename | See `execution-plan.md` §1 |
| 2026-05-16 | Closed Topic 1 revision items 1-4 | Visual verification passed, quiz answers + viva answers written, scope decision ratified |
| 2026-05-16 | Closed Topic 2 (revision item 4 of this plan) | Deep reading + source comparison + Lab 02 + consolidated rule sheet + checklist gates. PR A and PR B. |
| 2026-05-16 | Grade report v2 issued | Cumulative grade 87/100 (Excellent / Distinction) after Lyra-flagged reconciliation of v1's hidden scope-incompleteness deduction (subscore sum 93 minus explicit −6 adjustment). Topic 2 standalone 96/100. See `feedback/DES-001-grade-report-v2.md`. |
