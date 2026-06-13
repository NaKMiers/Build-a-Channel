---
name: visual-plan
description: Create or update step 5 render-trustworthy section visual plans for a Why It Works video project. Use when the user asks for Visual Plan, visual planning, scene-by-scene or second-by-second what-when-how screen direction, big-scene and cue-state timeline, reference board, real-life internet visual references, generated support assets, WIT pose planning, HyperFrames build guidance, run step 5, or plan visuals for one section or all sections; requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 04-voiceover.md, explicit project selection, and explicit section selection with All as the first option, then writes only the project's 05-visual-plan.md, visual-plan/ section folders, and visual reference assets.
---

# Visual Plan

## Purpose

Run step `5` of the `Why It Works` video workflow.

Turn approved script and section voiceover into a section-level visual blueprint that is trustworthy enough for HyperFrames render to follow.

This is the most important handoff before render. Treat the work as a professional video editor and professional content creator would:

- decide exactly what appears on screen
- decide when it appears against the voiceover
- decide how it attracts attention, supports the joke, and explains the idea
- decide what assets HyperFrames needs before building
- use sourced real-world references first, then generated images only as support, fallback, or controlled production mockups
- make every big scene, cue state, visual asset, WIT pose, label, and markup decision useful enough that render can build from it without guessing

Do not treat this as a loose mood board. It is a timed scene plan, asset plan, humor plan, reference board, and render handoff.

The current standard is based on the approved Section 1 rebuild for `why-cheap-products-keep-getting-worse`:

```text
few persistent big scenes -> small voice-timed cue changes -> real/local assets -> readable emotional WIT -> screenshot/contact-sheet QA handoff
```

The Section 4 recovery for `why-cheap-products-keep-getting-worse` adds the default pattern for explanatory list sections:

```text
few strong real/object backgrounds -> compressed memory labels -> 3-4 giant WIT emotional beats -> no scattered object-card tray
```

When a script lists many small product details, do not give every noun its own card, image, arrow, or label. Collapse related items into one visual idea per big scene and one short label per cue unless the voiceover needs a specific proof object.

If a visual plan would still force `render` to invent the main scene, timing, joke, asset choice, WIT pose, or markup placement, the plan is not finished.

The plan must also prevent the most common render-review failures before they happen:

- too many full-scene cuts for a short section
- too many cue overlays appearing at once
- every text block animating instead of appearing calmly on beat
- WIT appearing on every cue or as a tiny corner sticker
- WIT face/head/shoulders accidentally cropped
- WIT covering labels, proof, or main objects
- payoff text, stamps, or labels covering WIT's face/expression when WIT is the emotional subject
- red markup that points nowhere or marks obvious details
- generated/real references reused even when adjacent scenes look too similar
- HyperFrames needing to guess timing, placement, asset choice, or motion type

This skill is section-first. After voiceover, production branches by section:

```text
Voiceover S1 -> Visual plan S1 -> Render S1 -> Review S1
Voiceover S2 -> Visual plan S2 -> Render S2 -> Review S2
...
```

Use `All` only when the user explicitly selects `All`.

## Pipeline Position

This is step `5` of the main video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`
- `projects/<slug>/04-voiceover.md`
- selected section voiceover output under `projects/<slug>/voiceover/`

Write or update:

- `projects/<slug>/05-visual-plan.md`
- `projects/<slug>/visual-plan/section-XX-kebab-section-name/`
- `projects/<slug>/assets/visual-references/section-XX-kebab-section-name/`

If a required upstream file is missing or empty, stop and tell the user which previous skill to run.

If `01-research-pack.md` is older than `00-topic-intake.md`, treat the research pack as stale and stop. If `02-script.md` is older than topic intake or research pack, treat the script as stale and stop. If `04-voiceover.md` or a selected section voiceover output is older than script, treat voiceover as stale and stop or ask whether to regenerate the affected section.

When this skill creates, updates, or reruns `05-visual-plan.md` or any file under `visual-plan/`, every later output for the affected section becomes stale.

List stale downstream files in chat. Do not silently delete them.

## Required Context

Read these before creating or updating visual plans:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/reference-channels.md`
8. `.agents/_shared/channel/learning-log.md`
9. `.agents/_shared/channel/codex-collaboration.md`
10. `.agents/_shared/channel/production-workflow.md`
11. `.agents/_shared/channel/brand-system.md`
12. `.agents/_shared/systems/topic-packaging-hooks.md`
13. `.agents/_shared/systems/script-learner-voice.md`
14. `.agents/_shared/systems/visual-production.md`
15. `.agents/_shared/systems/audio-feedback-quality.md`
16. `references/memory.md`
17. `references/output-formats.md` before writing outputs
18. the chosen project files:
    - `00-topic-intake.md`
    - `01-research-pack.md`
    - `02-script.md`
    - `04-voiceover.md`

