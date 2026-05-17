# DES-001 Viva Answers

Answer date: 2026-05-16. Written to be defendable under questioning rather than to recite the lecture. Each answer is followed by the line a viva examiner would push on, and the follow-up response.

## Topic 1 — UI vs UX

### 1. Why is UI not equivalent to UX?

UI is one ingredient of UX. UI is the surface — controls, layout, states, feedback — and you can produce a flawless UI surface for a system that fails its user (wrong information architecture, wrong content, broken data trust, inaccessible to the user's assistive technology, unworkable in the user's context). UX is the property of the *whole journey*: did the user understand the situation, complete the task, recover from errors, and leave with the right confidence? A polished UI passes a UI review; only the end-to-end task passing passes a UX review.

*Examiner push: "Couldn't a perfect UI guarantee perfect UX in a simple enough system?"*

Only by collapsing UX onto UI by removing every other variable — no data, no context, no users with different needs. Once you reintroduce any of those (which is the whole point of building a system), UX has axes that UI cannot reach: data quality, accessibility, content correctness, support, recovery from external errors. A user can correctly press the right perfect button and still get a wrong outcome.

### 2. Which source gave the broadest definition of UX?

NN/g / Don Norman. The NN/g definition treats UX as "all aspects of the end-user's interaction with the company, its services, and its products." That phrasing explicitly leaves the screen — it includes service touch-points, support quality, content, marketing — and is broader than Figma's product-focused framing, IxDF's design-discipline framing, or UXDT's interaction framing. The breadth matters because it forces the designer to look outside the rendered HTML for failure modes.

*Examiner push: "Is broader always better? Could the broad definition become unfalsifiable?"*

It can. If everything is UX, nothing diagnoses what to fix. The discipline is to use the NN/g definition to *find* failure modes that narrow definitions miss (e.g. data-trust collapse in a dashboard) and then narrow the analysis when prescribing fixes — heuristic per heuristic, journey step per journey step, as Lab 01 did.

### 3. Why is data credibility a UX concern in the Destination Master Browser?

The reviewer's purpose is to make downstream decisions — promote to Planner, mark for enrichment, reject. Those decisions are only as good as the reviewer's confidence about which records are verified. If the UI cannot distinguish verified from unverified, the reviewer either over-trusts (promoting bad records) or under-trusts (re-verifying records that don't need it). Both are UX failures: the reviewer leaves with the wrong mental model. So data credibility is not a backend concern that the UI passively reflects — it is an output of the UX that the UI must actively signal.

*Examiner push: "Why is that a UX concern rather than a data-engineering concern?"*

The data engineering decides *whether* a record is verified. The UX decides *whether the reviewer knows*. A correctly verified record whose verification is invisible to the reviewer is functionally identical to an unverified one for the purposes of the next decision. The boundary between back-end correctness and front-end honesty is exactly where UX lives.

### 4. What is one example of attractive UI causing poor UX?

The card style in v1: rich typography, colour-coded badges, generous spacing — visually appealing — but the most decision-relevant signal (verified vs unverified) is encoded in a small chip among other chips, which trains the reviewer to discount chips as decoration. The pleasant card style raises the *perceived* trustworthiness of the data while reducing the *signal-to-noise* of the trust indicator itself. The UI looks more credible while becoming less informative.

*Examiner push: "How do you know it's the polish causing the problem rather than the data?"*

Because the same data displayed in a stripped-down table — same records, same verification flags, no colour — produces faster correct identification of unverified records in a manual walk-through. The polish is not neutral; it is shifting attention away from the signal.

### 5. Which browser feature is most justified by Topic 1?

A persistent, repeated trust signal at every level of detail: list view (badge on card), detail view (banner at top of drawer), and any export confirmation step. Topic 1 specifically calls out that data-trust is a UX concern that has to be carried through the entire reviewer journey, not just shown once on the list. v1 shows the verification flag on cards but loses it in deeper contexts. Carrying the signal through is the feature Topic 1 most directly justifies.

*Examiner push: "Wouldn't repeating the signal be redundant noise?"*

Only if the reviewer's confidence is constant through the journey. It isn't — by the time the reviewer is inside the detail drawer comparing fields, the list-level signal is out of sight and out of working memory. Repetition is not noise when the alternative is forgetting.

### 6. How should uncertainty be represented in a data-review interface?

By visible, named states rather than absence. A record should be in one of a small set of named states — verified, unverified, planner-ready, blocked, missing-fields, conflict — each with a defined visual treatment. *No badge* should mean "no state assigned yet", which is itself a state. Uncertainty should never be encoded by silence; silence is indistinguishable from "we forgot to check". Colour alone is not enough — accessibility requires the state to be conveyed by text or icon as well.

*Examiner push: "Doesn't naming every state create cognitive overhead?"*

It does, but it's the right kind of overhead. The reviewer has to learn the state vocabulary once. The alternative is that they re-derive trust judgements per record from incomplete cues, which is far more cognitively expensive and produces worse decisions.

### 7. Why should accessibility be treated as part of UX?

Because UX is the property of the journey for the actual users — and some reviewers use keyboard navigation, screen readers, low-contrast displays, or magnification. A journey that succeeds for sighted mouse users and fails for keyboard or screen-reader users has not succeeded — it has succeeded for a subset of users and silently excluded the rest. Treating accessibility as a separate post-hoc audit means the design has already encoded exclusion that needs retrofitting. The W3C framing makes the point explicit: accessibility, usability, and inclusion are facets of the same property.

*Examiner push: "Is accessibility not a legal or compliance concern rather than a UX one?"*

It is also those, but framing it as compliance lets designers pass the bar without engaging with the experience. A WCAG-compliant interface can still be a miserable experience for a screen-reader user if the heading hierarchy is wrong or the ARIA labels are uninformative. The UX framing treats accessibility as a design quality measure, not an audit hurdle.

### 8. What would you revise in the browser after completing the heuristic audit?

In order, the highest-leverage changes from Lab 01:

1. **Add reset and active-filter summary** — addresses "user control and freedom" and recovery. v1 cannot easily undo a filter combination.
2. **Add a table mode for the main list** — addresses "match between system and real world" for the *compare-many* task that cards serve poorly.
3. **Add a detail drawer with persistent trust badging** — addresses "visibility of system status" inside record inspection.
4. **Add explicit empty, loading, and error states** — addresses "help users recognize, diagnose, and recover" and is the data-honesty work Topic 1 most demands.
5. **Add a sort affordance** — addresses Fitts'-style efficiency and aligns to the "scan-by-attribute" reviewer task.

Each of these changes is tied to a heuristic and a reviewer task, not to aesthetics. The order reflects expected impact on workflow completion and trust preservation, the two UX gaps Lab 01 identified.

*Examiner push: "Why not start with visual hierarchy?"*

Because v1's visual hierarchy is competent. Starting there would polish a working surface while leaving the workflow gaps untouched — which is exactly the anti-pattern Topic 1 trains the designer to refuse.

## How these answers were defended

These answers were written to survive viva-style questioning: each one names a specific Lab 01 finding, a specific source, or a specific reviewer task rather than relying on generic design language. The examiner-push lines are real likely follow-ups, not rhetorical fill — they correspond to the points where Topic 1's argument is least obvious.

## Topic 2 — What is UI design

### 1. Define UI design as a discipline and explain why visual design is a sub-skill rather than a synonym.

UI design is the discipline of *choosing* which elements appear, *arranging* them, *specifying their behaviour across all states*, and *visually treating* them — so a user can complete a task with low cognitive cost and unambiguous feedback. The verbs do the load-bearing work: it is decision work. Visual design (colour, typography, illustration, mood) sits *inside* that discipline as the "visually treating" step. A perfectly visually-treated interface that picked the wrong container, missed the loading state, and gave no feedback is a UI failure that happens to look good — which is exactly what makes the conflation dangerous.

*Examiner push: "If visual design is downstream, why do design teams hire visual designers?"*

Because visual treatment is a real specialism — type hierarchy, colour systems, illustration craft are deep skills. The point isn't that visual design is unimportant; it's that visual design serves a UI decision that has already been made. The team that hires a visual designer to fix a usability problem is treating the symptom; the team that hires a UI designer to make the component choices and a visual designer to treat those choices is doing it correctly.

### 2. Name the nine standard component states. Which three are most commonly missing in data-review tools, and why?

`default`, `hover`, `focus`, `active`, `disabled`, `loading`, `empty`, `error`, `success`.

The three most commonly missing are **loading**, **empty**, and **error**. They appear only when the data layer is being honest — waiting, returning nothing, failing. A happy-path UI doesn't render them because the developer never saw them during build. In data-review tools the reviewer specifically needs these states: *loading* tells them the system is fetching (not broken); *empty* tells them the filters narrowed correctly (not that the system failed); *error* tells them what failed and what to do. Their absence reads as silence at exactly the moments the reviewer needs signal.

*Examiner push: "Loading you can argue. But isn't 'empty' just bad data? Why design it?"*

Because in a reviewer tool, *empty is sometimes the correct answer*. The reviewer might be specifically looking for unverified records in a region that happens to have none — that is a successful query with zero rows, and treating it as a failure state confuses the reviewer. A content-rich empty state ("No records match these filters" + which filters are active + a clear-all action) tells the reviewer the query worked and the data answered.

### 3. Distinguish affordance, signifier, and feedback. Why does Norman argue that the signifier does most of the design work in digital interfaces?

- **Affordance** — what the object can do. A button affords being pressed.
- **Signifier** — how the user *knows* it can be done. The button looks pressable: raised, coloured, hovered, focused.
- **Feedback** — confirmation that the action happened. The button visibly responds; the system state updates.

Norman's argument: in the physical world, affordances are often perceivable directly — a door handle suggests pulling. In a digital interface, almost nothing has a physical handle. A clickable card has the affordance of being clicked, but unless the signifier (hover treatment, focus ring, cursor change) makes that affordance visible, the user has no way to know. For digital interfaces, *all affordance is perceived affordance* — which means all affordance lives in the signifier.

*Examiner push: "Doesn't the cursor change handle the signifier?"*

It handles some of it for mouse users — and even then, only after the user hovers. It does nothing for keyboard users, nothing for touch users, and nothing for users who simply don't move their cursor over the element. The cursor change is a *secondary* signifier; the *primary* signifier has to be visible without interaction.

### 4. The five required Topic 2 sources differ less on definition than on emphasis. Name two specific emphasis differences that change a v1.1 design decision.

First: **modality**. Material Design 3 is permissive about dialogs and treats them as a standard container. Apple HIG, Carbon, and GOV.UK are all sceptical and prefer non-modal containers (drawer, side panel, inline disclosure). This is the difference between v1.1 opening records in a modal (Material-shaped) and opening them in a drawer that preserves the list context (HIG/Carbon/GOV.UK-shaped). For a reviewer tool whose central task involves peripheral context, the majority position wins.

Second: **data tables**. Only Carbon treats the data table as a first-class enterprise primitive with sortable / sticky-header / batch-select / row-expansion patterns. Material is light on tables; HIG and GOV.UK are light on tables. The Destination Master Browser's main task is "compare many records along one or two attributes" — a table task. Without Carbon in the source set, the design would default to cards (Material's most prominent list pattern) and miss the central reviewer task.

