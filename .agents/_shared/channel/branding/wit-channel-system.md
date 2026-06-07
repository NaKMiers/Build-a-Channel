# WIT Channel System

Classification: `Core`

Scope: `CHANNEL_WIDE`

This file defines WIT as a reusable channel character system for future `Why It Works` videos.
It does not apply the system to any existing video project.

## Current Design Reference

Status: `draft replacement generated - awaiting user review`

Previous current set removed:

`.agents/_shared/assets/wit/poses/original-wit-24/`

Removal date: `2026-06-07`

Reason:
the previous channel WIT did not match the stronger thumbnail WIT direction selected by the user.

New direction:
future WIT poses should be generated from the WIT style used in the `Why Cheap Products Keep Getting Worse` packaging thumbnails, especially the simple white round-headed character with thick black outline, oversized black glasses, expressive eyebrows, simple white body, and strong suspicious / betrayed / panicked reactions.

Draft replacement set:

`.agents/_shared/assets/wit/poses/thumbnail-wit-24/`

Draft contact sheet:

`.agents/_shared/assets/wit/poses/thumbnail-wit-24/thumbnail-wit-24-contact-sheet.png`

Until the user approves the draft replacement set, treat it as review-ready but not final.

Older `core-24`, `comedy-core`, and removed `original-wit-24` material should not be used as current channel WIT.

## Role

WIT is the audience-surrogate character for `Why It Works`.

WIT should not mainly feel like a polished presenter.
WIT should feel like:

- the viewer's unlucky friend
- a normal person trying to understand weird modern systems
- a victim of subscriptions, receipts, ads, habits, hidden fees, confusing prices, and social pressure
- a dry visual reaction device that lowers the seriousness of complex topics

Working rule:

`WIT is funniest when the system is happening to him.`

## Two Modes

### Clean WIT

Use Clean WIT for:

- title cards
- calm explanation beats
- channel identity moments
- simple pointing or evidence moments
- moments where the topic needs clarity more than emotion

Clean WIT can be neutral, curious, lightly skeptical, or quietly confident.

### Suffering WIT

Use Suffering WIT for:

- hooks
- punchlines
- retention beats
- thumbnails
- reveal moments
- absurd examples
- any moment where a system physically or emotionally attacks a normal person

Suffering WIT can be suspicious, betrayed, trapped, financially attacked, confused, panicked, or defeated.

## Comedy Principle

WIT should often look less cool than the topic.

Good WIT comedy usually comes from one of these patterns:

- WIT believes the obvious lie for one second too long.
- WIT tries to act smart while the system quietly wins.
- WIT is physically affected by an invisible rule.
- WIT points at evidence only when the evidence itself is the joke.
- WIT looks directly at the viewer when the explanation becomes painfully obvious.

Avoid making WIT cute in every scene.
Cute is the base design, not the joke.

## Acting Requirements

Future WIT poses should be:

- emotionally readable at `25%` screen size
- simple enough for HyperFrames use
- full-body or strong upper-body silhouettes
- consistent with WIT's rough hair, huge glasses, white shirt, black pants, oversized shoes, and receipt-tie motif
- rough enough to be funny, but still recognizable
- exported with transparent background and animation-safe margins

WIT should not:

- block the main joke text
- become the main topic of the video
- smile during suspicious, negative, betrayed, or trapped beats
- copy the exact Casually Explained stick-figure style
- use third-party logos or readable brand names as baked-in props

## Thumbnail Rule

In thumbnails, WIT must have one clear emotion:

- betrayed
- suspicious
- trapped
- panicked
- confused
- defeated

Avoid neutral WIT in thumbnails.

Thumbnail WIT should answer:

`How does this topic feel to a normal person?`

## Current Pose Set

There is currently a draft reusable WIT pose set awaiting user review.

Draft set:

`.agents/_shared/assets/wit/poses/thumbnail-wit-24/`

Contact sheet:

`.agents/_shared/assets/wit/poses/thumbnail-wit-24/thumbnail-wit-24-contact-sheet.png`

Until then:

- do not use `original-wit-24` as current WIT
- do not regenerate old hair / shirt / receipt-tie WIT
- do not treat `thumbnail-wit-24` as final until the user approves it
- keep thumbnail work aligned with this draft thumbnail-WIT style when packaging this video

## Frequency Rule

In comedy-heavy videos, plan at least one Suffering WIT moment every `20-30` seconds.

This does not mean WIT must always be on screen.
It means the video should regularly show how the topic feels to a normal person.

## Future Video Use

For future videos:

1. Choose the main emotional arc for WIT before production.
2. Use Clean WIT for setup and explanation.
3. Use Suffering WIT for hooks, jokes, and reveal beats.
4. Use the approved replacement WIT pose set once it exists.
5. Do not use removed `original-wit-24` assets as the default character.
6. Keep all generated reusable poses in `.agents/_shared/assets/wit/poses/` until a specific video explicitly copies approved assets into its own project folder.

Do not apply this system to a video project unless the user explicitly asks:

`Apply this channel-wide system to projects/<slug>`
