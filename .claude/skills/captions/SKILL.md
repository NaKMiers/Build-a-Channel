---
name: captions
description: Translate a finished transcript into SRT subtitle files for English, Vietnamese, Spanish, Japanese, Dutch, Hindi, Chinese, and Korean. Saves one .srt file per language to outputs/captions/. Use when the user asks for captions, subtitles, subtitle files, or to translate the transcript into another language.
---

# Captions (Claude wrapper)

This is the Claude discovery wrapper for the **captions** skill. The canonical definition lives
under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/captions/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/captions/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/captions/references/memory.md` (the
   single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever disagree,
`.agents/skills/captions/SKILL.md` wins.
