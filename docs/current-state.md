# Current State

This file is the fastest way for a new Codex session to rebuild context.

It should stay short and reflect the latest stable state of the project.

## Project

- Project: `Why It Works`
- Type: `English-first no-face explainer YouTube channel`
- Status: `foundation stage with standardized video-project workspace and first working production pipeline`

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
- `remotion-studio` is the working Remotion app for long-form video assembly
- Remotion should prioritize simple static scenes, WIT poses, voiceover, hard cuts, captions, and handwritten-looking text instead of full animation
- ElevenLabs voiceover generation is configured through local env vars
- Sample scene timing now follows generated voiceover files automatically
- First rendered voiceover-only cut exists for `Why Free Apps Are Never Really Free`
- Current WIT visual reference experiment: [wit-character-reference-v3-cute-short.png](C:\ME\THINGS\Build a Channel\common\assets\wit\wit-character-reference-v3-cute-short.png)

## Current Active Video

- Active folder: [why-free-apps-never-really-free](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free)
- Current step: `Review full board rough cut v1`
- Current decision: restart the Remotion opening around simple board-based scenes, hard cuts, handwritten labels, red markup, and minimal WIT movement
- Current voice decision: use `George`; keep Anh Khoa's voice sample for future cloning after workflow stabilizes
- Latest render: [full-board-rough-cut-v1.mp4](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\renders\full-board-rough-cut-v1.mp4)

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

1. Review `full-board-rough-cut-v1.mp4`
2. Mark scene-level fixes for pacing, layout, and joke clarity
3. Polish only after the full rough cut direction is approved
