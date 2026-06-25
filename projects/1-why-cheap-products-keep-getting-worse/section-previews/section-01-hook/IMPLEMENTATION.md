# Section 1 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 1: Hook`

Status:
`review-adjusted reduced-WIT low-motion layout ready for review`

## Result

- Preview project: `projects/1-why-cheap-products-keep-getting-worse/section-previews/section-01-hook/`
- Source: `02-script.md` + `04-voiceover.md` + real WIT manifest + user reviews on connected big-scene pacing, fewer cues, meaningful markup, larger WIT, exact callout alignment, sequential voice-matched reveals, reduced text-animation density, exaggerated/funnier WIT placement, and reduced WIT-pose density
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `21.205s`
- Voiceover: `section-01-hook-david23-am_eric-0.84.mp3`
- Visual plan: old visual plan explicitly skipped by user request; current revision follows the user-reviewed big-scene/small-cue mechanism with reduced cue count
- Export file: `not requested`
- MP4 files removed: `section-01-hook-animated.mp4` and `section-01-hook-remake.mp4` were deleted by user request
- Preview QA rule: use Studio/direct preview screenshots for normal render fixes; do not export MP4 unless the user explicitly asks
- Manual Studio preservation: user made direct localhost/Studio edits after this pass. Treat `section-previews/section-01-hook/index.html` as the canonical source before any future Section 1 update; never restore from an older visual plan or `hyperframes/review/section-01.html` without first diffing against this file.
- Manual element removals: the current preview intentionally omits several prior cue-plan support elements after Studio edits, including the product/failure tiny notes, `SOLD` stamp, `FUTURE NOT INCLUDED` dangle in the sold-week cue, `ONE LEG` label, and true-cost receipt. Do not re-add them unless the user asks.

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
| Cue labels and WIT | cue starts plus phrase offsets | Most text hard-shows at the spoken beat with no fly-in. WIT appears only on selected emotional beats. Only emphasized beats keep impact motion. | Reduces visual noise while preserving voice-matched sequential reveals. | Every delayed element is set hidden at cue start, then shown or smashed in at its intended moment. |
| Red callouts | `11.280s+` | Circle pops in, arrow slides in, labels follow. | Keeps screw evidence readable while adding a small emphasis beat. | Markup remains aligned to the screw in preview. |
| Final tag | `18.850s+` | Stamp and WIT hard-show, then final tag uses a short smash-in. | Lets the payoff land on `future not included` without animating every block. | Final label remains readable through the end frame and WIT face is not edge-cropped. |

## Cue Plan Implemented

| Cue | Local Time | Voice Cue | Visual Change | Key Animation | Source |
|---:|---:|---|---|---|---|
| 1 | `0.000-2.200` | `I find a chair for nine dollars.` | Chair base, giant thinker WIT peeking from lower left, then `$9` tag. | chair label hard-shows at `0.12s`, WIT hard-shows at `0.42s`, `$9` tag smash-in at `1.08s` | script + WIT manifest |
| 2 | `2.200-5.350` | `four legs... a seat... confidence` | Same chair; product detail labels only, no meaningless red leg marks, no WIT so the scene can breathe after the opening reaction. | `4 LEGS + 1 SEAT` at `2.36s`, confidence label at `3.42s`, note at `4.14s`, all hard-show | script |
| 3 | `5.350-8.400` | `So he buys it. For the first week... fine.` | Same chair; buy label, first-week mini calendar, fine label, awkward-celebration WIT half-enters from the right. | buy label, calendar, WIT, and fine label hard-show on their spoken beats | script |
| 4 | `8.400-11.250` | `noise that sounds like legal advice` | Broken-leg close-up with no white overlay; sound lines, legal-ish creak, and note reveal in phrase order. WIT is held for the later failure beat. | sound lines at `8.92s`, legal label at `9.72s`, note at `10.02s`, all hard-show | script |
| 5 | `11.250-16.300` | `screw gets loose... one leg begins exploring other career options` | Same broken-leg close-up; circle/arrow aligned to the actual screw and career-options label; hidden-fee-panic WIT pops up large from lower left. | screw mark keeps small pop/slide; screw label, one-leg label, WIT, and career label hard-show by phrase | script + WIT manifest |
| 6 | `16.400-18.850` | `the cheap chair was not really cheap` | Desk/cost board; not-cheap label only. WIT is held for the final payoff. | not-cheap label at `17.34s`, hard-show | script |
| 7 | `18.850-21.205` | `future not included` | Same desk/cost board; small-problem stamp, large money-panic WIT behind the final tag, final `FUTURE NOT INCLUDED` smash. | stamp at `19.10s`, WIT at `19.28s`, final tag smash-in at `19.86s` | script |

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `1.080` | `nine dollars` | `$9` tag | tag reveal | matched |
| `2.360` | `four legs... a seat` | `4 LEGS + 1 SEAT` | label reveal | matched |
| `3.420` | `confidence` | confidence label | label reveal | matched |
| `5.700` | `buys it` | `HE BUYS IT` | label reveal | matched |
| `6.720` | `first week` | mini calendar | calendar reveal | matched |
| `7.220` | `everything is fine` | fine label | label reveal | matched |
| `9.720` | `legal advice` | `LEGAL-ISH CREAK` | label reveal after scene/sound setup | matched |
| `11.420` | `screw gets loose` | screw circle + arrow + screw label | evidence reveal | matched |
| `13.020` | `one leg` | one-leg and career labels | label reveal sequence | matched |
| `17.340` | `not really cheap` | not-cheap label | label reveal | matched |
| `19.860` | `future not included` | final tag | payoff reveal | matched |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| chair scene | broken-leg scene | `0.22s` incoming fade + small blur/scale settle | smooths the move from normal chair to failure close-up | medium if labels appear before new scene | kept after fixing cue-start hiding |
| broken-leg scene | cost scene | `0.22s` incoming fade + small blur/scale settle | smooths the move from failure evidence to cost board | medium if old failure labels hold into cost cue | kept after shortening failure overlay to end at `16.300s` |
| cue overlays | next cue overlays | no fly-out; cue removal remains timing-driven | prevents old labels from disappearing before the line finishes | low | keep |
| final scene | end | no fade-out | preserves final payoff readability | low | keep |

