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
- `topic-intake`: step 0, writes `00-topic-intake.md`
- `research-pack`: step 1, writes `01-research-pack.md`
- `script-draft`: main step 2, writes `02-script.md`
- `packaging`: side branch step 3, requires only `00-topic-intake.md` and `01-research-pack.md`, writes `03-packaging.md`
- `voiceover`: main step 4, writes `04-voiceover.md` and section audio
- `visual-plan`: main step 5, writes `05-visual-plan.md`, section plans, reference boards, and visual reference assets
- `render`: main step 6, writes `06-production-board.md`, section HyperFrames previews, review copies, and optional renders
- `wiw-take-note`: reusable memory capture

Sequential production skills enforce prerequisites. Main pipeline order is `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> review -> upload -> learning`. Packaging is a side branch from `research-pack`; it requires only topic intake and research pack and does not block script, voiceover, visual plan, render, review, upload, or learning. Rerunning an earlier main-pipeline dependency makes downstream main outputs stale until removed by explicit user request or regenerated in order. After voiceover, production branches by section: each section can move through visual plan, render, and review separately. Render uses fixed ports: unified preview on `localhost:1000`, section `N` on `localhost:1000 + N`.

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
- Current step: Section 1 Hook second replacement implemented; awaiting user review
- Section 1 replacement composition: `Section01Hook`
- Section 1 replacement runtime: `24.085s`
- Section 1 replacement preview: `http://localhost:1001/#project/section-01-hook`
- Section 1 replacement render: `projects/why-everyone-pretends-to-be-busy/renders/section-01-hook/section-01-hook-remake.mp4`
- Section 1 current style: real channel WIT pose PNGs, simple illustrative static boards, hard cuts only, old visual plan skipped
- Section preview rule: review and approve one section at a time; assemble sections only after the user asks
- Section asset rule: use one video-level shared asset library at `projects/why-everyone-pretends-to-be-busy/assets`; local section `assets` folders should be junctions, not copied media folders

Legacy active-project preview URLs when needed:

These belong to the existing `why-everyone-pretends-to-be-busy` work that predates the new `render` skill port rule. Future `render` skill runs should use `localhost:1000` for unified preview and `localhost:1000 + section number` for section previews.

- Section 1 Studio: `http://localhost:3021/#project/section-01-hook`
- Section 2 Studio: `http://localhost:3022/#project/section-02-reframe`
- Section 3 Studio: `http://localhost:3023/#project/section-03-busy-status`

Key current project files:

- `projects/why-everyone-pretends-to-be-busy/06-review.md`
- `projects/why-everyone-pretends-to-be-busy/12-section-03-visual-plan.md`
- `projects/why-everyone-pretends-to-be-busy/13-section-03-implementation.md`
- `projects/why-everyone-pretends-to-be-busy/hyperframes/review/section-01.html`
- `projects/why-everyone-pretends-to-be-busy/section-previews/section-01-hook/index.html`
- `projects/why-everyone-pretends-to-be-busy/hyperframes/review/section-02.html`
- `projects/why-everyone-pretends-to-be-busy/hyperframes/review/section-03.html`

## Current Production Lesson

For short hooks, start with `6-8` static boards: one real-life image or object, one WIT reaction, one main label, and hard cuts.

Do not add transition overlays, rapid label pop-ins, object pile-ons, or WIT shake unless the static version is approved and the motion has a clear joke or clarity job.

## Best Next Steps

1. Review the rebuilt Section 1 Hook replacement at `http://localhost:1001/#project/section-01-hook`.
2. Write feedback into `projects/why-everyone-pretends-to-be-busy/06-review.md`.
3. Continue to the next section only after the current section is approved.
