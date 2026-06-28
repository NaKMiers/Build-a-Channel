# Section 7 Render Design

Video: `Why Cheap Products Keep Getting Worse`
Section: `Section 7: Replacement Becomes Normal`
Composition: `Section07ReplacementBecomesNormal` (`1920x1080`, `data-duration 29.312`)
Port: `1007`

## Structure

- 3 big scenes (track 1): `scene-ewaste` 0/11.74, `scene-system` 11.74/9.4, `scene-subscription` 21.14/8.172
- 7 cue states (track 2): replacement-normal, not-waste, system-easier, four-reasons, buy-again, receipt-loop, subscription
- Scene cuts at `11.74` and `21.14`
- 3 WIT beats: `facepalm` (held cues 1-2), `holding-receipt-evidence` (cue 5), `deadpan-side-eye` (cue 7); Scene 2 WIT-free

## Scene bases

- Scene 1: real e-waste photo (`assets/section-07/ewaste-pile-photo-base.jpg`, Reconrabbit, CC0), clean
- Scene 2: real fulfillment-boxes photo (`assets/section-07/fulfillment-boxes-photo-base.jpg`, WillNemoy, CC BY-SA 4.0), clean
- Scene 3: real warm cherry-wood surface (`assets/section-07/checkout-wood-photo-base.jpg`, Dietmar Rabich, CC BY-SA 4.0) + CSS objects on top (new box, smiling price tag, re-buy receipt). Replaced the original flat CSS counter + card-reader background on 2026-06-21 after review ("looked bad").

## Timing

`estimated` - no word-timings file; whisper-cpp not available to generate one. Cue times estimated from the marked script + 29.312s. GSAP timed reveals: landfill note 5.79; four reasons 16.17/17.5/19.36; price-tag smile 23.18; deadpan payoff 26.7.

## Motion rules

- hard-show default; no transitions/impact effects
- WIT-bearing cues use `data-layout-allow-overflow` + `overflow:visible` (intentional off-canvas giant WIT)
- payoff underline = `border-bottom` on the text span (full text width, one line)

## Checks

- lint 0 err / validate 0 err (5 contrast warnings, dark-label style) / inspect 0 layout issues across 9 samples
- snapshot QA at `2,8,13,18,20,22.5,25,28`

## Known notes

- Timing is estimated; confirm sync in Studio against the audio (or re-pin from a generated word-timings file later).
- Scene 1's e-waste photo has a baked-in "ALL TRASH" arrow - generic and on-theme; left as-is.
