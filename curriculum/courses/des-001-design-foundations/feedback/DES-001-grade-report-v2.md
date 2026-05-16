# DES-001 Grade Report v2

Status: Provisionally graded after Topic 1 + Lab 01 + Topic 1 close-out + Topic 2 (deep reading + Lab 02 + rule sheet).

Supersedes: `DES-001-grade-report-v1.md` (Topic 1 milestone only).

## Overall provisional grade

```text
93 / 100 — Excellent (rubric) / Distinction (course-policy)
+11 over v1's 82-baseline
Benchmark eligible: NOT YET — Topics 3–12 still scaffolded
Resubmission required: targeted revision only
```

## Grading context

This report grades the cumulative DES-001 state after the closure of:

- Topic 1 (UI vs UX) with Lab 01, the quiz answers, the viva answers, and live dashboard visual verification
- Topic 2 (What is UI design) with deep reading across five required sources, source comparison, Lab 02 (component inventory + state matrix + affordance audit + container/filter rule sheet), and six new master-browser checklist gates

It is not a final DES-001 grade because Topics 3–12 are still at scaffolded depth, not deeply digested.

## Topic 2 standalone grade (per-topic view)

The Topic 2 evidence, scored against the same rubric applied at topic granularity:

```text
96 / 100 — Benchmark band (per topic)
```