*Examiner push: "Why not pick the source whose values you share and follow it consistently?"*

Because each source has known blind spots. Material is consumer-shaped; HIG is platform-shaped; Carbon is corporate-shaped; GOV.UK is transactional-shaped. The Destination Master Browser is none of those — it is an internal data-review tool. Picking one source means inheriting its blind spot. Reading all five and using each where it is strongest gives the design a more accurate operating range.

### 5. For the Destination Master Browser, when should a record open in a drawer rather than a modal? When does the choice flip?

Inspecting a record is a *non-blocking* task — the reviewer wants to read the record's full fields, possibly compare it to other records in the list, and either close the inspection or take an action. Peripheral context (the list, the active filters, the trust banner) matters during the inspection. That makes it a **drawer** task.

The choice flips when the task is *blocking and must finish or cancel*. Examples for this product:

- **Confirm destructive action**: "promote 3 records to Planner — confirm?" The reviewer cannot continue browsing while the action is in flight; cancellation is a real option; the wrong outcome is irreversible. **Modal.**
- **Edit with validation that must complete**: rare in this product, but if a single-record edit needed to validate against the master schema before saving, that's a modal task.

The criterion: *does the task need to block the rest of the UI?* If yes, modal. If no, drawer.

*Examiner push: "What about full-page for the inspect task?"*

Full-page is too much for "look at one record and decide". It strips the peripheral context the reviewer is using and adds navigation cost (back-button, scroll-restore). Full-page belongs to flows that have their own substructure — preparing a verified record for export, or editing a record across several fields. Inspect-then-decide is drawer-shaped.

### 6. Why does the topic argue that the unit of design is the *pattern* (master-detail, faceted search) rather than the *component*?

Because component-by-component decisions don't produce coherent interfaces. If a designer decides "add a card", then "add a filter", then "add a button", then "add a modal", each decision can be defensible on its own and the result still fails — because the pattern (the relationship between list, detail, filter, and action) was never named. Naming the pattern first ("this is a master-detail tool with faceted search") fixes most of the component choices: master-detail implies *table + drawer*; faceted search implies *filter chips + persistent active-filter summary*; the persistent stats banner becomes the natural top-of-pattern element. Component invention stops once the pattern is named.

*Examiner push: "Doesn't that just push the decision up a level? You still have to pick the pattern."*

Yes — and that's the point. Picking the pattern is a *task* decision (what is the reviewer doing?), not an *aesthetic* decision. There are maybe a dozen patterns for this whole category of tool; the designer has to pick the one that matches the task. Once that's done, the per-component decisions are mostly determined. Pushing the decision up a level is exactly the improvement.

### 7. Give one example of a Topic 2 anti-pattern that v1 commits, and the v1.1 fix.

v1 commits **inconsistent affordance** in its narrowing controls. The search input and the filter chips are both narrowing controls but use different visual languages (rectangular input vs rounded chip), different state treatments (the input has a clear-button and focus ring; the chips currently have neither visible focus ring nor obvious active state), and produce different feedback (input live-updates; chip toggles are slower to perceive). A reviewer has to learn each separately.

**v1.1 fix**: treat search-and-chips as one "narrow the result set" pattern. Standardise focus rings across both. Make chip-active and chip-inactive states visually as strong as the input's "has content / has been cleared" states. Make both produce the same feedback: a visible result-count animation when state changes.

*Examiner push: "Isn't visual consistency superficial?"*

It's not — it's the *signifier* that tells the reviewer two controls do similar work. Without that signifier the reviewer has to derive the relationship from documentation or trial-and-error. With it, the reviewer learns "things that look like this narrow the list" once and applies it everywhere.

### 8. The topic adds a "when not to use" gate to the master-browser checklist. Why is that gate more important than a "when to use" rule?

