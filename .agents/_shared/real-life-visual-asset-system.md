# Why It Works Real-Life Visual Asset System

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
make future `Why It Works` videos feel like rough drawings commenting on real life, not clean slide decks about real life.

This system applies to future video planning, asset sourcing, HyperFrames production, packaging, and quality review. It does not create an asset board for any existing video project.

## Core Standard

Working rule:

```text
Use real-life assets as evidence, not decoration.
```

Real-life assets should make the viewer think:

```text
That is my phone, my bill, my cart, my desk, or my bad decision.
```

The channel style should mix:

- WIT as the unlucky audience surrogate
- handwritten labels, arrows, captions, and red corrections
- real or real-looking objects from daily life
- simple drawings when a real asset would distract

The target feel is:

```text
rough drawings commenting on real life
```

not:

```text
polished stock footage with labels on top
```

## Relationship To Existing Systems

Use this system together with:

- [WIT Channel System](../.agents/_shared/channel/branding/wit-channel-system.md)
- [WIT Usage Rules](assets/wit/usage-rules.md)
- [Hook System](hook-system.md)
- [Thumbnail Packaging System](thumbnail-packaging-system.md)

The practical chain:

```text
real object -> suspicious detail -> WIT reaction -> handwritten explanation
```

For future videos, the dominant object should usually appear in the thumbnail, the first `10` seconds, and at least one later explanation beat.

## Visual Mix Rule

For a compact `3-5` minute video:

- use WIT regularly
- use handwritten text constantly
- use one real or real-looking asset every `10-15` seconds when the topic is object-driven
- use red marker only for corrections, reveals, contradiction labels, and punchline fixes
- use simple drawings when real assets would reduce clarity

For longer `6-10` minute videos:

- keep the same texture density in the hook and key retention beats
- make sure every major section has at least one recognizable real-life object, paper, screen, or physical consequence
- avoid filling the whole video with assets if the explanation needs a clean diagram

## Asset Categories

Allowed default sources:

- self-shot photos
- generated images
- public-domain images
- properly licensed images
- self-made UI mockups
- screenshots recreated as generic mockups
- scanned paper textures
- receipt photos with private data removed
- phone photos with private data removed
- rough object cutouts

Default channel categories:

| Category | Use For | Preferred Style |
| --- | --- | --- |
| `self-shot` | desks, hands, wallets, bills, clutter, phones | imperfect, real, cropped cleanly |
| `generated` | hard-to-shoot generic objects or scenes | realistic enough, not glossy stock |
| `public-domain-licensed` | safe external reference assets | documented source and license |
| `paper-textures` | receipts, notes, checklists, bills | scanned, rough, readable |
| `receipts-and-bills` | money, hidden cost, subscriptions | fake data or fully redacted |
| `object-cutouts` | phones, cards, bags, boxes, price tags | transparent PNG/SVG-friendly |
| `physical-context` | rooms, desks, delivery bags, moving boxes | lived-in but uncluttered |
| `ui-mockups` | apps, feeds, banks, browsers, comments | fake UI, no real private data |

## Topic Defaults

For money topics, prioritize:

- receipts
- wallets
- payment terminals
- bills
- subscription cards
- bank app mockups
- checkout screens
- price tags

For internet topics, prioritize:

- phone screens
- notification mockups
- feed mockups
- app-store-style screens
- fake profile cards
- comment sections
- browser windows

For modern-life topics, prioritize:

- desks
- calendars
- checklists
- moving boxes
- delivery bags
- cluttered rooms
- tired worker silhouettes
- generic office objects

## Default Asset Pattern

For any future topic, define at least five reusable visual anchors:

| Anchor | Job |
| --- | --- |
| one recognizable real-world object | makes the topic concrete |
| one hidden-cost object | reveals what the viewer did not notice |
| one UI or paper mockup | turns the system into readable evidence |
| one physical consequence for WIT | makes the joke happen to a person |
| one red correction asset | turns the false promise into the real explanation |

Example pattern:

```text
phone screen -> hidden monthly bill -> fake checkout receipt -> WIT buried in paper -> red "not free" correction
```

## Future Per-Video Workflow

Use this workflow only when starting or updating a future video with explicit permission to work inside its `projects/<slug>/` folder.

1. Define the video's recurring metaphor.
2. List `20` possible real-life objects.
3. Select `8-12` objects that can appear in the video.
4. Decide which assets should be self-shot, generated, licensed, or mocked.
5. Create a video-specific visual reference board inside the video project.
6. Build cutout-ready assets.
7. Test each important asset at `1920x1080`.
8. Test each important asset at mobile scale.
9. Copy approved assets into the video project's local asset folder.
10. Document source and usage notes with [source-note-template.md](assets/source-note-template.md).

