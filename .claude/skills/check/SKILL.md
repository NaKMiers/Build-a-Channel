---
name: check
description: Validate a TossExplains project against the rule files and report what is missing or malformed, then name the next pipeline step. Checks the verbatim style strings, timestamp alignment, cast token integrity, file formats, and banned patterns. Use when the user says "check", "validate", "is this correct", "what is missing", or "audit the project".
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
