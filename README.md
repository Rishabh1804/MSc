# CodeMike MSc Repository

This repository is the working academic and project repository for the CodeMike MSc simulation.

The repository must stay navigable. Academic performance depends on clear evidence, clear submissions, and clear separation between coursework, reusable project artifacts, and generated/output files.

## Repository map

Open the visual map first:

```text
docs/repo-map.html
```

If served through GitHub Pages, use one of these depending on Pages configuration:

```text
https://rishabh1804.github.io/MSc/docs/repo-map.html
https://rishabh1804.github.io/MSc/repo-map.html
```

## Current active course

| Course | Status | Current next step |
|---|---|---|
| DES-001 Design Foundations | Active — Topic 1 graded provisional Excellent/Distinction (82/100); Topic 2 scaffolded | Execute Topic 2 reading (five required sources) and run Lab 02 |

## Primary locations

| Folder | Purpose |
|---|---|
| `charter/` | Slow-change policy and rule docs (hard rules, structure, budget, tooling, etc.) |
| `operations/` | Live registers and logs (skill map, project log, evidence, next actions, etc.) |
| `capabilities/` | Reusable capability cards, patterns, anti-patterns, case studies, decision science |
| `curriculum/courses/` | Course environment: syllabus, lectures, readings, labs, submissions, feedback, revisions, viva, portfolio |
| `curriculum/assignments/` | Assignment briefs and rubrics |
| `curriculum/modules/` | Per-module workspaces (00-foundations … 09-capstone) |
| `curriculum/thesis/` | Capstone thesis workspace |
| `cockpit/` | PWA source — operating view of the workspace; fetches `operations/` data at runtime |
| `decks/` | Slide-deck HTML source; `.pptx` is a workflow artifact, not committed |
| `docs/` | Renderable/public artifacts and browser dashboards |
| `design/` | Reusable design foundations, checklists, and design standards |
| `datasets/` | Data inputs, reference files, and synthetic samples + generators |
| `notebooks/` | Exploratory notebooks |
| `projects/` | Active project work |
| `prompts/` | Reusable prompt templates |
| `references/` | Cited literature and academic references |
| `reports/` | Evidence reports |
| `src/` | Reusable library code |
| `.github/scripts/` | Build, validation, or utility scripts (deck export, link sweep) |

See `charter/REPO_STRUCTURE.md` for the authoritative layout standard and `operations/MIGRATION_LOG.md` for the per-batch record of how the repository reached this state.

## Active artifacts

| Artifact | Path |
|---|---|
| Repository visual map | `docs/repo-map.html` |
| Design Foundations dashboard v2 | `docs/design-foundations-v2.html` |
| Design Foundations app modules | `docs/design-foundations-app/` |
| Destination Master Browser v1 | `docs/destination-master-browser-v1.html` |
| DES-001 course folder | `curriculum/courses/des-001-design-foundations/` |
| CodeMike Cockpit (PWA) | `cockpit/` (deployed to GitHub Pages via `.github/workflows/cockpit-build.yml`) |

## Working rule

Do not create files casually. Every new file must be one of:

1. course evidence
2. public/rendered artifact
3. reusable design standard/checklist
4. dataset/source file
5. script/tooling
6. index/governance file

If a file does not fit one of those buckets, it should not be added.

## GitHub workflow rule

For future work, prefer one batched commit per phase instead of many one-file commits. See `charter/GITHUB_WORKFLOW.md`.
