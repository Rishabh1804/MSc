# Quiz 01 — Answers

Answer date: 2026-05-16. Answered without consulting the answer key first; cross-checked afterwards. Examples are drawn from the Destination Master Browser v1 (`docs/destination-master-browser-v1.0.html`).

## 1. Define UI in one or two sentences.

UI is the interface layer the user actually sees and touches — the visible controls, layout, labels, components, states, and interaction feedback that mediate the user's contact with the system. It is the mechanism that makes a task expressible; it is not, on its own, evidence that the task is well-served.

## 2. Define UX in one or two sentences.

UX is the quality of the user's whole task journey through a system — whether the user can understand the situation, complete the work, trust the result, recover from mistakes, and leave with the correct mental model. It includes UI, but also data trust, accessibility, content, and the surrounding workflow.

## 3. Explain why a visually polished dashboard can still have poor UX.

Polish is a UI surface property. UX depends on whether the user's task actually succeeds. A dashboard can have a flawless type scale, generous whitespace, and tasteful colour and still fail UX if (a) the user cannot tell which records are verified, (b) the filters cannot be reset, (c) errors are silent, or (d) the user leaves with a false confidence in the data. Polish without honest signals about data state is decoration over a usability problem.

## 4. Identify three UI elements in the Destination Master Browser and the UX tasks they support.

- **Search input** — supports the *narrow* step of the reviewer journey, letting the reviewer reduce the result set by name match.
- **Filter chips (e.g. verified, planner-ready)** — support the *narrow* and *compare* steps by constraining the result set to records that share a property the reviewer cares about.
- **Stats banner at the top of the list** — supports the *understand dataset status* step by giving an immediate read of how many records are present, verified, or flagged before any inspection starts.

## 5. Why is data credibility a UX concern in this project?

The reviewer is not browsing for entertainment — they are making downstream decisions (e.g. promoting a record to Planner). If the UI cannot distinguish verified from unverified data, the reviewer will either over-trust unverified records or waste effort double-checking verified ones. Both outcomes are UX failures even when every button works perfectly. Credibility is the property that lets the reviewer leave the system with the right level of confidence; that is squarely a UX concern.

## 6. A card uses attractive colours and badges but does not show whether a record is verified. What is the design problem?

The badge is acting as a signifier without a referent. It implies *something is being signalled* but the signal does not include the data-trust state the reviewer needs to act on. The card looks credible without being honest. The fix is not to remove the badges but to make a badge mean something operationally relevant (e.g. "verified", "planner-ready", "blocked") and to ensure the *absence* of a badge also has a defined meaning.

## 7. Which source gives the broadest definition of UX, and why does that matter?

NN/g / Don Norman gives the broadest definition: UX is "all aspects of the end-user's interaction with the company, its services, and its products" — not only the digital interface, but the surrounding system. This matters for the Destination Master Browser because it explicitly extends the UX scope past pixel-level concerns to include data quality, content, support workflow, and the reviewer's wider task — exactly where the v1 audit found the worst gaps.

## 8. Write one design-decision gate question that should be asked before adding a new browser feature.

"Which step of the reviewer journey does this feature improve, and which risk (over-trust, missed record, wasted effort, irrecoverable state) does it reduce — measured how?"

A wrong answer ("it looks better", "competitors have it") fails this question on its face.

## 9. Give one example of an anti-pattern from Topic 1.

Decorative-only badging: applying colour-coded badges to records based on a property that does not affect the reviewer's decision (e.g. arbitrary category tags), which trains the reviewer to ignore badges in general — including the badges that *do* matter (verified, blocked). Once badge attention is consumed by decorative chrome, the genuine trust signals become invisible.

## 10. Explain how accessibility relates to UX.

Accessibility is a precondition of UX, not a separate concern. If a reviewer cannot read the type, cannot operate the filter chips by keyboard, cannot perceive the verified/unverified distinction without colour, or cannot use the system with assistive technology, the UX has failed for that reviewer regardless of how well the system serves anyone else. The W3C framing makes this concrete: usability, accessibility, and inclusion are the three faces of the same property — a system that works for the people who need to use it.

## Self-mark vs answer key

Cross-checked against `quiz-01-ui-vs-ux-answer-key.md` is not in the repo (Topic 1 had no answer key written — only the quiz file). The answers above were written from the lecture, reading pack, and Lab 01 results without an internal key. Topic 2's quiz does include both quiz and answer-key files (`quiz-02-what-is-ui-design.md` and `-answer-key.md`) so future self-marking has a reference.
