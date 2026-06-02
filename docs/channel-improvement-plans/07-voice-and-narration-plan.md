# Plan 07: Voice And Narration

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide voice and narration system so all future narration sounds clear, deadpan, and human while remaining easy for English learners.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable voice and narration system for the entire channel. It must not edit active video voiceover text or generate voice for a specific video.

Allowed outputs:

- `common/voice/narration-system.md`
- `common/voice/script-markup-guide.md`
- `common/voice/voice-test-protocol.md`

Forbidden outputs:

- no edits to active video voiceover text
- no regenerating voiceover for any existing video
- no edits to `video-projects/<slug>/`

## Problem

David23 is clear and learner-friendly, but narration can sound too sincere or too generated.

Weaknesses:

- Punchlines may not have enough pause.
- The tone may feel like a helpful explainer.
- The voice may not sound unimpressed enough.
- The rhythm may not separate setup and punchline.

## Target

Narration should feel like:

`a calm person explaining something ridiculous while refusing to act surprised`

## Delivery Rules

- Keep pronunciation clear.
- Keep pace moderate.
- Pause before punchlines.
- Lower emotional exaggeration.
- Let absurd lines stay dry.
- Avoid sounding excited about every point.
- Avoid dramatic trailer-style energy.

## Script Markup System

Before generating voiceover, mark the script:

- `[pause]` for short pause
- `[beat]` for punchline beat
- `[deadpan]` for flatter delivery
- `[slower]` for learner clarity
- `[emphasis]` for key word

Example:

```text
Free apps are not lying. [pause]
They are just very patient. [beat]
```

## Voice Testing Workflow

1. Select the first `45-60` seconds.
2. Generate `2-3` narration variants.
3. Compare clarity, deadpan feel, and joke timing.
4. Test with the first `10` second visual hook.
5. Pick the voice style before full production.
6. Generate full voice only after the script is locked.

## Timing Rules

- Key joke label should appear on or just before the punchline word.
- Do not let visual punchlines arrive too early.
- Do not rush final insight.
- Give English learners time to read key labels.

## Acceptance Criteria

Narration is ready if:

- the voice is easy to understand
- jokes have breathing room
- punchlines do not sound overacted
- the voice does not feel corporate
- timing can drive board cuts naturally
- the first `30` seconds feels like a real creator, not a tutorial

## Do Not Do

- Do not imitate Casually Explained's exact voice.
- Do not sacrifice learner clarity for sarcasm.
- Do not use a voice that sounds old, raspy, or too dramatic unless explicitly approved.
- Do not render full video before the voice test passes.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/07-voice-and-narration-plan.md.
Create or update the channel-wide narration system.
Allowed outputs are common/voice/narration-system.md, common/voice/script-markup-guide.md, and common/voice/voice-test-protocol.md.
Do not edit video-projects.
Do not prepare a specific script for narration unless I explicitly ask.
```
