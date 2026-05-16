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
| Master-detail-with-faceted-search pattern card | 3 | Name the pattern for any data-review tool (table + drawer + filter chips + persistent stats + four-depth trust signal); pattern-first design replaces component-by-component invention | DES-001 Topic 2 deep-reading doc §6.1 + `ui-design-component-rules.md` §3.6 | Promote to a formal capability card under `capabilities/` after Browser v1.1 ships |
| Nine-state interactive checklist | 3 | Audit every interactive's state coverage (default / hover / focus / active / disabled / loading / empty / error / success); loading/empty/error are first-class | `topic-02-ui-design-component-inventory.md` Step 2 + `ui-design-component-rules.md` §2 | Apply to Browser v1.1 components as the v1.1 readiness gate |
| Affordance-signifier-feedback triple-check | 3 | Per-control review item (Norman): every interactive answers what-it-does, how-the-user-knows, what-they-see-when-it-happens | `topic-02-ui-design-component-inventory.md` Step 3 + `ui-design-component-rules.md` §5 | Apply during Browser v1.1 implementation reviews |
| Seven-step reviewer-journey template | 3 | Reusable journey-map shape for data-review tools (arrive / understand / narrow / compare / inspect / recover / leave); each step has goal / cost / failure-mode / trust-check | `topic-03-ux-design.md` §7 + `topic-03-ux-design-journey-map.md` Step 1 | Apply to next data-review tool (e.g. validator review, Planner review) |
| UX acceptance-criterion form | 3 | Workspace-wide form for testable, behavioural, mechanism-independent UX criteria: *"The reviewer can [behaviour], in [cost budget], with [feedback requirement]"* | `topic-03-ux-design.md` §8 + `ux-acceptance-criteria.md` (14-criterion exemplar) | Adopt as the default UX-criterion form for any future product decision |
| User-need vs request vs solution-shape triage | 3 | GOV.UK-derived classification preventing solution-shape thinking from passing as user needs; every backlog item must produce a user need in GOV.UK form (no UI mechanism named) | `topic-03-ux-design.md` §6 + `topic-03-ux-design-journey-map.md` Step 3 (22-item audit) | Adopt as default intake discipline for any product decision |

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
