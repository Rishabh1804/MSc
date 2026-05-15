# MIGRATION_LOG.md — Repository Migration Log

Chronological record of migration batches as they commit. The frozen target state lives in `MIGRATION_PLAN.md`; this file records what has actually happened.

All batches stack as commits on branch `claude/review-msc-sproutlab-docs-HzsrJ` and ship under PR #1. Batches merge into `main` together at PR close.

## Entry template

~~~md
## Batch <N> — <short title>

Date:
PR: #1
Commit: <short SHA>
Scope: <one sentence>
Files added:
Files moved:
Files deleted:
Verification: <link-check status, build status, manual smoke check>
Notes:
~~~

A batch's own commit SHA is backfilled by the next batch's log update (since a commit cannot know its own SHA at write time). The most recent batch's `Commit` field will read `(pending — backfilled next batch)` until then.

## Plan revisions

### 2026-05-15 — Stacked-commit cadence

PR: #1  
Commit: `ee68591`  
Affects: All batches from Batch 1 onward; Batch 0 retroactively reclassified from "draft PR per batch" to "first commit on PR #1".  
Change: Migration plan now describes the cadence as stacked commits on a single branch / single PR, not one PR per batch.  
Reason: Aligns with the session's designated working branch and reduces PR overhead. Per-commit review preserves batch-level reviewability.

## Register

### Batch 0 — Foundation

Date: 2026-05-15  
PR: #1  
Commit: `32cd4f3`  
Scope: Added the four foundation files that make subsequent batches reviewable and idempotent.  
Files added:
  - `charter/HARD_RULES.md`
  - `charter/REPO_STRUCTURE.md` (rewritten in place)
  - `operations/MIGRATION_PLAN.md`
  - `operations/MIGRATION_LOG.md`  

Files moved: none  
Files deleted: none  
Verification: PR #1 opened as draft; `mergeable_state: clean`; no review threads; 0 check runs (no workflows configured yet).  
Notes: First commit on the migration branch. Citations in `HARD_RULES.md` to `charter/...` and `operations/...` paths intentionally do not resolve until Batches 2 and 3 land.

### Batch 1 — Stub READMEs for new top-level buckets

Date: 2026-05-15  
PR: #1  
Commit: (pending — backfilled next batch)  
Scope: Added README files to the new top-level buckets so they exist in git and explain their purpose to anyone landing there.  
Files added:
  - `charter/README.md`
  - `operations/README.md`
  - `curriculum/README.md`
  - `cockpit/README.md`
  - `decks/README.md`  

Files modified:
  - `operations/MIGRATION_LOG.md` (this entry)

Files moved: none  
Files deleted: none  
Verification: Five new files, none overwriting existing content. `capabilities/README.md` deliberately NOT touched — the directory already exists with nine capability cards indexed (`dashboard-insight-design`, `data-cleaning`, `exploratory-analysis`, `model-evaluation`, `optimisation-modelling`, `project-transfer`, `recommendation-scoring`, `research-synthesis`, plus the existing README). It will be updated in Batch 5 when `patterns/`, `anti-patterns/`, `case-studies/`, `decision-science/` land underneath it.  
Notes: `curriculum/`, `cockpit/`, `decks/` are entirely new directories created by this commit. `charter/` and `operations/` already existed from Batch 0; their READMEs document the bucket's purpose for anyone landing there.
