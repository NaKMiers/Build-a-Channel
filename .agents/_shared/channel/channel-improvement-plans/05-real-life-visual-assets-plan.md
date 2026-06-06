# Plan 05: Real-Life Visual Assets

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide real-life visual asset system so future videos mix rough drawings with real or real-looking assets.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable real-life asset system for the entire channel. It must not create a reference board or asset list for one specific video.

Allowed outputs:

- `.agents/_shared/real-life-visual-asset-system.md`
- `.agents/_shared/assets/real-life/`
- `.agents/_shared/assets/ui-mockups/`
- `.agents/_shared/assets/source-note-template.md`

Forbidden outputs:

- no edits to `projects/<slug>/`
- no video-specific asset board

## Problem

The current visual style can become too abstract.

Weaknesses:

- Cards and labels explain the system but do not always feel lived-in.
- The viewer may not recognize their own phone, bills, apps, or daily behavior.
- Scenes can feel like clean diagrams rather than funny evidence.

## Target

Every video should feel like:

`rough drawings commenting on real life`

not:

`a clean slide deck about real life`

## Asset Categories

Build or collect assets from safe sources:

- self-shot photos
- generated images
- public-domain or licensed images
- self-made UI mockups
- simple screenshots recreated as mockups
- scanned paper textures
- receipt photos
- phone photos
- rough object cutouts

## Default Asset Types

For money topics:

- receipts
- wallets
- payment terminals
- bills
- subscription cards
- bank app mockups
- price tags

For internet topics:

- phone screens
- notifications
- feed mockups
- app-store-style screens
- fake profile cards
- comment sections
- browser windows

For modern-life topics:

- desks
- calendars
- checklists
- moving boxes
- delivery bags
- cluttered rooms
- tired worker silhouettes

## Visual Mix Rule

For each `3-5` minute video:

- use WIT regularly
- use handwritten text constantly
- use real or real-looking assets every `10-15` seconds
- use red marker only for corrections and reveals
- use simple drawings when real assets would distract

## Asset Workflow

1. Define the video's recurring metaphor.
2. List `20` possible real-life objects.
3. Select `8-12` that can appear in the video.
4. Decide which assets need to be real, generated, or mocked.
5. Create a visual reference board.
6. Build cutout-ready assets.
7. Test each at `1920x1080` and mobile scale.
8. Place assets into the video folder.
9. Document asset source and usage notes.

## Safety Rules

- Do not use copyrighted images without a safe plan.
- Do not use real private information.
- Do not show real personal account data.
- Do not use actual app logos unless necessary and defensible.
- Prefer fake UI that clearly represents the idea.

## Acceptance Criteria

A visual asset pass is successful if:

- At least one asset makes the viewer think, `this is my life`.
- The video does not feel like only cards and labels.
- Assets support jokes instead of decorating.
- Real-life texture does not reduce learner clarity.
- Assets are safe to use and stored locally.

## Example Asset Pattern

For any topic, define:

- one real-world object the viewer recognizes
- one hidden-cost object
- one UI or paper mockup
- one physical consequence for WIT
- one red correction asset

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read .agents/_shared/channel/channel-improvement-plans/05-real-life-visual-assets-plan.md.
Create or update the channel-wide real-life visual asset system.
Allowed outputs are .agents/_shared/real-life-visual-asset-system.md and reusable .agents/_shared/assets folders.
Do not edit projects.
Do not create a visual asset board for one specific video unless I explicitly ask.
```
