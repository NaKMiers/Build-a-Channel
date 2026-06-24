# Section 7 Render Implementation

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 7: Payoff: Free Cuts Your Judgment`
Status: `built to full bar (kinetic, fresh bright bases), ready for review`

## Result

- Preview project: `section-previews/section-07-free-cuts-your-judgment/`
- Composition: `Section07Payoff`
- Port: `1007`
- Studio URL: `http://localhost:1007/#project/section-07-free-cuts-your-judgment`
- Direct composition URL: `http://localhost:1007/api/projects/section-07-free-cuts-your-judgment/preview/comp/index.html`
- Runtime: `38.912s`
- Word timings: `voiceover/section-07-free-cuts-your-judgment/section-07-word-timings.json` (clean, no glitch)

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice Cue | Scene | What Changes | Motion | WIT | Sync |
|---:|---:|---|---|---|---|---|---|
| A1 | 0.30 | "why does free beat 50%?" | A chess | question | hard-show | thinking R ~1320 | word |
| A2 | 3.86 | "the two signs" | A | FREE / 50% OFF face-off + vs | pop/impact | - | word |
| A3 | 4.96 | "playing different games" | A | "two different GAMES" | impact | - | word |
| B1 | 7.16 | "fifty percent off cuts the price" | B scissors | "cuts the PRICE" | impact | suspicious L ~1320 | word |
| B2 | 9.76 | "cuts your judgment" | B | "free cuts your JUDGMENT" (red) | impact | - | word |
| C1 | 11.30 | "asks your brain a question" | C calculator | calc "5−4=?" (live) | pop | talking-front R ~1320 | word |
| C2 | 17.04 | "sometimes you genuinely want two" | C | "✓ want two" caveat | pop | - | word |
| C3 | 18.88 | "sometimes free really is free money" | C | "✓ free is free" caveat | pop | - | word |
| C4 | 23.36 | "switches off your inner accountant" | C | calc FLIPS to "switched off" + stamp | impact | - | word |
| D1 | 27.40 | "buy one get one 50% off" | D mask | "BUY 1 GET 1 50% OFF" sign | pop | betrayed L ~1320 | word |
| D2 | 29.46 | "that is not free anything" | D | "not free anything…" | hard-show | - | word |
| D3 | 31.14 | "25% off" | D | "= 25% OFF" reveal | impact | - | word |
| D4 | 32.64 | "in a costume" | D | "…in a costume" stamp | impact | - | word |
| E1 | 33.84 | "same shelf, same product" | E cards | "same shelf · same product" | hard-show | pointing-right R ~1320 | word |
| E2 | 35.24 | "completely different game" | E | "different GAME" | impact | - | word |
| E3 | 36.84 | "now go be slightly harder to trick" | E | payoff line | impact | - | word |

## Render Review-Prevention Pass

- voice cue map from `section-07-word-timings.json` (clean)
- full bar: 5 FRESH bright distinct bases (no reuse, no dark overlay - light text-side scrim only), kinetic devices, giant WIT, clean spaced text
- WIT density: 5 (1/scene), giant ~1320px; sides R/L/R/L/R; poses thinking/suspicious/talking-front/betrayed/pointing-right
- kinetic devices: sign face-off (A), thesis smash (B), calculator live→off flip (C, two-element swap), unmask reveal (D), payoff smash (E)
- HyperFrames mechanics: lint 0 errors (1 advisory), validate 0 errors, deterministic GSAP, sequential cue track, audio clip

## Verification

- lint: 0 errors, 1 warning (timeline_track_too_dense advisory)
- validate: 0 errors, 0 warnings, contrast advisories only
- contact sheets: at 13+ timestamps - thesis lands, calc flips off, "25% off in a costume" stinger lands on the mask, sign-off reads; bright bases, giant WIT clean, no text overlap
- export/render: not requested (no MP4)

## Notes

- Bases: chess (CC0), scissors (CC BY-SA), calculator (CC0), carnival mask (CC0), playing cards (CC BY-SA). All fresh for S7. WIT shared poses. Local working-set assets.
- Final section of the video - all 7 sections now built. Next pipeline step: combine.

## 2026-06-24 Scene C fix (owner: "0:12 background looks bad/buggy")

Two fixes: (1) BUG - the Scene C photo used `class="photo calc"`, colliding with the `.calc` calculator-CARD class (`width:520px` + bg/border), which shrank the background image into a narrow box. Renamed the photo grade class to `.photo abak` (calculator card keeps `.calc`) → background now fills the frame. (2) Swapped the busy B&W calculator+laptop base for a clean warm wooden **abacus** (`base-c-abacus.jpg`, Wikimedia CC BY-SA) - clearer "your inner accountant," brand-free, brighter. Also corrected Scenes A/B scrim sides (were on the WIT side; moved to the text side so chess/scissors bases show fully). Re-validated 0 errors; re-snapshotted - Scene C fills, base reads, calc card + caveats + off-flip intact. Mirror synced.
- Lint note: avoid reusing a device class name (`.calc`, `.cd`, etc.) as a `.photo.<x>` grade class - it collides and breaks the base.
