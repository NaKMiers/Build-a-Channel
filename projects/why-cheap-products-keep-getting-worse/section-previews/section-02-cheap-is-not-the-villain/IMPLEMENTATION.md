# Section 2 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 2: Cheap Is Not The Villain`

Status:
`review-adjusted giant-WIT preview with subtitle-safe lower layout running on fixed section port`

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-02-cheap-is-not-the-villain/`
- Source: `02-script.md` + `04-voiceover.md` + `05-visual-plan.md` + render-side review-prevention pass
- Port: `1002`
- Studio URL: `http://localhost:1002/#project/section-02-cheap-is-not-the-villain`
- Direct composition URL: `http://localhost:1002/api/projects/section-02-cheap-is-not-the-villain/preview/comp/index.html`
- Runtime: `22.315s`
- Voiceover: `section-02-cheap-is-not-the-villain-david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-02-cheap-is-not-the-villain/section-02-cheap-is-not-the-villain-visual-plan.md`

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| 1 | `0.000-2.700` | `cheap things are bad` | Wrong-villain correction | Real blank tag crop shows `CHEAP`, `BAD?`, red X, and learner-friendly anchor `CHEAP IS NOT BAD`. | static | Giant facepalm WIT rises from the lower/right edge; face and shoulders clear, lower body intentionally cropped. | Red X targets `BAD?`, not `CHEAP`. | matched |
| 2 | `2.700-5.900` | `unfair... emotionally expensive` | Wrong-villain correction | `BAD?` and red X clear; `UNFAIR`, fake shopping receipt, and `EMOTIONALLY EXPENSIVE` appear in separate zones. | phrase-timed hard-show | Same giant facepalm WIT holds as the emotional reaction; labels stay readable over/around the WIT zone. | Receipt uses fake text only; `UNFAIR` no longer overlaps the emotion label. | matched |
| 3 | `5.900-7.800` | `Some affordable products are great.` | Fair comparison | Generated two-box base shows `AFFORDABLE + WORKS` and `OK`. | static | No WIT; box and check carry the beat. | No red markup. | matched |
| 4 | `7.800-10.700` | `nicer jacket` | Fair comparison | Right box gets rebuilt generic jacket, `REGULAR PRODUCT`, `NICE JACKET`, and `EXPENSIVE IS NOT MAGIC`. | hard-show | Giant confused WIT peeks from the right, behind the jacket/labels; face fully visible, lower body cropped. | `EXPENSIVE IS NOT MAGIC` moved left of the jacket so it remains readable. | matched |
| 5 | `10.700-13.100` | `real question is smaller` | Missing-tomorrow autopsy | Generated cutaway base opens with `THE REAL QUESTION`, small annoyance note, `LOOK INSIDE`, and arrow. | static | No WIT yet; object inspection leads. | Arrow points to compartments. | matched |
| 6 | `13.100-16.400` | `less tomorrow inside them` | Missing-tomorrow autopsy | Question labels clear; `MISSING TOMORROW`, four compartments, and shocked WIT appear. | phrase-timed hard-show | Giant shocked WIT peeks from the right; head/shoulders/face clear and text remains unobstructed. | Main reframe label dominates. | matched |
| 7 | `16.400-18.700` | `Less strength. Less repair.` | Missing-tomorrow autopsy | Strength slot changes to `LESS STRENGTH`; repair slot changes later at `17.45s` to `LESS REPAIR` with a small red screw circle. | phrase-timed hard-show | Same shocked WIT holds; no WIT spam. | Decorative crack removed after frame QA because it covered text. | matched |
| 8 | `18.700-19.800` | `Less support.` | Missing-tomorrow autopsy | Support slot changes to `LESS SUPPORT` with dark support-light mark. | hard-show | Same shocked WIT holds. | No extra arrows. | matched |
| 9 | `19.800-22.315` | `Less time before... buy the same thing again.` | Missing-tomorrow autopsy | Time slot changes to `LESS TIME`; buy-again box, receipt loop, and `BUY AGAIN SOON` appear. | hard-show | Shocked WIT clears; giant money-panic WIT rises from the lower/right edge without text covering face or key prop. | Loop arrow connects product to new box. | matched |

## Render Review-Prevention Pass

