---
name: youtube
description: Read and write YouTube data for the TossExplains channel through the official YouTube Data API v3 and YouTube Analytics API. Subcommands pull video stats, fetch official captions as [M:SS], read day-by-day analytics, upload a finished video, and profile a competitor channel. Use when the user says "/youtube", "pull video stats", "upload to YouTube", "fetch transcript from YouTube", "channel analytics", or "competitor research".
---

# Youtube (Claude wrapper)

This is the Claude discovery wrapper for the **youtube** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/youtube/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/youtube/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/youtube/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/youtube/SKILL.md` wins.
