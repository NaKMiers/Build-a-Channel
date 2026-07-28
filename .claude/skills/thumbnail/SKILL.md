---
name: thumbnail
description: Write five A/B-testable thumbnail concepts for a TossExplains video into prompts/thumbnail-prompts.md, following the evidence-backed rules from the competitor teardown. Use when the user says "thumbnail", "thumbnails", "thumbnail prompts", or "thumbnail concepts".
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
