# 05 Production Board

Video: `Vì sao giá vàng tăng điên cuồng?` (Vietnamese-language experiment)
Status: `Section 1 rendered (preview)`
Source skill: `render`
Source files: `02-script.md`, `03-voiceover.md`, `04-visual-plan.md`, `assets/asset-manifest.md`

## Port Map

| Target | Port | Direct URL | Status |
|---|---:|---|---|
| Unified preview | 1000 | - | reserved |
| Section 1: Hook | 1001 | http://localhost:1001/#project/section-01-hook | running |

## Section Render Index

| # | Section | Status | Port | Preview project | Audio | Checks | Notes |
|---:|---|---|---:|---|---|---|---|
| 1 | Hook | preview built | 1001 | `section-previews/section-01-hook/` | `section-01-hook-nam-minh.mp3` (29.352s, edge-tts vi) | lint 0 err / validate 0 err (warnings) | 5 scenes, composited from `assets/` |

## Composition

- `Section01Hook`, 1920×1080, root duration `29.352s`, audio wired (track 10).
- 5 scenes (per visual plan), composited from pre-made assets in `assets/` (built by `visual-implement`):
  - S1 white + `gold-bar-on-table.jpg` + `pose_deadpan_unimpressed_half_lidded` + 3 struck labels
  - S2 `gold-shop-crowd.png` (no-face) + `pose_excited_giddy_fists_at_face`
  - S3 `gold-price-chart-rising.png` + `pose_hugging_gold_bar_eyes_gold` (NEW pose) at the peak
  - S4 white + `gold-bar-on-table.jpg` (reused) + `gold-glowing-brain.png` + `pose_pondering_skeptical_hand_on_chin` + 2 questions
  - S5 white focus + `pose_deadpan_unimpressed_half_lidded` (reused) + title + `doodle-scalpel.png`
- Timing basis: `estimated` (no word-timings for the Vietnamese audio this run).

## QA (snapshot contact sheet)

Works end-to-end. Known issues (test-acceptable):
1. **Placeholder poses are boxy on photo scenes** - the 3 Vui Vẻ placeholder PNGs are not transparent, so a white box shows around the mascot on the S2 crowd photo. Resolved when the real channel WIT poses (transparent) are made. On white scenes they blend fine.
2. **Gold "?" low contrast on white** (S4) - add a dark outline / darker gold.
3. **Minor overlap** (S1) - the 3rd struck label crosses the gold-bar photo; nudge label up or bar down.
4. **White quote on the light chart** (S3) - strengthen shadow / add a small backing for readability.
5. Estimated timing - re-pin to real word timings if a Vietnamese word-timer is added.

## Shared Asset Rules

- Video-level assets: `projects/<slug>/assets/` (+ `asset-manifest.md`, `ATTRIBUTION.md`).
- Section junction: `section-previews/section-01-hook/assets` → `../../assets` (Windows junction).
- Poses for S1/S2/S4/S5 are Vui Vẻ TEST placeholders; regenerate with channel WIT before any publish.

## Stale / Regeneration Notes

- If `04-visual-plan.md` Section 1 changes → rerun `visual-implement` + `render` for Section 1.
- Sections 2–7 not yet planned/rendered.

## Next Step Boundary

Next workflow step: `Review`. Do not continue into review/upload/learning until asked.
