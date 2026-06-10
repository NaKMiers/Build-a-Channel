# Section 2 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 2: Cheap Is Not The Villain`

Status:
`revised generated-base preview running on fixed section port`

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-02-cheap-is-not-the-villain/`
- Source: `02-script.md` + `04-voiceover.md` + revised `05-visual-plan.md` + Section 2 visual plan and reference board
- Port: `1002`
- Studio URL: `http://localhost:1002/#project/section-02-cheap-is-not-the-villain`
- Direct composition URL: `http://localhost:1002/api/projects/section-02-cheap-is-not-the-villain/preview/comp/index.html`
- Runtime: `22.315s`
- Voiceover: `section-02-cheap-is-not-the-villain-david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-02-cheap-is-not-the-villain/section-02-cheap-is-not-the-villain-visual-plan.md`

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source Plan |
|---:|---:|---|---|---|---|
| 1 | `0.000-2.700` | `not about saying cheap things are bad` | Real tag photo base, `CHEAP`, `BAD?`, red cross-out, suspicion WIT. | static hard cut | visual plan cue 1 |
| 2 | `2.700-5.900` | `unfair... emotionally expensive` | Same tag correction board plus fake receipt, `EMOTIONAL TAX`, `UNFAIR`, empty-wallet WIT. | static hard cut | visual plan cue 2 |
| 3 | `5.900-7.790` | `Some affordable products are great.` | Generated two-box base, left box labeled `AFFORDABLE + WORKS`, check badge, pointing WIT. | static hard cut | visual plan cue 3 |
| 4 | `7.800-10.700` | `regular products wearing a nicer jacket` | Same generated two-box base, right box gets rebuilt jacket overlay, `EXPENSIVE != MAGIC`, deadpan WIT. | static hard cut | visual plan cue 4 |
| 5 | `10.700-13.100` | `real question is smaller` | Generated cutaway base, `THE REAL QUESTION`, `LOOK INSIDE`, thinking WIT. | static hard cut | visual plan cue 5 |
| 6 | `13.100-16.400` | `less tomorrow inside them` | Same generated cutaway base, `MISSING TOMORROW`, four future slots. | static hard cut | visual plan cue 6 |
| 7 | `16.400-18.700` | `Less strength. Less repair.` | Strength slot cracks first; repair slot appears inside the same cue at `17.45s`. | one deterministic `tl.set` reveal for repair | visual plan cue 7 |
| 8 | `18.700-19.800` | `Less support.` | Support slot becomes the focused missing piece. | static hard cut | visual plan cue 8 |
| 9 | `19.800-22.315` | `Less time before... buy the same thing again.` | Time slot focuses; receipt loop points to a new box; `BUY AGAIN SOON`; defeated WIT. | static hard cut | visual plan cue 9 |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.000` | `cheap things are bad` | `CHEAP != BAD` and red cross-out | visible immediately | matched |
| `2.700` | `unfair... emotionally expensive` | fake receipt and `EMOTIONAL TAX` | cue visible | matched |
| `5.900` | `affordable products are great` | generated two-box comparison, left good product | new big scene | matched |
| `7.800` | `nicer jacket` | right product jacket overlay and deadpan WIT | cue visible | matched |
| `10.700` | `smaller... annoying` | generated cutaway base with `LOOK INSIDE` | new big scene | matched |
| `13.100` | `less tomorrow inside them` | `MISSING TOMORROW` cutaway slots | cue visible | matched |
| `16.400` | `Less strength` | cracked strength slot | cue visible | matched |
| `17.450` | `Less repair` | repair slot and screw circle | cue-level reveal | matched |
| `18.700` | `Less support` | support slot focus | cue visible | matched |
| `19.800` | `buy the same thing again` | receipt loop and new box | cue visible | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| cue | next cue in same big scene | hard cut or static overlay replacement | approved section style; visual continuity comes from the persistent base image | low | keep |
| big scene | next big scene | hard cut | narration moves to a new object or mechanism | low | keep |

## Element Motion Notes

- Entrances: `none`
- Holds: `each cue is readable as a static paused frame`
- Emphasis: `red cross-out, unfair stamp, check badge, rebuilt jacket, slot focus cards, receipt loop`
- Exits: `none before cue replacement`
- Repeated effects avoided: `no repeated pop-ins or default transitions`
- One internal timing action: `repair slot opacity switches on at 17.45s so Less repair does not appear too early while keeping the cue-state count at 9`

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal hardlinked working set under `section-previews/section-02-cheap-is-not-the-villain/assets/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used: `price-tag-suspicion`, `empty-wallet`, `pointing-right`, `deadpan-side-eye`, `thinking`, `suspicious`, `tiny-defeated`
- Direct real assets used: `real-blank-tag-pexels-padrinan.jpg`
- Direct generated support assets used: `fair-comparison-two-boxes-generated.png`, `missing-tomorrow-cutaway-generated.png`
- Mockup/reference-only assets not used directly: `real-receipt-pexels-towfiqu-barbhuiya.jpg`, `real-black-jacket-hanger-pexels-mishchenko.jpg`, `real-plain-white-boxes-pexels-dalprat.jpg`
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: `pass with 2 non-blocking warnings: duplicate media discovery risk from repeated static WIT/image references, and dense cue track from 9 timed cue clips`
- validate: `pass; no console errors; 225 text elements pass WCAG AA`
- inspect: `pass; 0 layout issues at 0.4, 2.8, 5.0, 6.6, 8.8, 11.4, 14.4, 16.7, 17.8, 18.9, 20.8, 22.0`
- render: `not requested`
- preview server: `running on port 1002; direct composition URL returned HTTP 200`
- visual thumbnail check: `latest generated-base thumbnails inspected at comparison, cutaway, and support beats`

## Notes

This rerender fixes the earlier visual-plan/render mismatch. The prior Section 2 preview used CSS-built boxes and a CSS-built cutaway; this version uses the revised visual plan's generated two-box comparison base and generated missing-tomorrow cutaway base directly, then adds all labels, WIT, red marks, and jokes in HyperFrames.