Because "when to use" rules are easy to satisfy — there is almost always a defensible reason to add a component. A team that wants to add a carousel can justify it ("it shows multiple items in less space", "competitors use it"). A team that wants to add a modal can justify it ("we needed somewhere to put the form"). "When to use" rules are permissive by construction.

"When not to use" rules are restrictive by construction. They prevent additions that would have passed a "when to use" test but fail the negative-space test ("modal is wrong here because the task is non-blocking; the carousel is wrong here because research shows users miss content past the first slide"). The GOV.UK Design System publishes "when not to use" guidance per component, with research links, precisely because they discovered that "when to use" guidance let through almost any addition.

For the Destination Master Browser, the gate is operationally useful: a request to add a new component must answer "what reviewer task does this serve?" AND "what is the case where this would be wrong?" If the second question has no answer, the component is decoration and is refused.

*Examiner push: "Couldn't a team just write a weak 'when not to use' clause to pass the gate?"*

They could. The mitigation is to make the "when not to use" clause come from user research, prior failure, or a competing pattern that already solves the task — not from imagination. That's the GOV.UK posture: every "when not to use" links to evidence, so it is testable. A "when not to use" clause without evidence is a smell.

## How the Topic 2 answers were defended

Each Topic 2 answer cites at least one specific source (Material, HIG, Carbon, GOV.UK, Norman) and at least one specific reviewer task or v1 finding. The examiner-push lines are the points where Topic 2's argument is least obvious — where a casual reader might agree and then drift back to component-shopping. The follow-ups close those drifts.

## Topic 3 — UX design

### 1. Define UX design and explain why "thinking about users" is not by itself UX design.

UX design is the discipline of *understanding* the user's task, *modelling* the journey they take through it, *designing* the interactions that make the journey succeed, and *evaluating* whether the design actually produces success for real users. The four verbs are load-bearing — UX design is decision work that produces artifacts (journey maps, acceptance criteria, evaluation reports), not a stance.

"Thinking about users" is an input — sometimes a useful one — but it produces no artifact and no decision. A team that "thinks about users" without modelling and without acceptance criteria will still design feature-first, because the abstract thinking does not constrain the next design move. UX design imposes constraints: every journey step has a goal, a cost, a failure mode, and a trust check; every feature has a user-need statement; every design has acceptance criteria that produce reproducible pass/fail verdicts.

*Examiner push: "Couldn't a very experienced designer skip the artifacts and just produce good UX?"*

Possibly for very small designs by a single person — but not at the team or organisation scale that DES-001 targets. The artifacts exist to make the design reproducible across reviewers and auditable across versions. A senior designer who "just knows" produces good UX once; the artifacts produce good UX repeatably and let others contribute without losing the discipline.

### 2. Norman's two gulfs

The **gulf of execution** is between the user's goal and the system action — *how does the user act on the system?* The **gulf of evaluation** is between the system state and the user's understanding — *how does the user know what the system did?* Every interaction crosses both. Most UX failures live in one of them.

v1's `.empty` shared loading/empty/error pane sits on the **gulf of evaluation**. The system is in different states (fetching, no data, failed) but renders the same visual region with the same styling — the user has no way to tell the states apart except by reading the message text. The system has done its work; the user cannot evaluate what it did. Norman's framing is precise: a perceptible difference in feedback is not a polish issue, it is a gulf-of-evaluation failure.

*Examiner push: "Isn't reading the message text sufficient evaluation?"*

It's the minimum, and it's brittle. The user has to remember the three message texts and distinguish them at a glance, often under time pressure. A perceptible *visual* difference — skeleton for loading, content-rich panel for empty, error-coloured banner with action for failure — gives the user instant evaluation without reading. Reading-as-the-only-feedback is a known cognitive-load failure mode that the gulf-of-evaluation framing names explicitly.

### 3. GOV.UK user-need form and the failure it prevents

The form: `As a [user], I need [outcome], so that [goal]` — with **no UI mechanism named**. The failure it prevents is *solution-shape language passing as a user need*. When a team writes "users need a reset button", "users need a dropdown for region", or "users need a card view", they have already locked the design before researching the underlying outcome. The reset button is the only solution if the need is "a reset button"; if the need is "recover from over-filtering without losing orientation", the team is free to pick the best mechanism. GOV.UK's discipline keeps the design options open by forcing the need-statement form upstream of the design.

*Examiner push: "Doesn't naming mechanisms make the need more concrete and testable?"*

It makes it *easier to ship*, not more testable. A genuine user need is testable as a *behaviour*: can the reviewer recover from over-filtering? A mechanism-named need is testable as *presence*: is there a button? The behaviour test is the harder, more honest one. GOV.UK insists on the harder one because it is the one that survives mechanism change without rewriting requirements.

### 4. Two emphasis differences that change a v1.1 design decision

First: **user-need discipline**. GOV.UK strictly enforces the GOV.UK form (no UI mechanism named); NN/g, IDEO, and IxDF allow loose user-need language; Norman is conceptual rather than enforcing. Without GOV.UK in the source set, v1.1 would accept solution-shape needs ("users need a sort dropdown") and ship features that fail when the underlying behaviour wasn't isolated. With GOV.UK, every v1.1 feature must answer to a user-need statement in the strict form. This changes which v1.1 features get built and how they're specified.

Second: **emotional state in journey maps**. IDEO maps emotion per journey step; the other four sources do not. For the Destination Master Browser this difference flips: emotion is not the relevant journey-state variable — *trust state* is. The trust-check column in our seven-step journey map is IDEO's emotional-state column repurposed for a data-review tool. Without IDEO's framing we wouldn't think to put a column there; without GOV.UK's substance we wouldn't fill it with trust.

*Examiner push: "Are you sure trust replaces emotion? Couldn't both belong?"*

Both could belong in a tool where the reviewer's experience matters in emotional terms (e.g. a public-facing data-explorer). For an internal QA reviewer doing structured work, emotional state is a less reliable signal than trust state — and trust is the variable the wrong outcome ("over-trusted unverified records") most directly damages. We can revisit if reviewer feedback shows emotional state is also important; for now trust earns the column.

### 5. Seven steps + most expensive cost budget

The seven steps: **arrive → understand → narrow → compare → inspect → recover → leave**.

The most cognitively expensive is **Compare** (step 4). Cost budget per the deep-reading doc §7: *≤ 60s for the first comparison pass*. The reason: comparing multiple records along common attributes requires holding multiple records in working memory simultaneously, switching attention across rows, and maintaining the active filter context. Cards-only forces serial reading and is the failure mode the cost budget catches; v1.1's table mode with sortable columns is what brings the cost within budget.

*Examiner push: "Inspect feels harder than Compare. Wouldn't reading a full record cost more?"*

