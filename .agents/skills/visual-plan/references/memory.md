# Visual Plan Skill Memory

This file stores memory specific to the `visual-plan` skill.

Use `.agents/_shared/` for channel-wide visual systems, WIT identity, HyperFrames grammar, reference safety rules, and reusable production lessons.
Use this file for section-selection behavior, section visual-plan output shape, reference-board habits, asset planning notes, and lessons about making plans easier to build in HyperFrames.

> ## 2026-06-28 REBUILD NOTE (read first)
>
> `visual-plan` was rebuilt this date. The CANONICAL behavior is now in `SKILL.md`:
> ONE master plan + synced per-section copies; per-sentence scenes; an extreme-detail scene spec
> (composition, elements, mascot pose, on-screen text, emotion, insight, linkage, show-as-you-say
> timing, sound, color); and an ASSET list per scene (type generate/browse/screenshot/reuse, filename,
> layout). The plan DESCRIBES only - it never writes image-generation prompts (that is now
> `visual-implement`) - and imagination is unbounded (within copyright/law/YouTube community standards),
> so it may invent new poses/scenes, not just reuse the pose library. Asset creation moved to
> `visual-implement`; render now COMPOSITES pre-made assets.
>
> The "Current Skill Standard" / "Output Standard" sections below and the older feedback entries
> describe the PREVIOUS big-scene/cue-state HyperFrames-handoff era. Keep them as historical reference;
> the still-valid creative lessons (real/real-looking base per scene, vivid imagery, vary everything,
> mascot big-and-high with real personality, no stacked text, subtitle-safe layout, public-figure
> safety) carry forward and now live in `SKILL.md` + the shared docs. Where they conflict with the
> rebuilt `SKILL.md`, `SKILL.md` wins.

## Current Skill Standard

- Run after `voiceover`.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, `02-script.md`, and the voiceover index (`03-voiceover.md`; legacy `04-voiceover.md` - resolve by suffix per `.agents/rules/video-workflow.md`).
- Packaging is outside the main pipeline and must not block visual planning.
- If voiceover is older than script, stop and ask for `voiceover`.
- Require matching section voiceover output for each selected section.
- Require the user to explicitly select `All` or a specific section before creating or editing visual-plan files.
- Put `All` at the top of section choices.
- Interpret `All` as separate visual-plan outputs for every section, not one giant full-video board table.
- Write the visual-plan index (`04-visual-plan.md`; legacy `05-visual-plan.md`) as the project-level visual-plan index.
- Write section details under `visual-plan/section-XX-kebab-section-name/`.
- Put section reference images or generated references under `assets/visual-references/section-XX-kebab-section-name/`.
- Act as a professional editor and content creator: decide what appears on screen, when it appears, how it reveals or moves, and why the viewer keeps watching.
- Treat visual planning as the critical HyperFrames handoff. HyperFrames should not need to invent the main scene, timing, joke, asset list, or reference logic.
- Plan with `big scenes` and `cue states`, not disconnected sentence-by-sentence boards.
- For `20-25s` hooks, default to about `3` big scenes and `6-8` cue states unless the script truly needs more.
- Run a visual differentiation check before handoff: non-callback big scenes should not reuse the same background, object arrangement, camera language, or material mood. Reuse a base only for purposeful continuity or payoff memory.
- Every cue state needs a reason: clarity, evidence, emotion, joke, reveal, or payoff.
- Red markup must mean something and target a specific object. Decorative or obvious marks should be removed.
- WIT appearances must name exact approved PNG pose files and be large enough for facial emotion to read.
- Plan a subtitle-safe lower area. Important lower-third labels, receipts, stamps, arrows, boxes, and payoff props should usually sit a bit above the bottom subtitle zone so YouTube captions do not cover them.
- Every selected section must run a visual reference pass before finalizing the plan.
- Real internet, self-shot, or existing local images are the default first layer for the reference pass because they make the video feel closer to the viewer.
- Generated images are support assets, controlled mockups, cleanup/fallback images, or composition tests after real references are understood.
- Collected references can be inspected and skipped. Do not plan direct use of an image merely because it was downloaded or generated; mark it reference-only, fallback, inspiration, or reject when it does not improve the end viewer result.
- If a section uses zero real images, the reference board must explain why real images were unavailable, unsafe, irrelevant, or lower quality than the generated/self-made alternative.
- Normal sections should include at least `3` useful references: one real-life/object/material reference, one composition or attention reference, and one HyperFrames-buildable asset/mockup reference.
- Hooks and high-retention moments should usually include `4-6` references unless the section is extremely simple.
- Prompt-only references are a degraded fallback, not the default, and must explain why browsing/generation/local inspection was unavailable or unsafe.
- Use real-life assets as evidence, not decoration.
- Classify references as `safe asset`, `mockup target`, `inspiration only`, or `reject`.
- Use the current WIT direction from shared memory.
- Stop before HyperFrames build, renders, review, upload, or self-learning.

## Output Standard

For each selected section, create or update:

- `visual-plan/section-XX-kebab-section-name/README.md`
- `visual-plan/section-XX-kebab-section-name/section-XX-kebab-section-name-visual-plan.md`
- `visual-plan/section-XX-kebab-section-name/reference-board.md`
- `assets/visual-references/section-XX-kebab-section-name/`
- the visual-plan index (`04-visual-plan.md`; legacy `05-visual-plan.md`)

The visual-plan index (`04-visual-plan.md`; legacy `05-visual-plan.md`) should act as the project-level index for generated and not-yet-generated section visual plans.

Each section visual plan must include:

- a clear editor brief
- viewer attention strategy
- retention risk and visual fix
- scene-level what / when / how plan
- cue-state timing mapped to voiceover
- visual resource usage map with what / when / how / where for each important asset
- WIT pose plan with exact pose files and placement/scale guidance
- markup and label plan with exact target objects
- reference and asset plan with source status
- HyperFrames guidance that names what the renderer must not invent and suggests inspect plus screenshot/contact-sheet QA timestamps

## Feedback Log

### 2026-06-07 - Skill Created

Classification: `Core operational capability`

Context:
The user clarified that after voiceover, production branches by section. Each section should move through visual plan and later build/review steps independently.

Lesson:
Visual planning must be section-first. It should ask which project and which section to plan, include `All` as the first option, and produce separate section visual-plan outputs.

Apply next time:
Use the section list from `02-script.md`, verify matching voiceover section output (`03-voiceover.md`; legacy `04-voiceover.md`), and do not infer the target section from existing work.

Promote to shared memory:
Yes, as an operational production lesson.

### 2026-06-07 - Packaging Outside Main Pipeline Freshness

Classification: `Operational lesson`

Context:
The user clarified that packaging is outside the main pipeline and branches from Research Pack.

Lesson:
Visual planning must validate the main chain: topic intake -> research pack -> script -> voiceover. `03-packaging.md` must not be required and must not make visual planning stale.

Apply next time:

- stop if research is older than topic intake
- stop if script is older than topic intake or research pack
- stop if voiceover or the selected section voiceover is older than script

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-07 - Visual Plan Must Be Editor-Grade

Classification: `Visual plan lesson`

Context:
The user clarified that visual planning is the most important channel skill because HyperFrames depends on it. A text-only plan can be too weak even when the objects seem simple.

Lesson:
Visual planning must be performed from the role of a professional editor and content creator. For each scene, the skill must define what appears on screen, when it appears, how it changes, why it holds attention, and what visual assets or references are needed. Browsed, generated, or inspected local references are required for normal runs; prompt-only is only a degraded fallback.

