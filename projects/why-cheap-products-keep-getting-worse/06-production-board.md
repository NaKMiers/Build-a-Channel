# 06 Production Board

Video: `Why Cheap Products Keep Getting Worse`

Status: `section 8 payoff preview ready for review`

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
| Section 4 The Boring Parts Disappear | 1004 | `http://localhost:1004/#project/section-04-the-boring-parts-disappear` | `http://localhost:1004/api/projects/section-04-the-boring-parts-disappear/preview/comp/index.html` | running; HTTP 200 verified |
| Section 8 Payoff | 1008 | `http://localhost:1008/#project/section-08-payoff` | `http://localhost:1008/api/projects/section-08-payoff/preview/comp/index.html` | running; HTTP 200 verified |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | Hook | `review-adjusted reduced-WIT low-motion layout ready for review` | 1001 | `section-previews/section-01-hook/` | `02-script.md` + `04-voiceover.md`; old `05-visual-plan.md` skipped by explicit user request; approved static render kept as layout source; user requested simple TED-Ed-inspired motion at about `1/10` intensity; latest review requested less text animation, voice-matched sequential shows, funnier/larger WIT, no broken WIT crops, and fewer WIT poses per big scene | `lint: pass with 1 non-blocking dense-track warning`; `validate: pass, no console errors, 135 text elements pass WCAG AA`; `inspect: pass at 11 timestamps`; `snapshot: pass via runtime seek contact sheet`; `server: HTTP 200` | `not requested` | `3 persistent big scenes with 7 cue overlays and 4 WIT appearances. Most text now hard-shows on the spoken beat; only emphasis beats such as $9, screw evidence, and final payoff use impact motion. WIT is larger but no longer appears on every cue. MP4 files were deleted by user request; future render work should not export video unless explicitly asked.` |
| 2 | Cheap Is Not The Villain | `review-adjusted giant-WIT preview ready for review` | 1002 | `section-previews/section-02-cheap-is-not-the-villain/` | `02-script.md` + `04-voiceover.md` + revised `05-visual-plan.md` + Section 2 visual plan + render-side quality pass | `lint: pass, 0 warnings`; `validate: pass with 15 non-blocking final-receipt contrast sampler warnings`; `inspect: pass at 12 timestamps`; `snapshot: pass via review-pass-8 contact sheet`; `server: HTTP 200` | `not requested` | `3 persistent big scenes with grouped cue overlays instead of 9 separate cue clips. WIT kept to 4 emotional beats but upgraded to giant Section-1-style facepalm/confused/shocked/money-panic placements. UNFAIR, EXPENSIVE IS NOT MAGIC, and final buy-again elements were repositioned to avoid text/WIT collisions. Subtitle-prone lower elements were also nudged upward for YouTube caption safety.` |
| 3 | The Price Tag Speaks First | `auto-adjusted WIT-dominance preview ready for review` | 1003 | `section-previews/section-03-the-price-tag-speaks-first/` | `02-script.md` + `04-voiceover.md` + revised `05-visual-plan.md` + revised Section 3 visual plan + Auto Adjust pass | `lint: pass with 4 non-blocking warnings`; `validate: pass, no console errors, 30 contrast sampler warnings`; `inspect: pass, 0 layout issues at 12 timestamps`; `snapshot: pass via latest seeked auto-adjust contact sheet`; `server: HTTP 200` | `not requested` | `4 persistent big scenes with 10 cue states. Scene 3 remains a CSS-built checkout promise arena. Auto Adjust reduced WIT to selected emotional beats, removed the duplicate easy-price WIT, scaled remaining WIT by visible alpha/viewport size to roughly 32-36% frame width, moved nearby text away from WIT, and marked intentional lower-body crop as allowed overflow.` |
| 4 | The Boring Parts Disappear | `simple Section-1-style remake preview ready for review` | 1004 | `section-previews/section-04-the-boring-parts-disappear/` | `02-script.md` + `04-voiceover.md` + remade `05-visual-plan.md` + remade Section 4 visual plan after rejecting crowded object-card direction | `lint: pass with 2 non-blocking warnings`; `validate: pass, no console errors, 5 contrast sampler warnings`; `inspect: pass, 0 layout issues at 12 timestamps`; `snapshot: pass via simple-remake contact sheet`; `server: HTTP 200` | `not requested` | `3 persistent real-photo backgrounds with 6 cue states: fabric/stitching, screwdriver repair table, and cardboard/product box. WIT appears only on 3 emotional beats and is sized as a main character: suspicious inspector, printer-repair nerd, betrayed buyer. Phone/printer photos are not used directly; generic CSS overlays replace them.` |
| 8 | Payoff | `preview ready for review` | 1008 | `section-previews/section-08-payoff/` | `02-script.md` + `04-voiceover.md` + `05-visual-plan.md` + Section 8 visual plan | `lint: pass with 2 non-blocking warnings`; `validate: pass, no console errors, 95 text elements pass WCAG AA`; `inspect: pass, 0 layout issues at 9 timestamps`; `thumbnail spot check: pass`; `load check: direct composition HTTP 200 and 5 image assets loaded`; `server: HTTP 200` | `not requested` | `3 persistent payoff scenes with 8 cue states: hidden-future price tag, real-price receipt, and final cardboard/product question. WIT appears only on 3 emotional beats: suspicious evaluator, receipt evidence holder, and deadpan final checker. All receipt/tag wording is rendered in HyperFrames/CSS; no MP4/WebM export was requested or created.` |

