# Plan 00: Channel Core Upgrade Contract

Classification:
`Core channel upgrade contract`

Purpose:
make every plan in this folder upgrade the entire `Why It Works` channel system, not one existing video.

## Default Scope

Every plan in this folder means:

`CHANNEL_WIDE`

It does not mean:

- rewrite an active video
- patch an old script
- create a per-video plan
- edit a file under `projects/`
- apply the change to any existing video project

## Allowed Output Areas

Channel-wide plans may only create or update reusable channel files under:

- `.agents/_shared/channel/`
- `.agents/_shared/channel/channel-improvement-plans/`
- `.agents/_shared/channel/branding/`
- `.agents/_shared/`
- `.agents/_shared/assets/`
- `.agents/_shared/reference-boards/`
- `.agents/_shared/hyperframes/`
- `.agents/_shared/voice/`

## Forbidden Output Areas

Do not edit:

- `projects/`
- any existing video script
- any existing video packaging file
- any existing video HyperFrames composition
- any existing video voiceover text
- any existing video render notes

## Required Implementation Meaning

When a future Codex session runs any numbered plan, it must create or update reusable channel standards, templates, libraries, scorecards, rules, or quality gates.

It must stop after the channel system is improved.

It must not continue into applying that system to a video unless the user gives a separate explicit command.

## Explicit Apply Command

The only phrase that allows video-project edits is:

`Apply this channel-wide system to projects/<slug>`

Without that phrase, `projects/` is out of scope.

## Correct Examples

Correct:

- create `.agents/_shared/script-tone-system.md`
- create `.agents/_shared/script-templates/deadpan-explainer-template.md`
- create `.agents/_shared/thumbnail-packaging-system.md`
- create `.agents/_shared/assets/wit/poses/comedy-core/`
- create `.agents/_shared/production-quality-gate.md`

Incorrect:

- edit `projects/<slug>/02-script.md`
- create any per-video rewrite file
- update a specific video's title
- update a specific video's thumbnail direction
- copy assets into one active video folder

## Future Video Rule

Old video projects may be restarted later, but only after the channel-wide systems exist.

The workflow is:

1. Upgrade the channel core.
2. Lock reusable standards in `.agents/_shared/channel/` and `.agents/_shared/`.
3. Start a new video project or restart an old video from scratch using those standards.