Load additional files only when needed:

- `.agents/_shared/assets/wit/poses/manifest.json` when choosing WIT poses
- existing section visual plans from `projects/why-everyone-pretends-to-be-busy/` when the user asks to follow that reference style
- existing project `visual-plan/` section folders when updating a section

## Project Selection Gate

Always resolve the target project before planning visuals.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `04-voiceover.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find visual-plan candidates.

A visual-plan candidate has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `04-voiceover.md`
- at least one section voiceover output under `voiceover/`

When multiple candidates exist or context is unclear, ask the user to choose before writing.

Do not create a new project folder in this skill.

## Required Inputs Gate

Before section selection or writing files, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `04-voiceover.md`

If `02-script.md` does not contain parsable sections in the form:

```text
## Section N: Section Name
```

stop and ask the user to rerun `script-draft` or fix the script structure first.

If `01-research-pack.md` is older than `00-topic-intake.md`, stop and ask the user to rerun `research-pack`.

If `02-script.md` is older than `00-topic-intake.md` or `01-research-pack.md`, stop and ask the user to rerun `script-draft`.

If `04-voiceover.md` is missing, empty, or older than `02-script.md`, stop and ask the user to run or rerun `voiceover`.

## Section Selection Gate

Visual Plan must get an explicit target section before writing files.

The target must be selected by the user as `All` or as a specific section number/name in the current request or in the section-choice response.

Do not infer the target section from:

- active project state
- latest reviewed section
- next unfinished section
- existing visual plans
- missing visual-plan outputs
- prior chat context

Preferred option order:

1. `All`
2. `Section 1: <name>`
3. `Section 2: <name>`
4. Continue through the section list

Important:

- `All` means create or update each section as a separate visual-plan output.
- `All` does not mean one giant full-video visual plan unless the user explicitly asks for a macro plan.
- If option UI is available, show `All` first, then section choices.
- If option UI is unavailable, list numbered choices in chat and stop. Do not guess.

Fallback selection text:

```markdown
Choose visual plan target:

0. All sections
1. Section 1: <name>
2. Section 2: <name>
   ...
