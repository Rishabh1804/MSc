# DES-001 Topic 5 — Human-centred design

Status: deep reading executed; source comparison and browser application complete; ready as input to Lab 05 and to grade-report v3.

Lecture: `curriculum/courses/des-001-design-foundations/lectures/lecture-05-human-centered-design.md`
Reading pack: `curriculum/courses/des-001-design-foundations/readings/topic-05-human-centered-design-reading-pack.md`
Lab to be executed against this doc: `curriculum/courses/des-001-design-foundations/labs/lab-05-hcd-audit.md`
Companion topics:
- `design/foundations/topic-04-design-thinking.md` — the *loop* that runs *within* HCD's lifecycle
- `design/foundations/topic-03-ux-design.md` — the *practice* that satisfies HCD's user-requirements activity
- `design/foundations/topic-02-what-is-ui-design.md` — the *components* that deliver HCD's design solutions

## 1. Topic definition

Human-centred design (HCD) is the **standards-grade lifecycle** for designing interactive systems so that they fit the human, not the other way around. It is defined formally by **ISO 9241-210** as a four-activity iterative cycle governed by six principles, and is paired with the **W3C accessibility / usability / inclusion** triad as the lens through which the design's quality is assessed.

Three deliberate moves in this definition:

1. **Standards-grade** — HCD is *audit-shaped*. ISO 9241-210 is a checkable lifecycle, not a stance.
2. **Four activities + six principles** — both must be addressed. An HCD process that runs the activities but ignores the principles (or vice versa) is not HCD-compliant.
3. **Paired with the W3C triad** — accessibility is not a feature of HCD, it is a *part* of HCD's user-requirements and evaluation activities.

HCD is distinct from neighbouring disciplines:

- **vs Topic 3 (UX design)**: UX design *produces artifacts* (journey + criteria); HCD *audits* whether those artifacts satisfy a standards-grade lifecycle. Topic 3 is operational; HCD is regulatory.
- **vs Topic 4 (Design thinking)**: design thinking is a *loop run within HCD when the problem isn't well-framed*. The Topic-4 loop's stages map onto HCD's activities; HCD provides the lifecycle frame the loop sits inside.
- **vs Topic 2 (UI design)**: UI design is the *substrate*. HCD is the discipline that ensures the substrate is correct for the user *in their context*.

HCD is **the umbrella** — Topics 2, 3, 4 are sub-disciplines that operate within it.

## 2. The four ISO 9241-210 activities

The lifecycle:

```text
                                    ┌──────────────────────┐
                                    │   1. Understand and  │
                                    │   specify the        │
                                    │   CONTEXT OF USE     │
                                    └──────────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────────┐
                                    │   2. Specify the     │
                                    │   USER REQUIREMENTS  │
                                    └──────────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────────┐
                                    │   3. Produce         │
                                    │   DESIGN SOLUTIONS   │
                                    └──────────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────────┐
                                    │   4. EVALUATE        │◄──┐
                                    │   against            │   │ iterate
                                    │   requirements       │───┘
                                    └──────────────────────┘
```

Per-activity artifacts:

| Activity | Question it answers | Artifact |
|---|---|---|
| **Context of use** | Who is the user? What are they doing? Where? With what equipment? Under what constraints? | Context-of-use description; environmental + technical constraints; task descriptions |
| **User requirements** | What must the system enable the user to achieve? At what cost? With what accessibility? | User-need statements (GOV.UK form); usability + accessibility requirements; success criteria |
| **Design solutions** | What designs would meet those requirements? | Wireframes; prototypes; specifications; implementations |
| **Evaluation** | Does the design meet the requirements when tested with real users in the actual context? | Evaluation reports; identified gaps; prioritised changes |

The lifecycle is **iterative**: evaluation feeds back into context-of-use; outputs of any stage can trigger a return to any earlier stage.

## 3. The six ISO 9241-210 principles

Six principles that every HCD process must embody:

| # | Principle | Single-person-workspace translation |
|---:|---|---|
| 1 | The design is based on an explicit understanding of users, tasks, and environments | Three-persona synthesis (Lab 04 pattern) as the explicit-understanding substitute; name the limitation that no real users have been involved yet |
| 2 | Users are involved throughout design and development | Sponsor Reviewer concept (Topic 4 §12) — even one real reviewer is enough for compliance; name absence honestly |
| 3 | The design is driven and refined by user-centred evaluation | Playwright walkthrough is machine-grade; human-grade evaluation is the gap to close in v1.2 |
| 4 | The process is iterative | The DES-001 PR cadence + the design-thinking loop together provide iteration; this principle is naturally satisfied |
| 5 | The design addresses the whole user experience | Topic 1 framing (UX is the whole journey, not just the screen) + the seven-step journey already address this |
| 6 | The design team includes multidisciplinary skills and perspectives | The most-stretched principle for solo work. Mitigation: consciously adopt different lenses (designer/engineer/domain-reviewer/accessibility-need user); name the limitation that the same person plays all roles |

