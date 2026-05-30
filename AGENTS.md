# Why It Works Project Instructions

This workspace is the long-term memory for the `Why It Works` YouTube channel.

New Codex sessions do **not** have the full prior chat history, so they must rebuild context from the project files before making strategic decisions.

## Required Startup Routine

At the start of any new session in this workspace, read these files in order:

1. [README.md](C:\ME\THINGS\Build a Channel\README.md)
2. [docs/current-state.md](C:\ME\THINGS\Build a Channel\docs\current-state.md)
3. [docs/channel-foundation.md](C:\ME\THINGS\Build a Channel\docs\channel-foundation.md)
4. [docs/channel-guardrails.md](C:\ME\THINGS\Build a Channel\docs\channel-guardrails.md)
5. [docs/reference-channels.md](C:\ME\THINGS\Build a Channel\docs\reference-channels.md)
6. [docs/learning-log.md](C:\ME\THINGS\Build a Channel\docs\learning-log.md)
7. [docs/codex-collaboration.md](C:\ME\THINGS\Build a Channel\docs\codex-collaboration.md)

Do this before:

- changing strategy
- suggesting a pivot
- writing new persistent notes
- creating scripts or brand assets that depend on channel identity

## Memory Rules

- Treat the docs as the source of truth, not the current chat alone
- Preserve prior strategic decisions unless the user explicitly changes them
- If the current chat conflicts with the docs, pause and clarify before overwriting core decisions
- Keep new persistent notes short, structured, and reusable

## Persistence Rules

Use the project docs intentionally:

- `video-projects/<slug>/` for active per-video work and production decisions
- `common/` for reusable tools, templates, local skills, shared assets, and production conventions
- `docs/channel-foundation.md` for stable strategy
- `docs/current-state.md` for the latest compact summary
- `docs/reference-channels.md` for inspiration and benchmarks
- `docs/learning-log.md` for experiments, lessons, and dated changes
- `docs/channel-guardrails.md` for safety checks

## Project-Local Skills

- Use [WIW Take Note](C:\ME\THINGS\Build a Channel\.agents\skills\wiw-take-note\SKILL.md) when the user asks to take note of reviews, remember useful production feedback, or persist lessons that should improve future HyperFrames/video review passes.

## Workspace Boundaries

- One video project belongs in one folder under `video-projects/`
- Reusable systems belong in `common/`
- Channel-level strategy and memory belong in `docs/`
- HyperFrames is now the default video production and rendering path
- The old Remotion app remains in `remotion-studio/` temporarily for reference; do not delete or edit it unless explicitly asked

For active videos, write decisions into the relevant `video-projects/<slug>/` file before moving to the next workflow step.

## Safety Gate

Before writing any strategic idea into the project docs, classify it as:

- `Core`
- `Experiment`
- `Reject`

Only `Core` belongs in the channel foundation.
`Experiment` belongs in the learning log with a clear label.
`Reject` should not be persisted.

## Current Project Identity

- Channel name: `Why It Works`
- Primary language: `English`
- Format: `no-face explainer channel`
- Main audience lens: `English learners`
- Main lane: `money, internet, society, business, and modern life`
- Tone: `smart, simple, funny, dry`
- Default video text style: `handwritten labels and captions rendered through HyperFrames`

## Main Goal

Build a durable English-first no-face explainer brand for English learners that can later support products, including Deewas, without turning the channel into direct app promotion too early.
