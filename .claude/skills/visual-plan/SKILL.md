---
name: visual-plan
description: Create or update the step 4 visual plan for a Why It Works video project - the detailed, imagination-led blueprint of every scene. Use when the user asks for visual plan, scene plan, scene-by-scene screen direction, describe the visuals, plan the visuals, or step 4 of the Why It Works workflow. It builds ONE master plan per video and synced per-section copies, breaks the script into per-sentence (or few-sentence) scenes, and describes each scene in extreme detail (composition, every element, mascot pose, on-screen text, emotion, insight, element linkage, show-as-you-say timing, sound, color) plus an ASSET list per scene (type generate/browse/screenshot/reuse, filename, layout). visual-plan DESCRIBES only - it never writes image-generation prompts (that is visual-implement's job) and is not limited to the existing pose library (it may invent new poses/scenes if good, within copyright/law/YouTube community standards). Requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 03-voiceover.md and an explicit section selection with All first; writes only 04-visual-plan.md and the visual-plan/ section folders.
---

# Visual Plan (Claude wrapper)

This is the Claude discovery wrapper for the **visual-plan** skill. The canonical
definition - full purpose, workflow, output format, and self-improving memory - lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/visual-plan/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/visual-plan/references/memory.md` and `.agents/skills/visual-plan/references/output-formats.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/visual-plan/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/visual-plan/SKILL.md` wins.
