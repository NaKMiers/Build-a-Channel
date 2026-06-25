# Section 6 Render Implementation

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 6: Repair Gets A Security System`

Status:
`auto-adjusted 2026-06-21 (voice-synced re-time + gray-overlay removal) - live on port 1006, ready for review`

## Result

- Preview project: `section-previews/section-06-repair-gets-a-security-system/`
- Source: restored 1:1 from the surviving approved build `hyperframes/review/section-06.html` (the section-preview working folder and `06-production-board.md` were missing; the review mirror and saved references survived)
- Port: `1006`
- Studio URL: `http://localhost:1006`
- Direct composition URL: `http://localhost:1006/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Project id note: the HyperFrames preview server resolves this port's project id/title as `Build a Channel` (workspace/git root name); `dir` correctly points to the Section 6 folder, and this port serves only Section 6.
- Runtime: `42.816s` (`data-duration` matches the section voiceover)
- Voiceover: `section-06-repair-gets-a-security-system-david23-am_eric-0.84.mp3` (David23 / am_eric / 0.84 / en-us)
- Visual plan: `visual-plan/section-06-repair-gets-a-security-system/section-06-repair-gets-a-security-system-visual-plan.md`

## Big Scene / Cue Plan Implemented

All cue starts below are pinned to the faster-whisper word timings in `voiceover/section-06-.../section-06-word-timings.json` (auto-adjusted 2026-06-21).

| Cue | Local Time | Voice Cue (word-timing start) | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| 1 | `0-3.0` | `The third reason is repair.` (0.34) | 1 Repair Checkpoint (`0-9.86`) | Title over repair-bench photo | hard-show + scene in | `suspicious` giant lower-left `width 1120px`, legs cropped, face safe | `REPAIR CHECKPOINT`; `third reason` | ok |
| 2 | `3.0-5.3` | `...harder than replacing it.` (1.6; "harder" 3.82) | 1 | `BUY NEW` shortcut lane + red `HARDER THAN REPLACING` | hard-show | held `suspicious` | `BUY NEW`; red `HARDER THAN REPLACING` | ok |
| 3 | `5.3-9.85` | `part (5.28) / tool (6.94) / manual (8.3)` | 1 | 3 security trays appear one per spoken barrier (tracks 3/4/5) | hard-show | held `suspicious` | `NO PART`; `SPECIAL TOOL`; `NO MANUAL` | ok |
| 4 | `9.86-12.64` | `costs almost as much as buying a new one` (9.86) | 2a Cost (`scene-cost` `9.86-12.64`, paper bg) | Repair bill (9.86) → `ALMOST NEW PRICE` stamp (10.94) → `NEW ONE` box (11.8), staggered to the words | hard-show staggered; stamp impact | none | `REPAIR BILL`/`repair cost`/`NEW ONE`; red stamp `ALMOST NEW PRICE` | ok (snapshot 10.5/11.3/12.3) |
| 5 | `12.64-17.98` | `And sometimes the product looks at you... Very healthy relationship.` (12.64; quote 14.46; note 16.22) | 2b Ownership Lock (`scene-ownership-lock` `12.64-17.98`, real padlock photo bg) | Padlock photo + trapped WIT show at 12.64; quote reveals 14.46; relationship note reveals 16.2 | hard-show + staggered reveals | `trapped-by-app-screen` giant lower-right behind glass `width 1460px` | quote `YOU OWN ME... NOT ENOUGH TO OPEN ME`; red `VERY HEALTHY RELATIONSHIP` | ok (snapshot 13.5/15/16.5) |
| 6 | `17.98-22.86` | `This is why repairability matters... how easy something is to fix` (17.98) | 3 Repairability Test (`17.98-30.9`) | Definition card over screwdriver photo | hard-show | none (breathing) | `REPAIRABILITY` / `EASY TO FIX`; `this matters`; `not magic, just access` | ok |
| 7 | `22.86-30.9` | `battery? part? local shop? mystery machine?` (22.86) | 3 | Checklist board + shrunk definition | hard-show | none (breathing) | `BATTERY? / PART? / LOCAL SHOP? / MYSTERY MACHINE?`; red `LOCKED ROOM?` | ok |
| 8 | `30.9-42.816` | `governments... "Please have a future."` (30.9; reveals 38.9/41.5) | 4 Future Label (`30.9-42.816`) | Policy card; deadpan WIT enters `38.9`, tag lands `41.5` | hard-show; payoff reveal impact | `deadpan-side-eye` giant lower-right `width 1540px` | `FUTURE LABEL` rows; `society, gently:`; red `PLEASE HAVE A FUTURE` + underline | ok (snapshot 42) |

## Render Review-Prevention Pass

- voice cue map completed: `yes - each cue pinned to its spoken line; two timed reveals at 19.55 and 39.8`
- big-scene sanity checked: `yes - 4 persistent scenes, hard cuts at 12.0 / 21.8 / 34.8`
- cue density checked: `yes - 8 cue states over 42.816s`
- motion density checked: `yes - hard-show default; impact only on ALMOST NEW PRICE stamp and the two payoff reveals`
- WIT density: `3 beats (Scene 1 held suspicious, Scene 2 trapped, Scene 4 deadpan); Scene 3 WIT-free`
- WIT crop/collision checked: `inspect reports 0 layout issues at 8 samples; two collision points (cue 5 face vs glass/relationship note, cue 8 face vs PLEASE HAVE A FUTURE tag) handed to Review/Auto-Adjust for screenshot confirmation`
- markup target checked: `yes - shortcut lane, repair bill, locked product, mystery machine, future tag`
- scene differentiation checked: `yes - repair-bench photo, CSS bill/lock scene, screwdriver photo, grid-paper future scene`
- HyperFrames mechanics checked: `yes - lint 0 errors, validate 0 errors, inspect 0 layout issues`
- render decisions made beyond visual plan: `none - faithful restore of the approved build`

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|
| `0.34` | `third reason is repair` | REPAIR CHECKPOINT title + suspicious WIT | hard-show / scene in | ok |
| `3.0` | `harder than replacing it` | HARDER THAN REPLACING + BUY NEW lane | hard-show | ok |
| `5.3 / 6.95 / 8.3` | `part / tool / manual` | 3 security trays | hard-show | ok |
| `9.86` | `costs almost as much` | bill vs box + ALMOST NEW PRICE | hard-show + stamp | ok |
| `12.64` | `And sometimes the product looks at you...` | locked product + quote + trapped WIT | hard-show / scene in | ok |
| `16.2` | `Very healthy relationship` | VERY HEALTHY RELATIONSHIP note | delayed hard-show | ok |
| `17.98` | `repairability... easy to fix` | definition card | hard-show | ok |
| `22.86` | `battery? part? local shop?` | checklist | hard-show | ok |
| `30.9` | `governments... repairability labels` | FUTURE LABEL card | hard-show | ok |
| `38.9` | `society looking at a phone` | deadpan WIT enters | delayed reveal | ok |
| `41.5` | `Please have a future` | PLEASE HAVE A FUTURE tag + underline | delayed reveal | ok |

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|
| Scene 1 | Scene 2 | hard cut at `9.86` | new object (bill/lock) | low | keep |
| Scene 2 | Scene 3 | hard cut at `17.98` | pivot to definition | low | keep |
| Scene 3 | Scene 4 | hard cut at `30.9` | pivot to policy/payoff | low | keep |

## Element Motion Notes

- Entrances: hard-show on the spoken beat for all labels/trays/cards.
- Holds: photo/CSS bases persist for the whole scene; suspicious WIT held across cues 1-3.
- Emphasis: `ALMOST NEW PRICE` stamp; delayed reveal for `VERY HEALTHY RELATIONSHIP` (16.2); final payoff split so the deadpan WIT enters on "society looking at a phone" (38.9) and the `PLEASE HAVE A FUTURE` tag + underline land on the spoken line (41.5).
- Exits: hard cuts at scene boundaries.
- Repeated effects avoided: no fly-in parade; trays and labels simply appear.
- Hard-show vs impact decisions: impact reserved for the price stamp and the two payoff reveals only.
- WIT scale/crop checks: all 3 WIT beats are giant (1120-1540px wide, well above 1/3 frame); only legs/edges cropped.

## Assets

- Shared asset folder: section-local working set under `assets/` (copied from the approved review mirror per the Windows junction workaround).
- Section assets: `assets/section-06/repair-checkpoint-photo-base.jpg`, `assets/section-06/precision-screwdriver-photo-base.jpg`, `assets/section-06/ownership-lock-photo-base.jpg` (padlock, added 2026-06-21), `assets/wit/wit-pose-suspicious.png`, `assets/wit/wit-pose-trapped-by-app-screen.png`, `assets/wit/wit-pose-deadpan-side-eye.png`, `assets/fonts/patrick-hand-latin.woff2`, section audio mp3.
- Attribution: already recorded in the canonical `assets/ATTRIBUTION.md` — `repair-checkpoint-photo-base.jpg` (Wikimedia `SHIFT6mq Repair.jpg`, Triskal, CC BY-SA 4.0, graded + brand-masked) and `precision-screwdriver-photo-base.jpg` (Wikimedia `Precision Screwdriver Set 2.jpg`, oomlout, CC BY-SA 2.0). The `hyperframes/review/assets/ATTRIBUTION.md` mirror copy is older (scoped 1-5) and is stale.

## Verification

- lint: `0 errors, 3 warnings` (held WIT repeated across cues 1-3 = duplicate-media note; 2 track-density notes) - non-blocking
- validate: `0 errors, 0 warnings, 35 contrast warnings` - the contrast notes are the channel's dark-label-over-photo style; non-blocking for the approved direction
- inspect: `0 layout issues across 8 samples` (`1,4.5,9,14,20,24,31,40.5`)
- direct preview screenshots/contact sheet: `regenerated in Auto Adjust pass (2026-06-18) via hyperframes snapshot --at 1,9,14,20,24,31,41 -> snapshots/contact-sheet.jpg + 7 frames`
- export/render, only if explicitly requested: `not requested; no MP4/WebM created`

## Auto Adjust Pass (2026-06-18)

Backup before pass: `manual-saves/auto-adjust-20260618-194852-index.html`.

Verified the restored build against real composited frames (`snapshots/`). Findings:

- WIT Dominance Gate: all 3 WIT beats PASS on screenshots (not CSS box). Cue 1/3 `suspicious` left (~38% frame width, face dominant); cue 5 `trapped-by-app-screen` right behind a transparent glass outline (~40%, hands-up face clear); cue 8 `deadpan-side-eye` right (~36%, face clear). Only legs/lower body cropped; no face/head/shoulder crop.
- Collision (both directions): the two flagged risks are clear in the real render. Cue 5 - quote + `VERY HEALTHY RELATIONSHIP` are center-left, WIT is right, no text over the face. Cue 8 - `PLEASE HAVE A FUTURE` and policy card are center, WIT face is clear to the right.
- Fixed: `dev` script lacked the fixed port; patched to `preview --port 1006` (per the 2026-06-15 port-drift lesson) so future `npm run dev` restarts bind to 1006, not the default Studio port.
- Left intact (approved build, no real defect): at 41s the `PLEASE HAVE A FUTURE` tag overlaps the card's 4th row (`REPAIRABILITY: VISIBLE`); the 3 key policy rows + payoff still read clearly, so the approved payoff composition was preserved. The 35 validate contrast warnings are false positives - the dark labels (`BUY NEW`, `REPAIR BILL`, `repair cost`, `NEW ONE`, `third reason`, `not magic, just access`) render crisp and readable in the frames.
- index.html was not modified in this pass, so lint/validate/inspect results from the render still hold and the `hyperframes/review/section-06.html` mirror stays in sync.

## Auto Adjust Pass (2026-06-21)

Backup before pass: `manual-saves/auto-adjust-20260621-124928-index.html`. Review feedback addressed (4 items):

1. Gray overlay removed (issues 1 + 3): deleted the `<div class="photo-grade tool-grade">` wash over the screwdriver photo and the desaturating `filter` on `.repair-photo` / `.tool-photo`, plus the now-unused `.photo-grade` / `.repair-grade` / `.tool-grade` rules. Real repair-bench and screwdriver photos now read clean and vivid. Per the user's clarification, all scene backgrounds (paper gradients) were left untouched — only the gray wash was removed.
2. Ownership-lock re-timed to the voice (issues 2 + 4): the beat "And sometimes the product looks at you and says, 'You own me...' Very healthy relationship" starts at `12.64s` in the word timings but the cue was pinned at `16.8s`. Moved `cue-ownership-lock` to `12.64` (≈13s) and cascaded every downstream cue + scene cut + in-cue reveal to the faster-whisper word-timing starts (definition `17.98`, checklist `22.86`, future-label `30.9`; scene cuts `9.86 / 17.98 / 30.9`; relationship-note reveal `16.2`; final WIT `38.9`; final tag `41.5`).
3. Track fix required by the re-time: the three accumulating barrier trays overlapped on track 2 (they must be visible together). Moved `NO PART` / `SPECIAL TOOL` / `NO MANUAL` to tracks 3/4/5, added the missing `clip` class + stable ids (`tray-no-part` / `tray-special-tool` / `tray-no-manual`), and trimmed `cue-barrier-trays` to `4.55s` to clear a floating-point boundary overlap with the bill cue.

Preserved: manual Studio edits intact — `tray-special-tool` `data-hf-studio-box-size` (271×138) and `cue-future-label` `data-hf-studio-path-offset` were kept; only timing attributes changed.

Verification:
- lint: `0 errors, 3 warnings` (duplicate-media note for held WIT across cues 1-3; 2 track-density notes) — non-blocking.
- validate: `0 errors, 0 warnings, 35 contrast warnings` — known false positives (white-on-black labels measured against the wrong layer); confirmed crisp on snapshots.
- inspect: `0 layout issues across 9 samples` (`1.5,4,9,11,16.5,20,26,34,42`).
- snapshots regenerated via `hyperframes snapshot --at 1.5,9,11,13.5,16.5,20,26,34,42`: gray wash gone; ownership-lock present at 13.5; relationship note at 16.5; definition at 20; checklist at 26; future card at 34; deadpan WIT + PLEASE HAVE A FUTURE at 42. WIT faces clear at all 3 beats; no text-over-face collisions.
- review mirror `hyperframes/review/section-06.html` re-synced from the canonical preview.
- `package.json` `check` inspect timestamps updated to the new cue times; no MP4/WebM export.

## Auto Adjust Pass 2 (2026-06-21, second review)

Restore points: `manual-saves/auto-adjust-20260621-124928-index.html` (pre pass 1) and `manual-saves/auto-adjust-pass2-20260621-131905-index.html` (post pass 2). Note: no pre-edit backup was taken at the start of this pass because the file had been hand-modified mid-session (the user removed the CSS `locked-product`/`lock-icon`); that intentional edit is incorporated here. Addressed 4 new review notes, all on Scene 2:

1. Lock beat had no real background (issue 1) + the CSS lock-icon didn't read (issue 2): split `scene-cost-lock` into `scene-cost` (`9.86-12.64`, paper bg kept) and a new `scene-ownership-lock` (`12.64-17.98`) using a real graded padlock photo `assets/section-06/ownership-lock-photo-base.jpg` (Wikimedia Commons, Nino Barbieri, CC BY-SA 2.5). The photo is both the scene background and the locked-product depiction; the CSS `locked-product`/`lock-icon` are gone. `.lock-photo` uses `object-position: 42% center` so the padlock sits left and the trapped WIT reads on the right.
2. Text dumped at cue start (issue 3): Scene 2 text now staggers to the word timings via GSAP — `ALMOST NEW PRICE` stamp at 10.94 ("almost as much"), `NEW ONE` at 11.8 ("buying a new one"), quote bubble at 14.46 ("You own me"); relationship note stays at 16.2.
3. Empty decorative element (issue 4): removed the `mystery-machine` + `machine-dot` div from `scene-repairability-test` and its dead CSS. `LOCKED ROOM?` label kept (it pairs with the checklist's `MYSTERY MACHINE?` line).

Verification: lint 0 err / validate 0 err / inspect 0 issues (9 samples); contrast warnings dropped 35→30. Snapshots at `10.5/11.3/12.3/13.5/15/16.5/20/26` confirm the staggered bill+lock reveals, the real padlock background, clear trapped-WIT face, and the removed mystery-machine. Review mirror + its `assets/section-06/ownership-lock-photo-base.jpg` re-synced; ATTRIBUTION.md updated.

Open follow-up (not done, awaiting user): the `fake-phone` slab in `scene-future-label` is a similar empty decorative element; left in place because it ties to "society looking at a phone." The checklist (cue 7) still shows all 4 questions at once and could be staggered to "battery? / part? / local shop?" if desired.

## Auto Adjust Pass 3 (2026-06-21, third review)

Restore point: `manual-saves/auto-adjust-pass3-<ts>-index.html`. Addressed: two scenes lacked a descriptive real image, and the future-label list dumped all rows at once.

1. Cost beat (0:10) real image: `scene-cost` now uses a real euro-banknotes photo `assets/section-06/cost-money-photo-base.jpg` (Wikimedia, Images Money, CC BY 2.0) as the full-frame background, grounding "the repair costs almost as much as buying a new one" behind the REPAIR BILL vs NEW ONE comparison (replaced the flat `bill-scene` gradient).
2. Future-label scene (0:31) real image: `scene-future-label` now uses a real "phone on a table" photo `assets/section-06/future-phone-photo-base.jpg` (Wikimedia, Santeri Viinamäki, CC BY-SA 4.0) for "society looking at a phone" (replaced the empty `fake-phone` slab + grid gradient). First chose a desk photo (Pixel.la CC0) but it contained a recognizable laptop — swapped to a phone-only, logo-free image per the channel no-logo rule.
3. Future-label rows staggered to the words: REPAIR INFO @31.94, SPARE PARTS @33.02, BATTERY LIFE @33.72, REPAIRABILITY @34.52 (GSAP opacity sets; the FUTURE LABEL card + "society, gently:" still hard-show at 30.9).
4. Incidental fixes: repaired a stray line-break that had split `transform: rotate(3deg)` mid-word on the BUY NEW label; added `data-layout-allow-overflow` + `overflow: visible` to the two WIT-bearing cues (`cue-ownership-lock`, `cue-future-label`) so the intentional off-canvas WIT no longer trips clipped-text/overflow inspect errors at every sample time.

Scene clips now: `scene-repair-checkpoint` (0/9.86, repair photo), `scene-cost` (9.86/2.78, euro money photo), `scene-ownership-lock` (12.64/5.34, padlock photo), `scene-repairability-test` (17.98/12.92, screwdriver photo), `scene-future-label` (30.9/11.916, phone photo) — all four non-checkpoint beats now have real photographic backgrounds.

Verification: lint 0 err / validate 0 err (30 contrast false-positives) / inspect 0 layout issues across 8 samples (`11,13.5,16.5,20,31,32.5,35.5,42`). Snapshots confirm the euro-money cost bg, the phone future bg (no laptop/logo), and the staggered policy rows. Mirror + both new images re-synced; ATTRIBUTION.md updated.

## Auto Adjust Pass 4 (2026-06-21, fourth review)

Restore point: `manual-saves/auto-adjust-pass4-<ts>-index.html`. Single note: the repairability-test background (0:18, `scene-repairability-test`) looked bad — the precision-screwdrivers-on-white image read as sterile/floating.

Fix: replaced it with a real opened-phone / battery / repair-tools bench photo `assets/section-06/repairability-photo-base.jpg` (Wikimedia, Peretz Partensky, CC BY-SA 2.0). It directly illustrates the scene's voice ("repairability = easy to fix / can you replace the battery / can you buy the part"), is people-free and brand-free (battery shows only a generic Li-ion warning), and is visually distinct from Scene 1's repair-bench. Higher-res people-bearing options (e.g. "Electronics Repair Workbench" 4160×3120, "Repair Lab" 2400×1602) were rejected per the channel's no-real-people-in-direct-backgrounds guardrail; this image is 1200×900 but sits behind the large definition/checklist cards so the moderate resolution is not noticeable. The old `precision-screwdriver-photo-base.jpg` is superseded (kept on disk, no longer referenced).

Verification: lint 0 / validate 0 / inspect 0 layout issues (9 samples); snapshots at 18/20/26 confirm the new bench reads well behind the cards. Mirror + image synced; ATTRIBUTION.md updated.

## Auto Adjust Pass 5 (2026-06-21, fifth review)

Restore point: `manual-saves/auto-adjust-pass5-<ts>-index.html`. Single note: the `PLEASE HAVE A FUTURE` payoff tag wrapped to two lines and its separate red-underline bar (a fixed 250px `div` at `left:988`) didn't track the text.

Fix: forced one line and made the underline part of the text. `.future-tag` font-size `82px→60px`, width `730→820`, repositioned to `left:210/top:805` (clear of the deadpan WIT on the right); `.future-tag > span` now has `white-space:nowrap` + a `border-bottom` red underline, so the underline is always exactly the text width and aligned. Deleted the orphaned `.red-underline` div + CSS and dropped it from the GSAP reveal (tag still reveals at 41.5).

Verification: lint 0 / validate 0 / inspect 0 (9 samples); snapshot at 42s confirms one line + full-width aligned underline. Mirror synced. The payoff tag still intentionally overlaps the card's redundant 4th row (`REPAIRABILITY: VISIBLE`), as in the approved composition.

## Notes

- This was a restore, not a redesign: the Section 6 visual-plan markdown and the section-preview working folder were missing while the approved render survived. The plan was reconstructed first, then this preview was rebuilt 1:1 from the review mirror.
- Two layout QA points for Review/Auto-Adjust: (1) cue 5 - confirm the trapped WIT face reads clearly through the glass panel and is not covered by the quote bubble / relationship note; (2) cue 8 - confirm the `PLEASE HAVE A FUTURE` tag does not cover the deadpan WIT face.
- Contrast warnings could be reduced in a later pass by widening label padding or darkening label backgrounds, but that is a review decision, not part of this restore.
