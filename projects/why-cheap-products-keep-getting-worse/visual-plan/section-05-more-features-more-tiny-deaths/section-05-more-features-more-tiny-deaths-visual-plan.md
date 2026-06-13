# Section 5 Visual Plan

Video:
`Why Cheap Products Keep Getting Worse`

Section:
`Section 5: More Features, More Tiny Deaths`

Status:
`draft visual plan for approval`

## Section Goal

Explain that extra features can be useful and still create more failure points. The viewer should not hear "old products were always better" or "technology is bad." They should see a fair tradeoff: more useful parts can also mean more tiny ways for the product to fail and become expensive to fix.

## Source Inputs

- Script: `02-script.md`, `Section 5: More Features, More Tiny Deaths`
- Voiceover: `voiceover/section-05-more-features-more-tiny-deaths/scratch-audio/section-05-more-features-more-tiny-deaths-david23-am_eric-0.84.mp3`
- Script promise: `extra complexity can add useful value while quietly adding future repair risk`
- Section duration: `34.645s`

## Narration

```text
The second reason is that products can get more complicated.

This is not automatically bad.

Useful features are useful.

A safer appliance is good.

A better battery is good.

A phone that survives gravity is basically a public service.

But every extra feature is also one more thing that can break.

A simple fridge has one main job:

be cold.

A modern fridge may have screens, sensors, water lines, ice dispensers, software, and opinions.

At some point, the product is not just a product.

It is a small technology committee living in your kitchen.

And when one tiny part fails, the whole thing can become harder and more expensive to fix.
```

## Visual Direction

- Big-scene/cue rhythm: `3 persistent scenes, 8 cue states`
- Big scene rhythm: `fair useful-feature setup -> fridge feature pile-up -> technology committee failure`
- Cue-state count: `8`
- Main visual metaphor: `a simple appliance gains useful helpers until it becomes a committee with many tiny failure points`
- WIT emotional path: `suspicious but fair -> overwhelmed by opinions -> facepalm at one tiny part failing`
- WIT density: `3 total WIT beats, one per big scene`
- Motion density: `hard cuts between scenes; ordinary labels hard-show; only "ONE MORE BREAK POINT" and "TINY PART FAILS" can use impact`
- Real-life texture: `generic fridge silhouette, water-dispenser feature detail, worn control-panel buttons, appliance circuit-board density`
- Real image references: `4 Wikimedia Commons references saved locally and classified; mostly mockup targets, not direct production images`
- Generated/support assets: `none needed; final frames should be generic HyperFrames-built mockups for clean labels and no brand risk`
- Viewer attention strategy: `start fair, then make the feature pile visually funny, then make the final failure point painfully small`
- Retention risk: `the feature list can become a busy product spec sheet`
- Visual fix: `group features into one modern-fridge panel and one committee board instead of giving every noun a separate card`
- Red markup: `one failure-point mark in Scene 2, one precise red circle/cross on the tiny failed part in Scene 3`
- Motion rule: `labels hard-show on voice cues; no fly-in parade; WIT enters large only on emotional beats`

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|
| 1. Useful features are not the villain | `0:00-0:10.6 estimated` | `The second reason... public service.` | Clean neutral board with a generic appliance/phone feature shelf: `safer appliance`, `better battery`, `survives gravity`. Large thinking/suspicious WIT watches from left but does not look angry. | Makes the claim fair before the section turns into a joke about complexity. | Cut when the narration pivots to `every extra feature`. | Water-dispenser reference for useful feature reality, control-panel reference for appliance detail, WIT manifest. | Build in HyperFrames; references R2/R4 from `reference-board.md` are mockup/inspiration only. |
| 2. Simple fridge versus feature pile | `0:10.6-0:25.8 estimated` | `But every extra feature... and opinions.` | Split scene: left simple fridge labeled `ONE JOB: BE COLD`; right modern no-logo fridge gains one grouped feature stack: `screens + sensors + water + ice + software`. The right fridge gets a tiny opinion bubble. | Turns feature complexity into one readable comparison and one joke. | Cut after `and opinions` lands. | Domestic fridge silhouette, water-dispenser shape, appliance control-panel texture. | Build in HyperFrames; use `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/` only as reference. |
| 3. Tiny part, whole committee problem | `0:25.8-0:34.645 estimated` | `At some point... expensive to fix.` | Generic appliance circuit board becomes a "technology committee" table inside a kitchen-fridge outline. One tiny chip/valve gets circled red; a small repair tag appears. Giant facepalm WIT owns the emotional zone on the right. | Pays off the section: the problem is not features themselves, it is dependency and repair complexity. | End hold. | Appliance power-module reference for small-part density, control-panel texture, WIT manifest. | Build generic board in HyperFrames; optional R3 crop only if attribution is recorded by render. |

