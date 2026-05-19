# SKILL_MAP.md — CodeMike Skill Map

This file tracks CodeMike's skill domains, maturity levels, evidence, and transfer readiness.

## Competency Ladder

| Level | Meaning |
|---:|---|
| 0 | Not started |
| 1 | Concept understood |
| 2 | Example reproduced |
| 3 | Exercise solved independently |
| 4 | Applied to real project |
| 5 | Reusable / teachable / template-ready |

## Rule

A skill should not move upward without evidence.

Accepted evidence includes notebooks, scripts, reports, benchmarks, evaluations, case studies, project transfers, or viva-style defence notes.

## Core Skill Domains

| Domain | Current level | Evidence | Next action |
|---|---:|---|---|
| Research methods | 0 | None yet | Create research workflow |
| Big Data Analytics | 2 | Destination-enrichment workstream 2026-05-18: store→refine→categorise→analyse run end-to-end on the 359-row master against the strategy doc v1 spec (P5); calibration findings recorded as durable text (§18); §19 policy revision adopted (no-assumption + live-data + free-tier-only). The discipline-grade backbone behind the §19 policy is the Big Data Analytics module — applied to a real workspace artifact, surfaced category-level findings, prompted policy revision. Cycle: spec → ship → calibration → policy revision. Evidence: `datasets/reference/destination_master_enrichment_strategy.md` §18 + §19 + §19.6 + EXP-003 (`operations/EXPERIMENTS.md`). | Repeat the cycle on P20 (v2 source-backed strategy doc) — the second worked example promotes to level 3 (Exercise solved independently). Source registry + free-tier ETL (P19) is the concrete next deliverable. |
| Data engineering | 2 | E1 v1.0 enrichment ship 2026-05-18: deterministic stdlib-only 10-step per-row pipeline (`src/codemike/data/destination_master_enrichment_v1.py`) + structural validator (`destination_master_enrichment_validation.py`) + JSON catchment lookup (`origin_catchment_v1.json`); 359 enriched rows; three manual-review queue CSVs; two evidence reports; readiness `enriched_structurally_valid_not_planner_ready`. Established the workspace's heuristic-baseline pattern per §19.2 — the v1 artifact is retained as diff target, not rolled back. Source-backed pipeline (P21) is the v2 follow-up. | Build P19 source registry + free-tier ETL split (stable-derived layer + live-volatile per-query fetch layer) per §19.6 two-tier architecture; build `destination_sources_v1.csv` (the source registry the v2 database strategy named). Each output field carries `source_id` + `fetched_at`. Promotes to level 3 once P19 + P20 + P21 ship as the source-backed pipeline. |
| Exploratory data analysis | 0 | None yet | Build first EDA notebook |
| Data mining | 0 | None yet | Start after data foundations |
| Visualisation | 0 | None yet | Build chart interpretation standards |
| Machine learning | 0 | None yet | Establish baseline-first doctrine |
| Optimisation | 0 | None yet | Define optimisation problem template |
| High-performance computing | 0 | None yet | Define performance profiling basics |
| Decision science | 0 | None yet | Build scoring and tradeoff framework |
| Reproducible experimentation | 0 | None yet | Create experiment log format |
| Productisation | 0 | None yet | Define notebook-to-product path |
| Responsible AI | 0 | None yet | Create policy and checklist |
| UI / UX design for data-review tools | 5 | DES-001 Topics 1–3 closed (cumulative grade v2 87/100 Excellent / Distinction); component rule sheet + UX acceptance-criteria sheet signed off; **Destination Master Browser v1.1 shipped 2026-05-16 against both sheets and verified with a 15/15 Playwright walk-through** (`curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/`). The skill is now reusable / teachable: any future data-review tool inherits the master-detail-with-faceted-search pattern, the four-depth trust signal, the nine-state interactive checklist, and the seven-step reviewer-journey template. | Transfer the pattern to the next data-review tool (datasets browser, validator review, Planner review) when the need arises; record transfers in `operations/TRANSFER_LOG.md` |
| Design-discipline meta-skill (process + lifecycle + perceptual layer) | 5 | DES-001 Topics 4 + 5 + 6 closed 2026-05-17 in the ratified three-topic push. Topic 4 (Design thinking — d.school + IBM + Brown + NN/g) produced a worked design-thinking loop template + three-constraint triage frame + problem-framing decision tree, with Lab 04 Loop 1 (batch-promote-confirm modal). Topic 5 (HCD — ISO 9241-210 + IDEO + Norman + W3C) produced the HCD audit-shape (4 activities + 6 principles + W3C triad lens), with Lab 05 Audit 1 verdict "HCD-substantial but incomplete" (2 Pass + 3 Partial + 1 Fail; 7 findings; 6-item v1.2 list). Topic 6 (Gestalt — Wertheimer/Koffka/Köhler via secondary + IxDF + NN/g + Smashing) produced the Gestalt audit-shape (6 regions × 6 principles + conflict adjudication + density-vs-grouping) and the perceptual-constraint vs aesthetic-rule discipline, with Lab 06 Audit 1 verdict "Gestalt-substantial" (22 Pass + 5 Trade-off + 7 Violation; 6 findings + 1 meta; 6-item fix list). The canonical hierarchy (HCD umbrella over Topics 2/3/4 with Topic 6 as the perceptual constraint layer underneath Topic 2) is now established. Three audit-cycles run (Lab 04 loop output + Lab 05 HCD audit + Lab 06 Gestalt audit) with a consistent audit-shape that is itself a reusable workspace pattern. | Apply the consolidated discipline to v1.1.x polish (close Lab 06's 5 v1.1.x fixes) and to v1.2 (inherit the three-lab prioritised list). Topics 7–12 (Fitts' / button states / typography / colour / grid / design systems) deepen specific perceptual + visual + system concerns on top of this base. |

## Skill Entry Template

```md
## Skill: <name>

Domain:
Current level:
Target level:
Why it matters:
Prerequisites:
Evidence:
Reusable in:
Limitations:
Next action:
```
