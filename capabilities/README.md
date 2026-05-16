# capabilities/

Reusable capability cards live here.

A capability combines skill, method, judgement, evidence, limitations, and transfer value.

Each capability should describe:

- what it does
- inputs
- outputs
- method
- maturity
- evidence
- limitations
- reusable targets
- transfer history

## Layout

After Batch 5 this directory holds:

```text
capabilities/
├── README.md                 (this file)
├── <capability-slug>.md      Capability cards (one per skill)
├── patterns/                 Reusable templates and checklists (moved Batch 5 from /patterns/)
├── anti-patterns/            Documented failure modes (moved Batch 5 from /anti-patterns/)
├── case-studies/             Applied case studies (moved Batch 5 from /case-studies/)
└── decision-science/         Decision-science methods and frameworks (moved Batch 5 from /decision-science/)
```

A capability card names the pattern, anti-pattern, and case studies that ground it (see "First Capability Set" below).

## First Capability Set

| Capability | Card | Initial maturity | Linked pattern |
|---|---|---:|---|
| Data Cleaning | `data-cleaning.md` | 1 | `patterns/data-cleaning-checklist.md` |
| Exploratory Analysis | `exploratory-analysis.md` | 1 | `patterns/eda-notebook-template.md` |
| Research Synthesis | `research-synthesis.md` | 1 | `patterns/research-paper-summary-template.md` |
| Recommendation Scoring | `recommendation-scoring.md` | 1 | `patterns/recommendation-scoring-pattern.md` |
| Optimisation Modelling | `optimisation-modelling.md` | 1 | `patterns/optimisation-problem-template.md` |
| Model Evaluation | `model-evaluation.md` | 1 | `patterns/model-evaluation-template.md` |
| Dashboard Insight Design | `dashboard-insight-design.md` | 1 | `patterns/dashboard-kpi-pattern.md` |
| Project Transfer | `project-transfer.md` | 1 | `patterns/transfer-plan-template.md` |

The "Linked pattern" paths resolve correctly only after Batch 5 — before Batch 5 they pointed to a sibling `/patterns/` directory at the repo root which no longer exists.

## Maturity Rule

A capability can move beyond Level 1 only when evidence exists.

Evidence should be recorded in:

- `../operations/EVIDENCE.md`
- `../operations/EXPERIMENTS.md` where relevant
- `../operations/TRANSFER_LOG.md` where transferred
- the capability card itself

Cross-bucket references here use post-migration paths (`../operations/...`). The original README used bare filenames (`EVIDENCE.md`) that resolved to `capabilities/EVIDENCE.md` — wrong both before and after Batches 2-3. Batch 9 (internal link sweep) verifies the rest of the repo follows the same convention.

## Next Capability Candidates

- synthetic data generation
- data dictionary design
- feature engineering
- experiment reporting
- benchmark reporting
- responsible AI review
- privacy review
- notebook-to-module refactoring
- data product API design
