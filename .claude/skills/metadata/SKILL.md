---
name: metadata
description: Generate the publish-ready YouTube title, description with hashtags, and 25 to 40 SEO tags for a TossExplains video, saved to outputs/metadata.md. Use when the user says "metadata", "title", "description", "tags", "SEO", or "package the video".
---

# Metadata (Claude wrapper)

This is the Claude discovery wrapper for the **metadata** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/metadata/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/metadata/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/metadata/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/metadata/SKILL.md` wins.
