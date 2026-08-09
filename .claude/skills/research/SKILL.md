---
name: research
description: Research a HumanPrice topic and write the sourced evidence brief that gates scriptwriting, titles, thumbnails, and metadata. Use after a topic is selected, or when the user asks to research, fact-check, source, validate claims, or build an evidence brief for an episode.
---

# Research (Claude wrapper)

This is the Claude discovery wrapper for the **research** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/research/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/research/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/research/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/research/SKILL.md` wins.