```

## Section Voiceover Gate

For each selected section, verify section voiceover exists before planning visuals.

Acceptable evidence:

- a matching section folder under `voiceover/section-XX-kebab-section-name/`
- and a clean script or marked script file
- and either an audio file or `scratch-results.json` that honestly records `tts not generated`
- and an entry in `04-voiceover.md`

If a selected section is missing voiceover output, stop and ask the user to run `voiceover` for that section first.

If the selected section voiceover files are older than `02-script.md`, treat that section voiceover as stale. Stop and ask the user to rerun `voiceover` for the selected section.

If the user selected `All` and some sections are missing voiceover, stop and list the missing sections.

## Request Modes

### Section Create Mode

Use when the chosen section has no existing section visual plan.

Create:

```text
projects/<slug>/visual-plan/section-XX-kebab-section-name/
projects/<slug>/visual-plan/section-XX-kebab-section-name/README.md
projects/<slug>/visual-plan/section-XX-kebab-section-name/section-XX-kebab-section-name-visual-plan.md
projects/<slug>/visual-plan/section-XX-kebab-section-name/reference-board.md
projects/<slug>/assets/visual-references/section-XX-kebab-section-name/
projects/<slug>/05-visual-plan.md
```

### Section Update Mode

Use when the user asks to revise, simplify, add real-life images, change WIT actions, adjust timing, improve HyperFrames guidance, or fix a plan after review.

Read the existing section visual-plan folder first. Preserve approved decisions unless the user explicitly asks to replace them.

If the user says a section is chaotic, too text-heavy, too image-heavy, too slide-like, or asks to remake it "like Section 1", treat both the current visual plan and downstream render for that section as stale. Rebuild the plan from script, voiceover, approved references, and current skill memory. Prefer sparse Section-1-style structure: `2-4` persistent backgrounds, `5-8` cue states for a `30-45s` explanatory section, one or two short labels per cue, and WIT only on the emotional beats.

### All Sections Mode

Use when the user chooses `All`.

Create each section as its own output using Section Create or Section Update rules.

Do not collapse the whole video into one giant scene/cue table unless the user explicitly asks for a macro visual plan.

### Improve Memory Mode

Use when the user reviews a visual plan and gives reusable lessons.

Update in this order:

1. the project `05-visual-plan.md` or section visual plan if the review affects this video
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves the whole channel

Promote shared lessons with a clear classification such as `Operational lesson` or `Core production system`.

## Render-Trustworthy Planning Contract

The output must be something `render` can follow directly.

Every selected section must include these four layers:

1. `Big Scene Plan`
   - persistent base scenes that hold for multiple narration beats
   - one main visual object/place/mechanism per big scene
   - reason for cutting to the next big scene
2. `Cue State Timeline`
   - voice-timed cue states inside each big scene
   - exact local start/end times or approximate times derived from section duration
   - what changes on screen at each cue
   - what stays on screen from the big scene
   - whether each cue should hard-show, smash/stamp/pop for emphasis, or stay static
3. `Reference And Asset Plan`
   - real/local/generated references for each big scene
   - production decision for each asset: direct asset, mockup target, support base, inspiration only, or reject
   - saved paths/prompts/source notes
4. `Render Handoff`
   - composition target
   - expected cue-state count
   - WIT pose files and scale/placement guidance
   - WIT safe-crop guidance: face/head/shoulders and important props must not look accidentally cut
   - exact labels and markup jobs
   - motion density rule: ordinary labels hard-show on beat; impact motion only for emphasized beats
   - asset paths
   - inspect timestamps and screenshot/contact-sheet QA timestamps; MP4 QA timestamps only when export is explicitly requested
   - list of things HyperFrames must not invent

### Big Scene And Cue State Rules

Use big scenes first, not disconnected boards.

Definitions:

- `Big scene`: the persistent base image/illustration/layout that stays while the narration describes the same object, situation, place, or mechanism.
- `Cue state`: a small timed change inside the big scene, such as a short label, WIT reaction, arrow, hidden tag, one prop, or red correction.

For a `20-25s` hook, default to:

```text
3 big scenes
6-8 cue states
```

For longer sections, scale by idea density, not sentence count. Several sentences can share one cue state when they describe the same object or situation.

For explanatory list sections, first ask which `2-4` visual memory frames the viewer should remember. Lists of parts, features, costs, promises, or hidden support systems should usually be compressed into category labels rather than itemized on screen. Example: `fabric + stitching + hinge` can be one support label on a fabric background; `battery + screw + spare part` can become one repairability scene. If the section starts looking like a vocabulary worksheet or product-parts inventory, reduce cue count before adding more references.

Cut to a new big scene only when:

- the narration moves to a new object, place, mechanism, evidence type, or payoff
- the existing scene can no longer explain the current line clearly
- the viewer needs a visual reset for clarity or joke timing

Do not create a new full-screen scene just because a new sentence begins.

When a section has multiple big scenes, run a visual differentiation check before handoff. Non-callback scenes should not reuse the same background, object arrangement, camera language, or material mood just because a collected reference exists. Reuse a base only for purposeful continuity or payoff memory; otherwise plan a distinct scene base.

### Voice Timing Rules

The plan must map visuals to the selected section voiceover.

Use this priority:

1. exact transcript/word timestamps if available
2. marked script pauses and beats plus section audio duration
3. proportional timing from sentence length and known voiceover duration

If exact word timing is unavailable, estimate honestly and label timing as `estimated`.

Every cue state must include:

- local start/end time
- voice cue phrase
- on-screen change
- hold duration
- planned motion type: `static`, `hard-show`, `impact`, or `transition`
- reason the cue exists

The first `3s` of a hook must show the topic object/situation.
The first `5-6s` of a hook should show the contradiction or hidden detail when the section depends on one.

### Motion Intent Rules

Visual-plan must decide motion intent before render writes HTML.

Use these categories:

- `static`: element is present for the whole cue or scene.
- `hard-show`: element appears instantly on the spoken beat.
- `impact`: element uses a short smash, stamp, shake, pop, snap, or marker action.
- `transition`: scene-level movement between persistent big scenes.

Default to `hard-show` for ordinary labels, notes, props, and WIT appearances. Use `impact` only for emphasized spoken words, proof marks, contradiction labels, and payoff phrases. Do not ask render to animate every sequential label.

### WIT Planning Rules

Use only real channel WIT PNG pose files from:

```text
projects/<slug>/assets/wit/manifest.json
```

or the approved shared WIT manifest if the project does not have its own WIT folder.

For each WIT appearance, specify:

- exact pose file
- emotion
- local time range
- screen region
- visible footprint target, measured by the visible WIT character in the final frame, not by the PNG/CSS box
- creative placement concept, such as corner peek, upside-down top entrance, hiding behind a product/wardrobe/tag/box/screen, looming from behind an object, or half-body rise from an edge
- safe crop rule: face/head/shoulders and important props fully readable unless intentionally peeking
- why WIT is needed

WIT is useful on emotional beats: suspicion, betrayal, panic, confusion, judgment, evidence, trapped, payoff.

Do not use WIT as filler in every cue state.
Do not plan WIT for every cue just because the pose library has enough poses. For short sections, default to about `1-2` WIT beats per persistent big scene, then adjust only if the voice rhythm needs more emotional reactions.
Do not draw WIT in HTML/SVG/CSS.
Do not invent random WIT.
If WIT is planned for an emotional beat, its visible character footprint must occupy at least `1/3` of the frame in the planned screenshot/contact-sheet frame. This means the visible WIT body/face area, not the transparent PNG bounds or CSS box. Default to `1/3` to `1/2` of the frame, and go larger when it strengthens the joke without blocking labels or evidence.
Do not default to full-body WIT standing in a lower corner. For strong reaction/payoff beats, plan Section-1-style giant WIT placements: behind-layer oversized faces, half-body entrances from the lower edge, side peeks, WIT appearing from a corner, upside-down WIT dropping from the top, WIT hiding behind a wardrobe/product/tag/box/screen, WIT looming beside the main object, or cropped lower-body compositions that make the emotion dominate the frame.
Intentional WIT crop is allowed only for body/legs/edge peeking. Never plan a crop that cuts through WIT's face, glasses, head, shoulders, mouth, key prop, or readable emotion. If a contact-sheet frame would make WIT look accidentally broken, the plan must choose a different placement, scale, or pose.
When WIT is the emotional subject of a payoff or reaction beat, plan a clean WIT emotion zone. Payoff text, stamps, tags, and labels must not cover WIT's face, eyes, mouth, or key prop; solve this with separate screen regions, not by hoping render can layer around it later.
If the current approved pose library cannot express the beat, plan a new WIT pose asset and save it into the shared/project WIT asset library instead of settling for a weak pose.

Every WIT plan must include a density note:

- total WIT beats in the section
- WIT beats per big scene
- why any big scene exceeds `2` WIT beats
- which cue states intentionally have no WIT so the section can breathe
- which screenshot/contact-sheet timestamps must prove each emotional WIT beat reaches at least `1/3` visible frame presence

### Markup And Label Rules

Labels and red markup must explain the narration.

Use:

- short handwritten labels
- one key label per cue state when possible
- red markup only for exact evidence, correction, reveal, or punchline
- arrows/circles only when they point to a specific real object or detail
- hard-show timing for ordinary sequential labels
- smash, stamp, shake, or pop only for words the voice truly emphasizes or for payoff/evidence beats

Avoid:

- meaningless red boxes/circles/leg marks
- marking an obvious detail just because the voice names it
- labels that repeat the narration without adding clarity or joke value
- animating every label merely because it appears sequentially
- white wash overlays over real/object photos unless required for readability

If the image already proves the point, use a label instead of decorative annotation.

### Review-Prevention Checklist

Before writing the final section visual plan, run this self-check and fix the plan if any answer is weak:

- Voice sync: does every cue map to the phrase that triggers it?
- Big-scene rhythm: does a short hook avoid sprinting through unrelated full-screen boards?
- Cue density: does each cue add only one or two meaningful changes?
- Motion density: are ordinary labels planned as `hard-show`, not animated decoration?
- Emphasis: are smash/stamp/pop actions reserved for words or proof the voice stresses?
- WIT rhythm: does WIT appear only where the emotion changes or peaks?
- WIT size: does each emotional WIT beat visibly occupy at least `1/3` of the frame in the planned screenshot/contact-sheet frame?
- WIT placement: if this is a strong emotion beat, is WIT treated as the emotional subject with a creative giant placement instead of a small lower-corner sticker?
- WIT crop: are face/head/shoulders and important props safely inside frame, with only body/legs/edge peeks intentionally cropped?
- Text/WIT collision: does WIT avoid covering labels, main evidence, and payoff text, and do payoff text/stamps avoid covering WIT's face/expression?
- Subtitle-safe layout: do important lower-third labels, receipts, stamps, arrows, boxes, and payoff props sit high enough that typical YouTube subtitles will not cover them?
- Markup meaning: does every arrow/circle/underline point to a real target and explain the line?
- Visual differentiation: do non-callback big scenes avoid repeating the same visual language?
- HyperFrames readiness: can render build without inventing main scenes, timing, WIT choices, label text, markup placement, or motion type?

## Browsing And Asset Rules

Use the project-local `browse` skill for web or YouTube browsing when available.

Every selected section must run a visual reference pass before writing the final section visual plan.

The default order for the visual reference pass is:

1. real, sourced images from web search, image search, YouTube/reference-channel review, self-shot photos, or existing local assets
2. generated images only to fill gaps, create clean production-safe mockups, remove logos/text/private data, or test a composition
3. prompt-only references only as a degraded fallback

The reference pass must support the `Big Scene Plan`, not a random mood board.

For every planned big scene, collect or create enough visual evidence to answer:

- what the base image/illustration should look like
- what object/material/texture makes it feel real
- where labels and WIT can sit without blocking the main object
- which detail needs markup, if any
- whether the asset is safe for direct production or only a mockup/inspiration target

The visual reference pass must include at least one of:

- browsed web or image references for real objects, UI patterns, materials, composition, or visual benchmarks
- generated section-specific reference images
- self-shot or existing local visual assets that are inspected and documented

For normal runs, actively look for real-life internet or local images first. Do not make generated images the main visual reference layer when useful real images can reasonably be found.

If a selected section uses zero real images, the `reference-board.md` must explain why real images were unavailable, unsafe, irrelevant, or lower quality than the generated/self-made alternative.

For normal runs, use at least `3` useful references per selected section:

- one real-life/object/material reference
- one composition, editing, or attention reference
- one asset or mockup reference that HyperFrames can build from

For hooks and high-retention moments, prefer `4-6` references unless the section is extremely simple.

For render-ready plans, references should map to big scenes:

- at least one usable visual basis for each big scene
- one clear candidate base asset or generated-support prompt for each big scene
- at least one WIT/label placement note for each WIT-heavy big scene

Prompt-only references are allowed only as a degraded fallback when browsing and image generation are unavailable, fail, or would create unsafe assets. If using prompt-only fallback, state the reason in `reference-board.md` and in the chat response.

Do not skip the visual reference pass just because an object seems easy to draw. Even simple objects need visual certainty: silhouette, material, pose, camera angle, label placement, and readable contrast.

Use `.agents/_shared/channel/reference-channels.md` as the source-base for channel inspiration. When a section needs pacing, hook, humor, retention, or framing guidance, browse or review `1-3` relevant reference-channel examples and mark them as `inspiration only`. Learn from timing, board simplicity, and joke rhythm. Do not copy their exact frame, thumbnail, joke layout, or visual composition.

For each selected section, create a small reference board:

- real-life objects that explain the section
- real internet/self-shot/local images that make the video feel close to the viewer
- possible safe assets
- generated-image ideas only after real reference needs are understood
- self-made UI/mockup targets
- visual benchmark or editor-reference notes
- attention / retention reason for using each reference
- inspiration-only references
- rejected references
- source notes

Classify every reference as:

- `safe asset`
- `mockup target`
- `inspiration only`
- `reject`

Do not copy another creator's exact frame, thumbnail, joke layout, screenshot, or visual composition.

Prefer:

- self-shot images
- licensed/public-domain images
- real internet images with clear source and license notes
- generated images for support, cleanup, or missing-safe-asset cases
- self-made UI mockups
- simple object cutouts
- paper, receipts, phones, desks, product boxes, calendars, bills, or other lived-in objects

Avoid:

- private data
- unclear copyrighted images
- real app logos unless explicitly approved
- real screenshots copied into production
- generic stock images that do not explain the section

When image generation is available, generate or request section-specific reference images only when they materially improve the plan after the real-reference pass. Save generated references or returned image paths under:

```text
projects/<slug>/assets/visual-references/section-XX-kebab-section-name/
```

If generation is unavailable, write reusable generation prompts and mark status as `prompt only / image not generated`.

Generated or browsed images are not automatically production assets. Classify them first. Use them to clarify shape, mood, composition, or material. Only use them directly in production if their source and license are safe.

Collected references are allowed to be inspected and skipped. Do not plan direct use of an image merely because it was downloaded or generated. If it does not improve the end viewer result, mark it as reference-only, fallback, inspiration, or reject.

Generated images should normally be text-free and logo-free. Add labels, prices, UI text, red markup, and jokes in HyperFrames so timing and readability can be controlled.

When generating support images for render, write prompts that specify:

- object and camera angle
- simple uncluttered composition
- empty label-safe areas
- no text, logos, watermarks, brand marks, or private data
- realistic texture if the section is object-driven
- 16:9-friendly framing unless the render needs a cutout or transparent object

For real internet images, record:

- source page URL
- creator/credit when visible
- source/license status when visible
- direct saved path if downloaded
- production decision: direct asset, crop/blur/trace target, inspiration only, or reject

If a real image has unclear copyright, visible private data, real logos, or accidental brand accusation risk, classify it as `inspiration only` or `reject`, not `safe asset`.

## Visual Planning Rules

Work from the role of an editor, not a document writer.

For every selected section, plan the visual experience as:

```text
what appears on screen -> when it appears -> how it moves / cuts / reveals -> why the viewer keeps watching
```

Use the channel grammar:

```text
static drawing -> narration twist -> red markup or hard cut -> next static drawing
```

Each big scene should carry:

- one persistent object, situation, place, mechanism, or payoff
- one clear visual job
- one attention reason
- one reference basis
- one safe asset/build path

Each cue state should carry:

- one timed voice cue
- one small visual change
- one readable label or markup job when needed
- optional WIT emotion only when useful
- one reason it exists

Visual plans should guide HyperFrames implementation, not replace it.

For each selected section, plan:

- section goal
- viewer attention strategy
- section retention risk and visual fix
- narration beats
- big scene list with local timing from the section voiceover
- cue state list with exact/estimated local timing inside each big scene
- exact on-screen what / when / how / why for every big scene and cue state
- exact where each visual resource appears: big scene/cue number, time range, screen region, crop/placement, and whether it is direct asset, mockup target, support base, or inspiration only
- visual job per big scene and cue state
- joke or curiosity beat per cue state
- real-life or generated asset needs
- WIT pose/emotion per cue state, including exact PNG file when possible
- labels and handwritten captions
- red markup or joke beat
- motion notes
- voice-sync cues
- asset/source safety notes
- render / HyperFrames implementation guidance
- screenshot/contact-sheet QA timestamps for render to verify
- MP4 QA frame timestamps only when the user explicitly requests an export
- approval checks

Keep scenes simple. When a section gets abstract, return to a concrete object.

Use WIT as the audience surrogate. WIT should usually be affected by the system, not lecturing from outside it.

The plan fails if HyperFrames would need to invent the main scene, object, timing, joke, or asset logic from scratch.

The plan also fails if it creates too many full-scene cuts for a short section. Good visual pacing comes from a base scene evolving through small cue changes, not from sprinting through unrelated images.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Parse `02-script.md` sections.
4. Run the Section Selection Gate.
5. Run the Section Voiceover Gate for selected sections.
6. Read required shared context and skill memory.
7. For each selected section:
   - extract section narration from `02-script.md`
   - read the matching section voiceover files
   - inspect voiceover duration or timing notes when available
   - identify the section goal, contradiction, visual metaphor, and WIT emotion
   - run the Visual Editor Pass:
     - split narration into voice cue phrases
     - group related cue phrases into persistent big scenes
     - decide the target big-scene count and cue-state count before writing scene details
     - decide attention hook, retention risk, joke rhythm, and visual payoff
     - decide what must be shown, when it appears, and how it changes on screen
     - remove cue states that only repeat the narration without adding clarity, evidence, emotion, or joke value
     - mark each cue state with a motion type: `static`, `hard-show`, `impact`, or `transition`
   - run the Visual Reference Pass:
     - browse for real-life internet images, object/material references, UI patterns, or visual benchmarks for each big scene first
     - inspect/download useful real images only when source safety is acceptable
     - generate section-specific images only when they improve clarity, humor, source safety, or asset certainty after the real-reference pass
     - save generated references when available under the section visual reference folder
     - classify browsed/generated/self-made references before using them
     - document any prompt-only fallback as a degraded fallback
   - run the WIT Pass:
     - inspect the project `assets/wit/manifest.json` when present, otherwise inspect approved shared WIT manifest
     - choose exact WIT pose filenames only for cue states that need emotional clarity
     - count WIT appearances per big scene and reduce them if WIT starts reacting to every cue
     - specify placement and scale large enough for facial emotion to read
     - specify crop guard and label/evidence collision risk for every WIT beat
   - run the Markup Pass:
     - specify only meaningful labels, arrows, circles, stamps, or red corrections
     - delete decorative or obvious marks
     - define exact target object for every callout
   - run the Render Handoff Pass:
     - list big scenes and cue states with local timestamps
     - list WIT density, motion density, and known no-WIT breathing beats
     - list asset paths/prompts and what render must not invent
     - list suggested `inspect --at` timestamps
     - list suggested screenshot/contact-sheet QA timestamps, including any likely problem frames
     - list MP4 QA frame timestamps only when export is explicitly requested
   - run the Review-Prevention Checklist and revise before handoff
   - write `reference-board.md`
   - write `section-XX-kebab-section-name-visual-plan.md`
   - write or update the section `README.md`
8. Write or update `projects/<slug>/05-visual-plan.md` as the section visual-plan index.
9. Run the Downstream Stale Gate.
10. Respond with the Chat Response Format.
11. Stop before render, review, upload, or learning unless explicitly asked.

## Output Folder Standard

Section folder naming:

```text
visual-plan/section-XX-kebab-section-name/
```

Examples:

```text
visual-plan/section-01-hook/
visual-plan/section-02-cheap-is-not-the-villain/
visual-plan/section-06-repair-gets-a-security-system/
```

File naming:

```text
section-XX-kebab-section-name-visual-plan.md
reference-board.md
README.md
```

Use lowercase kebab-case.

## Output Formats

Use `references/output-formats.md` for the exact templates for:

- `05-visual-plan.md`
- section visual-plan files
- section `reference-board.md`
- section `README.md`
- chat response

If only one section has been planned, include remaining sections in `05-visual-plan.md` as `not planned`.

## Downstream Stale Gate

After creating, updating, or rerunning `05-visual-plan.md` or any section visual plan, check the same project for downstream files:

- `06-production-board.md`
- `hyperframes/`
- `renders/`
- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`

