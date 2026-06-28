---
name: shorts
description: Side sub-workflow after combine. Turn one finished Why It Works long video into 2-4 COMPLETE vertical short videos (1080x1920, 9:16) for YouTube Shorts / TikTok / Reels, then export each to MP4. Use when the user asks for shorts, vertical shorts, YouTube Shorts, TikTok/Reels clips, cut shorts from the main video, portrait clips, or "split the video into shorts". Has three modes - plan (pick clippable moments, write shorts/shorts-plan.md), build (native portrait HyperFrames rebuild per short on port 1100+N with regenerated voiceover + burned centered subtitles), and export (render approved shorts to projects/<slug>/output/shorts/*.mp4). Each short is a COMPLETE standalone short, NOT a hook/teaser, and carries NO "watch the full video" CTA. Requires one project whose sections are already built (combine done, or every section rendered). Reuses each source section's real photos, WIT poses, and font; never edits the long-form sections. Requires one project (named or smart-selected) and an explicit short selection with All as the first option.
---

# Shorts (Claude wrapper)

This is the Claude discovery wrapper for the **shorts** skill. The canonical
definition - full purpose, modes (plan/build/export), gates, locked rules, build
mechanics, self-check, and self-improving memory - lives under `.agents/` so Codex
and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/shorts/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/shorts/references/memory.md`, and reuse `references/gen-word-timings.mjs`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`, and the `render` skill's HyperFrames WIT/safe-layout guidance.
4. Write any skill self-improvement back to `.agents/skills/shorts/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/shorts/SKILL.md` wins.

Key guarantees this skill must honor:

- Side sub-workflow from `combine`; one project; 2-4 shorts (ideally 3); explicit short selection with `All` first; one-at-a-time review.
- Native portrait REBUILD (1080x1920), never a crop/letterbox.
- Each short is a COMPLETE standalone short - **NO CTA / "watch the full video" / subscribe card**; end on its own payoff.
- Platform-safe zone `x[60..880] · y[220..1490]`; WIT body may bleed off edges, FACE stays inside; verify with a temporary safe-guide overlay, then remove it.
- WIT big (≈1/3-1/2 frame), face above the centered caption; approved pose PNGs only.
- Captions = distinct white-on-translucent-dark subtitle, centered VERTICALLY; punchline/payoff carried by cards (no duplication, no overlap).
- Reuse the source section's real photos + WIT + font; regenerate per-short VO in the approved voice; caption from real word timings (tail re-timed).
- Ports `1100 + short number`. Export to `projects/<slug>/output/shorts/*.mp4`; verify 1080x1920 + h264/aac via ffprobe.
- Never edit or re-render long-form section content. Does not block caption/upload/learning.