Apply next time:

- run a visual editor pass before writing boards
- run a visual reference pass before finalizing the plan
- include `Scene What-When-How Plan`
- include attention / joke reason per board
- include browsed/generated/local reference status
- tell HyperFrames what not to invent

Promote to shared memory:
no for now; this is implemented as visual-plan skill behavior. Promote later if render results prove the standard improves production quality.

### 2026-06-07 - Reject Crude Diagram References For Production Visual Planning

Classification: `Visual plan lesson`

Context:
The user rejected the first Section 1 visual references for `Why Cheap Products Keep Getting Worse` because the generated contact sheet and SVG references looked ugly, crude, and below the accepted `Why Everyone Pretends To Be Busy` asset quality bar.

Lesson:
Visual references for this channel should usually look like polished real-world or real-looking production references, not rough SVG diagrams. Use real-world photos, real-world crops, and high-quality contact sheets as the main visual reference layer. Use generated realistic assets as support when a controlled, clean, safe production base is needed. SVG/vector references are acceptable only for simple overlay mechanics, WIT, labels, red marks, or when the user explicitly wants a diagram style.

Apply next time:

- inspect accepted prior-video assets before matching a visual style
- prefer safe real-world photos first, then realistic generated support images when needed
- keep generated images free of text/logos and add labels in HyperFrames
- mark crude diagram references as rejected if they are only placeholders
- do not leave rejected ugly references in the active `assets/visual-references/` folder

Promote to shared memory:
no for now; keep as visual-plan execution memory unless future renders confirm this should become a channel-wide visual-production rule.

### 2026-06-07 - Real Internet Images Before Generated Images

Classification: `Visual plan lesson`

Context:
The user clarified that generated images alone make the visual plan feel less close to the viewer. Real images explored on the internet should be prioritized because they carry familiar texture, mess, lighting, and ordinary-life detail that generated images often smooth away.

Lesson:
Visual planning should start with real, sourced internet images, self-shot photos, or inspected local assets whenever the section has real-world objects. Generated images should support the plan, fill safe-asset gaps, remove source/logos/private-data risk, or provide controlled composition only after real references define what the scene should feel like.

Apply next time:

- browse/search for real object and material images first
- download or link real references only with source/license notes
- classify each real image as `safe asset`, `mockup target`, `inspiration only`, or `reject`
- use generated images as support/fallback, not the default main layer
- explain in `reference-board.md` when no real images are used

Promote to shared memory:
yes, this affects the channel-wide visual reference standard.

### 2026-06-07 - Every Visual Resource Needs What-When-How-Where

Classification: `Visual plan lesson`

Context:
The user asked whether the visual-plan run decided what, when, how, and where each visual resource is used in the section video.

Lesson:
Big scene and cue-state plans are not enough if individual assets remain ambiguous. Each important visual resource needs a usage map: what it contributes, when it appears, how it is animated or transformed, where it sits or crops on screen, and whether it is a direct asset, mockup target, support base, inspiration only, or rejected.

Apply next time:

- include `Visual Resource Usage Map` in every section visual plan
- map each important resource to boards and local time ranges
- name crop/placement and overlay relationship
- tell HyperFrames what not to use directly

Promote to shared memory:
no; keep as visual-plan output contract unless repeated render failures show this belongs channel-wide.

### 2026-06-09 - Render-Trustworthy Big Scene And Cue State Planning

Classification: `Visual plan lesson`

Context:
The user clarified that `render` is currently trusted more than `visual-plan` because weak visual plans produced foolish, unreliable renders. The approved Section 1 rebuild for `why-cheap-products-keep-getting-worse` proved the better pattern: use HyperFrames through render, but make visual-plan responsible for deciding what to show each second, sourcing/browsing references, generating support assets when needed, and handing render a trustworthy big-scene/cue-state plan.

Lesson:
Visual-plan must stop producing loose boards or mood boards. It must create render-ready plans: few persistent big scenes, low cue-state count, exact voice timing, real WIT pose filenames, meaningful labels/markup, real/generated asset decisions, and screenshot/contact-sheet QA timestamps. Render should be able to follow the plan without inventing the main scene, timing, WIT, markup, or asset logic.

Apply next time:

- create `Big Scene Plan` before cue details
- create `Cue State Timeline` with local start/end times and voice cue phrases
- for `20-25s` hooks, default to about `3` big scenes and `6-8` cue states
- group related narration into one persistent scene instead of one full-screen cut per sentence
- browse or inspect real/local references for each big scene before generating support images
- generate text-free/logo-free support images only after real references define the scene
- choose exact WIT PNG pose filenames and size/placement guidance
- remove decorative or meaningless red markup from the plan
- include suggested `inspect --at` timestamps and screenshot/contact-sheet QA timestamps for render; include MP4 QA frame timestamps only when export is explicitly requested

Promote to shared memory:
no; keep as visual-plan execution memory unless multiple future sections confirm it as a channel-wide production rule.

### 2026-06-09 - End-State Self-Check Before Handoff

Classification: `Visual plan lesson`

Context:
The user challenged the first Section 2 visual plan for `why-cheap-products-keep-getting-worse` because it used only real-world images and left the final comparison/cutaway mechanics for render to invent. The user asked for more careful self-checking and to think about the final viewer-facing result before finishing.

Lesson:
Real references are necessary but not always sufficient. Before finalizing a visual plan, run an end-state self-check: ask what the viewer should remember, which paused frame should carry the section, and whether render still has to invent any key scene base, object, metaphor, joke, or asset layout. If real images only provide texture but not the exact buildable scene, create or request generated/self-made support assets after the real-reference pass.

Apply next time:

- add an `End-State Self-Check` or equivalent internal pass before writing final plans
- identify the best paused frame and final viewer memory target
- treat generated images as support bases when they remove render ambiguity
- do not leave important scene bases as prompt-only if image generation is available and safe
- mark existing downstream render outputs stale when a section visual plan is materially improved

Promote to shared memory:
no for now; keep as visual-plan execution memory until this pattern improves multiple rendered sections.

### 2026-06-10 - Visual Differentiation And Skipped References

Classification: `Visual plan lesson`

Context:
In `why-cheap-products-keep-getting-worse` Section 3, the plan approved a generated visible-promises image as the Scene 3 base. During render review, the user noticed that Scene 3 looked too similar to Scene 1 because both used a warm tabletop product/tag background. The user also pointed out that not every collected reference image needs to be used.

Lesson:
Visual-plan must think through the end viewer result across the whole section, not only each scene in isolation. Non-callback big scenes need visual differentiation in background, object arrangement, camera language, color mood, or metaphor. References are evidence and options, not obligations; a good plan may inspect an image and deliberately skip it.

Apply next time:

- compare all big-scene base visuals before finalizing the section plan
- reuse a base only for purposeful callback, continuity, or payoff memory
- if two non-callback scenes look similar, create a distinct scene base, CSS build, or generated support prompt
- classify unused but inspected images as `reference-only`, `fallback`, `inspiration only`, or `reject`
- include a short note explaining why skipped references were not used directly

Promote to shared memory:
no for now; keep as visual-plan memory until repeated across more sections.

### 2026-06-11 - Plan WIT As Emotional Subject And Motion As Intent

Classification: `Visual plan lesson`

