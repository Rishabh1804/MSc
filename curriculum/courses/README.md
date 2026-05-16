# CodeMike MSc Course Environment

This folder turns the repository into a simulated postgraduate course environment rather than a loose collection of notes and artifacts.

The course model is:

```text
syllabus → lectures → readings → labs → assignments → submissions → grading → feedback → revision → portfolio output
```

## Active courses

| Course | Status | Current topic | Primary artifact | Grade status |
|---|---|---|---|---|
| DES-001 Design Foundations | Active | Topic 1 — UI vs UX | `docs/design-foundations-v2.html` | Pending formal grading |

## Standard course folder pattern

Each course should follow this structure:

```text
courses/<course-id-course-name>/
  README.md
  syllabus.md
  weekly-plan.md
  learning-outcomes.md
  grading-policy.md
  competency-map.md
  learning-log.md
  lectures/
  readings/
  labs/
  quizzes/
  assignments/
  submissions/
  feedback/
  revisions/
  viva/
  portfolio/
```

## Course quality rules

1. Every topic should have readings from multiple source types.
2. Every lecture should translate concepts into CodeMike project implications.
3. Every lab should produce an execution artifact.
4. Every assignment should have a submission, grading report, feedback, and revision plan.
5. Every course should maintain a competency map.
6. Portfolio outputs should extract reusable project value from coursework.

## Academic levels

The simulated grading model uses:

| Level | Meaning |
|---|---|
| Fail | Does not meet minimum assignment requirements |
| Pass | Meets core requirements |
| Merit | Good synthesis, source use, and application |
| Distinction | Strong evidence, execution, reflection, and revision |
| High Distinction | Excellent synthesis, applied originality, rigorous evidence, and portfolio-quality output |

## Reuse rule

When a new MSc topic or course starts, copy the same pattern from DES-001 rather than inventing a new workflow.
