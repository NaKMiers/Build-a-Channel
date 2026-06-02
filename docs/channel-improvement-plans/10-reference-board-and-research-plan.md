# Plan 10: Reference Board And Research

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide reference-board and research system so every future video becomes visually and comedically specific before scripting or production.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable reference-board research system for the entire channel. It must not create references for any specific video project.

Allowed outputs:

- `common/reference-board-system.md`
- `common/reference-boards/README.md`
- `common/reference-boards/_template/`

Forbidden outputs:

- no edits to `video-projects/<slug>/`
- no active-video reference board

## Problem

Without a reference board, videos can become generic:

- abstract labels
- clean cards
- repeated WIT poses
- obvious metaphors
- safe thumbnails

Casually Explained feels specific because it uses weird, concrete evidence:

- real photos
- rough maps
- ugly diagrams
- awkward screenshots
- surprising cutouts
- simple labels on real-world objects

## Target

Before production, each video should have a small reference board that answers:

`What does this topic look like in real life?`

and:

`What would make this topic funny if paused?`

## Reference Board Contents

For each video, collect:

- `5` real-life object references
- `5` UI or screenshot references
- `5` visual metaphor references
- `5` thumbnail references
- `5` WIT emotion references
- `3` color/contrast references

Total target:
`20-30` useful references.

## Research Categories

### Topic Reality

Find what the issue looks like in the real world.

Examples:

- bills
- receipts
- notifications
- checkout pages
- calendars
- workplace dashboards
- app screens

### Comedy Objects

Find objects that can become jokes.

Examples:

- receipt printer
- red marker
- moving boxes
- fake warning sign
- tiny lock
- sad wallet
- angry phone

### Viewer Recognition

Find visuals viewers instantly understand.

Examples:

- `low battery`
- `free trial`
- `storage full`
- `streak lost`
- `payment failed`
- `subscribe to continue`

### Thumbnail Tension

Find one-frame contradictions.

Examples:

- `FREE` button plus bill
- `productivity` checklist crushing WIT
- `cheap` product leaking parts
- `budget` notebook on fire

## Workflow

1. Read the topic idea.
2. Write the main contradiction.
3. List real-life objects connected to the contradiction.
4. Build a local reference board folder.
5. Save only safe-to-use or inspiration-only references.
6. Write source notes.
7. Pick the recurring motif.
8. Use the board to write thumbnail, hook, and script.

## File Structure

For channel-wide templates:

```text
common/reference-boards/_template/
  README.md
  thumbnails/
  real-life/
  ui-mockups/
  visual-metaphors/
  wit-emotions/
```

For reusable references:

```text
common/reference-boards/
```

## Acceptance Criteria

The reference board is ready if:

- it suggests a thumbnail
- it suggests the first `10` seconds
- it suggests at least `5` visual jokes
- it contains real-life texture
- it avoids copying another creator's exact frame
- it helps the video feel specific

## Do Not Do

- Do not collect references only for aesthetics.
- Do not copy final layouts directly.
- Do not use references without source notes.
- Do not skip packaging research because the topic sounds obvious.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/10-reference-board-and-research-plan.md.
Create or update the channel-wide reference-board system.
Allowed outputs are common/reference-board-system.md and common/reference-boards/.
Do not edit video-projects.
Do not create a reference board for a specific topic unless I explicitly ask.
Use /browse for web research only if live references are needed.
```
