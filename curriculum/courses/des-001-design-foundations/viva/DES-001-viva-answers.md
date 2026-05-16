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
