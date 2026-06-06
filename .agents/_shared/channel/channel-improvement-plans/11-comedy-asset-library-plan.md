# Plan 11: Comedy Asset Library

Classification:
`Core channel upgrade plan`

Goal:
build a reusable library of funny visual objects, reactions, rough props, and running motifs so every video can become more specific and less slide-like.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable comedy asset library for the entire channel. It must not select assets for any specific video.

Allowed outputs:

- `.agents/_shared/assets/comedy/README.md`
- `.agents/_shared/assets/comedy/asset-inventory.md`
- `.agents/_shared/assets/comedy/source-note-template.md`
- `.agents/_shared/assets/comedy/contact-sheets/`

Forbidden outputs:

- no edits to `projects/<slug>/`
- no video-specific asset selection
- no copied assets inside an active video folder

Source insight:
The Casually Explained references feel alive because the screen often looks like a messy folder of evidence: real images, dumb drawings, rough labels, arrows, maps, and a character reacting to absurdity. `Why It Works` needs its own reusable comedy objects so each new video does not start from a blank visual language.

## Problem

Current production often depends on:

- WIT poses
- handwritten text
- simple cards
- clean diagrams
- abstract icons

These are useful, but they can make different videos feel too similar.

The channel needs reusable comedy assets that can quickly make a topic feel:

- real
- weird
- suspicious
- financially painful
- modern-life specific
- funny when paused

## Target

Create a shared asset system under:

```text
.agents/_shared/assets/comedy/
```

The library should include reusable objects that support the channel's main lane:

- money
- internet
- society
- business
- modern life

Each asset should have:

- transparent PNG or web-ready format
- simple source note
- intended use
- examples of jokes it supports
- whether it is safe for thumbnails
- whether it is safe for video only

## Core Asset Categories

### 1. Hidden Payment Objects

Use for money, subscriptions, free apps, confusing prices, and modern life costs.

Assets:

- receipt printer
- checkout terminal
- credit card machine
- long receipt
- tiny invoice
- subscription bill
- payment failed popup
- fake bank app screen
- wallet with leak
- price tag with asterisk

Comedy use:

- hide them behind friendly objects
- make them appear too late
- make WIT get attacked by them
- use them as the visual payoff behind "free"

### 2. Internet Trap Objects

Use for social media, apps, productivity, notifications, gurus, and online advice.

Assets:

- angry phone
- notification bubble
- fake comment card
- infinite feed strip
- app-store-style install button
- streak warning
- pop-up modal
- terms and conditions scroll
- fake guru thumbnail frame
- algorithm box

Comedy use:

- make the phone act like a boss
- make notifications physically pull WIT
- make streaks sound like hostage notes
- show the feed as a conveyor belt

### 3. Modern Life Pain Objects

Use for work, stress, productivity, lifestyle, and adulthood topics.

Assets:

- calendar wall
- checklist pile
- moving boxes
- cheap desk
- delivery bag
- broken product
- coffee cup tower
- unread email stack
- bills on floor
- "later" sticky note

Comedy use:

- bury WIT under admin tasks
- turn checklists into a cage
- show adulthood as a checkout line
- make "convenience" look physically heavy

### 4. Red Markup Tools

Use for correction beats and punchlines.

Assets:

- red cross-out
- rough circle
- warning arrow
- fake footnote star
- red underline
- "nope" stamp
- suspicious question mark
- bad math correction

Comedy use:

- correct the viewer's assumption
- mark the hidden trick
- expose the real business logic
- convert a clean claim into a suspicious claim

### 5. WIT Interaction Props

Use to make WIT physically involved instead of decorative.

Assets:

- tiny chair
- phone WIT can hold
- receipt scarf extension
- moving box labeled `data`
- red marker
- magnifying glass
- small shovel for "digging into fees"
- fake contract
- calculator
- tiny umbrella against bills

Comedy use:

- WIT carries the metaphor
- WIT gets trapped by the object
- WIT points at evidence
- WIT becomes the scale reference for absurd systems

## Asset Quality Rules

Assets should be:

- readable at mobile size
- visually simple
- rough enough to feel human
- not too polished or corporate
- easy to recolor or label
- reusable across many videos

Avoid:

- generic icon packs as the main asset
- overly detailed generated images
- stock photos that feel fake
- copyrighted logos as reusable default assets
- assets that only work for one joke unless the joke is excellent

## File Structure

Use:

```text
.agents/_shared/assets/comedy/
  README.md
  hidden-payment/
  internet-traps/
  modern-life-pain/
  red-markup/
  wit-props/
  contact-sheets/
```

Each folder should include:

```text
README.md
asset-name.png
asset-name.source.md
```

Source note template:

```markdown
# Asset: <name>

Status: `usable` / `draft` / `reference-only`
Type: `generated` / `drawn` / `self-made mockup` / `licensed` / `public-domain`
Safe for thumbnail: `yes/no`
Safe for video: `yes/no`
Best uses:
- ...
Do not use for:
- ...
```

## Build Workflow

1. Audit existing assets under `.agents/_shared/assets/`.
2. Identify reusable objects already present.
3. Create the `.agents/_shared/assets/comedy/` folder.
4. Start with `5` assets per category, not a giant library.
5. Make one contact sheet per category.
6. Test assets inside a mock `1920x1080` board.
7. Test assets at thumbnail size.
8. Promote only assets that remain readable.
9. Add source notes.
10. Update this plan when a new recurring asset proves useful.

## Per-Video Usage Rule

For each video, select:

- `1` main recurring motif
- `2-4` supporting comedy objects
- `1` red markup style
- `1-2` WIT props

Do not throw the whole library into one future video.

## Acceptance Criteria

The comedy asset library is working if:

- future video boards become faster to plan
- thumbnails become easier to mock up
- paused frames feel less generic
- WIT has more ways to interact with the topic
- the channel starts to have recognizable repeated objects
- assets support jokes without confusing English learners

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read .agents/_shared/channel/channel-improvement-plans/11-comedy-asset-library-plan.md.
Audit .agents/_shared/assets and propose the first comedy asset library pass.
Create a folder plan, asset list, source-note template, and first contact-sheet plan.
Do not use copyrighted images unless a safe-use plan is documented.
Do not edit projects.
```
