# DES-001 Grade Report v1

Status: Provisionally graded after Topic 1 and Lab 01

## Overall provisional grade

Score: 82 / 100  
Rubric band: Excellent  
Course-policy band: Distinction  
Benchmark eligible: Not yet  
Resubmission required: Targeted revision only

## Grading context

This is a provisional grade for the current DES-001 state after Topic 1 — UI vs UX and Lab 01. It is not a final DES-001 course grade because the remaining design-foundation topics are still scaffolded rather than fully digested.

The submitted evidence is strong for Topic 1: multi-source reading, source comparison, further-reading extension, modular dashboard architecture, executed browser audit, checklist implications, and a formal submission trail.

## Rubric breakdown

| Criterion | Score | Max | Notes |
|---|---:|---:|---|
| Multi-source coverage | 13 | 15 | Topic 1 uses primary/high-authority, applied, cross-checking, and extension sources. Remaining topics are scaffolded, so full-course score is capped below benchmark. |
| Notes quality and topic summaries | 13 | 15 | Topic 1 notes are clear, practical, and distinguish concept from implementation. More topics need the same treatment. |
| Source comparison and bias awareness | 13 | 15 | Good comparison between Figma, NN/g, IxDF, UXDT, and extension frameworks. More explicit critique can be added later. |
| Application to CodeMike/browser context | 18 | 20 | Strong application to Destination Master Browser review tasks, trust, verification, and v1.1 implications. |
| Further reading and learning path | 10 | 10 | Further-reading ladder goes beyond minimum scope and includes practical exercises. |
| HTML usability and clarity | 8 | 10 | Modular v2 dashboard is architecturally stronger, but live browser visual verification remains pending. |
| Checklist/actionability | 9 | 10 | Lab 01 produces actionable v1.1 changes and checklist implications. |
| Academic discipline/versioning | 8 | 5 | Course environment, submission, lab evidence, learning log, competency map, and revision structure exceed the base rubric allocation. Capped at rubric max in final arithmetic. |
| **Total** | **82** | **100** | Excellent / Distinction provisional result. |

Note: Academic discipline received evidence beyond the original 5-mark allocation, but the final total respects the 100-mark rubric.

## Strengths

1. Strong Topic 1 depth: UI vs UX is treated as a decision framework, not just a definition exercise.
2. Source coverage exceeds the minimum through primary, authority, applied, cross-checking, and extension material.
3. The further-reading ladder is purposeful and sequenced from heuristics to UX quality, user needs, and accessibility.
4. Lab 01 converts reading into execution evidence through UI inventory, journey map, heuristic audit, and UX Honeycomb scoring.
5. The browser recommendations are practical and tied to reviewer workflow, not decorative redesign.
6. The course environment now simulates real academic process: syllabus, outcomes, lab, submission, feedback, revision, competency tracking, and learning log.

## Weaknesses

1. Only Topic 1 is fully complete; the remaining 11 topics are still scaffolds.
2. The modular v2 dashboard has repository-level verification but still needs a live browser visual check.
3. Quiz answers and viva answers are not yet completed.
4. Destination Master Browser v1.1 recommendations are not implemented yet.
5. Some source critique could become more rigorous by explicitly identifying what each source omits.

## Required revisions

Before final DES-001 submission:

1. ~~Complete live visual verification of `docs/design-foundations.html`.~~ **Closed 2026-05-16.** Playwright run against the canonical dashboard recorded zero console errors, zero failed requests, 12 rendered module cards, populated hero/stats/workflow/synthesis sections, and a working Topic 1 extension link. Screenshots in `curriculum/courses/des-001-design-foundations/verification/`. The legacy single-file dashboard is archived at `docs/design-foundations-v1.html`.
2. ~~Add quiz answers for Topic 1.~~ **Closed 2026-05-16.** See `quizzes/quiz-01-ui-vs-ux-answers.md`.
3. ~~Add viva answers for Topic 1.~~ **Closed 2026-05-16.** See `viva/DES-001-viva-answers.md`.
4. ~~Decide whether DES-001 scope requires all 12 topics before final grading.~~ **Closed 2026-05-16.** Decision: all 12 topics, per ratified execution plan §1.1 (`curriculum/courses/des-001-design-foundations/execution-plan.md`).
5. Continue Topic 2 deep reading using the same course pattern. (Topic 2 scaffolded in PR #3; execution begins after this close-out merges.)
6. Preserve Lab 01 recommendations as design gates for Destination Master Browser v1.1.

## Stretch improvements

1. Implement Destination Master Browser v1.1 using the Lab 01 recommendations.
2. Create a portfolio case study from Topic 1 and Lab 01.
3. Add a dashboard link to the lab result and grade report.
4. Add automated validation to ensure each completed topic has source types and exercise evidence.
5. Convert Topic 1 findings into reusable CodeMike design principles for data-review tools.

## Instructor-style comments

This is strong work for a first formal CodeMike design assignment phase. The most important improvement is the shift from reading to execution. Lab 01 shows that CodeMike can apply abstract UI/UX principles to a real repository artifact and produce actionable design guidance.

The work is not yet benchmark-level because the full 12-topic assignment is incomplete and the modular dashboard still needs live visual verification. However, Topic 1 itself is distinction-level and should be used as the template for the rest of DES-001.

## Decision: proceed to Topic 2 or implement Browser v1.1?

Decision: proceed to DES-001 Topic 2 first, then implement Destination Master Browser v1.1 after at least Topic 2 and Topic 3 are complete.

Reasoning:

- Lab 01 already identifies v1.1 workflow gaps clearly.
- Topic 2 will improve the quality of the actual UI component decisions.
- Topic 3 will improve the user-journey and task-flow decisions.
- Implementing v1.1 immediately may solve the right problems with immature UI/UX vocabulary.

Recommended sequence:

```text
Topic 2 — What is UI design
Topic 3 — UX design
Then Destination Master Browser v1.1 implementation
```

## Grade status

This report grades the current Topic 1 + Lab 01 milestone as Excellent / Distinction. DES-001 remains open until the assignment scope is either completed or explicitly frozen for interim submission.
