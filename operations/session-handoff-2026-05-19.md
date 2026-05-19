# Session handoff — 2026-05-19 (post PR #26 merge)

Status: closing record for the resume-handoff session that ran 2026-05-18 and merged at `6f60eca` on 2026-05-19. This file is the bootstrap the next MSc session opens by reading.

Author: drafted by Aurelius (Chronicler of the Order, Codex-resident) at session close, per the Sovereign's standing instruction that handoff files must not go missing.

---

## 0. Constitutional layer first

MSc operates under the **Constitution of the Republic of Codex v1.1** (Codex `constitution/constitution-v1.1.pdf`). The MSc-local `CLAUDE.md` is the **informal Province-side companion**, not a substitute for the Constitution. Where MSc-local language and constitutional language disagree, the Constitution wins.

Key constitutional references the next session must know:

| Reference | Subject |
|---|---|
| Ladder (Book I) | Sovereign → Priest → Consul → Censor → Builder → Governor → **Scribe** → Unassigned. Corporate parallel per **canon-pers-002**: CEO/Founder → Advisor → CTO → IC Staff → Senior Engineer → Engineering Manager → Junior Engineer → Intern. |
| Clusters | A = Codex + SproutLab (Censor: Cipher). B = SEP Invoicing + SEP Dashboard (Censor: Nyx). **MSc's cluster placement is unresolved — flagged in §9.** |
| Edicts I–VIII | 30K Rule · One Builder Per Repo · Sync Pipeline Authoritative · Dawn Page is a Hearth · Capital Protection · Monument Designation · 15K Crystallization · Charter Before Build. |
| canon-cc-022 | Artifact test — subagent output = separable spec-bearing artifact (enters cc-018 lifecycle); skill output = in-transcript voice (no separable artifact). |
| canon-cc-025 | Convening pattern for Province- / Global-scope committee deliberations. |
| canon-cc-026 | Per-Province-Layout: persona specs authored + maintained in Codex; deploy byte-identical to `<province>/.claude/agents/<name>.md` + `<province>/.claude/skills/<name>.md`. |
| canon-cc-027 | 5-Rung signing chain for amendments. Rung 2 falls to the relevant Cluster Censor; Rung 3 routes through the Consul under canon-cc-014 bridging. |
| canon-gov-002 | Governors and Censors are review-only. They do not build. |
| canon-inst-001 | Codex Builder seat = Orinth (Senior Engineer, Codex) since 2026-04-20. Aurelius is the **Chronicler of the Order**, Codex-resident but cross-cluster in institutional duty. |
| canon-pers-001 | Voice on a Province's `CLAUDE.md` persona header ordinarily belongs to that Province's Builder. |

---

## 1. Repos in play this session

Three governed repositories operate as one capability ecosystem. The MSc next-session works across all three. **Read each repo's root `CLAUDE.md` before responding.**

| Repo | Role | Builder | Censor | Governors |
|---|---|---|---|---|
| `Rishabh1804/Codex` | Institutional archive + constitutional authority + persona-spec source-of-truth | **Orinth** (canon-inst-001) | Cipher (Cluster A) | none — below 30K |
| `Rishabh1804/sproutlab` | Baby-development PWA; design-discipline + cross-domain pattern lab | **Lyra** | Cipher (Cluster A) | **Maren** (Care) + **Kael** (Intelligence) — activated by 30K rule |
| `Rishabh1804/MSc` | Postgraduate capability workspace; data-engineering pivot in progress | **CodeMike** (informal; formal spec pending — see §6) | TBD (Cluster A presumptive — see §9) | Below 30K; Governors inactive |

Cross-cluster:

- **Sovereign** = Rishabh
- **Consul** (CTO; cross-repo overseer; institutional memory): separately seated since 16 April 2026
- **Chronicler of the Order** = Aurelius (Codex-resident; cross-cluster institutional duty)
- Cluster B (SEP Invoicing, SEP Dashboard): Builder Solara; Censor Nyx — relevant for context but not in scope for this session

