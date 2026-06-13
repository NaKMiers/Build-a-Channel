# Section 4 Visual Plan

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 4: The Boring Parts Disappear`

Status:
`remake plan - simple Section 1 style`

## Section Goal

Make the idea simple and visual: cheap products can still look normal because the missing parts are boring, quiet, and hidden inside the product's future.

## Source Inputs

- Script: `02-script.md`, `Section 4: The Boring Parts Disappear`
- Voiceover: `voiceover/section-04-the-boring-parts-disappear/scratch-audio/section-04-the-boring-parts-disappear-david23-am_eric-0.84.mp3`
- Script promise: `the boring parts are where a product's future lives`
- Section duration: `37.867s`
- Remake reason: `previous Section 4 render direction was too crowded, with too many text blocks and object cards spread across the screen`

## Narration

```text
The future of a product is usually not exciting.

It is boring things.

Thicker fabric.

Stronger stitching.

A hinge that does not act surprised by movement.

A battery you can replace.

A screw that uses a normal screwdriver instead of a secret handshake.

A spare part that still exists after the product leaves the factory.

These things are not very glamorous.

Nobody walks into a store and whispers, "Wow. Look at the long-term availability of replacement parts."

That person exists, but they are probably already repairing a printer.

Most people see the shape, the color, the price, and whether the product can arrive tomorrow.

So the boring future pieces are easy to hide.

The product still looks complete.

It just has less future built into it.
```

## Visual Direction

