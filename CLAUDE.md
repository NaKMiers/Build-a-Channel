# Why It Works Project Instructions

This workspace is the long-term memory for the `Why It Works` YouTube channel.

It is configured for **both Codex and Claude**. The shared brain, rules, and skill
logic live once under `.agents/` and are read by both tools. This file is Claude's
auto-loaded entry point; `AGENTS.md` is the Codex equivalent. Keep them in sync when
you change strategy, startup routine, or workflow rules.

New sessions do not have the full prior chat history, so they must rebuild context from
the project files before making strategic or production decisions.

## Required Startup Routine

At the start of any new session in this workspace, read these files in order:

1. [README.md](README.md)
2. [.agents/rules/README.md](.agents/rules/README.md)
3. [.agents/_shared/channel/current-state.md](.agents/_shared/channel/current-state.md)
4. [.agents/_shared/channel/channel-foundation.md](.agents/_shared/channel/channel-foundation.md)
5. [.agents/_shared/channel/channel-guardrails.md](.agents/_shared/channel/channel-guardrails.md)
6. [.agents/_shared/channel/reference-channels.md](.agents/_shared/channel/reference-channels.md)
7. [.agents/_shared/channel/learning-log.md](.agents/_shared/channel/learning-log.md)
8. [.agents/_shared/channel/codex-collaboration.md](.agents/_shared/channel/codex-collaboration.md)

Do this before:

- changing strategy
- suggesting a pivot
- writing new persistent notes
- creating scripts or brand assets that depend on channel identity
- creating or updating production skills

## Browsing Rule

Use the gstack `/browse` skill for all web or YouTube browsing.

If a project-local browse skill exists at `.agents/skills/browse/SKILL.md`, it is vendored
from gstack so the project can travel across machines; prefer it when present. Otherwise
fall back to the global gstack `/browse` skill.

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
- `.agents/rules/` for operating rules that all agents and future skills must follow
- `.agents/skills/` for the canonical skill definitions (logic + per-skill memory)
- `.claude/skills/` for Claude discovery wrappers that delegate to `.agents/skills/`

## Skills

Skills are defined once under `.agents/skills/<name>/`. Claude discovers them through thin
wrappers under `.claude/skills/<name>/SKILL.md` that delegate to the canonical definition.
When you run a skill, follow the canonical `.agents/skills/<name>/SKILL.md` and read/update
that skill's `.agents/skills/<name>/references/memory.md` — never a Claude-side copy.

- Use `/browse` for web or YouTube browsing, especially reference video research for topic intake.
- Use **topic-intake** when the user asks for topic intake, next video ideas, raw topic candidates, scored video angles, or step 0 of the video workflow.
- Use **research-pack** when the user asks for research pack, evidence pack, source gathering, visual reference research, or step 1 of the video workflow.
- Use **script-draft** when the user asks for script draft, a sectioned script, writing the video script, or step 2 of the main video workflow.
- Use **packaging** when the user asks for title, thumbnail, packaging, YouTube description, tags, hashtags, upload metadata, or the packaging side branch. Packaging requires only topic intake and research pack; it is outside the main production pipeline.
- Use **voiceover** when the user asks for section voiceover, generate audio for a script section, create narration audio, all section voiceovers, or step 4 of the main video workflow.
- Use **visual-plan** when the user asks for visual plan, section scene plan, real-life visual references, generated visual references, HyperFrames build guidance, or step 5 of the main video workflow.
- Use **render** when the user asks for render, HyperFrames build, create video from visual plan, section preview, localhost preview, section MP4 render, or step 6 of the main video workflow.
- Use **auto-adjust** after render when the user asks to auto-adjust, audit, QA, automatically fix a rendered section, apply Section 1/2 review lessons, preserve manual Studio edits, or prepare one selected section for review. Auto Adjust requires one project and one section; it has no `All` option.
- Use **combine** (final workflow step) when the user asks to combine, combine sections, unify, assemble the full video, build the full render, merge sections into one video, or run on `localhost:1000`. Combine requires one project and that ALL sections are already rendered; it reuses the existing section renders + assets and only assembles them into one unified preview on port `1000` with a single combined voiceover. It never re-renders, edits, or creates section content, and never exports MP4/WebM.
- Use **skill-sync** (utility, outside the pipeline gate) when the user asks to sync skills between Codex and Claude, reconcile the `.claude/skills/` wrappers, or sync `AGENTS.md` and `CLAUDE.md`. Manual only; run only when asked.
- Do not create additional sequential video-production skills until the user explicitly asks for the next skill-creation phase.

Pipeline gate:

- main production skills run in order: `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> auto-adjust -> review -> combine -> upload -> learning`
- `combine` is the final, project-level assembly step: it runs once after EVERY section is rendered, requires one project (named or smart-selected), reuses the existing section renders/assets without changing them, produces only the unified preview on `localhost:1000`, and never exports MP4/WebM
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
- Agent and skill rules belong in `.agents/rules/`.
- Canonical skill definitions belong in `.agents/skills/`; Claude discovery wrappers in `.claude/skills/`.
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
