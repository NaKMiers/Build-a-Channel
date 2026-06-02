# WIT Channel System

Classification: `Core`

Scope: `CHANNEL_WIDE`

This file defines WIT as a reusable channel character system for future `Why It Works` videos.
It does not apply the system to any existing video project.

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
- consistent with WIT's hair, glasses, shirt, shorts, shoes, and receipt motif
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

## Comedy-Core Pose Set

The channel-wide comedy-core pose layer lives at:

`common/assets/wit/poses/comedy-core/`

It is a reusable layer on top of the older `core-24` experiment.
Do not delete `core-24`.
Use `core-24` for general WIT coverage and `comedy-core` when the video needs stronger reaction acting.

Minimum comedy-core poses:

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

## Frequency Rule

In comedy-heavy videos, plan at least one Suffering WIT moment every `20-30` seconds.

This does not mean WIT must always be on screen.
It means the video should regularly show how the topic feels to a normal person.

## Future Video Use

For future videos:

1. Choose the main emotional arc for WIT before production.
2. Use Clean WIT for setup and explanation.
3. Use Suffering WIT for hooks, jokes, and reveal beats.
4. Select poses from `comedy-core` first when the beat is emotional.
5. Draw or generate missing comedy poses only when the script truly needs them.
6. Keep all generated reusable poses in `common/assets/wit/poses/comedy-core/` until a specific video explicitly copies approved assets into its own project folder.

Do not apply this system to a video project unless the user explicitly asks:

`Apply this channel-wide system to video-projects/<slug>`
