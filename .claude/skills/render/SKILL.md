---
name: render
description: Build or update step 5 section HyperFrames previews for a Why It Works video project. Use when the user asks for Render, HyperFrames build, create video from visual-plan, build a section preview, run section localhost, start preview servers, or run step 5; export MP4/WebM only when the user explicitly asks to export video; requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 03-voiceover.md, 04-visual-plan.md, selected section voiceover, selected section visual plan, ALL of the selected section's assets ready in assets/ (per assets/asset-manifest.md; render stops if any are missing or awaiting generation/drop rather than sourcing them itself), explicit project selection, and explicit section selection with All as the first option; creates 05-production-board.md, section-previews/ section HyperFrames projects, and hyperframes/ review copies while using port 1000 for unified preview and port 1000 plus section number for section previews.
---

# Render (Claude wrapper)

This is the Claude discovery wrapper for the **render** skill. The canonical
definition - full purpose, workflow, output format, and self-improving memory - lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/render/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/render/references/memory.md`, `.agents/skills/render/references/output-formats.md`, and `.agents/skills/render/references/render-motion-rules.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/render/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/render/SKILL.md` wins.
