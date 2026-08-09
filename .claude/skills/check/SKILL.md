---
name: check
description: Validate a HumanPrice project against research, script, transcript, cast, scene, metadata, and thumbnail contracts, then report failures and the next pipeline step. Use to check, validate, audit, or find what a project is missing.
---

# Check (Claude wrapper)

This is the Claude discovery wrapper for the **check** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/check/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/check/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/check/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/check/SKILL.md` wins.
