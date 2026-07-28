---
name: topic
description: Generate 5 viral TossExplains video topic ideas as a table, wait for the user to pick one, then scaffold the project folder for it. Use when the user says "topic", "topics", "new video", "video ideas", "what should I make next", or asks to start a new episode.
---

# Topic (Claude wrapper)

This is the Claude discovery wrapper for the **topic** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/topic/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/topic/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/topic/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/topic/SKILL.md` wins.