Do not create video-specific boards or copy assets into a video folder unless the user explicitly asks:

```text
Apply this channel-wide system to projects/<slug>
```

## Channel-Wide Storage Rules

Reusable channel assets live in:

```text
.agents/_shared/assets/real-life/
.agents/_shared/assets/ui-mockups/
```

Use `.agents/_shared/assets/real-life/` for reusable object photos, paper textures, cutouts, and physical environments.

Use `.agents/_shared/assets/ui-mockups/` for reusable fake app screens, browser windows, feed cards, comments, payment screens, and notification systems.

Use `.agents/_shared/assets/source-note-template.md` as the source note template for both folders.

Do not store one-off video assets in `.agents/_shared/`.
One-off assets belong in the relevant future video folder only after an explicit apply command.

## Naming Rules

Use lowercase kebab-case filenames:

```text
receipt-generic-001.png
phone-notification-stack-001.png
bank-app-mockup-balance-hidden-001.png
checkout-screen-fee-reveal-001.png
paper-texture-creased-001.jpg
```

Preferred filename shape:

```text
[asset-type]-[specific-job]-[number].[ext]
```

Avoid:

- spaces
- dates as the only identifier
- brand names in filenames unless the asset has a documented rights and accuracy reason
- vague names like `image1.png`, `final.png`, or `funny-card.png`

## Safe-Use Rules

### Private Information

Never use real private information.

Remove or replace:

- names
- addresses
- phone numbers
- email addresses
- account numbers
- QR codes
- barcodes
- order IDs
- card numbers
- transaction IDs
- exact balances from real accounts

When in doubt, recreate the object as a fake mockup.

### Copyright And Licensing

Do not use copyrighted images without a safe plan.

Allowed external images must have one of:

- public-domain status
- permissive license
- paid license
- explicit permission
- fair-use rationale approved for the specific video context

Every external asset needs a source note.

### Logos And Real Apps

Avoid real app logos and real brand UI unless the video has a specific reason.

Prefer:

- generic fake app names
- simple icon shapes
- recreated UI patterns
- fictional profile cards
- fake comments
- fake screenshots

Do not copy a real app screen pixel-for-pixel.
Represent the idea, not the protected interface.

### AI-Generated Assets

Generated images are allowed when they are:

- generic
- safe for commercial/video use under the tool terms
- free of watermarks
- free of private likenesses
- free of fake readable brand names
- documented with prompt, model/tool, date, and editing notes

Generated assets should not look like glossy stock photos unless the joke requires that exact feeling.

### UI Mockups

UI mockups should be clearly fictional.

Use:

- fake names
- fake balances
- fake comments
- fake app titles
- fake profile photos or simple avatars
- readable but generic labels

Avoid:

- real account data
- exact brand layouts
- real logos
- real app screenshots with sensitive data blurred only at the end
- tiny text that cannot be read on mobile

## HyperFrames Use

In HyperFrames, real-life assets should usually enter as:

- static background object
- cutout prop
- paper or receipt layer
- fake screen placed inside a phone frame
- texture behind handwritten text
- object that WIT reacts to
- red-marker corrected evidence

Use simple motion:

- hard cuts
- small slide-in
- tiny bounce
- red correction reveal
- quick receipt print
- small shake on suspicious labels

Avoid turning asset-heavy scenes into busy dashboards.
The object should make the joke or evidence clearer.

## Quality Gate

Before a real-life asset is approved for channel reuse, check:

- source note exists
- safe-use decision is clear
- no private data
- no watermark
- no accidental brand logo
- readable at `1920x1080`
- still readable at `25%` scale when it carries meaning
- crop works with handwritten labels
- WIT can react to it without blocking the main evidence
- asset supports a joke, example, or explanation

Before a future video passes visual planning, check:

- at least one asset makes the viewer think `this is my life`
- the video does not feel like only cards and labels
- assets support jokes instead of decorating
- real-life texture does not reduce learner clarity
- source and usage notes are documented locally

## Rejection Rules

Reject an asset if:

- the source is unclear
- the license is unclear
- private data is visible
- a logo dominates the frame without a specific reason
- it looks like generic stock decoration
- it makes the explanation harder to understand
- it cannot be read on mobile when readability matters
- it only exists because the scene felt empty

## Implementation Status

This is the channel-wide standard.

The reusable folder structure starts at:

```text
.agents/_shared/assets/real-life/
.agents/_shared/assets/ui-mockups/
.agents/_shared/assets/source-note-template.md
```

No existing `projects/` files are updated by this system.
