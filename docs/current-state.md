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
- Core lane: `money, internet, society, business, and modern life`
- Tone: `smart, simple, funny, dry`

## Core Promise

`Why It Works` explains money, the internet, and modern life in a way that's actually fun.

## Best Reference Mix

- `Half as Interesting` for topic selection
- `Casually Explained` for voice
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
- ElevenLabs voiceover generation is configured through local env vars
- Sample scene timing now follows generated voiceover files automatically
- First rendered voiceover-only cut exists for `Why Free Apps Are Never Really Free`

## Current Active Video

- Active folder: [why-free-apps-never-really-free](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free)
- Current step: `Step 8 - Visual Plan`
- Current decision: restart from approved idea, research, script, and packaging before producing another cut

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

1. Complete `Step 8 - Visual Plan` for `Why Free Apps Are Never Really Free`
2. Convert the approved visual plan into a production board
3. Only then generate voiceover/render a new rough cut
