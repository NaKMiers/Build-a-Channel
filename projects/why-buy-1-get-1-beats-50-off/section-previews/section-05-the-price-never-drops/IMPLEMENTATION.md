# Section 5 Render Implementation

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 5: The Price Never Drops`
Status: `built to subscription vivid-hook bar, ready for review`

## Result

- Preview project: `section-previews/section-05-the-price-never-drops/`
- Composition: `Section05Anchor`
- Port: `1005`
- Studio URL: `http://localhost:1005/#project/section-05-the-price-never-drops`
- Direct composition URL: `http://localhost:1005/api/projects/section-05-the-price-never-drops/preview/comp/index.html`
- Runtime: `36.416s`
- Word timings: `voiceover/section-05-the-price-never-drops/section-05-word-timings.json` (tail `27.2s+` hand-estimated — whisper-tiny dropped the final segment and looped; clean through "a lot" @26.94)

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice Cue | Scene | What Changes | Motion | WIT | Sync |
|---:|---:|---|---|---|---|---|---|
| A1 | 0.40 | "Trick #3, the sneaky one" | A cash | label | hard-show | price-tag-suspicion R ~1320 | word |
| A2 | 2.16 | "the price on the sign" | A | "$10 on the sign" tag | pop | — | word |
| A3 | 3.24 | "never drops" | A | blocked ↓ arrow + "never drops" | hard-show | — | word |
| B1 | 5.52 | "whispers" | B coins | whisper line | hard-show | deadpan-side-eye L ~1320 | word |
| B2 | 6.50 | "only really worth" | B | "$10" struck (real worth?) | pop | — | word |
| B3 | 8.80 | "five is the normal price now" | B | "$5 feels normal now" | pop | — | word |
| B4 | 11.34 | "looks cheap forever" | B | "LOOKS CHEAP forever" stamp | impact | — | word |
| C1 | 12.88 | "keeps that proud $10" | C curtain | proud gold $10 tag | pop | shocked C ~1320 | word |
| C2 | 18.48 | "a bonus on top" | C | "+1 FREE — a bonus" badge | impact | — | word |
| D1 | 20.02 | "stores love that" | D cash | "Stores LOVE this" | hard-show | facepalm R ~1280 | word |
| D2 | 21.74 | "without admitting it's cheap" | D | "a sale without admitting it's cheap" | hard-show | — | word |
| E1 | 23.68 | "they pick this shape on purpose" | E coins | label | hard-show | empty-wallet L ~1320 | word |
| E2 | 25.74 | "you want the first one a lot" | E | FIRST want card (hot) | pop | — | word |
| E3 | 27.60 | "the second one, eh, not really" | E | SECOND meh card | pop | — | word(est) |
| E4 | 33.74 | "charge full for the first" | E | "FULL price for #1, #2 free" stamp | impact | — | word(est) |

## Render Review-Prevention Pass

- voice cue map: from `section-05-word-timings.json`; Scene E tail (27.2s+) hand-estimated monotonic (whisper dropped it) and labeled
- subscription bar applied up front: vivid dark bases + giant CSS price-tag devices + giant WIT + 5 scenes + motion
- WIT density: 5 (1/scene), giant ~1280–1340px; sides R/L/C/R/L (well varied); poses price-tag-suspicion/deadpan/shocked/facepalm/empty-wallet
- collisions: devices arranged opposite each WIT; checked in contact sheets — clear
- HyperFrames mechanics: lint 0 errors (2 advisory), validate 0 errors, deterministic GSAP, sequential cue track, audio clip

## Verification

- lint: 0 errors, 2 warnings (timeline_track_too_dense advisory)
- validate: 0 errors, 0 warnings, 35 non-blocking contrast advisories
- contact sheets: `snapshots/contact-sheet-1.jpg` + `-2.jpg` at 11 timestamps — anchoring shrink/proud price/want-meter all read, giant WIT, no bad crops
- export/render: not requested (no MP4)

## Notes

- (superseded) v1 lazily reused cash/coins/curtain bases from other sections and stacked overlapping text.

## 2026-06-24 REMAKE (owner feedback)

Owner: "remake from scratch — you reuse too many images from other sections, don't be lazy; texts are covered by many texts; this section looks so bad." Two fixes:
1. **Fresh distinct bases** — replaced the recycled cash/coins/curtain with 5 newly-sourced retail photos (shelf price tags → red 50%/30% sale store → boutique mannequins → canned-goods aisle → HE/SHE clothing shop). None reused from S1–S4.
2. **Clean text** — one hero device per beat (a price tag / a single stacked shrink card / a proud tag / two short lines / a want-card pair), all well-spaced and revealed sequentially on their words so nothing overlaps. Side-gradient scrims darken only the text half. Giant WIT (~1280–1320px) alternating R/L/R/L/R, devices on the opposite half.
- Re-validated 0 errors; re-snapshotted at 9 timestamps — text never overlaps, bases distinct, giant WIT clear. Comp serves HTTP 200; mirror synced.