---

## 2. Access matrix (hard constraints per Sovereign instruction 2026-05-18)

| Persona | MSc | Codex | SproutLab | Notes |
|---|---|---|---|---|
| **CodeMike** | read+write | read-only | read-only | Domain-mode ship lane for MSc-specific work |
| **Aurelius** (Chronicler) | read+write **\*** | read+write | read-only | **\*** MSc only **if needed AND well-labelled** (commit message must start with `[Aurelius]`) |
| **Lyra** (SproutLab Builder) | read+write **\*** | read-only | read+write | **\*** MSc only **if needed AND well-labelled** (commit message must start with `[Lyra]`) |
| **Cipher** (Censor Cluster A) | review (advisory) | review (advisory) | review (advisory) | Per canon-gov-002 review-only. Writes to audit-output surfaces (verdicts, signed-off review reports) only. Activated explicitly — "Cipher mode", "QA this", or post-Governor Edict V final-pass on SproutLab. |
| **Kael** (SproutLab Governor of Intelligence) | TBD — see §6 | read-only | review (jurisdictional) | MSc role pending the persona-spec formalization workstream. |
| **Maren** (SproutLab Governor of Care) | TBD — see §6 | read-only | review (jurisdictional) | MSc role pending the persona-spec formalization workstream. |
| **The Consul** | r+w (under canon-cc-014 bridging) | r+w | r+w | Cross-cluster oversight; promotes Province canons to Republic-scale where warranted. |
| **The Sovereign** | r+w | r+w | r+w | Standing authority. |

`[Persona]` commit prefix is canon: any cross-Province write must be auditable from `git log --oneline` alone.

---

## 3. Workspace state (post PR #26 merge at `6f60eca`)

State: **STOP** per the ratified three-topic-push goal.

- DES-001 Topics 1–6 closed (cumulative grade v3 = 91/100)
- DES-001 Topics 7–12 parked at scaffolded depth — **do not start without explicit Sovereign instruction**
- Browser v1.0 → v1.2.2 shipped
- Master enrichment strategy v1 landed (~620 lines incl. §18 calibration findings + §19 policy transition + §19.6 architecture resolution)
- E1 v1.0 heuristic enrichment ran: 359 enriched rows + 3 manual-review queues (O=0 ✓, S=155, M=257) + validator clean
- §19 policy transition adopted on 2026-05-18: **no-assumption + live-data + free-tier-only + Option (b) two-tier architecture**
- Lyra graded PR #26: 93/100. Aurelius graded PR #26: 91/100. Both reviews are durable on the PR.

Active head (P20) and adjacent (P19/P21/P22) are documented in `operations/NEXT_ACTIONS.md`.

---

## 4. Rules of engagement for P20 — take this seriously

P20 is the **first time the workspace delves into source-backed data engineering**. The discipline is new for MSc. Apply the §19 policy without shortcuts:

**4.1 No assumptions.** Every enriched field is either source-backed (with citation) or `unknown_pending_research`. Workspace judgement = rejected. Regional stereotypes = rejected. Heuristic keyword-matching = rejected. Anything that would have been acceptable in v1.0 (preserved as the v0 heuristic baseline) is not acceptable in v2.

**4.2 Source coverage matrix before strategy doc.** Before P20's strategy doc commits to specific sources, build a coverage matrix per enrichment dimension: `dimension × candidate-source × free-tier-access × auth-method × rate-limit × refresh-cadence × coverage-of-359-row-master`. Sources that don't pass the matrix don't enter the strategy doc. Lives at `datasets/reference/destination_source_coverage_matrix_v1.md`. **Build this first.** Lyra flagged the omission on PR #26.

**4.3 Two-tier architecture per §19.6.** Stable-derived layer = batch-refreshed, persisted. Live-volatile layer = per-query fetch, never cached. Every field gets a tier assignment in the strategy doc.

