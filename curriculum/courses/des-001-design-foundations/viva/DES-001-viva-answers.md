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