## Shared Asset Rules

- Video-level assets: `projects/why-cheap-products-keep-getting-worse/assets/`
- Section asset rule: keep the project asset library as source of truth. Section previews use minimal hardlinked working sets under each `section-previews/<section>/assets/` because this Windows HyperFrames setup previously failed to serve junction-backed section assets during CLI checks.
- Review asset rule: `hyperframes/review/assets/` is a combined minimal hardlinked directory for mirrored review HTML files; it is not a Section 1-only junction.
- Attribution file: `projects/why-cheap-products-keep-getting-worse/assets/ATTRIBUTION.md`

## Active Section Notes

### Section 8

- Section 8 composition id: `Section08Payoff`
- Runtime: `29.141s`
- Voiceover runtime: `29.141s`
- Preview audio: local `section-08-payoff-david23-am_eric-0.84.mp3`
- Screen changes: static hard cuts between three payoff scenes plus phrase-timed hard-show cue layers; no decorative transitions or fly-ins
- Scene grammar: `callback hidden-future price tag -> true-cost receipt -> better final buying question`
- Direct generated support assets: `price-tag-hiding-future-tags-generated.png`, `price-tag-receipt-generated.png`
- Direct real background asset: `real-cardboard-boxes-pexels-harper-sunday.jpg`
- WIT poses used: `wit-pose-price-tag-suspicion.png`, `wit-pose-holding-receipt-evidence.png`, `wit-pose-deadpan-side-eye.png`
- WIT layout decision: WIT appears only on three emotional beats and is scaled as a main character on the right side, with face, glasses, head, shoulders, mouth, and receipt prop kept clear of labels.
- HyperFrames checks: `npm.cmd run check` passed. Lint reported 2 non-blocking warnings: duplicate media discovery risk from repeated WIT image sources and one dense timed cue track. Validate reported no console errors and 95 text elements passing WCAG AA. Inspect reported 0 layout issues across 9 explicit timestamps.
- Inspect timestamps: `0.8`, `3.6`, `7.2`, `10.8`, `13.6`, `18.2`, `22.2`, `26.8`, `28.7`
- Thumbnail spot check: inspected timed HyperFrames thumbnails around the correction beat, receipt evidence beat, and final question beat; text is readable and WIT remains large with face/props clear.
- Load check: local Chrome/Playwright direct composition check found `Section08Payoff` at `1920x1080`, 5 image assets loaded, and no broken images. The saved direct screenshot is a raw load artifact, not a timed contact sheet.
- Review mirror: `hyperframes/review/section-08.html` synced from the current preview source; review assets copied to `hyperframes/review/assets/section-08/`.
- Preview server: port `1008`, Studio and direct composition URLs returned HTTP `200`.
- Export file: `not requested`

### Section 4

