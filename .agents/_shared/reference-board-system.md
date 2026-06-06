# Why It Works Reference Board System

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
make every future `Why It Works` video visually and comedically specific before scripting, packaging, or HyperFrames production.

This system creates the channel-wide standard only. It does not create a reference board for any existing video project.

## Core Standard

Working rule:

```text
What does this topic look like in real life, and what would make it funny if paused?
```

Before a future video moves from topic idea into script or production, it should have a small reference board that gives the topic:

- real-life texture
- recognizable objects
- concrete UI or paper evidence
- thumbnail tension
- WIT emotion direction
- visual jokes that can survive a paused frame

The board is not an aesthetic moodboard. It is a research tool for specificity.

## Relationship To Existing Systems

Use this system before or alongside:

- [Thumbnail Packaging System](thumbnail-packaging-system.md)
- [Hook System](hook-system.md)
- [Real-Life Visual Asset System](real-life-visual-asset-system.md)
- [Scene Grammar System](scene-grammar-system.md)
- [Visual Humor Patterns](visual-humor-patterns.md)
- [HyperFrames Board Grammar](hyperframes/board-grammar.md)

The practical chain:

```text
reference board -> title/thumbnail tension -> first 10 seconds -> script examples -> visual boards -> HyperFrames assets
```

The reference board should usually happen before full script drafting. If the script already exists, use the board before production planning so the visuals do not become generic cards.

## Board Size

Target for each future video:

- `5` real-life object references
- `5` UI, paper, or screenshot references
- `5` visual metaphor references
- `5` thumbnail tension references
- `5` WIT emotion or character-state references
- `3` color and contrast references

Total target:

```text
20-30 useful references
```

Useful means the reference can improve at least one of:

- the thumbnail
- the first `10` seconds
- a visual joke
- a real-life example
- a WIT reaction
- a recurring motif
- a safe asset plan

## Research Categories

### 1. Topic Reality

Find what the issue looks like in daily life.

Use for:

- bills
- receipts
- forms
- warnings
- invoices
- calendars
- phone screens
- checkout pages
- workplace dashboards
- bank or payment mockups

Question:

```text
What would the viewer recognize in two seconds?
```

### 2. Comedy Objects

Find objects that can become jokes when exaggerated, labeled, corrected, or aimed at WIT.

Use for:

- receipt printers
- red markers
- tiny locks
- warning signs
- sad wallets
- angry phones
- moving boxes
- fake certificates
- broken checklists
- suspicious buttons

Question:

```text
What object can make the system feel stupid without needing a long explanation?
```

### 3. Viewer Recognition

Find visual patterns viewers instantly understand.

Use for:

- `low battery`
- `free trial`
- `storage full`
- `streak lost`
- `payment failed`
- `subscribe to continue`
- `your cart has changed`
- `limited time offer`
- `terms and conditions`

Question:

```text
What small screen or paper detail makes the viewer think, "I know this"?
```

### 4. Thumbnail Tension

Find one-frame contradictions.

Use for:

- `FREE` button plus a bill
- `cheap` product falling apart
- `budget` notebook on fire
- `productivity` checklist crushing WIT
- `convenience` object making life harder
- `smart advice` card next to a bad outcome

Question:

```text
What contradiction can be understood at mobile size?
```

### 5. WIT Emotion

Find the emotional state WIT should carry in the video.

Use for:

- suspicious
- trapped
- buried
- confused
- financially attacked
- politely betrayed
- trying to understand
- pretending everything is fine

Question:

```text
What is happening to WIT because of this system?
```

### 6. Color And Contrast

Find simple contrast references that help the topic read quickly.

Use for:

- warning red
- receipt paper white
- fake app blue
- sickly sale green
- dull office gray
- highlighter yellow
- black marker correction

Question:

```text
Which two or three colors make the promise and contradiction obvious?
```

## Workflow For Future Videos

Use this workflow only when starting a new video project or when the user explicitly applies this system to a video folder.

1. Read the topic idea.
2. Write the main contradiction in one sentence.
3. List the real-life objects connected to that contradiction.
4. Create a local board folder from [.agents/_shared/reference-boards/_template](reference-boards/_template).
5. Collect or describe `20-30` useful references.
6. Mark each item as `safe asset`, `mockup target`, `inspiration only`, or `reject`.
7. Write source notes before using any collected external or generated reference in production.
8. Pick one recurring motif.
9. Use the board to write the title-thumbnail direction.
10. Use the board to design the first `10` seconds.
11. Use the board to choose at least `5` visual jokes or paused-frame moments.
12. Move only approved assets into production after source and safety checks pass.

Do not create a video-specific board unless the user explicitly says:

```text
Apply this channel-wide system to projects/<slug>
```

## Source-Note Rules

Every board item needs a short source note if it is saved, copied, generated, or used to influence production.

Minimum source-note fields:

```text
Reference ID:
Category:
Source type:
Original source URL or local origin:
Creator/owner if known:
Date collected:
Usage status:
Safe-use decision:
Reason:
Production use allowed:
Notes:
```

Allowed usage statuses:

- `safe asset`
- `mockup target`
- `inspiration only`
- `reject`

Use `safe asset` only when the asset can be used in a public video with clear permission, no private data, no watermark, no dominant accidental logo, and a documented source.

Use `mockup target` when the reference should be recreated as a fictional UI, fake paper object, generated image, or self-made prop.

Use `inspiration only` when the reference helps understand the topic, but the final video must not copy the frame, layout, image, logo, screenshot, or creator-specific joke.

Use `reject` when the source is unclear, legally risky, too close to another creator's frame, privacy-sensitive, visually confusing, or off-brand.

For production assets, use the fuller template in [assets/source-note-template.md](assets/source-note-template.md).

## Copyright, Privacy, And Copying Rules

Do not:

- copy another creator's exact frame
- reuse YouTube thumbnails as final channel thumbnails
- use real private data
- rely on blurred private information
- copy real app screens pixel-for-pixel
- use unclear copyrighted images as final production assets
- treat a reference board as a license library

Prefer:

- self-shot photos
- self-made mockups
- generated generic objects
- public-domain or permissively licensed images
- fictional UI
- recreated paper objects
- source-labeled inspiration that becomes a new visual idea

## Recurring Motif Rule

Every future board should name one recurring motif.

Examples:

- free button that keeps printing bills
- progress bar that charges rent
- checklist that multiplies
- phone notification stack that becomes a wall
- tiny lock attached to every convenient thing
- red marker correcting every promise

The motif should be simple enough to appear in:

- the thumbnail
- the first `10` seconds
- one explanation section
- one payoff or callback

## Acceptance Criteria

A future reference board is ready when it:

- suggests a thumbnail
- suggests the first `10` seconds
- suggests at least `5` visual jokes
- contains real-life texture
- names the recurring motif
- separates safe assets from inspiration-only references
- has source notes for saved or generated references
- avoids copying another creator's exact frame
- makes the video feel more specific than cards and labels

If the board only collects pretty images, it is not ready.

## Channel-Wide Storage

The reusable template lives at:

```text
.agents/_shared/reference-boards/_template/
  README.md
  thumbnails/
  real-life/
  ui-mockups/
  visual-metaphors/
  wit-emotions/
  color-contrast/
  source-notes/
```

Channel-wide board standards live at:

```text
.agents/_shared/reference-board-system.md
.agents/_shared/reference-boards/README.md
```

Do not store one-off topic boards in `.agents/_shared/`.
Future one-off boards belong in the relevant `projects/<slug>/` folder only after an explicit apply command.

## Implementation Status

This is the channel-wide standard for Plan 10.

No existing `projects/` files are updated by this system.
