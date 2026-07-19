# Current State

This is the fastest way for a new Codex session to rebuild context.

Keep it short and current.

## Project

- Channel: `Why It Works`
- Type: English-first no-face explainer YouTube channel
- Status: foundation stage with project-local skills and HyperFrames-first production
- Main audience lens: English learners, level `A2–C1` (anchor at B1)
- Competitive advantage: `interesting English` - entertainment-first explainers so learners stay and learn (their motivation to keep watching = their motivation to learn)
- Topic sourcing: trending / currently-interesting topics the world cares about now, chosen with real demand evidence (see `topic-intake`)
- Main lane: money, internet, society, business, modern life, and current culture
- Tone: smart, simple, funny, dry, and allowed to be savage/cheeky (edge aimed at the system / the viewer's own wallet, never slurs; public figures only as transformative parody) - see `learning-log.md` confirmed tone + safety rules
- Audience-layer rule (owner-confirmed 2026-07-18): package for the money/modern-life mainstream (Layer 1, huge demand); deliver in learner-friendly English (Layer 3, script only). Never label the channel as "learn English". See `channel-foundation.md` -> Positioning -> Audience-layer rule.
- Monetization direction (owner-confirmed 2026-07-18): primary = personal-finance SaaS for developed-market viewers; secondary = language-learning apps. Steer topics/packaging toward the money/personal-finance angle. See `channel-foundation.md` -> Monetization direction.
- Packaging rules (owner-confirmed 2026-07-18): huge central text stating the VALUE, clean background, number/concrete stake in titles, stop opening every title with "Why...?". From the Simple Ways of Life teardown in `analysis/simple-way-of-life/`; full rules in `channel-foundation.md` -> Thumbnail direction -> Packaging rules.
- Long-video length (owner-confirmed 2026-07-18): sweet spot `8-10 min` now (8+ min = mid-roll ads + watch-time; ~10 min = achievable retention). Length follows value, never pad to a number; extend only when retention allows. Full ladder in `channel-foundation.md` -> Publishing System.
- Official channel voice (owner-locked 2026-07-18): **`Alan`** - custom ElevenLabs Voice-Design voice, `voice_id f8k6yACqa8sb7OSDGsSp`, model `eleven_multilingual_v2`, settings stability 0.4 / similarity 0.8 / style 0.35 / speaker_boost on. Young American man, warm + dry deadpan. Commercial license (owner on Starter+). Key from `ELEVENLABS_API_KEY` env var, NEVER committed. Legacy `David23 / am_eric` (Kokoro, free) is fallback/scratch only. Detail in voiceover skill + `channel-foundation.md` -> Voice And Tone.
- Production style (owner-decided 2026-07-19): the 2026-07-18 "SIMPLE + CONSISTENT held-image slideshow" experiment (and its "clean light background" locked base) was tried on video 7 section 1 and REJECTED by the owner ("worse than garbage"). The four skills topic-intake / visual-plan / visual-implement / render were reverted to their committed P6-standard state; the P6 per-sentence vivid style governs again. The entire video-7 project (`7-why-you-cant-get-your-first-job`) was then deleted at the owner's request - no project 7 exists. See `learning-log.md` -> "FAILED EXPERIMENT".
- Reference/competitor data tool: `.agents/_shared/tools/yt_collect.py` (YouTube Data API v3, stdlib only, key `YOUTUBE_API_KEY` in `.env`). Collected data lives in `analysis/<channel>/`. Useful for demand evidence during topic work; the topic-intake skill itself was reverted to its committed state (no built-in API requirement).
- Secrets: `ELEVENLABS_API_KEY` and `YOUTUBE_API_KEY` live in `.env` (gitignored). Skills read them from env vars; NEVER hardcode or commit keys.

## File Language Convention (owner-confirmed 2026-06-28)

Write ALL workspace/source files in **English** - skills, plans, research packs, manifests, docs,
generation prompts, notes. Non-English text appears ONLY as **in-video content**: the spoken narration
in the script and the on-screen text labels that appear in the video. Conversation with the owner may
be in Vietnamese, but written deliverables are English. This holds even for a Vietnamese-language
experiment video: its narration + on-screen labels are Vietnamese; every description/field around them
is English.

**HARD RULE (owner-confirmed 2026-06-28): NEVER use the em dash (Unicode U+2014) anywhere in this
project - not in any file and not in chat replies. Always use a plain hyphen "-" instead. The owner
never wants to see that character.**

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
- `voiceover`: main step 3, writes `03-voiceover.md` (legacy `04`) and section audio
- `visual-plan`: main step 4, writes `04-visual-plan.md` (legacy `05`) + synced section plans. As of 2026-06-28 it is a rebuild: ONE master plan + synced section copies, per-sentence scenes, extreme scene detail + an ASSET list per scene (type/filename/layout). It DESCRIBES only (no image prompts) and may invent new poses/scenes (within copyright/law/community standards).
- `visual-implement`: main step 4.5 (unnumbered), reads the visual plan's ASSET lists and produces them - writes image prompts + creates isolated `generate` elements, browses license-safe real photos / captures public screenshots, copies poses, REUSES by filename - into `assets/` + `assets/asset-manifest.md`.
- `render`: main step 5, writes `05-production-board.md` (legacy `06`), section HyperFrames previews, review copies, and optional renders. As of 2026-06-28 it COMPOSITES the mascot + pre-made assets from `assets/` per the plan's layout (re-sources only as a documented fallback).
- `packaging`: runs after `caption`; requires `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`; writes `output/packaging.md` (titles, descriptions, thumbnail prompts) and `output/thumbnails/`. No longer numbered (was `03-packaging.md`)
- `combine`: project-level assembly + export step after all sections; unifies on `localhost:1000` with one combined voiceover and exports the full MP4 to `output/`
- `caption`: post-combine; transcribes the full combined audio for real word timings, uses exact `02-script.md` wording, exports `output/captions.srt`
- `shorts`: side sub-workflow from `combine`; turns the finished long video into 2-4 COMPLETE vertical shorts (`1080x1920`) on ports `1100 + short number` via native portrait HyperFrames rebuilds (reused section assets + regenerated per-short voice + burned centered subtitles, NO CTA), exported to `output/shorts/`. First run: `why-cheap-products-keep-getting-worse` (3 shorts)

Sequential production skills enforce prerequisites. Main pipeline order is `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> visual-implement -> render -> review -> combine -> caption -> packaging -> upload -> learning`. Packaging now runs after `caption` (it requires topic intake, research pack, and script, and writes `output/packaging.md` + `output/thumbnails/`). `shorts` is a side sub-workflow after `combine`. As of `2026-06-26` the numbered files shifted up by one for NEW projects (voiceover `03`, visual-plan `04`, production-board `05`, review `06`, upload `07`, learning `08`); existing projects keep their original numbers, and all skills resolve step files by name suffix per `.agents/rules/video-workflow.md`. Rerunning an earlier main-pipeline dependency makes downstream main outputs stale until removed by explicit user request or regenerated in order. After voiceover, production branches by section: each section can move through visual plan, render, and review separately. Render uses fixed ports: unified preview on `localhost:1000`, section `N` on `localhost:1000 + N`.

## Current WIT

Status: `new pose-transferred set live - final WIT sign-off still pending`

Current reusable pose folder:

```text
.agents/_shared/assets/wit/poses/
```

It contains (replaced the old `wit-pose-*` 24-set on `2026-06-28`):

- `_origin_.png` - canonical neutral identity, transparent rgba (always attach this when generating any new pose)
- `pose.md` - the emotion/role catalog + quick index
- `67` pose PNGs, now TRANSPARENT RGBA cutouts (chroma-keyed in place + committed 2026-06-28) - use DIRECTLY in any video; no keying step and no `poses-keyed` folder (the green originals remain in git history)

The current WIT is the round bald white-headed mascot with a thick black outline, big rectangular glasses + dot eyes, expressive eyebrows, and a flat white body, drawn across a wide emotion/role range (boss, broke, gamer, doctor, etc.).

Mascot upgrade direction (owner-directed 2026-06-28): the plain white-blob WIT scored as a primary weakness; the target is a mascot that is a REAL character with a wide expression range and the ability to "play roles". The pose set above was pose-transferred from the studied reference casting sheet onto `_origin_` (originally delivered on a green screen, now keyed to transparent). The pose library is the starting palette; `visual-plan` may invent new poses and `visual-implement` generates them (always attaching `_origin_`). A finalized WIT sign-off is still pending owner approval.

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
