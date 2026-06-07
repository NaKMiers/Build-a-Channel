# Visual Production System

Classification: `Core production system`

Scope: `CHANNEL_WIDE`

Use this file for reference boards, real-life visual assets, UI mockups, WIT use, scene grammar, visual humor, and HyperFrames board checks.

## Core Rule

Static drawing -> narration twist -> red markup or hard cut -> next static drawing.

Start simple. Make paused frames clear before adding motion.

## Visual Plan Handoff Rule

Visual planning is the critical handoff into HyperFrames.

For each section, the visual plan must answer:

- what appears on screen
- when it appears against the voiceover
- how it moves, cuts, reveals, or changes
- why it holds attention
- what assets or references HyperFrames needs

The renderer should not need to invent the main scene, timing, joke, object, asset list, or reference logic.

## One-Board Contract

Each board should carry:

- one thought
- one joke or evidence object
- one WIT reaction or real-life object
- one readable label
- one clean timing beat

If a board needs three explanations, it is probably three boards.

## Board Types

Use these repeatedly:

- Situation board: show the normal thing.
- Suspicion board: reveal the weird detail.
- Correction board: cross out the naive explanation.
- Mechanism board: show how the system works.
- Evidence board: show concrete object, number, or example.
- Reaction board: let WIT show how it feels.
- Payoff board: make the final insight visible.

## Motion Rule

Use hard cuts by default.

Add motion only when it has a job:

- reveal
- emphasis
- joke timing
- visual cause/effect
- helping the viewer follow a change

Do not animate labels, props, WIT, and transitions all at once unless the user has approved the static frame.

## Reference Board Rule

Before full visual production, ask:

`What does this topic look like in real life, and what would make it funny if paused?`

Every normal section visual plan should include a real visual reference pass. Start with real internet images, self-shot images, or inspected local assets whenever the topic has real-world objects. Use generated images after that to fill gaps, create safer controllable mockups, remove logos/private data, or test composition. Prompt-only references are a fallback only when browsing, generation, or local inspection is unavailable, fails, or would create unsafe assets.

Good reference boards collect:

- real-life objects
- real internet/self-shot/local images that make the video feel close to the viewer
- UI patterns or self-made mockups
- visual metaphors
- thumbnail tension
- WIT emotion
- color and contrast references
- source notes

References must be classified:

- safe asset
- mockup target
- inspiration only
- reject

Do not copy another creator's exact frame, thumbnail, screenshot, or joke layout.

## Real-Life Asset Rule

Use real-life assets as evidence, not decoration.

Prefer:

- self-shot images
- licensed or public-domain images
- real internet images with clear source and license notes
- generated images for support, cleanup, or missing-safe-asset cases
- self-made UI mockups
- simple object cutouts
- paper, receipts, bills, phones, desks, product boxes

Avoid:

- private data
- unclear copyrighted images
- pixel-copied app screens
- real logos unless there is a specific approved reason
- generic stock images that do not explain the point

Channel-wide reusable assets should be rare and high-value. Most video-specific assets belong inside `projects/<slug>/assets/`.

## Visual Humor Patterns

Use a small set per video:

- red cross-out
- bad arrow
- fake diagram
- real object with stupid label
- WIT physically suffering
- hidden thing revealed behind clean thing
- list that gets more absurd
- tiny legal footnote
- suspicious asterisk
- impossible receipt
- progress bar of bad decisions

Do not throw every pattern into one video.

## WIT Use

Use `.agents/_shared/channel/brand-system.md` for the current WIT direction.

WIT is useful when:

- the system needs a human victim
- the board needs emotional clarity
- the joke needs a dry reaction
- a thumbnail needs instant feeling

WIT should not block labels or replace the explanation.

## HyperFrames Board Guidance

Use:

- simple HTML/CSS scenes
- stable board dimensions
- large readable text
- handwritten-looking fonts or rough labels
- hard cuts
- cue-timed popups only when needed

Check:

- text fits on desktop and mobile review sizes
- labels are readable when paused
- WIT emotion is visible at small size
- real-life assets are not muddy or decorative
- cue-critical elements are readable on the cue frame, not only starting animation there

## Short Hook Simplicity Rule

For a `20-30s` hook, start with `6-8` static boards:

- one real-life image or object
- one WIT reaction
- one main label
- hard cuts

Do not add transition overlays, rapid pop-ins, object pile-ons, or WIT shake unless the static version is approved and the motion has a clear joke or clarity job.