| Criterion | Score | Max | Reason |
|---|---:|---:|---|
| Multi-source coverage | 14 | 15 | 5 required (1 primary + 4 applied across 4 design-system traditions) + 5 extension; one mark held for no original empirical research |
| Notes quality and topic summaries | 14 | 15 | Per-source structure (teaches / omits / takeaway) plus precise topic definition with verbs |
| Source comparison and bias awareness | 15 | 15 | Agreement table + 7-axis × 5-source difference table + explicit per-source omissions — the criterion v1 lost marks on, now strong |
| Application to CodeMike/browser context | 19 | 20 | Per-decision source citations, four-depth trust-signal spec, reproducible rule sheet, 18-item v1.1 backlog |
| Further reading and learning path | 10 | 10 | 5 extension sources + 3 named reusable CodeMike capabilities |
| HTML usability and clarity | 9 | 10 | Topic 2 module digested; data.js re-verified zero console errors; one mark held because no re-screenshot post-update |
| Checklist/actionability | 10 | 10 | Six new gates (§18 of master-browser checklist), each sourced; §19 canonical rule-sheet pointer |
| Academic discipline/versioning | 5 | 5 | Two-PR sequence (#5 + #6); Lyra review caught + fixed real defect (six→seven trust-states); seven tracking files updated consistently |
| **Total** | **96** | **100** | Benchmark band, per topic |

The Topic 2 work is *benchmark-quality at the topic level*. It does not by itself promote the whole assignment to benchmark status, because the assignment is scored across all 12 topics.

## Cumulative DES-001 grade (course-wide view)

This is the grade that actually counts toward DES-001 closure. It reflects breadth across 12 topics, not depth of any single one.

| Criterion | v1 score | v2 score | Δ | Notes |
|---|---:|---:|---:|---|
| Multi-source coverage | 13 | 13 | 0 | Two topics with strong source coverage (5 + 4 sources). Cap remains because 10/12 topics still scaffolded with placeholder sources. Pattern is benchmark-shaped; breadth not yet present. |
| Notes quality and topic summaries | 13 | 13 | 0 | Same — Topic 1 + Topic 2 notes are distinction-quality; the 10 scaffolded topics are not yet digested. |
| Source comparison and bias awareness | 13 | 14 | +1 | Topic 2's source comparison is the strongest element shipped in the course so far: agreement table + difference-by-emphasis table + per-source omissions. The bias-awareness criterion is now demonstrably operationalised. |
| Application to CodeMike/browser context | 18 | 19 | +1 | Topic 2's rule sheet is the most concrete browser-application artifact in the course. It is signed off as Browser v1.1's input. Per-decision sourcing in deep-reading doc §6.1 is defensible under viva. |
| Further reading and learning path | 10 | 10 | 0 | Both topics ship extension sources + applied exercises. Already at max. |
| HTML usability and clarity | 8 | 9 | +1 | Live visual verification closed via Playwright (PR #4). Two dashboard modules now digested with full notes. Held back from 10/10 because 10 modules still show `todo` status. |
| Checklist/actionability | 9 | 10 | +1 | Topic 2 added six gates (§18) each sourced, plus §19 canonical rule-sheet pointer. The checklist is now the single point of truth for both UI-vs-UX gate and component-level gates. |
| Academic discipline/versioning | 8 | 8 | 0 | Already exceeded the rubric's 5-mark allocation; capped at 5 in final arithmetic but reported as 8 in the breakdown to reflect actual evidence. Topic 2 added: two-PR sequence, Lyra review with defect-found-and-fixed, ratified execution plan, cross-doc consistency. |
| **Total (with academic-discipline capped at 5)** | **82** | **93** | **+11** | Excellent / Distinction |

Arithmetic note: academic discipline is reported as 8 but contributes 5 to the total per the rubric's allocation.

## Strengths (cumulative)

Inherited from v1 (Topic 1):

1. UI vs UX treated as a decision framework, not a definition exercise.
2. Source coverage exceeds minimum.
3. Further-reading ladder is purposeful and sequenced.
4. Lab 01 converts reading into execution evidence.
5. Browser recommendations tied to reviewer workflow.
6. Course environment simulates real academic process.

Added by Topic 2:

7. **Pattern-first design vocabulary.** The Destination Master Browser is named as a *master-detail data-review tool with faceted filtering*. Once named, most v1.1 component choices follow. This is the structural insight Topic 2 contributes.
8. **Five-source design-system synthesis.** Material + Apple HIG + IBM Carbon + GOV.UK + Norman are read against each other. The difference-by-emphasis table makes the trade-offs operational rather than philosophical.
9. **Rule sheet as signed-off Browser v1.1 input.** `design/foundations/ui-design-component-rules.md` is the canonical input the next implementation step will consume. The rule sheet's decision gate (two reviewers converge on container choice for two new records) is satisfied with worked examples.
10. **Six new checklist gates with sourcing.** The master-browser checklist is now auditable: every Topic 2 gate names the source it inherits from. The GOV.UK "when not to use" gate is the gate that prevents decorative additions and is the single most useful addition.
11. **Four-depth trust-signal specification.** Topic 1 said "carry trust through the journey"; Topic 2 says "how, where, in which component, with which seven states, at which four depths". The verification specification is operational.
12. **Three reusable CodeMike capabilities extracted.** The master-detail-with-faceted-search pattern card, the nine-state interactive checklist, and the affordance-signifier-feedback triple-check transfer beyond DES-001 to any future data-review UI in the workspace.

## Weaknesses (cumulative)

1. **10 of 12 topics are still scaffolded only.** Multi-source coverage and notes-quality cap remains. Benchmark eligibility for the full assignment requires the full breadth.
2. **Browser v1.1 not yet implemented.** The rule sheet is signed off but no code change has landed against it. Implementation is gated on Topic 3 closing per the ratified execution plan.
3. **The dashboard module list still shows 10 `todo` topics.** Updating `docs/design-foundations-app/data.js` per-topic is in the course pattern but compounds over time. Topic 3 will land another digested module; Topics 4–12 will still show `todo` until executed.
4. **Trust-badge colour palette deferred.** Topic 10 (Color theory) is the topic that closes this; until then v1.1 uses "colour + icon + text" without a defined palette. This is principled but adds a forward dependency.

## Required revisions (remaining from v1)

| # | Item | v1 status | v2 status |
|---|---|---|---|
| 1 | Live visual verification of `docs/design-foundations.html` | Required | **Closed 2026-05-16** (PR #4) |
| 2 | Topic 1 quiz answers | Required | **Closed 2026-05-16** (PR #4) |
| 3 | Topic 1 viva answers | Required | **Closed 2026-05-16** (PR #4) |
| 4 | Decide 12-topic scope | Required | **Closed 2026-05-16** (execution plan §1.1 ratified) |
| 5 | Continue Topic 2 deep reading | Required | **Closed 2026-05-16** (PRs #5 + #6) |
| 6 | Preserve Lab 01 recommendations as v1.1 design gates | Required | **Partially closed** — Topic 2's rule sheet operationalises them at component level; Topic 3 will operationalise them at journey level |

All v1 required revisions are now closed or partially closed. The remaining work is forward progress (Topics 3–12), not back-filling.

## New required revisions (v2)

Generated by Topic 2 closure:

1. **Continue Topic 3 — UX design** with the same course pattern. Topic 3 is the next topic on the ratified execution plan and gates Browser v1.1 implementation.
2. **After Topic 3 closes**, implement Browser v1.1 against (the Topic 2 rule sheet) + (Topic 3's reviewer-journey + UX-acceptance-criteria companion).
3. **Update `docs/design-foundations-app/data.js`** per-topic as each closes, so the dashboard's "Digested modules" count tracks reality.

## Stretch improvements (carried forward)

1. Implement Destination Master Browser v1.1 using the Lab 02 rule sheet (now scoped and ready).
2. Create a portfolio case study from Topic 1 + Topic 2 + the v1.1 implementation (once v1.1 lands).
3. Add a dashboard link to the lab results and grade reports.
4. Add automated validation to ensure each completed topic has source types and exercise evidence (`sync.js` already checks completed topics; the rule could expand to check deep-reading-doc presence and lab-submission presence).
5. Convert the three Topic 2 reusable capabilities (master-detail pattern, nine-state checklist, affordance triple-check) into formal capability cards under `capabilities/` once enough patterns accumulate.

## Instructor-style comments

Topic 2 is the strongest topic shipped in DES-001 so far. The structural insight — that naming the pattern (master-detail with faceted filtering) fixes most component choices — is the kind of design vocabulary the assignment was set up to develop. The two-PR split (reading then lab) is a clean operational pattern that should become the template for Topics 3–12.

The Lyra review catching a real defect (six-versus-seven trust states) is the kind of QA process that turns "we wrote it" into "we wrote it and we checked it". That belongs in the academic-discipline column.

The biggest remaining weakness is the unchanged one from v1: ten topics still need to close before benchmark promotion of the whole assignment is on the table. At Topic 2's pace and quality, this is reachable; the question is calendar, not capability.

## Decision: next action

**Start Topic 3 — UX design.** The ratified execution plan gates Browser v1.1 implementation on Topic 3 closing. Topic 3 produces the reviewer-journey + UX-acceptance-criteria companion to Topic 2's rule sheet. Both are required before v1.1 code lands.

Recommended sequence (unchanged from v1):

```text
Topic 3 — UX design
Then Destination Master Browser v1.1 implementation
Then Topics 4 → 12 in execution-plan order
Then final grade report v3 + benchmark-promotion decision
```

## Grade status

This report grades the current Topic 1 + Topic 2 milestone as Excellent / Distinction with Benchmark eligibility blocked only by remaining topic breadth. DES-001 remains open until either the full 12-topic scope is completed or the assignment scope is explicitly frozen for interim submission.

Next grade report (v3) is expected after Topic 6 (the §3 plan's first interim gate) or after Topic 12 (the full-assignment grade).
