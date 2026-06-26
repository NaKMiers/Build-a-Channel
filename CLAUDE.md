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
- Use **voiceover** when the user asks for section voiceover, generate audio for a script section, create narration audio, all section voiceovers, or step 3 of the main video workflow.
- Use **visual-plan** when the user asks for visual plan, section scene plan, real-life visual references, generated visual references, HyperFrames build guidance, or step 4 of the main video workflow.
- Use **render** when the user asks for render, HyperFrames build, create video from visual plan, section preview, localhost preview, section MP4 render, or step 5 of the main video workflow.
- Use **combine** (assembly + export step) when the user asks to combine, combine sections, unify, assemble the full video, build the full render, merge sections into one video, export the final video, or run on `localhost:1000`. Combine requires one project and that ALL sections are already rendered; it reuses the existing section renders + assets and only assembles them into one unified preview on port `1000` with a single combined voiceover, then exports the final MP4. It never re-renders, edits, or creates section content. The final video renders to `renders/` as staging, then moves to `projects/<slug>/output/`; `renders/` is removed if left empty. `output/` is the single home for all final deliverables.
- Use **caption** (after combine) when the user asks to create captions, subtitles, an SRT/VTT file, closed captions, caption the video, or generate subtitles for upload. Caption requires one project (named or smart-selected) and a full-length audio source — the combined voiceover (`hyperframes/full-video/combined-voiceover.mp3`) or a full video render; it refuses on per-section audio only and tells the user to run `combine` first. It transcribes the full audio for real word-level timing, uses the exact `02-script.md` text as the caption wording, and exports `captions.srt` (optionally `.vtt`) to `projects/<slug>/output/`. Timing is always from the real audio, never estimated.
- Use **shorts** (side sub-workflow after combine) when the user asks for shorts, vertical shorts, YouTube Shorts, TikTok/Reels clips, cutting shorts from the main video, portrait clips, or splitting the video into shorts. Shorts requires one project whose sections are already built; it has plan/build/export modes, builds each short as a native `1080x1920` portrait HyperFrames rebuild on port `1100 + short number` (reusing the source section's real photos, WIT poses, and font), regenerates a per-short voiceover in the approved voice with burned centered subtitles, and exports each to `projects/<slug>/output/shorts/`. Each short is a COMPLETE standalone short with NO call-to-action; it never edits the long-form sections and does not block caption, upload, or learning.
- Use **packaging** (after caption) when the user asks for title, thumbnail, packaging, YouTube description, tags, hashtags, upload metadata, A/B title/thumbnail testing, or thumbnail prompts. Packaging requires `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`; its recommended position is after `caption` so it can also package shorts and use real chapters. It produces 5 LOCKED title+thumbnail A/B pairs for the main video (title N coupled to thumbnail N), the description/tags, and — when built shorts exist — one title/description/thumbnail per short. Everything (titles, descriptions, thumbnail prompts) goes into one file `output/packaging.md`; images to `output/thumbnails/`. No longer numbered (was `03-packaging.md`); no separate `PROMPTS.md`.
- Use **skill-sync** (utility, outside the pipeline gate) when the user asks to sync skills between Codex and Claude, reconcile the `.claude/skills/` wrappers, or sync `AGENTS.md` and `CLAUDE.md`. Manual only; run only when asked.
- Do not create additional sequential video-production skills until the user explicitly asks for the next skill-creation phase.

Pipeline gate:

- main production skills run in order: `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> review -> combine -> caption -> packaging -> upload -> learning`
- numbered files use NEW-project numbering (`03-voiceover`, `04-visual-plan`, `05-production-board`, `06-review`, `07-upload`, `08-self-learning`); existing projects keep the old numbers and skills resolve step files by name suffix (see `.agents/rules/video-workflow.md`)
- `combine` is the project-level assembly + export step: it runs once after EVERY section is rendered, requires one project (named or smart-selected), reuses the existing section renders/assets without changing them, produces the unified preview on `localhost:1000`, and exports the final MP4 to `projects/<slug>/output/` (rendered via `renders/` staging, then moved; `renders/` removed if left empty). `output/` holds all final deliverables
- `caption` runs once after `combine`: it requires one project and a full-length audio source (the combined voiceover or a full video render), transcribes that audio for real word-level timing, uses the exact `02-script.md` wording, and exports `captions.srt` to `projects/<slug>/output/`. It refuses on per-section audio only; never estimate caption timing
- `shorts` is a side sub-workflow from `combine` (not part of the linear gate): it turns the finished long video into 2-4 complete vertical shorts (`1080x1920`) on ports `1100 + short number`, regenerates per-short voiceover, burns centered subtitles, and exports to `projects/<slug>/output/shorts/`. Each short is a COMPLETE standalone short with NO CTA; it reuses section assets without editing them and does not block caption, upload, or learning
- `packaging` runs after `caption`: it requires `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`, and writes one file `output/packaging.md` (5 locked title+thumbnail A/B pairs, description, tags, thumbnail prompts, and per-short packaging when built shorts exist) plus images in `output/thumbnails/`. Rerunning it makes only `upload`/`learning` potentially stale
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
