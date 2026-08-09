---
name: transcript
description: Turn a recorded HumanPrice narration into transcribes/transcript.md, the timestamped [M:SS] cue list consumed by the scenes skill. Combine multi-part recordings into audios/full.mp3, align each part, and merge them onto one timeline. Use for transcripts, timestamps, audio alignment, subtitles, or a newly recorded voiceover.
---

# Transcript (Claude wrapper)

This is the Claude discovery wrapper for the **transcript** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/transcript/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/transcript/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/transcript/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/transcript/SKILL.md` wins.
