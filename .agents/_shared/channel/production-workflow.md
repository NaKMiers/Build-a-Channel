# Production Workflow

Classification: `Core operational structure`

Scope: `CHANNEL_WIDE`

This is the compact workflow source of truth for `Why It Works`.

## Folder Rule

- Channel-wide memory and reusable systems live in `.agents/_shared/`.
- Executable skills live in `.agents/skills/`.
- One video project lives in one folder under `projects/<slug>/`.
- Active production decisions belong in the relevant `projects/<slug>/` file before moving to the next step.

## Sequential Pipeline

The video pipeline is:

```text
00-topic-intake.md
01-research-pack.md
02-script.md
03-packaging.md
04-voiceover.md
05-visual-plan.md
06-review.md
07-upload.md
08-self-learning.md
```

Current executable steps:

- `topic-intake` creates or updates `00-topic-intake.md`.
- `research-pack` requires `00-topic-intake.md` and writes `01-research-pack.md`.
- `script-draft` requires `00-topic-intake.md` and `01-research-pack.md`, then writes `02-script.md`.
- `packaging` requires `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`, then writes `03-packaging.md`.
- `voiceover` requires `03-packaging.md`, then writes `04-voiceover.md` and section voiceover files.

Pipeline rules:

- Step `N` requires all previous step outputs.
- If a required output is missing, stop and tell the user which skill to run first.
- Rerunning an earlier step makes later outputs stale.
- Remove stale downstream outputs only by explicit user request, or regenerate them by rerunning later skills in order.

## Startup Read Set

Before strategy, production, or persistent memory changes, read:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`
4. `.agents/_shared/channel/channel-foundation.md`
5. `.agents/_shared/channel/channel-guardrails.md`
6. `.agents/_shared/channel/reference-channels.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`

For production work, also use the four compact systems:

- `.agents/_shared/systems/topic-packaging-hooks.md`
- `.agents/_shared/systems/script-learner-voice.md`
- `.agents/_shared/systems/visual-production.md`
- `.agents/_shared/systems/audio-feedback-quality.md`

## Quality Gates

Use lightweight gates instead of many separate checklists:

- Topic angle: the angle must combine topic, contradiction, visual metaphor, and viewer pain.
- Packaging: title and thumbnail must create curiosity without fake claims.
- Hook: the first `10` seconds must show the situation, contradiction, WIT emotion, and bigger question.
- Script: the script must teach the topic first and stay learner-friendly by design.
- Visuals: each board must carry one thought, one readable label, and one clear joke or evidence job.
- Audio: narration is the product; music and sound effects are support.
- Review: paused frames should be understandable, readable, and worth looking at.
- Learning: after publishing, record only reusable lessons.

## HyperFrames Rule

HyperFrames is the active rendering path.

Use simple board scenes, WIT poses, voiceover, hard cuts, cue-timed labels, red markup, and handwritten-looking text. Prefer clear static boards before adding motion.

Legacy Remotion notes are historical only. Do not revive Remotion production unless the user explicitly asks.

## Browsing Rule

Use the project-local `browse` skill for web or YouTube browsing when available. Fall back to global gstack `/browse` only if the project-local skill cannot run. Do not use other browser tools unless the user explicitly approves a fallback.

