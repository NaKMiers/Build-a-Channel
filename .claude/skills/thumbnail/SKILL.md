---
name: thumbnail
description: Create self-contained cinematic TossExplains thumbnail prompts from a finished script and cast. Supports one or more copyable chat prompts and the default five-prompt prompts/thumbnail-prompts.md workflow. Use when the user asks for a thumbnail, thumbnail prompt, thumbnail concept, alternate thumbnail, or YouTube packaging image.
---

# Thumbnail (Claude wrapper)

This is the Claude discovery wrapper for the **thumbnail** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/thumbnail/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/thumbnail/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/thumbnail/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/thumbnail/SKILL.md` wins.
