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

## Browsing Rule

Use the project-local [Browse](C:\ME\THINGS\Build a Channel\.agents\skills\browse\SKILL.md) skill for web or YouTube browsing when available. It is vendored from gstack so the project can travel across machines.

If the project-local browse skill is missing or cannot run, fall back to the global gstack `/browse` skill.

Never use `mcp__claude-in-chrome__*` tools.

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

- Use [Browse](C:\ME\THINGS\Build a Channel\.agents\skills\browse\SKILL.md) for web or YouTube browsing, especially reference video research for topic intake.
- Use [Topic Intake](C:\ME\THINGS\Build a Channel\.agents\skills\topic-intake\SKILL.md) when the user asks for topic intake, next video ideas, raw topic candidates, scored video angles, or step 0 of the video workflow.
- Use [Research Pack](C:\ME\THINGS\Build a Channel\.agents\skills\research-pack\SKILL.md) when the user asks for research pack, evidence pack, source gathering, visual reference research, or step 1 of the video workflow.
- Use [Script Draft](C:\ME\THINGS\Build a Channel\.agents\skills\script-draft\SKILL.md) when the user asks for script draft, a sectioned script, writing the video script, or step 2 of the main video workflow.
- Use [Packaging](C:\ME\THINGS\Build a Channel\.agents\skills\packaging\SKILL.md) when the user asks for title, thumbnail, packaging, YouTube description, tags, hashtags, upload metadata, or the packaging side branch. Packaging requires only topic intake and research pack; it is outside the main production pipeline.
- Use [Voiceover](C:\ME\THINGS\Build a Channel\.agents\skills\voiceover\SKILL.md) when the user asks for section voiceover, generate audio for a script section, create narration audio, all section voiceovers, or step 4 of the main video workflow.
- Use [Visual Plan](C:\ME\THINGS\Build a Channel\.agents\skills\visual-plan\SKILL.md) when the user asks for visual plan, section scene plan, real-life visual references, generated visual references, HyperFrames build guidance, or step 5 of the main video workflow.
- Use [Render](C:\ME\THINGS\Build a Channel\.agents\skills\render\SKILL.md) when the user asks for render, HyperFrames build, create video from visual plan, section preview, localhost preview, section MP4 render, or step 6 of the main video workflow.
- Use [Auto Adjust](C:\ME\THINGS\Build a Channel\.agents\skills\auto-adjust\SKILL.md) after render when the user asks to auto-adjust, audit, QA, automatically fix a rendered section, apply Section 1/2 review lessons, preserve manual Studio edits, or prepare one selected section for review. Auto Adjust requires one project and one section; it has no `All` option.
- Use [WIW Take Note](C:\ME\THINGS\Build a Channel\.agents\skills\wiw-take-note\SKILL.md) when the user asks to take note of reviews, remember useful production feedback, or persist lessons that should improve future HyperFrames/video review passes.
- Do not create additional sequential video-production skills until the user explicitly asks for the next skill-creation phase.

Pipeline gate:

- main production skills run in order: `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> auto-adjust -> review -> upload -> learning`
- packaging is a side branch from `research-pack`
- packaging requires only `00-topic-intake.md` and `01-research-pack.md`
- packaging does not block script, voiceover, visual plan, render, review, upload, or learning
- if a required previous output is missing, stop and ask the user to run the missing skill first
- rerunning an earlier step makes downstream outputs stale
- stale downstream outputs should be removed only by explicit user request or regenerated by rerunning later skills in order
- render uses fixed preview ports: unified preview on `localhost:1000`; section `N` on `localhost:1000 + N`

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

Build a durable English-first no-face explainer brand for English learners that grows influence on the internet through useful, funny explanations of money, internet behavior, business, society, and modern life.