- Big-scene/cue rhythm: `3 persistent backgrounds, 6 cue states; no scattered object-card board`
- Big scene rhythm: `material future -> repair table / printer joke -> complete outside, missing inside`
- Cue-state count: `6`
- Main visual metaphor: `background photos show boring physical texture; WIT carries the emotional read`
- WIT emotional path: `large suspicious inspector -> large printer-repair nerd -> large betrayed buyer`
- WIT density: `3 total WIT beats, one per big scene`
- Motion density: `static hard cuts only; ordinary labels hard-show; one final stamp`
- Real-life texture: `sewing/stitching photo, screwdriver table photo, cardboard box photo`
- Real image references: `reuse existing 6 Pexels references; direct background candidates are fabric, screwdriver, cardboard`
- Generated/support assets: `none; render builds simple generic overlays in CSS`
- Viewer attention strategy: `few real backgrounds plus big WIT emotion; each paused frame should read in one second`
- Retention risk: `the parts list can become vocabulary homework if every word gets its own label`
- Visual fix: `compress the list into three memory labels: BORING FUTURE, REPAIRABLE, LESS FUTURE BUILT IN`
- Red markup: `only the final missing-future stamp, plus optional small secret-handshake cross-out if it stays clean`
- Motion rule: `no decorative animation and no transition pileup; clarity beats motion`

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|
| 1. Boring future is material | `0:00-0:09.8` | `The future... hinge... movement.` | Full-frame sewing/fabric background with a soft local label zone; giant suspicious WIT on the left; one large label `BORING FUTURE`. | Shows that the future lives in unexciting material choices, not shiny features. | Cut after `hinge... movement` when the material list is established. | Sewing/stitching photo, hinge reference for mental model only. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-sewing-machine-stitching-fabric-pexels-shoreline-vehicles.jpg`; hinge photo is mockup/reference only |
| 2. Repair table / printer person | `0:09.8-0:28.8` | `A battery... repairing a printer.` | Full-frame screwdriver/repair table texture; one simple generic device outline; later a generic printer silhouette appears with giant thinking WIT. | Keeps battery, screwdriver, spare part, and printer joke inside one repair surface instead of many mini cards. | Cut after the printer joke has landed. | Screwdriver photo, phone repair mockup target, printer repair inspiration. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-screwdriver-bits-pexels-roseson-studios.jpg`; phone/printer photos are not used directly |
| 3. Looks complete, future missing | `0:28.8-0:37.867` | `Most people see... less future built into it.` | Full-frame cardboard/product-box background; simple complete-looking box silhouette opens to a hollow missing-future tag; giant betrayed WIT on the right. | Pays off the section in one memory frame: outside complete, inside missing future. | End hold. | Cardboard box photo. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-cardboard-boxes-pexels-harper-sunday.jpg` |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | Motion Type | WIT Pose / Size / Safe Crop | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|---|
| 1 | `0:00-0:04.8 estimated` | `future... not exciting / boring things` | 1 | Sewing/fabric background appears. WIT is large on left. One label says `BORING FUTURE`. | Same background and WIT. | `static` | `wit-pose-suspicious.png`, 1/3 to 1/2 frame emotional read, face/head/shoulders safe. | `BORING FUTURE` | Fabric photo direct background. | Opens with the idea, not a pile of icons. |
| 2 | `0:04.8-0:09.8 estimated` | `Thicker fabric... hinge... movement` | 1 | One small support label appears: `FABRIC + STITCHING + HINGE`. No separate object cards. | Background and suspicious WIT hold. | `hard-show` | same WIT, no new pose. | `FABRIC + STITCHING + HINGE` | Fabric direct; hinge only reference. | Compresses the list into one readable material beat. |
| 3 | `0:09.8-0:16.2 estimated` | `battery... normal screwdriver... secret handshake` | 2 | Hard cut to screwdriver background. Generic device outline sits over the table. One label says `REPAIRABLE`. Tiny red cross-out can hit `SECRET HANDSHAKE` only if it stays readable. | Repair table background. | `hard-show`, optional small `impact` cross-out | No WIT; let the table and label breathe. | `REPAIRABLE`; optional `not secret handshake` | Screwdriver direct background; generic CSS device. | Turns battery/tools into one repairability idea. |
| 4 | `0:16.2-0:20.5 estimated` | `spare part... after factory` | 2 | Small drawer/part tag appears near device: `SPARE PART STILL EXISTS`. | Same repair table. | `hard-show` | No WIT. | `SPARE PART STILL EXISTS` | CSS drawer/tag. | Names the support idea without adding another full scene. |
| 5 | `0:20.5-0:28.8 estimated` | `not glamorous... already repairing a printer` | 2 | Same repair table becomes a printer bench with a generic printer silhouette. Giant thinking WIT appears behind/left. Quote bubble: `Wow. Long-term parts.` | Repair table background holds. | `hard-show` | `wit-pose-thinking.png`, 1/3 to 1/2 frame emotional read, face above printer, no crop through glasses/head. | `Wow. Long-term parts.` | Generic CSS printer, no real printer photo direct. | Makes the dry aside funny without crowding the whole frame. |
| 6 | `0:28.8-0:37.867 estimated` | `Most people see... less future built into it` | 3 | Hard cut to cardboard/product box background. Label `LOOKS COMPLETE`, then final large stamp `LESS FUTURE BUILT IN`; betrayed WIT is huge on right. | Cardboard background and box silhouette. | `hard-show`; final stamp can `impact` | `wit-pose-betrayed.png`, 1/3 to 1/2 frame, clean face zone on right, stamp left/center. | `LOOKS COMPLETE`; `LESS FUTURE BUILT IN` | Cardboard direct background; CSS missing-future tag/box. | Final memory frame, clean and simple. |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop / Margin | Why WIT Is Needed |
|---|---:|---|---|---|---|---|
| 1-2 | `0:00-0:09.8` | suspicious inspector of boring material | `wit-pose-suspicious.png` | Giant left or lower-left, visible character about 1/3 frame; can overlap photo edge but not labels. | Face, glasses, head, shoulders fully readable. | Gives boring material a human reaction. |
| 5 | `0:20.5-0:28.8` | the one person who cares about replacement parts | `wit-pose-thinking.png` | Giant behind/left of printer silhouette, about 1/3 to 1/2 frame. | Printer must stay below face line; quote must not cover eyes or mouth. | Lands the printer joke. |
| 6 | `0:28.8-0:37.867` | betrayed by a complete-looking product | `wit-pose-betrayed.png` | Giant right side, about 1/3 to 1/2 frame. | Final stamp stays left/center; no text over WIT face/expression. | Final emotional payoff. |

WIT density note:

- Total WIT beats: `3`
- WIT beats per big scene: `Scene 1: 1`, `Scene 2: 1`, `Scene 3: 1`
- Any big scene above `2` WIT beats, and why: `none`
- Cue states intentionally without WIT: `3`, `4`; repair information should breathe.

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion Type | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|---|
| 1 | `0:00-0:04.8` | `BORING FUTURE` | `static` | Fabric/material background. | Names the section idea in one phrase. | No list of all parts yet. |
| 2 | `0:04.8-0:09.8` | `FABRIC + STITCHING + HINGE` | `hard-show` | Material background. | Compresses three lines into one visual beat. | No separate cards, circles, or arrows. |
| 3 | `0:09.8-0:16.2` | `REPAIRABLE`; optional crossed `SECRET HANDSHAKE` | `hard-show` / small `impact` | Generic device and tool area. | Keeps battery/tool idea simple. | No real brand phone/device marks. |
| 4 | `0:16.2-0:20.5` | `SPARE PART STILL EXISTS` | `hard-show` | Small part drawer/tag. | Shows long-term support as a physical small part. | No policy/legal board. |
| 5 | `0:20.5-0:28.8` | `Wow. Long-term parts.` | `hard-show` | Quote bubble near giant WIT/printer. | Makes the dry aside readable. | Do not add a cluttered printer workshop. |
| 6 | `0:28.8-0:37.867` | `LOOKS COMPLETE`; `LESS FUTURE BUILT IN` | `hard-show`; final `impact` | Product box/cutaway. | Lands the memory frame. | Do not add `shape/color/price/arrives tomorrow` as four separate labels unless review asks. |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|
| Sewing machine stitching fabric | `real image` | Pexels, shoreline vehicles | Direct background / material texture for Scene 1. | Safe asset candidate; no brand dependency. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-sewing-machine-stitching-fabric-pexels-shoreline-vehicles.jpg` |
| Screwdriver bits | `real image` | Pexels, Roseson Studios | Direct background / repair table texture for Scene 2. | Safe asset candidate. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-screwdriver-bits-pexels-roseson-studios.jpg` |
| Cardboard boxes | `real image` | Pexels, Harper Sunday | Direct background / complete outside texture for Scene 3. | Safe asset candidate. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-cardboard-boxes-pexels-harper-sunday.jpg` |
| Phone repair photo | `real image` | Pexels, Harry Tucker | Reference only for generic open device. | Mockup target only; do not expose Apple/device marks/UI text. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-phone-battery-repair-pexels-harry-tucker.jpg` |
| Printer repair photo | `real image` | Pexels, Bulat843 | Inspiration only for generic printer bench. | Do not use directly due person/text/clutter. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-printer-repair-pexels-bulat843.jpg` |
| WIT poses | `local channel asset` | Project WIT manifest | Direct WIT overlays. | Safe channel asset. | `assets/wit/wit-pose-suspicious.png`, `assets/wit/wit-pose-thinking.png`, `assets/wit/wit-pose-betrayed.png` |

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|
| Fabric photo | Scene 1, cues 1-2 | Material texture for boring future. | `0:00-0:09.8` | Full-frame background with overlay only where labels sit. | Direct background. | `safe direct asset` |
| Screwdriver photo | Scene 2, cues 3-5 | Repair table texture and tool clarity. | `0:09.8-0:28.8` | Full-frame background; device/printer CSS overlays on top. | Direct background. | `safe direct asset` |
| Cardboard photo | Scene 3, cue 6 | Complete-looking product/package texture. | `0:28.8-0:37.867` | Full-frame background; final label left/center, WIT right. | Direct background. | `safe direct asset` |
| Phone repair photo | Scene 2 planning only | Open-device layout. | Not on screen. | None. | Used mentally to build generic device. | `mockup target only` |
| Printer repair photo | Scene 2 planning only | Repair-bench joke reference. | Not on screen. | None. | Used mentally to build generic printer silhouette. | `inspiration only` |
| WIT poses | Cues 1, 5, 6 | Emotional rhythm. | 3 WIT beats. | Giant edge/side placements, face safe. | Direct PNG overlay. | `safe channel asset` |

