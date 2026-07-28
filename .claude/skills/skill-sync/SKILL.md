---
name: skill-sync
description: Reconcile the canonical .agents/skills definitions with the thin .claude/skills wrappers and the Codex agents/openai.yaml metadata for this repo. Run after adding, renaming, or removing a skill, or after editing a skill's name or description. Use when the user says "skill-sync", "sync skills", or "regenerate wrappers". Manual only.
---

# Skill Sync (Claude wrapper)

This is the Claude discovery wrapper for the **skill-sync** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/skill-sync/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/skill-sync/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/skill-sync/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/skill-sync/SKILL.md` wins.
