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
- HyperFrames should prioritize simple board scenes, WIT poses, voiceover, hard cuts, cue-timed labels, red markup, and handwritten-looking text instead of heavy animation
- Existing George voiceover files are reused as local HyperFrames audio assets when available
- First rendered voiceover-only cut exists for `Why Free Apps Are Never Really Free`
- Current channel-wide narration system: [Narration System](C:\ME\THINGS\Build a Channel\common\voice\narration-system.md)
- Current script narration markup rules: [Script Markup Guide](C:\ME\THINGS\Build a Channel\common\voice\script-markup-guide.md)
- Current voice test protocol: [Voice Test Protocol](C:\ME\THINGS\Build a Channel\common\voice\voice-test-protocol.md)
- Current channel-wide topic angle selection system: [Topic Angle Selection System](C:\ME\THINGS\Build a Channel\common\topic-angle-selection-system.md)
- Current topic angle quality gate: [Topic Angle Scorecard](C:\ME\THINGS\Build a Channel\common\topic-angle-scorecard.md)
- Current reusable topic angle template folder: [Topic Angle Scorecards](C:\ME\THINGS\Build a Channel\docs\topic-angle-scorecards)
- Current channel-wide WIT system: [WIT Channel System](C:\ME\THINGS\Build a Channel\docs\branding\wit-channel-system.md)
- Current WIT comedy layer: [Comedy Core WIT pose set](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\comedy-core)
- Current channel-wide packaging system: [Thumbnail Packaging System](C:\ME\THINGS\Build a Channel\common\thumbnail-packaging-system.md)
- Current packaging quality gate: [Packaging Scorecard](C:\ME\THINGS\Build a Channel\common\packaging-scorecard.md)
- Current thumbnail visual rules: [Thumbnail Visual Rules](C:\ME\THINGS\Build a Channel\docs\branding\thumbnail-visual-rules.md)
- Current reusable thumbnail templates: [Thumbnail Templates](C:\ME\THINGS\Build a Channel\common\thumbnail-templates)
- Current channel-wide first `10` seconds hook system: [Hook System](C:\ME\THINGS\Build a Channel\common\hook-system.md)
- Current reusable hook templates and gate: [Hook Templates](C:\ME\THINGS\Build a Channel\common\hook-templates)
- Current channel-wide reference-board research system: [Reference Board System](C:\ME\THINGS\Build a Channel\common\reference-board-system.md)
- Current reusable reference-board template: [Reference Boards](C:\ME\THINGS\Build a Channel\common\reference-boards)
- Current channel-wide real-life visual asset system: [Real-Life Visual Asset System](C:\ME\THINGS\Build a Channel\common\real-life-visual-asset-system.md)
- Current reusable real-life asset folders: [Real-Life Assets](C:\ME\THINGS\Build a Channel\common\assets\real-life) and [UI Mockups](C:\ME\THINGS\Build a Channel\common\assets\ui-mockups)
- Current reusable asset source-note template: [Source Note Template](C:\ME\THINGS\Build a Channel\common\assets\source-note-template.md)
- Current channel-wide comedy asset library: [Comedy Asset Library](C:\ME\THINGS\Build a Channel\common\assets\comedy)
- Current reusable comedy asset inventory: [Comedy Asset Inventory](C:\ME\THINGS\Build a Channel\common\assets\comedy\asset-inventory.md)
- Current reusable comedy source-note template: [Comedy Source Note Template](C:\ME\THINGS\Build a Channel\common\assets\comedy\source-note-template.md)
- Current channel-wide scene grammar system: [Scene Grammar System](C:\ME\THINGS\Build a Channel\common\scene-grammar-system.md)
- Current channel-wide visual humor patterns: [Visual Humor Patterns](C:\ME\THINGS\Build a Channel\common\visual-humor-patterns.md)
- Current HyperFrames board grammar and paused-frame review gate: [Board Grammar](C:\ME\THINGS\Build a Channel\common\hyperframes\board-grammar.md)
- Current channel-wide music and sound system: [Music And Sound System](C:\ME\THINGS\Build a Channel\common\music-and-sound-system.md)
- Current reusable sound effect rules: [Sound Effects Library](C:\ME\THINGS\Build a Channel\common\sound-effects-library\README.md)
- Current audio mix quality gate: [Audio Mixing Checklist](C:\ME\THINGS\Build a Channel\common\audio-mixing-checklist.md)
- Current channel-wide English learner clarity system: [English Learner Clarity System](C:\ME\THINGS\Build a Channel\common\english-learner-clarity-system.md)
- Current script clarity quality gate: [English Learner Script Checklist](C:\ME\THINGS\Build a Channel\common\english-learner-script-checklist.md)
- Current visual clarity quality gate: [English Learner Visual Checklist](C:\ME\THINGS\Build a Channel\common\english-learner-visual-checklist.md)
- Current useful phrase rules: [English Learner Useful Phrase Rules](C:\ME\THINGS\Build a Channel\common\english-learner-useful-phrase-rules.md)
- Current humor clarity rules: [English Learner Humor Clarity Rules](C:\ME\THINGS\Build a Channel\common\english-learner-humor-clarity-rules.md)
- Current channel-wide publishing feedback loop: [Publishing Feedback Loop](C:\ME\THINGS\Build a Channel\common\publishing-feedback-loop.md)
- Current reusable post-upload review template: [Post-Upload Review Template](C:\ME\THINGS\Build a Channel\common\post-upload-review-template.md)
- Current channel learning rules: [Channel Learning Rules](C:\ME\THINGS\Build a Channel\common\channel-learning-rules.md)
- Current WIT source experiment: [Core 24 funny WIT pose set](C:\ME\THINGS\Build a Channel\common\assets\wit\poses\core-24)
- Current HyperFrames WIT source for the active video: `video-projects/why-free-apps-never-really-free/hyperframes/assets/wit/poses/core-24`
- `remotion-studio/` is legacy and should remain untouched until the user asks to delete it

## Current Active Video

- Active folder: [why-free-apps-never-really-free](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free)
- Current step: `Review slower David23 HyperFrames rough cut`
- Current decision: active production is now the slower David23 HyperFrames draft; older local MP4 drafts were removed to reduce project weight
- Current voice decision: use `David23` as the default narrator; keep George and Anh Khoa's voice sample as fallback/reference voices
- Latest HyperFrames source: [index.html](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\hyperframes\index.html)
- Latest HyperFrames draft render: [why-free-apps-david23-slow-careful-draft.mp4](C:\ME\THINGS\Build a Channel\video-projects\why-free-apps-never-really-free\renders\why-free-apps-david23-slow-careful-draft.mp4)
- Latest draft runtime: `3:44.62`
- Latest HyperFrames composition set: `FullVideo` plus `Part01Hook` through `Part12PayoffEnding`
- Older prototype and draft MP4 renders were removed from the project folder; production notes keep the historical decisions.

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

1. Review `why-free-apps-david23-slow-careful-draft.mp4`
2. Mark scene-level fixes for pacing, layout, and joke clarity against the Remotion-matched HyperFrames cut
3. Polish individual part compositions only after the rough cut direction is approved
