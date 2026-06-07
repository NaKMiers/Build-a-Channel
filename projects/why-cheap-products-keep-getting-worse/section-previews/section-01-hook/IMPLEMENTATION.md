# Section 1 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 1: Hook`

Status:
`preview running - ready for review`

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-01-hook/`
- Source: `projects/why-cheap-products-keep-getting-worse/visual-plan/section-01-hook/section-01-hook-visual-plan.md`
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `21.605s`
- Voiceover: `assets/voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-01-hook/section-01-hook-visual-plan.md`

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source Plan |
|---|---:|---|---|---|---|
| 1 | `0:00-2.35` | `I find a chair for nine dollars.` | Clean chair with yellow tag, WIT pointing, `$9 CHAIR` | Label writes/slides in; WIT enters from left; small camera push | Board 1 deal setup |
| 2 | `2.35-4.75` | `four legs... confidence of a much better chair` | Same chair with confidence badge and note card | Short continuation transition; badge pops; note card rises | Board 2 confidence beat |
| 3 | `4.75-6.70` | `So he buys it.` | Under-chair hidden tag with `FUTURE NOT INCLUDED` | Reveal transition; tag label clips on; WIT stays unaware | Board 3 hidden future reveal |
| 4 | `6.70-9.20` | `For the first week, everything is fine.` | Chair returns with week card and question mark | Reset transition; week card drops in; question mark lands late in beat | Board 4 false calm |
| 5 | `9.20-11.90` | `noise that sounds like legal advice` | Hidden-tag angle with legal slip and creak scribble | Suspicion transition; legal slip slides out; scribble pops | Board 5 legal-advice gag |
| 6 | `11.90-15.90` | `screw gets loose... seat feels nervous... one leg...` | Loose-screw close-up with red circle, wobble marks, arrow, betrayed WIT | Consequence transition; circle lands on screw; wobble and arrow chain to cues | Board 6 failure proof |
| 7 | `15.90-18.40` | `not really cheap` | Desk/receipt evidence board with inset real receipt and cost tags | Evidence transition; receipt tags arrive in two beats; WIT holds evidence | Board 7 hidden cost evidence |
| 8 | `18.40-21.605` | `one small problem... future not included` | Real blank tag hero frame, tiny defeated WIT, red stamp | Payoff transition; small problem note enters; stamp lands on final line | Board 8 title promise payoff |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.18` | `chair for nine dollars` | `$9 CHAIR` | label enters and is readable before the phrase finishes | pass |
| `2.75` | `confidence` | confidence badge | badge lands during the confidence joke | pass |
| `5.08` | `So he buys it` | `FUTURE NOT INCLUDED` tag text | audience sees the trap before WIT | pass |
| `7.00` | `first week` | week card | calm board is readable immediately | pass |
| `9.82` | `legal advice` | legal slip | fake legal memo slides into frame on the joke | pass |
| `12.08` | `screw gets loose` | red circle | cue-critical circle lands directly on screw | pass |
| `14.18` | `other career options` | arrow + `ONE LEG: RESIGNING` | resignation beat gets the final visual emphasis | pass |
| `16.34` | `not really cheap` | `$9 NOW` / `BUY AGAIN LATER` | bargain becomes visible receipt logic | pass |
| `20.34` | `future not included` | final red stamp | stamp lands on the slowed final phrase | pass |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| 1 | 2 | continuation push | same object, same idea, bigger joke | low | keep |
| 2 | 3 | reveal drop | viewer moves under the chair to find the trap | low | keep |
| 3 | 4 | reset fade | false calm after hidden reveal | low | keep |
| 4 | 5 | suspicion slide | quiet scene turns strange | low | keep |
| 5 | 6 | consequence push | sound joke becomes physical failure | low | keep |
| 6 | 7 | evidence lift | mechanical failure becomes cost proof | low | keep |
| 7 | 8 | payoff settle | receipt logic resolves into the title phrase | low | keep |

## Element Motion Notes

- Entrances: labels and cards use different directions and eases; no repeated global pop-in pattern
- Holds: most photo boards stay nearly still after the entrance so labels remain readable
- Emphasis: screw circle, wobble, arrow, receipt tags, and final stamp are tied to spoken emphasis
- Exits: handled by the short scene transition, not by pre-transition element fade-outs
- Repeated effects avoided: only the wobble beat uses visible shake; other boards use slide, clip-on, or stamp motion

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section preview asset working set: `projects/why-cheap-products-keep-getting-worse/section-previews/section-01-hook/assets/`
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: `pass with 1 non-blocking warning (composition_file_too_large)`
- validate: `pass`
- inspect: `pass`
- render: `not run`

## Notes

- The original local `assets/` junction matched the render skill rule, but HyperFrames CLI checks returned 404s for image assets on this Windows setup.
- To keep the preview working without copying the full project asset library, the preview now uses a minimal hardlinked `assets/` working set that points back to the approved shared assets.
