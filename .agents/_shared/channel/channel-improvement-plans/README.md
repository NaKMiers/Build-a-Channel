# Channel Improvement Plans

Purpose:
channel-wide plans for upgrading the core `Why It Works` creative system closer to the quality bar of the Casually Explained references while preserving the channel's own identity.

Source analysis:

- Casually Explained reference analysis captured in project memory
- Existing `Why It Works` channel docs and production lessons

Classification:
`Core channel upgrade plan`

These plans are for the entire channel.

They are not video-specific instructions.

Default scope:
`CHANNEL_WIDE`

Default output folders:

- `.agents/_shared/channel/`
- `.agents/_shared/channel/channel-improvement-plans/`
- `.agents/_shared/channel/branding/`
- `.agents/_shared/`
- `.agents/_shared/assets/`
- `.agents/_shared/reference-boards/`
- `.agents/_shared/hyperframes/`
- `.agents/_shared/voice/`

Forbidden by default:

- Do not edit `projects/<slug>/`
- Do not rewrite any existing video script
- Do not create per-video implementation files
- Do not apply these plans to any existing video project

Only touch a video project if the user explicitly says:

`Apply this channel-wide system to projects/<slug>`

## Core Standard

The channel should move from:

`clean explainer board`

to:

`funny creator exposing a weird system with simple English, rough visuals, real-life texture, and deadpan timing`

## Master Output

Running these plans should improve the channel operating system itself.

The expected output is a reusable set of standards, libraries, templates, and gates that every future video must use.

It is not a rewrite of one active video.

## Plan Files

0. [00-channel-core-upgrade-contract.md](00-channel-core-upgrade-contract.md)
1. [01-remake-wit-plan.md](01-remake-wit-plan.md)
2. [02-tone-and-script-plan.md](02-tone-and-script-plan.md)
3. [03-thumbnail-packaging-plan.md](03-thumbnail-packaging-plan.md)
4. [04-first-10-seconds-hook-plan.md](04-first-10-seconds-hook-plan.md)
5. [05-real-life-visual-assets-plan.md](05-real-life-visual-assets-plan.md)
6. [06-scene-grammar-and-visual-humor-plan.md](06-scene-grammar-and-visual-humor-plan.md)
7. [07-voice-and-narration-plan.md](07-voice-and-narration-plan.md)
8. [08-music-and-sound-plan.md](08-music-and-sound-plan.md)
9. [09-production-quality-gate-plan.md](09-production-quality-gate-plan.md)
10. [10-reference-board-and-research-plan.md](10-reference-board-and-research-plan.md)
11. [11-comedy-asset-library-plan.md](11-comedy-asset-library-plan.md)
12. [12-english-learner-clarity-plan.md](12-english-learner-clarity-plan.md)
13. [13-topic-angle-selection-plan.md](13-topic-angle-selection-plan.md)
14. [14-publishing-feedback-loop-plan.md](14-publishing-feedback-loop-plan.md)

## Which Plan To Use

Use this quick routing table in future Codex sessions.

| If the task is about... | Start with |
|---|---|
| WIT, character poses, thumbnail reactions | `01-remake-wit-plan.md` |
| Script, humor, deadpan phrasing | `02-tone-and-script-plan.md` |
| Title, thumbnail, clickability | `03-thumbnail-packaging-plan.md` |
| Opening scene, retention start | `04-first-10-seconds-hook-plan.md` |
| Real photos, UI mockups, props | `05-real-life-visual-assets-plan.md` |
| Board timing, visual jokes, scene rhythm | `06-scene-grammar-and-visual-humor-plan.md` |
| Narrator delivery and voiceover prep | `07-voice-and-narration-plan.md` |
| Music, sound effects, mix | `08-music-and-sound-plan.md` |
| Deciding whether production is ready | `09-production-quality-gate-plan.md` |
| Researching visual references | `10-reference-board-and-research-plan.md` |
| Reusable funny props and motifs | `11-comedy-asset-library-plan.md` |
| Keeping videos clear for English learners | `12-english-learner-clarity-plan.md` |
| Choosing what topic angle deserves production | `13-topic-angle-selection-plan.md` |
| Learning from uploads and improving system | `14-publishing-feedback-loop-plan.md` |

## Implementation Prompts

Use [implementation-prompts](implementation-prompts) when opening a new Codex session to execute one of these plans.

Each prompt is written so a future session knows:

- which files to read first
- what constraints to preserve
- what files to create or update
- how to judge whether the plan was implemented correctly

## How Future Codex Sessions Should Use This Folder

Before starting or remaking any video:

1. Read `README.md`.
2. Read `00-channel-core-upgrade-contract.md`.
3. Read the plan files relevant to the task.
4. Build or update the channel-wide system in `.agents/_shared/channel/` or `.agents/_shared/`.
5. Only after the channel-wide system exists, apply it to a new video folder in a separate step.
6. Do not treat any plan as permission to copy Casually Explained exactly.

Before final render:

1. Run the quality gate plan.
2. Check the first `10` seconds.
3. Check thumbnail and title.
4. Check whether WIT has real comedic function.
5. Check whether the video has real-life texture.
6. Check whether the video is still clear for English learners.
7. Check whether the video produced any reusable lesson for the next upload.

## Required Future Workflow

Use this order:

1. Upgrade the channel systems with these plans.
2. Lock reusable standards in `.agents/_shared/channel/` and `.agents/_shared/`.
3. Start or remake a video from scratch using those standards.
4. Do not patch old video files as the implementation of a channel-wide plan.

## Non-Negotiable Quality Bar

A `Why It Works` video is not ready just because it is correct.

It should pass all of these:

- `Clickable`: title and thumbnail create curiosity.
- `Recognizable`: viewers see real life, not only abstract labels.
- `Funny on pause`: most paused frames have a joke, evidence, or strong reaction.
- `Clear`: an intermediate English learner can follow the structure.
- `Distinct`: it borrows roughness from references without copying their identity.
- `Reusable`: at least one asset, phrase, motif, or lesson improves the next video.