## Cue State Timeline

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | Motion Type | WIT Pose / Size / Safe Crop | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|---|
| 1 | `0:00-0:03.8 estimated` | `products can get more complicated / not automatically bad` | 1 | Clean board appears with a generic appliance icon and correction label `COMPLICATED != BAD`. Large WIT appears as a fair inspector on left. | Neutral background and feature shelf. | `static` | `wit-pose-thinking.png`, left third, visible WIT footprint at least `1/3` frame; face/head/shoulders safe. | `COMPLICATED != BAD` | CSS appliance/phone icons. | Prevents the section from sounding anti-technology. |
| 2 | `0:03.8-0:08.9 estimated` | `Useful features... safer appliance... better battery` | 1 | Two green check labels hard-show: `SAFER` and `BETTER BATTERY`. Optional small battery icon. | WIT and neutral feature shelf hold. | `hard-show` | Same WIT, no new pose. | `SAFER`; `BETTER BATTERY` | Generic CSS icons; R2/R4 for reference only. | Shows the positive side without adding a new scene. |
| 3 | `0:08.9-0:10.6 estimated` | `phone that survives gravity... public service` | 1 | A generic phone icon lands safely on a tiny pillow/airbag. Label `SURVIVES GRAVITY` appears. | Fair setup board. | `hard-show` | Same WIT, no new pose. Keep phone label away from WIT face. | `SURVIVES GRAVITY` | CSS phone and pillow. | Makes the deadpan public-service joke visual. |
| 4 | `0:10.6-0:14.2 estimated` | `every extra feature... one more thing that can break` | 2 | Hard cut to split fridge scene. A red tag hits the modern side: `ONE MORE BREAK POINT`. | Simple fridge left, modern fridge right. | `impact` for red tag, otherwise `hard-show` | No new WIT; let the comparison breathe. | `ONE MORE BREAK POINT` | CSS fridges. | Names the section thesis in one clean visual beat. |
| 5 | `0:14.2-0:17.6 estimated` | `A simple fridge has one main job: be cold.` | 2 | Left fridge gets a large calm label `ONE JOB: BE COLD`; modern side stays present but muted. | Split scene. | `hard-show` | No WIT. | `ONE JOB: BE COLD` | CSS simple fridge. | Gives the viewer a simple memory anchor. |
| 6 | `0:17.6-0:25.8 estimated` | `modern fridge may have screens... software... and opinions` | 2 | Modern fridge feature stack hard-shows as one grouped label: `SCREEN + SENSOR + WATER + ICE + SOFTWARE`. On `and opinions`, giant confused WIT drops from the top-right edge or peeks from behind the modern fridge; fridge bubble says `I HAVE THOUGHTS`. | Split fridge scene and simple-fridge label. | `hard-show`; optional tiny `impact` on `OPINIONS` only | `wit-pose-confused.png`, top-right or behind-fridge peek, visible WIT at least `1/3` frame; do not crop face/glasses/head/shoulders. | `SCREEN + SENSOR + WATER + ICE + SOFTWARE`; `I HAVE THOUGHTS` | CSS modern fridge/panel; R1/R2/R4 as references. | Compresses the list and lands the opinions joke without making a spec sheet. |
| 7 | `0:25.8-0:30.0 estimated` | `not just a product... small technology committee` | 3 | Hard cut to generic circuit-board committee scene inside a fridge outline. Tiny icons sit around a boardroom table. Label `TECHNOLOGY COMMITTEE` appears. | Circuit-board/committee base. | `hard-show` | No WIT for the first committee reveal; keep the board readable. | `TECHNOLOGY COMMITTEE` | CSS circuit board/committee table based on R3. | Turns the joke into one paused-frame metaphor. |
| 8 | `0:30.0-0:34.645 estimated` | `one tiny part fails... harder and more expensive to fix` | 3 | Red circle targets one tiny chip/valve. Labels hard-show: `TINY PART FAILS` then `WHOLE THING HARD TO FIX`. Giant facepalm WIT appears on right; small repair-cost tag stays left/center. | Committee/circuit base holds. | `impact` on red circle; labels `hard-show` | `wit-pose-facepalm.png`, right side, visible WIT `1/3-1/2` frame; repair tag and labels must not cover face, glasses, head, shoulders, or hand. | `TINY PART FAILS`; `WHOLE THING HARD TO FIX`; optional `repair cost: rude` | CSS tiny chip/valve, generic repair tag. | Final memory frame: a small failure can make the whole product painful to fix. |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop / Margin | Why WIT Is Needed |
|---|---:|---|---|---|---|---|
| 1-3 | `0:00-0:10.6` | fair inspector, not anti-tech | `wit-pose-thinking.png` | Left third, large but calm, visible WIT at least `1/3` frame. | Face, glasses, head, shoulders fully visible. Labels sit center/right. | Keeps the section fair before the critique begins. |
| 6 | `0:17.6-0:25.8` | overwhelmed by feature pile and fridge opinions | `wit-pose-confused.png` | Top-right upside-down entrance or side peek from behind modern fridge, visible WIT at least `1/3` frame. | Intentional edge peek is okay, but no crop through face, glasses, head, shoulders, or mouth. Opinion bubble must not cover WIT face. | Lands the absurd `and opinions` beat. |
| 8 | `0:30.0-0:34.645` | facepalm at tiny failure becoming expensive | `wit-pose-facepalm.png` | Right side, `1/3-1/2` frame visible footprint; WIT is the emotional subject. | Keep final labels and repair tag left/center; no text over face, glasses, or hand. | Gives the final repair-cost pain a human reaction. |

