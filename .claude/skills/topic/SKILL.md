---
name: topic
description: Generate five high-potential HumanPrice episode ideas, wait for the user to choose, then scaffold one project per selection. Use for topic ideas, a new video, what to make next, or starting a HumanPrice episode.
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