- Section 4 composition id: `Section04TheBoringPartsDisappear`
- Runtime: `37.867s`
- Voiceover runtime: `37.867s`
- Preview audio: local `section-04-the-boring-parts-disappear-david23-am_eric-0.84.mp3`
- Screen changes: static hard cuts only; no decorative transitions, fly-ins, or dense card/object tray
- Scene grammar: `boring material future -> repairable/spare-part table and printer joke -> complete outside, less future inside`
- User revision applied: the first Section 4 render direction was rejected as too crowded, with too many scattered text blocks, image cards, and object cutaways. The section was remade from a simplified Section-1-style visual plan.
- Direct real background assets: `real-sewing-machine-stitching-fabric-pexels-shoreline-vehicles.jpg`, `real-screwdriver-bits-pexels-roseson-studios.jpg`, `real-cardboard-boxes-pexels-harper-sunday.jpg`
- Reference-only assets not used directly: `real-rustic-hinge-pexels-brett-sayles.jpg`, `real-phone-battery-repair-pexels-harry-tucker.jpg`, `real-printer-repair-pexels-bulat843.jpg`
- WIT poses used: `wit-pose-suspicious.png`, `wit-pose-thinking.png`, `wit-pose-betrayed.png`
- WIT layout update: WIT appears only on three emotional beats and is scaled to roughly 1/3 to 1/2 frame presence, with the face/expression kept clear of labels.
- HyperFrames checks: `npm.cmd run check` passed. Lint reported 2 non-blocking warnings: duplicate media discovery risk from repeated WIT image sources and one dense timed cue track. Validate reported 5 non-blocking WCAG sampler warnings on a timed material-list label context. Inspect reported 0 layout issues at 12 timestamps.
- Inspect timestamps: `0.5`, `3.3`, `5.6`, `8.3`, `10.4`, `13.8`, `17.8`, `21.6`, `25.5`, `30.5`, `34.8`, `37.2`
- Visual snapshot check: `section-previews/section-04-the-boring-parts-disappear/snapshots/remake-simple-20260612/contact-sheet-simple-remake.png` inspected at `0.8`, `6.0`, `12.0`, `18.6`, `25.4`, `32.4`, and `36.9`; the frame language is now sparse, with 3 big backgrounds, 6 cue states, and large readable WIT placements.
- Review mirror: `hyperframes/review/section-04.html` synced from the current preview source; review background assets copied to `hyperframes/review/assets/section-04/`.
- Preview server: port `1004`, Studio and direct composition URLs returned HTTP `200`.

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
- WIT poses used after Auto Adjust: `wit-pose-price-tag-suspicion.png`, `wit-pose-empty-wallet.png`, `wit-pose-shocked.png`, `wit-pose-deadpan-side-eye.png`, `wit-pose-tiny-defeated.png`
- WIT layout update: Auto Adjust reduced WIT to selected emotional beats, removed WIT from informational list cues plus the duplicate easy-price cue, enlarged remaining WIT by visible alpha/viewport size rather than CSS box size, and used intentional lower-edge crop only where faces, heads, shoulders, mouths, glasses, and props remain readable.
- Auto Adjust preservation: backed up canonical preview to `section-previews/section-03-the-price-tag-speaks-first/manual-saves/auto-adjust-wit-dominance-20260612-151120-index.html`; SHA256 `284B6B85B4C5525FCF92B264684BD83E3F7E1A8460CD5FD2768D5C250A4CF1DE`.
- HyperFrames checks: `npm.cmd run check` passed after Auto Adjust. Lint reported 4 non-blocking warnings: repeated static media discovery risk and dense scene/cue tracks. Validate reported 30 non-blocking WCAG sampler warnings; actual preview frames were inspected for readability. Inspect reported 0 layout issues after intentional WIT lower-body crop was marked with `data-layout-allow-overflow`.
- Inspect timestamps: `0.4`, `2.8`, `5.8`, `8.8`, `11.6`, `15.6`, `18.3`, `22.6`, `25.5`, `28.5`, `31.8`, `33.0`
- Visual snapshot check: `section-previews/section-03-the-price-tag-speaks-first/snapshots/auto-adjust-wit-dominance-20260612-latest/contact-sheet-after.png` inspected from real Studio progress-bar seeks at `0.4`, `2.8`, `5.8`, `8.8`, `11.6`, `15.6`, `18.3`, `22.6`, `25.5`, `28.5`, `31.8`, and `33.0`; WIT no longer reads as a tiny corner sticker, final `TOMORROW` remains clear, and non-WIT promise-list frames breathe.
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
- WIT poses used: `wit-pose-facepalm.png`, `wit-pose-confused.png`, `wit-pose-shocked.png`, `wit-pose-money-panic.png`
- WIT layout update: WIT remains controlled at `4` emotional beats over `22.315s`, but the old small/corner feeling was replaced with giant Section-1-style emotional placements: facepalm for the unfair/emotionally-expensive correction, confused for the jacket joke, shocked for missing tomorrow, and money-panic for buying the same thing again. Head, shoulders, face, and key props were checked in the runtime-seek contact sheet; intentional crop is limited to lower body / edge peeking, not face.
- Render-side quality pass: grouped the old separate cue clips into `3` big-scene overlays, changed the opening anchor to `CHEAP IS NOT BAD`, cleared the `BAD?` red X before `UNFAIR`, removed a decorative crack after it covered `LESS STRENGTH`, moved `UNFAIR` away from `EMOTIONALLY EXPENSIVE`, moved `EXPENSIVE IS NOT MAGIC` out from under the jacket, shifted the final receipt/box left, raised lower-third labels/receipt-loop props into a subtitle-safe zone, and kept red markup tied to exact objects.
- HyperFrames checks: `npm.cmd run check` passed. Lint reported `0` warnings. Validate reported `15` non-blocking contrast sampler warnings from the small final receipt text. Inspect reported `0` layout issues.
- Inspect timestamps: `0.4`, `2.8`, `5.0`, `6.6`, `8.8`, `11.4`, `14.4`, `16.7`, `17.8`, `18.9`, `20.8`, `22.0`
- Snapshot QA: `section-previews/section-02-cheap-is-not-the-villain/snapshots/review-pass-8/contact-sheet.jpg` inspected at `0.4`, `2.9`, `6.6`, `8.8`, `11.4`, `14.4`, `16.7`, `17.8`, `18.9`, `20.8`, and `22.0`.
- Manual Studio preservation: Anh Khoa manually adjusted Section 2 on localhost/Studio after the giant-WIT pass. Current `section-previews/section-02-cheap-is-not-the-villain/index.html` is canonical for future updates.
- Latest manual save snapshot: `section-previews/section-02-cheap-is-not-the-villain/manual-saves/save-110159.html`; hash `0BFC3AD707F709F145A6DB919AC6BCBCFC75ADC7C9D329277AFEC63BE9F6DD14`.
- Previous manual save snapshot: `section-previews/section-02-cheap-is-not-the-villain/manual-saves/save-105019.html`.
- Future Section 2 update rule: read and diff the current preview `index.html` before editing, preserve manual/Studio positioning attributes, do not regenerate from the visual plan or older review mirror, and sync `hyperframes/review/section-02.html` only from the preview source.
- Subtitle-safe adjustment: `CHEAP IS NOT BAD`, `NICE JACKET`, and the final `AGAIN` receipt/loop cluster were moved upward slightly so typical YouTube subtitles are less likely to cover them near the bottom edge.
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

