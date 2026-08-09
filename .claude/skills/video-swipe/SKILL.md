---
name: video-swipe
description: Turn one competitor YouTube video into a swipe-file study under its own research folder, with every distinct frame extracted, contact sheets, frame-index.csv, and a Vietnamese visual-analysis.md. Requires the YouTube link plus the matching downloaded video file. Use for video swipe studies, frame extraction, competitor visual analysis, or a YouTube link paired with a local video.
---

# Video Swipe (Claude wrapper)

This is the Claude discovery wrapper for the **video-swipe** skill. The canonical
definition lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/video-swipe/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/video-swipe/references/memory.md`.
3. Apply the project rules in `CLAUDE.md` / `AGENTS.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/video-swipe/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/video-swipe/SKILL.md` wins.
