# Section 1 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 1: Hook`

Status:
`minimal animation pass preview ready for review`

## Result

- Preview project: `projects/why-cheap-products-keep-getting-worse/section-previews/section-01-hook/`
- Source: `02-script.md` + `04-voiceover.md` + real WIT manifest + user reviews on connected big-scene pacing, fewer cues, meaningful markup, larger WIT, and exact callout alignment
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `21.205s`
- Voiceover: `section-01-hook-david23-am_eric-0.84.mp3`
- Visual plan: old visual plan explicitly skipped by user request; current revision follows the user-reviewed big-scene/small-cue mechanism with reduced cue count
- Export file: `not requested`
- MP4 files removed: `section-01-hook-animated.mp4` and `section-01-hook-remake.mp4` were deleted by user request
- Preview QA rule: use Studio/direct preview screenshots for normal render fixes; do not export MP4 unless the user explicitly asks

## Big Scene Plan Implemented

| Big Scene | Local Time | Base Visual | Purpose |
|---:|---:|---|---|
| 1 | `0.000-8.400` | Same chair photo holds through setup, product details, purchase, and first week. | Introduce the object without rushing through unrelated boards. |
| 2 | `8.400-16.400` | Same broken-leg close-up holds through legal creak, loose screw, and career-options leg. | Let the failure escalate inside one connected scene without a washed overlay. |
| 3 | `16.400-21.205` | Same desk/tag/receipt board holds through true-cost and final payoff. | Land the cost reveal and `FUTURE NOT INCLUDED` without a new visual reset. |

## Motion Plan Implemented

| Target | Timing | Motion | Reason | Sync Guard |
|---|---:|---|---|---|
| Scene 1 -> Scene 2 | `8.400-8.620` | Incoming broken-leg scene fades in with small blur/scale settle over the chair scene. | Smooths the move from normal chair to failure close-up. | Legal-creak elements stay hidden until after the incoming scene is readable. |
| Scene 2 -> Scene 3 | `16.400-16.620` | Incoming cost desk fades in with small blur/scale settle over the failure scene. | Smooths the move from object failure to true-cost board. | Failure cue overlay ends at `16.300s`, leaving a short visual breath before the cost cue. |
| Cue labels and WIT | cue starts | Short fade/fly-ins, usually `0.18-0.34s`. | Adds life without changing the approved static composition. | Every animated element is set hidden at cue start, then animated in at its intended moment. |
| Red callouts | `11.280s+` | Circle pops in, arrow slides in, labels follow. | Keeps screw evidence readable while adding a small emphasis beat. | Markup remains aligned to the screw in preview. |
| Final tag | `18.850s+` | Fast scale/fade in, stamp and WIT follow. | Lets the payoff land without a big transition. | Final label remains readable through the end frame. |

## Cue Plan Implemented

