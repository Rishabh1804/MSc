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
| Design-thinking loop template (8-step) | 4 | Reusable 8-step loop shape (Pick pain point → Empathize → Define → Ideate ≥3 candidates → Three-constraint triage → Prototype-spec → Test-spec with falsification criteria → Decision) for design-thinking work when problems aren't well-framed | DES-001 Topic 4 deep-reading doc §6 + Lab 04 Loop 1 (`design/foundations/topic-04-design-thinking-loop.md` — batch-promote-confirm; Candidate B chosen via comparative triage) | Apply to any future not-well-framed product problem; second loop unlocks "single-pass design thinking" anti-pattern closure |
| Three-constraint triage frame (desirability / feasibility / viability) | 4 | Brown's three-constraint frame as the default decision form for v1.2+ candidates; each cell cites sourced evidence rather than opinion | DES-001 Topic 4 deep-reading doc §6 + Lab 04 Step 5 (four candidates × three constraints with comparative reasoning) | Adopt as default candidate-selection form for any product decision involving trade-offs |
| Problem-framing decision tree (Topic 4 first vs Topic 3 first) | 4 | Three-condition test (user-need writable without speculation; tested-success answerable; criterion measurable) that decides whether a problem is well-framed enough to skip Topic 4 and go straight to criteria-writing | DES-001 Topic 4 deep-reading doc §9 + master-browser checklist §23 problem-framing gate | Apply to every v1.2+ backlog item before scoping; saves loop-overhead on well-framed problems |
| HCD self-audit gate (four cells) | 4 | Standards-grade lifecycle gate (ISO 9241-210): every backlog item names (a) context of use, (b) user requirement, (c) design solution shape, (d) evaluation that would confirm it works; any empty cell returns the item to the missing activity | DES-001 Topic 5 deep-reading doc §10 + Lab 05 Audit 1 Step 7 + master-browser checklist §26 | Apply to every v1.2 backlog item; catches missing-activity drift at the per-item level |
| HCD audit template (Steps 1–7) | 4 | Reusable audit shape (Activity 1 / 2 / 3 / 4 / six-principle / W3C-triad / findings + prioritised leverage-ranked list) applicable to any standards-grade lifecycle audit | DES-001 Topic 5 Lab 05 (`design/foundations/topic-05-hcd-audit.md` — Audit 1; 7 findings; 6-item prioritised v1.2 list) | Run Audit 2 after v1.2 ships; pattern transfers to any HCD-compliant workspace |
| W3C accessibility / usability / inclusion triad lens | 4 | Per-PR lens-by-lens evaluation of every v1.2 feature; the worst-served lens is named explicitly (no silent skipping); inclusion lens is the most-stretched and most-named-as-deferred for solo workspaces | DES-001 Topic 5 deep-reading doc §4 + Lab 05 Step 6 (Inclusion lens Fail explicitly recorded) + master-browser checklist §26 | Apply to every v1.2 feature; recruit Sponsor Reviewer when inclusion-lens findings become actionable |
| Gestalt audit template (Steps 1–6) | 4 | Reusable per-region per-principle audit shape (region selection → 6×6 principle matrix → conflict adjudication → density-vs-grouping audit → leverage-ranked v1.1.x / v1.2 fix list → checklist appendix) for any visual interface | DES-001 Topic 6 Lab 06 (`design/foundations/topic-06-gestalt-audit.md` — Audit 1; 36 cells; 6 findings + 1 meta; 6-item fix list) | Run on any future visual artifact; pattern transfers to any UI design review |
| Gestalt violation taxonomy (3 sub-types) | 4 | Diagnostic vocabulary for UI review: false-positive grouping / false-negative grouping / unresolved principle conflict — promotes "feels off" into named violations citing principle + region + reviewer-task impact | DES-001 Topic 6 deep-reading doc §6 + Lab 06 Audit 1 (6 findings each typed per the taxonomy) | Adopt as standard review vocabulary for any UI work |
| Density-vs-grouping audit pattern | 4 | Per-region audit asking: does density force a proximity compromise? if yes, is the compensating signal (divider / tint / alignment) explicit or silent? silent collapse = finding; explicit substitution = trade-off | DES-001 Topic 6 deep-reading doc §10 + Lab 06 Audit 1 Step 4 (F-GES-7 cross-cutting meta-finding) | Apply to any information-dense interface; not just data-review tools |
| Audit-shape as a workspace standard (cross-topic) | 4 | Reusable Steps 1–N pattern (artifact + framework selection → per-dimension matrix → conflict / gap analysis → findings + leverage-ranked prioritised fix list → checklist appendix). Demonstrated by Topic 5 + Topic 6 audits; pattern transfers to any future structured assessment | Topic 5 audit Steps 1–7 + Topic 6 audit Steps 1–6; cross-validated by Topic 6's confirmation of Topic 2's four-depth trust spec | Apply to any future workspace task requiring discipline-grade assessment of an artifact |

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