Inspect is *deeper* per record but *narrower* across records. Cognitive cost for Inspect is "read this one record carefully"; cost for Compare is "hold five records' relevant fields and switch between them". The cognitive-load literature (and Norman's framing of working memory) treats the multi-record case as the harder one. Inspect has its own budget (≤ 2 interactions to open, ≤ 5s to render) — it's not free, just bounded differently.

### 6. "Compare three records side-by-side" classification and need

This is a **user request** — it came from a real user (a reviewer) but it names a UI mechanism (*side-by-side*) and a system structure (*three records*). The underlying need is:

> *"As a reviewer, I need to compare a small number of records (typically 2–5) on their full detail simultaneously, so that I can identify which is the strongest candidate for promotion or the one needing enrichment."*

The need leaves the design open. A side-by-side three-column comparison view is one valid implementation. A multi-select table-row that opens a compact comparison drawer is another. An export-to-comparison-CSV is another. The right implementation depends on Lab 03's criteria, the cost budget for the Compare step, and how often the task occurs (which is a research question — Topic 4–5 territory).

*Examiner push: "Doesn't 'compare' already exist as journey step 4? Why is this user request different?"*

Journey step 4 covers *scan-by-attribute-across-many*. This request covers *deep-compare-across-few*. They are related but not the same — the cost budget differs (60s for many; longer for deep), the visual treatment differs (sortable table for many; richer comparison for few), and the resulting v1.1 features differ. The journey-map framework can accommodate this as a sub-task of step 4 or as a step-4-plus that opens from inspect — Lab 03 will decide. The request is a useful surfacing of a need that the seven-step map under-specifies.

### 7. v1.1 decision that needs both sheets

**Recovery from an empty-result state.** The component rule sheet (Topic 2) specifies what the component is: *a content-rich empty state component, distinct from the loading and error components, containing an active-filter summary, a Clear-all action, and a what-to-try-next message*. The acceptance-criteria sheet (Topic 3) specifies what the behaviour is: *from any empty-result state, the reviewer can return to a non-empty result set in ≤ 1 interaction; the active filters are listed and individually removable*.

If the criteria sheet is missing: the components exist but the reviewer might still take 4 interactions to recover because the Clear-all is below the fold. The components passed; the behaviour failed.

If the rule sheet is missing: everyone agrees recovery should be ≤ 1 interaction, but no one decided what the component is — does the reviewer click a button, remove a chip, or hit a menu? Three teams build three different empty states.

Both are required. The rule sheet says *what to build*; the criteria sheet says *how it must behave*. v1.1 ships only when both are satisfied.

*Examiner push: "Couldn't a sufficiently good rule sheet imply the behaviour?"*

Rule sheets specify components; they say nothing about scroll position, cumulative-interaction count across the journey, or feedback latency. Two designs that ship the same components can produce very different behaviour. The criteria sheet is the gate that catches that gap.

### 8. Why "happy path only" is specifically dangerous in data-review tools

Most consumer products spend most user-time in happy paths: browsing Netflix, scrolling Instagram, sending email. Empty / error / loading states are real but represent a small fraction of total user-time.

Data-review tools spend most reviewer-time in **non-happy paths**:

- *Empty filters* — the reviewer is intentionally narrowing to find candidates with specific characteristics, and zero-result is a frequent and meaningful outcome
- *Conflicting records* — duplicates, contradictions, ambiguous trust state are the *work* of the reviewer, not edge cases
- *Missing fields* — incomplete data is the input the reviewer is reviewing
- *Blocked or unverified records* — the most decision-relevant records by definition

A UX that designs the happy path well and treats the rest as edge cases gets the *easy part* right and the *core work* wrong. For the Destination Master Browser, this is most visible in v1's shared `.empty` component (Lab 02 finding F3): loading, empty, and error — three of the most reviewer-relevant states — share one CSS class with text-only differentiation. The happy path looks polished; the working states are silent.

*Examiner push: "Couldn't a reviewer learn to read the message text quickly?"*

They could, and reviewers do, and that's exactly the problem. A working UX should not require the user to compensate for design omissions. Reviewers reading message text quickly is the *survival strategy*; the design has failed them by requiring it. Topic 3's criteria for non-happy-path states (skeleton for loading, content-rich for empty, named-error-with-action for failure) close this gap.

## How the Topic 3 answers were defended

Each Topic 3 answer cites at least one specific source (Norman, NN/g, IDEO, GOV.UK, IxDF), at least one specific Lab 01 / Lab 02 finding or reviewer task, and ties to the seven-step journey or the acceptance-criteria framework. The examiner-push lines are the points where Topic 3's argument is least obvious — typically where the discipline (user-need form, criteria reproducibility, non-happy-path priority) is most likely to slip back into looser practice. The follow-ups hold the line.

## Topic 4 — Design thinking

### 1. Define design thinking as a discipline (not a worldview)

Design thinking is the iterative *process* of moving from a fuzzy human problem to a tested solution through five stages — empathize, define, ideate, prototype, test — with each stage producing a tangible artifact and the whole loop running many times. What it *produces* that "thinking about design" does not is *evidence at every stage*: field notes, POV statements, candidate lists, prototypes, test results. The artifacts are the falsifiability surface: a team that did design thinking can show you the seven artifacts; a team that thought about design cannot.

*Examiner push: "Couldn't a skilled designer produce the same outcome without going through the named stages?"*

A skilled designer doing their best work probably does go through the stages; they may not name them. The discipline matters for two reasons: it makes the process *teachable* (others can do it without years of intuition-building) and it makes the process *auditable* (the seven artifacts are the audit trail). Norman's *Useful Myth* critique sits exactly here: the discipline isn't necessary for an excellent solo designer; it's necessary for organisations that want their design to be repeatable, reviewable, and not dependent on a single person's intuition.

### 2. d.school 5-stage vs IBM Loop 3-activity — what each hides

The d.school 5-stage **helps** by separating the artifacts (each stage has its own product) and **hides** the iteration (the diagram is linear; teams that take the diagram literally do one pass and ship).

The IBM Loop **helps** by making iteration explicit (the word "Loop" carries the meaning) and adding team-coordination devices (Hills, Playbacks) and **hides** the boundary moments where the heavy thinking happens (the transition from Reflect to Make is where Ideate's triage actually lives, but IBM doesn't draw that as a separate activity).

For a single-person workspace: use d.school for the named methods (Bootleg cards); use IBM's iteration language to keep yourself honest about looping; use NN/g's evidence-per-stage rule to falsify "I did design thinking" claims.

*Examiner push: "Wouldn't a 7-stage or 10-stage framing be even more useful?"*

No — at some point granularity becomes ceremony. d.school's 5 is enough resolution to separate the artifacts; finer-grained framings start to multiply micro-stages that don't have their own artifacts. The honest test of stage-count is: does each stage produce an artifact a reviewer can hold? IBM compresses to 3 and still satisfies this. Going to 7 or 10 would split artifacts across stages and produce stages that don't earn their place.

### 3. Tim Brown's three constraints applied

The three constraints: **desirability** (does a real user want this?), **feasibility** (can it be built?), **viability** (does it fit the surrounding context?).

Applied to v1.2-candidate **batch-promote-to-Planner with confirm modal**:

- Desirability: **strong**. Reviewers explicitly fear silently shipping the wrong record (Lab 01 finding); confirm-modal-with-undo is the standard mitigation.
- Feasibility: **strong**. Modality rules from Topic 2 rule sheet §3.5 cover the case; the single-file canonical HTML supports modals.
- Viability: **partial**. The "approve and promote" workflow state isn't yet in the master CSV schema. The candidate requires upstream data-model work before it ships.

Weakest constraint: **viability**. The candidate is *correct* design-thinking work, but requires Topic 5 (HCD) and a master-schema extension before it can ship. Decision: refine — not ship-now, but high-value to scope properly.

*Examiner push: "Couldn't you ship a half-version that just shows the confirm modal without the workflow integration?"*

You could, but then the modal would do nothing meaningful — the reviewer confirms, and the record's state doesn't change because the schema doesn't support the new state. That's worse than not shipping; it's a *broken-by-design* trust signal in a tool whose whole purpose is data trust. Brown's framing makes this visible: a candidate that fails viability isn't a candidate to ship-with-asterisks; it's a candidate to refine.

### 4. Healthy jump vs evidence-skipping jump

**Healthy:** Test → Empathize. Testing the prototype with a reviewer surfaces a need we didn't know about; we return to learn more. The principle: jumps that *gather more evidence* are healthy.

**Evidence-skipping:** Empathize → Prototype. Skipping Define + Ideate. "We already know what to build" commits to the first plausible solution. The principle: jumps that *skip evidence-collection* are anti-patterns.

The single rule that distinguishes them is the *evidence flow*. Healthy jumps move *backward* in the loop to collect more evidence at an earlier stage. Anti-pattern jumps move *forward* to bypass evidence-collection at the stages being skipped. NN/g's *Design Thinking 101* makes this explicit; the d.school cards leave it implicit.

*Examiner push: "Couldn't a very fast Empathize → Prototype be efficient rather than evidence-skipping?"*

In small, well-framed problems — yes. But that's exactly the case where you should skip to Topic 3 entirely, not pretend you ran a Topic 4 loop. The honest move: name the problem as well-framed, skip the loop, go straight to criteria-writing. Pretending to run a loop while actually skipping it is what the discipline most needs to defend against.

### 5. Norman's *Useful Myth* critique — sharpen or undermine?

**Sharpens.** Norman's two prongs — design thinking risks being a brand for what skilled designers already do, and risks devaluing domain expertise — are *boundary conditions* on the discipline. They tell the discipline what it is *not*: it is not a substitute for hiring experts; it is not a process organisations can attend instead of practising. Sources that ignore the critique end up overselling. Sources that engage with it (d.school's classroom framing, IBM's Sponsor User integration) end up *more* defensible, not less.

For DES-001 specifically: the critique tells CodeMike that design thinking is a *complement* to deep domain knowledge of the data-review work, not a *substitute* for it. The Destination Master Browser would not be improved by more design-thinking workshops; it is improved by design thinking *applied to real reviewer evidence by someone who understands the data*.

*Examiner push: "Doesn't 'sharpens' just mean 'we ignored the strongest part of the critique'?"*

The strongest part of Norman's critique is that the discipline risks substituting for expertise. We defend against it by *naming the substitution risk explicitly* in CodeMike's interpretation (deep-reading doc §8) and by structuring the Topic 4/Topic 3 pairing so that loops only run when the problem isn't well-framed (i.e., when domain expertise alone is insufficient). That's engagement, not avoidance.

### 6. Test that tells you a problem is well-framed enough to skip Topic 4

Three conditions (deep-reading doc §9):

1. The user-need statement (GOV.UK form: `As a [reviewer], I need [outcome], so that [goal]`) is writable without speculation
2. The "what would tested success look like" question is answerable
3. The criterion is measurable (interaction count / time / scroll / visibility)

If any of those three fail, the problem isn't well-framed; run a loop. If all three pass, write the criterion (Topic 3) and skip Topic 4.

Example of a well-framed problem (skip Topic 4): "the empty state silently fails — fix it". All three conditions hold; the criterion `U-REC-1: recovery in ≤ 1 interaction` follows directly.

Example of a not-well-framed problem (Topic 4 first): "reviewers feel slow on Planner-promotion". The user-need is writable but the *outcome* is unclear (faster how? safer how? with what guard-rails?). Loop first.

*Examiner push: "Couldn't the criterion-writing process itself surface that the problem isn't well-framed, and the loop happens then?"*

Yes — and the cleanest version of the discipline catches it both ways. Either the framing-check fails before Topic 3 starts, or Topic 3 surfaces an unanswerable criterion and recursively triggers Topic 4. Both paths converge to the same outcome: a loop runs when domain expertise alone is insufficient.

### 7. Topic 4 disciplines in single-person workspaces

**Transfer directly:**
- Evidence-per-stage rule (NN/g) — works regardless of team size; writing artifacts is a one-person task
- Three-constraint triage (Brown) — works for one designer assessing one set of constraints
- POV statement form (d.school) — works for one-person framing
- The decision tree (Topic 4 first vs Topic 3 first) — works regardless of team size

**Need translation:**
- IBM Hills + Playbacks — Hills work fine as solo-written outcome statements; Playbacks need translation to "regular self-imposed check-in artifacts" because there's no sponsor to demo to. Lab 04 effectively *is* a Playback for a solo workspace.
- Empathy methods — co-located interview techniques don't apply; three-persona synthesis (deep-reading doc §11 anti-pattern 3) substitutes
- IBM Sponsor Users — translate to "Sponsor Reviewer concept" (deep-reading doc §12 item 4); if no real Sponsor Reviewer is available, stay in self-as-user mode but name the limitation explicitly

*Examiner push: "Doesn't the lack of a sponsor mean the discipline is degraded for solo workspaces?"*

It's degraded relative to a team with embedded sponsor users — yes. But it's also degraded relative to design thinking that doesn't run at all. The honest move is to *name* the degradation (self-as-user is not equivalent to real-user-tested) and to defer the heaviest decisions until a real sponsor reviewer is available. That keeps the discipline honest at the scale we have.

### 8. Evidence-free version of a stage + consequence

**Evidence-free Define:** "The problem is the browser is bad."

**Consequence for Ideate:** the next stage has no constraint. "Browser is bad" can be ideated against in a thousand directions; the team commits to whichever direction sounded best in the room. Without a sharpened POV ("[reviewer] needs a way to [specific need] because [insight from Empathize]"), Ideate produces undirected output. The chosen candidate is the one with the strongest advocate in the room, not the one that best serves the (unframed) problem.

Other valid examples:
- Evidence-free Empathize ("we talked to some users", no notes) → Define has no insight to sharpen
- Evidence-free Ideate ("we brainstormed", no list) → Prototype defaults to "the obvious one"
- Evidence-free Prototype ("we described what we'd build") → Test runs on imagination
- Evidence-free Test ("users liked it") → next loop has no input; the loop becomes one-pass design thinking

## How the Topic 4 answers were defended

Each Topic 4 answer cites at least one specific source (d.school, IBM, Brown, NN/g; sometimes Norman from the extension), at least one specific reviewer-task or v1.2-candidate, and connects to Topics 1–3's framework (user-need form, acceptance criteria, journey-step). The examiner-push lines target the points where Topic 4's argument is most likely to slip back into either pure-process advocacy (over-selling) or pure-skepticism (under-selling). The follow-ups defend the middle position the deep-reading doc takes: design thinking is a *tool*, useful when paired with domain expertise, evidence-shaped at every stage.

## Topic 5 — Human-centred design

### 1. Define HCD; distinguish from Topics 3 and 4

HCD is the **standards-grade lifecycle** (ISO 9241-210) for designing interactive systems so they fit the human, not the other way around. Four activities (Context of use → User requirements → Design solutions → Evaluation), six principles, paired with the W3C accessibility/usability/inclusion triad. Distinct from Topic 4 (design thinking is the *loop* run *within* HCD's lifecycle when problems aren't well-framed) and from Topic 3 (UX design is the *practice* that produces journey + criteria artifacts; HCD is the *audit* that ensures those artifacts satisfy a standards-grade lifecycle).

*Examiner push: "If HCD is just an audit, why does it need its own topic?"*

Because the audit-shape itself is a design move. Without ISO 9241-210, "we did HCD" is unverifiable — there's no checklist to satisfy. With it, every artifact maps to one of four activities, and missing activities are visible. The audit-shape transforms HCD from a stance into a checkable lifecycle. That's what makes it standards-grade, and that's what makes it different from Topics 3 and 4 (which produce artifacts but don't audit them).