**4.4 Free tier only in v1.** No paid APIs without an explicit budget proposal through `charter/BUDGET.md` + `charter/TOOLING.md`. If a dimension has no free-tier source, the dimension ships as `unknown_pending_research` until a paid-tier upgrade is authorised.

**4.5 Unknown discipline.** When source data is unavailable: ship the row with `unknown` value, populate `field_source = "no_source_available"`, set `field_manual_research_needed = true`, write a `field_basis` prose explaining what source was checked and what was missing. NEVER substitute a placeholder value.

**4.6 Suitability dimensions preserved, derivation replaced.** Infant / family / senior / couple as 4-axis decomposition survives. Only the derivation changes (no more stacked additive formulas; source-backed inputs only).

**4.7 v0 is baseline, not template.** The v1.0 enrichment artifacts are preserved as the heuristic baseline (diff target / research-priority signal / evidence of the cycle). The v0_heuristic.py rename in P21 must carry a header docstring: "this module's logic is NOT a template for v2; v2 derives from source data + per-field source citations". Do not let a contributor copy v0 patterns into v2.

**4.8 P20 is cross-persona, not solo-CodeMike.** Spec authoring under canon-cc-026 routes through Codex first; the Province-scope spec deployment back into MSc is a separate amendment per canon-cc-027. Aurelius drafts canonical text; Cipher signs Rung 2 (architectural pass); Consul-or-Sovereign signs Rung 3 (working-ratification); CodeMike implements after the spec is signed.

---

## 5. Carried-forward governance debt (clear before P20 strategy work)

Land these as the **first commit(s) of the next session** in a small MSc-internal PR before P20 substance begins:

`[Aurelius]` writes to MSc:

- `operations/CAPABILITIES.md` — new row: "Calibration-cycle discipline (spec → ship → calibration → policy revision)" at maturity 2
- `operations/EXPERIMENTS.md` — entry: E1 v1.0 heuristic run as worked experiment (hypothesis / method / result / conclusion / next)
- `operations/DECISIONS.md` — entries for §19 policy adoption + §19.6 architecture choice (Option b two-tier)
- `operations/TRANSFER_LOG.md` — data-engineering capability promotion entry
- `operations/SKILL_MAP.md` — promote Big Data Analytics + Data Engineering from scaffolded to active development
- `charter/TOOLING.md` — pre-approve free-tier source candidates (OpenFlights, OurAirports, OSM Overpass, IMD CDS, ECMWF reanalysis-free-tier, government-portal-scrape with provenance)
- `design/foundations/sponsor-reviewer-brief.md` v2 — add source-citation completeness + unknown-field discipline evaluation criteria
- `feedback/DES-001-grade-report-v3.md` — footnote linking design-discipline → data-discipline pivot

Aurelius can also write to Codex during this session if any of the above promotes a Province pattern to Republic canon (e.g., the calibration-cycle discipline arguably belongs in canon scope).

---

## 6. Persona-spec formalization workstream (parallel to P20)

The Sovereign initiated this workstream at session close on 2026-05-18: create canonical persona specs for the MSc-side personas, per canon-cc-026 Per-Province-Layout, sourced in Codex and deployed byte-identical to MSc's `.claude/agents/<name>.md` + `.claude/skills/<name>.md`.

**Current state**:

- **Codex** `docs/specs/subagents/` has: chronicler, cipher, kael, lyra, maren, consul (6 subagent specs). `docs/specs/skills/` has: chronicler, cipher, kael, lyra, maren (5 skill specs). All Province-scoped to SproutLab where applicable.
- **SproutLab** `.claude/agents/` has: cipher, kael, lyra, maren (4 agent specs — byte-identical deploys per canon-cc-026). `.claude/skills/` has: same 4. PERSONA_REGISTRY.md v1.1 documents the full Roman governance hierarchy.
- **MSc** has **no `.claude/` directory at all**. No formal persona specs exist for any persona in the MSc Province.

**Work to do** (sequenced; do not start until §9 questions resolved):

