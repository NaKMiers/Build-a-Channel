# Section 6 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 6: Repair Gets A Security System`

Status:
`auto-adjusted image-base preview ready for review`

## Result

- Preview project: `section-previews/section-06-repair-gets-a-security-system/`
- Source: `02-script.md` + `04-voiceover.md` + `05-visual-plan.md` + Section 6 visual plan + user recovery feedback
- Port: `1006`
- Studio URL: `http://localhost:1006/#project/section-06-repair-gets-a-security-system`
- Direct composition URL: `http://localhost:1006/api/projects/section-06-repair-gets-a-security-system/preview/comp/index.html`
- Runtime: `42.816s`
- Voiceover: `voiceover/section-06-repair-gets-a-security-system/scratch-audio/section-06-repair-gets-a-security-system-david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-06-repair-gets-a-security-system/section-06-repair-gets-a-security-system-visual-plan.md`
- Review mirror: `hyperframes/review/section-06.html`

## Recovery Decision

The first Section 6 build used self-made CSS repair-door/product/checklist graphics. The user rejected that direction as too graphic-heavy and asked to reference Sections `3`, `1`, and `8`. This pass supersedes the CSS-heavy render with the same script and timing but uses dominant illustrative image bases, sparse labels, and large WIT emotional beats.

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source |
|---|---:|---|---|---|---|
| 1 | `0.0-18.7s` | `repair`, `harder than replacing`, `part/tool/manual`, `repair costs` | Opened phone repair table photo with sparse repair labels | Static base plus hard-show labels/stamp | Section 6 visual plan, remade through Section 1/3/8 image-base grammar |
| 2 | `18.7-23.6s` | `You own me... not enough`, `Very healthy relationship` | Darkened phone repair close-up with trapped WIT and speech bubble | Static hard cut | User recovery feedback |
| 3 | `23.6-34.4s` | `repairability matters`, `easy to fix`, checklist questions | Precision screwdriver photo with definition card and compact checklist | Static hard-show checklist | User recovery feedback |
| 4 | `34.4-42.816s` | `governments`, `labels`, `Please have a future` | Cardboard texture, simplified phone future label, giant deadpan WIT | Static hard cut plus final underline | Visual plan scene 4, simplified to avoid official label copying |

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| 1 | `0.0-3.2s` | `The third reason is repair` | Opened phone repair table | Image base establishes the repair world | `static` | Suspicious WIT left edge, large, face/head/shoulders visible | `REPAIR` | mapped |
| 2 | `3.2-7.4s` | `harder than replacing it` | Opened phone repair table | Replacement warning label and `NEW ONE` sticky appear | `hard-show` | No WIT; image carries the beat | `FIXING IS HARDER THAN REPLACING`, `NEW ONE` | mapped |
| 3 | `7.4-13.8s` | `part/tool/manual` | Opened phone repair table | Three sticky blockers appear on top of the real device image | `hard-show` | No WIT; labels stay off the main phone detail | `NO PART`, `SPECIAL TOOL`, `NO MANUAL` | mapped |
| 4 | `13.8-18.7s` | `repair costs almost as much as buying a new one` | Opened phone repair table | Repair bill card and cost stamp appear | `hard-show` / `impact mark` | No WIT; cost card is the focus | `REPAIR BILL`, `ALMOST NEW PRICE` | mapped |
| 5 | `18.7-23.6s` | `You own me... not enough`, `Very healthy relationship` | Dark locked close-up | Speech bubble and trapped WIT appear over dim repair photo | `hard cut` | Trapped WIT right side, enlarged after screenshot review, face clear | `YOU OWN ME, BUT NOT ENOUGH TO OPEN ME`, `VERY HEALTHY RELATIONSHIP` | mapped |
| 6 | `23.6-28.0s` | `Repairability just means how easy something is to fix` | Screwdriver base | Definition card appears over real tool image | `hard cut` | No WIT breathing beat | `REPAIRABILITY / EASY TO FIX` | mapped |
| 7 | `28.0-34.4s` | `battery`, `part`, `local repair shop`, `mysterious machine` | Screwdriver base | Compact checklist appears instead of multiple drawn props | `hard-show` | No WIT breathing beat | `REPLACE BATTERY`, `BUY THE PART`, `READ THE MANUAL`, `NO MYSTERY MACHINE` | mapped |
| 8 | `34.4-42.816s` | `repair information`, `spare parts`, `battery life`, `repairability labels`, `Please have a future` | Cardboard/future label | Simplified label card, final future request, giant deadpan WIT | `hard cut` / `hold` | Deadpan WIT right side, large, face/glasses clear of final tag | `PHONE FUTURE LABEL`, `PLEASE HAVE A FUTURE` | mapped |

