# EXPERIMENTS.md — CodeMike Experiment Register

This file records experiments, tests, prototypes, and structured investigations.

## Experiment Rule

An experiment should answer a question, compare against a baseline where possible, and produce an interpretable result.

## Experiment Entry Template

```md
## Experiment: <title>

ID:
Date:
Question:
Dataset:
Baseline:
Method:
Metric:
Result:
Interpretation:
Limitations:
Evidence path:
Next step:
```

## Experiment Register

## Experiment: Destination Master Enrichment v1.0 (heuristic baseline)

ID: EXP-003  
Date: 2026-05-18  
Question: Can a deterministic stdlib-only heuristic pipeline derive the strategy doc §3 enrichment-field catalogue across all 359 master rows, surface honest calibration findings, and produce three manual-review queues sized within their per-session caps?  
Dataset: `datasets/reference/destinations_master_v2.csv` (359 rows; structurally valid; not Planner-ready).  
Output: `datasets/reference/destinations_master_v2_enriched.csv` (39 columns; every row at `verification_status=enriched_unverified` + `planner_use_status=needs_verification` + `source_confidence=low`); three manual-review queue CSVs at `reports/evidence/destination-master-v2-enrichment-manual-review-queues/{O,S,M}.csv`.  
Baseline: master dataset's existing seed-only `destination_enrichment.py` (CCU-secondary lookup only; no S/M queues; no infant/family/senior/couple decomposition).  
Method: 10-step deterministic per-row pipeline implementing strategy doc §10.1: derive access → derive cautions → origin_fit (CCU + IXR via JSON catchment) → travel_fatigue (band + drivers) → medical_access (with pediatric subset) → planning_complexity → season + weather cautions → suitability (infant 0–100 score + 4 bands per §5) → defaults → manual-review queue assignment per §11. Validator separately runs 8 structural + controlled-value + consistency checks. Pure stdlib; no YAML / external deps (catchment changed from YAML to JSON per §18.7).  
Metric: (a) structural validation pass/fail per validator's 8 checks; (b) queue sizes O / S / M against §11 caps (O ≤ catchment-tuning-pass; S ≤ 25/session; M ≤ 20/session); (c) calibration findings worth durable text (spec-tweak signal); (d) reproducibility (byte-identical re-run modulo `enrichment_pass_date`).  
Result: 359/359 rows pass structural validation (readiness=`enriched_structurally_valid_not_planner_ready`; 0 missing columns; 0 duplicate IDs; 0 controlled-value violations; 0 band/score mismatches; 0 pediatric>medical; 0 permit-hint gaps; 0 derived-field blanks). Queue sizes: **O = 0 ✓** after catchment tuning (95 → 0); **S = 155** (>>25/session — 6× over cap); **M = 257** (>>20/session — 13× over cap). Four calibration findings surfaced in strategy doc §18: input-data sparseness (§18.1), catchment tuning (§18.2), Queue S flattening-trigger over-fire (§18.3), Queue M missing region/resort_zone medical branch (§18.4). Plus §18.5 (fatigue band skew) + §18.7 (reproducibility confirmed).  
Interpretation: The heuristic pipeline is *structurally* honest — every output cites its derivation rule, no row crosses to `planner_ready`, queues isolate the low-confidence rows for human review. But the queue-size overshoot proves the *calibration question* was understated in the v1 spec: the strategy doc assumed §5.3 band-bumping rules would fire often enough to differentiate suitability bands, when in practice the input tags were sparse enough that bands flatten to `medium` for ~99 rows — a category signal that the heuristic is mis-shaped for these inputs, not a parameter tweak. The S + M overshoot is the experimental evidence that promoted the workspace to §19's no-assumption policy revision.  
Limitations: (a) heuristic derivation = workspace judgement, not source-cited fact — explicit per §19.2; (b) caution-tag / context-tag input columns were near-empty in the master so Step 1a/1b derived them from other populated fields, which is itself a workspace-judgement layer; (c) origin catchment tables are workspace-curated, not flight/train-data-verified; (d) no real-user evaluation of enriched-layer outputs (Lab 05 F-PRIN-1; queued for Sponsor Reviewer cycle per priority 9); (e) v1.0 medical-access heuristic was *already* named §8.3 as the weakest formula in v1 — running it confirmed the gap, did not surprise the spec.  
Evidence path: `reports/evidence/destination-master-v2-enrichment-report.md` (pipeline status + distributions); `reports/evidence/destination-master-v2-enrichment-validation-report.md` (structural verdict); `reports/evidence/destination-master-v2-enrichment-manual-review-queues/{O,S,M}.csv` (queue artifacts); `datasets/reference/destination_master_enrichment_strategy.md` §18 (calibration findings as durable text).  
Next step: Treated as the heuristic baseline per §19.2; preserved unchanged, will rename `destination_master_enrichment_v1.py` → `destination_master_enrichment_v0_heuristic.py` in P21. Replaced (not iterated) by the v2 source-backed pipeline (P19 source registry → P20 v2 strategy doc → P21 v2 enrichment service). v1.1 calibration recommendations from §18.3–§18.5 are explicitly **superseded** by §19's policy revision (P18 retired).