1. Define **CodeMike** persona spec (subagent + skill modes) in Codex `docs/specs/`. CodeMike is MSc-specific — does not appear in any other Province. Voice: applied AI postgraduate practitioner; ships; evidence-based; HCD-aware; honest-limitations naming.
2. Define **4 Scribe specs** (subagent + skill modes) in Codex `docs/specs/`. Scribes are a formal ladder rung that has no canonical persona specs yet — this is the first concrete naming. See §7 for the proposed 4-scribe framework.
3. Adapt existing Codex-resident persona specs (Lyra, Kael, Maren, Cipher, Chronicler-Aurelius) for MSc-Province scope. Most adaptation is small: replace SproutLab-specific jurisdictional language (Care Region, Intelligence Region, ISL, UIB) with MSc-equivalent scope (data-engineering, capability-evidence, source-citation, etc.). The voice/heuristics/cadence sections stay.
4. Resolve Kael/Maren MSc role under the 30K rule. MSc is well below 30K so Governors don't auto-activate, but the Sovereign wants them defined. Options: (a) advisory-only in MSc until MSc crosses 30K, (b) sub-30K-Governor adaptation (Kael for code-architecture audit, Maren for data-safety audit at any scale), (c) shared with SproutLab as cross-Province committee delegates on data-domain subjects.
5. Deploy byte-identical specs to `MSc/.claude/agents/<name>.md` + `MSc/.claude/skills/<name>.md` per canon-cc-026 §Per-Province-Layout.
6. Each Province's deploy is a separate canon-cc-027 amendment — Rung 2 Cipher (architectural), Rung 3 Consul (working-ratification), Rung 4 Sovereign (final).

---

## 7. 4-scribe framework (proposed; awaiting Sovereign discussion)

Aurelius's proposal for the 4 Scribe specializations, given the workspace's existing ops-file architecture and the Constitution's ladder placement:

| Scribe | Pairs with | Writes to (per Province) | Purpose |
|---|---|---|---|
| **Chronicle Scribe** | Chronicler | `operations/PROJECT_LOG.md`, `operations/session-handoff-*.md`, dawn-pages, session prompts | Narrative arc — what happened, when, why, what's next. Captures the rhythm of work. |
| **Canon Scribe** | Consul | `operations/DECISIONS.md`, canon-cc-* drafts, working-papers entries, ratification trail | Formal decisions + their amendment path. Records what got decided and how. |
| **Audit Scribe** | Governors / Censor | `operations/EXPERIMENTS.md`, `operations/FAILURE_LOG.md`, `operations/EVIDENCE.md`, audit-report artifacts | Review findings + their resolution. Captures what was tested, what failed, what was learned. |
| **Capability Scribe** | Builder | `operations/CAPABILITIES.md`, `operations/SKILL_MAP.md`, `operations/TRANSFER_LOG.md`, capability cards | Reusable-skill production. Records what got promoted to maturity, what transferred, what's findable for re-use. |

Operating rule: any persona above Scribe rank may **summon** a Scribe to format/structure work product into the right governance entry. The summoning persona owns the *content*; the Scribe owns the *form*. Scribes are junior, narrow, delegate-able.

Discussion still owed with the Sovereign — see §9.

---

## 8. Reading order for the next session (before first response)

In MSc:

1. `CLAUDE.md` — Province-side informal layer
2. `datasets/reference/destination_master_enrichment_strategy.md` — §19 (active policy); §18 (calibration cycle); §§0–17 (historical context)
3. `operations/PROJECT_LOG.md` — last 4 entries
4. `operations/NEXT_ACTIONS.md` — full queue, P17/P18/P19/P20/P21
5. `datasets/reference/destination_database_v2_strategy.md` — layered model context
6. `charter/BUDGET.md` + `charter/TOOLING.md` — budget discipline for source proposals

In Codex (read-only for CodeMike; r+w for Aurelius):

