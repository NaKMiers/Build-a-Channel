# 06 Production Board

Video: `Why Cheap Products Keep Getting Worse`

Status: `section 2 review-adjusted collision-safe preview ready for review`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 |  |  | reserved |
| Section 1 Hook | 1001 | `http://localhost:1001/#project/section-01-hook` | `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html` | running; preview HTTP 200 verified |
| Section 2 Cheap Is Not The Villain | 1002 | `http://localhost:1002/#project/section-02-cheap-is-not-the-villain` | `http://localhost:1002/api/projects/section-02-cheap-is-not-the-villain/preview/comp/index.html` | running; HTTP 200 verified |
| Section 3 The Price Tag Speaks First | 1003 | `http://localhost:1003/#project/section-03-the-price-tag-speaks-first` | `http://localhost:1003/api/projects/section-03-the-price-tag-speaks-first/preview/comp/index.html` | running; HTTP 200 verified |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook | `review-adjusted reduced-WIT low-motion layout ready for review` | 1001 | `section-previews/section-01-hook/` | `02-script.md` + `04-voiceover.md`; old `05-visual-plan.md` skipped by explicit user request; approved static render kept as layout source; user requested simple TED-Ed-inspired motion at about `1/10` intensity; latest review requested less text animation, voice-matched sequential shows, funnier/larger WIT, no broken WIT crops, and fewer WIT poses per big scene | `lint: pass with 1 non-blocking dense-track warning`; `validate: pass, no console errors, 135 text elements pass WCAG AA`; `inspect: pass at 11 timestamps`; `snapshot: pass via runtime seek contact sheet`; `server: HTTP 200` | `not requested` | `3 persistent big scenes with 7 cue overlays and 4 WIT appearances. Most text now hard-shows on the spoken beat; only emphasis beats such as $9, screw evidence, and final payoff use impact motion. WIT is larger but no longer appears on every cue. MP4 files were deleted by user request; future render work should not export video unless explicitly asked.` |
| 2 | Cheap Is Not The Villain | `review-adjusted collision-safe preview ready for review` | 1002 | `section-previews/section-02-cheap-is-not-the-villain/` | `02-script.md` + `04-voiceover.md` + revised `05-visual-plan.md` + Section 2 visual plan + render-side quality pass | `lint: pass, 0 warnings`; `validate: pass with 10 non-blocking final-receipt contrast sampler warnings`; `inspect: pass at 12 timestamps`; `snapshot: pass via review-pass-4 contact sheet`; `server: HTTP 200` | `not requested` | `3 persistent big scenes with grouped cue overlays instead of 9 separate cue clips. WIT reduced to 4 emotional beats. Opening anchor changed to CHEAP IS NOT BAD. Decorative crack removed after snapshot QA. UNFAIR and EXPENSIVE IS NOT MAGIC were moved to prevent label collisions.` |
| 3 | The Price Tag Speaks First | `scene 3 revised preview running for review` | 1003 | `section-previews/section-03-the-price-tag-speaks-first/` | `02-script.md` + `04-voiceover.md` + revised `05-visual-plan.md` + revised Section 3 visual plan | `lint: pass with 4 non-blocking warnings`; `validate: pass, no console errors, 30 contrast sampler warnings`; `inspect: pass at 12 timestamps`; `snapshot: pass at 18.3, 22.6, 25.5`; `server: HTTP 200` | `not requested` | `4 persistent big scenes with 10 cue states. Scenes 1, 2, and 4 use the generated hidden-future-tag base. Scene 3 is now a CSS-built checkout promise arena, not the generated visible-promises photo. Uses real project WIT PNG poses and hard cuts only.` |

## Shared Asset Rules

- Video-level assets: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section asset rule: keep the project asset library as source of truth. Section previews use minimal hardlinked working sets under each `section-previews/<section>/assets/` because this Windows HyperFrames setup previously failed to serve junction-backed section assets during CLI checks.
- Review asset rule: `hyperframes/review/assets/` is a combined minimal hardlinked directory for mirrored review HTML files; it is not a Section 1-only junction.
- Attribution file: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Active Section Notes

### Section 3

