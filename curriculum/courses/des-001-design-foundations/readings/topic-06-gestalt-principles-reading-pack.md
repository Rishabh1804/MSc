# Reading Pack — Topic 06 Gestalt principles

## Required readings

| Source | Role |
|---|---|
| **Wertheimer / Koffka / Köhler** — original Gestalt papers, via authoritative secondary | Primary historical source. Max Wertheimer's 1912 paper on apparent motion (the founding moment); Kurt Koffka's 1935 *Principles of Gestalt Psychology* and Wolfgang Köhler's 1929 *Gestalt Psychology* (the consolidating textbooks). Read via an authoritative secondary source (e.g., the Stanford Encyclopedia of Philosophy entry on Gestalt psychology, or chapters in Goldstein's *Cognitive Psychology* textbook). The original papers establish *Prägnanz* and the foundational principles. |
| **Interaction Design Foundation** — Gestalt principles for interaction designers | Authority / applied source. IxDF's Gestalt-principles articles operationalise the original psychology into specific UI guidance with worked examples. The discipline's standard educational treatment. |
| **Nielsen Norman Group** — Gestalt principles in UI design (multiple articles) | High-authority applied source. NN/g's series on Gestalt principles in interface design provides specific named violations + their fixes with screenshots from real products. The most-cited treatment for working designers. |
| **Smashing Magazine** — Gestalt principles in interface design (worked-example essays) | Cross-check / applied source. Smashing's essays provide the *practitioner's* view: where Gestalt principles meet real product constraints (content density, accessibility, multi-screen layouts) and how to adjudicate. |

## Extension readings

| Source | Role |
|---|---|
| Andy Rutledge — *Design and Gestalt theory* | A practitioner's deep treatment with strong opinions; useful counterweight to NN/g's measured framing |
| Refactoring UI (Schoger & Wathan, revisited from Topic 2) | Operationalisation of Gestalt + visual hierarchy into per-component decisions; bridges Topic 6 with Topic 2's component rule sheet |
| Tufte — *The Visual Display of Quantitative Information* | Gestalt principles applied to information design (charts, tables, dashboards) — directly relevant to the table view in the Destination Master Browser |
| Bartoshuk / Cognitive Psychology textbook chapter on perception | The cognitive-science foundation for *why* Gestalt principles work the way they do — useful for understanding when they break down |
| Steve Krug — *Don't Make Me Think* | Practitioner essays on visual hierarchy + scannability that lean heavily on Gestalt without naming it; useful for understanding the *internalised* application of the principles |

## Reading questions

1. The Gestalt psychologists worked on apparent motion and still-image experiments in the early 20th century. What specific findings from that work still hold up under modern cognitive science, and which have been refined or challenged?
2. The *Prägnanz* principle says the visual system prefers the simplest stable interpretation. Where in v1.1 is the simplest interpretation also the correct one? Where might the simplest interpretation mislead the reviewer?
3. The six core principles (proximity, similarity, continuity, closure, common region, common fate) can conflict. Find one v1.1 region where two principles pull in different directions; how does each source say to adjudicate?
4. Each source has a different treatment of the principles' *strength order* — which one wins when they conflict. State each source's position and identify the source-disagreement.
5. The critique that Gestalt principles can degrade into aesthetic rules of thumb: which sources engage it explicitly? Which leave it implicit?
6. Each source has different examples (consumer products / dashboards / forms / marketing pages). Map each source's example-domain to whether it transfers to the Destination Master Browser's QA-review-tool category.
7. Where do the principles *break down*? Each source has a position on cases where Gestalt-driven design doesn't help (very high density, very low contrast, motion-disabled accessibility settings). Compile the breakdown cases.
8. What does each source omit or under-emphasise that the others surface? Compile a per-source omission list.

## Extraction target

The reading should produce:

- topic definition (with perceptual-constraint framing, not aesthetic-rule framing)
- explanation of *Prägnanz* and how every specific principle is a corollary
- table of the six core principles with UI consequence and one browser-specific example each
- *Gestalt violation* taxonomy (false-positive grouping / false-negative grouping / conflict between principles)
- source-by-source notes (what each teaches / what it omits / strongest takeaway)
- structured source comparison (agreement table + difference-by-emphasis table + per-source omissions)
- the "perceptual constraint vs aesthetic rule of thumb" critique + how each source positions itself
- CodeMike interpretation — Gestalt as the perceptual constraint layer underneath Topic 2's components
- application to the Destination Master Browser: per-screen-region audit plan for Lab 06
- anti-patterns specific to Gestalt in data-review tools (where information density conflicts with Gestalt grouping)
- implementation implications for v1.1.x / v1.2
- further reading + applied exercises
- checklist updates for the master-browser checklist (Topic 6 gates)

## Linked extension

```text
design/foundations/topic-06-gestalt-audit.md
```

The Lab 06 output: a Gestalt audit of v1.1 against the six principles, focused on the screen regions where grouping signals carry the most weight (cards, table, toolbar, trust banner + stats, drawer). The audit produces a per-region violation list and a v1.1.x / v1.2 fix list, scoped against existing component rules and acceptance criteria.
