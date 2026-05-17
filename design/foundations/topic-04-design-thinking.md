# DES-001 Topic 4 — Design thinking

Status: deep reading executed; source comparison and browser application complete; ready as input to Lab 04 and to Browser v1.2 backlog work.

Lecture: `curriculum/courses/des-001-design-foundations/lectures/lecture-04-design-thinking.md`
Reading pack: `curriculum/courses/des-001-design-foundations/readings/topic-04-design-thinking-reading-pack.md`
Lab to be executed against this doc: `curriculum/courses/des-001-design-foundations/labs/lab-04-design-thinking-loop.md`
Companion topics:
- `design/foundations/topic-03-ux-design.md` (UX design — Topic 4's downstream pairing for criteria-writing)
- `design/foundations/topic-02-what-is-ui-design.md` (UI design — Topic 4's downstream pairing for component decisions)

## 1. Topic definition

Design thinking is the **iterative process** of moving from a fuzzy human problem to a tested solution, by repeatedly:

1. **Understanding** the user through observation and conversation
2. **Framing** the right problem as a point-of-view that opens — rather than presupposes — the solution space
3. **Generating** many candidate solutions without filtering
4. **Making** something concrete cheap enough to throw away
5. **Testing** with real users and capturing what they did
6. **Returning to step 1** with what was learned

The verbs are load-bearing: design thinking is a *process that produces artifacts at every stage*. It is not "thinking about design", not "being creative", not "having a workshop", and not a worldview. It is the artifact-producing iterative loop and the evidence-per-stage discipline that distinguishes it from design-by-opinion.

Three further claims:

- The loop is the point. Single-pass design thinking is design thinking only by accident.
- The most common practical failure is to skip Ideate — committing to the first plausible solution rather than choosing the best from a generated set.
- Design thinking sits *upstream* of UX-criteria-writing (Topic 3): it figures out *what* the journey must produce when the team doesn't already know.

## 2. The five-stage canonical and its compressions

### 2.1 d.school 5-stage

The Stanford d.school *Bootleg* method cards define the canonical stages:

```text
Empathize → Define → Ideate → Prototype → Test
```

Each stage has 5–10 methods (interview techniques, POV templates, brainstorm patterns, prototype types, test scripts). The 5-stage diagram is the most-cited representation of design thinking in the field.

### 2.2 IBM Loop 3-activity

IBM Enterprise Design Thinking compresses the 5 stages into 3 activities — *Observe, Reflect, Make* — and adds two team-coordination devices:

- **Hills** — short ambitious user-outcome statements that the team commits to (similar in shape to Topic 3's GOV.UK user-need form, but more aspirational)
- **Playbacks** — regular structured demos to sponsors and users that keep the loop honest and surface the next iteration's input

### 2.3 NN/g 5-stage (with iteration emphasis)

NN/g's "Design Thinking 101" teaches the same five stages as d.school but emphasises two things the d.school diagram understates:

- The loop is **iterative and non-linear** — teams jump back from Test to Empathize, from Prototype to Define
- Each stage produces a **tangible evidence artifact**; a stage that produced no evidence has not been done

### 2.4 Mapping table

| d.school | IBM Loop | NN/g | Artifact |
|---|---|---|---|
| Empathize | Observe | Empathize | Field notes, interview transcripts, observation summaries |
| Define | Reflect | Define | POV statement, "how might we" question |
| Ideate | Reflect → Make boundary | Ideate | Numbered candidate list (≥3 meaningfully different) |
| Prototype | Make | Prototype | The thing itself — sketch, mock, video, code, role-play |
| Test | Observe (next loop's input) | Test | Feedback notes, observed behaviour, decisions |

The three framings differ on **emphasis** (number of named stages, team coordination) but not on **shape**. A loop run faithfully under any one frame produces the same artifacts.

## 3. Source list and type classification

| # | Source | Type | Why chosen |
|---|---|---|---|
| S1 | Stanford d.school — *Bootleg Bootcamp* | P (Primary process source) | The canonical 5-stage diagram + per-stage method cards. Most-cited single source on the discipline. |
| S2 | IBM Design Thinking — *The Loop, Hills, Playbacks* | A (Applied / team-scale) | Compresses the 5 stages into 3 and adds team coordination devices; useful for understanding how the discipline operates at organisational scale. |
| S3 | Tim Brown — *Change by Design* + HBR essay "Design Thinking" (2008) | P (Primary conceptual / strategic) | The three-constraint frame (desirability / feasibility / viability) that disciplines candidate selection. |
| S4 | Nielsen Norman Group — *Design Thinking 101* + connected articles | X (Cross-check / educational) | The iterative/non-linear discipline + the evidence-per-stage rule. Functions as honest framing against process-purist readings. |

| # | Extension source | Type | Why |
|---|---|---|---|
| E1 | IDEO — *Field Guide to HCD* (different chapters than Topic 3 used) | X | Method catalogue; bridges Topic 4 with Topic 5. |
| E2 | Jeanne Liedtka — *Design Thinking for the Greater Good* + HBR essays | X | Empirical research on design thinking as a managerial discipline; counterweight to consultancy framings. |
| E3 | Kim Goodwin — *Designing for the Digital Age* (scenarios + personas) | X | Operationalising Empathize / Define output into design-ready artifacts. |
| E4 | Don Norman — *Design Thinking: A Useful Myth* (2010 essay) | X (Critique) | The strongest critique; tells the discipline what to defend against. Crucial honesty. |
| E5 | GOV.UK Service Manual — *Discovery* phase | X | Public-sector framing of Empathize + Define; complements IDEO/d.school consulting framings. |

Selection covers: the canonical process (d.school), the team-scale operationalisation (IBM), the strategic frame (Brown), and the honest educational framing (NN/g) — plus a critique (Norman) in the extensions to keep the topic from over-selling.

## 4. Source-by-source notes

### 4.1 Stanford d.school *Bootleg* (S1)

**What it teaches.** The 5-stage diagram is a teaching device. The real meat is the per-stage method library: 30+ methods across the five stages, each on a small card with when-to-use, time estimate, expected output. The implicit thesis is that design thinking is a *toolbox of methods organised by stage*, not a sequential workflow.

**Strongest takeaway.** The d.school is the only required source that publishes named, time-boxed methods per stage. The other sources describe the process; d.school equips you to *do* it. The methods catalogue is the workshop-grade reusable component.

**What it under-emphasises.** Iteration. The diagram is linear; iteration is mentioned but not drawn. NN/g and IBM are needed to correct this.

### 4.2 IBM Enterprise Design Thinking (S2)

**What it teaches.** Three activities — Observe / Reflect / Make — plus three coordination devices: *Hills* (ambitious outcome statements), *Playbacks* (regular demo gates), *Sponsor Users* (real users embedded with the team). The compression to three activities is honest about where the *thinking* happens: the boundary moments (Reflect → Make, Make → Observe).

**Strongest takeaway.** The team-coordination layer. d.school assumes the team is in one room; IBM assumes the team is distributed across multiple roles in an enterprise. For any team larger than one, Hills + Playbacks + Sponsor Users are the difference between "we ran a design-thinking workshop" and "design thinking is how we work".

**What it under-emphasises.** The single-person workspace case. Hills and Playbacks assume sponsors and teammates; CodeMike works alone. The IBM frame still helps (the discipline of stating outcomes ambitiously + producing periodic check-in artifacts), but it needs translation.

### 4.3 Tim Brown — *Change by Design* + HBR (S3)

**What it teaches.** Design thinking as an *innovation discipline* that integrates three perspectives: what people want (desirability), what's technically possible (feasibility), and what's commercially sustainable (viability). The thesis: solutions that satisfy all three are rare and worth building; solutions that satisfy two are candidates to refine; solutions that satisfy one are noise.

**Strongest takeaway.** The three-constraint triage. It is the most-cited disciplining device in design thinking and is the single move that turns Ideate's "many candidates" into Prototype's "one candidate", honestly.

**What it under-emphasises.** Adjudication when the constraints conflict. "Very desirable + barely feasible" vs "highly feasible + mildly desirable" — Brown doesn't tell you how to choose, only that you must satisfy all three. Liedtka (E2) is more useful for the adjudication step.

### 4.4 Nielsen Norman Group (S4)

**What it teaches.** Two correctives to the process-purist framings:

- *Iterative and non-linear*: the actual workflow jumps stages (Test → Empathize, Prototype → Define). The linear diagram is for teaching.
- *Evidence per stage*: each stage must produce a tangible artifact. A stage that produced no artifact has not been done.

**Strongest takeaway.** The evidence-per-stage rule is the honest framing the discipline needs. It separates "we did design thinking" (workshop theatre) from "we did design thinking and here are the seven artifacts to prove it" (the discipline).

**What it under-emphasises.** Strategy. NN/g's framing is operational; Brown's is strategic. Both are useful.

### 4.5 Don Norman — *Useful Myth* (E4, extension)

**What it teaches.** Two arguments:

1. "Design thinking" risks being a *brand* for what skilled designers already do. Calling it a methodology lets organisations claim they "do design thinking" by attending workshops rather than by employing skilled designers.
2. The discipline risks *devaluing domain expertise*. Implying that anyone with the right process can solve any problem under-respects the years of practice that make a domain expert effective.

Norman doesn't call the discipline worthless; he calls it a *useful myth* because the myth gets non-designers to take design seriously. But the myth is dangerous when it substitutes for hiring people with real domain knowledge.

**Strongest takeaway.** Treats Topic 4 as a discipline that needs to be defended against its own overuse. Sources that ignore Norman's critique end up overselling. For DES-001, the critique sharpens the topic's CodeMike interpretation: design thinking is a tool, not a substitute for *also* learning the data-review domain deeply.

## 5. Source comparison

### 5.1 Where the four required sources agree

- The shape is *understand → frame → generate → make → test*, organised as discrete stages with artifacts at each.
- The discipline is *iterative*: one loop is not enough; many loops compound.
- The output of each stage is a *tangible artifact*, not a feeling.
- Empathy with the user is upstream of solution-shaping; skipping Empathize is a process failure.

### 5.2 Where they differ — by emphasis

| Question | d.school | IBM | Brown | NN/g |
|---|---|---|---|---|
| Number of named stages | 5 | 3 | implicit (focus on constraints, not stages) | 5 |
| Team scale | small/co-located | enterprise/distributed | strategic/cross-functional | small to medium |
| Coordination devices | none beyond facilitation | Hills, Playbacks, Sponsor Users | none specified | none beyond evidence-discipline |
| Strategic vs operational | operational | operational + organisational | strategic | operational |
| Iteration emphasis | implicit | explicit (Loop) | implicit | **explicit + diagrammed jumps** |
| Evidence discipline | implicit | medium (Playbacks force it) | low | **explicit per-stage** |
| Per-stage method catalogue | **yes (Bootleg cards)** | partial | no | yes (article-level) |

### 5.3 Where they diverge in ways that matter for the browser

- **Method catalogue.** Only d.school publishes a named, time-boxed method per stage. For CodeMike running solo, this is the most useful single source — it equips the loop with concrete techniques (5 Whys, "yes, and", "I like / I wish / what if", bodystorm). The other sources describe; d.school equips.
- **Iteration.** NN/g most explicitly draws the non-linear jumps; the others leave them implicit. For a single-person workspace where there's no facilitator to enforce iteration, NN/g's explicit framing matters.
- **Three constraints.** Only Brown publishes the triage frame. Without it, Ideate→Prototype is ad-hoc; with it, the transition is defensible.
- **Team coordination.** Only IBM publishes Hills/Playbacks. For CodeMike-solo, Playbacks translate to "regular self-imposed check-in artifacts" — basically the discipline of writing the loop down (which is what Lab 04 does).

### 5.4 What each source omits explicitly

- **d.school**: iteration discipline; the strategic frame; the critique
- **IBM**: small-team / single-person case; the critique
- **Brown**: per-stage methods; adjudication when constraints conflict
- **NN/g**: strategic framing; team-coordination at enterprise scale

No single source covers Topic 4 alone. The four together cover it; one or two would have known gaps.

## 6. The three-constraint triage frame (Brown)

A candidate solution must satisfy:

| Constraint | Question | Pass criteria |
|---|---|---|
| **Desirability** | Does a real user actually want this? | Sourced from Empathize evidence; not "users will love it" speculation |
| **Feasibility** | Can it be built with available technology / skill / time? | Sourced from honest assessment of the team's capacity + the architecture's constraints |
| **Viability** | Does it operate within the surrounding business / operational / regulatory context? | Sourced from the data-trust constraints, the CSV ingest pipeline, the v1.x scope |

**Application to the Destination Master Browser** (three v1.2-candidate examples):

| Candidate | Desirability | Feasibility | Viability | Verdict |
|---|---|---|---|---|
| Batch-promote-to-Planner with confirm modal | Reviewers fear silently shipping the wrong record — strong | Single-file canonical HTML supports modal; modality rules from rule sheet §3.5 apply — feasible | Requires "approve" workflow state; not yet in master CSV schema — partial | Refine — needs Topic 5 / Topic 6 HCD work first |
| Trust-state colour palette (replace placeholder neutrals) | Reviewers asked for it — strong | Trivial CSS change — strong | Requires Topic 10 (Color theory) to be done first — defer | Defer to post-Topic-10 |
| Saved-search / saved-filter URLs | Reviewers want to bookmark common queries — moderate | URL serialisation of filter state — trivial | Fits CSV-static pipeline — strong | Proceed (good v1.2 candidate) |

The triage is *evidence-shaped*: each cell cites a source, not an opinion. A "we just think so" cell is a finding.

## 7. The iterative / non-linear discipline (NN/g)

NN/g's diagram shows the linear path with explicit jumps overlaid. The jumps are:

| Jump | Why it happens | Whether it's healthy |
|---|---|---|
| Test → Empathize | Testing revealed a need we didn't know about | **Healthy** — this is exactly why we test |
| Test → Define | Testing revealed we were solving the wrong problem | **Healthy** — re-framing is the whole point |
| Test → Ideate | Testing revealed the chosen candidate fails; we have other candidates from the original Ideate to fall back on | **Healthy** if the original ≥ 3 candidates still feel fresh; *unhealthy* (Ideate-skipping) if it's a quick swap to a candidate that wasn't in the original triage |
| Prototype → Ideate | While making, we saw a better candidate | **Healthy** — Ideate gets refined as Make exposes constraints |
| Prototype → Define | While making, we realised the problem was framed wrong | **Healthy** but rare; usually means Define was rushed |
| Empathize → Prototype (skipping Define + Ideate) | "We already know what to build" | **Anti-pattern** — the most common practical failure |
| Define → Prototype (skipping Ideate) | "Only one solution comes to mind" | **Anti-pattern** — if only one comes to mind, the team hasn't ideated yet |

The healthy/unhealthy distinction is: jumps that *gather more evidence* are healthy; jumps that *skip evidence-collection* are anti-patterns.

## 8. The Norman critique (E4) and how the other sources respond

Norman's *Useful Myth* argument has two prongs:

1. **Branding hazard** — "design thinking" risks being a label for what skilled designers already do.
2. **Domain-expertise hazard** — the discipline risks implying that the right process substitutes for deep domain knowledge.

How each source implicitly responds:

- **d.school**: The Bootleg cards are explicitly *learning materials* for non-designers in a Stanford classroom. They don't claim to substitute for domain expertise; they claim to make the discipline learnable. This is the strongest defence against prong 1.
- **IBM**: Hills + Playbacks + Sponsor Users embed *domain experts* (the Sponsor User is, by definition, a domain expert) in the loop. This responds to prong 2 directly: the process doesn't substitute, it integrates.
- **Brown**: The three-constraint frame *requires* domain expertise to assess feasibility and viability. A designer alone can assess desirability; the other two need engineering and business expertise.
- **NN/g**: The evidence-per-stage rule is the strongest defence — workshop theatre produces no evidence; real design thinking does. The rule lets organisations tell the difference.

**For CodeMike**: Norman's critique is *useful*, not dispositive. The discipline matters more in domains where the workspace lacks expertise. For DES-001, the data-review domain expertise comes from the Destination Master Browser work itself; design thinking complements it rather than substitutes.

## 9. CodeMike interpretation

For the CodeMike workspace, design thinking is the **upstream pairing for Topic 3 (UX design)**. When the problem is well-framed, Topic 3 alone is enough — write the criterion, check against rule sheet, ship. When the problem is *not* well-framed, run a Topic 4 loop first to figure out what to write a criterion *about*.

```text
Decision tree:

 Problem is well-framed?
   ├─ Yes → Topic 3 (write criterion); reference Topic 4 only if Topic 3 reveals
   │        the criterion can't be written because the underlying need is unclear
   └─ No  → Topic 4 (run a loop); produce a defined problem + tested prototype;
            THEN Topic 3 turns the result into a criterion
```

The CodeMike-shaped working definition of "well-framed":

- The user-need statement (GOV.UK form) is writable without speculation
- The "what would a tested success look like" question is answerable
- The criterion is measurable (interaction count / time / scroll / visibility)

If any of those three fail, the problem isn't well-framed. Run a loop.

## 10. Application to the Destination Master Browser

### 10.1 The v1.2 backlog candidates that need Topic 4 first

Lab 03's gap analysis identified three findings deferred to v1.2+:

- **Collapsible filter panel** — defer; minimal user research; needs a Topic 4 loop to understand whether reviewers actually want collapse vs always-visible
- **Confirm modal for destructive batch actions** — defer; the "destructive batch actions" themselves aren't designed yet; needs Topic 4 to scope which actions, with what consequences
- **Faceted filter panel** — defer pending evidence that current chip-row + dropdown combination is insufficient; needs Topic 4 to test the hypothesis

All three are Topic 4 candidates. Lab 04 picks **one** for a worked loop; the other two stay in the v1.2 backlog with the note "needs Topic 4 loop".

### 10.2 The v1.2 candidates that can skip Topic 4 and go straight to Topic 3

Lab 03's full acceptance-criteria sheet plus the polish items that landed in PR #12 are well-framed. They go straight to Topic 3 criteria-writing when v1.2 starts.

### 10.3 The pairing with Topic 5

Topic 5 (Human-centred design) is the *standards-level* frame for both Topic 3 and Topic 4. HCD (ISO 9241-210) names four activities — *understand context of use*, *specify user requirements*, *produce design solutions*, *evaluate against requirements* — and these are essentially the same four design-thinking compresses. Topic 5 will provide the standards-grade vocabulary; Topic 4 provides the practical toolkit.

## 11. Anti-patterns to refuse

Five anti-patterns specific to design thinking, with attention to the single-person-workspace case:

1. **Skipping Ideate.** Committing to the first plausible solution. The single most common failure. Discipline: always generate ≥ 3 *meaningfully different* candidates.
2. **Single-pass design thinking.** Doing one loop and shipping. The full benefit comes from compounding loops. Discipline: name the next loop's input even if it isn't run yet.
3. **Empathy-by-introspection.** Single-person workspaces are particularly prone to "I am the user" — using self as data. Discipline: at minimum, synthesise three personas in writing (first-time, power, accessibility-need).
4. **Workshop theatre.** Producing no per-stage evidence. The NN/g evidence-per-stage rule is the corrective.
5. **Triage by taste.** Picking the chosen candidate without explicit desirability / feasibility / viability assessment. The Brown three-constraint frame is the corrective.

Each is sourced from ≥ 1 of the four required sources, and the *Useful Myth* critique (E4) is the meta-frame for #4.

## 12. Implementation implications for the v1.2+ roadmap

Topic 4 doesn't ship code. It ships *process discipline* for what to build next. Concrete implementation implications:

1. **Add a "Topic 4 first?" gate** to the v1.2 backlog. Every candidate is annotated *well-framed → Topic 3 only* or *not well-framed → Topic 4 loop first*.
2. **Adopt the three-constraint triage** as the default decision form for choosing one v1.2 candidate over another. Triage in writing; "we just chose this" is a finding.
3. **Adopt the evidence-per-stage rule** for any loop run in the workspace. If a stage produced no artifact, the stage hasn't been done.
4. **Add a Sponsor Reviewer concept** to v1.2 — the IBM frame translated to single-person workspace. A real future reviewer (or proxy) sees each Playback. If no Sponsor Reviewer is available, the workspace stays in self-as-user mode and the limitation is named explicitly.
5. **Run Lab 04** on one chosen pain point as the worked example of the discipline.

## 13. Further reading and exercise tasks

The reading-pack lists five extension sources. The applied exercises Lab 04 will execute:

- One full loop on a single pain point (the lab brief)
- POV statement rewrites (at least twice) to sharpen the insight
- ≥ 3 candidate Ideate output (meaningfully different, not three variants of one)
- Triage table with desirability / feasibility / viability per candidate
- Cheap-form Prototype + falsification-criteria Test specification

Lab 04's decision gate is *evidence-per-stage*: every stage must produce an artifact or the lab is not complete.

## 14. Reusable CodeMike capability extracted from this topic

Three reusable capabilities the workspace gains from Topic 4:

1. **Five-stage design-thinking loop template** with evidence-per-stage discipline — applicable to any future problem-shaped (not feature-shaped) design work in the workspace.
2. **Three-constraint triage frame** (desirability / feasibility / viability with sourced cells) — applicable to any product-decision intake where multiple candidates are in play.
3. **"Topic 4 first?" routing rule** — given a v1.2+ candidate, the workspace can decide whether to run a loop or to skip to criteria-writing.

Combined with Topics 1–3's six capabilities, the workspace now has nine reusable design capabilities — three more than at PR #11. Future capability-card promotion (per `capabilities/README.md`) gets easier as the catalogue grows.

## 15. Reflection on the source set

The reading was honest in one specific way: the four required sources have *different centres of gravity*. d.school is operational (the cards); IBM is organisational (the Hills); Brown is strategic (the constraints); NN/g is epistemic (the evidence rule). A team that stopped at d.school would have methods without strategy; a team that stopped at Brown would have strategy without methods; a team that stopped at IBM would have coordination without epistemic discipline; a team that stopped at NN/g would have honesty without ambition.

The five extension sources sharpen specific aspects: IDEO is methods-deep (overlaps with Topic 3); Liedtka is empirical (counterweight to consultancy); Goodwin is bridge-from-Empathize-to-Design; **Norman is critique** (the most important honest framing); GOV.UK is public-sector Discovery (the most disciplined Empathize → Define operationalisation).

The most operationally important corrective the topic introduces is the *evidence-per-stage* rule (NN/g) combined with the *three-constraint triage* (Brown). Together they distinguish design thinking from design-by-opinion at every stage.

## 16. Open work

- Run **Lab 04** against this topic (`labs/lab-04-design-thinking-loop.md`)
- Produce the **single-pain-point loop** at `design/foundations/topic-04-design-thinking-loop.md`
- Append Topic 4 section to `design/checklists/master-browser-design-checklist.md` (§23 + §24)
- After Lab 04 closes, start Topic 5 (Human-centred design) — the standards-grade frame for both Topic 4 (loops) and Topic 3 (criteria)