- Section 3 composition id: `Section03ThePriceTagSpeaksFirst`
- Runtime: `33.429s`
- Voiceover runtime: `33.429s`
- Preview audio: local `section-03-the-price-tag-speaks-first-david23-am_eric-0.84.mp3`
- Screen changes: static hard cuts only; no transitions or decorative element entrance animations
- Scene grammar: `loud visible price tag -> quiet future-cost witness -> checkout promise arena -> hidden tomorrow tags`
- User revision applied: Scene 3 was rebuilt because the generated visible-promises base looked too similar to Scene 1's tabletop/tag visual language.
- Direct generated support assets: `price-tag-hiding-future-tags-generated.png`
- Reference-only generated support assets: `visible-shopping-promises-generated.png`, inspected and intentionally skipped for direct use in the revised Scene 3
- Reference-only real assets: `real-blank-tag-pexels-padrinan.jpg`, `real-receipt-pexels-towfiqu-barbhuiya.jpg`, `real-plain-white-boxes-pexels-dalprat.jpg`
- WIT poses used: `wit-pose-price-tag-suspicion.png`, `wit-pose-empty-wallet.png`, `wit-pose-confused.png`, `wit-pose-shocked.png`, `wit-pose-deadpan-side-eye.png`, `wit-pose-pointing-right.png`, `wit-pose-tiny-defeated.png`
- HyperFrames checks: `npm.cmd run check` passed. Lint reported 4 non-blocking warnings: repeated static media discovery risk and dense scene/cue tracks. Validate reported 30 non-blocking WCAG sampler warnings; risky label styles were tightened and actual preview frames were inspected for readability. Inspect reported 0 layout issues.
- Inspect timestamps: `0.4`, `2.8`, `5.8`, `8.8`, `11.6`, `15.6`, `18.3`, `22.6`, `25.5`, `28.5`, `31.8`, `33.0`
- Visual snapshot check: `section-previews/section-03-the-price-tag-speaks-first/snapshots/contact-sheet.jpg` inspected at `18.3`, `22.6`, and `25.5`; the checkout promise arena reads distinctly from the opening hidden-tag tabletop.
- Preview server: port `1003`, direct composition URL returned HTTP `200`

### Section 2

- Section 2 composition id: `Section02CheapIsNotTheVillain`
- Runtime: `22.315s`
- Voiceover runtime: `22.315s`
- Preview audio: local `section-02-cheap-is-not-the-villain-david23-am_eric-0.84.mp3`
- Screen changes: static hard cuts between big scenes plus phrase-timed hard-shows inside each big scene; no decorative transitions or repeated pop/fly-ins
- Scene grammar: `wrong-villain correction board -> fair generated two-box comparison with jacket joke -> generated missing-tomorrow autopsy with less-list slot changes and buy-again consequence`
- Direct real assets: `real-blank-tag-pexels-padrinan.jpg`
- Direct generated support assets: `fair-comparison-two-boxes-generated.png`, `missing-tomorrow-cutaway-generated.png`
- Mockup/reference-only assets not used directly: `real-receipt-pexels-towfiqu-barbhuiya.jpg`, `real-black-jacket-hanger-pexels-mishchenko.jpg`, `real-plain-white-boxes-pexels-dalprat.jpg`
- WIT poses used: `wit-pose-price-tag-suspicion.png`, `wit-pose-deadpan-side-eye.png`, `wit-pose-suspicious.png`, `wit-pose-tiny-defeated.png`
- WIT layout update: WIT reduced from the old plan's near-every-cue usage to `4` emotional beats over `22.315s`: fairness suspicion, jacket judgment, missing-tomorrow suspicion, and repeat-buyer defeat. WIT face/expression and text-over-WIT collisions were checked in the runtime-seek contact sheet.
- Render-side quality pass: grouped the old separate cue clips into `3` big-scene overlays, changed the opening anchor to `CHEAP IS NOT BAD`, cleared the `BAD?` red X before `UNFAIR`, removed a decorative crack after it covered `LESS STRENGTH`, moved `UNFAIR` away from `EMOTIONALLY EXPENSIVE`, moved `EXPENSIVE IS NOT MAGIC` out from under the jacket, and kept red markup tied to exact objects.
- HyperFrames checks: `npm.cmd run check` passed. Lint reported `0` warnings. Validate reported `10` non-blocking contrast sampler warnings from the small final receipt text. Inspect reported `0` layout issues.
- Inspect timestamps: `0.4`, `2.8`, `5.0`, `6.6`, `8.8`, `11.4`, `14.4`, `16.7`, `17.8`, `18.9`, `20.8`, `22.0`
- Snapshot QA: `section-previews/section-02-cheap-is-not-the-villain/snapshots/review-pass-4/contact-sheet.jpg` inspected at `0.4`, `2.9`, `6.6`, `8.8`, `11.4`, `14.4`, `16.7`, `17.8`, `18.9`, `20.8`, and `22.0`.
- Preview server: port `1002`, direct composition URL returned HTTP `200`

### Section 1

