# Repository Structure Standard

This file defines the intended structure for the MSc repository.

## Top-level folders

```text
assignments/   Assignment briefs and rubrics
courses/       Course simulation environment and evidence trail
datasets/      Source/reference data
design/        Design standards, checklists, and foundation notes
docs/          Renderable HTML/public artifacts
scripts/       Build and validation utilities
```

## Folder responsibilities

### `courses/`

Use for academic process and evidence.

Allowed contents:

```text
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

### `docs/`

Use for files that are meant to be opened or rendered directly, especially HTML artifacts.

Allowed examples:

```text
docs/design-foundations-v2.html
docs/design-foundations-app/
docs/destination-master-browser-v1.html
```

Do not put long academic evidence directly into large HTML files. Keep HTML as presentation shell and load data/modules where possible.

### `design/`

Use for reusable design knowledge and standards.

Allowed examples:

```text
design/checklists/
design/foundations/
```

Keep course-specific grading, submissions, feedback, and logs under `courses/`, not `design/`.

### `assignments/`

Use for assignment briefs and rubrics only. Do not place submissions here.

### `datasets/`

Use for CSV/JSON/reference datasets. Data should not be mixed with coursework notes.

### `scripts/`

Use for build or validation scripts. Scripts should document their expected inputs and outputs.

## Naming conventions

Use stable prefixes:

| Type | Example |
|---|---|
| Topic note | `topic-02-what-is-ui-design.md` |
| Lecture | `lecture-02-what-is-ui-design.md` |
| Reading pack | `topic-02-what-is-ui-design-reading-pack.md` |
| Lab | `lab-02-ui-component-inventory.md` |
| Lab result | `lab-02-ui-component-inventory-results.md` |
| Grade report | `DES-001-grade-report-v1.md` |
| Revision plan | `DES-001-revision-plan-v1.md` |

## Anti-sprawl rules

1. Avoid one-off folders unless they match the course pattern.
2. Do not duplicate the same evidence in multiple places; link to the canonical source.
3. Use a course submission file as the index for evidence, not as a copy of every artifact.
4. Prefer small source files plus generated/rendered artifacts.
5. Move obsolete or superseded files to an archive only after they are clearly replaced.

## Current cleanup decision

The repository is not being mass-moved immediately. Instead:

1. establish this structure standard
2. use it for all new work
3. migrate messy files in planned batches
4. avoid single-file commit sprawl
