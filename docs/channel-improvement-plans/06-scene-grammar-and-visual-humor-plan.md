# Plan 06: Scene Grammar And Visual Humor

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide repeatable visual grammar that makes simple scenes funny, clear, and fast to produce across all future videos.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable scene grammar system for the entire channel. It must not turn a specific script into boards.

Allowed outputs:

- `common/scene-grammar-system.md`
- `common/visual-humor-patterns.md`
- `common/hyperframes/board-grammar.md`

Forbidden outputs:

- no edits to `video-projects/<slug>/`
- no per-video board plan

## Source Pattern

From the reference analysis:

`static drawing -> narration twist -> hard cut or red markup -> next static drawing`

The video feels alive because the idea changes at the right moment, not because everything moves constantly.

## Problem

The current production can drift toward:

- too many clean boards
- too many abstract labels
- too many full-sentence text blocks
- movement without joke value
- scene changes that explain but do not surprise

## Target

Every scene should have:

- one thought
- one visual joke or clear example
- one WIT reaction or one real-life object
- one readable text label
- one clean timing beat

## Default Scene Pattern

Use this pattern often:

1. Show what people think.
2. Red-correct it.
3. Show what is actually happening.
4. Let WIT react.
5. Cut to next example.

Example pattern:

`OBVIOUS MEANING`

red cross-out

`REAL MEANING`

WIT suspicious

## Visual Humor Types

Use these repeatedly:

- red cross-out
- bad arrow
- fake diagram
- real photo with stupid label
- WIT physically suffering
- object behaving like a person
- hidden thing revealed behind a clean thing
- list that gets more absurd
- tiny legal footnote
- before/after contradiction

## Board Count Guidance

For a `3-5` minute video:

- first `10` seconds: `4` boards
- each `20-30` second section: `3-6` boards
- full video: roughly `45-75` meaningful boards

Do not split every spoken phrase into a separate board.
Use timed labels inside one board when the idea is connected.

## Motion Rules

Allowed motion:

- red marker draw
- small pop-in label
- tiny WIT shake
- receipt printing
- phone buzz
- simple reveal
- hard cut

Avoid:

- decorative bouncing
- unnecessary slides
- complex transitions
- constant WIT movement
- object motion that does not land a joke

## On-Screen Text Rules

Prefer:

- `FREE*`
- `later`
- `attention inventory`
- `bad idea`
- `monthly pain`
- `checkout moved`
- `not a gift`

Avoid:

- long subtitle-like explanations
- multiple full sentences on one board
- labels that repeat narration without adding a joke

## Acceptance Criteria

A scene is ready if:

- the paused frame is understandable
- the paused frame has either joke value or clear evidence
- WIT's emotion matches the narration
- text can be read on mobile
- the scene has one main idea
- the cut arrives on the spoken beat

## Review Method

For each rough cut:

1. Pause every `5` seconds.
2. Ask what the frame's joke or evidence is.
3. If the answer is `nothing`, revise the board.
4. Check whether any scene is too clean.
5. Check whether any section has no real-life texture.
6. Check whether WIT is decoration or doing a job.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/06-scene-grammar-and-visual-humor-plan.md.
Create or update the channel-wide scene grammar and visual humor system.
Allowed outputs are common/scene-grammar-system.md, common/visual-humor-patterns.md, and common/hyperframes/.
Do not edit video-projects.
Do not turn a specific script into a board plan unless I explicitly ask.
```
