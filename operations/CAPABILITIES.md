# CAPABILITIES.md — CodeMike Capability Catalogue

Skills are small. Capabilities are reusable packages of skill, judgement, method, evidence, and transfer value.

## Capability Maturity

| Level | Meaning |
|---:|---|
| 0 | Idea only |
| 1 | Draft method |
| 2 | Prototype evidence |
| 3 | Reusable pattern |
| 4 | Transferred to project |
| 5 | Maintained capability with examples and limitations |

## Initial Capability Targets

| Capability | Maturity | Purpose | Next action |
|---|---:|---|---|
| Data cleaning | 0 | Convert messy data into analysis-ready datasets | Create checklist |
| Exploratory analysis | 0 | Understand data structure, quality, and patterns | Build first EDA notebook |
| Recommendation scoring | 0 | Rank options using criteria, weights, constraints, and penalties | Define pattern |
| Optimisation modelling | 0 | Convert constraints and objectives into solvable problems | Create template |
| Model evaluation | 0 | Evaluate models against baselines and risks | Create evaluation checklist |
| Dashboard insight design | 0 | Convert data into decision-support visual interfaces | Define dashboard pattern |
| Research synthesis | 0 | Turn sources into useful methods and limitations | Create paper summary template |
| HPC performance profiling | 0 | Measure runtime, memory, and scaling behaviour | Define benchmark basics |
| Master-detail-with-faceted-search pattern card | 4 | Name the pattern for any data-review tool (table + drawer + filter chips + persistent stats + four-depth trust signal); pattern-first design replaces component-by-component invention | DES-001 Topic 2 deep-reading doc §6.1 + `ui-design-component-rules.md` §3.6 + **transferred to Destination Master Browser v1.1** (`docs/destination-master-browser.html`; 15/15 walk-through pass 2026-05-16) | Promote to a formal capability card under `capabilities/` after 3–4 more transfers accumulate |
| Nine-state interactive checklist | 4 | Audit every interactive's state coverage (default / hover / focus / active / disabled / loading / empty / error / success); loading/empty/error are first-class | `topic-02-ui-design-component-inventory.md` Step 2 + `ui-design-component-rules.md` §2 + **applied as a v1.1 gate** (every interactive in v1.1 satisfies the matrix; loading/empty/error are distinct components per U-REC-2) | Apply to next data-review tool |
| Affordance-signifier-feedback triple-check | 4 | Per-control review item (Norman): every interactive answers what-it-does, how-the-user-knows, what-they-see-when-it-happens | `topic-02-ui-design-component-inventory.md` Step 3 + `ui-design-component-rules.md` §5 + **applied during v1.1 implementation** (focus rings, hover/active states, count-flash for feedback) | Apply during reviews of future UI work |
| Seven-step reviewer-journey template | 4 | Reusable journey-map shape for data-review tools (arrive / understand / narrow / compare / inspect / recover / leave); each step has goal / cost / failure-mode / trust-check | `topic-03-ux-design.md` §7 + `topic-03-ux-design-journey-map.md` Step 1 + **applied to v1.1** (all seven steps PASS in the 15/15 walk-through) | Apply to next data-review tool (datasets browser, validator review, Planner review) |
| UX acceptance-criterion form | 4 | Workspace-wide form for testable, behavioural, mechanism-independent UX criteria: *"The reviewer can [behaviour], in [cost budget], with [feedback requirement]"* | `topic-03-ux-design.md` §8 + `ux-acceptance-criteria.md` (14-criterion exemplar) + **proved reproducible by the 15/15 Playwright walk-through** (every criterion has a pass/fail test) | Adopt as the default UX-criterion form for any future product decision |
| User-need vs request vs solution-shape triage | 4 | GOV.UK-derived classification preventing solution-shape thinking from passing as user needs; every backlog item must produce a user need in GOV.UK form (no UI mechanism named) | `topic-03-ux-design.md` §6 + `topic-03-ux-design-journey-map.md` Step 3 (22-item audit) + **applied to the v1.1 backlog** (every item passed the need-vs-request gate before implementation) | Adopt as default intake discipline for any product decision |

## Capability Card Template

```md
# Capability: <name>

## What this capability does

## Inputs

## Outputs

## Method

## Current maturity

## Evidence

## Limitations

## Reusable in

## Transfer history

## Next action
```
