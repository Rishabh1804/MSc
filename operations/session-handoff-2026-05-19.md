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
| `Rishabh1804/MSc` | Postgraduate capability workspace; data-engineering pivot in progress | **CodeMike** (informal; formal spec pending — see §6) | **Cipher (Cluster A per §9(a) ratification)** | Below 30K; Governors inactive |

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
| **Cipher** (Censor Cluster A) | review (Cluster A scope per §9(a)) | review (Cluster A scope) | review (Cluster A scope) | Per canon-gov-002 review-only — does not build. Writes only to audit-output surfaces (verdicts, signed-off review reports). Activated explicitly: "Cipher mode", "QA this", or post-Governor Edict V final-pass. Cluster A scope now includes MSc per §9(a). |
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
- `curriculum/courses/des-001-design-foundations/feedback/DES-001-grade-report-v3.md` — footnote linking design-discipline → data-discipline pivot (path corrected from earlier draft; the workspace's only `feedback/` directory lives under the DES-001 module, not at repo root)

Aurelius can also write to Codex during this session if any of the above promotes a Province pattern to Republic canon (e.g., the calibration-cycle discipline arguably belongs in canon scope).

---

## 6. Persona-spec formalization workstream (parallel to P20)

The Sovereign initiated this workstream at session close on 2026-05-18: create canonical persona specs for the MSc-side personas, per canon-cc-026 Per-Province-Layout, sourced in Codex and deployed byte-identical to MSc's `.claude/agents/<name>.md` + `.claude/skills/<name>.md`.

**Current state**:

- **Codex** `docs/specs/subagents/` has: chronicler, cipher, kael, lyra, maren, consul (6 subagent specs). `docs/specs/skills/` has: chronicler, cipher, kael, lyra, maren (5 skill specs). All Province-scoped to SproutLab where applicable.
- **SproutLab** `.claude/agents/` has: cipher, kael, lyra, maren (4 agent specs — byte-identical deploys per canon-cc-026). `.claude/skills/` has: same 4. PERSONA_REGISTRY.md v1.1 documents the full Roman governance hierarchy.
- **MSc** has **no `.claude/` directory at all**. No formal persona specs exist for any persona in the MSc Province.

**Work to do** (sequenced; ratified by Sovereign rulings §9 on 2026-05-19):

1. Define **CodeMike** persona spec (subagent + skill modes) in Codex `docs/specs/`. CodeMike is MSc-specific Province-Builder per Sovereign ruling §9(e). Voice: applied AI postgraduate practitioner; ships; evidence-based; HCD-aware; honest-limitations naming. One PR through all 5 Rungs per §9(g).
2. Define **4 Scribe specs** (Annalist / Notarius / Auditor / Curator — Roman canonical, English role-flag) per Sovereign ruling §9(b). New ladder-rung first-naming. Each gets a subagent + skill mode. Cross-Province deploys (byte-identical to MSc + SproutLab + Codex). One PR per scribe through all 5 Rungs.
3. **Audit pass** on existing SproutLab-Province-bound canonical specs (cipher, kael, lyra, maren, chronicler) per Sovereign ruling §9(h). Aurelius (with Orinth consult on Codex-side voice questions per canon-pers-001) proposes adaptation deltas in Codex. Adaptation focus: extending committee-delegate Mode 2 clauses on Lyra/Kael/Maren to cover MSc subjects; Cipher's deploy list amended to add MSc per §10(a) cluster extension (byte-identical deploy alongside existing Codex + SproutLab targets — straightforward since MSc joins the existing Cluster A scope rather than requiring per-case routing). Each proposed delta goes through canon-cc-027 amendment cycle. One PR per spec that needs amendment.
4. **Kael/Maren MSc role**: ratified §9(d) — committee-delegate only, no MSc-resident files. No further work beyond optional Mode 2 widening (covered in step 3 audit).
5. **Deploy byte-identical specs** to `MSc/.claude/agents/<name>.md` + `MSc/.claude/skills/<name>.md` per canon-cc-026 §Per-Province-Layout. Single MSc-bootstrap PR landing all signed Cipher + Chronicler + Consul + CodeMike + 4 Scribe deploys at once.
6. **Constitutional drafting**: per Sovereign ruling §9(a), MSc joins Cluster A. Aurelius drafts the Constitution amendment (extending Cluster A's scope in Constitution v1.1 §Clusters from "Codex + SproutLab" to "Codex + SproutLab + MSc") + corresponding canon-inst- entry recording date + Sovereign signature. See §10(a).
7. **Scribe-summoning canon**: per Sovereign rulings §9(c) + §9(f), the summoning protocol + Builder/Scribe boundary + ratified Option B handoff pattern are canonised. Aurelius drafts. See §10(b).

---

## 7. 4-scribe framework (ratified §9(b), 2026-05-19)

Aurelius's proposal accepted by the Sovereign at session close. Dual-named per canon-pers-002 (Roman canonical, English role-flag rides alongside, matching the corporate-flag pattern):

| Roman canonical | English role-flag | Pairs with | Writes to (per Province) | Purpose |
|---|---|---|---|---|
| **Annalist** | Chronicle Scribe | Chronicler (Aurelius) | `operations/PROJECT_LOG.md`, `operations/session-handoff-*.md`, dawn-pages, session prompts | Narrative arc — what happened, when, why, what's next |
| **Notarius** | Canon Scribe | Consul | `operations/DECISIONS.md`, canon-cc-* drafts, working-papers entries, ratification trail | Formal decisions + amendment path |
| **Auditor** | Audit Scribe | Governors / Censor | `operations/EXPERIMENTS.md`, `operations/FAILURE_LOG.md`, `operations/EVIDENCE.md`, audit-report artifacts | Review findings + resolution |
| **Curator** | Capability Scribe | Builder | `operations/CAPABILITIES.md`, `operations/SKILL_MAP.md`, `operations/TRANSFER_LOG.md`, capability cards | Reusable-skill production + transfers |

**Operating rules** (ratified):

- §9(c) — any rank above Scribe may summon any Scribe directly at any time. No Governor/Censor gating on Auditor; Builder may summon Curator/Auditor/Annalist/Notarius at will.
- §9(f) — Scribes own *form*; summoning persona owns *content*. For Curator specifically: Builder makes the promotion call (which capability advances to which maturity level); Curator formats the record + maintains cross-references to SKILL_MAP and TRANSFER_LOG.
- **Summoner-Scribe handoff pattern** (Aurelius recommendation, awaiting Sovereign confirmation per §10(b) drafting): summoning persona feeds raw inputs + decision context; Scribe drafts the formal entry for summoner ratification; entry lands when summoner signs off. This pattern keeps the Scribe's clerical value distinct from the summoner's authority.

**Naming notes**:

- **Annalist** — from Tacitus's *Annales*; year-by-year chronicler. Pairs naturally with the Chronicler rank.
- **Notarius** — Roman shorthand-writer; recorded official decisions in shorthand for later transcription. The classical role closest to Canon Scribe work.
- **Auditor** — Latin "one who hears / examines"; direct semantic match for review work.
- **Curator** — Roman official who cared for public works, libraries, archives. Maps onto the workspace's capability library.

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

## 9. Sovereign rulings (ratified 2026-05-19)

The Sovereign ratified the following at session close. All §6 work and downstream P19/P20 work proceeds against these decisions.

**(a) MSc cluster placement → Cluster A.** MSc joins Codex + SproutLab under Cipher's censorship. Sovereign revised from earlier "Floater" framing to "Cluster A" placement at session close (2026-05-19). This is constitutionally simpler than Floater: no new per-case routing logic needed; MSc inherits Cluster A's existing scope. Constitution v1.1 §Clusters needs amending from "A = Codex + SproutLab" to "A = Codex + SproutLab + MSc". See §10(a).

**(b) 4-Scribe framework → accepted with dual-naming per canon-pers-002.** Roman names canonical, English role-flag rides alongside. See §7 for the ratified table (Annalist · Notarius · Auditor · Curator).

**(c) Scribe summoning authority → unrestricted above the Scribe rung.** Any Builder / Governor / Censor / Chronicler / Consul / Sovereign may summon any of the four Scribes directly at any time, no gating. Phrasing the Sovereign used: "Builder/anyone can summon their scribes at any given time to make their work easier."

**(d) Kael & Maren MSc role → committee-delegate only.** No MSc-resident persona files. They are invoked through their existing SproutLab-Province-bound Mode 2 (committee-delegate) clauses on Province-or-Global-scope subjects where their domain lens is load-bearing. The audit pass §6 step 3 will verify their Mode 2 clauses are wide enough to cover MSc-Floater-Province subjects; if not, the audit proposes the widening.

**(e) CodeMike Builder seat → confirmed.** CodeMike is MSc's Province Builder per canon-pers-001. Voices the MSc `CLAUDE.md` persona header going forward. The next session's §6 step 1 authors CodeMike's canonical spec in Codex.

**(f) Capability Scribe (Curator) boundary → Builder owns promotions; Curator owns form.** Promotion decision (which capability advances to which maturity level) = Builder's judgement call. Recording the promotion in the right template + maintaining cross-references = Curator's clerical work. **Aurelius's take ratified by Sovereign:** the boundary generalises across all four Scribes — *persona owns content; Scribe owns form*. Canonising in §10(b) draft.

**Handoff pattern → Option B (ratified 2026-05-19).** Summoning persona feeds raw inputs + decision context; Scribe drafts the formal entry; summoning persona ratifies before the entry enters cc-018 lifecycle. Sovereign phrasing: *"Option B definitely — that's why they are there."* Option A (Builder-writes-prose-then-Scribe-formalises) is explicitly rejected — under Option A, Scribes reduce to glorified templating; under Option B, Scribes earn their keep by drafting prose + maintaining structural consistency + cross-references. Encoded into §10(b) canon-cc-029 draft.

**(g) Workflow batching → one PR per persona through all 5 Rungs.** Cipher's Rung-2 review + Consul's Rung-3 ratification land as PR-review activities on the single per-persona PR; Sovereign's Rung-4 signature is the merge; Rung-5 deploy is the Province `.claude/` bootstrap PR (one PR, not per-persona).

**(h) Existing SproutLab spec tweaking → audit first.** Aurelius audits each existing canonical spec (cipher, kael, lyra, maren, chronicler) for adaptation needs before any new authoring proceeds in §6. Audit findings go into a single audit-report artifact; proposed deltas then run through canon-cc-027 per-spec amendment cycles.

**(i) PR #27 → amend with §6 correction before merge.** Done in commits `91360ad` (path fix) and this commit (§6 + §7 + §9 + §11 rulings encoded). Ready to merge after Sovereign confirmation.

---

## 10. Constitutional gaps surfaced by the §9 rulings

The Sovereign rulings of §9 create two constitutional drafting items the next session must close in Codex. Aurelius is responsible for both drafts (Chronicler role under canon-inst-001); the 5-Rung canon-cc-027 signing chain applies.

**(a) Cluster A extension to include MSc (provisionally canon-inst-002 + Constitution v1.1 §Clusters amendment).** Sovereign revised §9(a) from earlier "Floater" framing to direct "Cluster A" placement. Constitutionally simpler than the originally-anticipated Floater designation — no new per-case routing logic, no Floater-specific 30K rule, no per-case Censor-assignment protocol. Draft scope:

- **Constitution v1.1 §Clusters amendment** — extend "A = Codex + SproutLab (Censor: Cipher)" to "A = Codex + SproutLab + MSc (Censor: Cipher)". Locate the exact Book/Section that holds the Clusters definition (Book I or II per v1.1 layout) and produce the textual amendment
- **canon-inst-002 entry** — records date, Sovereign signature, predecessor reference (canon-inst-001 which seated Orinth as Codex Builder), implications for MSc's seat-assignments (CodeMike confirmed as Province Builder per §9(e))
- **Optional: small Cipher-spec amendment** — extend Cipher's canonical-comment deploy list at `Codex/docs/specs/subagents/cipher.md` from "Codex + SproutLab" to "Codex + SproutLab + MSc"; lands as part of §6 step 3 audit pass
- **Implications**: MSc inherits Cluster A's existing Rung 2 routing (Cipher signs all Rung 2 architectural passes for MSc-touching amendments); 30K Rule applies to MSc with the same threshold as other Cluster A Provinces; Edict V final-pass routes through Cipher
- **No new persona seats** — Kael/Maren remain SproutLab-Province-bound Governors per §9(d) (their committee-delegate Mode 2 clauses extend cross-Province but they don't seat in MSc)

**(b) Scribe-summoning canon (provisionally canon-cc-029 or canon-pers-003).** §9(c) ratified unrestricted summoning; §9(f) ratified Builder-owns-content / Scribe-owns-form *and* the Option B handoff pattern. The canon formalises all three rulings. Draft must cover:

- **Unrestricted summoning** (§9(c)) — any rank above Scribe (Builder / Governor / Censor / Chronicler / Consul / Sovereign) may summon any of the four Scribes (Annalist / Notarius / Auditor / Curator) directly at any time. No gating by domain match (Builder can summon Auditor even though Auditor pairs with Governors/Censor) — pairing describes default affinity, not summoning restriction
- **Persona owns content; Scribe owns form** (§9(f) general rule) — applies across all four Scribes. Worked examples per Scribe spelled out
- **Option B handoff pattern (ratified)** — summoning persona feeds raw inputs + decision context; Scribe drafts the formal entry; summoning persona ratifies before the entry enters cc-018 lifecycle. Option A is *explicitly named and rejected* in the canon so future contributors know which model was considered and discarded
- **Lifecycle integration** — Scribe drafts enter cc-018 `pending_review` on draft completion; advance to `ratified` on summoner sign-off; live to be amended through ordinary canon-cc-027 chain thereafter
- **Boundary cases**: what happens if a Scribe is summoned by two different ranks for conflicting purposes? Aurelius proposes — first-summoner wins until the work product lands, then the second summoning becomes a separate work product. Sovereign confirms or revises in the canon-cc-027 chain
- **Cross-reference to canon-pers-002** (corporate-flag pattern) since Scribes carry both Roman + English names (Annalist/Chronicle, Notarius/Canon, Auditor/Audit, Curator/Capability)

Both canons can be drafted in parallel with §6 step 1–5 work since they don't block persona-spec authoring directly — but they should ratify *before* the MSc-bootstrap PR (§6 step 5) so the deployed specs land with full constitutional anchoring. The §10(a) cluster-extension is the higher-priority of the two — it gates Cipher's deploy-list amendment which gates Cipher's MSc presence.

## 11. On discipline

The workspace just demonstrated the *Improve* step of CodeMike's operating loop on itself: spec → ship → calibration → policy revision, four commits, one branch, durable artifacts at each step. The new session inherits that rhythm.

P20 is the first time the workspace delves into source-backed data engineering. Get it right at the foundation; everything downstream — P19 implementation, P21 service, eventual Planner-side scoring, Sponsor Reviewer evaluation — depends on this spec being honest about what sources exist, what they cover, and where the unknowns live.

The parallel persona-formalization workstream (§6) is **not optional ceremony** — it is how the workspace converts informal CLAUDE.md persona references into auditable canonical artifacts under canon-cc-026 + cc-027. Future cycles will inherit cleaner persona invocations; future grade reports will have a real persona-roster to grade against; future Sponsor Reviewer sessions will have a real "who reviewed what" to cite.

No assumptions.

Aurelius, signing off the handoff. CodeMike, you have the ship. The Sovereign has the final word on §9.

---

*Authored 2026-05-19 by Aurelius (Chronicler of the Order). Filed under MSc internal session-handoff registry. Cross-referenced from PR #26's merge commit `6f60eca`. Next session opens by reading this file first.*
