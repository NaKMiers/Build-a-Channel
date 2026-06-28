# Codex Collaboration

This file describes how future Codex sessions should work inside `Why It Works`.

## Role Split

`Codex owns structure, speed, formatting, and reuse.`

`Anh Khoa owns taste, truth, and final judgment.`

## Core Decisions

- Channel name: `Why It Works`
- Primary language: English
- Format: no-face explainer
- Audience lens: English learners, level A2–C1 (advantage: interesting English - entertainment-first; edge allowed, see learning-log.md)
- Lane: money, internet, society, business, and modern life
- Tone: smart, simple, funny, dry
- Renderer: HyperFrames-first

## Startup Routine

Before strategy, production, or memory changes, read:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`
4. `.agents/_shared/channel/channel-foundation.md`
5. `.agents/_shared/channel/channel-guardrails.md`
6. `.agents/_shared/channel/reference-channels.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`

For production work, use:

- `.agents/_shared/channel/production-workflow.md`
- `.agents/_shared/channel/brand-system.md`
- `.agents/_shared/systems/topic-packaging-hooks.md`
- `.agents/_shared/systems/script-learner-voice.md`
- `.agents/_shared/systems/visual-production.md`
- `.agents/_shared/systems/audio-feedback-quality.md`

## Workspace Boundaries

- `projects/`: one folder per video
- `.agents/_shared/channel/`: strategy, state, guardrails, references, collaboration, brand, workflow
- `.agents/_shared/systems/`: reusable production standards
- `.agents/_shared/assets/`: approved reusable channel assets only
- `.agents/skills/`: executable project-local skills
- `.agents/rules/`: Codex operating rules

## Memory Rules

- Keep persistent notes short, structured, and reusable.
- Put active video decisions in `projects/<slug>/`.
- Put reusable lessons in `.agents/_shared/channel/learning-log.md`.
- Put stable production rules in the compact system docs only when they improve future videos.
- Do not create new shared docs unless the user asks or the current compact structure clearly cannot hold the idea.

## Safety Gate

Before writing strategic ideas into project docs, classify them as:

- `Core`
- `Experiment`
- `Reject`

Only `Core` belongs in `channel-foundation.md`.

`Experiment` belongs in `learning-log.md` with a clear label.

`Reject` should not be persisted.

Pause and ask for explicit confirmation before changing foundational identity:

- channel name
- primary language
- no-face format
- main audience
- core promise
- main content pillars
- voice and tone
- product-promotion boundary
- visual identity

## Browsing Rule

Use the project-local `browse` skill for web or YouTube browsing when available. Fall back to global gstack `/browse` only if needed. Do not use other browser tools unless the user explicitly approves a fallback.

## Production Rule

Sequential video-production skills run in order. Step `N` requires all previous project output files. Rerunning an earlier step makes downstream outputs stale.

Do not delete stale downstream outputs unless the user explicitly asks.

