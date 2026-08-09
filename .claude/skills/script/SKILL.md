---
name: script
description: Write a sourced 8 to 12 minute HumanPrice narration from an approved research brief and save it at the project root. Use when the user asks for a script, narration, outline-to-script conversion, or the next writing stage.
---

# Script (Claude wrapper)

This is the Claude discovery wrapper for the **script** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/script/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/script/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/script/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/script/SKILL.md` wins.
