# WIT Pose System

Status: `Experiment`
Created: `2026-05-23`
Purpose: turn WIT from a single character reference into a reusable acting library for `Why It Works` videos.

## Why This Exists

Explainer videos in the Mèo Giải Thích / Vui Vẻ direction need many fast visual beats.

WIT should not require a new custom drawing for every joke. The channel needs a reusable pose set that can cover:

- explanation
- confusion
- realization
- money stress
- internet absurdity
- business/system diagrams
- dry punchlines

Working rule:

`One character, many reactions.`

## Production Principle

Start with a small high-use pose set, then expand only when repeated scripts need new acting.

Recommended build order:

1. `Core 12` poses for the first complete video
2. `Expansion 24` after the first rough cut
3. `Special poses` only when a script truly needs them

## Naming Convention

Use lowercase kebab-case filenames:

```text
wit-pose-neutral-front.png
wit-pose-pointing-left.png
wit-pose-confused.png
wit-pose-receipt-panic.png
```

If later converted to vector or layered assets, keep the same base names:

```text
wit-pose-confused.svg
wit-pose-confused.psd
wit-pose-confused.json
```

## Core 12 Poses

These should be created first.

| Priority | Pose | Filename | Use Case |
|---|---|---|---|
| 1 | Neutral front | `wit-pose-neutral-front.png` | Default narrator/listener pose |
| 1 | Talking front | `wit-pose-talking-front.png` | Simple narration beats |
| 1 | Pointing left | `wit-pose-pointing-left.png` | Explaining on-screen text or chart |
| 1 | Pointing right | `wit-pose-pointing-right.png` | Explaining opposite-side object |
| 1 | Confused | `wit-pose-confused.png` | Viewer confusion, weird system moment |
| 1 | Shocked | `wit-pose-shocked.png` | Reveal, price jump, absurd fact |
| 1 | Deadpan | `wit-pose-deadpan.png` | Dry joke, cynical observation |
| 1 | Thinking | `wit-pose-thinking.png` | Reframe, setup, question |
| 1 | Holding phone | `wit-pose-holding-phone.png` | Apps, internet behavior, social media |
| 1 | Holding receipt | `wit-pose-holding-receipt.png` | Hidden cost, spending, subscriptions |
| 1 | Money panic | `wit-pose-money-panic.png` | Broke feeling, debt, fees |
| 1 | Tiny defeated | `wit-pose-tiny-defeated.png` | Punchline after modern-life frustration |

## Expansion 24 Poses

Create these after the first full rough cut shows where WIT feels too repetitive.

| Pose | Filename | Use Case |
|---|---|---|
| Walking | `wit-pose-walking.png` | Scene transitions, journey metaphors |
| Running | `wit-pose-running.png` | Panic, chase, urgency |
| Falling | `wit-pose-falling.png` | Failed plans, bad decisions |
| Celebrating | `wit-pose-celebrating.png` | False victory or ironic win |
| Suspicious | `wit-pose-suspicious.png` | Bad advice, shady business, hidden motive |
| Calculator | `wit-pose-calculator.png` | Budget, finance, math joke |
| Laptop | `wit-pose-laptop.png` | Work, internet, productivity |
| Presentation | `wit-pose-presentation.png` | Explaining diagrams |
| Magnifying glass | `wit-pose-magnifying-glass.png` | Investigation, hidden systems |
| Buried in bills | `wit-pose-buried-in-bills.png` | Subscriptions, debt, fees |
| Carrying giant coin | `wit-pose-carrying-coin.png` | Money burden |
| Holding credit card | `wit-pose-holding-card.png` | Consumer debt, app payments |
| Stretching receipt tie | `wit-pose-receipt-tie-stretch.png` | Hidden cost gag |
| Angel/devil choice | `wit-pose-choice.png` | Temptation, spending choice |
| Looking up | `wit-pose-looking-up.png` | Big systems, impossible scale |
| Looking down | `wit-pose-looking-down.png` | Charts, tiny details |
| Side eye | `wit-pose-side-eye.png` | Skepticism |
| Facepalm | `wit-pose-facepalm.png` | Obviously bad logic |
| Sweating | `wit-pose-sweating.png` | Stress, awkward money truth |
| Sleeping | `wit-pose-sleeping.png` | Boredom, passive behavior |
| Coffee tired | `wit-pose-coffee-tired.png` | Work life, burnout |
| With crown | `wit-pose-fake-rich.png` | Fake wealth, status spending |
| Empty wallet | `wit-pose-empty-wallet.png` | Broke punchline |
| Ascending insight | `wit-pose-realization.png` | Payoff, final insight |

## Expression Variants

For the most-used poses, generate expression variants instead of redrawing the whole body:

- neutral
- happy
- worried
- deadpan
- shocked
- skeptical

High-priority expression variant targets:

- `neutral-front`
- `talking-front`
- `pointing-left`
- `pointing-right`
- `holding-phone`
- `holding-receipt`

## HyperFrames Use

Each pose should be importable as a static asset and animated with lightweight HyperFrames/GSAP motion:

- scale bounce
- position slide
- eye blink overlay
- mouth flap overlay
- small rotation shake
- squash/stretch on punchlines
- opacity pop-in

Avoid making every pose a full custom animation. The production advantage comes from reusing still poses with smart movement.

## Asset Requirements

Each generated pose should have:

- transparent background
- consistent character proportions
- consistent glasses, hair, shirt, shorts, shoes, and receipt tie
- clean outline readable at small size
- no readable text on the receipt tie
- no logo, watermark, or background scene
- enough empty margin to avoid clipping during bounce/shake animation

Preferred export:

- `2048x2048 PNG`
- transparent background
- character centered

## First Generation Batch

Generate these first:

1. `wit-pose-neutral-front.png`
2. `wit-pose-talking-front.png`
3. `wit-pose-pointing-left.png`
4. `wit-pose-pointing-right.png`
5. `wit-pose-confused.png`
6. `wit-pose-shocked.png`
7. `wit-pose-deadpan.png`
8. `wit-pose-thinking.png`
9. `wit-pose-holding-phone.png`
10. `wit-pose-holding-receipt.png`
11. `wit-pose-money-panic.png`
12. `wit-pose-tiny-defeated.png`

## Prompt Template

```text
Create a transparent-background pose asset for WIT, the recurring mascot of the YouTube channel `Why It Works`.

Use the provided WIT reference as the identity source. Preserve the same cute short proportions, dark parted fluffy hair, black round glasses, pale blue striped short-sleeve shirt, dark shorts, black shoes, and receipt-like tie with tiny abstract marks only.

Pose requested:
[POSE DESCRIPTION]

Style:
simple 2D mascot, clean hand-drawn outline, soft friendly shape, readable silhouette, dry-humor explainer character, not glossy 3D, not heavy anime, not corporate mascot.

Technical requirements:
transparent background, centered character, full body visible, no readable text, no logo, no watermark, enough margin around the character for animation.
```

## Strategy Classification

Classification: `Experiment`

Reason:
This supports the current visual identity experiment for WIT and improves production speed, but it should not become locked core identity until tested in at least one finished video.
