# DES-001 Topic 1 — UI vs UX Further Reading Ladder

Status: extension reading added  
Primary assignment artifact: `docs/design-foundations.html`  
Related checklist: `design/checklists/master-browser-design-checklist.md`  
Purpose: strengthen Topic 1 beyond the minimum source requirement by adding a sequenced reading ladder, applied exercises, and browser-specific audit prompts.

## 1. Why this extra reading exists

The minimum Topic 1 digest already distinguishes UI from UX and maps that distinction to the destination master browser. To make the assignment stronger, CodeMike should now read beyond the definition-level sources and learn how UI/UX differences are evaluated in practice.

This extension adds four extra dimensions:

1. usability heuristics for evaluating the interface layer
2. UX quality facets for judging the wider experience
3. user-needs discipline for avoiding solution-first design
4. accessibility/usability/inclusion framing for making the review tool usable by more people and more situations

## 2. Further Reading Ladder

Read these in order. The order deliberately moves from interface evaluation to broader UX judgement, then to user-needs discipline, then to accessibility and inclusion.

| Order | Reading | Type | Why it matters | CodeMike output |
|---:|---|---|---|---|
| 1 | Nielsen Norman Group — 10 Usability Heuristics for User Interface Design | high-authority / applied | Converts the UI side of UI vs UX into a practical evaluation checklist: status visibility, real-world language, user control, consistency, error prevention, recognition, efficiency, minimalist design, error recovery, and help. | Run a heuristic pass on the current destination browser and mark each violation as low / medium / high severity. |
| 2 | Peter Morville — UX Honeycomb | conceptual / cross-check | Expands UX beyond usability into useful, usable, desirable, findable, accessible, credible, and valuable. This helps prevent a narrow “pretty and usable” definition of UX. | Score the browser against each honeycomb facet, especially findable, credible, accessible, and useful. |
| 3 | GOV.UK Service Manual — Learning about users and their needs | practical / public-sector | Forces user-needs-first thinking: start with what users are trying to do, validate assumptions, and avoid building features because the team wants them. | Rewrite browser needs as “As a reviewer, I need to…, so that…” statements. |
| 4 | GOV.UK Content Design — User needs | applied content design | Helps separate genuine user needs from solution-shaped needs. This is important before adding UI features such as chips, drawers, filters, or toggles. | Check whether each proposed browser feature exists because of a verified reviewer need, not because it sounds like a good UI feature. |
| 5 | W3C WAI — Accessibility, Usability, and Inclusion | standards / authority | Clarifies the overlap and difference between accessibility, usability, and inclusion. This raises the assignment from visual design into responsible web-interface design. | Add accessibility acceptance checks for controls, text labels, keyboard use, predictable interaction, and non-colour-only status. |
| 6 | W3C WAI — Accessibility Principles | standards / implementation bridge | Connects accessibility to perceivable, operable, understandable, and robust interface design. Useful before implementing custom controls or drawers. | Verify that the browser remains usable with semantic HTML, keyboard navigation, clear labels, readable text, and robust component roles. |

## 3. What each reading adds to Topic 1

### 3.1 Nielsen Norman Group — usability heuristics

Topic 1 already says UI is the visible/interactive layer. Nielsen's heuristics give CodeMike a way to inspect that layer systematically.

Useful questions for the destination browser:

- Is dataset loading / filtering status visible?
- Are labels written in reviewer language rather than implementation language?
- Can the user recover from over-filtering or empty results?
- Are filters, chips, warnings, status badges, and cards consistent?
- Are errors prevented before the user over-trusts unverified records?
- Can the user recognise source and Planner status without memorising definitions?

Browser implication:

```text
UI quality should be evaluated through heuristic violations, not personal taste.
```

### 3.2 UX Honeycomb

The UX honeycomb is useful because it prevents CodeMike from reducing UX to ease-of-use only.

For this browser:

| Honeycomb facet | Browser interpretation |
|---|---|
| Useful | Helps the reviewer inspect destination master records. |
| Usable | Search, filter, inspect, reset, sort, and switch view are easy to perform. |
| Desirable | Visual design supports confidence without decorative excess. |
| Findable | The user can quickly locate destination records and status information. |
| Accessible | Controls, labels, contrast, keyboard path, and mobile layout support broader access. |
| Credible | The interface is honest about unverified and not-Planner-ready data. |
| Valuable | The browser reduces QA friction and supports future enrichment work. |

