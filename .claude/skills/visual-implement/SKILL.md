---
name: visual-implement
description: Run step 4.5 of the Why It Works workflow — turn a completed visual plan into actual assets. Use when the user asks to implement the visual plan, create the assets, generate the scene images, build the assets folder, prep assets for render, or run visual-implement. It reads each scene's ASSET list in the section visual plan and, per asset, EITHER writes a detailed image-generation prompt and creates an isolated element (generate), OR browses for a license-safe real photo / captures a real public screenshot (browse), OR copies a pose from the library, and it REUSES any asset already produced (by filename) instead of recreating it. All assets are saved as isolated elements (transparent/plain background, never a pre-composed scene) into the project assets/ library, tracked in assets/asset-manifest.md with prompt/source/license/status. Requires a completed 04-visual-plan.md and the selected section's visual-plan folder; requires one project and an explicit section selection with All first. Runs after visual-plan and before render.
---

# Visual Implement (Claude wrapper)

This is the Claude discovery wrapper for the **visual-implement** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/visual-implement/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/visual-implement/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/visual-implement/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/visual-implement/SKILL.md` wins.
