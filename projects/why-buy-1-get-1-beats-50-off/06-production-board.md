# 06 Production Board

Video: `Why Buy 1 Get 1 Free Beats 50% Off`

Status: `section render in progress`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 | | | reserved |
| Section 1 | 1001 | `http://localhost:1001/#project/section-01-hook` | `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html` | running |
| Section 2 | 1002 | `http://localhost:1002/#project/section-02-same-to-you-not-to-them` | `http://localhost:1002/api/projects/section-02-same-to-you-not-to-them/preview/comp/index.html` | running |
| Section 3 | 1003 | `http://localhost:1003/#project/section-03-the-receipt-knows` | `http://localhost:1003/api/projects/section-03-the-receipt-knows/preview/comp/index.html` | running |
| Section 4 | 1004 | `http://localhost:1004/#project/section-04-the-magic-word` | `http://localhost:1004/api/projects/section-04-the-magic-word/preview/comp/index.html` | running |
| Section 5 | 1005 | `http://localhost:1005/#project/section-05-the-price-never-drops` | `http://localhost:1005/api/projects/section-05-the-price-never-drops/preview/comp/index.html` | running |
| Section 6 | 1006 | `http://localhost:1006/#project/section-06-when-the-store-loses` | `http://localhost:1006/api/projects/section-06-when-the-store-loses/preview/comp/index.html` | running |
| Section 7 | 1007 | `http://localhost:1007/#project/section-07-free-cuts-your-judgment` | `http://localhost:1007/api/projects/section-07-free-cuts-your-judgment/preview/comp/index.html` | running |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook: You're The Rabbit | built, ready for review | 1001 | `section-previews/section-01-hook/` | `visual-plan/section-01-hook/` | lint ✓ / validate ✓ (10 non-blocking contrast) / snapshot ✓ | none (no MP4 requested) | 3 scenes, 7 cues, word-pinned, magic-show motif |
| 2 | Same To You, Not To Them | built, ready for review | 1002 | `section-previews/section-02-same-to-you-not-to-them/` | `visual-plan/section-02-same-to-you-not-to-them/` | lint ✓(2 advisory) / validate ✓(15 contrast) / snapshot ✓ | none (no MP4 requested) | 5 scenes, 11 cues, math shown on screen word-pinned; real Wedgwood jasperware |
| 3 | The Receipt Knows | remade (subscription style), ready for review | 1003 | `section-previews/section-03-the-receipt-knows/` | `visual-plan/section-03-the-receipt-knows/` | lint ✓(2 advisory) / validate ✓(contrast only) / snapshot ✓ | none (no MP4 requested) | 5 scenes, vivid dark money bases + giant kinetic $5→$10 + giant WIT + glowing FREE; word-pinned |
| 4 | The Magic Word | built (subscription bar), ready for review | 1004 | `section-previews/section-04-the-magic-word/` | `visual-plan/section-04-the-magic-word/` | lint ✓(2 advisory) / validate ✓(contrast only) / snapshot ✓ | none (no MP4 requested) | 5 scenes; vivid bases + giant FREE + NUMBER-vs-FEELING + hostage shampoo + giant WIT; word-pinned |
| 5 | The Price Never Drops | remade KINETIC (subscription style), ready for review | 1005 | `section-previews/section-05-the-price-never-drops/` | `visual-plan/section-05-the-price-never-drops/` | lint ✓(1 advisory) / validate ✓(contrast only) / snapshot ✓ | none (no MP4 requested) | 5 FRESH bases; kinetic devices ($10 snap-back, $10→$5 morph, +1 toast, banner takeover, animated want-meter); giant WIT; word-pinned |
| 6 | When The Store Loses | remade KINETIC (subscription style), ready for review | 1006 | `section-previews/section-06-when-the-store-loses/` | `visual-plan/section-06-when-the-store-loses/` | lint ✓(1 advisory) / validate ✓(contrast only) / snapshot ✓ | none (no MP4 requested) | 5 FRESH bright bases; kinetic devices (profit morph +$2→−$1, toast rain, cart fill +$52, use-by→EXPIRED flip, yogurt drop+BINNED); giant WIT; word-pinned |
| 7 | Payoff: Free Cuts Your Judgment | built (full bar, kinetic), ready for review | 1007 | `section-previews/section-07-free-cuts-your-judgment/` | `visual-plan/section-07-free-cuts-your-judgment/` | lint ✓(1 advisory) / validate ✓(contrast only) / snapshot ✓ | none (no MP4 requested) | 5 FRESH bright bases (chess→scissors→calculator→mask→cards); kinetic; giant WIT R/L/R/L/R; word-pinned |

## Shared Asset Rules

- Video-level assets: `projects/why-buy-1-get-1-beats-50-off/assets/` (source of truth; bases under `assets/visual-references/section-01-hook/`, WIT under `assets/wit/`, font under `assets/fonts/`)
- Section asset junction rule: junctions 404 on this Windows HyperFrames setup — each section preview uses a minimal REAL local `assets/` working set (font + the section's bases + the section's WIT poses) copied from the project library.
- Attribution file: `assets/visual-references/section-01-hook/ATTRIBUTION.md` (magic hat is CC BY-SA 3.0 — credit "Magicianidris" if it ships).

## Active Section Notes

- Section 1 word timings generated to `voiceover/section-01-hook/section-01-word-timings.json` (transformers.js whisper-tiny.en; tail hand-corrected). Every cue/scene cut pinned to it.
- Review mirror: `hyperframes/review/section-01.html` (+ its own minimal assets).
- QA: `section-previews/section-01-hook/snapshots/contact-sheet.jpg`.

## Stale / Regeneration Notes

- Only Section 1 is rendered. If `02-script.md` S1, S1 voiceover, or S1 visual plan changes, this preview becomes stale.
- No `07-review.md` / `08-upload.md` / `09-self-learning.md` exist yet — nothing downstream to stale.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
