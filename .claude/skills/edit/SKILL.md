---
name: edit
description: Build the Kdenlive project for a TossExplains video, with every scene image already cut onto the timeline at its transcript timestamp and the narration on its own track. Use when the user says "edit", "kdenlive", "build the timeline", "assemble the video", or "join the scenes".
---

# Edit (Claude wrapper)

This is the Claude discovery wrapper for the **edit** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/edit/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/edit/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/edit/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/edit/SKILL.md` wins.
