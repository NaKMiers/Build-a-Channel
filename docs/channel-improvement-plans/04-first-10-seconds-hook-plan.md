# Plan 04: First 10 Seconds Hook

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide first `10` seconds system so every future video opens as a curiosity event, not a polite introduction.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable hook system for the entire channel. It must not design or edit the opening of any specific video.

Allowed outputs:

- `common/hook-system.md`
- `common/hook-templates/first-10-seconds-board-template.md`
- `common/hook-templates/hook-scorecard.md`

Forbidden outputs:

- no edits to active video compositions
- no edits to `video-projects/<slug>/`
- no first-10-seconds plan for a specific existing video

## Problem

The current opening style can be clear but too calm.

Weaknesses:

- It may explain before it creates suspicion.
- It may start like a title card instead of a situation.
- It may use clean text instead of a strong visual contradiction.
- It may not immediately prove the thumbnail promise.

## Target

The first `10` seconds should do four jobs:

1. Show the topic.
2. Show the contradiction.
3. Show WIT's emotional position.
4. Create a reason to keep watching.

## Hook Formula

Use this pattern:

`normal thing -> suspicious detail -> WIT reaction -> bigger question`

Example pattern:

1. A normal object promises something easy.
2. A suspicious cost appears behind it.
3. WIT stares at the viewer.
4. Narrator turns the object into a bigger question.

## First 10 Seconds Board Template

### Board 1: Topic Object

Duration:
`0:00-0:03`

Visual:
one clear object connected to the topic.

Text:
one phrase only.

### Board 2: Contradiction

Duration:
`0:03-0:06`

Visual:
something that should not be there.

Text:
short correction or suspicious label.

### Board 3: WIT Reaction

Duration:
`0:06-0:08`

Visual:
WIT reacts to the contradiction.

Text:
optional, `?`, `wait`, `later`, or red marker note.

### Board 4: Video Promise

Duration:
`0:08-0:10`

Visual:
the full question becomes clear.

Text:
the key phrase for the video.

## Hook Rules

- Use hard cuts unless one tiny motion is the joke.
- Do not introduce too many objects.
- Do not explain all mechanisms yet.
- Do not use long sentences on screen.
- Do not show a complex dashboard.
- Do not make WIT neutral.
- Do not spend the first `10` seconds on branding.

## Script Hook Rules

The first spoken lines should:

- be simple
- be specific
- sound like a person
- contain a contradiction
- avoid slow background explanation

Weak:

`In today's video, we are going to explain how free apps make money.`

Better:

`Modern life keeps offering convenience, and somehow your wallet still looks nervous.`

## Acceptance Criteria

The hook is ready if:

- The topic is clear with no audio.
- The contradiction is visible with no audio.
- The viewer has a question by second `5`.
- The thumbnail promise appears by second `10`.
- WIT's role is obvious.
- The scene can be understood on mobile.

## Testing Method

1. Export only the first `10` seconds.
2. Watch without sound.
3. Watch at `25%` size.
4. Pause at seconds `1`, `3`, `6`, and `9`.
5. Ask whether each paused frame is interesting.
6. Only continue production if the hook passes.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/04-first-10-seconds-hook-plan.md.
Create or update the channel-wide first 10 seconds hook system.
Allowed outputs are common/hook-system.md and common/hook-templates/.
Do not edit video-projects.
Do not design the opening for a specific video unless I explicitly ask.
```