### 2. Four activities + browser artifacts

| Activity | Browser artifact |
|---|---|
| Context of use | Topic 3 §6 user-need extraction (`topic-03-ux-design-journey-map.md` §Step 3) |
| Specify user requirements | Topic 3 `ux-acceptance-criteria.md` (14 criteria) |
| Produce design solutions | Topic 2 `ui-design-component-rules.md` + v1.1 `destination-master-browser.html` |
| Evaluate against requirements | 19-gate Playwright walkthrough |

The lifecycle is iterative; the v1.1 → v1.2 transition is the next iteration cycle, with Topic 5's audit informing the Context-of-use refresh.

*Examiner push: "Doesn't Topic 4's Lab 04 loop exercise all four activities by itself?"*

Yes, in compressed form. A Topic 4 loop maps Empathize→Context, Define→Requirements, Ideate+Prototype→Design solutions, Test→Evaluate. That's why HCD says design thinking runs *within* the HCD lifecycle — a loop is one *iteration* of the lifecycle, not a substitute for it. The HCD frame ensures that the loop is part of an ongoing process, not a one-off.

### 3. Three principles + single-person translation

- **Principle 1** (Explicit understanding of users, tasks, environments): solo = three-persona synthesis (first-time/power/accessibility-need) as the explicit-understanding substitute; *honestly name* that no real users have been involved.
- **Principle 3** (User-centred evaluation): solo = machine-grade walkthrough as the lower bound; *honestly name* the human-grade gap until a Sponsor Reviewer is recruited.
- **Principle 6** (Multidisciplinary team): the most-stretched principle for solo work. Translation = consciously adopt different lenses (designer/engineer/domain-reviewer/accessibility-need user) within one person; *honestly name* that the same person plays all roles.

