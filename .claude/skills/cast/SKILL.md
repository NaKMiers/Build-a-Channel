---
name: cast
description: Derive the 2 to 6 character cast for a HumanPrice episode and write reference-sheet prompts with a stable recurring protagonist. Use for cast, characters, character sheets, or locking visual identities from a finished script.
---

# Cast (Claude wrapper)

This is the Claude discovery wrapper for the **cast** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/cast/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/cast/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/cast/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/cast/SKILL.md` wins.
