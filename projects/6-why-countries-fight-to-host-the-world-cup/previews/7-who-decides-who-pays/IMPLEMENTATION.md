# Section 7 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 7: Who Decides Is Not Who Pays`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/7-who-decides-who-pays/`
- Source: `visual-plan/section-07-who-decides-who-pays/section-07-who-decides-who-pays-visual-plan.md` (built 1:1)
- Port: `1007`
- Studio URL: `http://localhost:1007/#project/7-who-decides-who-pays`
- Direct composition URL: `http://localhost:1007/api/projects/7-who-decides-who-pays/preview/comp/index.html`
- Runtime: `66.987s`, 9 scenes, composition `Section07WhoDecidesWhoPays`
- Voiceover: `./section-07-who-decides-who-pays.mp3` (copy of the approved David23/am_eric 0.81 take)
- Visual plan: current (word timings verified against the JSON; all pins exact)

## Voice Sync

Every `data-start` and GSAP reveal pinned to `section-07-word-timings.json` (217
words). Known anomaly: the whisper tail (words 206-216) is non-monotonic - a backward
jump to 60.51 right after `with@63.18-63.50`. Handled per the plan's +2.99s shift
interpolation: `no ticket money` cross ~64.26, `BUILD NOTHING.` ~65.04, `STILL PAY.`
~66.04, receipt unroll ~66.34; scene 7.9 end clamped to the real audio duration
66.987. No other cue is estimated. Hide-sets nudged 0.02-0.16s after clip starts.

## Render decisions beyond the plan

- 7.4 CSS spreadsheet grid + warm grade behind the calculator (manifest note: photo is
  on plain white; render supplies the budget-office context).
- 7.6 needle sweep built as a CSS needle (rotation -166deg -> -24deg, pivot at the
  hub) under a blurred cream patch that hides the asset's baked `meh` needle from the
  sweep beat on; `meh` label z-raised above the patch after snapshot QA.
- 7.8 X-button wiggle is a CSS patch drawn over the ad card's baked X.
- 7.5 anger mark dropped after snapshot QA (detached CSS arcs read as random red
  squiggles; the scream pose + giant `NO.` stamp carry the beat). Pose-catalog drift
  documented: `furious_shouting_anger_mark.png` pixels contain no separate mark.
- 7.3 pointing WIT mirrored via a wrapper (`.mirror img { scaleX(-1) }`) so GSAP never
  touches the flip.
- 7.9 endless receipt unroll built as an overflow-hidden floor strip wrapper with a
  90deg-rotated tall receipt inside, wiped across at the final beat.

## Snapshot QA defects found and fixed

- 7.4: markup box originally overlapped the roads/schools amounts, and the stamped
  `+$9.9 BILLION*` was covered by the `DOES NOT FIT` tag - box moved onto the empty
  prestige field, tag moved right, number/dash/crown/stamp repositioned.
- 7.5: detached CSS anger mark removed (see above).
- 7.6: cream needle-cover patch read as a bright pill - re-built as a blurred gradient;
  `meh` z-index raised.
- 7.2: speech-bubble tail re-aimed at the suits trio (was pointing at the trophy).
- 7.8: `100% LEGAL` text re-fitted inside the starburst.
- 7.9: `EACH.` stamp moved off the `US CITIES:` plate text; bill stack re-grounded
  (+70px); plate lowered.
- First-frame decode race observed once at 21.2s (WIT partially decoded) - re-snap with
  a throwaway first timestamp confirmed it was the known tool artifact, not a defect.

## Motion classification

- Hard-show: scene bases, WIT entrances, card headers, budget rows, jar/label, plates,
  chips, `(already)`, `(by acclamation)`, tally strokes, callback card.
- Impact: PAYS panel smash, `THE BILL` smash, `NO.` stamp, ballot pops x6, stamp slam +
  `+$9.9 BILLION*`, `DOES NOT FIT` bounce, gear tag smash, `BIDDERS: 1` smash, needle
  sweep + confetti, wallet slam + click pulse, polaroid pops + flash blooms, `ONE WEIRD
  TRICK` smash, sticker smash, odometer pulse, `EACH.` smash, `STILL PAY.` smash,
  receipt unroll wipe.
- Cue tween calls: 69 (26 show, 17 pop, 14 smash, 7 wipe, 5 reveal) plus helper
  micro-tweens (crown bob, X wiggle, odometer strip, flash blooms).
- WIT: exactly 1 hero appearance per scene (9 total, plus the 3 tiny taxpayer WITs as
  props in 7.1), sides C-R-L-R-L-R-L-R-L, giant-and-high per brand rule; poses:
  shrug_confused_flat_mouth, unimpressed_smirk_closeup, pointing_at_globe_explaining
  (mirrored), mildly_surprised_hand_at_chin, furious_shouting_anger_mark,
  deadpan_unimpressed_half_lidded, ok_hand_sign_content_closeup,
  smug_sly_smirk_leaning (rotate -5deg), shrug_both_hands_up_smile.

## Verification

- lint: 0 errors, 5 warnings (intentional: receipt roll + taxpayer WIT reuse
  `duplicate_media_discovery_risk`; reused flash-bloom element
  `overlapping_gsap_tweens` with `overwrite:"auto"`; file-size advisory)
- validate: 0 errors, 0 warnings, 105 contrast advisories (known false-positive class:
  text measured against the photo behind, ignoring the chip's own opaque background)
- inspect: 0 layout issues (66 samples)
- snapshot QA: full cue pass + 15-frame re-snap after fixes; all cue states verified
  readable, WIT face clear of text/props in every scene
- export: none (not requested)

## Assets

- Shared folder via `assets` symlink -> `../../assets`
- All 32 referenced assets pre-made by visual-implement; alpha-extrema check: all real
  RGBA (no baked checkerboard this section); content bboxes measured before layout
  (taxpayer WIT 31%w, receipt roll 37%w, trophy 46%w of canvas)
- No derived helper assets were needed this run
- Attribution: `assets/ATTRIBUTION.md` (unchanged; no new sourcing this run)