## Render Review-Prevention Pass

- voice cue map completed: `yes`
- big-scene sanity checked: `yes, 4 persistent scenes for 42.816s`
- cue density checked: `yes, 8 cue states`
- motion density checked: `yes, hard-show by default`
- WIT density: `3 total WIT beats; Scene 1: 1, Scene 2: 1, Scene 3: 0, Scene 4: 1`
- WIT crop/collision checked: `yes, direct preview screenshots verify faces/glasses clear of labels`
- image-base correction checked: `yes, each big scene now has a dominant photo/object texture`
- markup target checked: `repair labels attach to the opened phone image; cost stamp targets the bill card; final underline targets FUTURE`
- scene differentiation checked: `repair table, locked close-up, screwdriver base, and cardboard future-label scene are visually distinct`
- HyperFrames mechanics checked: `standalone HTML source, data-start/data-duration/data-track-index, audio clip, synchronous timeline registration`
- render decisions made beyond visual plan: `superseded CSS repair-door graphics after user feedback; used direct image bases with attribution`

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.0` | `third reason is repair` | Repair photo, large suspicious WIT, `REPAIR` | static open | mapped |
| `3.2` | `harder than replacing it` | Fixing/replacing warning and `NEW ONE` sticky | hard-show | mapped |
| `7.4` | `part/tool/manual` | Three blocker stickies over phone photo | hard-show | mapped |
| `13.8` | `repair costs almost as much` | Repair bill and `ALMOST NEW PRICE` stamp | hard-show / impact mark | mapped |
| `18.7` | `You own me... not enough` | Dark phone close-up, speech bubble, trapped WIT | hard cut | mapped |
| `23.6` | `repairability matters` | Screwdriver photo and definition card | hard cut | mapped |
| `28.0` | `battery? part? local repair shop?` | Compact checklist | hard-show | mapped |
| `34.4` | `Some governments now treat...` | Simplified future-label card on cardboard texture | hard cut | mapped |
| `41.6` | `Please have a future` | Final tag and giant deadpan WIT | hold / emphasis mark | mapped |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| Scene 1 | Scene 2 | hard cut | Ownership joke is a punchline reset | low | keep hard cut |
| Scene 2 | Scene 3 | hard cut | Move from joke to definition | low | keep hard cut |
| Scene 3 | Scene 4 | hard cut | Move from practical tests to policy proof | low | keep hard cut |

## Element Motion Notes

- Entrances: timed clips hard-show on the spoken cue.
- Holds: each big scene holds while the voice describes the same repair concept.
- Emphasis: `ALMOST NEW PRICE` stamp and `FUTURE` underline carry the only impact emphasis.
- Exits: clip duration clears old cues; no explicit exit animation.
- Repeated effects avoided: no label parade, no fly-ins, no camera moves.
- WIT scale/crop checks: WIT is deliberately large on emotional beats; screenshot contact sheet verifies visible footprint and face safety.

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: `projects/why-cheap-products-keep-getting-worse/assets/section-06/`
- Runtime assets: minimal hardlinked working set under `section-previews/section-06-repair-gets-a-security-system/assets/section-06/` and `hyperframes/review/assets/section-06/`
- Direct image bases: `phone-repair-table.jpg`, `precision-screwdrivers.jpg`, `cardboard-boxes.jpg`
- Attribution: updated in `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`
- Reference-only assets still not used directly: repair lab photo and European Commission smartphone/tablet label screenshot

## Verification

- lint: `pass with 3 non-blocking warnings`
  - duplicate media discovery risk from using the same phone photo in two timed scenes
  - dense track warnings for the single-file preview style
- validate: `pass, no console errors, 165 text elements pass WCAG AA`
- inspect: `pass, 0 layout issues across 10 explicit timestamps`
- direct preview console after reload: `no console errors`
- direct preview screenshots/contact sheet: `pass via snapshots/refine-image-bases-20260614/contact-sheet-section-06-image-base-refine-final.png`
- export/render, only if explicitly requested: `not requested`

## Auto Adjust 2026-06-15

Target:
`projects/why-cheap-products-keep-getting-worse` / `Section 6`

Backup created before editing:
`manual-saves/auto-adjust-20260615-080132-index.html`

Issues found:

| Issue | Evidence | Fix | Verification |
|---|---|---|---|
| Opening WIT was still under the Auto Adjust visible-width gate | Alpha audit measured `wit-pose-suspicious.png` at `374x591`, `19.5%` visible frame width | Increased `.wit-suspicious` from `780px` to `1040px` and repositioned as a stronger left-edge lower-body crop | Post-fix alpha audit: `500x732`, `26.0%` visible frame width; contact sheet frame `t=0.8` passes |
| Final deadpan WIT was emotionally readable but still narrow by the strict gate | Alpha audit measured `wit-pose-deadpan-side-eye.png` at `442x944`, `23.0%` visible frame width | Increased `.wit-deadpan` from `1360px` to `1600px` and shifted right/down to keep the face clear of the label | Post-fix alpha audit: `520x1003`, `27.1%` visible frame width; contact sheet frames `t=37.0`, `t=41.8`, `t=42.6` pass |
| Normal restart could ignore the fixed Section 6 port | `npm run dev` started HyperFrames on the default Studio port instead of `1006` | Updated `package.json` dev script to `hyperframes preview --port 1006` | Direct composition URL returned HTTP `200` on `localhost:1006` |

WIT audit after fix:

| Cue | Pose | CSS Box | Alpha Ratio | Visible Size | Region | Pass/Fail | Fix |
|---|---|---:|---|---|---|---|---|
| `cue-repair` / `0.8s` | `wit-pose-suspicious.png` | `1040x1040` | `0.480 x 0.854` | `500x732` (`26.0%` width, `67.8%` height) | left edge / giant lower-body crop | pass | scaled up from `780px` |
| `cue-ownership-joke` / `21.2s` | `wit-pose-trapped-by-app-screen.png` | `960x960` | `0.504 x 0.861` | `484x675` (`25.2%` width, `62.5%` height) | right-side trapped screen | pass | no change needed |
| `cue-policy-future` / `41.8s` | `wit-pose-deadpan-side-eye.png` | `1600x1600` | `0.325 x 0.857` | `520x1003` (`27.1%` width, `92.9%` height) | right side / giant deadpan | pass | scaled up from `1360px` |

Auto Adjust verification:

- `npm.cmd run check`: `pass`
- lint: `pass with 3 non-blocking warnings`
  - duplicate media discovery risk from using the same phone photo in two timed scenes
  - dense track warnings for the single-file preview style
- validate: `pass, no console errors, 165 text elements pass WCAG AA`
- inspect: `pass, 0 layout issues across 10 explicit timestamps`
- direct preview screenshot/contact sheet: `snapshots/auto-adjust-20260615/contact-sheet-section-06-auto-adjust.png`
- preview server: `http://localhost:1006/api/projects/section-06-repair-gets-a-security-system/preview/comp/index.html` returned HTTP `200`
- review mirror synced: `hyperframes/review/section-06.html`
- MP4/WebM export: `not requested`

## Notes

- This file supersedes the earlier CSS-heavy Section 6 render notes.
- The opened phone photo has visible source-product markings; it is used as a generic repair-table background only, with no claim that the pictured product is defective or criticized.
- The policy label remains a simplified fake HyperFrames card; the European Commission reference image is not copied into the render.
- The build follows the existing project exception for Windows HyperFrames asset serving by using minimal hardlinked preview/review assets instead of a junction.
