# Quiz 06 — Answers

Answer date: 2026-05-17. Written from the lecture, the four required Topic 6 sources, and the deep-reading doc at `design/foundations/topic-06-gestalt.md`, then cross-checked against `quiz-06-gestalt-principles-answer-key.md`. Examples are drawn from the Destination Master Browser v1.1.

## 1. Definition + non-definition

Gestalt principles are **perceptual constraints on how the human visual system groups visual elements** — empirical facts about perception established by the Berlin-school Gestalt psychologists (Wertheimer 1912; Koffka 1935; Köhler 1929) and validated repeatedly since. They are **not** aesthetic rules ("use whitespace generously"), style preferences, or designer conventions. The human will perceive grouping whether the designer intended it or not; the discipline's only job is to make perceived grouping match intended grouping.

The framing matters because the *style* reading lets designers override the principles on taste; the *constraint* reading forces every visual choice to defend itself against what the visual system *will* do. For the Destination Master Browser, this distinguishes "the cards look balanced" (taste) from "the cards' common-region boundary correctly groups name + place + trust badge + chips, and the trust badge's similarity to surrounding metadata is the violation we need to fix" (constraint).

## 2. Prägnanz + corollary

**Prägnanz** ("good figure" / "good form") says the visual system organises perception toward the **simplest, most stable, most symmetric** interpretation available. The system runs a least-cost interpretation continuously; the cheapest interpretation wins. Every specific Gestalt principle is a corollary because each one names a *specific way* the visual system simplifies:

- *Proximity* simplifies spatial relationships by grouping nearby elements (cheaper than perceiving each element as isolated)
- *Similarity* simplifies categorical relationships (visually-alike = one category is cheaper than tracking N categories)
- *Continuity* simplifies path-following (a single smooth aligned line is cheaper than discrete colinear segments)
- *Closure* simplifies shape recognition (a recognised closed form is cheaper than tracking arc-segments)
- *Common region* simplifies grouping (a bounded area is cheaper than tracking which elements belong together)
- *Common fate* simplifies relationship inference (co-moving = related is cheaper than tracking each motion separately)

Each principle is a consequence of "perceive the simplest stable form" applied to a specific kind of stimulus. Prägnanz is the *why*; the six principles are the *how*.

## 3. Six core principles + UI consequence

| # | Principle | UI consequence |
|---:|---|---|
| 1 | Proximity | Spacing is meaning — whitespace separates, tight space groups |
| 2 | Similarity | Visual similarity (colour, shape, size, font) implies functional similarity |
| 3 | Continuity | Alignment is structure — aligned elements feel like a continuous group |
| 4 | Closure | The eye completes partial shapes; bordered frames are perceived as wholes even with one open side |
| 5 | Common region | Bounded areas (cards, panels) create perceived groups regardless of element similarity |
| 6 | Common fate | Motion is grouping — elements moving together are perceived as related |

Browser-specific one-liners: proximity = toolbar's six controls read as "narrowing controls" group; similarity = trust badge at four depths reads as "one signal in multiple places"; continuity = table columns hold *because* values align vertically; closure = drawer overlay reads as a container despite no explicit top border; common region = each record card binds name + place + badge + chips into one unit; common fate = result-count flash animation co-varying with filter change implies they're related.

## 4. Gestalt violation + v1.1 candidate

