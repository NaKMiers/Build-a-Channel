# 06 Production Board

Video: `Why Everything Is a Subscription Now`

Status: `section render in progress (Sections 1-5 built + previewing)`

Source skill: `render`

Renderer: `HyperFrames 0.6.76`

## Port Map

| Section | Port | Studio URL | Comp URL |
| ------- | ---- | ---------- | -------- |
| 1 Hook | 1001 | `http://localhost:1001/#project/Build%20a%20Channel` | `http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html` |
| 2 Reframe | 1002 | `http://localhost:1002/#project/Build%20a%20Channel` | `http://localhost:1002/api/projects/Build%20a%20Channel/preview/comp/index.html` |
| 3 The Spread | 1003 | `http://localhost:1003/#project/Build%20a%20Channel` | `http://localhost:1003/api/projects/Build%20a%20Channel/preview/comp/index.html` |
| 4 Why Companies Love It | 1004 | `http://localhost:1004/#project/Build%20a%20Channel` | `http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html` |
| 5 The Free Trial | 1005 | `http://localhost:1005/#project/Build%20a%20Channel` | `http://localhost:1005/api/projects/Build%20a%20Channel/preview/comp/index.html` |

(Project id resolves to `Build a Channel` on this setup; build URLs from `/api/projects`, not the folder name.)

## Section Render Index

| # | Section | Status | Duration | Port | Big Scenes | Cues | Preview |
| --: | --- | --- | --: | --: | --: | --: | --- |
| 1 | Hook: It's More Than You Think | REMADE · built · previewing · awaiting review | 23.509s | 1001 | 3 | 12 | `section-previews/section-01-hook/index.html` |
| 2 | Reframe: You Stopped Buying, You Started Renting | REMADE · built · previewing · awaiting review | 37.909s | 1002 | 5 | 16 | `section-previews/section-02-reframe/index.html` |
| 3 | The Spread: From Apps To Your Car | built · previewing · awaiting review | 54.165s | 1003 | 5 | 19 | `section-previews/section-03-the-spread/index.html` |
| 4 | Why Companies Love It: One Sale Becomes Forever | built · previewing · awaiting review | 51.093s | 1004 | 6 | 15 | `section-previews/section-04-why-companies-love-it/index.html` |
| 5 | The Free Trial Is A Countdown | built · previewing · awaiting review | 53.867s | 1005 | 6 | 13 | `section-previews/section-05-free-trial-countdown/index.html` |
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

## Section 3 Build Record (2026-06-23, Section 1 template)

- Preview project: `section-previews/section-03-the-spread/`
- Composition: `Section03Spread` (1920x1080, 54.165s), port 1003
- Audio: `section-03-the-spread-david23-am_eric-0.8.mp3`
- Word timings: GENERATED this run via transformers.js whisper-tiny.en (none existed); pinned to word starts; duration capped at 54.165 (tail overshoot ignored)
- 5 distinct vivid bases: `base-desk` (software) → `base-tv-room` (streaming) → `base-cash` (five subs) → `base-jail` (dungeon) → `base-car` (heated seats). All CC0 via Openverse; car is a mockup target (Blaupunkt logo covered). See `assets/visual-references/section-03-the-spread/ATTRIBUTION.md`.
- Idea-devices: software window+padlock+ransom → streaming wall (vanishes)+POV → 5 sub tiles → "5>CABLE"+dungeon labels → heated-seat+padlock+EXPIRED banner.
- WIT (4 giant beats, varied side/pose): hidden-fee-panic CR → shocked L → trapped-by-app-screen C → deadpan-side-eye R. BS3 breathes. AVOIDED `typing-on-laptop`/`money-panic` (baked black bg).
- Build fixes: float overlap on track 2 (cue-d trimmed 6.20→6.18); EXPIRED banner hides the headline.
- Checks: `lint` 0 errors (1 non-blocking density note); `validate` 0 errors / 0 warnings / 40 contrast; `inspect` 0 layout issues; `snapshot` QA at 6.0/11.5/18.5/23.8/29.5/37.0/40.0/47.0/52.5.
- Review mirror: `hyperframes/review/section-03.html`. No MP4 exported.

## Section 4 Build Record (2026-06-23, Section 1 template)