## Experiment: Trip Options Sensitivity Analysis v1.1

ID: EXP-002  
Date: 2026-05-05  
Question: Are the top recommendations from the v1 trip-options scoring experiment robust when user priorities change?  
Dataset: `datasets/processed/trip_options_scored_v1.csv`  
Output: `datasets/processed/trip_options_sensitivity_v1_1.csv`  
Baseline: EXP-001 v1 recommendation ranking.  
Method: Re-ranked scoreable trip options under five weighting scenarios: family comfort, budget sensitive, premium comfort, low fatigue, and novelty heavy. Penalty rules were held constant.  
Metric: Scenario ranks, average scenario rank, top-five scenario count, and top-ten scenario count.  
Result: Goa, Phuket, Singapore comfort, and Dubai comfort appeared in the top five across all five scenarios. Kuala Lumpur appeared in four of five top-fives and remained top-ten across all scenarios.  
Interpretation: Practical comfort-tier options are stable. Premium Singapore is preference-sensitive: rank 1 under premium comfort but rank 13 under budget-sensitive scoring.  
Limitations: Synthetic data; hand-authored scenario weights; penalty rules not varied; no live travel validation; no user calibration.  
Evidence path: `reports/experiment-reports/trip-options-sensitivity-v1-1.md`  
Next step: Create a Planner transfer candidate or convert scoring logic into a reusable module.

## Experiment: Trip Options Recommendation Scoring v1

ID: EXP-001  
Date: 2026-05-05  
Question: Can CodeMike produce an explainable first-pass recommendation ranking for synthetic Planner-style trip options using criteria, weights, constraints, and penalties?  
Dataset: `datasets/processed/trip_options_flagged.csv`  
Output: `datasets/processed/trip_options_scored_v1.csv`  
Baseline: Data-quality-filtered scoreable rows ranked by a transparent weighted formula. A richer baseline comparison is still pending.  
Method: Weighted scoring with documented criteria, normalised cost score, visa score, fatigue score, risk-adjusted comfort, confidence, novelty, and penalty rules.  
Metric: `recommendation_score_v1`  
Result: Top five ranked options were `TRIP-014` Goa, `TRIP-008` Phuket, `TRIP-012` Kuala Lumpur, `TRIP-002` Singapore, and `TRIP-019` Dubai.  
Interpretation: The v1 formula favours practical family travel over pure luxury. Comfort-tier options dominated because they combine low cost, low fatigue, and easy visa complexity.  
Limitations: Synthetic data; provisional weights; hand-authored penalties; no sensitivity analysis; no live travel validation.  
Evidence path: `reports/experiment-reports/trip-options-recommendation-scoring-v1.md`  
Next step: Run sensitivity analysis as v1.1 and consider Planner OptionCard transfer after robustness checks.
