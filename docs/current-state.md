# Current State

This file is the fastest way for a new Codex session to rebuild context.

It should stay short and reflect the latest stable state of the project.

## Project

- Project: `Why It Works`
- Type: `English-first no-face explainer YouTube channel`
- Status: `foundation stage with standardized video-project workspace and HyperFrames-first production pipeline`

## Locked Decisions

- Channel name: `Why It Works`
- Primary language: `English`
- No-face format: `Yes`
- Main audience lens: `English learners`
- Core lane: `money, internet, society, business, and modern life`
- Tone: `smart, simple, funny, dry`

## Core Promise

`Why It Works` explains money, the internet, and modern life in simple, funny English that English learners can enjoy without feeling like they are studying.

## Audience Direction

English learners are now the primary audience lens.

The channel should still be an explainer channel, not a direct English-teaching channel. Each video should make modern life easier to understand while also being easy and satisfying for English learners to follow.

Practical rule:

`Teach the topic first. Make the English learner-friendly by design.`

## Best Reference Mix

- `Half as Interesting` for topic selection
- `Casually Explained` for voice, dry humor, and learner-friendly simple phrasing
- `Mèo Giải Thích` for structure
- `Vui Vẻ` for packaging
- `OverSimplified` for payoff and pacing

## First Recommended Launch Topics

- `Why Everyone Feels Broke Now`
- `Why Free Apps Are Never Really Free`
- `Why Productivity Content Never Fixes Your Life`

## Production Stack

- `video-projects/` stores per-video work and is the source of truth for active videos
- `common/` stores reusable tools, templates, local skills, shared assets, and production notes
- HyperFrames is the default renderer for new and active video production
- Active HyperFrames source lives inside each video folder at `video-projects/<slug>/hyperframes/`
- HyperFrames should prioritize simple board scenes, WIT poses, voiceover, transitions, captions, and handwritten-looking text instead of heavy animation
- Existing George voiceover files are reused as local HyperFrames audio assets when available
- First rendered voiceover-only cut exists for `Why Free Apps Are Never Really Free`
- Current WIT visual experiment: [Core 24 funny WIT pose set](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\core-24)
- Current HyperFrames WIT source for the active video: `video-projects/why-free-apps-never-really-free/hyperframes/assets/wit/poses/core-24`
- `remotion-studio/` is legacy and should remain untouched until the user asks to delete it

## Current Active Video

- Active folder: [why-free-apps-never-really-free](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free)
- Current step: `Review Remotion-matched HyperFrames rough cut`
- Current decision: migrate active production from Remotion to HyperFrames while keeping simple board-based scenes, handwritten labels, red markup, WIT pose anchors, minimal movement, and the legacy Remotion timing
- Current voice decision: use `George`; keep Anh Khoa's voice sample for future cloning after workflow stabilizes
- Latest HyperFrames source: [index.html](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\hyperframes\index.html)
- Latest HyperFrames draft render: [why-free-apps-hyperframes-remotion-match-draft.mp4](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\renders\why-free-apps-hyperframes-remotion-match-draft.mp4)
- Latest HyperFrames composition set: `FullVideo` plus `Part01Hook` through `Part12PayoffEnding`
- Previous Remotion rough cut kept for reference: [full-board-rough-cut-v1.mp4](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\renders\full-board-rough-cut-v1.mp4)

## Deewas Rule

Do not lead with Deewas.

Build trust first through broad explainer content, then connect to money behavior and only later connect softly to Deewas.

## Safety Rule

Do not change core strategy casually.

All new ideas must be treated as:

- `Core`
- `Experiment`
- `Reject`

Use [channel-guardrails.md](C:\ME\THINGS\Build a Channel\docs\channel-guardrails.md) before persisting new strategy.

## Best Next Steps

1. Review `why-free-apps-hyperframes-remotion-match-draft.mp4`
2. Mark scene-level fixes for pacing, layout, and joke clarity against the Remotion-matched HyperFrames cut
3. Polish individual part compositions only after the rough cut direction is approved
