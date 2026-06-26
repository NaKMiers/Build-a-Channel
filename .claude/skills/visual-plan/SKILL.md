---
name: visual-plan
description: Create or update step 4 render-trustworthy section visual plans for a Why It Works video project. Use when the user asks for Visual Plan, visual planning, scene-by-scene or second-by-second what-when-how screen direction, big-scene and cue-state timeline, reference board, real-life internet visual references, generated support assets, WIT pose planning, HyperFrames build guidance, run step 4, or plan visuals for one section or all sections; requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 03-voiceover.md, explicit project selection, and explicit section selection with All as the first option, then writes only the project's 04-visual-plan.md, visual-plan/ section folders, and visual reference assets.
---

# Visual Plan (Claude wrapper)

This is the Claude discovery wrapper for the **visual-plan** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/visual-plan/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/visual-plan/references/memory.md` and `.agents/skills/visual-plan/references/output-formats.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/visual-plan/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/visual-plan/SKILL.md` wins.
