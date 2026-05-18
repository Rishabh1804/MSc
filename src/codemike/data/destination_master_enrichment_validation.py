"""Validate destinations_master_v2_enriched.csv against the v1 enrichment spec.

Input:
    datasets/reference/destinations_master_v2_enriched.csv

Output:
    reports/evidence/destination-master-v2-enrichment-validation-report.md

Checks (per strategy doc §10 + §3 — required columns, controlled values, score
bounds, derived-field consistency, band-vs-score mapping). Structural validation
only; does not verify live travel facts or source citations.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ENRICHED_PATH = Path("datasets/reference/destinations_master_v2_enriched.csv")
MASTER_PATH = Path("datasets/reference/destinations_master_v2.csv")
REPORT_PATH = Path("reports/evidence/destination-master-v2-enrichment-validation-report.md")
EXPECTED_ROW_COUNT = 359

REQUIRED_COLUMNS = [
    "destination_master_id",
    "enrichment_version",
    "enrichment_pass_date",
    "enrichment_method",
    "origin_fit_ccu",
    "origin_fit_ccu_basis",
    "origin_fit_ccu_confidence",
    "origin_fit_ixr",
    "origin_fit_ixr_basis",
    "origin_fit_ixr_confidence",
    "infant_suitability_score",
    "infant_suitability_band",
    "family_suitability_band",
    "senior_suitability_band",
    "couple_suitability_band",
    "suitability_basis",
    "travel_fatigue_band",
    "travel_fatigue_drivers",
    "transfer_complexity_hint",
    "planning_complexity_band",
    "planning_complexity_drivers",
    "permit_or_visa_hint",
    "medical_access_confidence",
    "medical_access_basis",
    "pediatric_access_confidence",
    "season_window",
    "monsoon_caution",
    "heat_caution",
    "winter_road_caution",
    "altitude_caution",
    "weather_basis",
    "resort_family_density",
    "accommodation_breadth",
    "derived_access_complexity",
    "derived_caution_tags",
    "verification_status",
    "planner_use_status",
    "source_confidence",
    "enrichment_notes",
]


ALLOWED_VALUES: dict[str, set[str]] = {
    "enrichment_method": {"heuristic_v1", "manual_review_v1", "manual_review_v1.1", "imported_from_seed"},
    "origin_fit_ccu": {"strong", "moderate", "weak", "unknown"},
    "origin_fit_ixr": {"strong", "moderate", "weak", "unknown"},
    "origin_fit_ccu_confidence": {"low", "medium", "high"},
    "origin_fit_ixr_confidence": {"low", "medium", "high"},
    "infant_suitability_band": {"low", "low_medium", "medium", "high"},
    "family_suitability_band": {"low", "low_medium", "medium", "high"},
    "senior_suitability_band": {"low", "low_medium", "medium", "high"},
    "couple_suitability_band": {"low", "low_medium", "medium", "high"},
    "travel_fatigue_band": {"low", "medium", "high", "very_high"},
    "transfer_complexity_hint": {"simple", "multi_leg", "complex"},
    "planning_complexity_band": {"low", "medium", "high"},
    "medical_access_confidence": {"low", "medium", "high", "unknown"},
    "pediatric_access_confidence": {"low", "medium", "high", "unknown"},
    "monsoon_caution": {"none", "check", "avoid"},
    "heat_caution": {"none", "check", "avoid"},
    "winter_road_caution": {"none", "check", "avoid"},
    "altitude_caution": {"none", "check", "avoid"},
    "resort_family_density": {"low", "medium", "high", "unknown"},
    "accommodation_breadth": {"narrow", "moderate", "broad"},
    "derived_access_complexity": {"easy", "moderate", "hard"},
    "verification_status": {"enriched_unverified", "enriched_with_concerns", "source_verified", "planner_ready", "retired"},
    "planner_use_status": {"candidate", "needs_verification", "planner_candidate", "planner_ready", "retired", "transfer_candidate"},
    "source_confidence": {"none", "low", "medium", "high", "official"},
}

BAND_ORDER = ["low", "low_medium", "medium", "high"]


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read a CSV file as a list of dicts."""

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def validate(enriched: list[dict[str, str]], master_ids: set[str]) -> dict[str, object]:
    """Run all validation checks; return a results dict."""

    results: dict[str, object] = {}

    # Row count
    results["row_count"] = len(enriched)
    results["expected_row_count"] = EXPECTED_ROW_COUNT
    results["row_count_match"] = len(enriched) == EXPECTED_ROW_COUNT

    # Column presence + extras
    if not enriched:
        results["missing_columns"] = REQUIRED_COLUMNS
        results["extra_columns"] = []
        return results
    actual_columns = set(enriched[0].keys())
    expected = set(REQUIRED_COLUMNS)
    results["missing_columns"] = sorted(expected - actual_columns)
    results["extra_columns"] = sorted(actual_columns - expected)

    # Unique destination_master_id + join-with-master
    ids = [r["destination_master_id"] for r in enriched]
    id_counts = Counter(ids)
    results["duplicate_master_ids"] = sorted([i for i, c in id_counts.items() if c > 1])
    enriched_ids = set(ids)
    results["orphan_enriched_ids"] = sorted(enriched_ids - master_ids)
    results["unmatched_master_ids"] = sorted(master_ids - enriched_ids)

    # Controlled-value violations
    violations: dict[str, list[str]] = defaultdict(list)
    for r in enriched:
        for col, allowed in ALLOWED_VALUES.items():
            value = r.get(col, "")
            if value not in allowed:
                violations[col].append(f"{r['destination_master_id']}={value!r}")
    results["controlled_value_violations"] = {k: v[:10] for k, v in violations.items()}
    results["controlled_value_violation_counts"] = {k: len(v) for k, v in violations.items()}

    # Score bounds + band-vs-score mapping
    score_violations: list[str] = []
    band_mapping_violations: list[str] = []
    for r in enriched:
        try:
            score = int(r.get("infant_suitability_score", ""))
        except ValueError:
            score_violations.append(f"{r['destination_master_id']}=non-integer({r.get('infant_suitability_score')!r})")
            continue
        if not 0 <= score <= 100:
            score_violations.append(f"{r['destination_master_id']}=score_out_of_range({score})")

        # Band-vs-score consistency: low <30, low_medium 30-49, medium 50-74, high >=75
        band = r.get("infant_suitability_band")
        expected_band = (
            "low" if score < 30
            else "low_medium" if score < 50
            else "medium" if score < 75
            else "high"
        )
        if band != expected_band:
            band_mapping_violations.append(
                f"{r['destination_master_id']}: score={score} band={band} expected={expected_band}"
            )
    results["score_out_of_range"] = score_violations
    results["band_vs_score_mismatches"] = band_mapping_violations

    # Default-state checks (per strategy doc §3.9, §9.3)
    default_violations: list[str] = []
    for r in enriched:
        if r.get("enrichment_method") == "heuristic_v1":
            if r.get("verification_status") != "enriched_unverified":
                default_violations.append(f"{r['destination_master_id']}: heuristic_v1 + verification_status={r.get('verification_status')!r} (expected enriched_unverified)")
            if r.get("planner_use_status") != "needs_verification":
                default_violations.append(f"{r['destination_master_id']}: heuristic_v1 + planner_use_status={r.get('planner_use_status')!r} (expected needs_verification)")
            if r.get("source_confidence") != "low":
                default_violations.append(f"{r['destination_master_id']}: heuristic_v1 + source_confidence={r.get('source_confidence')!r} (expected low)")
    results["heuristic_default_violations"] = default_violations

    # Pediatric should be <= medical confidence (low, medium, high, unknown ordering — unknown side-channel)
    confidence_order = {"low": 0, "medium": 1, "high": 2}
    pediatric_violations: list[str] = []
    for r in enriched:
        medical = r.get("medical_access_confidence")
        pediatric = r.get("pediatric_access_confidence")
        if medical in confidence_order and pediatric in confidence_order:
            if confidence_order[pediatric] > confidence_order[medical]:
                pediatric_violations.append(
                    f"{r['destination_master_id']}: pediatric={pediatric} > medical={medical} (pediatric should be <= medical)"
                )
    results["pediatric_exceeds_medical"] = pediatric_violations

    # Permit/visa hint must be present whenever the relevant driver is named
    permit_hint_violations: list[str] = []
    for r in enriched:
        drivers = r.get("planning_complexity_drivers", "")
        hint = r.get("permit_or_visa_hint", "")
        if "permit_required" in drivers and not hint:
            permit_hint_violations.append(f"{r['destination_master_id']}: permit_required driver present but permit_or_visa_hint blank")
        if "visa_required" in drivers and "visa" not in hint:
            permit_hint_violations.append(f"{r['destination_master_id']}: visa_required driver present but visa not in permit_or_visa_hint ({hint!r})")
    results["permit_hint_violations"] = permit_hint_violations

    # Derivation outputs non-empty
    derived_empty: list[str] = []
    for r in enriched:
        if not r.get("derived_access_complexity"):
            derived_empty.append(f"{r['destination_master_id']}: derived_access_complexity blank")
        if not r.get("travel_fatigue_band"):
            derived_empty.append(f"{r['destination_master_id']}: travel_fatigue_band blank")
        if not r.get("season_window"):
            derived_empty.append(f"{r['destination_master_id']}: season_window blank")
    results["derived_field_empties"] = derived_empty[:50]
    results["derived_field_empties_total"] = len(derived_empty)

    # Distributions for the report
    results["dist_infant_band"] = dict(Counter(r["infant_suitability_band"] for r in enriched))
    results["dist_origin_fit_ccu"] = dict(Counter(r["origin_fit_ccu"] for r in enriched))
    results["dist_origin_fit_ixr"] = dict(Counter(r["origin_fit_ixr"] for r in enriched))
    results["dist_travel_fatigue"] = dict(Counter(r["travel_fatigue_band"] for r in enriched))
    results["dist_planning_complexity"] = dict(Counter(r["planning_complexity_band"] for r in enriched))
    results["dist_medical_access"] = dict(Counter(r["medical_access_confidence"] for r in enriched))

    # Aggregate readiness
    structural_ok = (
        results["row_count_match"]
        and not results["missing_columns"]
        and not results["duplicate_master_ids"]
        and not results["orphan_enriched_ids"]
        and not results["unmatched_master_ids"]
        and not any(results["controlled_value_violation_counts"].values())
        and not results["score_out_of_range"]
        and not results["band_vs_score_mismatches"]
        and not results["heuristic_default_violations"]
        and not results["pediatric_exceeds_medical"]
        and not results["permit_hint_violations"]
        and not results["derived_field_empties"]
    )
    results["readiness"] = (
        "enriched_structurally_valid_not_planner_ready" if structural_ok
        else "enriched_structurally_invalid"
    )
    return results


