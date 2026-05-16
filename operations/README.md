# operations/

Live registers and logs. Files here change on the order of days as work is logged. Treat as append-mostly: editing an existing entry is allowed; deleting one requires a note in `DECISIONS.md`.

See `../charter/REPO_STRUCTURE.md` for this bucket's role in the overall layout. The schedule by which files moved into this directory lives in `MIGRATION_PLAN.md` and `MIGRATION_LOG.md`.

## Contents

After Batch 3 this directory holds 18 files:

| File | Source | Role |
|---|---|---|
| `MIGRATION_PLAN.md` | Added Batch 0 | Frozen target state for the restructure |
| `MIGRATION_LOG.md` | Added Batch 0 | Running record of batches as they commit |
| `ARTIFACT_INDEX.md` | Moved Batch 3 | CodeMike Artifact Index |
| `CAPABILITIES.md` | Moved Batch 3 | CodeMike Capability Catalogue |
| `DATASETS.md` | Moved Batch 3 | Dataset Registry |
| `DECISIONS.md` | Moved Batch 3 | CodeMike Decision Log |
| `EVIDENCE.md` | Moved Batch 3 | Evidence Register |
| `EXPERIMENTS.md` | Moved Batch 3 | CodeMike Experiment Register |
| `FAILURE_LOG.md` | Moved Batch 3 | CodeMike Failure Log |
| `LIBRARY.md` | Moved Batch 3 | CodeMike Library |
| `NEXT_ACTIONS.md` | Moved Batch 3 | CodeMike Operational Queue |
| `PORTFOLIO.md` | Moved Batch 3 | CodeMike Portfolio Index |
| `PROJECT_LOG.md` | Moved Batch 3 | CodeMike Project Log |
| `RISK_REGISTER.md` | Moved Batch 3 | CodeMike Risk Register |
| `ROADMAP.md` | Moved Batch 3 | CodeMike Six-Month Roadmap |
| `SKILL_MAP.md` | Moved Batch 3 | CodeMike Skill Map |
| `TRANSFER_LOG.md` | Moved Batch 3 | CodeMike Transfer Log |
| `VIVA.md` | Moved Batch 3 | CodeMike Viva and Defence Framework |

`benchmarks/` and `trackers/` move in during Batch 6.

## Append discipline

These files are read by the cockpit (`../cockpit/`) and decks (`../decks/`) at runtime per HR-MSc-9 (no academic claim hardcoded in HTML). Schema-breaking edits — renaming columns, removing fields, restructuring entry shape — must be paired with a corresponding update to any cockpit or deck JS that fetches the file. New rows or new entries do not require coordination.
