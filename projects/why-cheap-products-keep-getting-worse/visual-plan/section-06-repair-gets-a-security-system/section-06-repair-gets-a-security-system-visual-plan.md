# Section 6 Visual Plan

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 6: Repair Gets A Security System`

Status:
`reconstructed from approved render - ready for re-render and review`

Reconstruction note:
The Section 6 visual-plan markdown was missing on disk while the approved render survived at `hyperframes/review/section-06.html` plus its photo bases. This plan is rebuilt to match that approved build exactly (4 big scenes, 8 cue states, 3 giant WIT beats, real repair/screwdriver photo bases, no WIT in the definition/checklist scene) so render can rebuild the section preview 1:1. All timings below are the actual render `data-start`/`data-duration` values, not estimates.

## Section Goal

Make repair feel like a security checkpoint the product must pass, then define `repairability` in plain English so an English learner leaves with a simple yes/no test. Keep the policy mention as one quick proof beat and land `Please have a future` warm and slightly deadpan. WIT should feel locked out of his own object without blaming the buyer.

## Source Inputs

- Script: `02-script.md`, `Section 6: Repair Gets A Security System`
- Voiceover: `voiceover/section-06-repair-gets-a-security-system/scratch-audio/section-06-repair-gets-a-security-system-david23-am_eric-0.84.mp3`
- Marked script: `voiceover/section-06-repair-gets-a-security-system/section-06-repair-gets-a-security-system-marked-script.md`
- Script promise: `a product becomes disposable when fixing it is harder than replacing it; repairability is how easy it is to fix`
- Section duration: `42.816s` (render uses this as the source of truth; final scene holds to the end)

## Narration

```text
The third reason is repair.

A product feels disposable when fixing it becomes harder than replacing it.

Sometimes the part is not available.

Sometimes the tool is special.

Sometimes the manual is missing.

Sometimes the repair costs almost as much as buying a new one.

And sometimes the product looks at you and says, "You own me, but not enough to open me."

Very healthy relationship.

This is why repairability matters.

Repairability just means how easy something is to fix.

Can you replace the battery?

Can you buy the part?

Can a local repair shop understand the product without needing a mysterious machine in a locked room?

Some governments now treat repair information, spare parts, battery life, and repairability labels as things worth requiring for certain products.

That is basically society looking at a phone and saying:

