# 05 Production Board

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`

Status: `section render in progress`

Source skill: `render`

Source files:

- `02-script.md`
- `03-voiceover.md`
- `04-visual-plan.md`
- `assets/asset-manifest.md` (all Section 1 assets `done` at gate time)

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 | - | - | reserved |
| Section 1 Hook | 1001 | `http://localhost:1001/#project/1-hook` | `http://localhost:1001/api/projects/1-hook/preview/comp/index.html` | stopped (owner request 2026-07-07) |
| Section 2 Reframe | 1002 | `http://localhost:1002/#project/2-reframe` | `http://localhost:1002/api/projects/2-reframe/preview/comp/index.html` | stopped (owner request 2026-07-07) |
| Section 3 Promise Machine | 1003 | `http://localhost:1003/#project/3-promise-machine` | `http://localhost:1003/api/projects/3-promise-machine/preview/comp/index.html` | live |
| Section 4 FIFA Keeps The Money | 1004 | `http://localhost:1004/#project/4-fifa-keeps-the-money` | `http://localhost:1004/api/projects/4-fifa-keeps-the-money/preview/comp/index.html` | live |
| Section 5 The Three Drains | 1005 | `http://localhost:1005/#project/5-three-drains` | `http://localhost:1005/api/projects/5-three-drains/preview/comp/index.html` | live |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook: The Trophy Prints A Receipt | `built - awaiting owner review` | 1001 | `previews/1-hook/` | section-01-hook visual plan + word timings | lint 0 err / validate 0 err / inspect 0 issues / snapshot QA passed | none (not requested) | 7 scenes, 35.904s; receipt motif born at 10.26 |
| 2 | Reframe: A Purchase, Not An Investment | `built - awaiting owner review` | 1002 | `previews/2-reframe/` | section-02-reframe visual plan + word timings | lint 0 err / validate 0 err / inspect 0 issues / snapshot QA passed (3 rounds) | none (not requested) | 5 scenes, 33.728s; trophy hero returns; pose substitution + derived wallet cutout documented in IMPLEMENTATION.md |
| 3 | The Promise Machine | `built - awaiting owner review` | 1003 | `previews/3-promise-machine/` | section-03-promise-machine visual plan + word timings | lint 0 err / validate 0 err (0 contrast warns) / inspect 0 issues / snapshot QA passed (3 rounds) | none (not requested) | 8 scenes, 60.779s; receipt motif returns; NEW hypnotized-numbers pose; mailbox generate-fallback per manifest; render adjustments in IMPLEMENTATION.md |
| 4 | FIFA Keeps The Money | `built - awaiting owner review` | 1004 | `previews/4-fifa-keeps-the-money/` | section-04-fifa-keeps-the-money visual plan + word timings | lint 0 err / validate 0 err 0 warn / inspect 0 issues / snapshot QA passed (4 rounds) | none (not requested) | 9 scenes, 62.101s; arrow direction language born; gold safe + cash bundle heroes; 2 NEW WIT poses; final payoff cue estimated ~61.40 (whisper tail regression, per plan) |
| 5 | The Three Drains | `built - awaiting owner review` | 1005 | `previews/5-three-drains/` | section-05-three-drains visual plan + word timings | lint 0 err / validate 0 err 0 warn / inspect 0 issues / snapshot QA passed (6 rounds) | none (not requested) | 7 scenes, 55.851s; drain-grate hero x4, shrinking boom-pile running gag; flock freeze [beat] -> ZURICH payoff; 1 NEW WIT pose (minister) |
| 6 | The Morning After | not rendered | 1006 | - | - | - | - | - |
| 7 | Who Decides Is Not Who Pays | not rendered | 1007 | - | - | - | - | - |
| 8 | Payoff: Check The Receipt | not rendered | 1008 | - | - | - | - | - |
| 9 | Outro: The Cheapest Host On Earth | not rendered | 1009 | - | - | - | - | - |

## Shared Asset Rules

- Video-level assets: `projects/6-why-countries-fight-to-host-the-world-cup/assets/` (single source of truth; poses in `assets/poses/`)
- Section asset junction rule: preview-local `assets` is a SYMLINK to `../../assets` (works on this Linux box; HTTP 200 verified). Fonts live in shared `assets/fonts/patrick-hand-latin.woff2`.
- Attribution file: `assets/ATTRIBUTION.md`
- Section voiceover mp3 is copied next to each section `index.html` (relative `src`).

