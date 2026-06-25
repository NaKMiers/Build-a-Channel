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
- YouTube publishing & growth: `.agents/_shared/systems/youtube-publishing-growth.md`

## Current Skills

- `browse`: project-local web and YouTube browsing
- `topic-intake`: step 0, writes `00-topic-intake.md`
- `research-pack`: step 1, writes `01-research-pack.md`
- `script-draft`: main step 2, writes `02-script.md`
- `packaging`: side branch step 3, requires only `00-topic-intake.md` and `01-research-pack.md`, writes `03-packaging.md`
- `voiceover`: main step 4, writes `04-voiceover.md` and section audio
- `visual-plan`: main step 5, writes `05-visual-plan.md`, section plans, reference boards, and visual reference assets
- `render`: main step 6, writes `06-production-board.md`, section HyperFrames previews, review copies, and optional renders
- `combine`: project-level assembly + export step after all sections; unifies on `localhost:1000` with one combined voiceover and exports the full MP4 to `output/`
- `caption`: post-combine; transcribes the full combined audio for real word timings, uses exact `02-script.md` wording, exports `output/captions.srt`
- `shorts`: side sub-workflow from `combine`; turns the finished long video into 2-4 COMPLETE vertical shorts (`1080x1920`) on ports `1100 + short number` via native portrait HyperFrames rebuilds (reused section assets + regenerated per-short voice + burned centered subtitles, NO CTA), exported to `output/shorts/`. First run: `why-cheap-products-keep-getting-worse` (3 shorts)

Sequential production skills enforce prerequisites. Main pipeline order is `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> render -> review -> combine -> caption -> upload -> learning`. Packaging is a side branch from `research-pack`; it requires only topic intake and research pack and does not block script, voiceover, visual plan, render, review, upload, or learning. `shorts` is a side sub-workflow after `combine`. Rerunning an earlier main-pipeline dependency makes downstream main outputs stale until removed by explicit user request or regenerated in order. After voiceover, production branches by section: each section can move through visual plan, render, and review separately. Render uses fixed ports: unified preview on `localhost:1000`, section `N` on `localhost:1000 + N`.

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

- Active folder: `projects/1-why-cheap-products-keep-getting-worse`
- Current step: Section 2 render review/update on localhost; Section 1 Hook and Section 3 previews also exist
- Section 1 composition: `Section01Hook`
- Section 1 runtime: `21.205s`
- Section 1 preview: `http://localhost:1001/#project/section-01-hook`
- Section 1 source of truth: `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-01-hook/index.html`
- Manual Studio preservation: Anh Khoa made direct localhost/Studio edits after the reduced-WIT pass. Future Section 1 updates must preserve this `index.html`, diff before editing, and never overwrite it from an older review mirror or visual plan.
- VFX cleanup state: accidental `vfx-liquid-glass` artifact was removed and root duration restored to the voiceover runtime.
- Section 1 render: `MP4 not requested; use preview only unless user explicitly asks to export video`
- Section 1 current style: connected big scenes, reduced cue count, low animation density, large but sparse WIT emotional beats
- Section 2 preview: `http://localhost:1002/#project/section-02-cheap-is-not-the-villain`
- Section 2 current style: `3` connected big scenes, grouped cue overlays, reduced WIT density, phrase-timed hard-shows, giant Section-1-style WIT emotional placements, no MP4 export
- Section 2 manual Studio preservation: Anh Khoa manually adjusted the localhost/Studio preview after the giant-WIT pass. Future Section 2 updates must preserve `section-previews/section-02-cheap-is-not-the-villain/index.html` as canonical, diff before editing, and never overwrite it from the visual plan, old generated drafts, or an older review mirror. The latest backup is `section-previews/section-02-cheap-is-not-the-villain/manual-saves/save-110159.html`.
- Section preview rule: review and approve one section at a time; assemble sections only after the user asks
- Section asset rule: use one video-level shared asset library at `projects/1-why-cheap-products-keep-getting-worse/assets`; local section previews use minimal hardlinked working sets on this Windows HyperFrames setup

Key current project files:

- `projects/1-why-cheap-products-keep-getting-worse/06-production-board.md`
- `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-01-hook/index.html`
- `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-01-hook/IMPLEMENTATION.md`
- `projects/1-why-cheap-products-keep-getting-worse/hyperframes/review/section-01.html`
- `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-02-cheap-is-not-the-villain/index.html`
- `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-03-the-price-tag-speaks-first/index.html`

## Current Production Lesson

For short hooks, start with a few persistent big scenes and `6-8` cue states/static boards: one real-life image or object, one WIT reaction when emotion matters, one main label, and hard cuts.

Do not add transition overlays, rapid label pop-ins, object pile-ons, or WIT shake unless the static version is approved and the motion has a clear joke or clarity job. Ordinary labels can hard-show on the spoken beat; reserve smash/pop/stamp motion for emphasized words, proof marks, and payoff phrases. WIT should be large enough for emotion to read, must not look accidentally cropped, and should usually appear only `1-2` times per persistent big scene in short sections. Check text/WIT collision both ways: WIT must not cover labels/proof, and payoff text or stamps must not cover WIT's face/expression.

## Best Next Steps

1. Review the manually adjusted Section 1 Hook at `http://localhost:1001/#project/section-01-hook`.
2. If Section 1 needs another update, preserve `section-previews/section-01-hook/index.html` as canonical before editing.
3. Continue to the next section only after the current section is approved.
