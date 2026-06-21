# Section 4 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 4: The Boring Parts Disappear`

Status:
`remade from scratch 2026-06-21 — preview running on port 1004, ready for review`

## Remake From Scratch (2026-06-21)

Rebuilt the entire composition fresh on the user's request, and fixed that the section-preview `assets/` folder was missing (a broken junction) so the standalone preview had been rendering without images.

- New build: 3 big scenes on real photo bases (`fabric.jpg` materials / `screwdriver.jpg` repairable mechanics / `cardboard.jpg` sealed box), 6 cues, 3 WIT beats (`thinking` held cues 1-2 / `deadpan-side-eye` cue 4 / `betrayed` cue 6). The 6 "boring parts" are a staggered stacked list that builds one row per spoken item (GSAP opacity sets); payoff `LESS FUTURE BUILT IN` (one line, span `border-bottom` underline). WIT cues carry `data-layout-allow-overflow` + `overflow:visible`.
- Assets restored into `assets/section-04/` (fabric/screwdriver/cardboard from the review mirror) + `assets/wit/` (thinking/deadpan/betrayed) + font; `dev` script patched to `preview --port 1004`.
- Timing is `whisper-derived`: after a first estimated pass mismatched the voice (~4s late on the parts list), the audio was transcribed with `transformers.js` (`@xenova/whisper-tiny.en`, WASM — no native deps) and word timings saved to `voiceover/section-04-.../section-04-word-timings.json`. Every scene cut + reveal is now pinned to real word times (hinge 5.66 / battery 7.62 / screw 9.46 / spare 12.72 / printer 25.46 / easy-to-hide 33.3 / payoff 36.2). Snapshot QA confirms each part appears as it is spoken.
- Retained the 3 attributed real bases (already in `assets/ATTRIBUTION.md`); the Scene-2 screwdriver-on-pink is the weakest and can be swapped for a warmer in-context tools photo on request.
- Verified: lint 0 err / validate 0 err / inspect 0 layout issues (7 samples); snapshot QA at `2.5/8/13/18/24/30/36`. Synced to `hyperframes/review/section-04.html` and refreshed the unified full video (`hyperframes/full-video/compositions/section-04.html`, audio stripped — the unified cut keeps its single combined voiceover; S4's duration is unchanged so offsets are unaffected).

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-04-the-boring-parts-disappear/`
- Source: `02-script.md` + `04-voiceover.md` + remade `05-visual-plan.md` + remade Section 4 visual plan and reference board
- Port: `1004`
- Studio URL: `http://localhost:1004/#project/section-04-the-boring-parts-disappear`
- Direct composition URL: `http://localhost:1004/api/projects/section-04-the-boring-parts-disappear/preview/comp/index.html`
- Runtime: `37.867s`
- Voiceover: `section-04-the-boring-parts-disappear-david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-04-the-boring-parts-disappear/section-04-the-boring-parts-disappear-visual-plan.md`
- Latest contact sheet: `snapshots/remake-simple-20260612/contact-sheet-simple-remake.png`

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source Plan |
|---:|---:|---|---|---|---|
| 1 | `0.000-4.790` | `boring parts are where the future lives` | Fabric/stitching photo background, giant suspicious WIT, `BORING FUTURE` label. | static hard cut | remade visual plan cue 1 |
| 2 | `4.800-9.800` | `quality of material, stitching, hinge` | Same fabric/stitching background and WIT, one added material-list label. | static hard cut | remade visual plan cue 2 |
| 3 | `9.800-16.190` | `repairable... understand repair` | Screwdriver repair-table background, generic device mockup, `REPAIRABLE`, crossed `SECRET HANDSHAKE`. | static hard cut | remade visual plan cue 3 |
| 4 | `16.200-20.490` | `finding spare parts later` | Same repair-table background, small drawer, `SPARE PART STILL EXISTS`. | static hard cut | remade visual plan cue 4 |
| 5 | `20.500-28.790` | `printer people should be shocked` | Same repair-table background, generic printer mockup, giant thinking WIT, dry quote. | static hard cut | remade visual plan cue 5 |
| 6 | `28.800-37.867` | `cheap product looks complete but... future built in` | Cardboard/product-box background, generic box, final labels, giant betrayed WIT. | static hard cut | remade visual plan cue 6 |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.000` | `boring parts` | `BORING FUTURE` and suspicious WIT | visible immediately | matched |
| `4.800` | `material, stitching, hinge` | `FABRIC + STITCHING + HINGE` | cue visible | matched |
| `9.800` | `repairable` | generic device and `REPAIRABLE` | cue visible | matched |
| `12.000` | `secret handshake` | red crossed `SECRET HANDSHAKE` | held inside cue | matched |
| `16.200` | `spare parts later` | `SPARE PART STILL EXISTS` | cue visible | matched |
| `20.500` | `printer person` | printer mockup, thinking WIT, quote | cue visible | matched |
| `28.800` | `looks complete... less future` | product box, final label, betrayed WIT | cue visible | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| cue | next cue in same big scene | hard cut / overlay replacement | keeps Section 4 calm and readable | low | keep |
| big scene | next big scene | hard cut | narration changes object/context | low | keep |

## Element Motion Notes

- Entrances: `none`
- Holds: `each cue is readable as a static paused frame`
- Emphasis: `SECRET HANDSHAKE` red slash and final `LESS FUTURE BUILT IN` stamp only
- Exits: `none before cue replacement`
- Repeated effects avoided: `no fly-ins, no card pile, no dense object tray, no decorative transition`

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal working set under `section-previews/section-04-the-boring-parts-disappear/assets/`
- Review mirror assets: copied to `hyperframes/review/assets/section-04/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used: `suspicious`, `thinking`, `betrayed`
- WIT layout update: WIT appears only on emotional beats and is sized to read as a main character, not a corner sticker. The opening and printer WIT occupy roughly the left half of the frame; the final WIT occupies roughly the right third-to-half with the face unobstructed.
- Direct real background assets used: `fabric.jpg`, `screwdriver.jpg`, `cardboard.jpg`
- Reference-only assets not used directly: phone repair photo, printer repair photo, and hinge reference
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: `pass with 2 non-blocking warnings: duplicate media discovery risk from repeated WIT image sources and one dense cue track`
- validate: `pass; no console errors; 5 non-blocking contrast sampler warnings remain on one inactive/timed material-list label context`
- inspect: `pass; 0 layout issues at 0.5, 3.3, 5.6, 8.3, 10.4, 13.8, 17.8, 21.6, 25.5, 30.5, 34.8, 37.2`
- render: `not requested`
- preview server: `running on port 1004; Studio URL and direct composition URL returned HTTP 200`
- visual snapshot check: `snapshots/remake-simple-20260612/contact-sheet-simple-remake.png` inspected at `0.8`, `6.0`, `12.0`, `18.6`, `25.4`, `32.4`, and `36.9`; the remake now uses 3 big backgrounds, 6 cue states, sparse labels, and large readable WIT placements

## Notes

The first Section 4 build direction was rejected because it became visually crowded: too many cards, text blocks, object cutaways, and scattered images competed on screen. This remake intentionally starts over from the Section 1 grammar: a few strong photo backgrounds, one or two large labels per beat, and WIT as the main emotional read. Do not regenerate Section 4 from the rejected object-card / parts-tray approach unless the user explicitly asks for that direction again.

No MP4/WebM export was created. The review source is the running preview and the mirrored HTML at `hyperframes/review/section-04.html`.