"Please have a future."
```

## Visual Direction

- Big-scene/cue rhythm: `4 persistent big scenes, 8 cue states over 42.816s`
- Big scene rhythm: `repair checkpoint -> cost + ownership lock -> repairability test -> future label payoff`
- Cue-state count: `8`
- Main visual metaphor: `repair as an airport-style security checkpoint - the product must pass NO PART / SPECIAL TOOL / NO MANUAL trays, and ownership does not include the right to open`
- WIT emotional path: `suspicious repairer at the checkpoint -> trapped/locked-out owner behind glass -> deadpan but warm at the "please have a future" plea`
- WIT density: `3 total WIT beats; one held pose in Scene 1, one in Scene 2, one in Scene 4; Scene 3 is intentionally WIT-free`
- Motion density: `hard cuts between big scenes; labels hard-show on the spoken beat; only ALMOST NEW PRICE stamp, the delayed VERY HEALTHY RELATIONSHIP reveal, and the final PLEASE HAVE A FUTURE reveal use impact/timed reveal`
- Real-life texture: `real phone-repair workbench photo (Scene 1 base) and real precision-screwdriver set photo (Scene 3 base), both graded and brand-masked`
- Real image references: `2 Wikimedia Commons photos saved and used as graded photo bases; 1 EU repairability/energy label reference (inspiration); 1 airport-security metaphor reference (inspiration)`
- Generated/support assets: `none; locks, bill, box, scanner, belt, trays, definition card, checklist, mystery machine, fake phone, and future-label card are all self-made CSS in HyperFrames`
- Viewer attention strategy: `open on a literal security checkpoint that matches the section title, escalate barriers as security trays, then pay off with a clean definition and a warm policy beat`
- Retention risk: `the barrier list (part/tool/manual/cost) could become a scattered card tray, and the repairability definition could read like a lesson`
- Visual fix: `compress barriers into 3 security trays on one belt, hold one large definition card, and keep the checklist to 4 short questions`
- Red markup: `one red ALMOST NEW PRICE stamp, one red HARDER THAN REPLACING / LOCKED ROOM? correction label per relevant cue, one red PLEASE HAVE A FUTURE tag with underline; no decorative circles`
- Motion rule: `static photo/CSS bases; ordinary labels hard-show; reserve impact for the price stamp and the two timed payoff reveals`

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|
| 1. Repair Checkpoint | `0:00-12.0` | `The third reason is repair.` -> `...the manual is missing.` | Graded, brand-masked real phone-repair-table photo + CSS airport checkpoint rig: conveyor belt, scanner arch, exposed-board phone on the belt, yellow `BUY NEW` shortcut arrow lane. | Turns "repair" into a literal security checkpoint the product must pass; the section title made visible. Barriers become security trays. | Cut after the three barrier trays land, on the pivot to repair cost. | `phone-repair-table-commons-triskal-cc-by-sa-4.jpg` (graded -> `repair-checkpoint-photo-base.jpg`); airport-security metaphor reference (inspiration). | `assets/section-06/repair-checkpoint-photo-base.jpg` |
| 2. Cost + Ownership Lock | `12.0-21.8` | `Sometimes the repair costs almost as much...` -> `Very healthy relationship.` | CSS bill-scene: a tall repair bill beside a similar-height new-product box; then a dark locked product with a yellow padlock behind a glass panel. | Proves the two strongest disposable pushes: repair ≈ new price, and you cannot even open what you own. | Cut on `This is why repairability matters.` | Self-made CSS only; ownership-lock metaphor; no real photo base. | none (CSS-built) |
| 3. Repairability Test | `21.8-34.8` | `This is why repairability matters.` -> `...a mystery machine in a locked room?` | Graded real precision-screwdriver-set photo + CSS mystery-machine; holds a large `REPAIRABILITY = EASY TO FIX` definition card and a 4-item yes/no checklist. | Defines repairability in plain English and turns it into a simple test for English learners. | Cut on the policy line. | `precision-screwdriver-set-commons-oomlout-cc-by-sa-2.jpg` (graded -> `precision-screwdriver-photo-base.jpg`). | `assets/section-06/precision-screwdriver-photo-base.jpg` |
| 4. Future Label | `34.8-42.816` | `Some governments now treat repair information...` -> `"Please have a future."` | CSS future-scene (grid paper) + a generic `fake-phone`; a `FUTURE LABEL` policy card with four requirement rows; final `PLEASE HAVE A FUTURE` red tag. | Lands the policy proof as one quick beat and the warm `future` motif callback that ties Section 6 back to the whole video. | End hold to `42.816s`. | EU repairability/energy label reference (inspiration only; rebuilt generic). | none (CSS-built); `policy/smartphones-tablets-energy-label-eu-reference.png` (inspiration) |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | Motion Type | WIT Pose / Size / Safe Crop | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|---|
| 1 | `0:00-3.0` | `The third reason is repair.` | 1 | Hard cut in. `REPAIR CHECKPOINT` yellow title + `third reason` small tag. Giant suspicious WIT rises from the lower-left edge. | Repair-table photo base + checkpoint rig (belt, scanner, board-phone). | `hard-show` + scene transition in | `wit-pose-suspicious.png`, `width 1120px`, anchored `left:-150px / bottom:-320px`, ~58% frame width, face/head/shoulders high and safe; only legs cropped by bottom edge. | `REPAIR CHECKPOINT`; `third reason` | Repair-table photo base. | Names the section as a security checkpoint in one frame. |
| 2 | `3.0-6.4` | `...harder than replacing it.` | 1 | `BUY NEW` shortcut-lane arrow appears bypassing the checkpoint; red `HARDER THAN REPLACING` correction lands. | Title, photo base, checkpoint rig, suspicious WIT. | `hard-show` | Same `wit-pose-suspicious.png`, same placement (held, not re-entered). | `BUY NEW`; red `HARDER THAN REPLACING` | CSS shortcut arrow. | Shows the disposable logic: replacing is the easy lane. |
| 3 | `6.4-12.0` | `Sometimes the part is not available. Sometimes the tool is special. Sometimes the manual is missing.` | 1 | Three security trays slide onto the belt: `NO PART`, `SPECIAL TOOL`, `NO MANUAL`. | Title, `BUY NEW`, photo base, checkpoint rig, suspicious WIT. | `hard-show` (one tray per spoken barrier) | Same `wit-pose-suspicious.png`, held. | `NO PART`; `SPECIAL TOOL`; `NO MANUAL` | CSS trays. | Compresses the barrier list into 3 checkpoint trays instead of scattered cards. |
| 4 | `12.0-16.8` | `Sometimes the repair costs almost as much as buying a new one.` | 2 | Hard cut to bill-scene. Tall `REPAIR BILL` with `repair cost` total appears beside a `NEW ONE` box of similar height; red `ALMOST NEW PRICE` stamp lands between them. | Bill-scene background. | `hard-show`; `impact` on `ALMOST NEW PRICE` stamp | No WIT (breathing beat). | `REPAIR BILL`; `repair cost`; `NEW ONE`; red stamp `ALMOST NEW PRICE` | CSS bill + 3D box + stamp. | Makes "costs almost as much" a single readable comparison. |
| 5 | `16.8-21.8` | `...You own me, but not enough to open me. Very healthy relationship.` | 2 | Dark locked product with a yellow padlock + quote bubble `YOU OWN ME... NOT ENOUGH TO OPEN ME`. On the deadpan beat (`~19.55s`) the red `VERY HEALTHY RELATIONSHIP` note hard-shows. Giant WIT sits trapped behind a glass panel on the lower-right. | Bill-scene background. | `hard-show`; delayed `hard-show` of the relationship note at `19.55s` | `wit-pose-trapped-by-app-screen.png`, `width 1460px`, anchored `right:-420px / bottom:-420px`, behind the glass panel (`z-index` below glass), face readable through glass; legs/side cropped by edges only. | quote `YOU OWN ME... NOT ENOUGH TO OPEN ME`; red `VERY HEALTHY RELATIONSHIP` | CSS locked product + padlock + glass panel. | Lands the locked-out joke; WIT is literally trapped behind glass. |
| 6 | `21.8-26.5` | `This is why repairability matters. Repairability just means how easy something is to fix.` | 3 | Hard cut to screwdriver photo base. Large `REPAIRABILITY` definition card with sub `EASY TO FIX`; small `this matters` and `not magic, just access` notes. | Screwdriver photo base + mystery-machine. | `hard-show` | No WIT (definition must read clean). | `REPAIRABILITY`; `EASY TO FIX`; `this matters`; `not magic, just access` | CSS definition card. | The held plain-English definition for English learners. |
| 7 | `26.5-34.8` | `Can you replace the battery? Can you buy the part? Can a local repair shop understand the product without needing a mysterious machine in a locked room?` | 3 | Definition card shrinks to the left; a checklist board appears with `BATTERY?`, `PART?`, `LOCAL SHOP?`, `MYSTERY MACHINE?`; red `LOCKED ROOM?` note near the CSS mystery-machine. | Screwdriver photo base, mystery-machine, shrunk definition card. | `hard-show` (rows appear with their questions) | No WIT (checklist breathes). | checklist `BATTERY? / PART? / LOCAL SHOP? / MYSTERY MACHINE?`; red `LOCKED ROOM?` | CSS checklist board. | Turns repairability into a simple yes/no test plus the locked-room joke. |
| 8 | `34.8-42.816` | `Some governments now treat repair information, spare parts, battery life, and repairability labels... "Please have a future."` | 4 | Hard cut to future-scene. `FUTURE LABEL` card with rows `REPAIR INFO: YES`, `SPARE PARTS: YES`, `BATTERY LIFE: LONGER`, `REPAIRABILITY: VISIBLE`; `society, gently:` tag. On the payoff (`~39.8s`) the giant deadpan WIT, the red `PLEASE HAVE A FUTURE` tag, and its underline hard-show together. | Future-scene + fake-phone. | `hard-show` on policy card; delayed `impact` reveal of WIT + `PLEASE HAVE A FUTURE` + underline at `39.8s` | `wit-pose-deadpan-side-eye.png`, `width 1540px`, anchored `right:-420px / bottom:-550px`, ~80% frame width, face/head high and safe; legs cropped by bottom edge only. | `FUTURE LABEL` rows; `society, gently:`; red `PLEASE HAVE A FUTURE` + underline | CSS future-label card + fake phone. | Quick policy proof + warm motif callback payoff. |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop / Margin | Why WIT Is Needed |
|---|---:|---|---|---|---|---|
| 1-3 | `0:00-12.0` | suspicious repairer eyeing the security checkpoint | `wit-pose-suspicious.png` | Lower-left giant edge entrance, `width 1120px` (`left:-150px / bottom:-320px`), visible footprint well above `1/3` frame. | Face, glasses, head, shoulders high and clear; only legs cropped by bottom edge. Labels live on the upper-left/center, away from the face. | Gives the checkpoint a human who is locked out and suspicious. |
| 5 | `16.8-21.8` | trapped, locked out of his own product | `wit-pose-trapped-by-app-screen.png` | Lower-right giant, behind glass panel, `width 1460px` (`right:-420px / bottom:-420px`), at least `1/3` frame. | Render behind the glass panel (intentional trapped look) but keep face readable; quote bubble and relationship note must not cover the face. | Lands "you own me, but not enough to open me" as a physical trap. |
| 8 | `34.8-42.816` (reveal `39.8`) | deadpan but warm; quietly hoping | `wit-pose-deadpan-side-eye.png` | Lower-right giant, `width 1540px` (`right:-420px / bottom:-550px`), ~80% frame width. | Face/head high and safe; legs cropped by bottom edge only. `PLEASE HAVE A FUTURE` tag sits lower-center, never over the face. | Carries the warm-deadpan `please have a future` payoff. |

WIT density note:

- Total WIT beats: `3`
- WIT beats per big scene: `Scene 1: 1 (held across cues 1-3)`, `Scene 2: 1 (cue 5)`, `Scene 3: 0`, `Scene 4: 1 (cue 8)`
- Any big scene above `2` WIT beats, and why: `none`
- Cue states intentionally without WIT: `4`, `6`, `7`; the cost comparison, the definition, and the checklist must read clearly without a reaction fighting them.

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion Type | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|---|
| 1 | `0:00-3.0` | `REPAIR CHECKPOINT`; `third reason` | `hard-show` | Whole checkpoint scene. | Names the metaphor and the section position. | No extra captions over the photo base. |
| 2 | `3.0-6.4` | `BUY NEW`; red `HARDER THAN REPLACING` | `hard-show` | Shortcut-lane arrow bypassing the checkpoint. | Shows replacing is the frictionless lane. | Do not mark the photo itself; keep the red note to one line. |
| 3 | `6.4-12.0` | `NO PART`; `SPECIAL TOOL`; `NO MANUAL` | `hard-show` | The three security trays on the belt. | Compresses the spoken barriers into 3 readable trays. | No fourth tray, no scattered cards, no arrows to each. |
| 4 | `12.0-16.8` | `REPAIR BILL`; `repair cost`; `NEW ONE`; red stamp `ALMOST NEW PRICE` | `hard-show`; stamp `impact` | Repair bill vs new-product box. | Makes "costs almost as much" one comparison + one stamp. | Do not list line-item prices; keep the bill lines abstract. |
| 5 | `16.8-21.8` | quote `YOU OWN ME... NOT ENOUGH TO OPEN ME`; red `VERY HEALTHY RELATIONSHIP` | `hard-show`; note delayed to `19.55s` | Locked product + padlock; deadpan beat. | Lands the talking-product joke and the dry punchline. | Note must not cover WIT face behind glass. |
| 6 | `21.8-26.5` | `REPAIRABILITY`; `EASY TO FIX`; `this matters`; `not magic, just access` | `hard-show` | Definition card. | Plain-English definition held long enough to read. | No paragraph; keep sub-line to 3 words. |
| 7 | `26.5-34.8` | `BATTERY?`; `PART?`; `LOCAL SHOP?`; `MYSTERY MACHINE?`; red `LOCKED ROOM?` | `hard-show` | Checklist board + mystery-machine. | Turns repairability into a 4-question test + joke. | No more than 4 questions; no real diagnostic UI. |
| 8 | `34.8-42.816` | `FUTURE LABEL` rows (`REPAIR INFO/SPARE PARTS/BATTERY LIFE/REPAIRABILITY`); `society, gently:`; red `PLEASE HAVE A FUTURE` + underline | `hard-show`; payoff reveal `impact` at `39.8s` | Future-label policy card + final tag. | Quick policy proof + warm motif payoff. | Do not reproduce the real EU label design/marks; keep it generic. |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|
| Phone repair table photo | `real image` | Wikimedia Commons, Triskal, `CC BY-SA 4.0`, saved and inspected | Scene 1 graded photo base (repair checkpoint) | `safe asset` for direct graded use with brand masks; attribution required | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/phone-repair-table-commons-triskal-cc-by-sa-4.jpg` -> graded `assets/section-06/repair-checkpoint-photo-base.jpg` |
| Precision screwdriver set photo | `real image` | Wikimedia Commons, oomlout, `CC BY-SA 2.0`, saved and inspected | Scene 3 graded photo base (repairability test) | `safe asset` for direct graded use; attribution required | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/precision-screwdriver-set-commons-oomlout-cc-by-sa-2.jpg` -> graded `assets/section-06/precision-screwdriver-photo-base.jpg` |
| EU smartphone/tablet energy + repairability label | `real reference image` | EU energy/repairability label reference, saved and inspected | Scene 4 inspiration for the generic `FUTURE LABEL` policy card | `inspiration only`; do not reproduce the official label layout/marks | `assets/visual-references/section-06-repair-gets-a-security-system/policy/smartphones-tablets-energy-label-eu-reference.png` |
| Airport security check | `real reference image` | CC0 reference, saved and inspected | Scene 1 inspiration for the belt/scanner/tray checkpoint metaphor | `inspiration only`; rebuilt generic in CSS | `assets/visual-references/section-06-repair-gets-a-security-system/metaphor/airport-security-check-cc0-inspiration.png` |
| WIT poses | `local channel asset` | Shared approved WIT manifest `.agents/_shared/assets/wit/poses/manifest.json` | Direct WIT overlays for cues 1-3, 5, 8 | `safe channel asset` | `assets/wit/wit-pose-suspicious.png`, `assets/wit/wit-pose-trapped-by-app-screen.png`, `assets/wit/wit-pose-deadpan-side-eye.png` |
| Checkpoint rig, bill, box, lock, glass, definition card, checklist, mystery machine, fake phone, future-label card | `self-made HyperFrames / CSS` | Built in the section HTML from script + references | Direct production objects for all 4 scenes | `safest route`: no logos, no real UI, exact label control | built in `section-previews/section-06-repair-gets-a-security-system/index.html` |

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|
| `repair-checkpoint-photo-base.jpg` | Scene 1, cues 1-3 | Real repair-bench texture under the checkpoint metaphor | `0:00-12.0` | Full-frame `object-fit: cover`, graded with a paper wash; brand masks over battery/tool marks | Direct graded background | `safe direct asset (brand-masked, attribution required)` |
| `precision-screwdriver-photo-base.jpg` | Scene 3, cues 6-7 | Real precision-tool texture under the repairability test | `21.8-34.8` | Full-frame `object-fit: cover`, graded with a paper wash | Direct graded background | `safe direct asset (attribution required)` |
| EU energy/repairability label reference | Scene 4 planning | What an official repairability/future label looks like | Not on screen | None | Translated into a generic `FUTURE LABEL` card | `inspiration only` |
| Airport security check reference | Scene 1 planning | Belt/scanner/tray checkpoint composition | Not on screen | None | Translated into generic CSS belt, scanner, trays | `inspiration only` |
| Checkpoint rig (belt + scanner + board-phone + shortcut lane) | Scene 1, cues 1-3 | The security-checkpoint metaphor | `0:00-12.0` | Center band over the photo base; `BUY NEW` arrow upper-right | CSS build | `self-made safe asset` |
| Repair bill + new box + stamp | Scene 2, cue 4 | Cost comparison | `12.0-16.8` | Bill left, box right, stamp center | CSS build | `self-made safe asset` |
| Locked product + padlock + glass panel | Scene 2, cue 5 | Locked-out ownership | `16.8-21.8` | Product center-left, glass over lower-right WIT | CSS build | `self-made safe asset` |
| Definition card + checklist + mystery machine | Scene 3, cues 6-7 | Definition and yes/no test | `21.8-34.8` | Definition left, checklist right, mystery machine lower-left | CSS build | `self-made safe asset` |
| Future-label card + fake phone | Scene 4, cue 8 | Policy proof + payoff frame | `34.8-42.816` | Card center, fake phone left, tag lower-center, WIT lower-right | CSS build | `self-made safe asset` |
| WIT poses | Cues 1-3, 5, 8 | Emotional read | 3 beats | Giant lower-edge placements, at least `1/3` frame | Direct PNG overlay | `safe channel asset` |

## HyperFrames Guidance

- Composition target: `Section06RepairGetsASecuritySystem`, `1920x1080`, `data-duration 42.816`, font `PatrickHandLocal` (`assets/fonts/patrick-hand-latin.woff2`)
- Big scene count: `4` (scene clips: `scene-repair-checkpoint` 0/12, `scene-cost-lock` 12/9.8, `scene-repairability-test` 21.8/13, `scene-future-label` 34.8/8.016)
- Cue state count: `8` (cue clips on track 2 with the exact starts/durations in the timeline above)
- Scene components: `PhotoBase (repair, screwdriver)`, `BrandMask`, `CheckpointRig (belt/scanner/board-phone/shortcut-lane)`, `SecurityTray x3`, `RepairBill`, `NewBox`, `Stamp`, `LockedProduct + LockIcon`, `GlassPanel`, `QuoteBubble`, `DefinitionCard`, `ChecklistBoard`, `MysteryMachine`, `FutureLabelCard`, `FakePhone`, `FutureTag`, `RedUnderline`, `WIT`
- Timing notes: `hard cuts at 12.0, 21.8, 34.8; relationship note opacity 0->1 at 19.55; final WIT + PLEASE HAVE A FUTURE + underline opacity 0->1 at 39.8 via the GSAP timeline`
- Motion density rule: `static bases; labels hard-show; impact only for the ALMOST NEW PRICE stamp and the two timed reveals`
- Text style: `handwritten cream/black labels, red correction labels and stamp, generic policy pills; never bake text into the photo bases`
- Asset paths: `assets/section-06/repair-checkpoint-photo-base.jpg`, `assets/section-06/precision-screwdriver-photo-base.jpg`, `assets/wit/`, `assets/fonts/patrick-hand-latin.woff2`, section audio `section-06-repair-gets-a-security-system-david23-am_eric-0.84.mp3`
- Audio sync notes: `REPAIR CHECKPOINT on "third reason is repair"; HARDER THAN REPLACING on "harder than replacing"; 3 trays on the 3 "sometimes" barriers; ALMOST NEW PRICE on the cost line; quote + delayed VERY HEALTHY RELATIONSHIP on the deadpan beat (~19.55); REPAIRABILITY = EASY TO FIX on the [slower] definition; checklist on the 3 questions; FUTURE LABEL on the policy line; PLEASE HAVE A FUTURE reveal on the final deadpan line (~39.8)`
- WIT pose files: `wit-pose-suspicious.png` (cues 1-3), `wit-pose-trapped-by-app-screen.png` (cue 5), `wit-pose-deadpan-side-eye.png` (cue 8)
- WIT exact rebuild coordinates: `cue1-3 suspicious: left:-150px; bottom:-320px; width:1120px`; `cue5 trapped (behind-glass): right:-420px; bottom:-420px; width:1460px`; `cue8 deadpan (final-reveal): right:-420px; bottom:-550px; width:1540px`
- WIT density: `3 total beats, one per big scene except Scene 3 (none)`
- WIT scale and crop guards: `each WIT beat fills well above 1/3 frame; crop only legs/lower body at the bottom edge; never crop face, glasses, head, shoulders, or mouth; keep the quote bubble, relationship note, and future tag off the face`
- No-WIT breathing beats: `4`, `6`, `7`
- Suggested inspect timestamps: `1.0s`, `4.5s`, `9.0s`, `14.0s`, `20.0s`, `24.0s`, `30.0s`, `40.5s`
- Suggested screenshot/contact-sheet QA timestamps: `1.2s` (checkpoint + suspicious WIT), `9.2s` (3 trays readable), `14.4s` (bill vs box + stamp), `20.2s` (trapped WIT face clear of glass + relationship note), `24.2s` (definition card readable), `31.0s` (checklist + LOCKED ROOM?), `41.0s` (final WIT + PLEASE HAVE A FUTURE clear of face)
- Suggested MP4 QA frame timestamps, only if export is explicitly requested: `none; export not requested`
- Build risks: `WIT face clipped by the right edge or covered by glass/labels at cues 5 and 8; barrier trays becoming a scattered tray; definition reading like a lesson; future-label card drifting too close to the real EU label; lowest labels (LOCKED ROOM?, PLEASE HAVE A FUTURE) creeping into the subtitle zone`
- Must not invent: `the checkpoint metaphor, the 4 scene bases, the 8 cue timings, the 3 WIT poses and their giant placements, the label text, the two timed reveals, or the brand masks on the photo bases`

## Review-Prevention Checklist

- voice sync mapped to phrase cues: `yes - each cue is pinned to its spoken line, with two timed reveals on the deadpan beats`
- big-scene rhythm avoids unrelated rapid boards: `yes - 4 persistent scenes, hard cuts only at 12.0 / 21.8 / 34.8`
- cue density stays readable: `yes - 8 cue states across 42.816s`
- motion density uses hard-show by default: `yes`
- impact motion reserved for emphasis: `yes - ALMOST NEW PRICE stamp and the two payoff reveals only`
- WIT rhythm not overused: `yes - 3 total beats, Scene 3 is WIT-free`
- WIT size readable: `yes - 1120-1540px wide, well above 1/3 frame`
- WIT crop safe: `verify at QA - faces high; cues 5 and 8 right-edge/glass crop must keep the face readable`
- WIT does not cover text/evidence: `yes - WIT on the lower edge, labels in upper/center zones`
- red markup targets exact objects: `yes - shortcut lane, repair bill, locked product, mystery machine, future tag`
- scene bases visually differentiated: `yes - repair-bench photo, CSS bill/lock scene, screwdriver photo, grid-paper future scene`
- render does not need to invent timing/layout/assets: `yes - exact clips, coordinates, and reveals are specified`

## Approval Checks

- visual reference pass completed: `yes - 2 real Wikimedia photos used as graded bases, EU label + airport-security used as inspiration; all saved under assets/visual-references/section-06-.../`
- what/when/how clear: `yes`
- big scenes grouped, not one full scene per sentence: `yes`
- cue states low enough for section duration: `yes`
- attention reason per big scene / cue state: `yes`
- label readable: `yes`
- WIT has a clear job: `yes - locked-out repairer arc`
- WIT pose files named: `yes`
- WIT facial emotion large enough: `yes`
- WIT face/head/shoulder crop safe: `verify at QA for cues 5 and 8`
- WIT density counted and justified: `yes`
- no-WIT breathing beats planned: `yes - cues 4, 6, 7`
- red markup points to exact object: `yes`
- ordinary labels hard-show unless emphasis needs impact motion: `yes`
- impact animation reserved for emphasized spoken beats: `yes`
- real-life asset explains, not decorates: `yes - repair bench and precision tools ground the metaphor`
- title-thumbnail promise still being paid off: `yes - "future" motif returns via PLEASE HAVE A FUTURE`
- safe for English learners: `yes - plain-English definition, 4 short questions, repeated simple labels`
- ready for HyperFrames: `yes - rebuildable 1:1 from this plan and the surviving review-mirror HTML`
