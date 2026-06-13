# Section 4 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 4: The Boring Parts Disappear`

Status:
`simple Section-1-style remake preview running on fixed section port`

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
