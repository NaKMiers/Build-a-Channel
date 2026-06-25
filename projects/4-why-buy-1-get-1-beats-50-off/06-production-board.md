# 06 Production Board

Video: `Why Buy 1 Get 1 Free Beats 50% Off`

Status: `COMBINED + final MP4 exported`

Source skill: `combine`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 | `http://localhost:1000/#project/full-video` | `http://localhost:1000/api/projects/full-video/preview/comp/index.html` | combined ✓ |
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

## Combine / Final Export

- Combine workspace: `hyperframes/full-video/` — parent composition `UnifiedBuy1Get1` mounts all 7 audio-stripped section builds (`compositions/section-01.html` … `section-07.html`) at cumulative offsets; assets consolidated at root (`assets/fonts`, `assets/wit`, `assets/visual-references/section-0N-*`).
- Combined voiceover: `hyperframes/full-video/combined-voiceover.mp3` (ffmpeg concat of the 7 section mp3s in order, 243.528s).
- Section mount offsets (start / duration, seconds): S1 0/23.088 · S2 23.088/40.536 · S3 63.624/32.304 · S4 95.928/37.152 · S5 133.080/36.480 · S6 169.560/34.992 · S7 204.552/38.976.
- Unified preview: `localhost:1000` (project id `full-video`), lint 0 errors, all 7 sections snapshot-verified mounting in order with real bases + WIT.
- **Final video: `output/4-why-buy-1-get-1-beats-50-off.mp4`** — 1920×1080 H.264 + AAC, 243.56s, 41.3 MB, standard quality. Rendered via `renders/` staging then moved to `output/`; `renders/` removed (left empty). `output/` is the single home for all final deliverables.

## Shared Asset Rules

- Video-level assets: `projects/4-why-buy-1-get-1-beats-50-off/assets/` (source of truth; bases under `assets/visual-references/section-01-hook/`, WIT under `assets/wit/`, font under `assets/fonts/`)
- Section asset junction rule: junctions 404 on this Windows HyperFrames setup — each section preview uses a minimal REAL local `assets/` working set (font + the section's bases + the section's WIT poses) copied from the project library.
- Attribution file: `assets/visual-references/section-01-hook/ATTRIBUTION.md` (magic hat is CC BY-SA 3.0 — credit "Magicianidris" if it ships).

## Active Section Notes

- Section 1 word timings generated to `voiceover/section-01-hook/section-01-word-timings.json` (transformers.js whisper-tiny.en; tail hand-corrected). Every cue/scene cut pinned to it.
- Review mirror: `hyperframes/review/section-01.html` (+ its own minimal assets).
- QA: `section-previews/section-01-hook/snapshots/contact-sheet.jpg`.

## Stale / Regeneration Notes

- All 7 sections are rendered and combined into `output/4-why-buy-1-get-1-beats-50-off.mp4`. If any section's `02-script.md`, voiceover, visual plan, or section build changes, the section preview AND the combined output become stale — rerun that section's render, then rerun `combine` (it re-concats the voiceover and re-exports the MP4).
- No `07-review.md` / `08-upload.md` / `09-self-learning.md` exist yet — nothing downstream to stale.

## Caption — 22 languages (2026-06-25)

Generated YouTube captions in all 22 supported languages from the FULL combined audio (real word-level timing), with English display text taken verbatim from `02-script.md`.

- Audio source: `hyperframes/full-video/combined-voiceover.mp3` (decoded 243.464s; board concat reports 243.528s — ~64ms mp3-frame rounding, within tolerance).
- Transcription: `Xenova/whisper-tiny.en` via `@xenova/transformers`, word timestamps over the whole timeline in one pass → **842 words**. Saved to `voiceover/combined-word-timings.json`.
- Alignment: Needleman-Wunsch of 843 script tokens (cues from `02-script.md` narration) against 832 hyp words → **95 cues**. Timing table emitted to `voiceover/_segments.json`.
- Whisper tail glitch (known whisper-tiny artifact): final words `be slightly harder to trick` jumped backward to ~235.7s while `Now go` sat at 241.4s. Last cue START (241.38s) was correct; only its END was short. Extended the final cue end to the audio duration (243.464s) per the documented fix, then regenerated `english.srt` from the corrected `_segments.json` so English + all translations share identical timing.
- Validation: 0 overlaps, 0 zero/negative-duration, monotonic, gapless; first cue `00:00:00,000`, last cue ends `00:04:03,464` (== audio duration).
- Sync cross-check vs combine section offsets (all within 0.25s): S2 23.20 vs 23.088 · S3 63.81 vs 63.624 · S4 96.00 vs 95.928 · S5 133.28 vs 133.080 · S6 169.62 vs 169.560 · S7 204.80 vs 204.552.
- Translation: each of the 21 other languages is a cue-for-cue translation of the English cue table (95 cues, same count/order), written via `write-translated-srt.mjs` (count-guard enforced).
- Output: **`output/captions/<language>.srt`** — 22 files (English + 21 translations). Compatibility `output/captions.srt` (English) kept at output root.
- Hard gate PASSED: every `<language>.srt` = **95 cues** with **byte-identical timestamps** to `english.srt` (0 mismatches across all 22), 0 empty cues, valid UTF-8 (Arabic / CJK / Indic / Thai render clean, no mojibake). Proper nouns (Dan Ariely, Wedgwood) kept verbatim.
- No `.vtt` requested.

## Next Step Boundary

Next workflow step: `upload` (then `learning`); `shorts` is an optional side sub-workflow from here.

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