Browser implication:

```text
A browser can be usable but not credible if it hides uncertainty. A browser can be attractive but not useful if it does not improve review work.
```

### 3.3 GOV.UK user-needs discipline

GOV.UK's guidance is useful because it warns against building around assumed needs or solution-shaped needs.

For CodeMike, this means avoiding statements like:

```text
As a reviewer, I need a drawer because drawers are a modern UI pattern.
```

Better:

```text
As a reviewer, I need to inspect the full source, verification, and notes for one destination without losing my filtered result set, so that I can judge whether the record needs enrichment.
```

Browser implication:

```text
Features must trace back to reviewer needs, not component fashion.
```

### 3.4 W3C accessibility, usability, and inclusion

W3C is important because it shows that accessibility, usability, and inclusion overlap but are not identical. A UI can be visually polished and still fail users if status is colour-only, keyboard navigation breaks, labels are ambiguous, or custom controls lack semantic meaning.

Browser implication:

```text
The destination browser should prefer native HTML controls unless a custom component can preserve keyboard, label, role, and state behaviour.
```

## 4. Extra applied exercises for Topic 1

### Exercise A — UI inventory

List every visible UI element in `docs/destination-master-browser-v1.0.html`:

- header badges
- title/subtitle
- warning notice
- search input
- source/region/scale/status filters
- stats cards
- side snapshot
- destination cards
- metadata blocks
- chips
- empty/loading/error states

For each one, answer:

```text
What UX task does this UI element support?
What happens if it is removed?
What risk does it reduce?
```

### Exercise B — UX journey map

Map the reviewer journey:

```text
1. Understand dataset status
2. Search or filter records
3. Compare visible records
4. Inspect one record deeply
5. Identify uncertainty or enrichment need
6. Reset / change direction
7. Leave with correct trust level
```

For each step, identify the UI elements that support it.

### Exercise C — Heuristic mini-audit

Use Nielsen's heuristics to audit the current browser:

| Heuristic | Browser audit prompt |
|---|---|
| Visibility of system status | Does the browser show loading, empty, filtered count, and data-trust status? |
| Match with real world | Are terms like `planner_use_status` translated into reviewer-readable labels? |
| User control and freedom | Can the user reset filters and close detail views easily? |
| Consistency and standards | Do chips, badges, filters, and statuses behave consistently? |
| Error prevention | Does the browser prevent over-trust in unverified rows? |
| Recognition rather than recall | Are source/status meanings visible instead of requiring memory? |
| Flexibility and efficiency | Do power users get sort, table mode, and quick filters? |
| Aesthetic and minimalist design | Does the page avoid decorative noise and field dumping? |
| Error recovery | Are empty/error states actionable? |
| Help and documentation | Does the browser explain what the dataset can and cannot prove? |

### Exercise D — UX Honeycomb score

Score the current browser from 1–5 for:

- useful
- usable
- desirable
- findable
- accessible
- credible
- valuable

A score below 3 requires a design note before v1.1 implementation.

## 5. Checklist additions suggested by this extension

Add these to the next checklist revision if not already covered:

- Every UI element must map to a UX task.
- Every UX task must map to one or more visible UI supports.
- Feature requests must be written as user needs before implementation.
- Heuristic violations should be recorded with severity.
- Credibility must be assessed separately from visual appeal.
- Accessibility must be checked as part of UX, not postponed as a final polish task.
- Prefer native semantic HTML controls unless custom controls preserve keyboard, label, role, and state semantics.

## 6. Assignment-quality note

This extension should be referenced in the final DES-001 submission as evidence of extra effort beyond minimum source comparison. It shows that Topic 1 was not treated as a simple definition exercise, but as a bridge between:

```text
UI/UX concepts → evaluation frameworks → user-needs discipline → accessibility → browser audit criteria
```

That bridge is exactly what makes the assignment more likely to score well under:

- source comparison and bias awareness
- application to CodeMike/browser context
- checklist/actionability
- academic discipline/versioning
