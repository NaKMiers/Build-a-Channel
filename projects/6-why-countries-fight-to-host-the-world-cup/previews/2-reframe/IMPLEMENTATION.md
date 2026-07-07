# Section 2 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 2: Reframe: A Purchase, Not An Investment`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/2-reframe/`
- Source: `previews/2-reframe/index.html` (composition `Section02Reframe`)
- Port: `1002`
- Studio URL: `http://localhost:1002/#project/2-reframe`
- Direct composition URL: `http://localhost:1002/api/projects/2-reframe/preview/comp/index.html`
- Runtime: `33.728s`
- Voiceover: `section-02-reframe.mp3` (copy of `voiceover/section-02-reframe/scratch-audio/section-02-reframe-david23-am_eric-0.81.mp3`)
- Visual plan: `visual-plan/section-02-reframe/section-02-reframe-visual-plan.md` (followed 1:1; scene layout micro-adjusted, see below)

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| 1 | 0.00 | Most people think... | 2.1 pool fantasy | base + floating WIT (gentle bob) | static | pool-float WIT bottom-left ~2/5, waist hidden by ring (intentional) | - | pinned |
| 2 | 2.82 | arrive | 2.1 | chip `tourists!` pops | impact (small pop) | - | chip | pinned |
| 3 | 3.70 | fill | 2.1 | chip `hotels full!` | impact (small pop) | - | chip | pinned |
| 4 | 4.70 | rich | 2.1 | chip `shops rich!` | impact (small pop) | - | chip | pinned |
| 5 | 5.52 | grows | 2.1 | chip `economy UP!` | impact (small pop) | - | chip | pinned |
| 6 | 6.70 | story...tells | 2.1 | teal ribbon | hard-show | - | `as told by every bidding government` | pinned |
| 7 | 9.06 | lovely | 2.1 | pink sticker slap + wobble | impact | - | `lovely!` | pinned |
| 8 | 10.04 | The numbers | 2.2 correction board | hard cut; green digits flicker | static + flicker | - | - | pinned |
| 9 | 10.84 | different | 2.2 | display snaps to red readout | impact (state snap) | - | illustrative `-4,000,000,000` (deliberately generic) | pinned |
| 10 | 12.30 | truth | 2.2 | WIT hard-shows | hard-show | GIANT right ~1/2, hip crop, head ~6% from top; text zone left | - | pinned |
| 11 | 12.80 | Hosting the World Cup | 2.2 | `INVESTMENT?` writes on (0.5s) | transition (write-on) | clear of WIT | verdict word | pinned |
| 12 | 13.82 | not | 2.2 | red X strokes (2, staggered +0.16) | impact | - | X targets the verdict word exactly | pinned |
| 13 | 15.42 | purchase | 2.2 | `PURCHASE` stamp + frame shake | impact (hero) | stamp below word, clear of WIT | red stamp | pinned |
| 14 | 16.32 | Nobody | 2.3 showroom | hard cut; car + flex WIT posed | static | WIT left ~2/5+, knee crop, leaning at fender | - | pinned |
| 15 | 17.82 | money | 2.3 | mini card | hard-show | - | `makes money? NO.` | pinned |
| 16 | 19.64 | SEEN | 2.3 | 3 flashes + glints + caption | impact | caption above car, clear of WIT face | `LOOK AT ME.` | pinned |
| 17 | 20.14 | Ferrari. | 2.3 | extra glint | impact (small) | - | - | pinned |
| 18 | 20.88 | Countries | 2.4 checkout | hard cut; car+trophy+`STATUS` tag preset | static | - | tag `STATUS` | pinned |
| 19 | 23.62 | football | 2.4 | tag detaches, arcs car->trophy | transition (cause-effect) | - | - | pinned (docks by 24.78) |
| 20 | 25.50 | billions | 2.4 | tag text flips red | impact | - | `BILLIONS...` | pinned |
| 21 | 26.14 | And | 2.4 | panic WIT rises behind counter | hard-show | center ~1/3, chest-up crop AT the counter line (intentional), face clear | - | pinned |
| 22 | 26.68 | credit | 2.4 | TAXPAYER card slides in | transition (slide) | card below WIT, no face overlap | emboss `TAXPAYER` | pinned |
| 23 | 27.48 | yours | 2.4 | `yours.` note + arrow at the card | impact (pop) | in the WIT/trophy gap, not on WIT | `yours.` | pinned |
| 24 | 28.32 | taxpayer's | 2.4 | emboss light sweep + card bounce | impact | - | - | pinned |
| 25 | 29.34 | So | 2.5 closer | hard cut; wallet + trophy + tag + WIT | static | GIANT left ~1/2, waist crop, head high; cards right of face | tag `PRESTIGE - price on request` | pinned |
| 26 | 29.90 | question | 2.5 | tag wiggle | impact (small) | - | - | pinned |
| 27 | 30.86 | will | 2.5 | question card 1 pops | hard-show (pop) | clear of WIT face | `"will it pay off?"` | pinned |
| 28 | 31.68 | off | 2.5 | red strike through card 1 | impact | - | strike tied to the text span width | pinned |
| 29 | 33.16 | pays | 2.5 | `WHO PAYS?` slams + double underline | impact (hero) | right of WIT face, above subtitle zone | red caps | pinned |

