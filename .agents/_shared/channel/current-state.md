# Current State

This file is the fastest way for a new Codex session to rebuild context.

It should stay short and reflect the latest stable state of the project.

## Project

- Project: `Why It Works`
- Type: `English-first no-face explainer YouTube channel`
- Status: `foundation stage with standardized projects workspace and HyperFrames-first production pipeline`

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

- `projects/` stores per-video work and is the source of truth for active videos
- `.agents/_shared/` stores reusable tools, templates, workflows, shared assets, and production notes
- `.agents/rules/` stores Codex and future skill operating rules
- `.agents/skills/` stores executable project-local Codex skills
- Current project-local skills: `browse` for portable web and YouTube browsing, `topic-intake` for step 1 topic intake, `research-pack` for step 2 evidence packs, `script-draft` for step 3 sectioned scripts, and `wiw-take-note` for memory capture
- HyperFrames is the default renderer for new and active video production
- Active HyperFrames source lives inside each video folder at `projects/<slug>/hyperframes/`
- HyperFrames should prioritize simple board scenes, WIT poses, voiceover, hard cuts, cue-timed labels, red markup, and handwritten-looking text instead of heavy animation
- Existing George voiceover files are reused as local HyperFrames audio assets when available
- First rendered voiceover-only cut exists for `Why Free Apps Are Never Really Free`
- Current channel-wide narration system: [Narration System](C:\ME\THINGS\Build a Channel\.agents_shared\voice\narration-system.md)
- Current script narration markup rules: [Script Markup Guide](C:\ME\THINGS\Build a Channel\.agents_shared\voice\script-markup-guide.md)
- Current voice test protocol: [Voice Test Protocol](C:\ME\THINGS\Build a Channel\.agents_shared\voice\voice-test-protocol.md)
- Current channel-wide topic angle selection system: [Topic Angle Selection System](C:\ME\THINGS\Build a Channel\.agents_shared\topic-angle-selection-system.md)
- Current topic angle quality gate: [Topic Angle Scorecard](C:\ME\THINGS\Build a Channel\.agents_shared\topic-angle-scorecard.md)
- Current reusable topic angle template folder: [Topic Angle Scorecards](C:\ME\THINGS\Build a Channel\.agents_shared\channel\topic-angle-scorecards)
- Current channel-wide WIT system: [WIT Channel System](C:\ME\THINGS\Build a Channel\.agents_shared\channel\branding\wit-channel-system.md)
- Current WIT pose set: [Original WIT 24](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\original-wit-24)
- Current WIT contact sheet: [Original WIT 24 Contact Sheet](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\original-wit-24\original-wit-24-contact-sheet.png)
- Superseded WIT comedy layer: [Comedy Core WIT pose set](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\comedy-core)
- Current channel-wide packaging system: [Thumbnail Packaging System](C:\ME\THINGS\Build a Channel\.agents_shared\thumbnail-packaging-system.md)
- Current packaging quality gate: [Packaging Scorecard](C:\ME\THINGS\Build a Channel\.agents_shared\packaging-scorecard.md)
- Current thumbnail visual rules: [Thumbnail Visual Rules](C:\ME\THINGS\Build a Channel\.agents_shared\channel\branding\thumbnail-visual-rules.md)
- Current reusable thumbnail templates: [Thumbnail Templates](C:\ME\THINGS\Build a Channel\.agents_shared\thumbnail-templates)
- Current channel-wide first `10` seconds hook system: [Hook System](C:\ME\THINGS\Build a Channel\.agents_shared\hook-system.md)
- Current reusable hook templates and gate: [Hook Templates](C:\ME\THINGS\Build a Channel\.agents_shared\hook-templates)
- Current channel-wide reference-board research system: [Reference Board System](C:\ME\THINGS\Build a Channel\.agents_shared\reference-board-system.md)
- Current reusable reference-board template: [Reference Boards](C:\ME\THINGS\Build a Channel\.agents_shared\reference-boards)
- Current channel-wide real-life visual asset system: [Real-Life Visual Asset System](C:\ME\THINGS\Build a Channel\.agents_shared\real-life-visual-asset-system.md)
- Current reusable real-life asset folders: [Real-Life Assets](C:\ME\THINGS\Build a Channel\.agents_shared\assets\real-life) and [UI Mockups](C:\ME\THINGS\Build a Channel\.agents_shared\assets\ui-mockups)
- Current reusable asset source-note template: [Source Note Template](C:\ME\THINGS\Build a Channel\.agents_shared\assets\source-note-template.md)
- Current channel-wide comedy asset library: [Comedy Asset Library](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy)
- Current reusable comedy asset inventory: [Comedy Asset Inventory](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy\asset-inventory.md)
- Current reusable comedy source-note template: [Comedy Source Note Template](C:\ME\THINGS\Build a Channel\.agents_shared\assets\comedy\source-note-template.md)
- Current channel-wide scene grammar system: [Scene Grammar System](C:\ME\THINGS\Build a Channel\.agents_shared\scene-grammar-system.md)
- Current channel-wide visual humor patterns: [Visual Humor Patterns](C:\ME\THINGS\Build a Channel\.agents_shared\visual-humor-patterns.md)
- Current HyperFrames board grammar and paused-frame review gate: [Board Grammar](C:\ME\THINGS\Build a Channel\.agents_shared\hyperframes\board-grammar.md)
- Current channel-wide music and sound system: [Music And Sound System](C:\ME\THINGS\Build a Channel\.agents_shared\music-and-sound-system.md)
- Current reusable sound effect rules: [Sound Effects Library](C:\ME\THINGS\Build a Channel\.agents_shared\sound-effects-library\README.md)
- Current audio mix quality gate: [Audio Mixing Checklist](C:\ME\THINGS\Build a Channel\.agents_shared\audio-mixing-checklist.md)
- Current channel-wide English learner clarity system: [English Learner Clarity System](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-clarity-system.md)
- Current script clarity quality gate: [English Learner Script Checklist](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-script-checklist.md)
- Current visual clarity quality gate: [English Learner Visual Checklist](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-visual-checklist.md)
- Current useful phrase rules: [English Learner Useful Phrase Rules](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-useful-phrase-rules.md)
- Current humor clarity rules: [English Learner Humor Clarity Rules](C:\ME\THINGS\Build a Channel\.agents_shared\english-learner-humor-clarity-rules.md)
- Current channel-wide publishing feedback loop: [Publishing Feedback Loop](C:\ME\THINGS\Build a Channel\.agents_shared\publishing-feedback-loop.md)
- Current reusable post-upload review template: [Post-Upload Review Template](C:\ME\THINGS\Build a Channel\.agents_shared\post-upload-review-template.md)
- Current channel learning rules: [Channel Learning Rules](C:\ME\THINGS\Build a Channel\.agents_shared\channel-learning-rules.md)
- Superseded WIT source experiment: [Core 24 funny WIT pose set](C:\ME\THINGS\Build a Channel\.agents_shared\assets\wit\poses\core-24)
- Current active video WIT source: `projects/why-everyone-pretends-to-be-busy/assets/wit`
- Legacy Remotion notes live in `.agents/_shared/remotion/`; HyperFrames remains the active production path.