The pattern: every translation works when the limitation is *named explicitly*. Pretending the principle is fully satisfied when it isn't is HCD non-compliance.

*Examiner push: "Naming a limitation doesn't fix it. Doesn't that just license cutting corners?"*

Naming doesn't fix; it preserves *honesty*. The fix is the Sponsor Reviewer in v1.2, the multidisciplinary team in v2.x, the iterative cycle that compounds. Naming the limitation makes the gap visible so the fix has a target. The alternative — claiming the principle is satisfied when it isn't — produces design that *looks* compliant but isn't. HCD's discipline is to never pretend.

### 4. W3C triad on v1.1

**Well-served:**
- **Usability** — the 19-gate walkthrough covers typical-case task completion across the seven-step journey. Pass.
- **Accessibility** — substantially served (focus rings, aria-describedby, keyboard nav, screen-reader-friendly drawer). Partial pending real assistive-tech testing.

**Worst-served:**
- **Inclusion** — Fail. Copy is English-only; assumes reviewer knows domain terms like "Planner-ready"; no low-bandwidth consideration; mobile layout exists but not tested as a primary use case; no consideration for non-Western reviewer contexts. The gap is concrete: v1.1 works for an English-speaking desktop reviewer with prior context; it fails for any reviewer outside that profile.

*Examiner push: "Couldn't most of those inclusion gaps be deferred indefinitely without harm?"*

Some can, in scope. But the *naming* matters. A v1.1 that says "we serve English-speaking desktop reviewers; multi-language and low-bandwidth are deferred to v2.x" is HCD-compliant. A v1.1 that silently ignores the gap and ships as "the browser for reviewers" is overclaiming. The inclusion gap is real; the fix is to scope it explicitly.

### 5. Norman's *HCD Considered Harmful?* — defend or attack

**Defend the position.** Norman is right that HCD risks over-centring the individual user. The risk is real because "centring the user" is structurally individualistic — it focuses attention on one user's experience, not on the system they're embedded in. For the Destination Master Browser specifically, v1.1's context-of-use is reviewer-focused; the downstream Planner workflow and the upstream data-engineering pipeline are documented in passing but not as full context-of-use specifications. Norman's critique surfaces this as a real gap.

The defence within HCD: ISO 9241-210's *context of use* activity *is* systems-thinking when done properly. The activity includes the user's organisation, workflow, equipment, downstream consumers, and constraints. A team that does context-of-use seriously is doing the systems thinking Norman calls for. So the discipline contains the corrective; the failure mode is *bad context-of-use work*, not HCD itself.

For DES-001: Lab 05's audit will surface the systems-level context-of-use gap explicitly and queue it for v1.2 to close.

*Examiner push: "Couldn't 'centring the user' be re-defined to mean 'centring the user-in-their-system'?"*

Yes — and that's what good HCD does. But the discipline has to *name* this explicitly. The simple "centre the user" reading risks the over-centring Norman warns about; the "centre the user-in-their-system" reading is what ISO 9241-210's context-of-use activity actually requires. The deep-reading doc §10's expected gaps list anticipates this exact issue for v1.1.

### 6. Topic 4's relationship to the four HCD activities

A Topic 4 design-thinking loop **most directly exercises** *Design solutions* (Ideate + Prototype produce candidate designs). It **secondarily exercises** User requirements (Define produces the POV statement; the requirement form follows) and Evaluation (Test specification names the falsification criteria). It **under-serves** Context of use — the loop assumes the user is understood enough to start Empathize; the broader systems-level context is left implicit.

HCD's compensation: Activity 1 (Context of use) runs *outside* the design-thinking loop. The workspace's context-of-use specification feeds *into* the loop as Empathize input, and the loop's findings refine the specification on the way out. The two work together: HCD provides the lifecycle frame; design thinking is the iteration mechanism inside it.

*Examiner push: "Couldn't you argue the loop's Empathize stage IS the context-of-use activity?"*

In a small workspace, yes — Empathize and Context-of-use can collapse into one. But ISO 9241-210 treats them as distinct because at organisational scale they are: Context-of-use includes stakeholder mapping, regulatory constraints, equipment and environment surveys — work that happens *before* and *outside* any design-thinking loop. For CodeMike solo, the two activities are tightly coupled but should still be *named separately* in the audit, so the gaps in either become visible.

### 7. Anticipated gaps + closures

**Gap 1: human-grade evaluation is absent.** v1.1 was tested with the 19-gate machine walkthrough only; no real reviewers have used it. **Closure**: recruit at least one Sponsor Reviewer in v1.2; run a real-user test of the modal anatomy from Lab 04 against its six falsification criteria.

**Gap 2: systems-level context-of-use is incomplete.** v1.1's context-of-use documents the reviewer's individual experience but not the surrounding Planner workflow downstream or the data-engineering pipeline upstream. **Closure**: produce a systems-context-of-use document in v1.2 (one page, mapping the reviewer's role in the wider workflow), and revisit the user-requirements activity to ensure Planner-downstream and data-upstream constraints are reflected.

*Examiner push: "Couldn't both gaps be closed by the same Sponsor Reviewer interview?"*

Partially. The reviewer can tell you about their own experience (closes Gap 1) and about the upstream/downstream context they know (helps with Gap 2). But a full systems-level context-of-use needs *also* the Planner team's perspective and the data-engineering team's perspective. The Sponsor Reviewer closes the reviewer-centred portion; the wider workflow needs separate stakeholder interviews. HCD's discipline is to name both inputs and not collapse them.

### 8. HCD self-audit gate on a v1.2 candidate

Candidate: **collapsible filter panel** (deferred from Lab 03; one of the three Topic 4 candidates).

| Cell | Content | Strength |
|---|---|---|
| Context of use | Reviewer uses six filters; sometimes wants screen real estate back when scanning many records | Weak — assumes the screen-real-estate need without evidence |
| User requirement | "As a reviewer, I need to reclaim screen space when reviewing many records, so I can scan faster" | Medium — writable but speculative |
| Design solution | Collapsible toolbar with toggle | Strong — Topic 2 rule sheet supports it |
| Evaluation | Walkthrough criterion: reviewer can collapse + expand in ≤ 1 interaction; preserves filter state | Strong — testable |

**Weakest cell: Context of use.** No evidence that reviewers actually want this. The need was inferred from Lab 03's "filters take screen space" observation, not from observed reviewer behaviour. HCD verdict: run a Topic 4 loop to validate the context-of-use claim before adding to v1.2 backlog. (This matches Topic 4 §9's "Topic 4 first when problem isn't well-framed" decision rule — the HCD gate caught the same issue the Topic 4 routing rule catches.)