## HyperFrames Guidance

- Composition target: `simple Section-1-style 16:9 preview using 3 real photo backgrounds, sparse labels, generic CSS overlays, and giant WIT emotional beats`
- Big scene count: `3`
- Cue state count: `6`
- Scene components: `PhotoBackground`, `LargeWIT`, `ShortHandwrittenLabel`, `GenericDeviceOverlay`, `GenericPrinterOverlay`, `SimpleBoxCutaway`, `FinalStamp`
- Timing notes: `Keep backgrounds persistent. Do not cut for every product part. Let WIT and one label carry each beat.`
- Motion density rule: `static hard cuts; ordinary labels hard-show; final stamp may impact`
- Text style: `very short labels; no paragraphs except the short quote`
- Asset paths: `assets/section-04/fabric.jpg`, `assets/section-04/screwdriver.jpg`, `assets/section-04/cardboard.jpg`, `assets/wit/`
- Audio sync notes: `BORING FUTURE on opening; material label on fabric/stitching/hinge; REPAIRABLE on battery/screwdriver; SPARE PART STILL EXISTS on spare part; quote on printer joke; final stamp on less future built into it`
- WIT pose files: `wit-pose-suspicious.png`, `wit-pose-thinking.png`, `wit-pose-betrayed.png`
- WIT density: `3 total beats`
- WIT scale and crop guards: `aim for visible WIT emotion around 1/3 to 1/2 frame; face/head/shoulders/glasses never cropped; final text must not cover WIT face`
- No-WIT breathing beats: `3`, `4`
- Suggested inspect timestamps: `0.8s`, `5.8s`, `11.8s`, `18.0s`, `24.8s`, `31.8s`, `36.8s`
- Suggested screenshot/contact-sheet QA timestamps: `0.8s`, `6.0s`, `12.0s`, `18.6s`, `25.4s`, `32.4s`, `36.9s`
- Suggested MP4 QA frame timestamps, only if export is explicitly requested: `none; export not requested`
- Build risks: `making labels too numerous again, letting background photo fight text readability, making WIT small because of PNG padding, final stamp covering WIT face`
- Must not invent: `new crowded parts tray, extra mini cards, extra full-scene cuts, direct phone/printer photo usage, fake WIT, MP4 export`

