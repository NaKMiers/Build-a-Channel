# Current State

This is the fastest way for a new Codex session to rebuild context.

Keep it short and current.

## Project

- Channel: `Why It Works`
- Type: English-first no-face explainer YouTube channel
- Status: foundation stage with project-local skills and HyperFrames-first production
- Main audience lens: English learners
- Main lane: money, internet, society, business, and modern life
- Tone: smart, simple, funny, dry

## Core Promise

`Why It Works` explains money, the internet, and modern life in simple, funny English that English learners can enjoy without feeling like they are studying.

Practical rule:

`Teach the topic first. Make the English learner-friendly by design.`

## Compact Shared Systems

Use these compact files instead of the old many-file system:

- Channel strategy: `.agents/_shared/channel/channel-foundation.md`
- Safety gate: `.agents/_shared/channel/channel-guardrails.md`
- Collaboration rules: `.agents/_shared/channel/codex-collaboration.md`
- Production workflow: `.agents/_shared/channel/production-workflow.md`
- Brand and WIT: `.agents/_shared/channel/brand-system.md`
- Topic, packaging, hooks: `.agents/_shared/systems/topic-packaging-hooks.md`
- Script, learner clarity, voice: `.agents/_shared/systems/script-learner-voice.md`
- Visual production: `.agents/_shared/systems/visual-production.md`
- Audio, feedback, quality: `.agents/_shared/systems/audio-feedback-quality.md`

## Current Skills

- `browse`: project-local web and YouTube browsing
- `topic-intake`: step 1, writes `00-topic-intake.md`
- `research-pack`: step 2, writes `01-research-pack.md`
- `script-draft`: step 3, writes `02-script.md`
- `packaging`: step 4, writes `03-packaging.md`
- `voiceover`: step 5, writes `04-voiceover.md` and section audio
- `wiw-take-note`: reusable memory capture

Sequential production skills enforce prerequisites. Later steps require previous output files. Rerunning an earlier step makes downstream outputs stale until removed by explicit user request or regenerated in order.

## Current WIT

Status: `draft replacement generated - awaiting user review`

Current reusable pose folder:

```text
.agents/_shared/assets/wit/poses/
```

It should contain only:

- `manifest.json`
- the `24` transparent PNG poses listed in the manifest

The current WIT direction is the simple white round-headed thumbnail WIT with thick black outline, oversized black glasses, expressive eyebrows, simple white body, and suspicious / betrayed / panicked reactions.

Do not use removed `original-wit-24`, older `core-24`, or `comedy-core` WIT as current channel WIT.

## Current Active Video

- Active folder: `projects/why-everyone-pretends-to-be-busy`
- Current step: Section 3 Busy Became Status implemented; awaiting user review
- Accepted Section 1 composition: `Section01Hook`
- Accepted Section 1 runtime: `24.085s`
- Section preview rule: review and approve one section at a time; assemble sections only after the user asks
- Section asset rule: use one video-level shared asset library at `projects/why-everyone-pretends-to-be-busy/assets`; local section `assets` folders should be junctions, not copied media folders

Restart preview URLs when needed:

- Section 1 Studio: `http://localhost:3021/#project/section-01-hook`
- Section 2 Studio: `http://localhost:3022/#project/section-02-reframe`
- Section 3 Studio: `http://localhost:3023/#project/section-03-busy-status`

Key current project files:

- `projects/why-everyone-pretends-to-be-busy/06-review.md`
- `projects/why-everyone-pretends-to-be-busy/12-section-03-visual-plan.md`
- `projects/why-everyone-pretends-to-be-busy/13-section-03-implementation.md`
- `projects/why-everyone-pretends-to-be-busy/hyperframes/review/section-01.html`
- `projects/why-everyone-pretends-to-be-busy/hyperframes/review/section-02.html`
- `projects/why-everyone-pretends-to-be-busy/hyperframes/review/section-03.html`

## Current Production Lesson

For short hooks, start with `6-8` static boards: one real-life image or object, one WIT reaction, one main label, and hard cuts.

Do not add transition overlays, rapid label pop-ins, object pile-ons, or WIT shake unless the static version is approved and the motion has a clear joke or clarity job.

## Best Next Steps

1. Review Section 3 Busy Became Status.
2. Write feedback into `projects/why-everyone-pretends-to-be-busy/06-review.md`.
3. Continue to the next section only after the current section is approved.