*Examiner push: "If two gates catch the same issue, isn't one redundant?"*

No — they catch it from different angles. Topic 4's routing rule asks "is the problem well-framed enough to skip a loop?"; HCD's self-audit gate asks "does every activity have evidence?". Both produce the same answer here because both surface the same kind of gap. Belt-and-braces is appropriate at a v1.2 backlog gate; redundancy is cheap, undetected gaps are not.

## How the Topic 5 answers were defended

Each Topic 5 answer cites at least one specific source (ISO 9241-210, Norman, IDEO, W3C), at least one specific v1.1 or Lab 04 artifact, and connects to the canonical hierarchy (HCD as umbrella over Topics 2 / 3 / 4). The examiner-push lines target the points where HCD's discipline most risks being treated as ceremony — "naming limitations" risks licensing corner-cutting; "audit-shape" risks being treated as a paperwork exercise; "centring the user" risks the over-individual reading Norman warns about. The follow-ups defend the substantive position: HCD is auditable and that's its value; honest naming is the discipline, not the corner-cutting; the audit catches what intuition misses.

## Topic 6 — Gestalt principles

### 1. Define Gestalt; perceptual constraint vs aesthetic rule

Gestalt principles are **perceptual constraints on how the human visual system groups visual elements** — empirical facts about perception established by Wertheimer 1912 / Koffka 1935 / Köhler 1929 and validated repeatedly since. They are not aesthetic rules of thumb, style preferences, or designer conventions. The human will perceive grouping whether the designer intended it or not; the discipline's only job is to make perceived grouping match intended grouping.

The constraint reading is operationally different from the style reading because *defensibility flips*. Under the style reading, "use whitespace generously" is unfalsifiable — a designer can override it on taste and there's no test. Under the constraint reading, every visual choice has to defend itself against what the visual system *will do*: "we used 16px between unrelated controls and 4px within related ones, defending the proximity signal for the toolbar's narrowing-controls group" is falsifiable — you can audit whether the proximity is doing what the design claims.

*Examiner push: "Isn't 'perceptual constraint' just a fancier way of saying 'good design'?"*

No — and the test is *falsifiability*. A good-design claim is satisfied by intuition: it looks fine, ship it. A perceptual-constraint claim is satisfied by audit: you can point to the proximity grouping the design intended and check whether the visual arrangement produces that grouping for a naïve viewer. The constraint framing forces designers to make claims that can be wrong, which is exactly what Topic 6's quiz Q10 gate enforces.

### 2. Prägnanz and the corollary

**Prägnanz** ("good figure" / "good form") says the visual system organises perception toward the **simplest, most stable, most symmetric interpretation** available. The system runs a least-cost interpretation continuously; the cheapest interpretation wins. Computationally: it's cheaper to perceive a group than N separate elements, cheaper to recognise a closed shape than track arc-segments, cheaper to assume aligned elements belong together than to treat each as independent.

Three corollaries worked through:

- **Proximity** is Prägnanz applied to *spatial relationships*: grouping spatially-close elements is cheaper than tracking each element's position independently. Tight spacing → one group is the system's least-cost interpretation.
- **Similarity** is Prägnanz applied to *categorical relationships*: assuming visually-alike elements are functionally alike is cheaper than tracking N categories. Same colour, same shape, same size → one category is the least-cost call.
- **Closure** is Prägnanz applied to *shape recognition*: recognising a closed familiar form is cheaper than perceiving incomplete arc-segments. A frame with one open side is perceived as a complete frame because that interpretation is simpler than "three independent line segments".

Each principle is a different *way* the visual system simplifies; Prägnanz is the *why*.

*Examiner push: "Isn't 'computationally cheaper' just hand-waving? Where does that claim come from?"*

It comes from the cognitive-science extension reading (E4) and from the experimental work in Köhler 1929 + Koffka 1935. Modern cognitive science has substantially confirmed the framing — the visual system is doing constraint-satisfaction with a bias toward simplicity, and this is computational, not metaphorical. The Wertheimer apparent-motion experiments are the original proof: the visual system *adds* perceived motion to discrete stimuli because perceiving continuous motion is the simpler interpretation. Computation is the right word.

### 3. Six core principles with honoured browser examples

| # | Principle | v1.1 example where it's currently honoured |
|---:|---|---|
| 1 | Proximity | Drawer body sections use generous vertical whitespace between sections + tight whitespace within sections — proximity correctly groups field+label pairs and separates sections |
| 2 | Similarity | Trust badge component is visually identical at four depths (card, drawer header, drawer banner, footer) → the eye correctly reads "one signal in multiple places" |
| 3 | Continuity | Table view's columns hold *because* values align vertically; the alignment is the column-as-category signal |
| 4 | Closure | Drawer overlay reads as a contained region even without an explicit top border — the visual system completes the shape from the three borders that *are* visible |
| 5 | Common region | Record cards correctly bind name + place + trust badge + chips into one perceptual unit via the card's bounded region |
| 6 | Common fate | PR #12's result-count flash animation co-varies with filter changes → the eye correctly infers "this count is reacting to that filter change" |

Each example will be audited in Lab 06 against alternative perceptual readings.

*Examiner push: "If the principles are honoured, why does Lab 06 exist?"*

Because *honoured in some regions* is not *honoured in every region*. The six examples above are the regions where v1.1 gets it right. Lab 06's job is to find the regions where v1.1 gets it wrong (toolbar grouping; trust badge inside card metadata grid; sortable column headers; active-filter summary bleed; caution-chip conflict; density compromises). Anticipated violations are listed in deep-reading doc §9.2 and will be confirmed/refuted regionally.

### 4. v1.1 false-positive grouping violation

**Region**: the toolbar (search input + filter selects + view-toggle).

**Principle(s) violated**: proximity + similarity, both arguing for false-positive grouping.

**Violation**: the search input and the filter selects sit close together (proximity → "one group") with similar rectangular input-styling (similarity → "one category of control"). The reviewer reads them as "one group of narrowing controls". But the interaction grammar differs: the search updates *live as you type*, the selects update *on selection change*. A reviewer trained on the search expects live update from a select and is surprised when nothing happens until commit.

**Reviewer-task consequence**: the journey step "Narrow" (step 3 of seven) takes longer than it should — the reviewer changes a select, expects immediate feedback, doesn't get it, hesitates, then commits the change explicitly. Cumulative cost across the seven-filter workflow is meaningful. The fix (Lab 06 to confirm and tag v1.1.x): either *unify* the grammar (selects update on change → consistent with search) or *visually separate* the two controls so the false-positive grouping breaks (proximity gap + distinct styling for the selects).

*Examiner push: "Couldn't a reviewer just learn the grammar difference and move on?"*

They could, and reviewers do — but that's the survival strategy that Topic 1 explicitly warns against. A reviewer learning to compensate for the false-positive grouping is paying a cognitive cost on every filter change that proper visual treatment could eliminate. Topic 6's discipline is to fix the perceptual mismatch at the source, not to expect the user to override their visual system's natural grouping.

### 5. Cards-view conflict + adjudication

**Conflict**: proximity vs similarity for caution chips inside record cards.

- Proximity says: caution chips are spatially close to the regular tag chips (same card, same row) → one group of card tags.
- Similarity says: caution chips are visually distinct (different colour, sometimes different icon) → a *different* category from regular tags.

