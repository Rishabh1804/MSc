# FAILURE_LOG.md — CodeMike Failure Log

Failure is part of postgraduate learning. CodeMike should record mistakes, weak assumptions, poor models, misleading charts, broken implementations, and failed transfers.

## Purpose

The failure log turns mistakes into reusable judgement.

## Failure Entry Template

```md
## Failure: <title>

Date:
Context:
What went wrong:
Why it mattered:
Lesson:
Reusable warning:
Related anti-pattern:
Next action:
```

## Initial Warnings

- Do not report model accuracy alone without checking class balance and error distribution.
- Do not build dashboards before defining the decision they support.
- Do not optimise before writing constraints plainly.
- Do not use real sensitive data without classification and approval.
- Do not treat an AI-generated answer as evidence without verification.

## Failure Register

## Failure: Unicode glyphs in CSS `content` shipped without mobile font-fallback verification

Date: 2026-05-18 (caught) / introduced 2026-05-18 by PR #20 (Lab 06 v1.1.x polish)

Context: Lab 06 Fix #4 added a sort-affordance indicator to sortable column headers in the Destination Master Browser via `table.records thead th[data-sort][aria-sort="none"]::after { content: " ↕" }`. The ↕ character (Unicode U+2195) renders correctly on macOS / Linux desktop fonts. The fix shipped to production via PRs #20 + #22.

What went wrong: On Android Chrome (and likely other mobile font stacks) the U+2195 character does not have glyph coverage in the device's default font fallback chain. The character rendered as a colon-like substitute, breaking the interactivity signal exactly as designed. The user caught this by opening the deployed build on their phone; the introspective Lab 06 audit, the Lyra + Aurelius PR #20 reviews, and the 19-gate Playwright walkthrough (all at 1440×900 desktop resolution) had all missed it.

Why it mattered: A CSS-content character is the worst kind of font-dependency to test for — it doesn't show up in regression tests, doesn't fail loudly, and depends on the device + browser font fallback chain. A reviewer who couldn't see the sort indicator would just not know columns were sortable — a silent feature regression. This is the exact "silent collapse" anti-pattern Topic 6's deep-reading doc §10 #1 warns against (substitution without explicit verification).

Lesson: Unicode glyphs in the 2190–21FF block (arrows) have inconsistent mobile font coverage. The geometric-shapes block 25B0–25FF (▲▼◆■) has much better cross-platform coverage. *More importantly*: any CSS `content` that depends on a Unicode character should either (a) be replaced with inline SVG, OR (b) be tested on at least one mobile + one desktop device before merging. The introspective audit-shape doesn't catch this because it grades the *design intent*, not the *rendering across environments*.

Reusable warning: **CSS `content: "<glyph>"` is not portable.** Use inline SVG via `background-image: url("data:image/svg+xml;...")` for any indicator that must render identically across all devices. The pattern is in `docs/destination-master-browser.html` at the v1.2.1 fix.

Related anti-pattern: Lab 06 §30 anti-pattern 1 (silent density collapse) at the typographic layer; Lab 05 F-W3C-1 W3C inclusion-lens (Fail on device sub-dimension) — the workspace knew it wasn't testing mobile but shipped CSS-content characters anyway. Both anti-patterns named; the gap was *between* them.

Next action:
1. v1.2.1 fix: replace `↕` with inline SVG `background-image` (shipped in this PR)
2. Lab 06 audit-shape upgrade: every CSS-content-character OR `position:absolute` change in a future polish PR gets a mobile-viewport screenshot before merge (provisional rule landed in `topic-06-gestalt-audit.md` Audit Addendum 2)
3. NEXT_ACTIONS: when capture-fixes.js scripts are expanded, add a mobile-viewport variant (priority deferred until next polish PR cycle)

## Failure: Audit-region with multiple sub-regions audited as one perceptual unit (drawer R6)

Date: 2026-05-18 (caught) / introduced 2026-05-17 by Lab 06 (PR #18)

Context: Lab 06's per-region per-principle audit graded R6 (drawer) as Similarity = Pass, evaluating the drawer-trust banner at the top of the drawer. The audit didn't independently examine the drawer's body sections (`<dl class="drawer-section">` with row-styled definition lists rendering individual fields including Verification).

What went wrong: The drawer's body has a Workflow section that renders `verification_status` as plain text alongside Promotion and Planner-use fields — exactly the same false-negative similarity-collapse pattern that produced F-GES-1 (card meta-grid) and F-GES-2 (table column) at other depths. The audit treated the drawer as one perceptual unit and graded based on the trust-banner; the actual reviewer's eye reads each section independently. The audit recorded a Pass for similarity at R6; the real verdict should have been a Violation at the body's Workflow section.

Why it mattered: The miss meant the v1.1.x polish PR closed F-GES-1 + F-GES-2 (card meta-grid + table column) but left the drawer's Workflow Verification field as plain text — a fifth depth of the *same* similarity-collapse, hidden in a region the audit thought was clean.

Lesson: A region with multiple visually-distinct sub-regions (e.g., drawer = trust-banner + body-with-sections + footer-buttons) needs the per-principle matrix at *sub-region granularity*, not just at the region level. A "Pass" verdict on a region is only safe when every sub-region passes independently.

Reusable warning: **Audit a region only at the granularity at which the user's eye reads it.** If a region contains independent sub-regions (separate visual containers, separate semantic groups), each sub-region gets its own row in the per-principle matrix. The audit-template shape should be: *region → list of sub-regions → per-sub-region × per-principle matrix*.

Related anti-pattern: Lab 06 deep-reading doc §6 violation-taxonomy sub-type 2 (false-negative grouping) at a *different* level — the audit-region hid the false-negative because the matrix granularity was wrong.

Next action:
1. v1.2.1 fix: drawer Workflow Verification row uses `verifPill(r)` (shipped in this PR)
2. Lab 06 audit-shape upgrade: provisional rule added to `topic-06-gestalt-audit.md` Audit Addendum 2 — if a data field appears in more than one sub-region of the same region, the primary-signal must be applied consistently OR a named compensating signal must explain why one appearance is plain text
3. Future Audit 2 (post-Sponsor-Reviewer) explicitly walks every audit-region's sub-regions before grading
