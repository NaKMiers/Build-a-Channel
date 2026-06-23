# 06 Production Board

Video: `Why Everything Is a Subscription Now`

Status: `section render in progress (Sections 1-2 built + previewing)`

Source skill: `render`

Renderer: `HyperFrames 0.6.76`

## Port Map

| Section | Port | Studio URL | Comp URL |
| ------- | ---- | ---------- | -------- |
| 1 Hook | 1001 | `http://localhost:1001/#project/Build%20a%20Channel` | `http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html` |
| 2 Reframe | 1002 | `http://localhost:1002/#project/Build%20a%20Channel` | `http://localhost:1002/api/projects/Build%20a%20Channel/preview/comp/index.html` |

(Project id resolves to `Build a Channel` on this setup; build URLs from `/api/projects`, not the folder name.)

## Section Render Index

| # | Section | Status | Duration | Port | Big Scenes | Cues | Preview |
| --: | --- | --- | --: | --: | --: | --: | --- |
| 1 | Hook: It's More Than You Think | REMADE · built · previewing · awaiting review | 23.509s | 1001 | 3 | 12 | `section-previews/section-01-hook/index.html` |
| 2 | Reframe: You Stopped Buying, You Started Renting | REMADE · built · previewing · awaiting review | 37.909s | 1002 | 5 | 16 | `section-previews/section-02-reframe/index.html` |
| 3 | The Spread | not rendered | 54.165s | 1003 | — | — | — |
| 4 | Why Companies Love It | not rendered | 51.093s | 1004 | — | — | — |
| 5 | The Free Trial | not rendered | 53.867s | 1005 | — | — | — |
| 6 | Easy In, No Way Out | not rendered | 53.013s | 1006 | — | — | — |
| 7 | Payoff | not rendered | 54.101s | 1007 | — | — | — |

## Section 1 Build Record (REMADE 2026-06-23)

Original build rejected on review (mundane photos, boring WIT, repetitive cream label boxes). Remade:

- Preview project: `section-previews/section-01-hook/`
- Composition: `Section01Hook` (1920x1080, 23.509s)
- Audio: `section-01-hook-david23-am_eric-0.8.mp3`
- Word timings: `voiceover/section-01-hook/section-01-word-timings.json`
- Design: vivid real bases (coins → cash → padlocks) + loved CSS real-UI — colorful app-grid, jumping "12+" counter, notification charge toasts, free-trial countdown→charge, full-screen EXPIRED modal, padlock-wall + kinetic payoff. No cream label boxes.
- Bases: `base-coins.jpg` (CC0), `base-cash.jpg` (CC BY), `base-padlock.jpg` (CC BY) — see section ATTRIBUTION.
- WIT poses: price-tag-suspicion, hidden-fee-panic, holding-phone-panic, trapped-by-app-screen (4 beats). Avoided `money-panic` (baked black bg).
- Checks: `lint` 0/0; `validate` 0 errors / 0 warnings / 40 non-blocking contrast warnings; `snapshot` QA at 1.2/5.9/8.6/13.2/18.2/21.2.
- Review mirror: `hyperframes/review/section-01.html`. No MP4 exported.

## Section 2 Build Record (REMADE 2026-06-23 to the Section 1 template)

Owner asked to remake S2 completely, based on S1. The prior build broke the standing template (one phone
base graded 4×; repeated cream label boxes; small WIT). Remade to `vivid object bases → varied CSS
idea-devices → giant WIT that varies per scene`.

- Preview project: `section-previews/section-02-reframe/`
- Composition: `Section02Reframe` (1920x1080, 37.909s)
- Audio: `section-02-reframe-david23-am_eric-0.8.mp3`
- Word timings: `voiceover/section-02-reframe/section-02-word-timings.json` (whisper-tiny.en; word starts clean, tail overshoot 39.16 ignored → duration 37.909)
- Bases (5 distinct vivid objects, one per scene): `base-night-phone.jpg` (defuse) → `base-vinyl.jpg` (own) → `base-phone-rent.jpg` (rent, non-consecutive device callback) → `base-padlock.jpg` (lock) → `base-devices-flatlay.jpg` (question). All CC0; see `assets/visual-references/section-02-reframe/ATTRIBUTION.md`.
- Idea-devices (varied): struck RANT banner + ✓ app tiles; OWN stamp + receipt; subscription paywall + OWN→RENT swap + toggle; MISS A PAYMENT banner + lock-screen card; kinetic headline + RENT tags + payoff. Only 2 cream asides.
- WIT poses (giant, varied side/scale/pose): facepalm RIGHT → thinking LEFT → betrayed CENTER giant → suspicious RIGHT (4 beats, BS3 breathes). Avoided `money-panic` (baked black bg).
- Build fixes: the `smash` helper ignores `scaleX`, so the struck-banner line uses an explicit scaleX tween; smashed elements use explicit left/top.
- Checks: `lint` 0 errors (1 non-blocking density note); `validate` 0 errors / 0 warnings / 45 contrast; `inspect` 0 layout issues; `snapshot` QA at 1.4/6.0/11.6/18.6/23.8/27.9/33.6/36.8.
- Review mirror: `hyperframes/review/section-02.html`. No MP4 exported.
- Review fixes (2026-06-23, round 2): BS1 base swapped to `base-apps-phone.jpg` (owner: aurora "not suitable"); BS3 `OWN`/`RENT` un-stacked (text-on-text); BS5 RENT tags hidden when payoff lands; all 4 WIT enlarged to giant (width 1200–1300, high anchor). Re-checked lint/validate/inspect clean; snapshots verified.

## Stale / Regeneration Notes

- Sections 1-2 are rendered. Sections 3-7 are `not rendered`.
- No `07-review.md` / `08-upload.md` / `09-self-learning.md` exist yet — nothing downstream is stale.
- If `02-script.md`, the Section 1 voiceover, or the Section 1 visual plan changes, this render becomes stale and must be rebuilt.

## Next Step Boundary

Next workflow step: `Review` (Section 1).

Do not continue into review, upload, or learning until the user asks. Sections 2-7 still need visual-plan + render.
