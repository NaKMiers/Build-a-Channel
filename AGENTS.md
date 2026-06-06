# Why It Works Project Instructions

This workspace is the long-term memory for the `Why It Works` YouTube channel.

New Codex sessions do not have the full prior chat history, so they must rebuild context from the project files before making strategic or production decisions.

## Required Startup Routine

At the start of any new session in this workspace, read these files in order:

1. [README.md](C:\ME\THINGS\Build a Channel\README.md)
2. [.agents/rules/README.md](C:\ME\THINGS\Build a Channel\.agents\rules\README.md)
3. [.agents/_shared/channel/current-state.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\current-state.md)
4. [.agents/_shared/channel/channel-foundation.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\channel-foundation.md)
5. [.agents/_shared/channel/channel-guardrails.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\channel-guardrails.md)
6. [.agents/_shared/channel/reference-channels.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\reference-channels.md)
7. [.agents/_shared/channel/learning-log.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\learning-log.md)
8. [.agents/_shared/channel/codex-collaboration.md](C:\ME\THINGS\Build a Channel\.agents\_shared\channel\codex-collaboration.md)

Do this before:

- changing strategy
- suggesting a pivot
- writing new persistent notes
- creating scripts or brand assets that depend on channel identity
- creating or updating production skills

## Memory Rules

- Treat `.agents/_shared/` as the channel brain.
- Treat `projects/<slug>/` as the source of truth for one video's active work.
- Preserve prior strategic decisions unless the user explicitly changes them.
- If the current chat conflicts with the shared memory, pause and clarify before overwriting core decisions.
- Keep new persistent notes short, structured, and reusable.

## Persistence Rules

Use the project folders intentionally:

- `projects/<slug>/` for active per-video work and production decisions
- `.agents/_shared/channel/` for stable channel strategy, guardrails, references, current state, and learning log
- `.agents/_shared/` for reusable production systems, templates, shared assets, tools, voice notes, and workflows
- `.agents/rules/` for operating rules that Codex and future skills must follow
- `.agents/skills/` for executable project-local Codex skills only

## Project-Local Skills

- Use [WIW Take Note](C:\ME\THINGS\Build a Channel\.agents\skills\wiw-take-note\SKILL.md) when the user asks to take note of reviews, remember useful production feedback, or persist lessons that should improve future HyperFrames/video review passes.
- Do not create the sequential video-production skills until the user explicitly asks for the skill-creation phase.

## Workspace Boundaries

- One video project belongs in one folder under `projects/`.
- Reusable channel memory belongs in `.agents/_shared/`.
- Codex and skill rules belong in `.agents/rules/`.
- Executable skills belong in `.agents/skills/`.
- HyperFrames is the default video production and rendering path.
- Legacy Remotion notes live in `.agents/_shared/remotion/`; do not revive, delete, or edit legacy Remotion production unless explicitly asked.

For active videos, write decisions into the relevant `projects/<slug>/` file before moving to the next workflow step.

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
