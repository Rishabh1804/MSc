# artifacts/html/

Single-file HTML review artifacts live here.

These files are not the source of truth. They are visual and interactive views over source data, reports, patterns, or code.

## Rules

- Keep source data in `datasets/`, reports in `reports/`, and reusable logic in `src/`.
- Use HTML for inspection, comparison, filtering, dashboarding, or visual review.
- Include source-file references and limitations inside the artifact.
- Treat artifacts as prototypes unless promoted into a PWA or app component.

## Current Artifacts

| Artifact | Purpose | Source |
|---|---|---|
| `destination-browser-v1.html` | Visual browser for the India + near-India destination seed database | `datasets/reference/india_region_destinations_seed.csv` |