**Adjudication**: similarity wins. The chips are *signalling different categories of information* — a caution chip means "the reviewer should know about a risk before promoting" while a regular tag means "this record has this vibe / trip-type / context". Distinguishing them is the reviewer-task; grouping them is the by-product of card layout. The resolution: maintain explicit visual separation (extra gap or a thin divider) so proximity stops fighting similarity and perceived grouping matches semantic grouping.

**General rule applied** (from Smashing, the only required source that adjudicates explicitly): when two principles conflict, the winning principle is the one that *better serves the user's task*. For caution chips the task is distinguishing risk-bearing records from neutral ones; similarity wins. For the toolbar's narrowing controls the task is treating them as one functional group; if proximity and similarity *agreed* there, both would win — they actually conflict with the interaction grammar (Q4) rather than with each other.

*Examiner push: "Doesn't 'task-driven' just push the decision to whoever defines the task?"*

Yes — and that's the right place to push it. The alternative is a fixed principle hierarchy ("similarity always wins over proximity") which would produce wrong calls in regions where the task makes proximity the decision-relevant signal. The task-driven rule means the adjudication is contestable on task grounds — "is distinguishing-cautions the actual reviewer task here?" — which is a productive argument, not a deadlock. Tasks come from Topic 3's user-need work; the Gestalt adjudication inherits the Topic 3 framing rather than reinventing it.

### 6. Canonical hierarchy + Gestalt underneath Topic 2

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   ├─ Topic 2 — UI design (the components)
   └─ Topic 6 — Gestalt (the perceptual constraint layer underneath visual treatment)
```

Topic 6 sits *underneath* Topic 2 (not alongside) because Topic 2 is *compositional* (which components exist) and Topic 6 is *perceptual* (how those components are visually grouped by the visual system). A design can satisfy Topic 2's rule sheet completely — the right components, the right states, the right modality — and still violate Gestalt, producing a "feels off" reaction that Topic 2 alone can't catch.

Concretely: Topic 2's rule sheet for v1.1 says "record card contains name, place, trust badge, chips, action buttons". Gestalt audits *how the card's internal arrangement groups those elements visually*. If the trust badge blends with surrounding metadata via similarity, the card is Topic-2-compliant but Gestalt-violating — and the violation is the false-negative grouping that hides the trust signal. Gestalt is the perceptual layer Topic 2 sits on top of.

*Examiner push: "Why not just fold Gestalt into Topic 2 as a sub-section?"*

Because the *audit-shape* differs. Topic 2's audit asks "is the right component present and specified?". Gestalt's audit asks "is the perceived grouping matching the intended grouping?". A Topic 2 component-correctness check passes a card that has all the right elements; a Gestalt audit can fail the same card if its internal arrangement groups those elements wrongly. The two audits run different tests and produce different fix lists; combining them would obscure which kind of failure a given finding represents. Keeping Topic 6 distinct (and underneath Topic 2) preserves both audit-shapes.

### 7. Scoping defence (~4–5h vs 5–7h)

The execution plan's smaller estimate reflects that Topic 6 covers a *smaller conceptual surface* than Topic 4/5. Topic 4 has multiple competing frameworks (d.school 5-stage, IBM Loop 3-activity, Brown's three-constraint triage, NN/g, plus Norman's *Useful Myth* critique) and the framework-comparison work is heavy. Topic 5 spans an ISO standard, Norman's *HCD Considered Harmful?* critique, IDEO's methods handbook, and W3C's accessibility triad — four sources at the standard / critique / methods / vocabulary level, each with substantial integration work. Topic 6 has six principles, four sources at the foundation / education / diagnosis / adjudication level, and most of the disagreement is on *emphasis* rather than on *substance*. The reading is shorter; the lab focuses on application rather than synthesis.

**Two things the smaller scope deliberately doesn't cover:**

- **Cognitive-science foundations** for *why* the visual system organises perception toward Prägnanz. This is genuinely deep territory (deferred to extension E4); covering it would expand Topic 6 to Topic 5 scale without changing the operational guidance. The constraint-framing is sufficient for the audit-shape.
- **Boundary cases** where Gestalt-driven design breaks down: very high information density (where every grouping signal compromises), motion-disabled accessibility settings (where common-fate can't be used), multi-screen multi-device contexts (where the perceptual context fragments). Topic 6 names these as known limits but doesn't develop the workarounds; that work is shared between later topics (Fitts in 7, typography in 9, colour in 10, accessibility in HCD).

*Examiner push: "If the cognitive-science foundations matter, isn't deferring them a real gap?"*

A real gap, yes — but a *named* gap, with the extension reading (E4) flagged for follow-up if the workspace ever needs to defend the *why* rather than just apply the *what*. For now, the operational guidance ("the principles are constraints; honour them or trade them off explicitly") is sufficient to run the Lab 06 audit and ship a Gestalt-compliant v1.2. If a future topic or capstone needs the deeper grounding, E4 is the entry point.

### 8. Two anticipated Lab 06 violations

**Violation 1: toolbar false-positive grouping** (deep-reading §9.2 row 1). The toolbar's search input + filter selects look like one group of narrowing controls (proximity + similarity) but have different interaction grammars (live update vs commit-on-change). Lab 06 audit will confirm by comparing the perceived grouping (one group) with the intended functional grouping (two groups by interaction grammar). Expected fix: visual separation between search and selects + unified interaction grammar across selects. Tag: v1.1.x (visual-treatment change) or v1.2 (if interaction-grammar change is needed).

**Violation 2: cards-view trust-badge false-negative grouping** (deep-reading §9.2 row 2). The trust badge inside the card metadata grid blends with surrounding metadata via similarity (similar size, similar visual weight) — hiding that the badge is the *primary* trust signal, not just another metadata field. Lab 06 audit will confirm by asking whether a naïve reviewer's eye lands on the badge first or treats it as equivalent to surrounding fields. Expected fix: visual elevation of the badge (size, contrast, position) so similarity stops grouping it with surrounding metadata. Tag: v1.1.x (likely; the rule sheet already specifies the badge as the primary trust signal — only the visual treatment needs to match).

(Four more anticipated violations are listed in deep-reading §9.2: active-filter summary bleed; sortable column header similarity; caution-chip conflict; density-compromise alignment-only grouping. Lab 06 will audit all six.)

*Examiner push: "What if Lab 06 finds the anticipated violations don't actually exist?"*

That's a valid outcome and a useful one. The deep-reading doc explicitly says the §9.2 list is "to be confirmed or refuted by Lab 06" — anticipating violations is *not* the same as having found them. If the audit refutes one, that's evidence the visual treatment is doing more work than expected, and the refutation becomes part of the audit findings (a *strength* rather than a violation). The discipline is to run the audit against every region against every relevant principle and let the cells decide, not to confirm a pre-baked list.

## How the Topic 6 answers were defended

Each Topic 6 answer cites at least one specific source (Wertheimer/Koffka/Köhler via secondary, IxDF, NN/g, Smashing — sometimes E1–E5 extensions), at least one specific v1.1 region, and connects to the canonical hierarchy (Gestalt underneath Topic 2). The examiner-push lines target the points where Topic 6's argument is most likely to slip — the "constraint vs style" framing is the most often weakened in practice (drift toward style), the task-driven adjudication is the most often misread as relativism (it's not — it's principled), and the deferred cognitive-science depth is the most often used as ammunition to dismiss the principles. The follow-ups defend the substantive position: Gestalt is constraint, adjudication is principled, the deferred depth is named not hidden.