WIT density note:

- Total WIT beats: `3`
- WIT beats per big scene: `Scene 1: 1`, `Scene 2: 1`, `Scene 3: 1`
- Any big scene above `2` WIT beats, and why: `none`
- Cue states intentionally without WIT: `4`, `5`, `7`; these are comparison and committee mechanics that need visual breathing room.

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion Type | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|---|
| 1 | `0:00-0:03.8` | `COMPLICATED != BAD` | `static` | Generic feature shelf. | Makes the safe claim visible. | Do not cross out technology or modern products. |
| 2 | `0:03.8-0:08.9` | `SAFER`; `BETTER BATTERY` | `hard-show` | Useful feature icons. | Shows that features can be good. | No long explanation text. |
| 3 | `0:08.9-0:10.6` | `SURVIVES GRAVITY` | `hard-show` | Generic phone landing safely. | Makes the public-service joke concrete. | No real phone brand or app UI. |
| 4 | `0:10.6-0:14.2` | `ONE MORE BREAK POINT` | `impact` | Modern fridge feature side. | Names the tradeoff. | Do not label every feature separately. |
| 5 | `0:14.2-0:17.6` | `ONE JOB: BE COLD` | `hard-show` | Simple fridge. | Clean memory frame. | Do not imply old products are always better. |
| 6 | `0:17.6-0:25.8` | `SCREEN + SENSOR + WATER + ICE + SOFTWARE`; `I HAVE THOUGHTS` | `hard-show`; optional small `impact` on `OPINIONS` | Modern fridge feature panel and speech bubble. | Compresses the list and lands the joke. | No scattered mini-card tray, no real logos, no real UI screenshots. |
| 7 | `0:25.8-0:30.0` | `TECHNOLOGY COMMITTEE` | `hard-show` | Boardroom/circuit scene. | Makes the metaphor visible. | Do not create many unreadable committee labels. |
| 8 | `0:30.0-0:34.645` | `TINY PART FAILS`; `WHOLE THING HARD TO FIX`; optional `repair cost: rude` | red circle `impact`; labels `hard-show` | One tiny chip/valve and generic repair tag. | Final payoff and repair-cost setup for next section. | Do not put the repair tag in the subtitle zone or over WIT face. |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|
| Domestic refrigerator photo | `real image` | Wikimedia Commons, Infrogmation of New Orleans, CC BY-SA 4.0 | Fridge silhouette and home context reference for Scene 2. | Mockup target only due visible brand and page-level failure claim. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-domestic-refrigerator-commons-infrogmation.jpg` |
| Water-dispenser refrigerator photo | `real image` | Wikimedia Commons, Dave Matos, CC BY-SA 2.0 | Useful dispenser feature reference for Scene 1/2. | Inspiration/mockup only due visible logos, stickers, and real hand/photo clutter. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-water-dispenser-refrigerator-commons-dave-matos.jpg` |
| Appliance power module photo | `real image` | Wikimedia Commons, Phiarc, CC BY-SA 4.0 | Circuit-board/failure-point reference for Scene 3. | Mockup target; optional direct crop only with attribution and no brand/product claim. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-appliance-power-module-commons-phiarc.jpg` |
| Appliance control panel photo | `real image` | Wikimedia Commons, Solomon203, CC BY-SA 4.0 | Button/panel texture and feature density reference. | Inspiration only due visible brand and text. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-control-panel-commons-solomon203.jpg` |
| WIT poses | `local channel asset` | Project WIT manifest | Direct WIT overlays. | Safe channel asset. | `assets/wit/wit-pose-thinking.png`, `assets/wit/wit-pose-confused.png`, `assets/wit/wit-pose-facepalm.png` |
| Generic fridge/feature/committee elements | `self-made HyperFrames mockup` | Built from script and references | Direct production objects for all scenes. | Safest route because no logos, no private data, exact label control. | Build in HTML/CSS; no generated image required. |

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|
| Domestic fridge reference | Scene 2 planning | Fridge proportions, handle placement, kitchen scale. | Not visible directly. | None. | Translate into generic CSS fridge silhouette. | `mockup target` |
| Water-dispenser reference | Scenes 1-2 planning | Useful feature shape: dispenser cavity, water/ice module. | Not visible directly. | None. | Translate into generic no-logo dispenser icon on modern fridge. | `inspiration only / mockup target` |
| Control panel reference | Scenes 1-3 planning | Button spacing, worn appliance texture, feature-panel feel. | Not visible directly. | None. | Translate into generic buttons/icons and committee board. | `inspiration only` |
| Power-module reference | Scene 3, cues 7-8 | Circuit-board density, many tiny parts, one targetable failure point. | Not visible directly by default. | If direct crop is later chosen, crop tightly to remove labels and record attribution. | Prefer generic CSS board; direct crop optional only after render attribution check. | `mockup target / optional direct texture` |
| Generic feature shelf | Scene 1, cues 1-3 | Fair positive-feature setup. | `0:00-0:10.6` | Center/right label zone, WIT left. | CSS icons/cards. | `self-made safe asset` |
| Generic split fridges | Scene 2, cues 4-6 | Main comparison: one job versus feature pile. | `0:10.6-0:25.8` | Left simple fridge, right modern fridge, labels above subtitle zone. | CSS/HTML illustration. | `self-made safe asset` |
| Generic technology committee board | Scene 3, cues 7-8 | Product as committee and tiny failure point. | `0:25.8-0:34.645` | Board/committee left/center; WIT right. | CSS/HTML illustration using circuit-board texture logic. | `self-made safe asset` |
| WIT poses | Cues 1-3, 6, 8 | Emotional clarity and dry humor. | Three WIT beats. | Large creative placements, at least `1/3` visible frame footprint. | Direct PNG overlay. | `safe channel asset` |

