# 06 Production Board

Video: `Why Cheap Products Keep Getting Worse`

Status: `section 1 minimal animation pass rendered for review`

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
| 1 | Hook | `minimal animation pass preview ready for review` | 1001 | `section-previews/section-01-hook/` | `02-script.md` + `04-voiceover.md`; old `05-visual-plan.md` skipped by explicit user request; approved static render kept as layout source; user requested simple TED-Ed-inspired motion at about `1/10` intensity | `lint: pass with 2 non-blocking warnings`; `validate: pass`; `inspect: pass`; `server: HTTP 200` | `not requested` | `3 persistent big scenes with 7 voice-timed cue overlays. Added only two incoming scene fade/blur transitions and short element fade/fly-ins. Cue-start hiding prevents delayed animation labels from appearing early. MP4 files were deleted by user request; future render work should not export video unless explicitly asked.` |
| 2 | Cheap Is Not The Villain | `revised generated-base preview running for review` | 1002 | `section-previews/section-02-cheap-is-not-the-villain/` | `02-script.md` + `04-voiceover.md` + revised `05-visual-plan.md` + Section 2 visual plan | `lint: pass with 2 non-blocking warnings`; `validate: pass, no console errors, 225 text elements pass WCAG AA`; `inspect: pass at 12 timestamps`; `server: HTTP 200` | `not requested` | `3 persistent big scenes with 9 cue states. Uses real tag texture, generated two-box comparison base, generated missing-tomorrow cutaway base, rebuilt jacket overlay, and real project WIT PNG poses only.` |
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
- Screen changes: static hard cuts only; no transitions or decorative element entrance animations
- Scene grammar: `wrong-villain correction board -> fair generated two-box comparison with jacket joke -> generated missing-tomorrow cutaway with less-list slot changes`
- Direct real assets: `real-blank-tag-pexels-padrinan.jpg`
- Direct generated support assets: `fair-comparison-two-boxes-generated.png`, `missing-tomorrow-cutaway-generated.png`
- Mockup/reference-only assets not used directly: `real-receipt-pexels-towfiqu-barbhuiya.jpg`, `real-black-jacket-hanger-pexels-mishchenko.jpg`, `real-plain-white-boxes-pexels-dalprat.jpg`
- WIT poses used: `wit-pose-price-tag-suspicion.png`, `wit-pose-empty-wallet.png`, `wit-pose-pointing-right.png`, `wit-pose-deadpan-side-eye.png`, `wit-pose-thinking.png`, `wit-pose-suspicious.png`, `wit-pose-tiny-defeated.png`
- HyperFrames checks: `npm.cmd run check` passed. Lint reported only 2 non-blocking warnings: repeated static media discovery risk and dense cue track.
- Inspect timestamps: `0.4`, `2.8`, `5.0`, `6.6`, `8.8`, `11.4`, `14.4`, `16.7`, `17.8`, `18.9`, `20.8`, `22.0`
- Visual thumbnail check: latest generated-base thumbnails inspected at the comparison, cutaway, and support beats.
- Preview server: port `1002`, direct composition URL returned HTTP `200`

### Section 1

- Section 1 composition id: `Section01Hook`
- Runtime: `21.205s` composition
- Voiceover runtime: `21.205s`
- Screen changes: approved connected static boards plus minimal animation pass
- Preview audio: local `section-01-hook-david23-am_eric-0.84.mp3` served through the HyperFrames preview project
- Scene grammar: `chair setup evolves through product details, purchase, and first week -> broken-leg close-up evolves through legal creak and screw/career-options failure -> cost board evolves through true-cost receipt and final future-not-included payoff`
- Motion grammar: `incoming scene fade/blur settle at 8.400s and 16.400s -> short cue element fade/fly-ins -> no decorative fly-outs before spoken ideas finish`
- Sync guard: animated elements are explicitly hidden at cue start before their entrance tween, so delayed entries cannot appear over the wrong scene or voice beat
- Boundary fix: the failure overlay now ends at `16.300s`, leaving a small visual breath before the `not really cheap` cost cue begins at `16.400s`
- Real direct-use assets: `real-blank-tag-pexels-padrinan.jpg`, `real-receipt-pexels-towfiqu-barbhuiya.jpg`
- Generated support assets: `chair-price-tag`, `hidden-future-tag`, `wobbly-leg-loose-screw`, `price-tag-receipt`
- WIT poses used: `wit-pose-thinking.png`, `wit-pose-price-tag-suspicion.png`, `wit-pose-suspicious.png`, `wit-pose-betrayed.png`, `wit-pose-holding-receipt-evidence.png`
- Export file: `not requested`
- MP4 files removed: `renders/section-01-hook/section-01-hook-animated.mp4` and `renders/section-01-hook/section-01-hook-remake.mp4` were deleted by user request
- Preview QA rule: use Studio/direct preview screenshots for normal render fixes; do not export MP4 unless the user explicitly asks
- User review applied: avoid many unrelated full-scene cuts in a short section; build connected big scenes, then change one or two cue elements inside the big scene while the narration advances
- Latest review applied: removed meaningless red leg marks, removed the white wash overlay from the failure photo, enlarged WIT, reduced cue states from `12` to `7`, and corrected the screw callout to circle the actual screw.
- Animation review applied: first motion attempt showed a label/scene mismatch at the `8.400s` transition; fixed by cue-start hiding.
- Frame-specific fix: moved the `EVERYTHING IS FINE` label right so WIT no longer covers it around frame `182f` / the settled first-week cue.

## Stale / Regeneration Notes

- Section 3 preview was revised after user feedback; Scene 3 is rebuilt as a CSS checkout promise arena and the previous generated visible-promises photo is now reference-only.
- No Section 3 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final render outputs were found during this run.
- Section 1 preview was regenerated for the minimal animation pass. MP4 outputs were removed by user request and should not be recreated unless the user explicitly asks for video export.
- No Section 1 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final assembly output was found during this run.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