- Preview project: `section-previews/section-04-why-companies-love-it/`
- Composition: `Section04Why` (1920x1080, 51.093s), port 1004
- Audio: `section-04-why-companies-love-it-david23-am_eric-0.8.mp3`
- Word timings: GENERATED this run via transformers.js whisper-tiny.en (none existed); pinned to clean word starts (a 24–26s backward-jump glitch was avoided); duration capped at 51.093
- 6 distinct vivid bases: `base-cash` (follow money) → `base-coffee` (one sale) → `base-coffee-machine` (recurring, same machine before/after) → `base-cash-lot` (worth a lot) → `base-calendar` (recurring/forgetfulness) → `base-mousetrap` (beautiful trap). All CC0 via Openverse. See `assets/visual-references/section-04-why-companies-love-it/ATTRIBUTION.md`.
- Idea-devices: FOLLOW THE MONEY word → one coin + wait-years → rising coin geyser + FOREVER → little-vs-A-LOT coin comparison + coin rain → giant RECURRING + calendar rings → BEAUTIFUL TRAP payoff.
- WIT (4 giant beats, varied side/pose): sleeping-burned-out R → empty-wallet L → confused L → suspicious R. BS1 + BS4 breathe. AVOIDED `typing-on-laptop`/`money-panic` (baked black bg).
- Build fixes: duplicate-media on the cash + coffee reuse → 2nd filename copies; S5 RECURRING/WIT overlap → WIT moved left, text/rings right; S2 sleeping WIT enlarged.
- Checks: `lint` 0 errors (1 non-blocking density note); `validate` 0 errors / 0 warnings / 30 contrast; `inspect` 0 layout issues; `snapshot` QA at 3.5/9.8/17.0/27.2/33.6/37.0/45.2/50.5.
- Review mirror: `hyperframes/review/section-04.html`. No MP4 exported.
- Review fix (2026-06-23, round 2): BS5's 4 red calendar rings circled nothing → replaced with an `AUTO-PAY · same charge every month` statement card (identical −$9.99 rows) that actually demonstrates "recurring." Re-checked clean.

## Section 5 Build Record (2026-06-23, Section 1 template)

- Preview project: `section-previews/section-05-free-trial-countdown/`
- Composition: `Section05Trial` (1920x1080, 53.867s), port 1005
- Audio: `section-05-free-trial-countdown-david23-am_eric-0.8.mp3`
- Word timings: GENERATED this run via transformers.js whisper-tiny.en (none existed); pinned to word starts; duration capped at 53.867
- 6 distinct vivid bases: `base-gift` (feel-free) → `base-desk` (pop card) → `base-hourglass` (countdown) → `base-busydesk` (forget) → `base-wallet` (ghost) → `base-piggy` (statement). All CC0 via Openverse. See section ATTRIBUTION. (Review fix: BS1/BS4 blank-phone → gift / everyday desk; all bases now distinct.)
- Real-UI idea-devices: FREE splash → credit card + form → FREE-TRIAL→$2.99 flip → Day-7 reminder fades → translucent ghost −$2.99 charges → bank statement with the `?? UNKNOWN −$3.00` row RINGED in red + EXPIRED banner.
- WIT (4 giant beats, varied side/pose): deadpan-side-eye R → hidden-fee-panic L → thinking R → holding-receipt-evidence L. S1 + S5 breathe. AVOIDED `typing-on-laptop`/`money-panic` (baked black bg).
- Build fixes: no emoji glyph (ghost = CSS card); notification grey-out via opacity (not className); the red ring nudged to land on the exact mystery-charge row; `$3 every month` label moved below the statement clear of WIT.
- Checks: `lint` 0 errors (1 non-blocking density note); `validate` 0 errors / 0 warnings / ~60 contrast; `inspect` 0 layout issues; `snapshot` QA at 4.0/10.8/17.0/19.6/27.0/35.0/44.0/51.5.
- Review mirror: `hyperframes/review/section-05.html`. No MP4 exported.
- Review fix (2026-06-23, round 2): BS1/BS4 blank-screen phone (placeholder-looking + reused) → distinct `base-gift` (free = a gift) and `base-busydesk` (forget / loud life). Re-checked clean.

## Stale / Regeneration Notes

- Sections 1-5 are rendered. Sections 6-7 are `not rendered`.
- No `07-review.md` / `08-upload.md` / `09-self-learning.md` exist yet — nothing downstream is stale.
- If `02-script.md`, the Section 1 voiceover, or the Section 1 visual plan changes, this render becomes stale and must be rebuilt.

## Next Step Boundary

Next workflow step: `Review` (Sections 1-5) or render Section 6.

Do not continue into review, upload, or learning until the user asks. Sections 6-7 still need visual-plan + render.