## HyperFrames Guidance

- Composition target: `Section-1-style sparse 16:9 explainer section with 3 persistent scenes, generic self-made appliance graphics, and giant WIT emotional beats`
- Big scene count: `3`
- Cue state count: `8`
- Scene components: `FeatureShelf`, `GenericSimpleFridge`, `GenericModernFridge`, `FeatureStack`, `OpinionBubble`, `TechnologyCommitteeBoard`, `TinyFailureMark`, `LargeWIT`, `ShortHandwrittenLabel`
- Timing notes: `Use 34.645s audio. Timings are estimated from marked script pauses. Give "and opinions" a distinct small beat and hold final failure frame through the end.`
- Motion density rule: `hard cuts between big scenes; ordinary labels hard-show; impact only for ONE MORE BREAK POINT and TINY PART FAILS`
- Text style: `short handwritten labels; no product-spec paragraphs; keep all cue-critical text above subtitle-safe lower area`
- Asset paths: `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/`, `assets/wit/`
- Audio sync notes: `COMPLICATED != BAD on opening correction; green feature labels on useful features; ONE MORE BREAK POINT on the pivot; ONE JOB: BE COLD on simple fridge line; I HAVE THOUGHTS on and opinions; TECHNOLOGY COMMITTEE on committee joke; TINY PART FAILS on final failure line`
- WIT pose files: `wit-pose-thinking.png`, `wit-pose-confused.png`, `wit-pose-facepalm.png`
- WIT density: `3 total beats, one per big scene`
- WIT scale and crop guards: `each emotional WIT beat must occupy at least 1/3 visible frame area; never crop face, glasses, head, shoulders, mouth, or facepalm hand; keep labels and repair tag away from WIT face`
- No-WIT breathing beats: `4`, `5`, `7`
- Suggested inspect timestamps: `0.8s`, `4.8s`, `9.8s`, `12.6s`, `16.2s`, `22.6s`, `27.4s`, `31.8s`, `34.1s`
- Suggested screenshot/contact-sheet QA timestamps: `0.8s`, `5.0s`, `10.0s`, `12.8s`, `16.4s`, `22.8s`, `27.6s`, `32.0s`, `34.2s`
- Suggested MP4 QA frame timestamps, only if export is explicitly requested: `none; export not requested`
- Build risks: `making a feature spec sheet, implying old/simple always means better, using real brand images directly, shrinking WIT below 1/3 frame, opinion bubble covering WIT face, final repair tag entering subtitle zone`
- Must not invent: `real brand appliance screenshots, extra feature cards beyond the grouped stack, anti-technology framing, new WIT drawings, additional product categories, MP4 export`

