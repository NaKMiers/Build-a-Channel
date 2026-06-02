# Plan 08: Music And Sound

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide music and sound system that supports dry humor without overpowering narration.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable music and sound system for the entire channel. It must not create a sound direction for any specific video.

Allowed outputs:

- `common/music-and-sound-system.md`
- `common/sound-effects-library/README.md`
- `common/audio-mixing-checklist.md`

Forbidden outputs:

- no edits to active video audio
- no edits to `video-projects/<slug>/`

## Problem

Music can accidentally make the channel feel:

- too corporate
- too cinematic
- too motivational
- too polished
- too serious

Casually Explained-style humor works better when music stays under the joke.

## Target Sound

The track should feel:

- light
- simple
- slightly playful
- slightly suspicious when needed
- low enough that narration dominates

The track should not feel:

- epic
- emotional
- inspirational
- luxury finance
- startup ad
- documentary trailer

## Music Selection Rules

Choose tracks with:

- simple rhythm
- minimal vocals
- low emotional drama
- no heavy bass
- no sudden drops
- loopable structure
- room for narration

## Sound Effect Rules

Use small sound effects only when they help a joke:

- receipt printer
- phone buzz
- notification pop
- red marker scribble
- tiny cash register
- paper slap
- lock click
- timer jump

Avoid:

- too many effects
- cartoon overload
- loud whooshes
- dramatic impacts
- effects that distract from words

## Mixing Rules

- Narration must be the clearest layer.
- Music should stay low.
- Lower music during dense explanation.
- Let silence or near-silence land some punchlines.
- Sound effects should be short and quiet.

## Workflow

1. Define emotional mode of video.
2. Pick `3` candidate tracks.
3. Test each under the first `30` seconds.
4. Reject anything too corporate or cinematic.
5. Add only essential sound effects.
6. Check audio on speakers and headphones.
7. Confirm English learner clarity.

## Acceptance Criteria

Audio is ready if:

- narration remains clear at low volume
- music does not make the video feel like an ad
- sound effects land jokes without clutter
- the track can loop without becoming annoying
- the audio supports the channel's dry tone

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/08-music-and-sound-plan.md.
Create or update the channel-wide music and sound system.
Allowed outputs are common/music-and-sound-system.md, common/sound-effects-library/, and common/audio-mixing-checklist.md.
Do not edit video-projects.
Do not create a music direction for one specific video unless I explicitly ask.
```