For each principle, single-person-workspace mitigation works when the *limitation is named explicitly*. Pretending the principle is fully satisfied when it isn't is HCD non-compliance.

## 4. The W3C accessibility / usability / inclusion triad

W3C frames three overlapping concerns:

```text
   Usability         Accessibility        Inclusion
   ─────────         ─────────────        ─────────
   Works for         Works for users      Works across the
   "most users"      with disabilities    full diversity of
   in "typical"      (including           users (language,
   contexts          assistive tech)      culture, age,
                                          device, context,
                                          ability)
```

The three overlap heavily but aren't identical:

- A design can be usable without being accessible (typical case works; assistive-tech case doesn't)
- A design can be accessible without being inclusive (compliant for users with disabilities but not for low-bandwidth, multi-language, multi-cultural contexts)
- A design that is *only* usable for the typical case can be inaccessible
- A design that meets accessibility standards but ignores typical-case usability is technically compliant but practically poor

HCD requires **all three** — they're three lenses on the same audit, not three separate audits.

**For DES-001**: accessibility is a *precondition* of HCD, not a feature. A design that fails accessibility has failed HCD's *user requirements* activity (which must specify accessibility requirements) and HCD's *evaluation* activity (which must test with accessibility users).

## 5. Source list and type classification

| # | Source | Type | Why chosen |
|---|---|---|---|
| S1 | **ISO 9241-210** — Human-centred design for interactive systems (current edition) | P (Primary standards-grade) | The discipline's auditable spec: four activities, six principles, lifecycle definition. Cited by every other source. |
| S2 | **Don Norman** — HCD essays at NN/g (*HCD Considered Harmful?*; *The Future of Design*; *DOET* chapters) | P (Primary conceptual) | The honest engagement with HCD's risks (over-centring individual user; missing systems thinking). Tells the discipline what to defend against. |
| S3 | **IDEO** — *Field Guide to HCD* (HCD-specific chapters: Mindsets, Methods, Case Studies — distinct from Topic 3/4 chapters) | A (Applied / methods-heavy) | The operational handbook for running HCD work in the field. Specific methods per activity. |
| S4 | **W3C** — *Accessibility, Usability, and Inclusion* (WAI note) | X (Cross-check / standards-grade) | The triad framing that ensures accessibility is part of HCD, not separate from it. |

| # | Extension source | Type | Why |
|---|---|---|---|
| E1 | ISO 9241-11 — Usability definitions and concepts | X (Standards) | The definition of usability that ISO 9241-210 inherits |
| E2 | WCAG 2.2 (revisited from Topic 2) | X (Standards) | The technical accessibility requirements that any HCD-evaluated design must meet |
| E3 | Norman & Nielsen — Definition of User Experience (revisited from Topic 1) | X | The UX scope that HCD's requirements activity must address |
| E4 | Microsoft Inclusive Design Toolkit | X | A concrete operationalisation of the W3C inclusion lens |
| E5 | Jakob Nielsen — *Why You Only Need to Test with 5 Users* | X | Empirical basis for HCD's evaluation activity in practice |
| E6 | GOV.UK Service Manual — Accessibility chapter | X | Public-sector operationalisation of W3C's accessibility-as-part-of-HCD framing |

This selection covers: the standards-grade definition (ISO), the honest critique (Norman), the methods catalogue (IDEO), and the accessibility-inclusion framing (W3C) — plus six extension sources that deepen specific aspects.

## 6. Source-by-source notes

### 6.1 ISO 9241-210 (S1)

**What it teaches.** A four-activity lifecycle (Context-of-use → User requirements → Design solutions → Evaluation) governed by six principles. The standard is *deliberately method-agnostic* — it says what must be done, not how. This is its strength (any team can run an HCD process and have it be HCD-compliant if it hits the four activities) and its weakness (the standard alone doesn't equip you with techniques).

**Strongest takeaway.** HCD is *audit-shaped*. Every artifact a design team produces can be mapped to one of the four activities; an artifact that doesn't map serves no HCD purpose. The audit-shape distinguishes HCD from "we did some user research" — it makes the lifecycle checkable.

**What it under-emphasises.** Methods. ISO 9241-210 leaves the method choice to the team; teams need IDEO (or equivalent) for operational guidance.

### 6.2 Don Norman (S2)

**What it teaches.** Norman's HCD writing makes two important arguments:

1. *HCD Considered Harmful?* — HCD risks over-centring the individual user at the cost of systems thinking. The user is embedded in a larger system (team, workflow, organisation, downstream consumers); designing for the individual without designing for the system can produce locally-optimal, globally-suboptimal designs.
2. *DOET chapters* — HCD is the *only* design framing that doesn't drift into designer-centred design. Every other framing (designer-led, technology-led, market-led) eventually puts the designer's or the technology's or the market's needs above the user's. HCD's structural commitment to *centring* the user is the corrective.

The two arguments are complementary: HCD as a corrective against designer-centring, while warning that "centring the user" doesn't mean "ignoring the system".

**Strongest takeaway.** Norman's *context of use* reading is the strongest defence against his own critique. Context-of-use done properly *is* systems thinking — it includes the user's organisation, workflow, equipment, and downstream consumers, not just the user's individual experience.

**What it under-emphasises.** Specific methods. Norman is a critic and a framer; for operational guidance, pair with IDEO.

### 6.3 IDEO Field Guide HCD chapters (S3)

**What it teaches.** A methods catalogue organised by HCD mindset (e.g., *Embrace ambiguity*, *Learn from failure*) + by activity (research methods, synthesis methods, prototyping methods, evaluation methods). The chapters distinct from Topic 3 (journey-mapping) and Topic 4 (design-thinking methods) cover HCD-specific operationalisation: stakeholder mapping, expert interviews, immersion techniques, co-design sessions.

**Strongest takeaway.** The Field Guide is the most-cited operational handbook for HCD work in the field. For a solo workspace, the case-studies chapters are particularly valuable — they show *what HCD work looks like at scale*, which calibrates expectations for what solo work can and can't claim.

**What it under-emphasises.** Standards-grade compliance. IDEO's framing is *practice*, not *standard*; for the audit-shape, pair with ISO.

### 6.4 W3C Accessibility / Usability / Inclusion (S4)

**What it teaches.** The triad framing. The three concerns overlap heavily but aren't identical; any HCD process must address all three. The note is short and precise; its value is the *vocabulary* it gives: a designer working with the triad can describe gaps in language that all stakeholders understand.

**Strongest takeaway.** Accessibility is not a feature — it's a *part* of HCD's user-requirements and evaluation activities. A team that "did HCD" without explicitly addressing accessibility has not done HCD.

**What it under-emphasises.** Specific techniques for the inclusion lens. The W3C note frames the concern; Microsoft Inclusive Design Toolkit (E4) operationalises it.

## 7. Source comparison

### 7.1 Where the four required sources agree

- HCD is a *lifecycle*, not a method or a workshop
- The lifecycle is iterative — evaluation feeds back into context-of-use
- User involvement is *throughout* the process, not just at the start (research) or the end (testing)
- Accessibility is part of HCD, not separate from it
- The discipline is *standards-grade* and audit-shaped

### 7.2 Where they differ — by emphasis

| Question | ISO 9241-210 | Norman | IDEO | W3C |
|---|---|---|---|---|
| Primary form | Specification | Essay / framing | Methods catalogue | Note / framework |
| Method specificity | Low (intentional) | Low | **High** | Low |
| Auditability | **High** (the standard) | Medium | Medium | Medium |
| Critique surface | None (descriptive) | **High** (warns about over-centring user) | Low | Low |
| Accessibility centrality | Mentioned | Mentioned | Mentioned | **High** (dedicated framing) |
| Team-scale assumption | Multidisciplinary team | Individual + team | Multidisciplinary team | Multidisciplinary team |

### 7.3 Where they diverge in ways that matter for the browser

- **Auditability.** Only ISO gives a checkable specification. Without ISO, "we did HCD" is unverifiable; with ISO, the four activities + six principles are a checklist.
- **Critique.** Only Norman engages the *risk* of HCD over-centring the individual user. Without Norman's framing, HCD risks producing designs that serve individual users but miss the system they're embedded in.
- **Method specificity.** Only IDEO publishes operational methods at depth. ISO is method-agnostic by design; IDEO fills the operational gap.
- **Accessibility centrality.** Only W3C centres accessibility as a *part* of HCD rather than a separate concern. Without W3C's framing, accessibility risks being a post-hoc audit.

### 7.4 What each source omits explicitly

- **ISO 9241-210**: methods; team-scale variation; the critique of HCD itself
- **Norman**: standards-grade compliance; operational techniques
- **IDEO**: standards compliance; the critique
- **W3C**: the wider HCD process; method specificity

No single source covers HCD alone. The four together cover it.

## 8. Norman's *HCD Considered Harmful?* and how the other sources respond

Norman's argument (summarised): HCD risks over-centring the *individual* user at the cost of *systems thinking*. The user is embedded in a larger system (team, workflow, organisation, downstream consumers). Designing for the individual without designing for the system can produce locally-optimal, globally-suboptimal designs.

How each source implicitly responds:

| Source | Response |
|---|---|
| **ISO 9241-210** | The *context of use* activity *is* systems thinking. Done properly, it includes the user's organisation, workflow, equipment, downstream consumers, and constraints. ISO's response is structural: the standard already requires the systems view. |
| **IDEO** | The HCD-specific methods include stakeholder mapping, expert interviews, and immersion techniques — all of which collect systems-level evidence. IDEO's response is methodological: here are the techniques to gather systems context. |
| **W3C** | The inclusion lens explicitly addresses the *system* — language, culture, organisational context. W3C's response is to make systems-level concerns part of the triad. |

**For CodeMike**: Norman's critique is most relevant for the Destination Master Browser's *systems context* — the reviewer is not just an individual; they're a node in a workflow that includes the Planner downstream and the data-engineering team upstream. The v1.1 context-of-use is reviewer-focused; Lab 05's HCD audit will surface this as a gap to close in v1.2.

## 9. CodeMike interpretation — HCD as the umbrella

The hierarchy:

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   └─ Topic 2 — UI design (the components)
```

Every Topic 2/3/4 artifact should map to at least one ISO 9241-210 activity:

| Artifact | ISO activity |
|---|---|
| Topic 1 Lab 01 heuristic audit | Evaluate |
| Topic 2 component rule sheet | Produce design solutions |
| Topic 2 component inventory + state matrix + affordance audit | Evaluate (of v1) |
| Topic 3 user-need extraction | Context of use + User requirements |
| Topic 3 acceptance-criteria sheet | User requirements |
| Topic 3 journey map | Context of use |
| Topic 4 design-thinking loop output | All four activities (compressed into one loop) |
| Topic 4 falsification criteria | Evaluation |
| v1.1 implementation | Produce design solutions |
| 19-gate Playwright walkthrough | Evaluate (machine-grade) |

The HCD frame's value isn't *new artifacts*; it's the *audit* that ensures every artifact ties back to the lifecycle, and that nothing is missing. Lab 05's audit is the worked example.

**Under-served activities in v1.1**:
- *Context of use* at the **systems** level (Norman critique territory) — the workflow downstream of the browser isn't fully documented
- *Evaluation* at the **human** level — no real users have tested v1.1; only machine-grade walkthrough exists

Both gaps are honest; the v1.2 work + Sponsor Reviewer recruitment closes them.

## 10. Application to the Destination Master Browser

### 10.1 The HCD-audit framing for Lab 05

Lab 05 audits v1.1 + Lab 04 Loop 1 against:
- ISO 9241-210's four activities (one row per activity, evidence per row)
- ISO 9241-210's six principles (Pass / Partial / Fail per principle, with evidence)
- W3C triad (usability / accessibility / inclusion) (gap analysis per lens)

The audit produces a prioritised v1.2 HCD findings list, with each finding tagged by the ISO activity it serves.

### 10.2 The expected gaps (anticipated)

Based on the deep-reading work, the audit will likely surface:

| Activity | Expected gap |
|---|---|
| Context of use | Systems-level context (workflow downstream of Planner; data-engineering upstream) not yet documented |
| User requirements | Inclusion-lens requirements (language, multi-cultural reviewer pool, low-bandwidth contexts) not specified |
| Design solutions | Strong (Topic 2 + Topic 3 work covers it well) |
| Evaluation | Human-grade evaluation absent (only machine-grade walkthrough exists) |

Six-principle gaps expected:
- Principle 2 (Users involved throughout): Partial — the three-persona synthesis is a substitute; no real users involved
- Principle 3 (User-centred evaluation): Partial — machine-grade only
- Principle 6 (Multidisciplinary team): Partial — solo workspace; mitigation is naming the limitation

W3C triad gaps expected:
- Usability: Pass (the 19-gate walkthrough covers it)
- Accessibility: Partial (ARIA + keyboard + focus done; full assistive-tech testing pending Sponsor Reviewer)
- Inclusion: Fail (no language, culture, low-bandwidth, or multi-cultural-reviewer considerations yet)

These are anticipated by the deep-reading doc; Lab 05 will confirm or refute and prioritise.

## 11. Anti-patterns to refuse

Four HCD anti-patterns specific to single-person workspaces:

1. **Treating self as user (introspection-as-context).** Filling in *context of use* by writing what the designer themselves does. Collapses HCD's four activities into one. Mitigation: three-persona synthesis (Topic 4 §11) + explicit naming of the limitation.
2. **Skipping the *evaluate* activity.** "We shipped, that's enough" — common in solo workspaces with no team to demo to. Mitigation: at minimum, machine-grade evaluation (walkthrough) + named human-grade gap.
3. **Treating accessibility as a post-hoc audit.** Adding ARIA / keyboard / focus *after* the design is done, instead of specifying them as *user requirements* in Activity 2. Mitigation: accessibility appears in the requirements sheet, not only in the implementation.
4. **Defining the user as "the user" without naming personas or contexts.** Treating the user as monolithic. Mitigation: name personas explicitly; describe contexts per persona.

Each is sourced from ≥ 1 of the four required sources.

## 12. Implementation implications for the v1.2+ roadmap and grade-report v3

Topic 5 contributes the *HCD audit* as a v1.2 backlog gate. Concrete implications:

1. **Every v1.2 backlog item passes the HCD self-audit gate** (quiz Q10): name (a) context of use it serves, (b) user requirement it satisfies, (c) design solution shape, (d) evaluation that would confirm it works. Items that can't pass return to the missing activity.
2. **The v1.2 HCD findings list from Lab 05** is the prioritised list of HCD-driven changes to ship in v1.2 (in addition to the existing v1.2 backlog from prior topics).
3. **A Sponsor Reviewer is recruited** for v1.2 work — even one real reviewer satisfies Principle 2; absence is named explicitly until then.
4. **Grade report v3** (after Topic 6) incorporates HCD compliance as a marking criterion alongside the existing rubric. The HCD audit's findings inform the v3 grade.

## 13. Further reading and exercise tasks

The reading-pack lists six extension sources. The applied exercises Lab 05 executes:

- Per-activity audit of v1.1 + Lab 04 Loop 1 (Steps 1–4)
- Six-principle audit with Pass/Partial/Fail and evidence (Step 5)
- W3C triad audit per lens (Step 6)
- Prioritised v1.2 HCD findings list (Step 7)
- Master-browser checklist Topic 5 section (Step 8)

Lab 05's decision gate is *audit completeness*: every activity has evidence, every principle has a verdict, every lens has findings.

## 14. Reusable CodeMike capability extracted from this topic

Three reusable capabilities the workspace gains from Topic 5:

1. **HCD-lifecycle audit template** (per-activity evidence + per-principle verdict + per-lens findings) — applicable to any product the workspace builds.
2. **HCD self-audit gate** (the quiz Q10 four-question check) — applicable to any backlog item before implementation.
3. **W3C triad lens** (usability / accessibility / inclusion) as a per-feature evaluation tool.

Combined with prior topics' twelve, the workspace now has **fifteen+ reusable design capabilities** at maturity ≥ 3 (the precise count grows as Lab 05 extracts further capabilities).

## 15. Reflection on the source set

The reading was honest in one specific way: the four required sources have *different roles*, not different positions on the same axis. ISO is the *standard* (audit); Norman is the *critic* (honest framing); IDEO is the *handbook* (methods); W3C is the *vocabulary* (the triad). A team that stopped at ISO would have audit without methods or critique; stopped at Norman, critique without audit or methods; stopped at IDEO, methods without standards or critique; stopped at W3C, vocabulary without lifecycle or methods.

The most operationally important corrective Topic 5 introduces is the *audit-shape* of the discipline (ISO) combined with the *honest naming of single-person-workspace limitations* (Norman's critique applied to solo work). Without the audit-shape, HCD is unverifiable; without the honest limitations, HCD claims become design theatre.

## 16. Open work

- Run **Lab 05** against this topic (`labs/lab-05-hcd-audit.md`)
- Produce the **HCD audit doc** at `design/foundations/topic-05-hcd-audit.md`
- Append Topic 5 section to `design/checklists/master-browser-design-checklist.md` (§26 + §27 + §28)
- After Lab 05 closes, start Topic 6 (Gestalt principles) — the final topic in the three-topic push ending in grade-report v3