## Review-Prevention Checklist

- voice sync mapped to phrase cues: `yes`
- big-scene rhythm avoids unrelated rapid boards: `yes, 3 persistent scenes`
- cue density stays readable: `yes, 8 cue states for 34.645s`
- motion density uses hard-show by default: `yes`
- impact motion reserved for emphasis: `yes, pivot/failure marks only`
- WIT rhythm not overused: `yes, 3 total WIT beats`
- WIT size readable: `yes, every WIT beat requires at least 1/3 visible frame footprint`
- WIT crop safe: `yes`
- WIT does not cover text/evidence: `yes, separate label zones and WIT zones`
- red markup targets exact objects: `yes, modern feature side and one tiny failed part`
- scene bases visually differentiated: `yes, fair feature board, split fridge scene, circuit-board committee`
- subtitle-safe lower layout: `yes, important labels and repair tag stay above lower subtitle zone`
- render does not need to invent timing/layout/assets: `yes`

## Approval Checks

- visual reference pass completed: `yes, project-local browse failed, global gstack browse succeeded, 4 Wikimedia references saved and classified`
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
- real-life asset explains, not decorates: `yes, references guide generic objects`
- title-thumbnail promise still being paid off: `yes, future risk appears as tiny failures and repair difficulty`
- safe for English learners: `yes, repeated simple labels and concrete appliance example`
- ready for HyperFrames: `yes`
