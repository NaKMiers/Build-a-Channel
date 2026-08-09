---
name: scenes
description: Turn a timestamped HumanPrice transcript and locked cast into a visual plan plus one detailed image prompt per timestamp. Use for scenes, image prompts, visual planning, or prompts for every narration cue.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# scenes

Creates the HumanPrice scene plan and generation prompts. It writes text only.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/visual-style.md`
- `.agents/rules/cast-identity.md`
- `.agents/rules/file-formats.md`
- `.agents/rules/image-generation.md`
- `.agents/skills/scenes/references/memory.md`

## Inputs and hard gates

Resolve one project. Require:

- `transcribes/transcript.md` with ordered `[M:SS] narration` cues;
- `prompts/character-prompts.md` with 2 to 6 stable handles;
- `brand/PROTAGONIST.jpeg` when the cast declares it required.

Do not infer timestamps from the script. Do not proceed with an unlocked recurring
protagonist.

## Plan the episode

Read the entire transcript and map its reveal ladder. Write `prompts/visual-plan.md` with:

- the visual thesis and recurring economic symbols;
- surface, register, and density distribution;
- 4 to 7 build chains and their locked base plates;
- cast continuity notes;
- pacing notes for the hook, mechanisms, evidence, and ending;
- any claims that must stay symbolic because generated text would be unreliable.

Target 180 to 320 visual states for an 8 to 12 minute episode. Every transcript timestamp
must receive one prompt. A build variant counts as a visual state but must retain the
same plate composition.

## Write image prompts

Write `prompts/image-prompts.md` in timestamp order. Every block must:

- reproduce the transcript cue exactly;
- name register, density tier, and surface family;
- state the one visual claim;
- describe composition, cast handles, actions, props, lighting, and negative space;
- explain the visual change when it belongs to a build chain;
- end with the exact style and generation strings from `visual-style.md`.

Use `---` only as a chain break according to `image-generation.md`. Never place it
between variants that must share a plate. No generated labels, factual tiny text, logos,
watermarks, photorealism, or literal coin mascot.

## Validate

Confirm one prompt per timestamp, exact chronological order, valid handles, nonempty
style strings, and no chain discontinuity. Report file paths and prompt count.

Then say: `Next: generate the scene images, then run /scene-polish.`

## Self-improvement

Append durable prompt or continuity lessons to `references/memory.md`.