If any exist, list them as stale in chat and tell the user they should be removed or regenerated by rerunning downstream skills in order, starting with `Render`.

Do not delete downstream files unless the user explicitly asks.

For section-level projects, note whether the stale output affects the selected section, all sections, or is unclear.

## Chat Response Format

After creating or updating visual plans, respond with a short summary.

Do not paste the full visual plan unless the user asks.

Use this structure:

```markdown
Done. I created/updated:

[05-visual-plan.md](<absolute path>)

Section target: `<All or Section X: name>`

Status: `<status>`

Generated:

| Section | Status | Big Scenes | Cue States | Reference assets | Section plan |
| ------- | ------ | ---------: | ---------: | ---------------- | ------------ |

Notes:

- <line 1>
- <line 2>
- <line 3>

Stale downstream:

- <file or none>
```

## Quality Bar

A section visual plan is ready when:

- selected section was explicitly chosen
- selected section has matching voiceover output
- section goal is clear
- big scene plan maps to narration structure and voiceover duration
- cue state timeline maps to narration beats and voiceover timing
- each big scene states what persists, when it starts/ends, why it exists, and when to cut away
- each cue state states what changes, what stays, when it appears, and why it exists
- each cue state has a motion type: `static`, `hard-show`, `impact`, or `transition`
- cue count is intentionally low enough for the section duration
- WIT emotion supports the viewer's feeling
- WIT pose filenames, placement, and scale guidance are included when WIT appears
- emotional WIT beats specify a visible WIT footprint of at least `1/3` of the frame, measured by visible character area rather than CSS/PNG bounds
- strong WIT emotion beats are planned as emotional subjects, not small full-body lower-corner stickers
- WIT density is counted and justified per big scene
- WIT crop and text/evidence collision risks are handled
- ordinary labels use hard-show unless emphasis needs impact motion
- labels are short and readable
- red markup and callouts have exact target objects and are not decorative
- the visual reference pass produced browsed, generated, inspected local, or clearly degraded prompt-only references
- real-life, benchmark, and generated references are classified with source notes
- references map to big scenes and buildable asset decisions
- generated images, browsed images, or prompts are marked honestly
- HyperFrames guidance is concrete enough to build from without inventing scene timing, asset choices, WIT, or markup
- suggested `inspect --at` and screenshot/contact-sheet QA timestamps are included
- script promise is paid off in the section when relevant
- stale downstream files are listed
- no render, review, upload, or learning files are created