## Current Active Video

- Active folder: [why-everyone-pretends-to-be-busy](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy)
- Current step: `Section 3 Busy Became Status implemented; awaiting user review`
- Current decision: Section 1 should use a simple Casually Explained-style static-board rhythm, not dense cue-by-cue animation
- Accepted Section 1 composition: `Section01Hook`
- Accepted Section 1 runtime: `24.085s`
- Accepted Section 1 voice test: `section-01-hook-young-fast-am_adam-1.05.mp3`
- Current active preview composition: separate per-section HyperFrames previews
- Current active preview runtimes: Section 1 `24.085s`; Section 2 `23.9s`; Section 3 `46.763s`
- Section separation rule: preview and approve one section at a time; assemble sections only after the user asks
- Section preview operation rule: during section-by-section production, run each section as a separate HyperFrames preview project on its own port
- Section asset operation rule: use one video-level shared asset library at `projects/why-everyone-pretends-to-be-busy/assets`; local `assets` folders inside `hyperframes/` and `section-previews/<section>/` should be junctions, not copied media folders
- Separate section Studio preview ports when restarted: Section 1 `http://localhost:3021/#project/section-01-hook`; Section 2 `http://localhost:3022/#project/section-02-reframe`; Section 3 `http://localhost:3023/#project/section-03-busy-status`
- Separate section direct composition URLs when restarted: Section 1 `http://localhost:3021/api/projects/section-01-hook/preview/comp/index.html`; Section 2 `http://localhost:3022/api/projects/section-02-reframe/preview/comp/index.html`; Section 3 `http://localhost:3023/api/projects/section-03-busy-status/preview/comp/index.html`
- Section 2 draft voice test: `section-02-reframe-young-fast-am_adam-1.05.mp3`
- Section 3 draft voice test: `section-03-busy-status-young-fast-am_adam-1.05.mp3`
- Standalone Section 1 source: [section-01.html](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\hyperframes\review\section-01.html)
- Standalone Section 2 source: [section-02.html](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\hyperframes\review\section-02.html)
- Standalone Section 3 source: [section-03.html](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\hyperframes\review\section-03.html)
- Latest Section 3 implementation note: [13-section-03-implementation.md](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\13-section-03-implementation.md)
- Latest Section 3 visual plan: [12-section-03-visual-plan.md](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\12-section-03-visual-plan.md)
- Latest Section 2 asset refresh note: [11-asset-refactor-section-02-refresh.md](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\11-asset-refactor-section-02-refresh.md)
- Previous Section 2 implementation note: [10-section-02-implementation.md](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\10-section-02-implementation.md)
- Latest HyperFrames source: [index.html](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\hyperframes\index.html)
- Latest Section 1 review notes: [06-review.md](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\06-review.md)
- Latest Section 1 accepted plan: [08-section-01-simple-remake.md](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\08-section-01-simple-remake.md)
- Latest Section 1 contact sheet: [section01-contact-sheet.jpg](C:\ME\THINGS\Build a Channel\projects\why-everyone-pretends-to-be-busy\hyperframes\qa\section01-contact-sheet.jpg)

Section 1 production lesson:
for short hooks, start with `6-8` static boards: one real-life image, one WIT reaction, one main label, and hard cuts.
Do not add transition overlays, rapid label pop-ins, object pile-ons, or WIT shake unless the static version is approved and the motion has a clear joke or clarity job.

## Influence Rule

Do not frame the channel as app promotion.

Build influence first through broad, useful, funny explainer content about money, internet behavior, business, society, and modern life.

## Safety Rule

Do not change core strategy casually.

All new ideas must be treated as:

- `Core`
- `Experiment`
- `Reject`

Use [channel-guardrails.md](C:\ME\THINGS\Build a Channel\.agents_shared\channel\channel-guardrails.md) before persisting new strategy.

## Best Next Steps

1. Restart the section preview servers from the new `projects/why-everyone-pretends-to-be-busy/section-previews/<section>/` paths if review is needed.
2. Review Section 3 Busy Became Status and write feedback into `projects/why-everyone-pretends-to-be-busy/06-review.md`.
3. Continue to the next section only after the current section is approved.