Context:
During Section 1 review for `why-cheap-products-keep-getting-worse`, the render improved only after WIT stopped being a small corner sticker and became the emotional subject of the frame. The user also rejected dense animation where many text blocks flew in sequentially; they wanted ordinary labels to appear exactly on the spoken beat and only emphasized words such as `$9` to smash in. Some WIT layouts looked broken because the head, face, or shoulder was cropped by the frame.

Lesson:
Visual-plan must decide WIT emotion, scale, placement, safe crop, and cue motion before render starts. It is not enough to name a WIT pose. For each cue, plan whether the element is static, hard-shows on the spoken beat, or uses impact motion. WIT should be planned as an oversized emotional read when the joke depends on feeling, often `1/3` to `1/2` of the frame, while preserving text/evidence readability and avoiding accidental face/head/shoulder crops.

Apply next time:

- add a `Motion Type` for every cue state: `static`, `hard-show`, `impact`, or `transition`
- reserve smash/stamp/pop motion for emphasized spoken words, proof marks, and payoff labels
- plan ordinary supporting labels to hard-show on the voice cue instead of animating every label
- specify WIT pose file, emotion, screen region, scale target, and safe crop/margin
- treat WIT as the emotional subject when the beat needs suspicion, panic, confusion, betrayal, or payoff
- if the approved WIT library lacks the right funny/emotional pose, plan a new WIT asset in shared/project assets instead of forcing a weak pose
- include screenshot/contact-sheet QA timestamps for WIT-heavy beats; use MP4 QA timestamps only when export is explicitly requested

Promote to shared memory:
yes; summarized in `.agents/_shared/systems/visual-production.md` because it applies across future sections and projects.

### 2026-06-11 - Plan WIT Rhythm, Not WIT Per Cue

Classification: `Visual plan lesson`

Context:
After WIT was enlarged and made more expressive in Section 1 of `why-cheap-products-keep-getting-worse`, the user said `7` WIT poses in a `21.205s` section felt dense. The render was fixed by reducing WIT to `4` appearances: `2` in the opening chair big scene, `1` in the failure big scene, and `1` in the final cost/payoff big scene.

Lesson:
Visual-plan must plan WIT rhythm, not just WIT pose choice. WIT should appear when the voice needs an emotional punctuation beat. Explanatory labels, props, and red markup should carry many cue states without WIT. For short sections, start with about `1-2` WIT beats per persistent big scene and only exceed that with a clear voice-rhythm reason.

Apply next time:

- count WIT beats per big scene in the WIT Pose Plan
- avoid assigning WIT to every cue state
- let WIT appear for setup reaction, escalation/reversal, or payoff rather than all three if the section is very short
- keep WIT large and expressive when it appears, but reduce frequency before reducing emotion
- include a `WIT density note` in section visual plans

Promote to shared memory:
yes; summarized in `.agents/_shared/systems/visual-production.md` and `.agents/_shared/channel/learning-log.md`.

### 2026-06-11 - Visual Plan Must Prevent Render Review Failures

Classification: `Visual plan lesson`

Context:
The user asked to update `visual-plan` so future plans avoid the Section 1 review problems before render starts: dense cue animation, WIT overuse, weak/small WIT placement, broken WIT crop, text overlap, meaningless markup, and render needing to guess the correct motion or placement.

Lesson:
Visual-plan must include a review-prevention pass, not only a scene table. A render-trustworthy plan must specify motion type, WIT density, WIT crop guard, no-WIT breathing beats, exact markup targets, and screenshot/contact-sheet QA timestamps. If render still has to decide these fundamentals, the visual plan is incomplete.

Apply next time:

- require `Motion Type` for every cue
- require a `WIT density note`
- require safe crop/margin guidance for WIT
- require no-WIT breathing beats where explanation should be carried by text/props/markup
- require exact target object for every red mark
- require review-prevention checklist before handoff

Promote to shared memory:
no; the channel-wide summary already lives in shared visual-production rules.

### 2026-06-11 - Payoff Text Must Not Cover WIT Emotion

Classification: `Visual plan lesson`

Context:
In Section 1 of `why-cheap-products-keep-getting-worse`, the final payoff card `FUTURE NOT INCLUDED` and `SMALL PROBLEM` stamp initially covered the oversized money-panic WIT. The user flagged that the text was hiding WIT's expression in the final emotional beat.

Lesson:
Visual-plan collision checks must work both ways. It is not enough to ensure WIT does not cover labels or proof. When WIT is the emotional subject, payoff text, stamps, tags, and cards must not cover WIT's face, eyes, mouth, or key prop. Plan separate text and WIT zones for final/payoff beats.

Apply next time:

- reserve a clean WIT emotion zone for payoff/reaction boards
- keep final cards/stamps readable but away from WIT face/expression
- specify where WIT sits and where text can safely land
- add final/payoff beat timestamps to screenshot/contact-sheet QA suggestions
- reject visual plans where the final memory frame hides WIT's emotion under text

Promote to shared memory:
yes; summarized in shared visual-production and learning log.

### 2026-06-12 - Plan Giant WIT Placement For Strong Emotion Beats

Classification: `Visual plan lesson`

Context:
After Section 2 of `why-cheap-products-keep-getting-worse` was updated with larger WIT poses, the user still said WIT was not dominant enough and pointed back to Section 1, where WIT became much more interesting by occupying roughly half the screen as a giant behind-layer or edge-peek emotional subject. The user said lower-body crop from the bottom is acceptable, but broken face/head/shoulder crop is not.

Lesson:
For strong emotional beats, visual-plan should not merely specify a pose and a corner placement. It should plan WIT as the emotional subject: giant behind-layer faces, side peeks, lower-edge half-body entrances, WIT looming beside or hiding around the main object, and other exaggerated compositions. WIT can occupy about `1/2` of the frame when the emotion carries the joke, as long as labels/evidence stay readable and face/head/shoulders/key props are safe.

Apply next time:

- avoid default full-body lower-corner WIT on strong reaction/payoff beats
- plan giant WIT placements when WIT carries the emotion
- allow intentional crop only through lower body, legs, or non-emotional edge areas
- never plan crop through WIT's face, glasses, head, shoulders, mouth, or key prop
- include separate text/evidence and WIT emotion zones in the cue plan
- if existing poses do not fit a giant emotional composition, plan a new approved WIT pose asset

Promote to shared memory:
no; core shared rules already say WIT can be large, but this keeps the more concrete Section 1/2 placement pattern in visual-plan memory and SKILL.md.

### 2026-06-12 - Plan Subtitle-Safe Lower Layouts

Classification: `Visual plan lesson`

Context:
While adjusting Section 2 of `why-cheap-products-keep-getting-worse`, the user pointed out that some lower-third elements were too close to the bottom edge and would likely be covered by YouTube subtitles after upload.

Lesson:
Visual-plan should reserve a small subtitle-safe margin near the bottom of the frame. Important lower-third labels, receipts, arrows, loop boxes, and payoff props should be planned slightly higher unless they are intentionally background-only.

Apply next time:

- check every lower-third cue for subtitle overlap risk
- place important text and props slightly above the bottom edge by default
- treat the subtitle zone as unsafe for cue-critical information
- if WIT rises from the bottom edge, move nearby text and props up instead of stacking them into the subtitle area
- include subtitle-safe placement in the render handoff when a cue uses the lower third

Promote to shared memory:
yes; this affects future sections and future video projects on YouTube.

### 2026-06-12 - Compress Explanatory Lists Into Memory Frames

Classification: `Visual plan lesson`

