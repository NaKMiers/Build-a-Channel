# 06 Production Board

Video: `Why Cheap Products Keep Getting Worse`

Status: `section 1 review-adjusted connected-scene remake preview and MP4 ready for review`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 |  |  | reserved |
| Section 1 Hook | 1001 | `http://localhost:1001/#project/section-01-hook` | `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html` | running |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Render file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook | `review-adjusted connected-scene remake preview and MP4 ready for review` | 1001 | `section-previews/section-01-hook/` | `02-script.md` + `04-voiceover.md`; old `05-visual-plan.md` skipped by explicit user request; user reviews applied: big scenes, fewer cues, meaningful markup, larger WIT | `lint: pass with 2 non-blocking warnings`; `validate: pass`; `inspect: pass`; `ffprobe: pass` | `renders/section-01-hook/section-01-hook-remake.mp4` | `3 persistent big scenes with 7 voice-timed cue overlays. Uses only real project WIT PNG poses from assets/wit. No transitions or element animations. Local MP3 path is used directly; audio helper is no longer required.` |

## Shared Asset Rules

- Video-level assets: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section asset rule: keep the project asset library as source of truth; current Section 1 preview materializes a minimal hardlinked working set under `section-previews/section-01-hook/assets/` because HyperFrames CLI checks previously returned asset 404s when the local `assets/` path was a junction
- Attribution file: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Active Section Notes

- Section 1 composition id: `Section01Hook`
- Runtime: `21.205s` composition; MP4 container duration `21.248s`
- Voiceover runtime: `21.205s`
- Screen changes: instant hard cuts only; no push, slide, fade, wipe, photo zoom, board entrance, or cross-screen transition remains
- Preview audio: local `section-01-hook-david23-am_eric-0.84.mp3` served through the HyperFrames preview project
- Scene grammar: `chair setup evolves through product details, purchase, and first week -> broken-leg close-up evolves through legal creak and screw/career-options failure -> cost board evolves through true-cost receipt and final future-not-included payoff`
- Real direct-use assets: `real-blank-tag-pexels-padrinan.jpg`, `real-receipt-pexels-towfiqu-barbhuiya.jpg`
- Generated support assets: `chair-price-tag`, `hidden-future-tag`, `wobbly-leg-loose-screw`, `price-tag-receipt`
- WIT poses used: `wit-pose-thinking.png`, `wit-pose-price-tag-suspicion.png`, `wit-pose-suspicious.png`, `wit-pose-betrayed.png`, `wit-pose-holding-receipt-evidence.png`
- MP4 frame verification: `renders/section-01-hook/mp4-check-frames/contact-sheet.png`
- Temporary render dependency: FFmpeg/FFprobe were installed in `%TEMP%/wiw-ffmpeg-static` because no system FFmpeg was available
- User review applied: avoid many unrelated full-scene cuts in a short section; build connected big scenes, then change one or two cue elements inside the big scene while the narration advances
- Latest review applied: removed meaningless red leg marks, removed the white wash overlay from the failure photo, enlarged WIT, reduced cue states from `12` to `7`, and corrected the screw callout to circle the actual screw in exported MP4 frame `frame-05.png`

## Stale / Regeneration Notes

- No downstream files were present during this render run: `07-review.md`, `08-upload.md`, `09-self-learning.md`
- If Section 1 is rerendered later, any future review, upload, learning, unified preview, or final render outputs for this section become stale and must be regenerated in order

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
