# Lab 02 — UI Design Component Inventory and Rule Set

## Lab objective

Convert Topic 2 readings into applied evidence by inventorying every UI component pattern in the current Destination Master Browser, auditing its state coverage and affordance honesty, and producing a consolidated rule sheet that the Browser v1.1 redesign will follow.

Target artifact:

```text
docs/destination-master-browser-v1.0.html
```

## Materials

- `curriculum/courses/des-001-design-foundations/lectures/lecture-02-what-is-ui-design.md`
- `curriculum/courses/des-001-design-foundations/readings/topic-02-what-is-ui-design-reading-pack.md`
- `design/foundations/topic-01-ui-vs-ux-exercise-results.md` (Lab 01's UI inventory and heuristic audit)
- `design/checklists/master-browser-design-checklist.md`
- `docs/destination-master-browser-v1.0.html`

## Lab steps

### Step 1 — Component catalogue

For every distinct UI pattern in v1, record:

- pattern name (e.g. *record card*, *filter chip*, *stats banner*)
- element category (control / container / navigation / data display / feedback / editorial)
- the reviewer task it serves
- variants currently in use (e.g. *card – verified*, *card – unverified*)

Output a table with one row per pattern. This is the inventory.

### Step 2 — State coverage matrix

Build a matrix: rows are the patterns from Step 1, columns are the nine standard states (`default`, `hover`, `focus`, `active`, `disabled`, `loading`, `empty`, `error`, `success`). For each cell:

- ✓ if the state exists in v1
- ✗ if the state is missing but should exist
- — if the state does not apply

Highlight rows where loading / empty / error are missing — those are the data-honesty gaps.

### Step 3 — Affordance / signifier / feedback audit

For each interactive pattern (controls, plus any clickable containers), write three columns:

- **affordance** — what action it can perform
- **signifier** — how the reviewer knows it can perform that action
- **feedback** — what the reviewer sees when they perform it

A row where the signifier or feedback column is empty or guessed is a finding.

### Step 4 — Container-selection rules

For the four container patterns (`card`, `table`, `list`, `drawer`, `modal`), write explicit selection criteria:

- when each is the right choice for a reviewer task
- when each is wrong (anti-pattern)
- one Destination Master Browser task that fits each

Resolve the v1 question: *cards vs table mode for the main list*. Pick criteria; do not pick by aesthetics.

### Step 5 — Filter UI selection rules

For the four filter patterns (`search input`, `filter chip`, `dropdown`, `faceted panel`), write selection criteria. Specify which filters in v1 should use which pattern. The result should be reproducible: another reviewer applying the same criteria should pick the same patterns.

### Step 6 — Consolidated rule sheet

Combine Steps 1-5 into `design/foundations/ui-design-component-rules.md`. Structure:

1. Element vocabulary (from lecture)
2. State requirements per element category
3. Container-selection rules
4. Filter-UI rules
5. Affordance / signifier / feedback minimums
6. Anti-patterns to refuse

This file becomes the input to Browser v1.1.

## Expected outputs

```text
design/foundations/topic-02-ui-design-component-inventory.md
design/foundations/ui-design-component-rules.md
curriculum/courses/des-001-design-foundations/submissions/lab-02-ui-design-component-inventory.md
```

## Submission checklist

- Component catalogue completed (Step 1)
- State coverage matrix completed (Step 2)
- Affordance / signifier / feedback audit completed (Step 3)
- Container-selection rules drafted with criteria (Step 4)
- Filter-UI rules drafted with criteria (Step 5)
- Consolidated rule sheet produced (Step 6)
- v1.1 implications recorded against `design/checklists/master-browser-design-checklist.md`
- Findings cross-referenced against Lab 01 results (do not duplicate)

## Rubric alignment

This lab supports:

- *Multi-source coverage* (component patterns sourced from at least three design systems)
- *Application to CodeMike/browser context* (every rule must cite a specific reviewer task)
- *Checklist/actionability* (the rule sheet is the next-step input for v1.1)
- *Academic discipline/versioning* (rules versioned; superseded patterns are noted, not silently replaced)

## Decision gate before continuing

This lab is complete when a second reviewer, given the rule sheet and v1's screenshot, would produce the same container and filter decisions for two new records added to the dataset. If two reviewers diverge on which container to use, a rule is missing and the lab is not yet done.
