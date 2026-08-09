---
name: caption
description: Create five publish-ready SRT caption files from a completed HumanPrice transcript. Use after /transcript when the user asks for captions, subtitles, SRT files, translated subtitles, Spanish, Japanese, Chinese, or Hindi captions.
---

# Caption (Claude wrapper)

This is the Claude discovery wrapper for the **caption** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/caption/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/caption/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/caption/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/caption/SKILL.md` wins.
