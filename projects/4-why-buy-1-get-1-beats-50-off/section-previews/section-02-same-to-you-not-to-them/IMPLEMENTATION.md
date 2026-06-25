# Section 2 Render Implementation

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 2: Same To You, Not To Them`

Status:
`section preview built, ready for review`

## Result

- Preview project: `section-previews/section-02-same-to-you-not-to-them/`
- Source: `05-visual-plan.md` → `visual-plan/section-02-same-to-you-not-to-them/`
- Composition: `Section02Counter`
- Port: `1002`
- Studio URL: `http://localhost:1002/#project/section-02-same-to-you-not-to-them`
- Direct composition URL: `http://localhost:1002/api/projects/section-02-same-to-you-not-to-them/preview/comp/index.html`
- Runtime: `40.469s`
- Voiceover: `voiceover/section-02-same-to-you-not-to-them/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-02-same-to-you-not-to-them/section-02-word-timings.json`

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice Cue | Big Scene | What Changes | Motion | WIT / Crop | Sync |
|---:|---:|---|---|---|---|---|---|
| A1 | 0.40 | "Look at the store's side" | A register | hand label | hard-show | thinking RIGHT ~1/3 | pinned |
| A2 | 4.46 | "$10" | A | SELLS $10 tag | impact | thinking | word |
| A3 | 6.06 | "$4 to make" | A | COSTS $4 tag | impact | thinking | word |
| B1 | 7.62 | "Fifty percent off" | B cash | card header | hard-show | - | word |
| B2 | 8.66 | "you pay five" | B | "You pay $5" | hard-show | - | word |
| B3 | 9.88 | "spent four to make" | B | "− Cost $4" | hard-show | - | word |
| B4 | 12.62 | "keeps one dollar" | B | "= keeps $1" red box | impact | - | word |
| C1 | 13.92 | "Buy one, get one free" | C coins | card header | hard-show | - | word |
| C2 | 15.38 | "pay ten and take two" | C | "You pay $10" | hard-show | - | word |
| C3 | 17.08 | "cost the store eight" | C | "− Cost $8" | hard-show | - | word |
| C4 | 20.52 | "keeps two dollars" | C | "= keeps $2" red box | impact | - | word |
| C5 | 21.94 | "Double." | C | card hidden → DOUBLE stamp + WIT | impact | shocked CENTER ~1/2 | word |
| D1 | 23.28 | "same five for you" | D register-callback | YOU $5/item | hard-show | - | word |
| D2 | 25.24 | "double the profit for the store" | D | STORE 2× profit | hard-show | - | word |
| D3 | 27.24 | "sign never changed / still says ten" | D | $10 price tag | impact | - | word |
| D4 | 30.70 | "felt clever doing it" | D | WIT | hard-show | awkward-celebration LEFT ~1/2 | word |
| E1 | 32.42 | "this trick is old" | E Wedgwood | "≈250 years old" | hard-show | - | word |
| E2 | 34.42 | "Wedgwood … 1700s" | E | "Wedgwood · 1700s" | hard-show | - | word |
| E3 | 37.74 / 38.32 | "not the first sucker / just the latest" | E | WIT + sucker ticket | impact | facepalm RIGHT ~1/2 | word |

## Render Review-Prevention Pass

- voice cue map: built from `section-02-word-timings.json` (whisper-tiny.en; final word "latest" tail-glitch noted, payoff lands by ~39.2)
- big-scene sanity: 5 scenes, ~6–9s each
- cue density: one math line per beat
- motion density: hard-show math lines; impact on $1/$2 results, DOUBLE, $10 tag, sucker ticket
- WIT density: 4 (A/C/D/E; Scene B intentionally none)
- WIT crop/collision: faces/glasses/shoulders clear; cards always cleared to the side WIT is not on; "DOUBLE" takeover hides the math card so nothing sits under it
- markup target: red boxes on the result numbers only
- scene differentiation: register / cash / coins / Wedgwood; register reused for D only as a non-consecutive callback (cooler grade `reg2`)
- HyperFrames mechanics: lint 0 errors (2 advisory warnings), validate 0 errors, deterministic GSAP, sequential cue track, audio clip
- render decisions beyond plan: scene cuts pinned to real word starts; the "DOUBLE" beat hides the math card and takes over with stamp + shocked WIT (S1 takeover pattern)

## Verification

- lint: 0 errors, 2 warnings (timeline_track_too_dense advisory ×; cosmetic)
- validate: 0 errors, 0 warnings, 15 non-blocking WCAG contrast advisories
- direct preview contact sheets: `snapshots/contact-sheet-1.jpg` + `-2.jpg` at 6.5/9.0/12.9/16.0/21.0/22.3/26.0/29.6/31.2/35.0/39.2 - every number lands on its word, math reads, WIT varies and is uncropped, no collisions
- export/render: not requested (no MP4)

## Notes

- Bases (current, after the 2026-06-24 revert): cash register (CC BY 2.0, credit "Old cash register") for Scenes A + D (D = `reg2` callback), USD cash (CC0) for B, rising coins (CC0) for C, real Josiah Wedgwood blue jasperware (CC0) for E. WIT shared poses. Local working-set assets (junctions 404 on this box).
- The on-screen subtraction directly reinforces the rev 2.1 "speak the math aloud" script fix - audio and screen show the same derivation, one number at a time.

## 2026-06-24 Funny-Image Pass - then REVERTED

Tried a pink piggy bank for Scenes A + D (with brightened cash/coins) per "find more suitable and funny images." Owner reviewed and said it was "even worse - back to previous images." REVERTED: restored the cash register (A + `reg2` D), the original cash/coins/wedgwood grades, and the standard scrim. Composition is back to the validated register version. Validate 0 errors (15 non-blocking contrast); comp serves HTTP 200; review mirror re-synced. Piggy file kept on disk but unreferenced. Takeaway for this owner: keep Section 2 on the literal money/counter objects, not a cute mascot prop.
