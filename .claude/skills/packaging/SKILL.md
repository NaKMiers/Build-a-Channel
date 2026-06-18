---
name: packaging
description: Create or update side-branch step 3 YouTube packaging for a Why It Works video project. Use when the user asks for Packaging, title and thumbnail, YouTube description, upload metadata, tags, hashtags, thumbnail concepts, thumbnail images, A/B thumbnail testing, packaging, or step 3 of the side-branch workflow; requires completed 00-topic-intake.md and 01-research-pack.md only, does not require script or voiceover, creates thumbnail drafts using the current approved or pending WIT direction with reusable generation prompts, scores them, then writes only the project's 03-packaging.md and thumbnail assets under assets/thumbnails/.
---

# Packaging (Claude wrapper)

This is the Claude discovery wrapper for the **packaging** skill. The canonical
definition — full purpose, workflow, output format, and self-improving memory — lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/packaging/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/packaging/references/memory.md`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/packaging/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/packaging/SKILL.md` wins.
