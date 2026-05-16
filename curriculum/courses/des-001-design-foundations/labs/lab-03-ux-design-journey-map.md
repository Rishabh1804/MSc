# Lab 03 — UX Design Journey Map and Acceptance Criteria

## Lab objective

Convert Topic 3's reading evidence into applied coursework evidence by mapping the full reviewer journey for the Destination Master Browser and producing a *UX acceptance-criteria sheet* — the journey-level companion to Topic 2's component rule sheet. The acceptance-criteria sheet becomes Browser v1.1's UX gate; the component rule sheet is its component gate. Both are required before v1.1 code lands.

Target artifact:

```text
docs/destination-master-browser-v1.0.html
```

## Materials

- `curriculum/courses/des-001-design-foundations/lectures/lecture-03-ux-design.md`
- `curriculum/courses/des-001-design-foundations/readings/topic-03-ux-design-reading-pack.md`
- `design/foundations/topic-03-ux-design.md` (deep-reading doc, PR A)
- `design/foundations/topic-01-ui-vs-ux-exercise-results.md` (Lab 01 — heuristic-level journey map)
- `design/foundations/topic-02-ui-design-component-inventory.md` + `ui-design-component-rules.md` (Topic 2 component rule sheet)
- `design/checklists/master-browser-design-checklist.md`
- `docs/destination-master-browser-v1.0.html`

## Lab steps

### Step 1 — Full reviewer journey map

For each of the seven reviewer-journey steps from Lecture 03, record:

- **goal** — what the reviewer is trying to achieve (in user-need form: *as a reviewer, I need [outcome], so that [goal]*)
- **cost budget** — max interactions, time, or cognitive load before the step is "too expensive"
- **failure mode** — what goes wrong if the step is poorly supported
- **trust check** — what trust signal must be visible at this depth
- **current v1 state** — does v1 support this step? Pass / partial / fail, with evidence
- **gap vs Lab 01** — what does this step's analysis add beyond Lab 01 Exercise B?

Output a table with one row per step.

### Step 2 — UX acceptance criteria

For each step, write 1–3 acceptance criteria. Each criterion must be:

- **testable** — a second evaluator can apply it to a design and produce the same verdict
- **behavioural** — describes what the reviewer can do, not what the UI looks like
- **independent of UI mechanism** — does not name dropdowns, chips, drawers, etc.
- **measurable** — has a budget (interactions / time / scroll / clicks) where applicable

Cross-reference each criterion to:
- the journey step it serves (Step 1)
- the Lab 01 heuristic finding it closes (if any)
- the Topic 2 rule-sheet component(s) that implement it

### Step 3 — User-need extraction

For each currently-implemented browser feature and each v1.1 backlog item, write the underlying user need in GOV.UK form:

```text
As a [reviewer], I need [outcome], so that [goal].
```

Then mark each as:
- **need** (passes the test — names outcome, not mechanism)
- **request** (came from a user but names a mechanism)
- **solution-shape** (designer assumption, no user evidence)

This produces a need-vs-request audit that will gate further v1.1 additions.

### Step 4 — Gap analysis vs Lab 01

For each Lab 01 finding (UI inventory, journey-map step, heuristic finding, UX Honeycomb score), state:

- whether Lab 03 confirms, refines, or contradicts it
- whether Lab 03 produces a testable criterion that closes the finding
- whether the finding can be marked Closed after v1.1 lands

The gap analysis is the bridge between Lab 01's heuristic-level findings and Lab 03's behavioural-level criteria.

### Step 5 — Consolidated UX acceptance-criteria sheet

Combine Steps 1–4 into `design/foundations/ux-acceptance-criteria.md`. Structure:

1. Reviewer-journey map (the seven steps with goal / cost / failure / trust / criteria)
2. The full criteria list (numbered, traceable, cross-referenced to rule sheet)
3. User-need extraction (need / request / solution-shape audit)
4. Lab 01 → Lab 03 gap-analysis table
5. v1.1 UX gates (the subset of criteria that *must* pass for v1.1 to ship)
6. Hand-off note to Browser v1.1 implementation

This file is the *journey-level companion* to `design/foundations/ui-design-component-rules.md`. Both are required.

### Step 6 — Checklist gates and Topic 3 anti-patterns

Append a Topic 3 section to `design/checklists/master-browser-design-checklist.md` containing:

- the four UX gates (criterion-presence, behaviour-testability, need-vs-request, journey-completeness)
- the four UX anti-patterns specific to data-review tools
- a canonical pointer to the acceptance-criteria sheet

## Expected outputs

```text
design/foundations/topic-03-ux-design-journey-map.md           — Lab Steps 1-4 evidence
design/foundations/ux-acceptance-criteria.md                   — Lab Step 5 consolidated sheet (Browser v1.1's UX gate)
curriculum/courses/des-001-design-foundations/submissions/
  lab-03-ux-design-journey-map-results.md                      — formal lab submission
design/checklists/master-browser-design-checklist.md           — Topic 3 section appended (§20 + §21)
```

## Submission checklist

- Reviewer-journey map completed for all seven steps (Step 1)
- 7–15 UX acceptance criteria produced, each cross-referenced to journey step + rule-sheet component + Lab 01 finding (Step 2)
- User-need / request / solution-shape audit completed (Step 3)
- Lab 01 → Lab 03 gap analysis completed (Step 4)
- Consolidated acceptance-criteria sheet at `design/foundations/ux-acceptance-criteria.md` (Step 5)
- Master-browser checklist updated with Topic 3 section (Step 6)
- Findings cross-referenced against Lab 01 and Lab 02 (no duplication)

## Rubric alignment

- *Multi-source coverage* — every criterion cites the source(s) it derives from
- *Application to CodeMike/browser* — every criterion ties to a reviewer task
- *Checklist/actionability* — the criteria sheet is the next-step input for v1.1
- *Academic discipline* — criteria are versioned and traceable

## Decision gate before closing the lab

Lab 03 is complete when a second evaluator, given the acceptance-criteria sheet and the v1 browser, would produce the same pass/fail verdict for each criterion. If two evaluators diverge on more than one criterion, the criterion is under-specified and must be tightened before v1.1 implementation begins.

This is the *reproducibility* test: behavioural criteria must produce the same verdict across evaluators, by design.