- Section 1 composition id: `Section01Hook`
- Runtime: `21.205s` composition
- Voiceover runtime: `21.205s`
- Screen changes: approved connected static boards plus review-adjusted low-motion reduced-WIT pass
- Preview audio: local `section-01-hook-david23-am_eric-0.84.mp3` served through the HyperFrames preview project
- Scene grammar: `chair setup evolves through product details, purchase, and first week -> broken-leg close-up evolves through legal creak and screw/career-options failure -> cost board evolves through true-cost receipt and final future-not-included payoff`
- Motion grammar: `incoming scene fade/blur settle at 8.400s and 16.400s -> phrase-timed hard-show for most cue elements -> impact motion only on emphasized beats`
- Sync guard: delayed elements are explicitly hidden at cue start before their show/smash beat
- Boundary fix: the failure overlay now ends at `16.300s`, leaving a small visual breath before the `not really cheap` cost cue begins at `16.400s`
- Real direct-use assets: `real-blank-tag-pexels-padrinan.jpg`, `real-receipt-pexels-towfiqu-barbhuiya.jpg`
- Generated support assets: `chair-price-tag`, `hidden-future-tag`, `wobbly-leg-loose-screw`, `price-tag-receipt`
- WIT poses used: `wit-pose-thinking.png`, `wit-pose-awkward-celebration.png`, `wit-pose-hidden-fee-panic.png`, `wit-pose-money-panic.png`
- WIT layout update: WIT reduced to `4` emotional beats over `21.205s`: giant lower-left thinker, right-side awkward celebration, lower-left hidden-fee panic, and final money-panic behind-tag framing. Big scene 1 uses `2` WIT beats, big scene 2 uses `1`, and big scene 3 uses `1`. WIT heads/faces were checked in runtime screenshots to avoid broken crops.
- Export file: `not requested`
- MP4 files removed: `renders/section-01-hook/section-01-hook-animated.mp4` and `renders/section-01-hook/section-01-hook-remake.mp4` were deleted by user request
- Preview QA rule: use Studio/direct preview screenshots for normal render fixes; do not export MP4 unless the user explicitly asks
- Manual Studio preservation: user made direct localhost/Studio edits after the reduced-WIT pass. Future Section 1 updates must read and preserve `section-previews/section-01-hook/index.html` as canonical before changing anything; do not copy the older review mirror or visual-plan output over it.
- Manual element removals preserved: current preview omits prior support items such as product/failure tiny notes, `SOLD`, sold-week dangling future tag, `ONE LEG`, and the true-cost receipt. These should not be reintroduced from older docs unless requested.
- User review applied: avoid many unrelated full-scene cuts in a short section; build connected big scenes, then change one or two cue elements inside the big scene while the narration advances
- Latest review applied: removed meaningless red leg marks, removed the white wash overlay from the failure photo, enlarged WIT, reduced cue states from `12` to `7`, and corrected the screw callout to circle the actual screw.
- Animation review applied: first motion attempt showed a label/scene mismatch at the `8.400s` transition; fixed by cue-start hiding.
- Frame-specific fix: moved the `EVERYTHING IS FINE` label right so WIT no longer covers it around frame `182f` / the settled first-week cue.
- Latest review applied: most text blocks now hard-show on their spoken beat to reduce animation density. `$9`, screw evidence, and final payoff keep impact motion for emphasis. WIT was reduced from every cue to selected emotional beats so the section breathes with the voice rhythm.
- Accidental VFX cleanup: removed the unreferenced `vfx-liquid-glass` registry composition and restored Section 1 root duration from `41.21s` to `21.205s`, matching the voiceover.
- Validation cleanup: removed dead GSAP timeline calls for Studio-removed elements; this preserves the current visual layout while preventing missing-target warnings.
- Final-scene overlap fix: the final tag and `SMALL PROBLEM` stamp were repositioned left while money-panic WIT was shifted right, so text no longer covers WIT's final expression.
- Preview snapshot QA: `section-previews/section-01-hook/review-snapshots/section-01-review-contact-sheet.png` was created from direct preview screenshots at `0.7`, `1.35`, `2.65`, `3.85`, `6.15`, `7.45`, `9.95`, `11.9`, `13.9`, `17.55`, and `20.05`.

## Stale / Regeneration Notes

- Section 2 preview was revised after the render skill update and is now the current canonical preview for review. The matching review mirror `hyperframes/review/section-02.html` was synced from the preview source. No Section 2 MP4/WebM export was requested or created.
- Section 3 preview was revised after user feedback; Scene 3 is rebuilt as a CSS checkout promise arena and the previous generated visible-promises photo is now reference-only.
- No Section 3 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final render outputs were found during this run.
- Section 1 preview was revised after user feedback on animation density, sequential reveal timing, WIT emotional placement, WIT scale, broken WIT crops, and WIT overuse. MP4 outputs were removed by user request and should not be recreated unless the user explicitly asks for video export.
- No Section 1 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final assembly output was found during this run.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
