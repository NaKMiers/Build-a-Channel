# Section 9 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 9: Outro: The Cheapest Host On Earth`

Status: `built, lint/validate/inspect 0 errors, snapshot QA passed, preview server running`

## Result

- Preview project: `previews/9-outro/`
- Source: `visual-plan/section-09-outro/section-09-outro-visual-plan.md` (built 1:1; deviations documented below)
- Port: `1009`
- Studio URL: `http://localhost:1009/#project/9-outro`
- Direct composition URL: `http://localhost:1009/api/projects/9-outro/preview/comp/index.html`
- Runtime: `17.877s` (root data-duration; audio duration)
- Voiceover: `./section-09-outro.mp3` (copy of `voiceover/section-09-outro/scratch-audio/section-09-outro-david23-am_eric-0.81.mp3`)
- Visual plan: current (pinned times verified against `section-09-word-timings.json` - exact match)

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| 1 | 0.00 | By | 9.1 cafe counter | base + trophy + receipt band + blank CSS face | static (hard cut) | none (by design) | - | pinned |
| 2 | 1.10 | hosting | 9.1 | trophy glint pop (ambience) | pop | - | - | ambience |
| 3 | 1.52 | channel | 9.1 | `HOSTING: THIS CHANNEL` prints + paper nudge | hard-show | - | dot-matrix header | pinned |
| 4 | 3.24 | stadiums | 9.1 | `STADIUMS ... $0` prints + nudge | hard-show | - | green $0 | pinned |
| 5 | 4.24 | taxes | 9.1 | `TAXES ... $0` prints + nudge | hard-show | - | green $0 | pinned |
| 6 | 5.12 | receipt | 9.1 | double rule + `TOTAL: $0.00` scale-punch + green flash | impact | - | bold green total | pinned |
| 7 | 5.45 | (post-word) | 9.1 | stub tears: drops 20px, straightens, settles | impact | - | - | pinned |
| 8 | 5.66 | If | 9.2 desk | hard cut; card pops in (0.3s) | entrance | WIT hidden below frame | parody card | pinned |
| 9 | 6.60 | something | 9.2 | SVG cursor slides in, lazy arc to LIKE by 7.92 | transition device | - | - | pinned |
| 10 | 8.22 | there | 9.2 | LIKE click: dip + ring + boing + blue flip + thumb tips -15deg | impact | - | Liked | pinned |
| 11 | 8.92 | free | 9.2 | green `$0.00` tag swings out of pill corner (elastic) | impact | - | $0.00 | pinned |
| 12 | 9.94 | hundred ("100") | 9.2 | `100% ours` annotation + hand-drawn SVG arrow (10.10) | hard-show | - | amber marker | pinned |
| 13 | 11.32 | Subscribe | 9.2 | cursor click: SUBSCRIBE -> SUBSCRIBED + bell ring + confetti + +6% push-in | impact | - | SUBSCRIBED | pinned |
| 14 | 11.62 | (end of "Subscribe") | 9.2 | toast `Welcome to the channel!` slides up | pop | - | toast | pinned |
| 15 | 12.86 | money | 9.2 | amber underline swipes under `stories about money` | hard-show (wipe) | - | marker underline | pinned |
| 16 | 14.22 | goes | 9.2 | tiny bell wiggle | micro | - | - | pinned |
| 17 | 15.48 | consultants | 9.2 | WIT rises beside the card's right edge (0.45s) | entrance | giant (~79% frame h), head+glasses+peace hand fully in frame, legs crop at frame bottom only; z below card | - | pinned |
| 18 | 16.66 | predict | 9.2 | `CONSULTANT-FREE` stamp thuds onto WIT's chest | impact | stamp below his hand, 280px clear of face/mouth | green stamp | pinned |
| 19 | 17.877 | (end) | 9.2 | full final state holds | static | - | - | clamped |

## Render Review-Prevention Pass