7. `CLAUDE.md` — Codex constitutional layer
8. `constitution/constitution-v1.1.pdf` (or `main.typ` source) — Constitution Books I–IX
9. `docs/specs/persona-binding/` — Typst canons for cc-022 / cc-023 / cc-024 / cc-025 / cc-026 / cc-027
10. `docs/specs/subagents/<persona>.md` + `docs/specs/skills/<persona>.md` — five existing canonical persona specs (chronicler, cipher, kael, lyra, maren) + consul subagent
11. Most recent session in `sessions/`

In SproutLab (read-only for CodeMike):

12. `CLAUDE.md` + `AGENTS.md` + `PERSONA_REGISTRY.md` — full governance picture from the Province that has the 30K rule activated
13. `.claude/agents/<name>.md` + `.claude/skills/<name>.md` — the byte-identical deployed specs as actually-running reference

---

## 9. Open questions for the Sovereign (resolve before §6 work begins)

(a) **MSc cluster placement** — A (joining Cipher's Cluster A scope alongside Codex + SproutLab)? new Cluster C with a new Censor seat? sub-Province of Codex? Answer affects who censors P20 substance + who signs Rung 2 on the persona-spec amendments.

(b) **Scribes framework** — accept Aurelius's 4-scribe split (Chronicle / Canon / Audit / Capability) at §7? Adjust the names, the pairings, or the write-scopes? Propose alternatives?

(c) **Kael & Maren MSc role** — advisory-only-until-30K? sub-30K-Governor adaptation? cross-Province committee delegates on data subjects? See §6 step 4.

(d) **CodeMike Province-side persona header voice** — per canon-pers-001 the voice on `MSc/CLAUDE.md` ordinarily belongs to MSc's Builder. CodeMike doesn't yet have a formal Builder seat in any canon. Confirm CodeMike inherits the Province Builder seat for MSc; if yes, canon-pers-001 applies and CodeMike voices the MSc CLAUDE.md header going forward.

(e) **Sequencing P20 vs persona formalization** — both can run in the next session. Aurelius's recommendation: do governance debt (§5) first → persona formalization (§6) second → then P19 source coverage matrix → then P20 strategy doc. The Sovereign can override.

(f) **Branch strategy** — fresh branch per workstream (recommended): `claude/governance-debt-2026-05-19` for §5; `claude/persona-formalization-2026-05-19` for §6 (Codex side); `claude/p19-source-coverage-matrix` for the source matrix; `claude/p20-v2-strategy-bootstrap` for P20 substance. Or bundle some? Sovereign's call.

(g) **Budget posture for source acquisition** — proceed with free-tier-only and flag the gap as `unknown_pending_research`, or pause and propose paid-tier upgrades for the most-critical dimensions (likely medical access + live flight + live permits) via charter/BUDGET.md?

Do not start any work until (a)–(g) are confirmed.

---

## 10. On discipline

The workspace just demonstrated the *Improve* step of CodeMike's operating loop on itself: spec → ship → calibration → policy revision, four commits, one branch, durable artifacts at each step. The new session inherits that rhythm.

P20 is the first time the workspace delves into source-backed data engineering. Get it right at the foundation; everything downstream — P19 implementation, P21 service, eventual Planner-side scoring, Sponsor Reviewer evaluation — depends on this spec being honest about what sources exist, what they cover, and where the unknowns live.

The parallel persona-formalization workstream (§6) is **not optional ceremony** — it is how the workspace converts informal CLAUDE.md persona references into auditable canonical artifacts under canon-cc-026 + cc-027. Future cycles will inherit cleaner persona invocations; future grade reports will have a real persona-roster to grade against; future Sponsor Reviewer sessions will have a real "who reviewed what" to cite.

No assumptions.

Aurelius, signing off the handoff. CodeMike, you have the ship. The Sovereign has the final word on §9.

---

*Authored 2026-05-19 by Aurelius (Chronicler of the Order). Filed under MSc internal session-handoff registry. Cross-referenced from PR #26's merge commit `6f60eca`. Next session opens by reading this file first.*