- voice cue map completed: `yes`
- big-scene sanity checked: `yes - kept 3 persistent big scenes`
- cue density checked: `yes - reduced timed clip density by grouping overlays per big scene`
- motion density checked: `yes - no decorative transitions; phrase-timed hard-shows only`
- WIT density: `4 WIT beats total across 22.315s; no WIT on every cue`
- WIT crop/collision checked: `yes - review-pass-8 contact sheet checked giant WIT, safe head/shoulder/face crop, and text-over-WIT directions`
- markup target checked: `yes - removed crack that hurt readability; red X and repair circle target exact objects`
- scene differentiation checked: `yes - real tag, generated comparison, and generated cutaway remain distinct`
- HyperFrames mechanics checked: `yes - root duration, audio clip, deterministic GSAP timeline, data-start/data-duration/data-track-index`
- render decisions made beyond visual plan: `reduced WIT appearances, grouped overlays into 3 timed scene overlays, changed opening anchor to CHEAP IS NOT BAD, removed decorative crack after snapshot QA, moved UNFAIR and EXPENSIVE IS NOT MAGIC to prevent label collisions, replaced small/corner WIT poses with giant behind-layer facepalm/confused/shocked/money-panic emotional beats, and raised bottom-adjacent labels/receipt-loop props into a subtitle-safe zone for YouTube captions`

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.000` | `cheap things are bad` | `CHEAP`, `BAD?`, red X, `CHEAP IS NOT BAD` | visible immediately | matched |
| `2.700` | `unfair... emotionally expensive` | `UNFAIR`, fake receipt, `EMOTIONALLY EXPENSIVE` | hard-show | matched |
| `5.900` | `affordable products are great` | two boxes, `AFFORDABLE + WORKS`, `OK` | hard cut | matched |
| `7.800` | `nicer jacket` | jacket overlay, `NICE JACKET`, `EXPENSIVE IS NOT MAGIC`, confused WIT | hard-show | matched |
| `10.700` | `real question is smaller` | cutaway base, `THE REAL QUESTION`, `LOOK INSIDE` | hard cut | matched |
| `13.100` | `less tomorrow inside them` | `MISSING TOMORROW`, compartment labels, shocked WIT | hard-show | matched |
| `16.400` | `Less strength` | `LESS STRENGTH` slot | hard-show | matched |
| `17.450` | `Less repair` | `LESS REPAIR` slot and screw circle | hard-show | matched |
| `18.700` | `Less support` | `LESS SUPPORT` slot | hard-show | matched |
| `19.800` | `Less time... buy the same thing again` | `LESS TIME`, receipt loop, new box, money-panic WIT | hard-show | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| Big scene 1 | Big scene 2 | hard cut | narration moves from fairness correction to product comparison | low | keep |
| Big scene 2 | Big scene 3 | hard cut | narration moves from comparison joke to real reframe | low | keep |
| Cues inside big scenes | next cue | phrase-timed hard-show | supports voice sync without noisy animation | low | keep |

## Element Motion Notes

- Entrances: `hard-show only`
- Holds: `base scene and WIT hold while small cue elements change`
- Emphasis: `red X, UNFAIR stamp, OK badge, jacket gag, missing-tomorrow slot changes, buy-again loop`
- Exits: `bad accusation clears before UNFAIR appears; shocked WIT clears before final money-panic WIT`
- Repeated effects avoided: `no repeated pop/fly-ins; no default transitions`
- Hard-show vs impact decisions: `all ordinary labels hard-show; no impact animation was needed for this conceptual reframe`
- WIT scale/crop checks: `runtime-seek review-pass-8 contact sheet reviewed at 0.4, 2.9, 8.8, 14.4, 20.8, and 22.0`

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal hardlinked working set under `section-previews/section-02-cheap-is-not-the-villain/assets/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used: `facepalm`, `confused`, `shocked`, `money-panic`
- Direct real assets used: `real-blank-tag-pexels-padrinan.jpg`
- Direct generated support assets used: `fair-comparison-two-boxes-generated.png`, `missing-tomorrow-cutaway-generated.png`
- Reference-only assets not used directly: `real-receipt-pexels-towfiqu-barbhuiya.jpg`, `real-black-jacket-hanger-pexels-mishchenko.jpg`, `real-plain-white-boxes-pexels-dalprat.jpg`
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: `pass; 0 errors, 0 warnings`
- validate: `pass; no blocking errors; 15 non-blocking contrast sampler warnings from the small final receipt text`
- inspect: `pass; 0 layout issues at 0.4, 2.8, 5.0, 6.6, 8.8, 11.4, 14.4, 16.7, 17.8, 18.9, 20.8, 22.0`
- direct preview screenshots/contact sheet: `snapshots/review-pass-8/contact-sheet.jpg` reviewed after giant-WIT fixes
- export/render, only if explicitly requested: `not requested; no MP4/WebM generated`
- preview server: `port 1002 reused; endpoints returned HTTP 200 after update`

## Manual Preservation Save

- Date: `2026-06-12`
- Trigger: `Anh Khoa manually adjusted Section 2 on localhost/Studio and asked to save before future edits.`
- Canonical source: `section-previews/section-02-cheap-is-not-the-villain/index.html`
- Latest backup snapshot: `section-previews/section-02-cheap-is-not-the-villain/manual-saves/save-110159.html`
- Previous backup snapshot: `section-previews/section-02-cheap-is-not-the-villain/manual-saves/save-105019.html`
- Saved hash: `0BFC3AD707F709F145A6DB919AC6BCBCFC75ADC7C9D329277AFEC63BE9F6DD14`
- Review mirror: `hyperframes/review/section-02.html` was synced from the current preview source after the manual save.
- Preservation rule: future Section 2 updates must read and diff the current preview `index.html` first, preserve `data-hf-studio-*` and manual layout edits, and never overwrite from visual-plan output, older generated drafts, or an older review mirror. Mirror only from preview to review after edits are accepted.

## Notes

This update is a render-side quality recovery pass, not a script or voiceover change. It keeps the Section 2 visual plan's real/generated asset choices but improves execution by reducing timed clip density, keeping WIT frequency controlled, replacing small/corner WIT with giant Section-1-style emotional placements, removing decorative clutter, and making the opening correction more learner-friendly.

Subtitle-safe pass:
The lower-third elements most likely to be covered by YouTube subtitles were nudged upward without changing the approved scene structure: `CHEAP IS NOT BAD`, `NICE JACKET`, and the final `AGAIN` receipt/loop cluster now sit higher in the frame. The stale `show("#jacket-overlay")` GSAP call was also removed so the current manual Studio deletion stays clean in validation.
