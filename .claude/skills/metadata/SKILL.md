---
name: metadata
description: Generate publish-ready HumanPrice titles, description, chapters, hashtags, and SEO tags from a finished script and research brief. Use for YouTube metadata, title options, descriptions, chapters, hashtags, tags, or SEO packaging.
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