- Section 4 visual plan and preview were remade after user feedback that the previous direction was chaotic, text-heavy, and image-heavy. The current canonical Section 4 source is `section-previews/section-04-the-boring-parts-disappear/index.html`; do not regenerate from the rejected crowded object-card / parts-tray direction.
- No Section 4 MP4/WebM export was requested or created.
- No Section 4 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final assembly output was found during this run.
- Section 2 preview was manually adjusted by the user after the giant-WIT pass and saved as the current canonical preview for review. The matching review mirror `hyperframes/review/section-02.html` was synced from the preview source. No Section 2 MP4/WebM export was requested or created.
- Section 3 preview was revised after user feedback; Scene 3 is rebuilt as a CSS checkout promise arena and the previous generated visible-promises photo is now reference-only.
- No Section 3 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final render outputs were found during this run.
- Section 1 preview was revised after user feedback on animation density, sequential reveal timing, WIT emotional placement, WIT scale, broken WIT crops, and WIT overuse. MP4 outputs were removed by user request and should not be recreated unless the user explicitly asks for video export.
- No Section 1 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final assembly output was found during this run.
- No Section 8 MP4/WebM export was requested or created.
- No Section 8 `07-review.md`, `08-upload.md`, `09-self-learning.md`, unified preview, or final assembly output was found during this run.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