## Active Section Notes

- Section 5: built 1:1 from the visual plan; all cues pinned to `section-05-word-timings.json` (monotonic; end clamped to 55.851s). Render-side adjustments in `previews/5-three-drains/IMPLEMENTATION.md`: 5.1 all-ground confetti base + dark numbered chips on the grates, 5.2 black-wallet grade + labels onto dark leather, 5.4 U-turn rebuilt as a real loop path, 5.5 WIT re-anchored by snapshot measurement, mirrored wrappers for the hiding local / flying flock / walking guests, 5.6 flock freeze beat (no tweens 50.54-50.82), 5.7 bye. as cream chip.
- Section 4: built 1:1 from the visual plan; all cues pinned to `section-04-word-timings.json` (final three tokens regressed -> last payoff line estimated ~61.40, scene end clamped to 62.101s, per the plan's note). Render-side adjustments in `previews/4-fifa-keeps-the-money/IMPLEMENTATION.md`: 4.6 pose substitution (`rich_flex_gold_chain_sunglasses` pixels are the plain smirk again -> `boss_suit_sunglasses_sparkle` mirrored), 4.8 built to the real scale photo geometry (hanging left pan + flat right disc; no fake beam tilt; sack lands in the real pan), 4.5 safe among the foreground lupins (photo has no lawn), 4.4 ink pad is dark blue (manifest-accepted substitution), 4.5 pointing pose mirrored in a wrapper, 4.1 mayor pose wrapper-cropped at its baked desk edge.
- Section 3: built 1:1 from the visual plan; all cues pinned to `section-03-word-timings.json` (final token corrupted -> end clamped to 60.779s, per the plan's note). Render-side adjustments in `previews/3-promise-machine/IMPLEMENTATION.md`: receipt line on a white excerpt chip (receipt PNG paper is ~37% of canvas width), 3.3 balloon strings dropped, 3.7 WIT moved to frame-right with bottom crop (photo has no waist-height barrier for the planned behind-the-bar crop) + money cluster recentered, 3.8 deflated balloons rotated to lie in the confetti, 3.4 window haze over airline tails. Scene 3.6 uses the manifest-documented mailbox generate-fallback with a warm-graded `gold-bokeh-black-1.jpg` backdrop.
- Section 2: built 1:1 from the visual plan; cues pinned to `section-02-word-timings.json` first pass (whisper duplicate backward pass at words 91-109 skipped per the plan; end clamped to 33.728s). Render-side decisions in `previews/2-reframe/IMPLEMENTATION.md`: pose substitution (`rich_flex_gold_chain_sunglasses.png` pixels do not match its `pose.md` catalog entry - plain smirk, no chain/sunglasses; used `boss_suit_sunglasses_sparkle.png` instead, copied to `assets/poses/`), derived `assets/wallet-empty-cutout.png` (white studio bg keyed; `mix-blend-mode` is isolated in the capture path), 2.1 ribbon/sticker rearranged below the chip arc, 2.4 CSS boutique backdrop + counter line for the chest-up panic WIT.
- Section 1: built 1:1 from the visual plan; every cue pinned to `section-01-word-timings.json` (pre-existing, verified monotonic). Render-side deviations (map seam crop-out, receipt plinth pivot, pan distance -1100, S7 drape off the face) documented in `previews/1-hook/IMPLEMENTATION.md`.
- Known snapshot-tool artifact: first captured frame of a run can miss a late-decoding PNG (screenshot fallback mode). All elements verified present via re-snaps. Re-check if MP4 export is requested.
- Environment (Linux box, first render here): unprivileged port floor lowered to 1000 via `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=1000` - NOT persistent across reboots; re-run before starting servers or persist in `/etc/sysctl.d/`.

## Stale / Regeneration Notes

- None. No downstream outputs exist yet (review/combine/caption/packaging not run).

## Next Step Boundary

Next workflow step: `Review` (owner reviews Section 3 on `localhost:1003`, Section 4 on `localhost:1004`, and Section 5 on `localhost:1005`; Sections 1-2 built, their servers stopped per owner request - restart on demand)

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