- voice cue map completed: yes - built from `section-09-word-timings.json`; every plan-pinned time matched the JSON exactly
- big-scene sanity checked: 2 scenes; 9.2 is one continuous 12.22s interactive scene per the owner-approved animated-UI device rule (no hard cut mid-interaction)
- cue density checked: 19 cues over 17.877s across an interactive CTA device - matches the approved project-5 S8 precedent
- motion density checked: prints hard-show; impact reserved for TOTAL, clicks, tag, stamp, tear
- WIT density: exactly 1 appearance (plan-specified); 9.1 deliberately WIT-free
- WIT crop/collision checked: face/head/shoulders/peace hand fully inside frame; only legs crop at frame bottom; no text on face (stamp 280px below mouth); annotation clears his head
- markup target checked: annotation arrow lands above the Liked pill/tag cluster; underline equals the `stories about money` text width; tag physically hangs off the pill
- scene differentiation checked: warm cafe counter vs lamp-lit console desk - both warm but distinct subjects; distinct from S8's living-room mantel
- HyperFrames mechanics checked: per-scene clips on own tracks (1, 2), audio track 30, synchronous GSAP registration, no random/async, allow-overflow + overflow:visible on scenes and zoom wrapper, cue sets 0.04-0.06s after clip starts
- render decisions made beyond visual plan:
  1. All receipt print text lives on a CSS receipt face panel (paper card, sawtooth tear edge) attached to the receipt-strip asset instead of directly on the PNG - the asset's paper band is only ~37% of its canvas width (Image.getbbox), too narrow for cue-critical text (standing S3 lesson). The panel IS the tear-off stub at 5.45.
  2. WIT "torso half-occluded by the card" was adapted: the plan's own zones barely overlap (card ends 58% x, WIT starts 55% x), so WIT rises from below the frame beside the card's right edge (z below card) - reads as "peeks up from behind the card" without a fake mid-air crop (S3 lesson: don't fake a behind-crop the photo can't support).
  3. Stamp given a translucent white label backing (rgba 255,255,255,0.72) so the tail that extends past WIT's torso stays readable on the busy photo; placement on the chest below his hand is the plan's explicit certification gag (documented exception to the keep-marks-off-WIT's-body habit - face/expression fully clear).
  4. Annotation `100% ours` sits on a translucent cream pill so the amber handwriting reads over the bright lamp-shade area (chip-any-text-on-texture rule).
  5. No SFX/music files - sibling convention (voiceover only; sound design is a later pipeline concern).

## Voice Sync Map

See Big Scene / Cue Plan - all cue `data-start`s and GSAP reveals pinned to word starts from the JSON. Word-timing anomalies handled: whisper's final "it." end runs to 20.2s (known tail glitch) - the section end is clamped to the real 17.877s audio duration; no backward-jump or chunk-seam reorder anywhere in this JSON (verified monotonic); mishearings "explains"/"100"+"%" are token-level only and carry correct timestamps.

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| (S8) | 9.1 | hard cut | grey-blue payoff to warm relief | none | hard cut |
| 9.1 | 9.2 | hard cut + 0.3s card pop | tear-off settles, then the CTA card takes over | none | hard cut |
| inside 9.2 | - | +6% push-in at 11.32 | plan's two-phase device to keep the long scene alive | none | keep |

## Element Motion Notes

- Entrances: card pop (back.out), cursor arc (split-ease left/top), WIT rise (power3.out), toast rise, tag elastic swing
- Holds: every flipped state (Liked, SUBSCRIBED, bell, tag, toast, stamp, underline, annotation) holds to the end - nothing resets
- Emphasis: TOTAL scale-punch + green flash; click dips + rings + boings; stamp thud
- Exits: cursor drifts off 12.30-12.90; glint fades 1.85; confetti self-fades in 0.8s
- Repeated effects avoided: two different click celebrations (tag vs confetti+toast); each print line identical by design (printer rhythm)
- Hard-show vs impact decisions: receipt lines hard-show (printer chirps are audio-domain), clicks/total/stamp are impact
- WIT scale/crop checks: verified in snapshots at 16.0/17.0/17.7

## Assets

- Shared asset folder: `../../assets` via plain symlink `assets -> ../../assets` (Linux box - serves fine, HTTP 200 verified)
- Section assets used: `cafe-counter-warm-1.jpg`, `desk-cozy-evening-1.jpg`, `trophy-gold-parody.png` (9.1 hero + 9.2 card thumbnail - final two appearances), `receipt-endless-roll.png` (final appearance), `poses/peace_sign_calm_open_mouth.png`, `fonts/patrick-hand-latin.woff2`
- All 3 PNGs alpha-checked (real RGBA cutouts, extrema (0,255) - no baked checkerboard) and bbox-checked before layout
- No derived/helper assets created; subscribe UI is 100% CSS/SVG per manifest
- Attribution: both browse bases already recorded in `assets/ATTRIBUTION.md` (StockSnap CC0)

## Verification

- lint: 0 errors, 8 warnings - all expected/documented: 1x `duplicate_media_discovery_risk` (trophy PNG intentionally reused in 9.1 + the 9.2 card thumbnail - the motif), 6x `overlapping_gsap_tweens` (boing/click-dip intentional micro-sequences, `overwrite:"auto"` set), 1x `font_family_without_font_face` (Liberation Sans is a system UI-parody font by design; PatrickHand is the @font-face brand font)
- validate: 0 errors, 0 warnings, 30 contrast advisories (validator measures stylized text against the photo behind, ignoring the card/pill/chip own backgrounds - same class as S1-S8, non-blocking)
- inspect: 0 layout issues across 19 cue timestamps
- snapshot QA: 19-frame full pass + 7-frame re-verify pass; defects found and fixed: (1) green TOTAL flash div mis-anchored below the total row -> moved inside the l4 wrap as inset overlay; (2) toast glyphs dipped past the 80% subtitle line after push-in -> card raised 10px (click targets/rings/confetti re-pinned); (3) LIKE click point sat on the pill's right EDGE (x=400) -> re-centered to the pill's right half (x=360); (4) stamp tail low-contrast on the photo -> translucent label backing. First-frame decode race checked: 5.3s snapped in first-run position 2 and re-run position 7 - identical, no race
- direct preview screenshots: `snapshots/` (both runs kept)
- export/render: not requested, none created

## Notes

- Preview server: `nohup npx --yes hyperframes@0.6.76 preview --port 1009` (project id `9-outro`); sysctl port floor already at 1000 this session
- Review mirror synced: `hyperframes/review/section-09.html`
