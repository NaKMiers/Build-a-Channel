---
name: scene-images
description: Safely check, rename, move, and verify TossExplains scene images against image-prompts.md timestamps. Use when the user asks to manage scene-image files, timestamp names, range folders, or scene-image validation.
---

# Scene Images (Claude wrapper)

This is the Claude discovery wrapper for the **scene-images** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/scene-images/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/scene-images/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/scene-images/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/scene-images/SKILL.md` wins.