A **Gestalt violation** is the gap between *intended* and *perceived* grouping. Three sub-types: **false-positive grouping** (visual arrangement implies a relationship that doesn't exist), **false-negative grouping** (visual arrangement hides a relationship that does), and **unresolved principle conflict** (two principles pull in different directions and the design leaves it to the user to figure out).

**v1.1 candidate (false-positive)**: the toolbar's search input and filter selects sit close together with similar input-styling, so proximity + similarity say "same group of narrowing controls". But the interaction grammar differs — the search updates *live as you type*, the selects update *on selection change*. A reviewer trained on the search expects live update from a select and is surprised when nothing happens until commit. Two principles say "same group"; the actual behaviour says "different grammar". That is a false-positive grouping violation that Lab 06 should confirm and surface for v1.1.x.

(Other valid v1.1 candidates: the trust badge inside the card metadata grid blends with surrounding metadata via similarity, hiding that it is the *primary* trust signal — false-negative; the active-filter summary chip row may bleed into the toolbar without explicit separation — proximity / common region; sortable column headers may not signal interactivity because they look similar to non-sortable headers — similarity.)

## 5. Conflicting principles in v1.1 cards view

**Proximity** says: the vibe / trip / context / caution chips inside a single card are all spatially close → they're one group of card tags. **Similarity** says: caution chips are visually distinct (different colour / icon) → they're a *different* group from the regular tags.

**Adjudication**: similarity wins for the *categorical* signal. Caution chips should not be perceived as part of the regular tag group — the difference is semantic, not visual decoration. Proximity loses on this region because the trade-off is between "they're in the same card" (true but coarse) and "they signal a different category of information" (true and reviewer-relevant). Resolution: maintain visual separation (extra gap or a thin divider) so proximity stops fighting similarity — the perceived grouping then matches the semantic grouping rather than the spatial co-location.

The general rule (from Smashing, the only required source that adjudicates explicitly): when two principles conflict, the winning principle is the one that *better serves the user's task*. For caution chips, distinguishing them *is* the task; proximity within the card is the by-product of card layout. For navigation labels in a top bar, grouping them is the task; similarity is the by-product. The principles don't have a fixed hierarchy; the task picks the winner.

## 6. Canonical hierarchy

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   ├─ Topic 2 — UI design (the components)
   └─ Topic 6 — Gestalt (the perceptual constraint layer underneath visual treatment)
```

Gestalt sits *underneath* Topic 2 — Topic 2 specifies *which components* appear (cards, drawer, toolbar, modal); Gestalt audits *how those components will be perceived together* by the visual system. A design can satisfy Topic 2 (correct components per the rule sheet) and Topic 3 (correct acceptance criteria) and *still* violate Gestalt (wrong perceived grouping) — and that violation produces a "feels off" reaction even when the design checks every component-and-criterion box. Topic 6 is the perceptual audit that catches what Topics 2 and 3 alone don't.

## 7. "Aesthetic rules of thumb" critique

**Defend the critique partially.** Treating Gestalt principles as aesthetic rules — "use whitespace generously", "align things" — is a real and recurring failure mode. It strips the principles of their perceptual-constraint authority and reduces them to taste-level recommendations a designer can override on intuition. When that happens, designers lose the ability to *defend* their visual choices: "I used whitespace because it's good design" is unfalsifiable.

**But the critique doesn't undermine the discipline.** The corrective is to treat Gestalt principles as *what the visual system will do* — facts that the design must accommodate regardless of style. A designer can still make stylistic choices, but those choices have to *honour* the perceptual constraints or *explicitly trade them off* with a named compensating signal.

**Verdict: sharpens.** The critique tells the discipline what to defend against — Gestalt becoming style. Sources that ignore the critique (some IxDF and NN/g examples) end up with vague "use Gestalt" advice; sources that engage it (Smashing best, Wertheimer/Koffka/Köhler by construction) end up with specific, defensible per-region recommendations. For CodeMike: the discipline is *name the principle, name the trade-off if any, defend the choice* — exactly the gate-shape the quiz Q10 captures.

## 8. Topic 6 lighter than Topic 4/5

The execution plan's ~4–5h estimate reflects that Topic 6 covers a *smaller conceptual surface* — six principles, with relatively settled experimental science behind them — compared to Topic 4 (design thinking has multiple competing frameworks: d.school 5-stage + IBM Loop + Brown's three-constraint + NN/g + Norman's *Useful Myth* critique) or Topic 5 (HCD spans an ISO standard, Norman's *HCD Considered Harmful?* critique, IDEO's operational handbook, and W3C's accessibility triad). Gestalt principles are *fewer*, *more empirically grounded*, and *more agreed-on*. The reading is shorter; the lab focuses on application rather than synthesis.

**What the smaller scope doesn't cover**: the cognitive-science foundations for *why* the visual system works this way (deferred to extension reading E4); the boundary cases where Gestalt-driven design breaks down (very high information density, motion-disabled accessibility settings, multi-screen contexts); and the relationship to other perceptual constraints (Fitts' law in Topic 7, typography in Topic 9, colour in Topic 10). Topic 6 introduces the six principles + audit-shape; subsequent topics deepen specific perceptual concerns.

## 9. Gestalt anti-pattern for data-review tools

**Silent density collapse**. Data-review tools pack a lot of information per screen — many columns, many records, many filters, many badges. Whitespace (the proximity-based grouping signal) is expensive in screen real estate. The temptation is to *silently* compress whitespace to fit more information, which collapses Gestalt groupings: filters bleed into search; cards bleed into stats; trust badges blur with metadata. The user can still see everything, but the *grouping signal* degrades and the reviewer has to re-derive groupings every time their eye moves.

The discipline (Smashing's adjudication): when density forces a Gestalt compromise, *name the compromise explicitly* and use a *different* grouping signal to compensate — a thin divider in lieu of generous whitespace; a background tint in lieu of explicit cards; alignment continuity where common-region is impractical. The silent collapse is the failure mode; explicit grouping-signal substitution is acceptable.

Other valid anti-patterns: decorative motion (using common-fate for visual polish rather than meaningful grouping); too many similarity signals (using colour/shape/size for too many categories at once, defeating the categorical signal); accidental mis-alignment (violating continuity invisibly — the eye notices but the designer doesn't); cards-inside-cards (over-using common-region until the nested boundaries blur the perceptual hierarchy).

## 10. Design-decision gate for visual-treatment changes

> *"For this visual treatment change, name (a) the Gestalt principle(s) the change satisfies AND (b) the Gestalt principle(s) the change violates. If there is a violation, name (c) the compensating signal that substitutes for the violated principle AND (d) the user task served by accepting the trade-off. If you can't fill all four cells, the change is being adjusted by taste, not by perceptual constraint — return it for redesign."*

A wrong answer is immediately visible: a change that names no principle ("it looks better"); a change that names a satisfied principle but ignores violated ones (selective citation); a violation without a compensating signal (silent collapse); a violation without a named user task (taste masquerading as discipline). A right answer cites specific principles, names trade-offs, and connects the resolution to a specific reviewer task.

The gate's value is that it catches *silent* Gestalt drift — the kind that accumulates over many small "looks better" tweaks until the visual hierarchy is broken. Each individual tweak passes a "looks fine" check; the cumulative effect is a hierarchy that no longer matches the intended grouping. The four-cell gate makes the drift visible per-change, which is the only way to prevent it without re-auditing every region every release.

## Self-mark

Cross-checked against `quiz-06-gestalt-principles-answer-key.md`. All ten answers are grounded in the deep-reading doc and at least one Topic 6 source. The answers extend the key on Q1 (added the constraint-vs-style operational distinction with a v1.1-specific contrast), Q2 (worked the corollary mapping for all six principles explicitly), Q4 (added three alternative valid candidates), Q9 (named four alternative anti-patterns), and Q10 (expanded to a four-cell gate matching the violation taxonomy from deep-reading §6). No corrections needed; the answers and key are aligned.
