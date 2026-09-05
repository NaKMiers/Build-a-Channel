---
name: captions
description: Build word-accurate SRT subtitle files for a TossExplains video from the forced-aligned words.json, then translate them into up to 25 languages. Writes one .srt per language to outputs/captions/. Runs after /transcript. Use when the user says "captions", "subtitles", "srt", "translate the transcript", or names a language to subtitle into.
---

# Captions (Claude wrapper)

This is the Claude discovery wrapper for the **captions** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/captions/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/captions/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/captions/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/captions/SKILL.md` wins.
