# DATA_POLICY.md — CodeMike Data Policy

CodeMike may eventually work with public, synthetic, internal, confidential, sensitive, or restricted data. Data must be classified before use.

## Core Rule

No sensitive real-world data should enter the repo unless its privacy level is explicitly classified and approved.

## Data Classification

| Level | Meaning | Handling |
|---|---|---|
| Public | Publicly shareable data | Can be committed if licence allows |
| Synthetic | Generated data with no real records | Preferred for practice and prototypes |
| Internal | Low-risk non-public working data | Avoid committing unless approved |
| Confidential | Business-sensitive operational data | Do not commit without explicit approval |
| Sensitive | Health, finance, identity, family, customer, or high-risk data | Do not commit; use summaries or synthetic versions |
| Restricted | Data requiring legal, contractual, or special handling | Do not use without explicit approval and documented controls |

## Rules

- Prefer synthetic data for experiments and prototypes.
- Do not commit secrets, credentials, private records, or raw sensitive datasets.
- Document dataset source, licence, limitations, and allowed uses.
- Anonymisation must be checked; removing names is not always enough.
- If data is uncertain, treat it as sensitive until clarified.

## Dataset Linkage

All datasets used in experiments should be recorded in `DATASETS.md`.