## Hard Fails

Reject or stop before finishing if:

- the project lacks `04-voiceover.md`
- the selected section lacks voiceover output
- the user has not explicitly selected `All` or a specific section
- the section target is inferred instead of selected
- the skill plans a section from stale script or voiceover
- the visual plan copies another creator's frame or thumbnail structure
- the skill skips the visual reference pass without documenting a failed/unavailable fallback
- the skill defaults to generated images without first trying useful real-world references
- the reference board is prompt-only while browsing or image generation was available and safe
- the plan does not include a big scene plan and cue state timeline
- the cue timeline creates too many unrelated full-scene cuts for a short section
- cue states are based on sentence count instead of visual idea changes
- a cue state has no clarity, evidence, emotion, or joke reason to exist
- a list-style narration becomes a scattered tray of mini cards, images, arrows, or labels instead of a few memory frames
- red markup is decorative, meaningless, or does not target a specific object
- the plan does not map every important visual resource to what / when / how / where usage
- HyperFrames would need to invent the main visual idea, asset list, or timing
- HyperFrames would need to choose WIT pose files, WIT scale, label text, or markup placement from scratch
- real private data or unclear copyrighted screenshots are treated as production assets
- generated images are described as existing when they were only prompted
- WIT is decorative and has no emotional job
- WIT is planned for every cue without a voice-rhythm reason
- a short section exceeds `2` WIT beats in a big scene without a clear reason
- WIT appears without a real approved pose filename when WIT assets exist
- WIT is planned too small to read facial emotion
- emotional WIT is planned below `1/3` visible frame presence without an explicit user-approved tiny/background reason
- WIT is planned as a small lower-corner sticker on a beat where WIT should carry the main emotion
- WIT crop would make the character look broken
- WIT would cover the main label, proof object, or payoff text
- payoff text, stamps, tags, or labels would cover WIT's face/expression in the emotional beat
- ordinary labels are planned with repeated fly-ins/smashes that create visual noise
- labels are too long for a paused cue state
- big scenes or cue states are too crowded to understand
- real/object photos are globally washed out with white overlays without a documented readability reason
- generated-image prompts include text, logos, watermarks, or brand marks without an explicit safe reason
- the skill creates render, review, upload, or learning files

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user approves or rejects a visual-plan style
- a reference-board approach works or fails
- generated images help or hurt clarity
- a later HyperFrames build exposes missing planning details
- a review shows recurring timing, label, WIT, or asset problems
- the user clarifies how section branching should behave

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify each promoted lesson as `Core`, `Experiment`, `Operational lesson`, or `Reject` according to `.agents/_shared/channel/channel-guardrails.md`.

Do not rewrite channel foundation, audience, tone, WIT direction, or product-promotion boundary from one visual-plan run without explicit user confirmation.