Context:
In Section 4 of `why-cheap-products-keep-getting-worse`, the first visual direction became chaotic because the plan/render treated many boring product parts as separate objects, labels, and cards. The user rejected it as too text-heavy and image-heavy, and asked for the simpler Section 1 style. The successful remake used three large backgrounds, six cue states, and three giant WIT beats.

Lesson:
When a section lists many small product details, visual-plan must not itemize every noun on screen. Build a few memory frames instead: one persistent background per idea cluster, one or two short labels per cue, and WIT only where the emotion changes. Real/object backgrounds can carry texture while labels compress the concept.

Apply next time:

- start list-style sections by choosing `2-4` viewer memory frames
- compress related terms into category labels instead of separate cards
- prefer strong real/object backgrounds plus sparse labels over many small images
- keep WIT large but limited to the main emotional beats
- reject plans that feel like a vocabulary worksheet, product-parts inventory, or scattered object tray
- if the user asks for Section-1-style simplicity, treat the existing plan as stale and remake it from script, voiceover, and approved references

Promote to shared memory:
no for now; this is captured in visual-plan and render skill behavior. Promote after the same pattern improves another project.

### 2026-06-13 - Giant Creative WIT Is The Default Emotional Read

Classification: `Visual plan lesson`

Context:
The user clarified that they love giant WIT with creative placements: appearing from a corner, upside down from the top, hiding behind an object such as a wardrobe, and other playful compositions. They want future renders to ensure WIT occupies at least one third of the screen on emotional beats.

Lesson:
Visual-plan must treat giant WIT as the default emotional design language. For any WIT emotional beat, plan the visible WIT character footprint to occupy at least `1/3` of the frame, measured by visible character area in the final screenshot/contact sheet, not by CSS box or transparent PNG bounds. The plan should include a creative placement concept rather than defaulting to a small full-body lower-corner sticker.

Apply next time:

- specify visible WIT footprint target for every WIT appearance
- require at least `1/3` visible frame presence for emotional WIT beats
- plan creative placements such as corner peeks, upside-down top entrances, hiding behind wardrobes/products/tags/boxes/screens, looming faces, or lower-edge half-body entrances
- reserve a clean text/evidence zone so giant WIT can be large without covering the point
- include WIT-heavy timestamps in screenshot/contact-sheet QA suggestions

Promote to shared memory:
no for now; keep in visual-plan/render skill memory until the same rule is proven across more future videos.

### 2026-06-18 - Reconstruct A Missing Plan From The Surviving Approved Render

Classification: `Operational lesson`

Context:
For `why-cheap-products-keep-getting-worse` Section 6, the `05-visual-plan.md` index claimed Section 6 was planned and rendered, but the `visual-plan/section-06-.../` markdown folder and the `section-previews/section-06-.../` working preview were missing on disk. The approved render survived at `hyperframes/review/section-06.html` with its photo bases, and the 4 browsed references survived under `assets/visual-references/section-06-.../`. The user asked to run visual-plan for Section 6, then render.

Lesson:
The project index can drift from the filesystem. Always verify actual files with a glob before deciding Create vs Update mode. When the plan markdown is missing but an approved (or ready-for-review) render survives, reconstruct the plan to match the render 1:1 - read the render HTML for exact scene/cue starts, durations, labels, WIT poses, placements, and timed reveals - instead of inventing a new, contradictory plan. This preserves prior approved decisions and gives render a clean rebuild spec. Reuse the already-saved references rather than re-browsing.

Apply next time:
- glob the `visual-plan/`, the section previews folder (`previews/` new / `section-previews/` legacy), and `hyperframes/review/` folders before trusting the index
- if a render survives, treat it as the source of truth and document it (exact timings/coordinates/reveals) in the reconstructed plan
- reconcile the index row and stale notes to the real filesystem (missing preview, missing `06-production-board.md`, surviving review mirror)
- reuse surviving saved references; document them in `reference-board.md` with their licenses

Promote to shared memory:
no; this is visual-plan execution behavior, not a channel-wide creative rule.

### 2026-06-21 - Plan A Real Photo Base Per Scene + Sourcing Recipe (Section 6 review synthesis)

Classification: `Visual plan lesson`

Context:
Section 6 of `why-cheap-products-keep-getting-worse` shipped several CSS-only / flat-gradient scene bases (cost, ownership-lock, future-label) plus a sterile screwdrivers-on-white base. Reviewers rejected each as "no background / doesn't have an image to describe the voice / looks bad." Later review/fix passes had to source real Wikimedia photos (padlock, euro money, phone-on-table, opened-phone repair bench) pass by pass - work that should have been decided in the visual plan. Brand/people traps surfaced: a CC0 desk photo had a recognizable MacBook, a battery showed a Motorola brand, and the sharpest repair photos contained real people.

Lesson:
Every persistent big scene must name a real, descriptive image base (or a justified self-made base) - never a bare gradient/empty color. The plan must give the base's search terms, a fallback, and a one-line "why it describes this voice beat" so render can source/grade it without guessing. Apply a hard selection rubric: describes the beat, brand-free, people-free (no-face channel), non-sterile/in-context, distinct from adjacent scenes, palette-clean (no gray wash), reads behind overlays. Verify on the pixels, not the filename, and record creator/license.

Apply next time:
- for each big scene, plan a real base + search terms + fallback; reserve self-made CSS for objects/labels/overlays, not the background
- use the Wikimedia Commons API recipe (curl + `node -e`; no python/jq on this box) and capture `Artist`/`License`/`descriptionurl`
- reject brand/logo/branded-device images and real-people images for direct-use backgrounds even when sharper; keep them `inspiration only`
- avoid objects-on-white sterile stock; prefer textured lived-in scenes
- note for render: `object-fit: cover` from a frame-width source only crops vertically, so a side-edge element can't be cropped away - pick a different image
- this is now codified in `visual-plan/SKILL.md` (Real Scene Base Rule + Image Sourcing Recipe And Selection Rubric)

Promote to shared memory:
no; keep as visual-plan execution behavior. The sourcing recipe could move to `_shared/systems/visual-production.md` if render starts sourcing the same way.

### 2026-06-21 - Plan Exact Word-Timed Cue + List Reveals (Section 6 review synthesis)

Classification: `Visual plan lesson`

Context:
Section 6's timing reviews (ownership-lock spoken at 12.64s but planned at 16.8s; list items dumped at once) were partly a planning gap - the cue timeline used round/estimated times and did not call out per-item reveals, so render had nothing precise to build to even though `section-06-word-timings.json` existed.

Lesson:
When the section has a `voiceover/section-XX-*/section-XX-word-timings.json`, the cue-state timeline should cite real word timestamps, not estimates, and should explicitly mark which multi-element beats and on-screen lists (policy rows, checklist questions, quotes) reveal item-by-item on each spoken word. That removes the timing guesswork that caused the render rework.

Apply next time:
- read the section word-timings JSON and quote real timestamps in the cue timeline
- for any list or multi-label beat, plan a per-item staggered reveal keyed to each word, and say so in the Render Handoff
- label timing `estimated` only when no word-timings file exists

Promote to shared memory:
no; visual-plan execution behavior that pairs with the render Voice-Sync Timing Contract.

### 2026-06-22 - Source Clean Real Photos Via Openverse (Commons skews dingy)

Classification: `Visual plan lesson`