## Element Motion Notes

- Entrances: most blocks hard-show exactly on cue; no repeated fly-ins, large travel, spins, bounces, or decorative motion.
- Holds: approved static board positions remain the final layout.
- Emphasis: `$9`, screw callout, and final `FUTURE NOT INCLUDED` use short impact motion; ordinary supporting labels simply appear.
- Exits: no decorative fly-outs before spoken ideas finish.
- Repeated effects avoided: only two base-scene fade/blur transitions; normal cue elements now mostly hard-show rather than animating.
- WIT placement: WIT now uses fewer oversized emotional reads instead of appearing on every cue: giant lower-left thinker, right-side awkward celebration, lower-left hidden-fee panic, and final money-panic behind-tag framing.
- WIT density: `4` WIT appearances over `21.205s`; big scene 1 uses `2` WIT beats, big scene 2 uses `1`, and big scene 3 uses `1`.
- Crop guard: WIT heads/faces are kept inside the frame or intentionally behind a foreground label; no frame shows a broken head/shoulder crop.

## Assets

- Shared asset folder: `projects/1-why-cheap-products-keep-getting-worse/assets/`
- Section assets: minimal hardlinked working set under `section-previews/section-01-hook/assets/`
- WIT source: `assets/wit/manifest.json`
- WIT poses used: `thinking`, `awkward-celebration`, `hidden-fee-panic`, `money-panic`
- Review fixes applied: removed meaningless leg marks, removed failure-scene white overlay, enlarged WIT, reduced cue count from `12` to `7`, and aligned the screw circle to the actual screw
- Attribution: `projects/1-why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Verification

- lint: pass with 1 non-blocking warning: dense cue track
- validate: pass, no console errors, 135 text elements pass WCAG AA
- inspect: pass, 0 layout issues at `0.7,1.35,2.65,3.85,6.15,7.45,9.95,11.9,13.9,17.55,20.05`
- preview snapshot QA: `review-snapshots/section-01-review-contact-sheet.png` created from runtime `window.__player.seek(...)` screenshots on `localhost:1001`
- preview server: HTTP `200` verified at `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- video export: not requested; MP4 files removed by user request
- animation-map: attempted earlier, but the local plugin helper failed because `@hyperframes/producer` is missing from the plugin cache; standard HyperFrames checks and preview verification should be used instead

## Notes

This revision keeps the approved real-WIT connected-scene render direction, then adds a minimal motion pass. The first animation attempt exposed a label/scene mismatch at the `8.400s` transition; it was fixed by hiding animated cue elements at cue start before animating them in. A later `16.400s` boundary check showed old failure labels too close to the cost beat, so the failure cue overlay now ends at `16.300s` while the voice cue and scene start remain unchanged.

Micro-fix after review: moved the `EVERYTHING IS FINE` blue label from `left: 118px` to `left: 430px` so WIT no longer covers the text around frame `182f` / the settled first-week cue.

Operational correction: MP4 export is no longer part of normal render/review work. Only create MP4/WebM files when the user explicitly asks to export video.

Review update after user feedback: reduced animation density so most labels now hard-show at the spoken beat. Impact animation is reserved for `$9`, the screw callout, and the final `FUTURE NOT INCLUDED` payoff. WIT is now treated as emotional punctuation rather than a reaction on every cue: only `4` WIT beats remain across `3` big scenes. No new WIT pose generation was needed because the existing shared WIT set covered the required expressions.

Manual Studio preservation update: an accidental `vfx-liquid-glass` registry composition added `20s` of dead duration; it was removed and root composition duration was restored to `21.205s`, matching the voiceover. The remaining current `index.html` changes are preserved as the user's manual Studio-adjusted source of truth.

Manual cleanup after validation: removed dead GSAP calls targeting elements that were intentionally removed in Studio, so validation no longer warns about missing targets. No visible layout was restored or overwritten.

Final-scene overlap fix: moved the final `FUTURE NOT INCLUDED` tag to the left and reduced it slightly, moved the `SMALL PROBLEM` stamp to the lower-left, and shifted `money-panic` WIT farther right. The goal is to keep the payoff text readable without covering WIT's face/expression in the final beat.