| Cue | Local Time | Voice Cue | Visual Change | Key Animation | Source |
|---:|---:|---|---|---|---|
| 1 | `0.000-2.200` | `I find a chair for nine dollars.` | Chair base plus `$9` tag and larger WIT. | label, price tag, and WIT enter with short fade/fly-ins | script + WIT manifest |
| 2 | `2.200-5.350` | `four legs... a seat... confidence` | Same chair; labels only, no meaningless red leg marks. | labels stagger in; WIT slides in lightly | script + WIT manifest |
| 3 | `5.350-8.400` | `So he buys it. For the first week... fine.` | Same chair; `SOLD`, hidden future tag, first-week mini calendar, fine label. | stamp pops in; tag/calendar/label enter sequentially | script |
| 4 | `8.400-11.250` | `noise that sounds like legal advice` | Broken-leg close-up with no white overlay; legal-ish creak and suspicious WIT. | scene fade/blur, then legal label, sound lines, note, and WIT enter | script + WIT manifest |
| 5 | `11.250-16.300` | `screw gets loose... one leg begins exploring other career options` | Same broken-leg close-up; circle/arrow aligned to the actual screw and career-options label. | callout pops, arrow slides, labels and WIT enter | script + WIT manifest |
| 6 | `16.400-18.850` | `the cheap chair was not really cheap` | Desk/cost board; true-cost receipt and evidence WIT. | scene fade/blur, then label, receipt, and WIT enter | script + WIT manifest |
| 7 | `18.850-21.205` | `future not included` | Same desk/cost board; final large tag covers the board. | final tag fast fade/scale; stamp and WIT follow | script |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.000` | `chair for nine dollars` | chair + `$9` tag | cue visible | matched |
| `2.200` | `four legs... seat... confidence` | product-detail labels | cue visible on same chair | matched |
| `5.350` | `buys it... first week` | sold/future tag/calendar | cue visible on same chair | matched |
| `8.400` | `legal advice` | `LEGAL-ISH CREAK` | new big scene base | matched |
| `11.250` | `screw... seat... one leg` | screw circle + career-options label | cue visible on same close-up | matched |
| `16.400` | `not really cheap` | true-cost receipt | new big scene base | matched |
| `18.850` | `future not included` | final tag | cue visible on same cost board | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| chair scene | broken-leg scene | `0.22s` incoming fade + small blur/scale settle | smooths the move from normal chair to failure close-up | medium if labels appear before new scene | kept after fixing cue-start hiding |
| broken-leg scene | cost scene | `0.22s` incoming fade + small blur/scale settle | smooths the move from failure evidence to cost board | medium if old failure labels hold into cost cue | kept after shortening failure overlay to end at `16.300s` |
| cue overlays | next cue overlays | no fly-out; cue removal remains timing-driven | prevents old labels from disappearing before the line finishes | low | keep |
| final scene | end | no fade-out | preserves final payoff readability | low | keep |

## Element Motion Notes

- Entrances: small fade/fly-ins only; no large travel, spins, bounces, or repeated transition gimmicks.
- Holds: approved static board positions remain the final layout.
- Emphasis: screw callout uses a quick circle pop and arrow slide; final `FUTURE NOT INCLUDED` uses a short scale/fade.
- Exits: no decorative fly-outs before spoken ideas finish.
- Repeated effects avoided: only two base-scene fade/blur transitions; cue elements use varied but small entrance directions.

## Assets

- Shared asset folder: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal hardlinked working set under `section-previews/section-01-hook/assets/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used: `thinking`, `price-tag-suspicion`, `suspicious`, `betrayed`, `holding-receipt-evidence`
- Review fixes applied: removed meaningless leg marks, removed failure-scene white overlay, enlarged WIT, reduced cue count from `12` to `7`, and aligned the screw circle to the actual screw
- Attribution: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: pass with 2 non-blocking warnings: repeated media reference from reused static assets, and dense cue track
- validate: pass, no console errors, 215 text elements pass WCAG AA
- inspect: pass, 0 layout issues at `1.1,3.8,6.9,9.8,13.4,17.5,20.2`
- preview server: HTTP `200` verified at `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- video export: not requested; MP4 files removed by user request
- animation-map: attempted earlier, but the local plugin helper failed because `@hyperframes/producer` is missing from the plugin cache; standard HyperFrames checks and preview verification should be used instead

## Notes

This revision keeps the approved real-WIT connected-scene render direction, then adds a minimal motion pass. The first animation attempt exposed a label/scene mismatch at the `8.400s` transition; it was fixed by hiding animated cue elements at cue start before animating them in. A later `16.400s` boundary check showed old failure labels too close to the cost beat, so the failure cue overlay now ends at `16.300s` while the voice cue and scene start remain unchanged.

Micro-fix after review: moved the `EVERYTHING IS FINE` blue label from `left: 118px` to `left: 430px` so WIT no longer covers the text around frame `182f` / the settled first-week cue.

Operational correction: MP4 export is no longer part of normal render/review work. Only create MP4/WebM files when the user explicitly asks to export video.