## Render Review-Prevention Pass

- voice cue map completed: yes, from `section-02-word-timings.json`; duplicate backward pass (words 91-109) skipped per plan; end clamped to 33.728s
- big-scene sanity checked: 5 persistent scenes, one main idea each
- cue density checked: 29 cue states / 33.7s, grouped per plan (2.1 fantasy montage, 2.2 correction board)
- motion density checked: ordinary labels hard-show; impact reserved for lovely!/X/PURCHASE/LOOK AT ME./BILLIONS.../sweep/WHO PAYS?
- WIT density: exactly 1 WIT per big scene (5 total); 2.4 WIT enters only on the final beat per plan
- WIT crop/collision checked: all crops intentional (ring/waist, hip, knee, counter chest-up, waist); no face/head/shoulder cuts; no text on WIT's face; verified in contact sheets
- markup target checked: X crosses `INVESTMENT?` exactly; strike crosses the quoted question; `yours.` arrow points at the card; no decorative marks
- scene differentiation checked: 5 fresh bases (pool / calculator / showroom / marble / dark wood), none reused from Section 1
- HyperFrames mechanics checked: per-scene clips on own tracks, `<audio>` clip, synchronous timeline registration, deterministic GSAP, off-canvas WIT wrapped with `data-layout-allow-overflow` + `overflow:visible`
- render decisions made beyond visual plan:
  1. POSE SUBSTITUTION: `rich_flex_gold_chain_sunglasses.png` (planned for 2.3) does NOT match its `pose.md` catalog entry - actual pixels are a plain hands-behind-back smirk (no chain, no sunglasses, no flex). Used `boss_suit_sunglasses_sparkle.png` (glasses-adjust smug flex, hand on hip) from the approved shared library instead; copied into `assets/poses/`. The sunglasses beat is carried by the 2.1 pool-float pose.
  2. DERIVED ASSET: `assets/wallet-empty-cutout.png` keyed from `wallet-empty-1.jpg` (white studio bg -> transparency, border-connected BFS + 1px dilation) because `mix-blend-mode:multiply` is isolated/unreliable in the capture path. Original untouched.
  3. 2.1 layout: ribbon + sticker moved below the chip arc (plan's % zones collided chip 3 / ribbon / sticker); chip 1 moved off WIT's face.
  4. 2.4: CSS warm blurred boutique backdrop + counter line added so the flat marble texture reads as a counter and panic WIT can rise chest-up behind it.

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| S1 end | 2.1 | hard cut | brightness whiplash is the joke | none | keep |
| 2.1 | 2.2 | hard cut | fantasy dies instantly | none | keep |
| 2.2 | 2.3 | hard cut | new mechanism (analogy) | none | keep |
| 2.3 | 2.4 | hard cut | analogy transfers | none | keep |
| 2.4 | 2.5 | hard cut | quiet closer | none | keep |

Within-scene motion only (tag arc, card slide, write-on) - all cause-effect, all pinned to words.

## Assets

- Shared asset folder: `../../assets` (symlink; HTTP 200 verified incl. `wallet-empty-cutout.png`)
- Section assets: `resort-pool-1.jpg`, `calculator-desk-1.jpg`, `showroom-floor-1.jpg`, `marble-counter-1.jpg`, `desk-darkwood-1.jpg` (2.5 table per manifest note), `wallet-empty-1.jpg` (via derived cutout), `wit-pool-float-shades.png`, `red-supercar-generic.png` (2.3 + flipped small in 2.4), `trophy-gold-parody.png` (2.4/2.5, video hero), `price-tag-blank.png` (2.4/2.5, CSS text), `credit-card-taxpayer.png`, poses: `lecturing_finger_raised_eyes_closed`, `boss_suit_sunglasses_sparkle` (substitution), `panic_hands_on_cheeks_scream`, `skeptical_side_eye_doubtful`
- Attribution: `assets/ATTRIBUTION.md` (cutout noted as derived from the CC0 wallet photo)

## Verification

- lint: 0 errors, 1 warning (`duplicate_media_discovery_risk` - intentional motif reuse: trophy/tag/car across 2.4-2.5)
- validate: 0 errors, 35 contrast advisories (stylized text measured against the photo behind opaque cards - known non-blocking class)
- inspect: 0 layout issues across 27 cue-timed samples
- direct preview screenshots/contact sheet: full 27-frame snapshot QA, 3 review rounds; fixes applied: chip-on-WIT-face, degenerate `scaleX(0)` X strokes, 2.3 WIT scale + caption contrast, 2.4 scale-up + readable tag text + `yours.` arrow target, 2.5 wallet blend -> keyed cutout; "missing TAXPAYER emboss" at 27.9 confirmed as the known snapshot first-frame decode race (re-snap rendered fully)
- export/render: not requested; no MP4/WebM created

## Notes

- Preview server project id resolves to the folder name `2-reframe` (confirmed via `/api/projects`).
- Snapshot tool runs in screenshot-fallback mode on this box (system Chrome); first captured frame of a run can miss a late-decoding PNG - re-snap before diagnosing.