def write_report(results: dict[str, object], path: Path = REPORT_PATH) -> None:
    """Write the validation report."""

    def fmt_list(items: list, cap: int = 25) -> str:
        if not items:
            return "- None"
        shown = items[:cap]
        body = "\n".join(f"- {x}" for x in shown)
        if len(items) > cap:
            body += f"\n- ... ({len(items) - cap} more not shown)"
        return body

    def fmt_dict(d: dict) -> str:
        return "\n".join(f"- `{k}`: {v}" for k, v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0])))

    cv_counts = results.get("controlled_value_violation_counts", {})
    cv_total = sum(cv_counts.values())

    body = f"""# Evidence Report — Destinations Master v2 Enrichment Validation (E1, v1.0)

Date: see enrichment_pass_date column in enriched CSV.
Author: CodeMike
Validator: `src/codemike/data/destination_master_enrichment_validation.py`
Input: `datasets/reference/destinations_master_v2_enriched.csv`

## 1. Objective

Validate the v1 enriched master against the strategy spec (structural checks only).
Does not verify live travel facts or source citations.

## 2. Validation Summary

| Check | Result |
|---|---:|
| Rows checked | {results['row_count']} |
| Expected rows | {results['expected_row_count']} |
| Row count match | {results['row_count_match']} |
| Missing required columns | {len(results.get('missing_columns', []))} |
| Extra columns | {len(results.get('extra_columns', []))} |
| Duplicate destination_master_id | {len(results.get('duplicate_master_ids', []))} |
| Orphan enriched IDs (not in master) | {len(results.get('orphan_enriched_ids', []))} |
| Unmatched master IDs (not in enriched) | {len(results.get('unmatched_master_ids', []))} |
| Total controlled-value violations | {cv_total} |
| Infant score out of range | {len(results.get('score_out_of_range', []))} |
| Band-vs-score mismatches | {len(results.get('band_vs_score_mismatches', []))} |
| Heuristic-default violations | {len(results.get('heuristic_default_violations', []))} |
| Pediatric > medical confidence | {len(results.get('pediatric_exceeds_medical', []))} |
| Permit/visa hint violations | {len(results.get('permit_hint_violations', []))} |
| Derived-field blanks | {results.get('derived_field_empties_total', 0)} |

Readiness:

```text
{results['readiness']}
```

## 3. Missing Columns

{fmt_list(results.get('missing_columns', []))}

## 4. Extra Columns

{fmt_list(results.get('extra_columns', []))}

## 5. Controlled-Value Violations (by column)

{fmt_dict(cv_counts) if cv_counts else "- None"}

## 6. Score Out-of-Range

{fmt_list(results.get('score_out_of_range', []))}

## 7. Band-vs-Score Mismatches

{fmt_list(results.get('band_vs_score_mismatches', []))}

## 8. Heuristic-Default Violations

{fmt_list(results.get('heuristic_default_violations', []))}

## 9. Pediatric > Medical Confidence

{fmt_list(results.get('pediatric_exceeds_medical', []))}

## 10. Permit/Visa Hint Violations

{fmt_list(results.get('permit_hint_violations', []))}

## 11. Derived-Field Blanks (sample)

{fmt_list(results.get('derived_field_empties', []))}

## 12. Distributions (sanity check)

### origin_fit_ccu

{fmt_dict(results.get('dist_origin_fit_ccu', {}))}

### origin_fit_ixr

{fmt_dict(results.get('dist_origin_fit_ixr', {}))}

### infant_suitability_band

{fmt_dict(results.get('dist_infant_band', {}))}

### travel_fatigue_band

{fmt_dict(results.get('dist_travel_fatigue', {}))}

### planning_complexity_band

{fmt_dict(results.get('dist_planning_complexity', {}))}

### medical_access_confidence

{fmt_dict(results.get('dist_medical_access', {}))}

## 13. Interpretation

If readiness is `enriched_structurally_valid_not_planner_ready`, the enriched layer
has passed all structural and controlled-value checks. It is ready for the E2
manual-review sessions (batches O / S / M).

It is still not Planner-ready because: heuristic-derived values carry
`source_confidence = low`; live travel facts have not been verified; the E3
source-verified promotion step has not been run.

## 14. Next Actions

1. If any failures above, fix the enrichment script and re-run.
2. If clean: schedule the E2 manual-review sessions per the strategy doc §11–§12.
3. After E2 completes, NEXT_ACTIONS priority 6 (scoring v1) can begin.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def main() -> None:
    """Run validation end-to-end."""

    enriched = read_rows(ENRICHED_PATH)
    master = read_rows(MASTER_PATH)
    master_ids = {r["destination_master_id"] for r in master}
    results = validate(enriched, master_ids)
    write_report(results)

    # Concise console summary
    print(f"Enrichment validation: readiness = {results['readiness']}")
    print(f"  rows: {results['row_count']} (expected {results['expected_row_count']})")
    print(f"  missing columns: {len(results.get('missing_columns', []))}")
    print(f"  controlled-value violations: {sum(results.get('controlled_value_violation_counts', {}).values())}")
    print(f"  band/score mismatches: {len(results.get('band_vs_score_mismatches', []))}")
    print(f"  pediatric > medical: {len(results.get('pediatric_exceeds_medical', []))}")
    print(f"  report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