Context:
For `why-everyone-pretends-to-be-busy` Section 1, the first bases were raw Wikimedia Commons photos
(a dated 2007 wall calendar + an overhead desk). The user rejected them as "filthy and bad." A
flat-illustrated CSS rebuild was ALSO rejected ("use real images or generated images instead of
this... find real-world images"). No image-generation tool is connected this session, and
Google/Bing/DuckDuckGo/Pexels are all bot-blocked from this network. The fix that was accepted:
clean CC0 real-world stock photos sourced via the **Openverse API** (warm work desk + bright
minimal desk), composited with WIT + handwritten overlays.

Lesson:
For real-world photo bases, query the **Openverse API first** - it is scriptable without a key,
works when search engines are blocked, and surfaces clean modern CC0 stock (StockSnap, rawpixel)
that reads far better than raw Wikimedia Commons (which skews dingy, antique, or branded for
everyday objects). Wikimedia Commons is the secondary source. Always VIEW candidates and reject
brand-bearing (Apple Magic Mouse/iMac, Logitech, Casio) and people images (no-face channel).

Apply next time:
- `curl https://api.openverse.org/v1/images/?q=...&license_type=commercial,modification&size=large`, parse with `node -e`
- prefer CC0 + `source` stocksnap/rawpixel + width >= 900; record source in ATTRIBUTION.md
- view every pick; reject brands/people even when sharper
- no image generator is connected - don't promise generated art; if clean photos are rejected, offer the "user drops in files" path
- channel taste signal: dingy stock AND code-drawn CSS bases both get rejected; clean modern CC0 photos are accepted
- the SKILL.md "Image Sourcing Recipe And Selection Rubric" now documents the Openverse-first recipe

Promote to shared memory:
no; the channel-wide visual reference standard already lives in `_shared/systems/visual-production.md`. This is the concrete sourcing recipe for visual-plan/render.

### 2026-06-22 - Don't Reuse One Base For Two Scenes In The Same Section

Classification: `Visual plan lesson`

Context:
Section 2 used the SAME image (S1's minimal desk, copied) for both Scene B (0:09) and Scene D
(0:19) as an intended "quiet/real-work bookend." On review the user said "they both the same, I
need this more vary." Fixed by sourcing two distinct CC0 photos: a blank notebook on dark wood
(B = "thinking looks like nothing") and a glowing bulb on black (D = "real work hides in the part
you cannot see").

Lesson:
A reused/identical base across two scenes in the same short section reads as a repeated image, even
when intended as a callback - and reusing a prior section's base compounds it. Default to a DISTINCT
base per scene. Only reuse a base for a true payoff callback the viewer will consciously recognize
(e.g. S1's hook motif returning at the S1 payoff), and even then vary the grade/overlay. Across
sections, prefer fresh imagery over re-running an earlier section's base.

Apply next time:
- give every scene in a section its own distinct base unless a deliberate, recognizable callback
- if a "quiet/real-work" beat recurs, pick different concrete objects (notebook, bulb, window, books) rather than the same desk twice
- a glowing bulb on black is a strong, distinct metaphor for "the hidden idea / invisible real work"

Promote to shared memory:
no; visual-plan execution refinement of the existing differentiation rule.

### 2026-06-22 - Split Long Scenes + Vary WIT Poses (don't repeat one base ~15-20s)

Classification: `Visual plan lesson`

Context:
Section 3 (45s) first shipped with 3 big scenes: the trophy held ~15.7s and the meeting room held
~19s. The user said the section is "pretty" but wanted more scenes - specifically a new scene after
"...important" (splitting the trophy beat) and a second scene for the long meeting-room stretch -
and noted the WIT poses were "not vary" (deadpan-side-eye repeated). Fixed by expanding to 5 scenes
(trophy → coffee chat → beach → meeting → wall clock) and using 6 distinct poses.

Lesson:
For longer sections, scale big-scene count to runtime, not just idea count - a single base holding
~15-20s reads as static even with cue changes. Target a fresh base roughly every ~6-10s of talky
content. And rotate WIT poses: don't reuse the same pose (esp. deadpan-side-eye) twice in a section;
pull from the wider library (talking-front, confused, suspicious, facepalm, tiny-defeated,
awkward-celebration, thinking, shocked, etc.) so each emotional beat looks different.

Apply next time:
- a ~45s section wants ~4-6 big scenes; a ~30s section ~3-4; don't let one base run past ~10s without a cut or a strong reason
- give each WIT beat a distinct pose; avoid repeating one pose within a section
- splitting a beat just needs a new distinct base for the second half + a 0.2s fade; cue timing stays word-pinned

Promote to shared memory:
no; visual-plan/render pacing refinement (pairs with the existing differentiation + WIT-rhythm lessons).

### 2026-06-22 - Full-HD Bases + Clear Object Metaphors (Section 4 rebuild)

Classification: `Visual plan lesson`

Context:
Section 4 first used a hand-drawn app-sketch wireframe (StockSnap 960px) as the base, reused across
scenes, with only 3 distinct scenes for 42s. The user rejected it: "the illustrative images are
completely poor and vague... not suitable for the script... find other illustrative images (at least
fullhd)... you're repeating many scenes... I need more scenes." Rebuilt with 5 distinct full-HD
object photos.

Lesson:
Three compounding mistakes to avoid: (1) low-res bases - StockSnap (~960px) and rawpixel
(~1024–1300px) are BELOW full-HD; when full-HD is needed, use Wikimedia `iiurlwidth=1920` or Flickr
`_k`(2048)/`_o`. (2) vague/abstract bases - a wireframe sketch reads as "poor/vague"; use CLEAR object
metaphors (red emergency button = urgency, fire alarm = "every ping is an emergency", open fridge =
"sad vegetable", blank-screen phone + CSS UI = the apps). (3) too few scenes / repeated images - give
a ~42s section ~5 scenes, each a DISTINCT image; a reused base is only OK as a non-consecutive callback.

Apply next time:
- check the resolution requirement; if full-HD, source Wikimedia@1920 / Flickr large, not StockSnap/rawpixel thumbs
- pick a concrete, instantly-readable object per beat over abstract/wireframe imagery
- brand-free screens: use a "blank white screen" phone photo and add the UI/notifications in CSS
- ~5 scenes for ~40s; every scene a distinct image; reuse only as a deliberate non-consecutive callback

Promote to shared memory:
no; the SKILL.md sourcing recipe now carries the full-HD/Flickr/Wikimedia + blank-phone note.

### 2026-06-22 - User Can Approve Real App Branding (Section 4 v3)

Classification: `Visual plan lesson`

Context:
After Section 4's object-metaphor pass, the user asked to use REAL app branding: an iPhone screen
full of notifications, and real app icons (Gmail, Messenger, Microsoft To Do, Google Calendar) on
the email/chat/task/calendar beats, plus a chat conversation instead of a blank phone. The channel
default is "no real app logos."

Lesson:
The no-logos rule is a DEFAULT, not absolute - the channel owner can explicitly approve real brand
logos for a section (the "unless specifically approved" clause). When they do, use the real icons.
Source app logos from Wikimedia Commons (rasterize SVG→PNG via `iiurlwidth`); they exist for Gmail,
Messenger, To Do, Google Calendar, WhatsApp, Slack, and a thumbs-up emoji (Android/Noto). Record
them in ATTRIBUTION as trademarks used editorially with owner approval.

Build technique that worked: app UI is best built in CSS (iPhone frame + notification cards; an
app-icon grid with red badges; a Messenger-style chat with bubbles + a thumbs-up icon), with the
real icon PNGs dropped in. CRITICAL: put accumulating UI (notification cards, badges, chat bubbles)
INSIDE the scene div (so it persists and is clipped to the phone/tiles), not in short cue clips -
cue-clip elements vanish when the cue ends and broke continuity. The 👍 emoji glyph does NOT render
in the snapshot Chromium (font fallback to a coin glyph); use a thumbs-up PNG via `<img>` instead.

Apply next time:
- treat no-logos as a default the owner can waive per-section; if waived, use real icons from Commons
- build app/notification/chat UI in CSS with real icon PNGs; keep accumulating UI in the scene div
- never rely on emoji glyphs in HyperFrames snapshots - use an emoji/icon PNG
- record trademark logos in ATTRIBUTION with the editorial/owner-approved note

Promote to shared memory:
no; section-specific brand-approval + technique. Keep in visual-plan/render execution memory.

### 2026-06-22 - STANDING PREFERENCE: Real-UI Illustration (owner confirmed)

Classification: `Core` (confirmed channel creative direction)

Context:
After the Section 4 rebuild with real app icons + iPhone/chat mockups, the owner said: "Yes good,
I love to use real illustrative like phone, app icons to describe the script like this. Please note
to the skills." This is now a STANDING preference, not a one-off.

Lesson:
For every section going forward, when the script names or depicts real apps/products/screens, prefer
REAL recognizable UI to illustrate it - phone/iPhone mockups, real app icons (Gmail, Messenger,
Microsoft To Do, Google Calendar, WhatsApp, Slack, etc.), notification lists, app grids with badges,
chat conversations. This overrides the old "avoid real logos" default. Use editorially (depict, not
endorse); keep private data out; build the screens in CSS with real icon PNGs from Wikimedia Commons;
keep accumulating UI inside the scene div; use emoji/icon PNGs (not emoji glyphs).

Promoted to shared memory: YES - recorded in `_shared/channel/brand-system.md` ("Real-UI Illustration"),
`_shared/systems/visual-production.md`, and `_shared/channel/channel-foundation.md`. The SKILL.md
Image Sourcing section also carries the technique.

### 2026-06-22 - Abstract-concept sections: CSS metaphor + real-UI chat OVER real photos

Classification: `Visual plan lesson`

Context:
Section 6 ("I'm Busy Is A Shield") has an abstract thesis (busy = a social defense) with no single
literal object. Owner had just established two strong preferences: real photo backgrounds make scenes
lively, and real-UI (chat/app screens) is preferred when the script depicts messages. Plan blended both.

Lesson:
For abstract/concept sections, satisfy the Real Scene Base Rule by putting a REAL people-free photo
behind every scene, then build the metaphor and the messages in CSS on top:
- the metaphor as a CSS construct over the photo (a shield labeled `I'M BUSY` deflecting request
  bubbles; struck-out speech bubbles over an empty meeting room for "things you can't say")
- the "requests/messages" beats as real-UI chat (1:1 + group) floated as a `.screen` on a real desk,
  with a real app icon (Messenger) used editorially
Pick photo bases that literally echo a line (an empty meeting room for "this meeting could've been a
message"; a wall of sticky notes for "really are overloaded") - it makes an abstract section concrete.

Apply next time:
- abstract section → real photo base per scene + CSS metaphor/labels on top (never a bare gradient)
- use real-UI chat for message/notification beats; keep people as initials avatars (no-face)
- match a base to a specific spoken line where possible; keep all 5 surfaces visually distinct
- when the section's word-timings JSON is missing, GENERATE it first (whisper prefix) before timing cues

Promote to shared memory:
no; execution refinement of the Real Scene Base Rule + the standing real-UI preference.

### 2026-06-22 - Session synthesis (S5–S7): real bg behind EVERY scene + WIT big-and-high

Classification: `Core` (confirmed channel creative direction)

Context:
Across `why-everyone-pretends-to-be-busy` Sections 5, 6, 7 the owner gave three consistent reviews:
(1) S5 "missing some real-world images that make the section not lively" → grounded the CSS-UI scenes
on real desk photos; (2) S5 "the last scene still not have background" → even the stylized CSS theater
got a real red-curtain photo; (3) S7 "WIT too low / covered by the frame" then "make the WIT bigger,
re-arrange other items if it covers content."

Lesson (now the default, codified in SKILL.md + shared):
- EVERY scene needs a real, people-free photo base - including real-UI scenes (chat/Meet/Trello/
  spreadsheet/calendar) and stylized/CSS constructs (shield, stage). Float the UI as a `.screen` on a
  real desk; back a CSS construct with a real photo. All-CSS-on-gradient = "not lively," gets rejected.
  Pick a base that literally echoes the line. Hands-at-keyboard photos are OK (no-face allows hands).
- Plan WIT BIG (`1/3`–`1/2` frame) AND HIGH (head+torso inside frame, only legs cropped). If a big WIT
  would cover content, the PLAN relocates the other items (opposite side/top/bottom) - never shrink or
  lower WIT to fit. State both WIT's region and the cleared zone for labels in the cue plan.
- Real-UI illustration remains the standing preference (see the 2026-06-22 STANDING PREFERENCE entry).

Apply next time: assume real photo base per scene by default; assume WIT big+high by default; design
label/UI positions AROUND a big high WIT from the start so render doesn't have to rescue collisions.

Promote to shared memory: yes - added to `_shared/systems/visual-production.md` (real-bg-behind-every-scene
+ WIT size/anchor) and the SKILL.md files; brand-system already carries the real-UI preference.

### 2026-06-23 - Vivid object photos + dynamic WIT + VARIED idea-devices (not repeated label boxes)

Classification: `Core` (confirmed channel creative direction)

Context:
`why-everything-is-a-subscription-now` Section 1 v1 used calm stock photos (two phones in a park, a
dim home-office desk), the milder WIT poses (suspicious/shocked/deadpan), and the SAME cream
handwritten rectangle label box for nearly every on-screen idea. Owner rejected it: "illustrative
images not suitable, mundane and boring… WIT poses are boring… the rectangle boxes show up boring and
repeat, not creative - try another way to demonstrate ideas, make it vary… remake completely." The
accepted remake: vivid on-topic OBJECT photos (a pile of coins, a pile of cash, padlocks on a gate),
DYNAMIC expressive WIT (price-tag-suspicion, hidden-fee-panic, holding-phone-panic, trapped-by-app-screen),
and VARIED idea-demonstration devices - a colorful app-tile grid, a jumping "12+" counter, notification
charge toasts, a free-trial countdown that flips to "$/mo", a full-screen EXPIRED system modal, and a
padlock-wall with bold kinetic payoff type. Zero cream label boxes.

Lesson (apply to ALL future sections):
- IMAGERY: prefer vivid, concrete, on-topic OBJECT photos that dramatize the line (money/coins/cash for
  "money leaving", padlocks for "locked/rent", a glowing screen, etc.) over calm desks/hands. If clean
  topical photos are scarce, pivot to a strong concrete object (money, lock) + the owner's loved CSS real-UI.
- WIT: pick the most EXPRESSIVE/funny pose for the beat (panic, hidden-fee-panic, trapped, betrayed,
  empty-wallet, receipt-attacked, facepalm) - not the mild suspicious/neutral/deadpan defaults. NOTE:
  current WIT poses ship on a flat green #00B140 screen - chroma-key the green at render; always VIEW a pose first.
- TEXT/IDEA DEVICES: do NOT show every idea in the same handwritten cream rectangle. VARY the device per
  beat - app-grid tiles, a big kinetic number/counter, notification toasts, a countdown timer, a system
  error/EXPIRED banner, badges, a padlock wall, bold kinetic headline type, a chat bubble, a stamp. Reserve
  the cream label for the occasional handwritten aside, not the default for everything.
- WIT VARIETY ACROSS SCENES (owner-confirmed 2026-06-23, follow-up): do NOT park WIT on the SAME side every
  scene with the text always on the opposite-same side. VARY WIT per scene in side (left / center / right),
  scale, vertical anchor, AND pose; flip the text/UI to whichever side WIT is not using. Across a section,
  aim for distinct WIT sides (e.g. scene1 left, scene2 center, scene3 right) and visibly different scales.
  WIT stays GIANT (≈1/2 frame) and is the soul of each scene - rearrange the other items around it.

Apply next time: plan 2-3 DISTINCT idea-devices per section; an expressive WIT pose per beat; a vivid
object/real-UI base per scene; and a DIFFERENT WIT side+scale+pose per scene (never all-right/text-left).
Treat "repeated identical label boxes" and "WIT always same side" as review failures to avoid up front.
This Section-1 remake is the STANDING template for all remaining sections of this video and future videos.

Promote to shared memory: yes - this is a channel-wide creative-direction signal; add a short note to
`_shared/systems/visual-production.md` (vivid object imagery + varied idea-devices + expressive WIT) on the
next shared-memory pass. Pairs with the standing Real-UI Illustration preference.

### 2026-06-23 - "Remake like Section 1" = distinct vivid base per scene + varied devices + varied WIT

Classification: `Visual plan lesson`

Context:
`why-everything-is-a-subscription-now` Section 2 was remade "based on Section 1." The first S2 plan
reused ONE phone base across 4 scenes (graded normal/warm/cool/dark) and leaned on repeated cream label
boxes - the exact pattern the owner rejected for S1 v1. Remade to the standing template: 5 distinct vivid
object bases (glowing phone / vinyl crate / phone+paywall / padlock / device flat-lay), varied idea-devices
per beat, and giant WIT varied per scene (facepalm R / thinking L / [breathe] / betrayed CENTER giant /
suspicious R).

Lesson:
When the owner says "remake to Section 1," do NOT keep one base graded N ways - plan a DISTINCT vivid,
on-topic OBJECT base per scene. A base may return only as a NON-CONSECUTIVE callback, and that is exactly
right when the script intends "the same device shown two ways" (here the phone returns for the RENT beat,
re-dressed with a cool grade + paywall + RENT stamp, with the vinyl scene between). Pair it with varied
idea-devices (struck banner, stamps, receipt, real-UI paywall, lock-screen card, RENT tags, kinetic
payoff) and a giant WIT that changes side/scale/pose each scene. Cream labels are for ≤2 asides.

Apply next time:
- one distinct vivid object base per scene; reuse only as a deliberate non-consecutive callback the script asks for
- plan 2-3 idea-devices per section, an expressive WIT pose per beat, and a different WIT side+scale each scene
- treat a stale "one base graded N ways + cream boxes" plan as a remake trigger

Promote to shared memory:
no; the Core template already lives in `_shared/systems/visual-production.md` and the 2026-06-23 entries above.

### 2026-06-24 - "Funnier" ≠ a cute mascot prop (keep literal on-beat objects)

Classification: `Visual plan lesson`

Context:
On `why-buy-1-get-1-beats-50-off` Section 2 (the store-side math), the owner first said the bases
"aren't good, find more suitable and funny images." I swapped the cash register (Scenes A/D) for a
bright pink piggy bank (a cute money mascot). The owner rejected it: "back to previous images,
currently even worse," and we restored the register/cash/coins/Wedgwood set.

Lesson:
For this owner, "make it funnier" does NOT mean substitute a generic cute prop (piggy bank, mascot
object) for the literal, on-beat object. The humor should come from WIT + labels + the dry framing,
while the base stays a real, literal object that matches the spoken beat (a counter/register for
"behind the counter," money for the money math, the actual Wedgwood piece for Wedgwood). A cute
stand-in that doesn't literally depict the line reads as worse, not funnier.

Apply next time:
- when asked for "funnier" backgrounds, first improve the LITERAL base (clearer/brighter/better
  composed real object of the same thing), and add the funny via WIT pose + label/markup, not via a
  cute mascot swap.
- offer a mascot/abstract prop only as an explicit option, not as the default fix.
- keep already-approved literal bases (e.g. the real Wedgwood jasperware) unless the owner names them.

Promote to shared memory:
no for now; a per-owner taste signal. Revisit if it recurs across videos.

### 2026-06-24 - Source FRESH bases per section + never stack/overlap text (S5 remake)

Classification: `Visual plan lesson`

Context:
`why-buy-1-get-1-beats-50-off` Section 5 v1 reused cash/coins/red-curtain bases from S1–S4 and stacked
several text elements close together. Owner: "you reuse too many images from other sections, don't be
lazy; texts are covered by many texts; this section looks so bad - do it again." The accepted remake
sourced 5 FRESH distinct retail photos for the section (shelf price tags, red 50%/30% sale store,
boutique mannequins, supermarket aisle, clothing shop) and used one clean hero device per beat with
well-spaced, sequentially-timed text.

Lesson:
Two hard rules, applied up front:
1. SOURCE FRESH BASES PER SECTION. Reusing the same money/coins/curtain photos across sections reads as
   lazy to this owner. Each section gets its own distinct, on-topic vivid bases (a few minutes of
   Openverse/Wikimedia sourcing). Money objects can recur thematically only with genuinely different
   photos + distinct grades - never literally the same files section after section.
2. ONE CLEAN HERO PER BEAT, NO STACKED TEXT. Don't pile multiple labels/cards close together. Per scene:
   one large hero device + at most one small caption, vertically well-spaced (≥~150px gaps), revealed
   SEQUENTIALLY on their words (not all at once), all on the half opposite the giant WIT. Use a
   side-gradient scrim to darken only the text half so labels read on busy photos.

Apply next time:
- budget sourcing time for fresh per-section bases; do not default to copying a prior section's assets.
- design each scene as hero + spaced caption; stagger reveals; check the contact sheet for any
  text-over-text or text-near-text crowding before handoff.

Promote to shared memory:
no for now; strong per-owner execution rules. Fold a one-liner into the SKILL Default Build Bar.

### 2026-06-24 - Keep bases BRIGHT; no heavy dark overlay (correction)

Classification: `Visual plan lesson`

Context:
Across the S3–S6 rebuilds I graded bases dark (`brightness ~0.42–0.55`) + a heavy full-frame/side
scrim for text contrast. The owner pushed back twice: "remove the dark area behind the WIT" and then
"why it always has dark areas overlay, I don't think it good." Fixed by brightening all bases to
`~0.7–0.85` and replacing the heavy scrim with only a subtle edge vignette / a light text-side
gradient that fades fully transparent before mid-frame.

Lesson:
This owner wants the vivid base photo to SHOW - a heavy dark overlay (full-frame radial or a strong
half-darkening gradient) reads as "not good." Keep bases bright/visible. Get text readability from:
strong text-shadow on bare labels, the device cards' own opaque backgrounds (chips/stamps/toasts/
signs already carry contrast), and at most a faint edge vignette or a light text-side gradient. Never
a full-frame dark scrim, and never darken the half where WIT stands.

Apply next time:
- grade bases ~0.7–0.85 brightness; design text as cards/stamps with their own bg, or bold text +
  heavy shadow, so no big dark overlay is needed.
- if a bare label sits on a busy/bright area, give THAT label a small local backing - don't darken the
  whole frame.
- SKILL Default Build Bar (BASES bullet) updated to this; the earlier "dark dramatic grade + heavy
  scrim" guidance is superseded.

Promote to shared memory:
no for now; per-owner taste correction folded into the SKILL build bar.

### 2026-06-28 - UNLIMITED imagination + generate-forward; do NOT reuse one base as a crutch (owner-directed, Core)

Classification: `Core` (confirmed channel creative direction)

Context:
On `5-why-the-internet-is-full-of-ai-slop` the owner reviewed S3 v1 and pushed back hard: `grey-sludge-flood-1.jpg`
was reused in nearly every section "with no clear purpose"; S1 had bespoke generated imagery but S2/S3 drifted
into reusing old/browsed photos; and the plan "wasn't creative enough - I need it crazier and unlimited."
Quote (paraphrased): "Visual-plan does NOT limit imagination; always find every way to REALIZE the plan's
ideas, don't restrict the plan." Rebuilt S3 v2: 10 bespoke GENERATE heroes (slop-machine, melting AI
influencer, firehose of grey clones, robot-in-a-human-mask payoff), 8 FRESH distinct browse bases, ZERO sludge.

Lesson (apply to ALL future sections):
- IMAGINATION IS THE DEFAULT, not the exception. The plan should be bold/surreal/funny; if an idea is good
  it MUST be executed by all means - lean on `generate` to realize it (write the prompt in visual-implement,
  owner generates in ChatGPT + drops it in, exactly like the S1 cards). Do NOT downgrade a wild idea to a
  safe browsed photo just because generation is an extra step.
- NO CRUTCH BASE. Never reuse one background across many sections to save effort (the sludge overuse was
  rejected). Each section earns its own distinct, purposeful imagery; a motif may recur ONLY within the
  section/where it has clear meaning, graded/varied, not as a universal filler.
- Per scene, prefer a bespoke generated HERO (object/creature/surreal device) + a fresh base; reuse only a
  deliberate within-section callback (e.g. the same influencer shown perfect then melting; the machine
  returning for the stamp).
- Generate volume is fine: a section may call for ~8-12 generate assets. Batch them for the owner. The
  constraint is copyright/law/YouTube community standards (parody not real logos; non-existent people), NOT effort.

Apply next time: open every section by asking "what is the CRAZIEST true way to show this line?" and
generate it. Treat browsed real photos as grounding bases/textures, not as a substitute for bold heroes.
Rerunning a plan restales that section's implemented assets + render (list them; orphan unused old assets).

Promote to shared memory: YES - added to `.agents/_shared/channel/learning-log.md` as a Core creative-direction
signal (pairs with the existing vivid-imagery / varied-idea-devices entries).

### 2026-06-30 - Animated interactive UI-mockup graphics are a go-to device (owner loved the S8 subscribe popup, Core)

Classification: `Core` (confirmed channel creative direction)

Context:
On `5-why-the-internet-is-full-of-ai-slop` the owner first found the Section 8 outro (a flat, static
like/share/subscribe card) boring and asked for "something super unrealistic, superficial... a popup
that looks like a YouTube screen with subscribe and like buttons, a pointer that clicks them, buttons
that wiggle and become subscribed/liked." I rebuilt it as an animated fake-YouTube card: a drawn SVG
mouse cursor flies in and CLICKS LIKE then SUBSCRIBE on their spoken words; the buttons boing/wiggle and
flip state (red SUBSCRIBE -> grey SUBSCRIBED + ringing bell, Like turns blue), a "Link copied!" toast +
confetti pop, all on a parody "WhyTube" UI. The owner's reaction: "you used visualize VERY well at the
subscribe popup - use this advantage in future videos to make them livelier, and update it into
/visual-plan so whenever a video needs this kind of graphics-animation illustration it applies
excellently." So this is now a STANDING device, not a one-off.

Lesson (apply to ALL future videos):
- When a beat describes USING an app/site or asks the viewer to DO something (subscribe/like/share, tap,
  toggle, search, buy, swipe, fill a form, watch a value change), default to an ANIMATED interactive
  UI-mockup instead of a static screen. The screen performs the action itself.
- The kit: a drawn SVG mouse cursor (or a tap-ripple) that moves and clicks; buttons that boing/wiggle
  (one combined scale+rotate "boing" tween, single transform set, so tweens don't fight) and FLIP STATE
  by cross-fading two stacked state elements; counters/badges that tick; progress bars that fill;
  toasts + confetti on the click. Pin every click and state-change to the real word-timings.
- Build rules learned: CSS/SVG only; use SVG/CSS icons + an SVG cursor, NEVER emoji glyphs (they don't
  render in the snapshot Chromium); namespace decorative classes (confetti = `.cfp`, not `.cf`) so they
  can't collide with structural icon sub-element classes; a single continuous scene (no hard cut) lets
  an interactive card hold its final state through the end of the beat.
- Honesty + safety: parody UI with our own branding (e.g. "WhyTube", "Why It Works") - never a real
  screen-grab, never a real channel/person, and NO fake inflated metrics (the owner explicitly rejected
  "1.2M subscribers" for a small channel; use a non-numeric line like "Subscribe for more" ->
  "Welcome to the channel!" and a humble tick instead).

Apply next time: for CTAs, "how it works" demos, before/after toggles, settings/permission beats, and
any "tap/scroll/click/type" line, plan the interactive-mockup device by default; describe the cursor
path, each button's state flip, and the celebration beat, all pinned to the spoken words. Reserve it for
beats that genuinely depict interaction (don't force it onto every scene).

Promote to shared memory: YES - add to `_shared/systems/visual-production.md` (a named device:
"Animated interactive UI mockup") and `_shared/channel/learning-log.md` as a Core creative-direction
signal; pairs with the standing Real-UI Illustration preference.

### 2026-07-02 - Generate word timings BEFORE planning (working recipe on this machine)

Classification: `Operational lesson`

Context:
Planned `6-why-countries-fight-to-host-the-world-cup` Section 1. Instead of writing the plan
with estimated times (the project-5 S1 fallback), generated the word-timings JSON first, so
every scene cut and reveal in the plan cites a real timestamp (fight@10.26, money@19.10,
behind@26.96...). Working recipe, verified end-to-end on this Windows box:
(1) `npm install @xenova/transformers ffmpeg-static` in a scratch folder;
(2) a ~30-line `gen-timings.mjs`: ffmpeg-static decodes the MP3 to 16 kHz mono f32 raw,
`pipeline('automatic-speech-recognition','Xenova/whisper-tiny.en')` with
`return_timestamps:'word', chunk_length_s:30, stride_length_s:5`, write
`{transcript, meta, words:[{word,start,end}]}`;
(3) checks: monotonic starts (no backward jumps), clamp the section/root duration to the real
audio seconds (whisper's last-word end overshoots), ignore harmless mishearings ("beg" ->
"bag") - the timestamps are what matter.

Lesson:
Visual-plan should generate the timings itself when missing rather than planning on
estimates - the plan quality jump is large (every show-as-you-say line is real) and the cost
is ~2 minutes. The whisper-tiny mishearing of words does NOT block use; map misheard tokens
to the script words by position.

Apply next time:
- If `section-XX-word-timings.json` is missing, run the wtgen recipe before writing scenes.
- Always clamp scene-end to the real audio duration; check for backward jumps before pinning.
- Keep the plan's timing-source note explicit (file + extractor + date + clamp note).

Promote to shared memory:
no; pairs with the existing learning-log whisper line - this is the concrete working recipe
for visual-plan/render on this machine.

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Visual plan lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
