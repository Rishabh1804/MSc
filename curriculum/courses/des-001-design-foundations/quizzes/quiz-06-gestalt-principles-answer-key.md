# Quiz 06 — Answer Key

Guideline answers. A response that says the same thing differently — particularly grounded in the Destination Master Browser — scores equally.

## 1. Definition + non-definition

Gestalt principles are **perceptual constraints on how the human visual system groups visual elements** — facts about perception that any visual interface must accommodate. They were established experimentally by the Berlin-school Gestalt psychologists (Wertheimer 1912; Koffka 1935; Köhler 1929) and validated repeatedly since. They are **not** aesthetic rules of thumb, style preferences, or designer conventions — the human will perceive grouping whether the designer intended it or not; the discipline's job is to make perceived grouping match intended grouping.

## 2. Prägnanz + corollary

**Prägnanz** ("good figure" / "good form") says: the visual system organises perception toward the **simplest, most stable, most symmetric** interpretation available. Every specific Gestalt principle is a corollary because each one names a *specific way* the visual system simplifies: proximity simplifies *spatial relationships* by grouping nearby elements; similarity simplifies *categorical relationships* by grouping visually-alike elements; continuity simplifies *path-following* by preferring smooth aligned lines; etc. Each principle is a consequence of "perceive the simplest stable form" applied to a specific kind of stimulus.

## 3. Six core principles + UI consequence

| # | Principle | UI consequence |
|---:|---|---|
| 1 | Proximity | Spacing is meaning — whitespace separates; tight space groups |
| 2 | Similarity | Visual similarity (colour, shape, size, font) implies functional similarity |
| 3 | Continuity | Alignment is structure — aligned elements feel like a continuous group |
| 4 | Closure | The eye completes partial shapes; bordered frames are perceived as wholes |
| 5 | Common region | Bounded areas (cards, panels) create perceived groups |
| 6 | Common fate | Motion is grouping — elements moving together are perceived as related |

## 4. Gestalt violation + v1.1 candidate

A **Gestalt violation** is the gap between perceived and intended grouping: the visual arrangement implies a relationship that doesn't exist (false positive) or hides a relationship that does (false negative).

**v1.1 candidate**: the toolbar's filter dropdowns and the search input may be perceived as a *single group of narrowing controls* (proximity + similar input-style) when they actually have **different interaction patterns** (the search updates live as you type; the selects update on selection change). The proximity says "same kind of thing"; the actual behaviour is "different interaction grammar". A reviewer trained on one will be surprised by the other.

(Other valid candidates: the trust banner + page header sometimes blend into one visual unit when scrolled, hiding that the banner is a *separate, persistent* element; the table sort icons might be perceived as decorative rather than interactive because of similarity to the column header text.)

## 5. Conflicting principles in v1.1 cards view

**Proximity** says: vibe/trip/context/caution chips are close together within a card → same group. **Similarity** says: caution chips are visually distinct (different colour) → different group.

**Adjudication**: similarity wins for *categorical* signal (caution chips should NOT be perceived as part of the regular tag group — the difference is semantic). Proximity loses because the trade-off is between "they're in the same card" (true but coarse) and "they signal different things" (true and reviewer-relevant). The resolution: maintain visual separation (slight extra gap or a visual divider) so proximity matches semantic grouping, not just spatial co-location.

The general rule: when proximity and similarity conflict, prefer the principle that better serves the *user's task*. For caution chips, distinguishing them is the task; for navigation labels in a top bar, grouping them is the task. The principles don't have a fixed hierarchy; the task picks the winner.

## 6. Canonical hierarchy

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   ├─ Topic 2 — UI design (the components)
   └─ Topic 6 — Gestalt (the perceptual constraint layer underneath visual treatment)
```

Gestalt sits *underneath* Topic 2 — Topic 2 specifies *which components* appear; Gestalt audits *how those components will be perceived together* by the human visual system. A design can satisfy Topic 2 (correct components) and still violate Gestalt (wrong visual grouping).

## 7. "Aesthetic rules of thumb" critique

**Defend the critique partially.** Treating Gestalt principles as aesthetic rules ("use whitespace generously") is a real failure mode — it strips the principles of their perceptual-constraint authority and reduces them to style advice that a designer can override on taste. When that happens, designers lose the ability to *defend* their visual choices: "I used whitespace because it's good design" is unfalsifiable.

**But the critique doesn't undermine the discipline.** The corrective is to treat Gestalt principles as *what the human will perceive* — facts about perception that the design must accommodate, regardless of style. A designer can still make stylistic choices, but those choices have to honour the perceptual constraints or explicitly trade them off. The discipline is: name the principle, name the trade-off if any, defend the choice.

**Verdict: sharpens.** The critique is useful because it tells the discipline what to defend against — Gestalt becoming style. Sources that ignore the critique end up with vague "use Gestalt" advice; sources that engage it (NN/g + Smashing best) end up with specific, defensible per-region recommendations.

## 8. Topic 6 lighter than Topic 4/5

The execution plan's ~4–5h estimate reflects that Topic 6 covers a *smaller* conceptual surface — six principles, with relatively settled science behind them — compared to Topic 4 (design thinking has competing frameworks: d.school + IBM + Brown + NN/g, plus the Norman critique) or Topic 5 (HCD has standards + critique + methods + triad spanning multiple disciplines). Gestalt principles are *fewer* and *more agreed-on*; the reading is shorter and the lab focuses on application rather than synthesis.

**What the smaller scope doesn't cover**: the cognitive-science foundations (why the visual system works this way), the boundary cases (where Gestalt principles break down — very high density, motion-disabled accessibility settings, multi-screen multi-tasking), and the relationship to other perceptual constraints (Fitts' law in Topic 7, typography in Topic 9, colour in Topic 10). Topic 6 introduces the six principles; subsequent topics deepen specific perceptual concerns.

## 9. Gestalt anti-pattern for data-review tools

**Density vs grouping conflict**. Data-review tools pack a lot of information per screen — many columns, many records, many filters, many badges. Whitespace (the proximity-based grouping signal) is expensive in screen real estate. The temptation is to *compress* whitespace to fit more information, which collapses Gestalt groupings: filters bleed into search; cards bleed into stats; trust badges blur with metadata. The user can still see everything, but the *grouping signal* degrades.

The discipline: when density forces a Gestalt compromise, name the compromise explicitly and use a *different* grouping signal to compensate (e.g., a thin divider in lieu of generous whitespace; a background tint in lieu of explicit cards). Silently collapsing whitespace is the failure mode; explicit grouping-signal substitution is acceptable.

Other valid anti-patterns:
- Using motion (common fate) for *decorative* animation rather than *meaningful* grouping
- Using colour (similarity) for too many categories at once, defeating the categorical signal
- Mis-aligning elements (violating continuity) accidentally — the eye notices but the designer doesn't
- Treating common region (bordered cards) as the *only* grouping signal, then nesting cards inside cards and losing the perceptual hierarchy

## 10. Design-decision gate for visual-treatment changes

> *"For this visual treatment change, name the Gestalt principle(s) the change satisfies AND the Gestalt principle(s) the change violates. If there's a violation, explain the trade-off — what other principle compensates for the violation, what user task is served by accepting it? If you can't name either side, the visual treatment is being adjusted by taste, not by perceptual constraint."*

A wrong answer is immediately visible: a change that names no principle ("it looks better"); a change that names a satisfied principle but ignores violated ones; a violation without compensation. A right answer cites specific principles, names trade-offs, and connects the resolution to a specific user task. The gate catches *silent* Gestalt drift — the kind that accumulates over many small "looks better" tweaks until the visual hierarchy is broken.
