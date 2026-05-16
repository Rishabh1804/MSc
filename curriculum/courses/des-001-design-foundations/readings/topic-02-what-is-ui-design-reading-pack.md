# Reading Pack — Topic 02 What is UI design

## Required readings

| Source | Role |
|---|---|
| Material Design — Foundations & Components | Primary component-system framing; how a major design system decomposes UI |
| Apple Human Interface Guidelines — Components | Component vocabulary and behaviour rules from a platform-led perspective |
| IBM Carbon — Component patterns | Enterprise-grade component patterns and usage rules |
| GOV.UK Design System — Components | Public-sector, accessibility-first component patterns with usage criteria |
| Don Norman — *The Design of Everyday Things*, chapter on affordances and signifiers | The conceptual foundation for component clarity |

## Extension readings

| Source | Role |
|---|---|
| Schoger & Wathan — *Refactoring UI* | Visual treatment as a sub-skill inside UI design |
| Nielsen Norman Group — Card design, table design, modal design articles | Pattern-specific deep dives |
| Brad Frost — *Atomic Design* | Hierarchical decomposition: atoms, molecules, organisms |
| Smashing Magazine — Pattern selection essays | When-to-use guidance for cards vs tables vs lists |
| WCAG 2.2 / W3C ARIA Authoring Practices — interactive component patterns | Accessibility patterns for buttons, dialogs, menus, tabs, listbox, etc. |

## Reading questions

1. How does each source define a "component"? Where do they disagree?
2. Which source gives the strongest framing for **when** to use a card versus a table?
3. Which sources treat **states** (default / hover / focus / active / disabled / loading / empty / error / success) as first-class? Which treat them as an afterthought?
4. How does each source handle the gap between affordance, signifier, and feedback?
5. Which source is most useful for choosing a container (card / table / list / drawer / modal) for a data-review task?
6. What does each source omit or under-emphasise — especially around data-trust and uncertainty signalling?
7. Which patterns from the extension readings translate directly to the Destination Master Browser, and which do not?

## Extraction target

The reading should produce:

- summary of UI design as a discipline (one paragraph)
- element-vocabulary table (controls, containers, navigation, data display, feedback, editorial) with examples and the reviewer task each supports
- state-coverage table for the browser's current components
- container-selection rule sheet (card vs table vs list vs drawer vs modal) with explicit criteria
- affordance / signifier / feedback audit of v1 — three columns, one row per interactive element
- source comparison: where the five required sources agree, where they differ
- CodeMike interpretation: how the discipline translates to Destination Master Browser decisions
- anti-patterns specific to data-review tools (e.g. decorative badges, missing empty states, modal-when-drawer-was-correct)
- implementation implications for Destination Master Browser v1.1
- further reading and exercise tasks

## Linked extension

```text
design/foundations/ui-design-component-rules.md
```

This file will hold the consolidated container-selection and component-state rules produced by Lab 02. It is the deliverable that Topic 3 (UX design) will reference, and that the Browser v1.1 redesign will follow.
