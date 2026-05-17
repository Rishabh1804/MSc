# Lab 06 — Gestalt Audit of v1.1

## Lab objective

Run a **Gestalt audit** of the Destination Master Browser v1.1 against the six core principles (proximity, similarity, continuity, closure, common region, common fate), focused on the screen regions where grouping signals carry the most weight. Produce a per-region violation list and a v1.1.x / v1.2 fix list scoped against existing Topic 2 component rules and Topic 3 acceptance criteria.

## Materials

- `curriculum/courses/des-001-design-foundations/lectures/lecture-06-gestalt-principles.md`
- `curriculum/courses/des-001-design-foundations/readings/topic-06-gestalt-principles-reading-pack.md`
- `design/foundations/topic-06-gestalt.md` (deep-reading doc, PR A)
- Topic 2 rule sheet + Topic 3 acceptance-criteria sheet (the constraint frames against which fixes are scoped)
- Topic 5 HCD audit findings list (for v1.2 context)
- v1.1 build at `docs/destination-master-browser.html` + walk-through screenshots

## Lab steps

### Step 1 — Pick the screen regions to audit

The browser has many regions; an audit-everything approach loses focus. Pick the regions where grouping signals carry the most weight:

| Region | Why it matters |
|---|---|
| Cards view (record card composition) | Multiple visual groups within one card; high information density |
| Table view (column alignment + row separators) | Continuity (alignment) + common region (rows) at scale |
| Toolbar (search + filter selects + view-toggle) | Proximity (controls together) + similarity (input/select uniformity) |
| Active-filter summary (chip row) | Perceived as a group separate from the toolbar or the result region? |
| Trust banner + page header + stats banner | Three persistent visual units; do they read as separate concerns or one mass? |
| Drawer (header + trust banner + body sections) | Per-section common region + proximity for related fields |

Record the audit region list; name any region intentionally excluded with a one-line reason.

### Step 2 — Per-region per-principle audit

For each region × each of the six principles, mark:

| Verdict | Meaning |
|---|---|
| **Pass** | Principle is honoured; the perceived grouping matches intended grouping |
| **Trade-off** | Principle is violated but the violation is acceptable; compensating signal named |
| **Violation** | Principle is violated and the violation is a finding (no acceptable compensation) |
| **N/A** | Principle doesn't apply to this region |

Cells marked **Violation** become per-region findings.

### Step 3 — Conflict adjudication

For each region, identify cases where two principles conflict (e.g., proximity says "group these"; similarity says "these aren't grouped"). For each conflict:

- Name the two principles in tension
- Identify which user task the region is meant to support
- Pick the winning principle with a comparative reason

Conflicts that go unresolved are findings.

### Step 4 — Density-vs-grouping audit

Data-review tools pack information densely. The whitespace required by proximity-based grouping is expensive. For each region, ask:

- Does the current density force a proximity compromise?
- If yes, what compensating signal (divider, tint, alignment) substitutes for whitespace?
- Is the substitution explicit, or is it silent collapse?

Silent collapses become findings.

### Step 5 — Findings + prioritised fix list

Consolidate the audit into:

- **Strengths**: regions where Gestalt principles are cleanly honoured
- **Violations**: regions where the audit found unacceptable Gestalt violations
- **Trade-offs**: regions where violations are acceptable with named compensation
- **Prioritised fix list**: ranked by leverage (which fixes close the most violations? which serve the most user tasks?). Tag each fix as v1.1.x (small visual treatment change) or v1.2 (component-rule-affecting change).

### Step 6 — Master-browser checklist Topic 6 section

Append Topic 6 gates + anti-patterns + canonical pointer to `design/checklists/master-browser-design-checklist.md`:

- Three Gestalt gates (perceptual-constraint gate; principle-conflict adjudication gate; density-vs-grouping gate)
- Three anti-patterns specific to data-review tools
- A canonical pointer to the Gestalt audit doc

## Expected outputs

```text
design/foundations/topic-06-gestalt-audit.md
  ├─ Step 1: audit-region list + exclusion rationale
  ├─ Step 2: per-region per-principle audit matrix
  ├─ Step 3: conflict adjudication per region
  ├─ Step 4: density-vs-grouping audit
  └─ Step 5: findings + prioritised fix list (v1.1.x / v1.2 tags)

curriculum/courses/des-001-design-foundations/submissions/
  lab-06-gestalt-audit-results.md
    Formal lab submission with exec summary, key findings, decision-gate
    satisfaction, and reusable capabilities extracted.

design/checklists/master-browser-design-checklist.md
  Topic 6 section appended (§29 + §30 + §31).
```

## Submission checklist

- [ ] Audit-region list with exclusion rationale (Step 1)
- [ ] Per-region per-principle audit matrix (Step 2)
- [ ] Conflict adjudication per region (Step 3)
- [ ] Density-vs-grouping audit (Step 4)
- [ ] Findings + prioritised fix list (v1.1.x / v1.2 tags) (Step 5)
- [ ] Master-browser checklist Topic 6 section appended (Step 6)

## Rubric alignment

- *Multi-source coverage* — every audit cell cites the source(s) (Wertheimer/Koffka/Köhler via secondary, IxDF, NN/g, Smashing) the principle derives from
- *Application to CodeMike/browser* — the audit runs against v1.1, not a hypothetical
- *Checklist/actionability* — outputs feed into v1.1.x or v1.2 backlog with explicit Gestalt tags
- *Academic discipline* — audit is versioned (Audit 1) so future audits can be tracked

## Decision gate before closing the lab

Lab 06 is complete when:

1. Every chosen region has been audited against every relevant principle
2. Every Trade-off cell names a compensating signal
3. Every Violation has a fix in the prioritised list
4. Every conflict is adjudicated, not left unresolved
5. The prioritised fix list tags each item as v1.1.x or v1.2

Failure on any of these means re-run the relevant step.
