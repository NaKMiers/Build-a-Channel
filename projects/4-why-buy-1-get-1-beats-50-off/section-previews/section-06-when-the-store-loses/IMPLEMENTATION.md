# Section 6 Render Implementation

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 6: When The Store Loses`
Status: `built to subscription bar, ready for review`

## Result

- Preview project: `section-previews/section-06-when-the-store-loses/`
- Composition: `Section06Loses`
- Port: `1006`
- Studio URL: `http://localhost:1006/#project/section-06-when-the-store-loses`
- Direct composition URL: `http://localhost:1006/api/projects/section-06-when-the-store-loses/preview/comp/index.html`
- Runtime: `34.923s`
- Word timings: `voiceover/section-06-when-the-store-loses/section-06-word-timings.json` (one whisper duplicate ~21.8–25.5; the continuous pass was used for cue anchors; clean tail to 34.56)

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice Cue | Scene | What Changes | Motion | WIT | Sync |
|---:|---:|---|---|---|---|---|---|
| A1 | 0.40 | "okay, fair is fair" | A produce | caption | hard-show | awkward-celebration R ~1320 | word |
| A2 | 4.50 | "sometimes they lose too" | A | "the store can LOSE too" | impact | - | word |
| A3 | 6.00 | "Good." | A | "…good." stamp | pop | - | word |
| B1 | 7.80 | "milk, bread, eggs" | B milk | "milk·bread·eggs" tag | pop | thinking L ~1320 | word |
| B2 | 10.08 | "give one away… lose money" | B | "barely any profit → LOSE money" chip | impact | - | word |
| C1 | 13.76 | "Bait." | C lure | "BAIT" | impact | suspicious R ~1320 | word |
| C2 | 14.92 | "a loss leader" | C | "a loss leader" | hard-show | - | word |
| C3 | 18.18 | "fill the rest of the cart" | C | "drags you in → fill the cart" chip | hard-show | - | word |
| C4 | 21.16 | "spoiler, you will" | C | "spoiler: you will" stamp | impact | - | word |
| D1 | 24.74 | "two-for-one you can't finish" | D fridge | "2-for-1 you can't finish" | hard-show | confused L ~1300 | word |
| D2 | 27.62 | "science experiments in the fridge" | D | "→ science experiments…" | impact | - | word |
| E1 | 32.06 | "binning a free yogurt" | E bin | "binning a 'free' yogurt" | hard-show | facepalm R ~1320 | word |
| E2 | 33.76 | "you forgot you owned" | E | "…you forgot you owned" | hard-show | - | word |

## Render Review-Prevention Pass

- voice cue map from `section-06-word-timings.json` (continuous pass; duplicate segment ignored)
- subscription bar up front: 5 FRESH distinct bases (no reuse), giant WIT, kinetic devices, motion
- TEXT CLEAN: one hero + one short support per scene, vertically spaced ≥~150px, revealed SEQUENTIALLY, all OPPOSITE the giant WIT, side-gradient scrim on the text half - no stacked/overlapping text
- WIT density: 5 (1/scene), giant ~1280–1320px; sides R/L/R/L/R; poses awkward-celebration/thinking/suspicious/confused/facepalm
- HyperFrames mechanics: lint 0 errors (1 advisory), validate 0 errors, deterministic GSAP, sequential cue track, audio clip

## Verification

- lint: 0 errors, 1 warning (timeline_track_too_dense advisory)
- validate: 0 errors, 0 warnings, 25 non-blocking contrast advisories
- contact sheets: `snapshots/contact-sheet-1.jpg` + `-2.jpg` at 12 timestamps - fresh distinct bases, no text overlap, giant WIT clear, bait/fridge/bin payoff reads
- export/render: not requested (no MP4)

## Notes

- Bases: produce flat-lay (CC0), milk bottles (CC BY), red fishing lure (CC0), open night fridge (CC BY-SA), litter bin (CC BY-SA). All fresh for S6. WIT shared poses. Local working-set assets.
- Applied the two new SKILL rules (fresh bases per section + no stacked text) from the first pass.

## 2026-06-24 KINETIC REMAKE (owner: "remake completely, reference subscription-now")

Rebuilt the devices to be genuinely kinetic/accumulating like subscription S1 (kept the 5 fresh bases, now BRIGHT ~0.78–0.85 with light text-side scrim, giant WIT):
- A: profit counter MORPHS `+$2` (green) → `−$1` (red) on "sometimes they lose too."
- B: staple TOASTS RAIN (milk/bread/eggs pop sequentially) → "give one away → store LOSES money" chip.
- C: "BAIT" smash → cart-item toasts pop (snacks +$7, wine +$12) → "+$52" total counter → "spoiler: you will" stamp (accumulation).
- D: a "USE BY: 3 days" countdown card FLIPS to "SCIENCE EXPERIMENT / EXPIRED" (subscription countdown-flip pattern).
- E: a CSS yogurt cup DROPS into the bin (bounce) → "BINNED." stamp.
Copied subscription S1 patterns (counter morph, toast rain, accumulation, countdown flip). Re-validated 0 errors; re-snapshotted at 11 timestamps - all devices animate, bright bases, giant WIT clean; comp serves HTTP 200; mirror synced.
