# Plan 01: Remake WIT

Classification:
`Core channel upgrade plan`

Goal:
remake the channel-wide WIT system so WIT functions as a funny reaction device and modern-life victim in every future video, not only as a cute mascot presenter.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable WIT system for the entire channel. It must not inspect, rewrite, or modify any video project.

Allowed outputs:

- `.agents/_shared/channel/branding/wit-channel-system.md`
- `.agents/_shared/assets/wit/README.md`
- `.agents/_shared/assets/wit/poses/comedy-core/`
- `.agents/_shared/assets/wit/poses/comedy-core/contact-sheet.png`
- `.agents/_shared/assets/wit/usage-rules.md`

Forbidden outputs:

- no edits to `projects/<slug>/`
- no per-video WIT plan
- no copying WIT poses into an active video project
- no updating an active video's visual plan

Source insight:
Casually Explained's character works because he is rough, dumb-looking in a good way, emotionally readable, and never too polished. The character lowers the seriousness of complex topics.

## Problem

Current WIT is usable, cute, and recognizable, but often too polished.

Weaknesses:

- WIT can feel like a presenter instead of the person suffering from the topic.
- WIT often reacts after the explanation instead of creating the joke visually.
- WIT is too visually nice for some dry, absurd topics.
- WIT does not yet have enough extreme comedy poses.
- WIT is not always integrated with real-life props.

## Target

WIT should feel like:

- the viewer's unlucky friend
- a victim of modern systems
- suspicious of everything that says `free`
- financially attacked by receipts, subscriptions, ads, habits, and hidden fees
- cute enough to be recurring, but rough enough to be funny

## Design Direction

Create two WIT modes:

1. `Clean WIT`
   Use for title cards, calm explanations, and channel identity.

2. `Suffering WIT`
   Use for punchlines, thumbnails, hooks, and retention beats.

Do not delete the existing WIT system.
Add a comedy layer on top of it.

## Required Pose Set

Create or refine a reusable `comedy-core` WIT pose set.

Minimum poses:

- `deadpan-front`
- `deadpan-side-eye`
- `suspicious-phone`
- `betrayed-by-phone`
- `financially-attacked`
- `buried-in-receipts`
- `subscription-panic`
- `tiny-defeated`
- `fake-confident`
- `confused-math`
- `staring-at-viewer`
- `pointing-at-evidence`
- `holding-red-marker`
- `dragging-data-box`
- `trapped-in-app`
- `receipt-printer-victim`

## Visual Rules

- WIT should often look less cool than the topic.
- WIT should be physically affected by the system being explained.
- WIT should point at evidence only when the evidence is the joke.
- WIT should not smile during suspicious or negative beats.
- WIT can be ugly-funny in expressions, but should remain recognizable.
- WIT should be large enough to read clearly on mobile.
- WIT should never block the main joke text.

## Thumbnail WIT Rules

For thumbnails, WIT should have one clear emotion:

- betrayed
- suspicious
- trapped
- panicked
- confused
- defeated

Avoid neutral WIT in thumbnails.

Thumbnail WIT should answer:

`How does this topic feel to a normal person?`

## Production Steps

1. Audit current WIT pose folder.
2. Mark which poses already support comedy.
3. List missing emotional states.
4. Generate or draw rough comedy variants.
5. Build a contact sheet.
6. Test the poses at thumbnail size.
7. Test the poses at video frame size.
8. Add approved poses to `.agents/_shared/assets/wit/poses/`.
9. Write channel-wide WIT usage rules.
10. Define channel rules for how future videos should select WIT poses after the channel system is complete.

## Acceptance Criteria

A WIT remake pass is successful if:

- WIT is funny when paused.
- WIT's emotion is readable at `25%` screen size.
- WIT has at least one suffering moment every `20-30` seconds in comedy-heavy videos.
- WIT helps explain the topic without becoming the topic.
- WIT is usable in thumbnails.
- WIT feels distinct from Casually Explained's stick figure.

## Do Not Do

- Do not copy Casually Explained's exact stick figure.
- Do not replace WIT with a generic mascot.
- Do not make WIT too detailed to animate or reuse.
- Do not make WIT cute in every scene.
- Do not use WIT as decoration when no reaction is needed.

## Session Prompt For Future Codex

Use this prompt when starting a WIT improvement session:

```text
Scope: CHANNEL_WIDE.
Read .agents/_shared/channel/channel-improvement-plans/01-remake-wit-plan.md.
Audit the current WIT assets under .agents/_shared/assets/wit.
Create or update the channel-wide WIT system only.
Allowed outputs are .agents/_shared/channel/branding and .agents/_shared/assets/wit.
Do not edit projects.
Do not apply this to any specific video until I explicitly ask.
```
