# Section 3 Render Implementation

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 3: The Receipt Knows`
Status: `section preview built, ready for review`

## Result

- Preview project: `section-previews/section-03-the-receipt-knows/`
- Composition: `Section03Receipt`
- Port: `1003`
- Studio URL: `http://localhost:1003/#project/section-03-the-receipt-knows`
- Direct composition URL: `http://localhost:1003/api/projects/section-03-the-receipt-knows/preview/comp/index.html`
- Runtime: `32.235s`
- Voiceover: `voiceover/section-03-the-receipt-knows/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-03-the-receipt-knows/section-03-word-timings.json`

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice Cue | Scene | What Changes | Motion | WIT | Sync |
|---:|---:|---|---|---|---|---|---|
| A1 | 1.78 | "what you actually spend" | A wood | label + WIT | hard-show | holding-receipt RIGHT ~1/3 | word |
| A2 | 3.20 | "fifty percent off… paid five, done" | A | Receipt #1 TOTAL $5 (1 item) | pop | — | word |
| A3 | 6.86 | "buy one, get one free" | A | Receipt #2 appears | pop | — | word |
| A4 | 8.78 | "the full ten" | A | $10 TOTAL + red ring | impact | — | word |
| A5 | 10.62 | "twice as much" | A | "×2 TWICE AS MUCH" stamp | impact | — | word |
| A6 | 12.82 | "a second one you did not need" | A | "+1 you didn't need" tag | hard-show | — | word |
| B1 | 16.32 | "smaller price" | B basket | "50% off = smaller price" | hard-show | — | word |
| B2 | 20.02 | "bigger basket" | B | "BUY 1 GET 1 = BIGGER BASKET" | impact | — | word |
| B3 | 22.20 | "the other spends it" | B | WIT empty-wallet | hard-show | empty-wallet LEFT ~1/2 | word |
| B4 | 24.52 | "robs you" | B | "ROBBED (with a smile)" stamp | impact | — | word |
| C1 | 25.40 | (scene start) | C wood2 | two signs (50% OFF / FREE) | hard-show | — | pinned |
| C2 | 27.48 | "better deal" | C | green check on 50% OFF | impact | — | word |
| C3 | 28.60 | "you walked right past it" | C | WIT facepalm | hard-show | facepalm RIGHT ~1/2 | word |
| C4 | 31.62 | "the magic word" | C | "the magic word →" glow | impact | — | word |

## Render Review-Prevention Pass

- voice cue map: built from `section-03-word-timings.json` (whisper-tiny.en, clean)
- big-scene sanity: 3 scenes (receipts/wood, basket, signs/wood-callback)
- cue density: one change per beat; receipts build over Scene A
- motion density: hard-show; impact on $10 ring, ×2, ROBBED, check, magic-word
- WIT density: 3 (1/scene); sides right → left → right
- WIT crop/collision: faces clear, legs-only crop, labels cleared opposite WIT
- markup target: red ring on $10 total; green check on the 50%-off sign
- scene differentiation: wood receipts / bright veg basket / wood-cooler signs (wood is a non-consecutive checkout-counter callback)
- HyperFrames mechanics: lint 0 errors (1 advisory), validate 0 errors, deterministic GSAP, sequential cue track, audio clip
- render decisions beyond plan: receipts/signs/stamps built in CSS (no clean modern receipt photo available); scene cuts pinned to word starts

## Verification

- lint: 0 errors, 1 warning (timeline_track_too_dense advisory)
- validate: 0 errors, 0 warnings, 30 non-blocking WCAG contrast advisories (receipts/signs render legibly)
- direct preview contact sheet: `snapshots/contact-sheet.jpg` at 4.5/9.2/11.0/13.5/20.5/23.5/27.0/31.6 — $5-vs-$10 reads, basket = bigger basket, WIT varies, no bad crops
- export/render: not requested (no MP4)

## Notes

- (superseded) v1 bases were a dark wood table + white veg basket with all-CSS receipts.

## 2026-06-24 Subscription-Style Remake (owner feedback)

Owner: "backgrounds too simple, WIT too small, texts/items too simple — follow subscription-now style, remake section 3 completely." Rebuilt to the standing vivid-hook template:
- **5 scenes** (was 3): A cash ($5) → B coins (BOGO $10 / twice as much) → C basket (BIGGER BASKET) → D red curtain (robs you while smiling) → E cash+glowing FREE (magic word).
- **Vivid dark bases** with dramatic grades (`brightness 0.42–0.52`, high saturation) + heavy scrim — money/coins/curtain instead of plain wood/white.
- **Giant kinetic devices**: a 300px `$5` then a red 300px `$10` (the subscription "bignum" counter), a "×2 TWICE AS MUCH" stamp, a "+1 you didn't need" toast, a giant gold "BIGGER BASKET" banner, "ROBBED :)" stamp, and a 230px glowing red **FREE** payoff. The plain CSS receipt is now just a small supporting strip.
- **GIANT WIT** (~1120–1200px, was ~780) varied per scene: holding-receipt R → receipt-attacked (wrapped in the receipt) center → betrayed L → empty-wallet center → facepalm L.
- All cues word-pinned to `section-03-word-timings.json`. Collision fix pass: moved the ×2/+1 clear of WIT in B; flipped WIT left + FREE/sign right in E.
- Verify: lint 0 errors (2 advisory), validate 0 errors (contrast advisories only), re-snapshotted — all devices clear of WIT faces, giant WIT reads, bases vivid. Comp serves HTTP 200. Review mirror synced.