## Review-Prevention Checklist

- voice sync mapped to phrase cues: `yes`
- big-scene rhythm avoids unrelated rapid boards: `yes, 3 persistent backgrounds`
- cue density stays readable: `yes, 6 cue states for 37.867s`
- motion density uses hard-show by default: `yes`
- impact motion reserved for emphasis: `yes, final stamp only, optional small cross-out`
- WIT rhythm not overused: `yes, 3 total WIT beats`
- WIT size readable: `yes, plan requires 1/3-1/2 frame emotional read`
- WIT crop safe: `yes`
- WIT does not cover text/evidence: `yes, separate label and WIT zones`
- red markup targets exact objects: `yes, only optional secret-handshake cross-out and final stamp`
- scene bases visually differentiated: `yes, fabric photo, repair table photo, cardboard photo`
- subtitle-safe lower layout: `yes, final label kept left/center and above bottom zone`
- render does not need to invent timing/layout/assets: `yes`

## Approval Checks

- visual reference pass completed: `yes, existing Section 4 references reused and reclassified for a simpler remake`
- what/when/how clear: `yes`
- big scenes grouped, not one full scene per sentence: `yes`
- cue states low enough for section duration: `yes`
- attention reason per big scene / cue state: `yes`
- label readable: `yes`
- WIT has a clear job: `yes`
- WIT pose files named: `yes`
- WIT facial emotion large enough: `yes`
- WIT face/head/shoulder crop safe: `yes`
- WIT density counted and justified: `yes`
- no-WIT breathing beats planned: `yes`
- red markup points to exact object: `yes`
- ordinary labels hard-show unless emphasis needs impact motion: `yes`
- impact animation reserved for emphasized spoken beats: `yes`
- real-life asset explains, not decorates: `yes`
- title-thumbnail promise still being paid off: `yes, future removed from product`
- safe for English learners: `yes, fewer words and clearer repeated labels`
- ready for HyperFrames: `yes`
