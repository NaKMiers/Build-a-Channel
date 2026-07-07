# Render Skill Memory

This file stores memory specific to the `render` skill.

Use `.agents/_shared/` for channel-wide visual rules, audio rules, WIT identity, and HyperFrames-first production strategy.
Use this file for section preview structure, port behavior, HyperFrames CLI habits, server handling, and lessons about making section builds easier to review.

## Current Skill Standard

- Run after `visual-plan`.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, `02-script.md`, the voiceover index (`03-voiceover.md`; legacy `04-voiceover.md`), and the visual-plan index (`04-visual-plan.md`; legacy `05-visual-plan.md`). Resolve by suffix per `.agents/rules/video-workflow.md`.
- Require matching section voiceover output and matching section visual-plan output.
- WIT poses are TRANSPARENT RGBA cutouts in the shared library (keyed in place 2026-06-28): copy/reference them DIRECTLY from `assets/poses/`. No chroma-key step at render, no `poses-keyed` folder.
- Require ALL of the selected section's assets ready before building (owner-confirmed 2026-06-28): check `assets/asset-manifest.md`, confirm every referenced asset is a file present in `assets/` (or `assets/poses/`) or explicitly render-CSS; if any is missing on disk or marked `prompt-ready / awaiting generation` / `awaiting drop`, STOP and tell the user to finish `visual-implement` for those assets - do NOT source/generate/substitute them yourself (only when the user explicitly asks for a specific asset this run). See the All Section Assets Ready Gate in SKILL.md.
- Do not require `03-packaging.md`; packaging is a side branch.
- Require explicit user section selection: `All` or a specific section.
- Build one HyperFrames preview project per section. NEW projects (folder convention changed 2026-06-30): under `previews/<N>-kebab-section-name/` (folder `previews/`, unpadded number, e.g. `1-hook`, `2-it-has-a-name-slop`). LEGACY projects keep `section-previews/section-XX-kebab-section-name/`. Do not rename existing folders unless asked; resolve a section by checking `previews/<N>-*/` first, then legacy `section-previews/section-XX-*/`. See Output Folder Convention in SKILL.md.
- Never put all sections into one localhost during section review.
- Use port `1000 + section number` for section preview:
  - Section 1 -> `1001`
  - Section 2 -> `1002`
  - Section 3 -> `1003`
- Reserve port `1000` for unified/final preview only.
- If the required port is occupied by the correct section server, reuse it.
- If the required port is occupied by an unrelated process, stop and report the conflict.
- Use one video-level shared asset library at `projects/<slug>/assets/`.
- Use local section `assets` junctions instead of copied asset folders.
- Keep asset filenames SHORT (kebab `<subject>-<n>.jpg`); put photographer/source/license in `ATTRIBUTION.md`, not the filename. Long descriptive+attribution filenames nested under `section-previews/section-XX-.../assets/visual-references/section-XX-.../...` overflow Windows `MAX_PATH` and break `git add` (`Filename too long`). Do not repeat the long section slug twice in one path.
- HyperFrames preview/Studio and `snapshot` generate a `.thumbnails/` cache that MIRRORS the asset tree under the preview folder - these are the deepest, longest paths in the repo. They are regenerable and `.gitignore`d; never commit them. If a `git add` fails on a long path, it is almost always a `.thumbnails/` file - delete the `.thumbnails/` dirs (`find . -type d -name .thumbnails | xargs rm -rf`) and re-add.
- Inspect real-world visual references and source notes from the selected visual plan before using generated support assets.
- Treat generated images as controlled support bases unless the visual plan explicitly approves them as primary.
- Before using a planned image as a direct scene base, compare it against adjacent big scenes. If a non-callback scene repeats the same background, object setup, camera language, or material mood, rebuild it as a more distinct CSS/self-made/generated scene and document the reason.
- Do not force every collected reference image into production. Inspect each image, use it only if it improves the final viewer result, and mark skipped images as reference-only in attribution and implementation notes.
- Do not use `inspiration only` or `reject` real images directly in final render output.
- Require a voice cue map before animation: every scene and on-screen element must match the current voiceover beat.
- Build hard-cut timing first. Add transitions only after the section matches the voiceover.
- Choose transitions per scene boundary. Do not reuse one default transition everywhere.
- If a transition damages voice sync, simplify it or use a hard cut.
- Design element entrance, hold, emphasis, and exit against spoken cues.
- Emphasized spoken words such as `FREE`, `URGENT`, or `BUSY` should get matching visual emphasis when they are important to the beat.
- Keep a subtitle-safe lower area. Important lower-third labels, receipts, stamps, arrows, boxes, and payoff props should usually sit a bit above the bottom edge so YouTube subtitles do not cover them.
- If the user manually edits a localhost/HyperFrames Studio preview, preserve the current section `index.html` as canonical. Diff before editing, do not overwrite from review mirrors or older plans, and remove only targeted accidental artifacts such as unreferenced VFX blocks or duration extensions.
- Do not create MP4/WebM files during normal render, preview, animation, timing, QA, or review-fix work. Only export video files when the user explicitly asks to export video, render an MP4/WebM, or create a video file.
- Stop before review, upload, or learning unless explicitly asked.

## Output Standard

For each selected section, create or update (NEW-project paths; legacy projects use `section-previews/section-XX-kebab-section-name/`):

- `previews/<N>-kebab-section-name/index.html`
- `previews/<N>-kebab-section-name/DESIGN.md`
- `previews/<N>-kebab-section-name/package.json`
- `previews/<N>-kebab-section-name/hyperframes.json`
- `previews/<N>-kebab-section-name/assets` junction to `../../assets`
- `hyperframes/review/section-XX.html`
- the production board file (`05-production-board.md`; legacy `06-production-board.md`)

Explicitly requested MP4/WebM section exports belong under:

- `renders/section-XX-kebab-section-name/`

## Feedback Log

### 2026-06-07 - Skill Created

Classification: `Core operational capability`

Context:
The user clarified that the skill should be named `Render`, use HyperFrames, and create one localhost per video section for easier adjustment. Unified final preview should use port `1000`.

Lesson:
Render must be section-first. Each section gets its own HyperFrames preview project and fixed port. Do not combine sections during section review.

Apply next time:
Use section port `1000 + section number`, reserve `1000` for unified preview, and write section build status into the production board file (`05-production-board.md`; legacy `06-production-board.md`).

Promote to shared memory:
Yes, as an operational production lesson.

### 2026-06-07 - Voice Sync Before Effects

Classification: `Render lesson`

Context:
The user reported that prior HyperFrames renders often showed scene elements that did not match the voiceover. Transitions also caused timing mismatch even when hard cuts were timed correctly.

Lesson:
Render must treat every scene and element as a visual description of the current voiceover beat. Build a hard-cut timing pass first, verify it against the audio, then add transitions only where they improve continuity without moving the perceived cue.

Apply next time:

- create a voice cue map before animation
- remove elements that explain earlier or later lines
- make cue-critical labels readable on the spoken cue frame
- rewatch after transitions and adjust timing
- remove or simplify any transition that hurts sync

Promote to shared memory:
No. Keep in Render skill memory unless repeated across multiple skills.

### 2026-06-07 - Transition And Element Motion Must Be Designed

Classification: `Render lesson`

Context:
The user noted that repeated default transitions make the video feel mechanical, while the best transition makes two scenes feel like one connected movement. The user also wants emphasized words to get matching visual action, such as `FREE` landing with a smash animation.

Lesson:
Transitions and element motion must be selected per beat. Avoid one transition effect for all screens. Design how each meaningful element appears, holds, emphasizes, and disappears in relation to the voiceover.

Apply next time:

- choose each transition based on continuation, reveal, contrast, cause/effect, punchline, or reset
- use hard cuts where transitions hurt clarity
- vary label entrances and emphasis animations
- tie emphasis actions to the spoken word
- avoid decorative motion while viewers need to read the main point

Promote to shared memory:
No. Keep in Render skill memory unless it becomes a channel-wide production rule.

### 2026-06-07 - Render Must Respect Real-Image-First Visual Plans

Classification: `Render lesson`

Context:
The user clarified that real internet images should be prioritized because they make videos feel closer to viewers. Visual-plan now classifies real images as safe assets, mockup targets, inspiration only, or reject.

Lesson:
Render should inspect the selected section's `real-world/` references and source notes before choosing generated assets. Generated images are useful as clean production bases, but they should be informed by real object texture and should not replace real references by default.

Apply next time:

- read `reference-board.md` and `source-notes.md`
- use `safe asset` real images directly only with required attribution/source notes
- recreate or cover risky `mockup target` images
- use `inspiration only` images for texture/composition only
- document direct production assets in `projects/<slug>/assets/ATTRIBUTION.md`

Promote to shared memory:
no; shared visual-production rules already contain the channel-wide standard.

### 2026-06-07 - HyperFrames CLI Did Not Serve Junction Assets On This Setup

Classification: `Operational lesson`

Context:
Section 1 Hook for `why-cheap-products-keep-getting-worse` used the approved preview-local `assets` junction first, but `hyperframes validate` returned repeated image 404s even though the junction resolved correctly in PowerShell.

Lesson:
Keep `projects/<slug>/assets/` as the source of truth, but if HyperFrames CLI checks fail to serve a section preview's junction-backed `assets/` folder on this Windows setup, materialize a minimal preview-local hardlinked asset working set for only the files used by that section and document the exception in the production board file (`05-production-board.md`; legacy `06-production-board.md`).

Apply next time:

- try the normal local `assets` junction first
- if CLI checks return asset 404s while the filesystem path resolves correctly, replace the section preview's local asset runtime with a minimal hardlinked working set
- hardlink only the files used by that section, not the entire project asset tree
- keep the project asset library and attribution file as the source of truth
- record the workaround in the section implementation notes and production board

Promote to shared memory:
no; this is an environment-specific HyperFrames runtime note, not a channel-wide production rule.

### 2026-06-08 - Failed Visual Plans Need A Style Override Path

Classification: `Render lesson`

Context:
The user rejected Section 1 of `why-everyone-pretends-to-be-busy` because it felt like bad presentation slides with mismatched transitions and voiceover. The user explicitly asked to delete the failed Section 1 HyperFrames render and rebuild from Casually Explained reference analysis instead of following the old Section 1 visual plan.

Lesson:
When the user says the visual plan is the likely failure source, render should not keep polishing that plan. Treat the visual plan as stale for the selected section, delete only the failed render artifacts the user names, rebuild from script plus voice timing plus approved reference analysis, and document the override in the project implementation notes.

Apply next time:

- ask whether the visual plan should be skipped only if the user has not already said so
- remove stale section preview artifacts before rebuilding
- use hard-cut timing first
- keep the replacement style sparse enough that paused frames read clearly
- document which source replaced the visual plan

Promote to shared memory:
no; keep in render memory until this override path is approved across more than one rebuild.

### 2026-06-08 - Render Must Use The Real WIT Pose Library

Classification: `Render lesson`

Context:
The user rejected the second Section 1 replacement for `why-everyone-pretends-to-be-busy` because the rendered WIT was not the channel's WIT and the section still felt messy. The user pointed to the complete WIT pose library in `projects/1-why-cheap-products-keep-getting-worse/assets/wit` and asked for a complete remake.

Lesson:
Do not draw, approximate, or improvise WIT inside HyperFrames when approved WIT pose PNGs exist. Copy or junction the current WIT library into the active project, use only the pose files listed in its manifest for new work, and reserve WIT for emotional beats rather than every board.

Apply next time:

- inspect the active WIT manifest before building section HTML
- use actual WIT PNGs for reactions, pointing, panic, thinking, and payoff beats
- keep simple illustrated objects in CSS or generated images around WIT
- verify direct preview screenshots, not just Studio playback; use exported MP4 frames only when the user explicitly asked for video export
- if using a web font, store the correct Latin subset locally and confirm the iframe reports the font as loaded

Promote to shared memory:
no; keep in render memory unless repeated across more sections.

### 2026-06-08 - Windows Render Needs npm.cmd And Temporary FFmpeg

Classification: `Operational lesson`

Context:
While remaking Section 1 for `why-cheap-products-keep-getting-worse`, HyperFrames checks worked but MP4 render failed because `ffmpeg` and `ffprobe` were not on PATH. Running `npm run check` also failed under PowerShell because `npm.ps1` execution is disabled.

Lesson:
On this Windows setup, use `npm.cmd` instead of `npm` for scripts. If no system FFmpeg exists, install `ffmpeg-static` and `ffprobe-static` into a temp folder, then prepend both binary folders to PATH for the render and verification commands.

Apply next time:

- run checks with `npm.cmd run check`
- install temp render binaries with `npm.cmd install --prefix $env:TEMP/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static`
- set PATH to include `node_modules/ffmpeg-static` and `node_modules/ffprobe-static/bin/win32/x64`
- avoid HTTP audio-helper URLs for rendered MP4s; use a local audio file path when possible

Promote to shared memory:
no; this is environment-specific render setup.

### 2026-06-11 - Preserve Manual Studio Edits Before Cleanup

Classification: `Operational lesson`

Context:
During Section 1 of `why-cheap-products-keep-getting-worse`, the user manually adjusted the localhost/HyperFrames Studio preview and then accidentally added a `vfx-liquid-glass` registry composition that extended the section by about `20s`.

Lesson:
When the user reports manual Studio edits, the live preview `index.html` is the source of truth. Do not regenerate or mirror from older files before reading and diffing it. For accidental Studio/VFX changes, remove only the identified artifact and restore root duration to the voiceover duration unless the user approved silent extra time.

Apply next time:

- read `section-previews/section-XX-*/index.html` before editing
- preserve `data-hf-studio-*` layout attributes unless they belong to the accidental artifact
- do not copy `hyperframes/review/section-XX.html` or visual-plan output over the preview
- check for unreferenced registry blocks under `compositions/`
- verify root `data-duration` matches the voiceover duration after cleanup
- record the preservation note in project docs

Promote to shared memory:
yes, as a workflow safety rule for all future render updates.

### 2026-06-08 - Approved Static Remake Quality Pattern

Classification: `Render lesson`

Context:
The user approved the remade Section 1 for `why-cheap-products-keep-getting-worse` after the failed low-quality render was removed and rebuilt from script, voice timing, real WIT poses, simple object boards, local handwritten font, and frame checks.

Lesson:
For future rejected or low-quality section renders, the best recovery pattern is a complete static remake: one voice cue per board, one main visual idea, hard cuts only, short handwritten labels, real channel WIT PNGs only on emotional beats, and preview screenshot verification before handoff.

Apply next time:

- delete only the failed section artifacts the user asks to remove
- skip the old visual plan when the user says it caused the bad result
- rebuild the board plan from `02-script.md` and selected section voiceover timing
- inspect `assets/wit/manifest.json` and use only those WIT PNG poses
- use WIT sparingly for suspicion, betrayal, panic, judgment, evidence, or payoff
- keep scene boards static until the user approves the visual direction
- use local font files for handwritten labels
- use Studio/direct preview screenshots or screenshot contact sheets for QA
- export MP4, run `ffprobe`, extract key frames, and inspect a contact sheet only when the user explicitly asks for video export
- record the override, checks, render path, and stale downstream notes in the production board file (`05-production-board.md`; legacy `06-production-board.md`)

Promote to shared memory:
no; keep in render memory unless the same pattern is approved across several sections.

### 2026-06-08 - Connected Big Scenes Prevent Rushed Hooks

Classification: `Render lesson`

Context:
After approving the real-WIT static Section 1 remake for `why-cheap-products-keep-getting-worse`, the user reviewed the pacing and pointed out that too many independent full-scene cuts made the short hook feel hurried. The reference style uses big scenes that hold for several seconds, while small elements appear, disappear, or change inside that scene on voice cues.

Lesson:
One voice cue per visual beat does not mean one unrelated full-frame board per beat. For short hooks, group related narration into connected big scenes, then use hard-cut cue overlays or small static changes inside the same scene. The visual continuity carries the viewer while still matching the spoken words.

Apply next time:

- identify the few big scenes first: setup object, problem/escalation, payoff or reframe
- keep the same base image/illustration while the voice describes parts of the same object or situation
- add or remove only one or two cue elements per spoken beat, such as labels, arrows, marks, small props, WIT reaction, or a hidden tag
- cut to a new big scene only when the narration moves to a different place, mechanism, or payoff
- verify a screenshot contact sheet for continuity, not just cue readability

Promote to shared memory:
no; keep in render memory until repeated across more approved sections.

### 2026-06-08 - Markup Must Mean Something And WIT Must Read

Classification: `Render lesson`

Context:
In the Section 1 remake for `why-cheap-products-keep-getting-worse`, the user rejected meaningless red leg marks, a screw circle that missed the screw, a washed-out white overlay over the failure image, too many cue clips for a `21s` hook, and WIT that was too small. The user also explicitly pointed back to the `hyperframes` skill as the expected render/composition workflow.

Lesson:
Red markup is not decoration. Every circle, arrow, underline, or box must point to the exact object it explains and must still be correct in direct preview screenshots. If a mark does not add meaning, remove it. WIT must be large enough for facial emotion to read at normal Studio/screenshot review size.

Apply next time:

- use the bundled `hyperframes` skill as the HTML composition source of truth before rendering
- reduce short hooks to the fewest cue states that still match the voiceover
- remove visual marks that only prove something obvious or do not explain the line
- check callout alignment against direct preview screenshots, not just the editor canvas
- avoid white wash overlays on real/object photos unless the user approves that treatment
- scale WIT large enough for the expression to be readable without covering the main object or label

Promote to shared memory:
no; keep in render memory until repeated across more approved sections.

### 2026-06-09 - Approved Section 1 Final Render Checklist

Classification: `Render lesson`

Context:
The user approved the final adjusted Section 1 render for `why-cheap-products-keep-getting-worse` after the section was simplified to `3` big scenes and `7` cue states, WIT was enlarged, meaningless red leg marks were removed, the failure-photo white wash overlay was removed, and the screw callout was verified against the actual preview frame.

Lesson:
High-quality short section renders should feel calm and connected: few big scenes, low cue count, meaningful labels, exact markup alignment, readable WIT emotion, and screenshot-frame QA. Studio playback alone is not enough because stale contact sheets and misaligned callouts can hide mistakes.

Apply next time:

- use the `hyperframes` skill as the source of truth for composition HTML before rendering
- for `20-25s` hooks, start with about `3` big scenes and `6-8` cue states
- remove decorative or meaningless red marks instead of trying to make them look better
- preserve real/object photo texture; avoid full-frame white wash overlays unless needed for readability
- scale WIT so the face and emotion are readable in Studio and direct preview screenshots
- align circles/arrows to the exact object in the direct preview frame
- delete old extracted `frame-*.png` files before creating a new contact sheet, when working from screenshots or explicit exports
- inspect problem frames individually, not only the full contact sheet

Promote to shared memory:
no; this is specific render execution memory for the `render` skill.

### 2026-06-10 - Direct Scene Assets Need Visual Differentiation

Classification: `Render lesson`

Context:
In `why-cheap-products-keep-getting-worse` Section 3, the initial render used a generated visible-promises photo as the direct base for Scene 3. The user correctly pointed out that it felt too similar to Scene 1 because it reused the same tabletop/product/tag visual language. The revised render inspected the references again, skipped that generated image as direct production, and rebuilt Scene 3 as a distinct CSS checkout promise arena.

Lesson:
Render must not blindly use every image from a visual plan. Before direct use, compare each scene base against adjacent big scenes and the section's final viewer memory. If a non-callback scene looks too similar to another scene, build or generate a distinct scene instead. Reference images can be inspected and intentionally skipped.

Apply next time:

- compare big-scene backgrounds, camera language, object setup, color mood, and material texture before locking scene bases
- reuse a scene base only when it is a purposeful callback or mechanism continuity
- if a planned image weakens visual variety, replace it with a distinct CSS/self-made/generated scene
- document skipped assets as `reference-only` in attribution and implementation notes
- verify the revised scene with fresh snapshots/contact sheets instead of stale thumbnail cache

Promote to shared memory:
no; keep in render memory until repeated across more renders.

### 2026-06-10 - Cue Animation Needs Explicit Hidden State

Classification: `Render lesson`

Context:
While adding a minimal animation pass to `why-cheap-products-keep-getting-worse` Section 1, delayed `gsap.from()` entrances with `immediateRender:false` allowed labels to appear in their final state between the cue clip start and the delayed tween start. This briefly put `LEGAL-ISH CREAK` over the old chair scene during the transition.

Lesson:
For cue-timed HyperFrames overlays, do not rely on delayed `from()` tweens to hide elements before they enter. At the cue's `data-start`, explicitly set animated elements to their hidden/offset state with `tl.set(...)`, then animate them to their final layout with `tl.to(...)` at the intended entrance moment.

Apply next time:

- keep the approved cue `data-start` as the timing anchor
- use a helper that sets `opacity: 0` and small `x` / `y` / `scale` offsets at cue start
- animate to `opacity: 1`, `x: 0`, `y: 0`, and `scale: 1` shortly after the cue start
- check transition boundary screenshots from direct preview, not just Studio playback
- if an old cue label appears over a new voice beat, shorten the old overlay or add a tiny visual breath before the next cue

Promote to shared memory:
no; keep in render memory unless the same sync issue appears across more sections.

### 2026-06-10 - MP4 Export Requires Explicit User Request

Classification: `Operational lesson`

Context:
During Section 1 animation work for `why-cheap-products-keep-getting-worse`, MP4 review renders were created while the user only asked for render/preview fixes. The user clarified that MP4 export wastes time and tokens and should happen only when they explicitly ask to export video.

Lesson:
Normal render work means HyperFrames HTML/Studio preview, checks, screenshots, and notes. Do not create MP4/WebM files for QA, timing fixes, animation passes, or review fixes unless the user explicitly asks for an export.

Apply next time:

- run `npm.cmd run check`, Studio/direct preview verification, and screenshot/frame checks instead of video export
- use browser or HyperFrames screenshots for frame-specific QA
- treat `export video`, `render MP4`, `render WebM`, `create video file`, or equivalent wording as the only trigger for video export
- if the user asks to "render" a section without saying export/video/MP4, build or update the preview only
- remove accidental MP4 outputs if created without explicit export permission

Promote to shared memory:
no; this is a render skill operating rule already captured in the skill source.

### 2026-06-11 - Phrase-Timed Reveals And Exaggerated WIT Placement

Classification: `Render lesson`

Context:
The user reviewed Section 1 of `why-cheap-products-keep-getting-worse` and said the transition/animation pass still made many blocks appear almost together. They wanted elements to appear when the voice reaches the matching words, such as `$9` appearing on `nine dollars` and `4 LEGS + 1 SEAT` appearing when that phrase is spoken. The user also said WIT should not default to the lower-left or lower-right corner; WIT is the emotional soul of each beat and should use exaggerated, funny placements.

Lesson:
Inside a cue, do not batch-reveal all labels, props, and WIT at cue start. Give each meaningful text block, tag, callout, and WIT entrance its own phrase-timed reveal. Treat WIT placement as part of the joke and emotion: large edge peeks, upside-down top peeks, half-body entrances from the side, hiding behind objects, behind-tag framing, and oversized faces are valid when they do not cover text or evidence.

Apply next time:

- map the spoken phrase before placing each reveal, especially price tags, evidence labels, and punchline text
- use cue-start hiding plus boundary cleanup sets when delayed elements leak into the next cue
- make WIT large enough to read emotion and vary placement across beats
- avoid using WIT only as a lower-corner sticker
- if an existing WIT pose cannot express the beat, generate or add a new approved pose into the shared/project WIT asset library and document it
- verify major WIT/layout changes with direct preview screenshots or contact sheets from runtime seek, not only `inspect`

Promote to shared memory:
partial yes; phrase-timed cue readability and WIT-as-emotion are summarized in `.agents/_shared/systems/visual-production.md`, while the detailed Section 1 timing case stays here.

### 2026-06-11 - Reduce Animation Density And Guard WIT Crops

Classification: `Render lesson`

Context:
After the phrase-timed Section 1 pass for `why-cheap-products-keep-getting-worse`, the user said the animation still felt dense and visually noisy. They wanted the same scene/cue structure but fewer text-block animations: only emphasized spoken beats such as `$9` should smash in, while ordinary sequential text should simply appear at the correct voice cue. They also said WIT poses were too small/not funny enough and called out broken WIT crops where the head, shoulder, or face was cut by the frame.

Lesson:
Sequential timing does not require every block to animate. For review fixes, prefer hard-showing ordinary labels exactly on the spoken beat, and reserve smash/pop/stamp motion for true emphasis beats. WIT must be treated as the emotional subject: use bigger, goofier approved poses when available, but verify direct preview frames so WIT does not look accidentally broken through cropped faces, heads, or shoulders.

Apply next time:

- preserve approved scene-transition count unless the user asks for a structural rebuild
- use `show at beat` for supporting labels and notes
- use impact motion only for highlighted spoken words, proof marks, or payoff labels
- scale WIT for readable emotion, often `1/3` to `1/2` of the frame
- prefer approved WIT library poses before generating new ones
- verify WIT-heavy changes with runtime seek screenshots/contact sheets, not just lint/inspect
- if a WIT crop looks accidental rather than intentionally peeking, reposition or scale it before handoff

Promote to shared memory:
yes; summarized in `.agents/_shared/systems/visual-production.md` because the rule affects future sections and projects.

### 2026-06-11 - WIT Density Must Follow Voice Rhythm

Classification: `Render lesson`

Context:
After the low-motion WIT-emphasis pass for Section 1 of `why-cheap-products-keep-getting-worse`, the user said the section still felt too dense because WIT appeared on too many cues across only `21.205s`. The fix reduced WIT from `7` appearances to `4`: big scene 1 kept `2` WIT beats, big scene 2 kept `1`, and big scene 3 kept `1`.

Lesson:
Making WIT large and expressive does not mean using WIT on every cue. WIT should act as emotional punctuation timed to voice rhythm. Text, props, marks, and the base scene should carry explanatory beats between WIT moments. For short sections with persistent big scenes, default to about `1-2` WIT appearances per big scene unless the narration clearly needs more.

Apply next time:

- count WIT appearances before handoff, especially in sections under `30s`
- decide WIT rhythm from the voiceover: setup reaction, escalation reaction, payoff reaction
- let explanatory cues breathe without WIT when labels/objects already explain the line
- keep WIT large when it appears, but reduce frequency if the section starts feeling crowded
- verify the reduced WIT rhythm with a contact sheet, not only a single hero frame

Promote to shared memory:
yes; summarized in `.agents/_shared/systems/visual-production.md` and skill rules because it affects future renders and visual plans.

### 2026-06-11 - Render Must Run Its Own Review-Prevention Pass

Classification: `Render lesson`

Context:
The user clarified that `render` should not blindly depend on `visual-plan`. Render also relies on HyperFrames skill mechanics and its own judgment. The Section 1 fixes required render-side decisions about hard-show timing, WIT density, WIT crop, asset use, markup alignment, and contact-sheet verification.

Lesson:
Render must run a review-prevention pass after reading the visual plan and before writing HTML. If the visual plan leaves gaps, render should make explicit decisions and document them instead of building a weak plan. HyperFrames core rules handle mechanics, but Why It Works channel rules control readability, voice sync, WIT rhythm, and motion density.

Apply next time:

- build static/end-state layouts before GSAP
- classify cue elements as `static`, `hard-show`, `impact`, or `transition`
- count WIT per big scene and reduce overuse before implementation
- use hard-show for ordinary delayed labels
- reserve impact motion for emphasized beats
- verify WIT/callout-heavy changes with runtime screenshots/contact sheets
- document render decisions that override or complete a weak visual plan

Promote to shared memory:
no; this is render-skill execution behavior, while the reusable production principles already live in shared visual-production rules.

### 2026-06-11 - Check Text Covering WIT, Not Only WIT Covering Text

Classification: `Render lesson`

Context:
After the manual Section 1 cleanup for `why-cheap-products-keep-getting-worse`, the user reviewed the final frame and noted that the payoff text covered WIT. The fix moved the `FUTURE NOT INCLUDED` tag and `SMALL PROBLEM` stamp left while shifting money-panic WIT right, preserving the payoff text without hiding WIT's face/expression.

Lesson:
Render must check visual collision in both directions. WIT should not cover labels, proof, or payoff, but payoff labels/cards/stamps also must not cover WIT's face, eyes, mouth, or key prop when WIT is carrying the emotion. Solve this by separating layout zones, not by relying on z-index or accepting partial face coverage.

Apply next time:

- inspect final/payoff frames specifically for text-over-WIT overlap
- create separate text and WIT emotion zones before adding motion
- keep WIT face/expression readable even when WIT sits behind a tag/card
- if a final tag must be large, shift or resize the tag before sacrificing WIT emotion
- sync the review mirror from the corrected preview after layout fixes

Promote to shared memory:
yes; summarized in shared visual-production and learning log.

### 2026-06-12 - Render Giant WIT When Emotion Carries The Beat

Classification: `Render lesson`

Context:
After Section 2 of `why-cheap-products-keep-getting-worse` was updated with larger WIT poses, the user still said WIT looked too small compared with Section 1. The accepted direction was to make WIT a giant emotional layer occupying roughly half the screen, sometimes rising from the bottom or peeking from an edge. Cropping lower body is acceptable; cropping face/head/shoulders is not.

Lesson:
Render must not settle for a small full-body corner WIT when WIT is carrying the main emotion. For strong reaction/payoff beats, test giant behind-layer or edge-peek compositions before handoff. The right crop style is intentionally oversized and funny: lower body can disappear off the bottom or side, but the face, glasses, head, shoulders, mouth, key prop, and expression must remain readable.

Apply next time:

- inspect the visual plan but still run render-side WIT placement judgment
- scale strong WIT beats toward `1/2` frame when labels/evidence can stay readable
- use behind-layer giant WIT, lower-edge half-body, side-peek, looming face, or object-hiding placements instead of default lower-corner full body
- treat face/head/shoulder crop as a blocking bug even if `inspect` passes
- verify all giant WIT changes with runtime-seek screenshots/contact sheets
- if no current pose reads well at giant scale, add or request a new approved WIT pose in shared/project assets

Promote to shared memory:
no; shared visual-production already contains the general WIT rule. Keep this concrete render execution pattern here and in `render/SKILL.md`.

### 2026-06-12 - Render Must Reserve Subtitle-Safe Lower Margin

Classification: `Render lesson`

Context:
While updating Section 2 of `why-cheap-products-keep-getting-worse`, the user said some elements were too close to the bottom edge and would likely be covered by YouTube subtitles after upload. The accepted fix moved `CHEAP IS NOT BAD`, `NICE JACKET`, and the final `AGAIN` receipt/loop cluster upward slightly without changing the approved scene structure.

Lesson:
Render should treat the lower subtitle zone as unsafe for cue-critical information. Important lower-third labels, receipts, stamps, arrows, boxes, and payoff props should be nudged upward by default unless they are intentionally background-only.

Apply next time:

- inspect lower-third elements for likely subtitle overlap before handoff
- move cue-critical bottom-edge elements slightly upward instead of leaving them flush with the frame edge
- preserve approved scene structure while adjusting only the risky lower-third placements
- if WIT rises from the bottom edge, move nearby text and props upward rather than stacking them into the subtitle zone
- document subtitle-safe adjustments in implementation notes when they materially affect layout

Promote to shared memory:
yes; this is a reusable YouTube layout rule for future sections and projects.

### 2026-06-12 - Remake Crowded List Sections With Sparse Backgrounds

Classification: `Render lesson`

Context:
In Section 4 of `why-cheap-products-keep-getting-worse`, the first render direction used too many text blocks, object cards, and scattered images. The user rejected it and asked for Section-1-style simplicity. The accepted recovery used three full-frame real/object backgrounds, six cue states, three giant WIT emotional beats, and only a few labels.

Lesson:
For explanatory-list sections, render should not build a separate visual object for every listed detail. Use a few persistent backgrounds and compressed labels, then let giant WIT carry emotion on selected beats. If the frame starts reading like a product-parts tray or slide full of cards, simplify structure before adding motion.

Apply next time:

- for `30-45s` list sections, start around `3` big scenes and `5-8` cue states
- use real/object backgrounds as the base and keep labels sparse
- group related details into memory labels such as material quality, repairability, spare parts, or missing future
- use generic CSS overlays for risky references like real phones, printers, UI, people, or brands
- use WIT on only the main emotional beats and make it large enough to dominate the reaction
- create a contact sheet from runtime seeks before handoff to confirm the section reads simply

Promote to shared memory:
no for now; keep as concrete render execution memory unless repeated across more sections.

### 2026-06-13 - Verify Giant WIT By Visible Footprint

Classification: `Render lesson`

Context:
The user asked to check `visual-plan` and `render` again and make sure the next render makes WIT occupy at least one third of the screen. They specifically like giant creative WIT poses: corner appearances, upside-down top entrances, hiding behind a wardrobe/object, and similar playful framing.

Lesson:
Render must verify WIT size by the visible character footprint in the preview frame, not the image element size. Transparent padding around WIT PNGs can make a large CSS box still read small. Emotional WIT beats should be rejected or resized if the visible character does not occupy at least `1/3` of the frame in the screenshot/contact sheet.

Apply next time:

- measure WIT by visible body/face/prop presence, not CSS width
- target at least `1/3` visible frame presence for every emotional WIT beat
- actively try creative placements before accepting a conventional corner WIT
- use corner peeks, upside-down top peeks, object/wardrobe hiding, lower-edge half-body entrances, behind-object looming, or oversized faces when they fit the joke
- create or inspect runtime screenshots/contact sheets for WIT-heavy frames before handoff
- treat under-1/3 emotional WIT as a layout bug unless the user explicitly requested a tiny/background WIT

Promote to shared memory:
no for now; keep as render execution memory unless repeated across more sections.

### 2026-06-13 - Failed Synthetic Sections Need Real Texture, Not Polish

Classification: `Render lesson`

Context:
Section 5 of `why-cheap-products-keep-getting-worse` was rejected because it had no real image, normal/boring WIT poses, and too many small synthetic objects competing in the frame. The recovery did not polish the CSS appliance mockup. It rebuilt the section from the script, voice timing, Section 1/8 visual grammar, two real image bases, and stronger WIT poses.

Lesson:
When the user rejects a section as synthetic or useless, treat the existing visual plan/render as stale. Rebuild around one real/object texture per big scene, fewer cue labels, and WIT poses that are emotionally specific to the joke.

Apply next time:

- do not keep iterating on a CSS-only mockup after the user complains that it lacks real image texture
- reuse approved reference sections to copy the successful frame grammar
- choose real/generated bases first, then add only sparse handwritten cue labels
- replace neutral WIT poses with expressive approved poses tied to the spoken joke
- keep listed details compressed into one or two readable labels instead of many separate props
- make a contact sheet before handoff and check whether the frame still reads like a pile of boring things

Promote to shared memory:
no for now; keep as render execution memory unless this failure pattern repeats again.

### 2026-06-14 - Too Many Graphic Elements Means Switch To Image Bases

Classification: `Render lesson`

Context:
Section 6 of `why-cheap-products-keep-getting-worse` was rejected because it used too many self-made graphic/CSS elements instead of illustrative images. The user specifically pointed to Sections `3`, `1`, and `8` as references for how the visual render should demonstrate the idea.

Lesson:
When the user says a render uses too many graphic elements, do not keep refining the drawn-object scene. Rebuild the section around dominant illustrative photo/object bases, then add only sparse handwritten cue labels and large WIT beats.

Apply next time:

- compare the rejected section against approved nearby sections before editing
- replace drawn product props with one strong image or texture base per big scene
- keep listed details compressed into sticky labels, stamps, or a compact checklist
- preserve the voice timing but let the image base carry most of the explanation
- re-run direct-preview contact sheets after WIT scale changes

Promote to shared memory:
no; this confirms the existing Section 4/5 render recovery pattern, but the detailed action belongs in render execution memory.

### 2026-06-18 - Restore A Lost Section Preview From The Surviving Review Mirror

Classification: `Operational lesson`

Context:
For `why-cheap-products-keep-getting-worse` Section 6, the `section-previews/section-06-.../` working folder and `06-production-board.md` were missing, but the approved build survived at `hyperframes/review/section-06.html` with its photo bases, and the saved references survived. The user asked to render Section 6.

Lesson:
When a section preview working folder is lost but the review mirror (`hyperframes/review/section-XX.html`) survives and represents the approved build, restore the preview 1:1 from the mirror instead of re-rendering from scratch. Copy the mirror HTML to `section-previews/section-XX-*/index.html`, rebuild a minimal `assets/` working set by copying only the files that section uses (from the mirror's `assets/`), copy the section voiceover mp3 as a sibling so the HTML's relative `src` resolves, and add `package.json` + `hyperframes.json` matching the sibling sections. Then run `lint` / `validate` / `inspect` and start the port `1000 + N` server.

Apply next time:
- glob `section-previews/`, `hyperframes/review/`, and the project root before assuming a section is unrendered
- restore from the review mirror to avoid drift from the approved build
- copy assets from the mirror's `assets/` (junctions fail on this Windows setup); keep the working set minimal
- expect the preview server to resolve project id/title as the workspace/git root name (`Build a Channel`) while `dir` points to the section folder; verify via `GET /api/projects/Build%20a%20Channel/preview/comp/index.html`
- recreate `06-production-board.md` if it is also missing
- hand any WIT face/glass/tag collision QA points to Review rather than redesigning during a restore

Promote to shared memory:
no; this is render-skill execution behavior for recovering lost preview folders.

### 2026-06-21 - Word-Timings JSON Is The Source Of Truth; Cascade + Stagger (Section 6 review synthesis)

Classification: `Render lesson`

Context:
Section 6 of `why-cheap-products-keep-getting-worse` went through four review passes that were almost all preventable at render time. The biggest was timing: the ownership-lock cue was placed at `16.8s` but the voice says it at `12.64s`, which pushed every downstream cue late. The section voiceover folder had `section-06-word-timings.json` (faster-whisper word timings) the whole time; the render had been timed from estimates/prior values instead. Reviewers also asked for within-cue text and list items to appear as each is spoken, not all at once.

Lesson:
Render must build the voice cue map from `voiceover/section-XX-*/section-XX-word-timings.json` and pin every `data-start`, scene cut, and GSAP reveal to actual word starts. When one cue moves, cascade the whole downstream chain. Within a cue, stagger every label/quote/list item to its spoken word (GSAP opacity sets), never batch them at cue start. Re-point `package.json` `inspect --at` + snapshot `--at` to the new cue mid-points and regenerate.

Apply next time:
- read the section word-timings JSON first; if absent, generate it before timing, else label all cue times `estimated`
- pin each cue + reveal to its word; "show each item when the voice says it" is the default for any on-screen list
- cascade downstream cues/scenes/reveals on every timing change
- mechanics that block validation: accumulating same-track clips must move to separate tracks with `clip` class + ids; trim float-overlap boundaries (`5.3+4.56` overlaps `9.86`); intentional off-canvas WIT needs `data-layout-allow-overflow` + `overflow:visible` on the cue div, not just the img
- verify with `hyperframes snapshot --at` at one timestamp per cue/reveal

Promote to shared memory:
no; render execution behavior. The word-timings-first rule now lives in `render/SKILL.md` (Voice-Sync Timing Contract).

### 2026-06-21 - Every Scene Needs A Real Photo Base, Not A Gradient (Section 6 review synthesis)

Classification: `Render lesson`

Context:
Section 6's CSS-only beats (cost gradient, ownership-lock gradient, future grid + empty `fake-phone`, and a sterile screwdrivers-on-white scene) were each rejected across passes as "no background / doesn't have an image to describe the voice / looks bad". Each was fixed by sourcing a real CC photo from Wikimedia (padlock, euro money, phone-on-table, opened-phone repair bench) and grading it clean. Brand/people pitfalls appeared: a CC0 desk photo had a recognizable MacBook (swapped), a Motorola battery showed a brand (rejected), and high-res repair photos contained real people (rejected per no-face rule).

Lesson:
If a scene base is a flat gradient or empty color, render should treat it as a defect and source a real descriptive photo (Wikimedia Commons API; brand-free, people-free, non-sterile, distinct, palette-clean) rather than ship the gradient. This should normally be fixed in `visual-plan`, but render must not build a gradient-only beat just because the plan left one.

Apply next time:
- replace any gradient/empty scene base with a real descriptive image that matches the voice beat
- verify brand-free/people-free on the actual pixels; keep photos clean (no gray wash); record creator/license in `ATTRIBUTION.md`
- `object-fit: cover` from a frame-width source only crops vertically - pick a different image if a side-edge element must go

Promote to shared memory:
no; the upstream prevention lives in `visual-plan/SKILL.md` (Real Scene Base Rule + sourcing recipe). Keep render-side enforcement here.

### 2026-06-21 - Generate Word Timings With transformers.js (Don't Estimate)

Classification: `Render lesson`

Context:
Sections 4 and 7 of `why-cheap-products-keep-getting-worse` were first built with estimated cue timing because no `word-timings.json` existed and `hyperframes transcribe` needs whisper-cpp (not installed; no Python/faster-whisper either). The estimates drifted badly - for Section 4 the voice rattled the parts list out ~4s earlier than estimated (e.g. "a hinge" spoken at 5.66s but shown at 9.5s), so Anh Khoa reported "the text doesn't match the voice again." Generating real word timings and re-pinning every cut/reveal fixed it.

Lesson:
Estimating cue timing is unreliable and keeps producing "text doesn't match the voice" review hits. When a section lacks `word-timings.json`, generate it. Whisper via `transformers.js` (`@xenova/transformers@2.17.2`, `Xenova/whisper-tiny.en`) runs in WASM with NO native deps - it works on this Windows box where whisper-cpp/Python do not.

Apply next time:
- `npm.cmd install --prefix %TEMP%/wiw-whisper --no-save @xenova/transformers@2.17.2`
- decode mp3 → 16 kHz mono f32 with the static ffmpeg (`-ar 16000 -ac 1 -f f32le`), read into a `Float32Array`
- `pipeline('automatic-speech-recognition','Xenova/whisper-tiny.en')` with `{return_timestamps:'word', chunk_length_s:30, stride_length_s:5}`; `result.chunks` = `[{text, timestamp:[start,end]}]`
- save `voiceover/section-XX-*/section-XX-word-timings.json` ({transcript, words[]}) and pin every `data-start`, scene cut, and GSAP reveal to it; re-derive any unified/combined-audio offsets from the actual durations
- only fall back to proportional estimation if generation genuinely fails, and label cues `estimated`

Promote to shared memory:
No; render execution practice. The concrete recipe now lives in `render/SKILL.md` (Voice-Sync Timing Contract).

### 2026-06-21 - Word-Timings Gen Worked For Busy S1; Retry Corrupt Model Download

Classification: `Operational lesson`

Context:
First render for `why-everyone-pretends-to-be-busy` Section 1. Generated
`section-01-word-timings.json` with the documented transformers.js recipe (whisper-tiny.en, WASM).
The first two runs threw `Error: Unsupported model type: whisper` - caused by an earlier
`ECONNRESET` that left a partial/corrupt model in the transformers.js cache. A third run (after
the model finished downloading/caching) succeeded and produced clean monotonic word timings.
The final two words ("a", "difference.") had a chunk-boundary timestamp glitch (jumped back to
~11.5s) and were hand-corrected to 20.46 / 20.58–21.0.

Lesson:
The transformers.js word-timing recipe is reliable on this box, but a flaky first download can
poison the cache and surface as "Unsupported model type" rather than a network error. Just retry
the node run until the model fully caches. Always sanity-check the last 1-2 words for a
chunk-boundary timestamp reset and clamp them to the section duration.

Apply next time:
- if `Unsupported model type` appears, retry the same node command (model finishes caching), don't change code
- after generating, eyeball the JSON tail for non-monotonic/garbage timestamps and clamp to the audio duration
- ESM ignores NODE_PATH - run the gen script from inside the `--prefix` dir where node_modules resolves

Promote to shared memory:
no; environment/tooling note for the render word-timings step.

### 2026-06-21 - Dingy Real Photos Rejected → Clean Flat-Illustrated Bases (no generator)

Classification: `Render lesson`

Context:
`why-everyone-pretends-to-be-busy` Section 1 first rendered with real PD photo bases (a dated 2007
wall calendar + an overhead minimalist desk). The user rejected them: "the images look really
filthy and bad... use better image, you can generate new images if needed." No image-generation
tool was available this session, and clean brand-free/people-free real photos of busy-calendar /
quiet-desk were not findable on Commons.

Lesson:
When real photo bases are rejected as ugly/dingy and no generator is available, do not keep
swapping in more stock photos. Rebuild the scene bases as clean, bold **flat-illustrated CSS
scenes** that match the channel's actual identity (bold flat 2D illustration, not photoreal). A
fully-drawn illustration (e.g. a calendar wall with header/weekday row/numbered cells packed with
colored event chips; a desk room with notebook/pen/mug/plant) is a justified self-made descriptive
base - it is NOT the "bare gradient" the hard-fail rule forbids. This is usually cleaner AND more
on-brand than dingy stock. Keep cue timing/WIT unchanged; only swap the base layer.

Apply next time:
- confirm no image generator, then build flat-illustrated bases instead of re-searching stock
- a packed calendar reads "overbooked" via many small colored event chips in the cells
- reuse the same illustrated base for an intentional bookend (Scene A bright, Scene C cool+cage bars)
- keep the photo refs on disk as `inspiration only`; document the base swap in IMPLEMENTATION.md + visual plan
- expect many non-blocking contrast warnings from a grid of small cells; 0 errors is the gate

Promote to shared memory:
no; render execution behavior. (If image generation becomes available, prefer generated clean bases.)

### 2026-06-22 - STANDING PREFERENCE: Build Real-UI Mockups (owner confirmed)

Classification: `Core` (confirmed channel creative direction)

Context:
Section 4 was rebuilt with real app icons + an iPhone notification screen, an app-icon overload grid
with red badges, and a Messenger-style chat - all built in CSS with real icon PNGs. The owner
confirmed: "I love to use real illustrative like phone, app icons to describe the script like this."

Lesson (render side):
When a section depicts real apps/products/screens, build clean **real-UI mockups in CSS** with real
icon PNGs (Wikimedia Commons): iPhone/phone frames, notification cards, home-screen/app grids with
red badges, chat conversations. Key mechanics learned:
- Put accumulating UI (notification cards, badges, chat bubbles) INSIDE the scene `<div>` so it
  persists and clips to the phone/tiles; cue-clip elements vanish when the cue ends (broke continuity).
- Position notification cards relative to the phone frame (not the 1920 frame) or they render full-width.
- Put app-icon badges INSIDE each `.apptile` (corner), not at fixed composition coords (they misalign/stretch).
- The 👍 emoji glyph does NOT render in the snapshot Chromium - use a thumbs-up PNG via `<img>`.
- Real logos are used editorially (depict, not endorse); no private data / pixel-copied screenshots.

Promote to shared memory: covered in `_shared/channel/brand-system.md` ("Real-UI Illustration"); keep the render build mechanics here.

### 2026-06-22 - Section 5: more CSS real-UI surfaces + preview project-id varies

Classification: `Render lesson` / `Operational lesson`

Context: Section 5 ("Visible Work Beats Quiet Thinking") built four CSS real-UI surfaces - a Google
Meet call grid, a survey poll card, a Trello Kanban board, and a Google Sheets spreadsheet on a
theater stage - plus one CC wall photo. Lint/validate/snapshot all clean.

Lesson:
- Real-UI scope keeps widening per owner preference: Meet grids, Kanban boards, poll/survey cards,
  and spreadsheets all read clearly as CSS mockups with real icon PNGs. Use initials avatars (not
  faces) in any "call/people" UI to keep the no-face rule.
- Two reliable custom GSAP tweens beyond reveal/show/smash: (1) animate a `.pollbar i` width from
  0%→target for a survey-bar "fill"; (2) translate a Kanban `.movecard` via `x` from one column
  offset to 0 to show "move a task column→column" on the spoken beat.
- Float overlap on track 2: `25.76 + 3.14 = 28.900000000000002` tripped `overlapping_clips_same_track`
  against a 28.9 start. Trim the earlier cue's duration (3.14→3.12) rather than nudging the start.
- Preview project-id is NOT always `Build a Channel`: Section 5's server resolved the project id to
  the section FOLDER name. Always read `/api/projects` from the running server and build the Studio /
  comp URLs from the reported id; don't assume the workspace-root title.

Apply next time: check `/api/projects` for the real id before recording preview URLs; expect to build
calls/boards/sheets/polls as CSS real-UI; watch track-2 float sums for overlap.

Promote to shared memory: no - render/operational mechanics; real-UI policy already in `brand-system.md`.

### 2026-06-22 - Pure CSS-UI scenes feel flat; ground them on real desk photos

Classification: `Render lesson`

Context: Section 5 v1 was 4 CSS real-UI scenes (Meet/poll/Trello/Sheets) + 1 real photo. Owner: "it
look like it's missing some real-world images that make the section not lively." The crisp UI was
liked, but full-frame flat-gradient backgrounds read as synthetic slides.

Lesson:
- Real UI is loved, but a whole section of full-frame CSS UI on flat gradients feels like slides.
  Ground each digital scene in a REAL, people-free photo so the app reads as a real screen in a real
  space - much livelier without losing the recognizable UI.
- Pattern: `.deskphoto` (real photo, object-fit cover, slight darken filter) + radial `.deskscrim` +
  a floating `.screen` window (≈1500x846, rounded, big drop shadow) that holds the UI. The real desk
  shows around the window = environment/texture.
- Rescale UI internals to the window (not the 1920 frame); recompute any absolute-coord animation
  offsets (e.g. the Trello card's DOING→DONE x-translate changed when columns shrank).
- Pick DISTINCT surfaces to avoid the repeat complaint: white desk / marble / dark wood. Bonus when a
  prop matches the beat (a real "To Do List" notepad under a Kanban board).
- Sourcing people-free modern desks: most "office desk" hero photos include a person (no-face fail);
  CC0 StockSnap top-down desk FLAT-LAYS (coffee/notebook/laptop, ~960w) are reliably people-free and
  fine as darkened backdrops. Keep a clearly stylized scene (CSS theater) as a deliberate contrast.

Apply next time: don't ship an all-CSS-UI section on flat gradients - float the UI on real
people-free desk/space photos for liveliness; vary the surface; verify no faces.

Promote to shared memory: candidate - consider a short "ground real-UI on real photos" note in
`_shared/channel/brand-system.md` if this recurs across sections.

### 2026-06-22 - Whisper tail glitch: last sentence jumps BACKWARD (re-time monotonically)

Classification: `Operational lesson`

Context:
Section 7's generated `section-07-word-timings.json` had a clean body but the FINAL sentence
("…you are not lazy. You are just trapped in a calendar with Wi-Fi") had word timestamps that jumped
BACKWARD to ~40s after a correct run to 43.56s - a whisper-tiny chunk-boundary artifact (the 30s
chunk + 5s stride re-decoded the tail). Earlier sections showed the related tail-DUPLICATION variant.

Lesson:
After generating word timings, always inspect the LAST ~15 words for monotonicity, not just for
duplication. If a trailing run of words jumps backward (out of order vs the transcript), re-time that
run monotonically from the last good timestamp to the audio duration, keeping each word's spoken
order. Pin the final payoff label to the corrected time (here "A CALENDAR WITH WI-FI" @45.40).

Apply next time:
- print the tail with indices and verify start times strictly increase
- fix backward-jump runs by hand (even spacing from last-good → audio end) before pinning cues
- this is in addition to the known tail-duplication slice fix

Promote to shared memory: no; word-timing QA mechanic for render/voiceover.

### 2026-06-22 - WIT bottom-peek anchored too low reads as "covered by the frame"

Classification: `Render lesson`

Context:
Section 7 used the established bottom-edge WIT peek at `bottom:-560/-600px` (width ~860–1000). Owner:
"The WIT in all scenes is too low and it's covered by the frame, move the WIT to higher position."
Only the head was peeking; most of the body bled below the canvas, reading as cut/hidden.

Lesson:
For the bottom-edge WIT placement, `bottom:-540…-600px` pushes too much of the figure off-canvas -
head+shoulders only, looks broken. Anchor higher: `bottom ≈ -250…-320px` (trim width to ~640–880)
so head + glasses + torso + arms sit inside the frame and only the legs crop. Keep WIT horizontally
off to a side/corner so it clears labels; verify in a snapshot. This is the safer default going forward.

Apply next time:
- default bottom-peek WIT to ~`-260px`, not ~`-560px`; show head→hips, crop legs only
- re-check face/head/shoulders are well inside frame and not covering labels/evidence
- the prior low anchor (S4–S6) may get the same complaint - raise on request

Promote to shared memory: no; render WIT-placement mechanic (pairs with the WIT safe-crop rule).

### 2026-06-22 - WIT default: BIG and HIGH; re-arrange content around it (Section 7)

Classification: `Render lesson`

Context:
Right after the "WIT too low" fix, the owner said: "Make the WIT bigger, if the bigger wit cover
content behind, you can re-arrange positions of other items." So the raised-but-medium WIT (width
~640–880) was still not what they wanted - they want it BIG too.

Lesson:
The two WIT defaults combine into one rule: WIT is BIG (≈`1/3`–`1/2` frame) AND HIGH (head+torso inside
the frame, `bottom≈-260…-340`, legs cropped). When a big WIT collides with a label/board/chat/UI, MOVE
the other items, don't shrink/lower WIT. Section 7 moves that worked: A → board to top-left; B → WIT
centered-bottom with NOT LAZY/SAFER on top and the two label columns at the far sides; C → ≠ rows on
the left, WIT big on the right; D → WIT to the LEFT (chat bubbles are right-aligned), stamp to the
right; E → calendar shrunk + shifted right, labels to the right, big trapped WIT center-left.
Check both the early AND late cue frames (a label that appears later, e.g. "SAFER"/"Busy.", must also
clear the now-bigger WIT).

Apply next time:
- start WIT big + high; rearrange the supporting items to clear it (opposite side / top / bottom)
- centered-bottom WIT works when labels can live at top + far sides; side WIT works when content is on the opposite side
- snapshot a mid/late timestamp too, not just the WIT's entrance, to catch later labels colliding
- now codified in `render/SKILL.md`, `visual-plan/SKILL.md`, and `_shared/systems/visual-production.md`

Promote to shared memory: yes - done (WIT size+anchor rule added to `_shared/systems/visual-production.md`).

### 2026-06-23 - GSAP smash drops percentage translateX; center animated els via explicit left

Classification: `Render lesson`

Context:
First render for `why-everything-is-a-subscription-now` Section 1 (subscription hook). Built clean on
the established busy-S1 pattern (real photo bases + CSS bank-app/subscription cards = real-UI; 3 scenes,
7 cues, 4 WIT beats; word-timings via transformers.js). Two build-time gotchas fixed before handoff.

Lesson:
- A `smash`/`reveal` helper that animates `scale`/`x`/`y` OVERWRITES an element's CSS `transform`, so a
  percentage `transform: translateX(-50%)` used for centering is LOST mid-tween (the element jumps to its
  `left` with no offset). For any element you smash/scale, position it with an explicit `left` (no
  percentage translate). Rotation in the inline/CSS transform is preserved by GSAP; only the percentage
  translate breaks. (`show`-only opacity elements are safe to keep `translateX(-50%)`.)
- Collision check the LATE frame of a multi-WIT scene: a deadpan WIT swapped in on the right covered the
  punchline pop-up + item labels. Fix = put the swapped WIT on the same clear side as the earlier pose
  (left) and keep labels/pop-up on the opposite side; verify with a snapshot just AFTER the smash
  completes (e.g. 18.3s for a 17.9s stamp), since at the exact smash start opacity is still 0.
- Duplicate-media lint warning: reusing one photo file in two scenes trips `duplicate_media_discovery_risk`
  - give the second scene its own copy (`*-dim.jpg`) to keep lint 0/0.

Apply next time:
- never put `translateX(±%)` on an element you also smash/scale; use explicit `left`
- snapshot multi-WIT/stamp scenes a beat AFTER the impact, not on its `data-start`
- copy a reused base to a second filename per scene

Promote to shared memory:
no; render execution mechanics.

### 2026-06-23 - STANDING TEMPLATE: vivid object bases + varied CSS idea-devices + giant VARIED WIT

Classification: `Core` (confirmed channel creative direction)

Context:
`why-everything-is-a-subscription-now` Section 1 was rebuilt twice on owner review and then approved as
the template for all following sections ("I want next section will be similar to section 1, update the
skill"). Rejections that shaped it: mundane stock photos; mild/boring WIT poses; repeated identical cream
rectangle label boxes; WIT too small; and WIT always on the right with text always on the left.

Build standard to apply to every section going forward:
- BASES: vivid, on-topic, brand/people-free OBJECT photos that dramatize the line (coins/cash for money,
  padlocks for locked/rent, a glowing screen, etc.) - not calm desks/hands. If clean topical photos are
  scarce, use a strong concrete object + CSS real-UI. Grade per scene; keep scenes distinct.
- IDEA DEVICES (vary per beat; NOT a repeated cream box): app-grid of colorful subscription tiles; a big
  kinetic NUMBER/counter; notification TOAST cards (icon + red "−$X.XX"); a free-trial COUNTDOWN that flips
  to "$/mo"; a full-width top EXPIRED system BANNER; a PADLOCK wall; bold kinetic headline type; badges.
  Reserve the handwritten cream label for the occasional aside only.
- WIT: GIANT (≈1/2 frame), the soul of each scene, with an EXPRESSIVE on-topic pose per beat
  (price-tag-suspicion, hidden-fee-panic, holding-phone-panic, trapped-by-app-screen, betrayed, empty-wallet…).
  VARY WIT across scenes: side (left / center / right), scale, vertical anchor, and pose - never all-right.
  Flip the text/UI to the side WIT is not using; rearrange items around WIT rather than shrinking it.
  NOTE: current WIT poses ship on a flat green #00B140 screen - chroma-key the green out at render before compositing.

Build mechanics that mattered (reuse these):
- A full-screen "system" message reads best as a TOP BANNER (z above WIT), and HIDE the underlying
  toast/UI column when it takes over (otherwise the banner sits over the boxes = "text covering boxes").
- Any element you scale/smash must be positioned with explicit left/top - GSAP scale drops percentage
  `translateX(-50%)` centering. `show()` (opacity-only) elements may keep `translateX(-50%)`.
- No emoji glyphs in snapshot Chromium (⚠ etc. fail) - draw a CSS shape (e.g. a red "!" circle) instead.
- Reuse one photo file across scenes only via separate filename copies (`-own/-rent/-lock`) to dodge the
  `duplicate_media_discovery_risk` lint warning.
- Snapshot a beat just AFTER an impact (e.g. 18.3s for a 17.9s stamp), not on its `data-start` (opacity 0 there).
- A reusable CSS kit now exists in `section-previews/section-01-hook/index.html` (tiles .g1-.g8, .toast,
  .countdown, .modal banner, .lock padlock, .bignum counter, .payoff) - copy/adapt it for new sections.

Apply next time: build new sections from the Section-1 CSS kit; vary WIT side/scale/pose per scene; vary
the idea-device per beat; lint/validate 0 errors; snapshot every beat and check WIT-size + collisions.

Promote to shared memory: yes - Core direction; add a short note to `_shared/systems/visual-production.md`.

### 2026-06-23 - Remake S2 to the S1 template; the smash helper ignores scaleX

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 2 was remade completely "based on Section 1." The prior
S2 build broke the standing template exactly like S1 v1 (one phone base graded 4×; repeated cream label
boxes carrying every idea; small WIT). Rebuilt to `vivid object bases per scene → varied CSS idea-devices
→ giant WIT that varies side/scale/pose`: phone (defuse) / vinyl crate (own) / phone+paywall (rent) /
padlock (lock) / device flat-lay (question); struck RANT banner, OWN/RENT stamps, receipt, paywall,
lock-screen card, RENT tags, payoff; WIT facepalm R → thinking L → betrayed CENTER giant → suspicious R.

Lesson:
- When a section is "remade based on Section 1," treat the prior build as stale and rebuild to the
  template: a DISTINCT vivid object photo base per scene (a phone reused on a non-consecutive scene is OK
  when the script intends "the same device shown two ways" - re-dress it heavily, separate filename to
  dodge `duplicate_media_discovery_risk`), 2-3 varied idea-devices per beat instead of cream boxes, and a
  giant WIT whose side/scale/pose changes each scene. Cream `.aside` is for ≤2 short handwritten asides.
- GOTCHA: the shared `reveal`/`smash` helper only maps `x/y/scale/opacity` to its end state. Feeding it
  `{scaleX:0}` animates nothing (it stays 0 → invisible). For a draw-on line (e.g. a strike crossing a
  banner), use an explicit `tl.set({scaleX:0}); tl.to({scaleX:1})` with `transform-origin:left center`,
  not `smash`. A silent invisible element can invert a message (an un-struck "ANTI-SUBSCRIPTION RANT"
  banner reads as the opposite of the intent) - always snapshot-verify impact/draw beats.

Apply next time:
- rebuild remade sections to the template; one distinct vivid base per scene; vary the idea-device + WIT per scene
- never pass `scaleX`/`scaleY`/`rotation` to the x/y/scale/opacity helper - write an explicit tween
- snapshot every impact beat; confirm draw-on/strike elements actually rendered

Promote to shared memory:
no; the template is already Core in `_shared/systems/visual-production.md`. This is render execution mechanics.

### 2026-06-23 - WIT at width ~900-1000 still "too small"; default to ~1300; bg must read as the topic

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 2 review (round 2). Even after WIT was built "big" at
width 900–1000 (bottom:-300), the owner said "WIT too small, make it bigger or giant." Also flagged the
BS1 base (a glowing phone against an aurora/night SKY) as "not suitable" - it read as a travel/landscape
photo, not subscriptions - and two text-on-text overlaps (a red RENT stamp sitting on a struck OWN; a
payoff colliding with on-screen tags). Fixes: WIT widths → 1200–1300 (≈1/2+ frame) at bottom:-320;
swapped BS1 to a phone-full-of-app-icons photo; un-stacked OWN/RENT vertically; hid the tag set when the
payoff lands.

Lesson:
- WIT "big" means width ≈1200–1400 on a 1920 frame (≈1/2+ visible), not 900–1000. Start there by default;
  these full-body PNGs have transparent padding so a 900px box still reads as a small character. Anchor
  bottom:-300…-340 so head+torso are in frame and only legs crop.
- A scene base must read as the TOPIC, not just "a nice photo." A phone against a pretty sky reads as
  travel; a phone full of app icons reads as "subscriptions." Pick the base by what the line is about.
- Two text-on-text traps to pre-empt: (1) a stamp swap (OWN→RENT) must place the two stamps in separate
  spots (stack vertically), not overlap; (2) when a payoff lands over a field of tags/labels, HIDE the
  tags at the payoff beat (the S1 "hide the column when the banner takes over" pattern) so the payoff is clean.

Apply next time: default WIT width ~1300; choose bases by topic-read; never overlap two text blocks - stack or hide.

Promote to shared memory:
no; the WIT big+high rule is already Core in `_shared/systems/visual-production.md`. This sharpens the
default size and the bg-reads-as-topic + no-overlap checks for render execution.

### 2026-06-23 - S3 built to template; typing-on-laptop ALSO has baked black bg; ~10s/scene for 54s

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 3 ("The Spread", 54.165s) built fresh to the standing
template: 5 distinct vivid object bases (laptop desk → living-room TV → euro cash → jail corridor →
car interior), varied CSS idea-devices per beat (software window+padlock+ransom; streaming-tile wall
that VANISHES + POV card; 5 subscription tiles; "5 subs > CABLE" + dungeon labels; heated-seat button +
padlock + EXPIRED running-gag banner), and 4 giant WIT beats varied by side/pose (hidden-fee-panic CR →
shocked L → trapped-by-app-screen C → deadpan-side-eye R), with the cash scene breathing (no WIT).

Lesson / reusables:
- (HISTORICAL - old `wit-pose-*` set, removed 2026-06-28.) That set had baked black backgrounds on some
  poses, so the habit was: always VIEW a pose before first use. The current WIT poses ship on a flat green
  #00B140 screen (rgb24) and are chroma-keyed at render; only `_origin_.png` is transparent. Keep the
  VIEW-before-use habit. Former known-transparent set (legacy note): facepalm, thinking, betrayed,
  suspicious, shocked, trapped-by-app-screen, deadpan-side-eye, hidden-fee-panic, holding-phone-panic,
  price-tag-suspicion.
- For a ~54s section, ~5 scenes at ~10s each reads well; when one idea-cluster would hold one base >15s
  (here the "five subs / cable / dungeon" stretch), SPLIT it onto a second on-topic base (a jail corridor
  for "five smaller dungeons") rather than riding one base - matches the owner's "fresh base every ~6-10s."
- Brand-cover technique: when the only good modern base carries a small logo (a "Blaupunkt" car head unit),
  keep it but COVER the logo in the final frame with a CSS panel + the giant side WIT; classify it a mockup target.
- Generate word timings when missing (whisper-tiny.en) - Section 3 had none; pinned every cue to real word starts.

Promote to shared memory:
no; template is already Core. The typing-on-laptop black-bg fact is a concrete asset gotcha for render/visual-plan.

### 2026-06-23 - S4 built; CSS coins as an idea-device; reused-base 2nd-filename; whisper backward-jump

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 4 ("Why Companies Love It", 51.093s) built to the template:
6 vivid object bases (cash → espresso machine → same machine as a "money machine" → cash → calendar →
mousetrap), varied idea-devices, 4 giant WIT beats (sleeping-burned-out R → empty-wallet L → confused L →
suspicious R; two scenes breathe).

Reusable lessons:
- CSS GOLD COINS are a strong new idea-device for money/recurring beats: a single coin (one sale), a
  staggered rising GEYSER (recurring revenue), a vertical STACK (worth a lot), and a few RAIN coins ("keeps
  coming like rain"). `.coin` = a radial-gradient circle + `$`. Pop each on its spoken word.
- A real object can carry a before/after on ONE base: the espresso machine = "you sell it once" (BS2) then
  the same machine warm-graded + coin geyser = "now they pay monthly" (BS3). When you reuse a base file in two
  scenes you MUST give the 2nd scene its own filename copy (`base-coffee-machine.jpg`, `base-cash-lot.jpg`) or
  `duplicate_media_discovery_risk` fires. (Both before/after-adjacent and non-consecutive reuse need this.)
- A centered kinetic word (`RECURRING`) and a centered WIT collide - put the WIT on one half and ALL the
  text/marks on the other half (here WIT left, word+calendar-rings+label right). Cleaner than nudging z-index.
- Verified-transparent poses (safe on photos): sleeping-burned-out, empty-wallet, confused (+ the earlier list).
  Still AVOID `typing-on-laptop` and `money-panic` (baked black bg) - both now flagged in the SKILL files.
- Whisper word-timings can jump BACKWARD mid-line at a chunk boundary (S4's "worth a little / pays every
  month" re-emitted ~24–26s). Don't trust the glitched run - pin cues to the CLEAN word starts around it.

Promote to shared memory:
no; template is Core. These are concrete render idea-device + asset + timing mechanics.

### 2026-06-23 - Red rings over a photo circle nothing - use a meaningful device instead

Classification: `Render lesson`

Context:
S4 (`why-everything-is-a-subscription-now`) BS5 used 4 red CSS rings on the calendar photo to suggest
"recurring charges." Reviewer: "the circles don't circle anything - I don't know what they're on." The
rings sat over blurry "Novembre" grid text, aligned to no actual date.

Lesson:
A red ring/circle/arrow on a PHOTO base only works if it lands exactly on a real, legible target in that
photo (a specific date number, a button, an object). Over a soft/typographic/blurred photo it reads as
decoration pointing at nothing - the classic meaningless-markup failure. When you can't guarantee a precise
target, drop the markup and SHOW the idea with a built device instead. Here the fix was an `AUTO-PAY · the
same charge, every month` statement card with identical `−$9.99` rows (Jan/Feb/Mar/Apr) popping one-per-beat
- it demonstrates "recurring" far more clearly than circles ever could, and it's real-UI (owner-preferred).

Apply next time:
- only place a circle/arrow when it aligns to a specific readable target verified in the snapshot
- otherwise use a label, stamp, or a real-UI card/list that depicts the concept
- "recurring/repeating" reads best as the SAME item repeating in a small statement/list, not as circles

Promote to shared memory:
no; reinforces the existing "markup must target a real object" rule with a concrete photo-base case.

### 2026-06-23 - S5 built; blank-phone CSS canvas; meaningful ring on a CSS row; object-per-beat for UI sections

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 5 ("The Free Trial Is A Countdown", 53.9s) - the most
real-UI-heavy section. Built to template with 5 distinct vivid bases (blank phone → keyboard desk →
HOURGLASS → blank phone → wallet → piggy) and CSS real-UI per beat (FREE splash, credit card, FREE-TRIAL
00:00 → $2.99/mo flip, Day-7 reminder that fades, translucent ghost charges, a bank statement). 4 giant
WIT beats. Sourcing was very flaky (Openverse empty on card/desk/calendar/statement queries).

Reusable lessons:
- For UI-heavy sections, satisfy "real photo base + real-UI" two ways: (1) a "Hand holding smartphone with
  BLANK WHITE SCREEN" photo (Wikimedia) is the perfect CSS-UI canvas - float the app screen on it; (2) pick
  a literal OBJECT for the concept instead of forcing a phone every time - an HOURGLASS for "the free trial
  is a COUNTDOWN" is far better than another phone, and keeps bases distinct.
- The earlier S4 "rings circle nothing" lesson, applied forward: here the one red ring rings a row in a CSS
  bank statement *I control*, so it lands exactly on the `?? UNKNOWN −$3.00` row. A ring on a CSS element is
  safe/meaningful; a ring on a photo is not. NOTE: estimating the row's Y from CSS padding was off by a row -
  it took 2 snapshot nudges to align; always snapshot-verify a ring's target row.
- When sourcing is blocked, lean into the owner's real-UI love: build the card/statement/flip/notification in
  CSS rather than chasing stock photos of them. Reject person-in-frame card photos (no-face), Apple flat-lays,
  ID-cards-with-faces, and cutout-illustrations-on-white.
- Don't plan emoji (👻/👍) - render a CSS shape/card instead (emoji fail in snapshot Chromium).

Promote to shared memory:
no; template is Core. Concrete render mechanics (blank-phone canvas, object-per-concept, ring-on-CSS-row).

### 2026-06-23 - A blank-screen-phone base reads as a placeholder; pick a concrete metaphor object

Classification: `Render lesson`

Context:
S5 review. Owner: "0:00 and 0:23 the illustrative images is white screen phone - this phone doesn't match
the scene and script… use 2 images instead of reuse the same image for 2 scenes." I'd used the same
blank-white-screen phone (the CSS-UI canvas) as the base for BS1 ("make it feel free") and BS4 ("they
forget"). Fixed: BS1 → a pink GIFT box (free = a gift/lure); BS4 → an everyday DESK (notebook + coffee =
a loud, busy life where the reminder is lost). All 6 bases now distinct.

Lesson:
- A "hand holding a phone with a blank white screen" is great as a CSS-UI *canvas*, but as a visible BASE it
  reads as an empty placeholder/mockup, not a scene - and it doesn't describe the line. Prefer a CONCRETE
  metaphor object that depicts the beat: a gift box for "they make it feel free," an everyday desk/clutter
  for "you forget / life is loud," an hourglass for "countdown," a wallet for "drained account."
- Reusing one base image for two scenes is a review failure even when non-adjacent - give every scene its
  own distinct base. (The earlier lint-driven "2nd filename" trick avoids the lint warning but NOT the
  visual repetition the owner objects to - only use it for a genuine, intended callback.)
- The CSS idea-devices (FREE splash, Day-7 reminder) are base-independent: swapping the photo base under
  them needed no device changes.

Promote to shared memory:
no; sharpens the existing "vivid object base per scene / no reuse" rule with the blank-phone-placeholder case.

### 2026-06-23 - S6 built; a literal maze for "cancel ordeal"; menu-breadcrumb device; callback-when-sourcing-fails

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 6 ("Easy In, No Way Out", 53s) - the cancel-maze /
negative-option-billing section. Strong distinct bases: a STOPWATCH (time asymmetry), a wooden LABYRINTH
game (the cancel ordeal - perfect for "vision quest / final boss / wandering the menus"), and a CONTRACT
(fine-print trick). Hero device: a 7-step CSS menu breadcrumb trail (account→settings→…→a phone number)
winding through the maze, each chip popping on its spoken step.

Reusable lessons:
- For an abstract PROCESS section (cancelling), a literal MAZE/labyrinth photo is a great hero - the
  "menu steps" become a breadcrumb path through it, and a running-away WIT sells the ordeal. Keep the
  breadcrumb chips in the left 2/3 so a side WIT doesn't cover them.
- Sourcing abstract tail beats ("the unfair burden / −1000 aura", "a part-time job with no salary") failed
  on the CC sources. When that happens, prefer a DELIBERATE darker-graded CALLBACK of the section's own
  controlling metaphor (here the maze returns for "−1000 aura, still lost"; the stopwatch returns for "an
  unpaid part-time job") over a sterile/off-tone stock photo - distinguish it with a dark grade + different
  CSS device + different WIT + a 2nd filename, and flag it to the owner as swappable. This is the allowed
  "purposeful callback" exception, not the lazy-reuse the owner rejects.
- Search-term traps to watch: "free labyrinth maze" surfaced a Holocaust memorial (off-tone); "white flag"
  surfaced war photos; "alarm/time clock" surfaced only PNG sticker illustrations or cluttered museum displays.
  Always VIEW before using; reject off-tone/illustration/people-bearing hits.

Promote to shared memory:
no; render execution mechanics (maze-as-process-hero, menu-breadcrumb device, callback-when-sourcing-fails).

### 2026-06-23 - S7 payoff built; ALL 7 sections done; closer recaps the motif + resolves on the script's final image

Classification: `Render lesson`

Context:
`why-everything-is-a-subscription-now` Section 7 ("Payoff: The Product Is You Not Cancelling", 54s) - the
closer. Built with 4 distinct bases (2 different money shots, a phone, a coin jar) + the phone reused ONCE
non-adjacently for the script's literal final image (the bank-app salary screen). This completes all 7
sections of the video (previewing on 1001–1007).

Reusable lessons:
- A payoff/closer can legitimately RECAP the video's core motif imagery (here money + the phone/device) -
  that's a feature of a closer, not lazy reuse - but still use DISTINCT shots per scene (two different money
  photos, not the same one) and only reuse the device non-adjacently for a motivated beat. Resolve on the
  script's literal final image: the bank-app salary card ("the one screen not asking for money") + the dry
  "your salary. for now." was the satisfying, on-script close.
- New CSS idea-devices that worked: a barcode `.ptag` ("THE PRODUCT: YOU") via `repeating-linear-gradient`;
  a bank statement where the "keep" row is green and the "ghost" rows are struck (`text-decoration:line-through`,
  red) for "keep what you love / cancel the ghosts"; a green "money coming IN" bank-app card for the salary.
- Emotional arc for a closer: realize → reframe (it's OK, just notice) → take control (cancel the ghosts) →
  wry win (the salary, for now). Map one giant WIT pose per beat: thinking → shocked → holding-receipt → deadpan.

Promote to shared memory:
no; render execution mechanics for closers (motif-recap, script-literal-final-image, barcode/statement devices).

### 2026-06-24 - Subscription vivid-hook template is the DEFAULT bar for this owner

Classification: `Render lesson`

Context:
On `why-buy-1-get-1-beats-50-off` Section 3, the first render used plain bases (dark wood table, white
veg basket) + all-CSS receipt cards + ~780px WIT. Owner rejected it: "backgrounds too simple, WIT too
small, texts/items too simple - follow subscription-now style, remake completely." Accepted remake:
5 vivid dark-graded money/coins/curtain bases, a giant kinetic number hero ($5 → red $10), popping
stamps/toast/banner, a 230px glowing FREE payoff, and GIANT WIT (~1120–1200px) varied per scene.

Lesson:
For this owner, the `why-everything-is-a-subscription-now` S1 vivid-hook template is the DEFAULT for
every section, not an option. Apply up front, don't wait for rejection: (1) vivid object base per scene
with a DARK dramatic grade (brightness ~0.42–0.55, high saturation) + heavy scrim/glow; (2) a varied
KINETIC hero device per beat (giant number/counter, popping toasts, banner takeover, glowing payoff) -
plain label/receipt cards only as small supporting strips; (3) WIT GIANT (~1120–1300px, ~1/2 frame),
varied side/scale/pose per scene; (4) ~5 scenes for a ~30s section with lots of pop/smash motion.
Money/coins/cash/curtain bases reused across sections (distinct grades) are fine and on-brand.

Apply next time:
- copy the subscription S1 CSS kit (bignum, toast, stamp, banner, payoff, giant WIT) and adapt content.
- a giant kinetic NUMBER beats a plain receipt/label card as the hero for any money/count beat.
- keep devices clear of the giant WIT's face (arrange opposite); fix collisions before handoff.

Promote to shared memory:
no; the template already lives in `_shared/systems/visual-production.md` + visual-plan memory. This
confirms it is the per-section DEFAULT for this owner - apply by default, not as a special case.

### 2026-06-24 - CSS class collision can shrink a scene base (name photo grades uniquely)

Classification: `Render lesson`

Context:
`why-buy-1-get-1-beats-50-off` Section 7 Scene C used `<img class="photo calc">` for the background,
but `.calc` was ALSO the class of the calculator-CARD device (`position:absolute; width:520px;
background; border`). The `.calc` rule overrode the `.photo` full-frame sizing, so the background
image rendered shrunk into a ~520px box with the rest of the frame black. The owner flagged it as
"the background looks bad / looks bug" at 0:12. Renaming the photo grade class to `.photo.abak`
(device card keeps `.calc`) fixed it instantly.

Lesson:
Never reuse a device/component class name (`.calc`, `.cd`, `.toast`, `.chip`, `.tag`, etc.) as a
`.photo.<x>` base-grade modifier in the same composition - the device CSS (width/position/background)
will clobber the full-frame `.photo` rule and break or shrink the base. Keep photo-grade modifiers in
their own namespace (e.g. `.photo.bgCalc`, `.photo.abak`) distinct from every device class.

Apply next time:
- when adding a `.photo.<x>` grade class, grep the file's CSS for an existing `.<x>` rule first; if it
  exists as a device, pick a different grade name.
- a base that renders as a narrow strip / partially black is the signature of this collision (or a
  bad src) - check the class names before re-sourcing the image.
- lint/validate do NOT catch this (it's valid CSS) - only the snapshot shows it; always eyeball each
  scene's base in the contact sheet.

Promote to shared memory:
no; render mechanics gotcha.

### 2026-06-28 - Green-screen WIT poses: chroma-key with a temp static ffmpeg before compositing

> SUPERSEDED same day: the owner had the WHOLE pose library chroma-keyed to TRANSPARENT in place
> (`.agents/_shared/assets/wit/poses/*.png` are now RGBA cutouts, committed). Render now composites
> poses DIRECTLY from `assets/poses/` - NO per-render keying, NO `poses-keyed` folder. The recipe below
> is kept only for history / if a future green-delivered pose ever needs keying.

Classification: `Operational lesson`

Context:
First render using the new green-screen WIT pose set (`#00B140`, rgb24, no alpha) on
`5-why-the-internet-is-full-of-ai-slop` Section 1. HyperFrames previews are browser HTML, so the green
cannot be keyed in CSS - the pose PNGs must be pre-keyed to transparent before being referenced. No
ffmpeg/whisper-cpp/python-whisper on PATH this box.

Lesson (reusable recipe on this Windows box):
- Get a static ffmpeg without polluting the system: `npm.cmd install --no-save @ffmpeg-installer/ffmpeg`
  in a temp dir; path = `node -e "console.log(require('@ffmpeg-installer/ffmpeg').path)"`.
- Key each pose: `ffmpeg -y -i pose.png -vf "colorkey=0x00B140:0.30:0.12,despill=type=green:mix=0.5:expand=0" out.png`.
  Result: clean transparent bg, white mascot fill + black outline + glasses preserved (verified by Read).
  Save keyed copies to `projects/<slug>/assets/poses-keyed/` and reference `./assets/poses-keyed/*.png`
  in the HTML (keep the green originals in `assets/poses/` as the library record).
- Word timings (the skill's word-timings-first rule) also worked via that same ffmpeg + transformers.js:
  `ffmpeg -i mp3 -ar 16000 -ac 1 -f f32le s.raw`, then `@xenova/transformers` `whisper-tiny.en`
  `return_timestamps:"word"` -> save `voiceover/section-XX-*/section-XX-word-timings.json`. ~1 min,
  aligned clean TTS well; pinned every cue/reveal to it (no estimating).
- Build skeleton copied from the approved `projects/3-.../section-01-hook/index.html` (per-scene clip on
  its own track, `<audio>` clip, GSAP timeline registered to `window.__timelines`, off-canvas WIT via
  `data-layout-allow-overflow` + `style="overflow:visible"`). Pre-made cards (owner-generated PNGs) with
  an artifact below them were cropped with CSS `clip-path: inset(...)`.

Apply next time:
- Always pre-key the green WIT poses to `assets/poses-keyed/` before writing HTML; verify one keyed pose
  with the Read tool before batching all.
- Generate real word-timings with the temp ffmpeg + transformers.js recipe rather than estimating.

Promote to shared memory:
no; render tooling recipe for the green-screen pose era. The chroma-key requirement is already implied
by brand-system; this records the concrete working command on this machine.

### 2026-06-28 - Render requires ALL section assets ready (no silent gap-filling)

Classification: `Operational lesson`

Context:
Owner directive: "When using /render require all assets of section are ready, update skills to require
that." Previously render was allowed to source/generate/placeholder a missing asset as a documented
fallback. Owner wants render to be a pure compositor: every asset must be produced by `visual-implement`
first.

Lesson:
Added the **All Section Assets Ready Gate** (hard) to `render/SKILL.md`: before building/rendering a
section, read `assets/asset-manifest.md`, confirm every referenced asset is a file present in `assets/`
(or `assets/poses/`) or explicitly render-CSS; if ANY is missing on disk or marked `prompt-ready /
awaiting generation` / `awaiting drop`, STOP and tell the user to finish `visual-implement` for those
assets, then rerun render. Render no longer fills gaps itself - the only exception is when the user
explicitly asks render to make a specific named asset this run. Also added matching Hard Fails, a
Quality-Bar line, a Workflow step, and updated the frontmatter description (and the Claude wrapper's
copy) so discovery reflects the new requirement. For `All`, gate per section and skip blocked sections.

Apply next time:
- Run the assets gate every render; never build a partial section or substitute a missing asset silently.
- In `All` mode, build only fully-ready sections and report the blocked ones with their missing files.

Promote to shared memory:
no; this is a render-skill gate. The pipeline architecture (visual-implement makes assets, render
composites) already lives in `_shared/channel/learning-log.md`.

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Render lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```

### 2026-06-30 - Section 4 (ai-slop) Built Clean First Pass; Cover Manifest-Flagged Brand Logos With A Bezel-Matching CSS Patch

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `5-why-the-internet-is-full-of-ai-slop` Section 4 ("The Machine That Feeds Itself", 52.971s,
9 scenes). All assets were already produced by visual-implement (8 generated heroes + 7 fresh photo
bases + 9 poses, all present on disk), so the All-Assets gate passed - note the manifest PROSE table
still said `prompt-ready / awaiting generation` for the generate rows even though the files existed and
the checklist marked them `[x]`; trust the files-on-disk + checklist, then fix the stale status text.
The per-section whisper scripts are pre-staged in `%TEMP%/wiw-whisper` (incl. `gen-s04.mjs`) with the
model cached; generating `section-04-word-timings.json` worked first try (ffmpeg-static decode ->
gen-sNN.mjs). Built to the standing bar (bright photo bases + side scrim, giant varied WIT, hard-show
labels, impact only on emphasis) and it passed snapshot QA with only minor fixes.

Lessons:
- A base photo can carry an incidental brand logo the manifest flags for crop/blur (here a DELL laptop
  bezel on `clean-bright-desk-1.jpg`). If the object is too central to crop out with `object-position`,
  COVER the logo with a small CSS patch whose color matches that exact surface (here a black
  `#0b0b0d` rounded rect over the black bezel; a silver patch on a black bezel reads as a blotch).
  Measure the logo position on the FULL-RES snapshot frame, not the scaled contact sheet - my first
  patch was placed from contact-sheet coords and landed on the screen instead of the bezel.
- `duplicate_media_discovery_risk` lint warnings are expected + non-blocking when the same file is the
  reused section MOTIF (engine across 4.1/4.8/4.9) or an intentionally TILED asset (`slop-clone.png`
  x6 as the flood barrage). Snapshots confirmed all instances render. Document, don't chase to zero.
- A persistent continuity HUD (the loop-ring lighting one node per Step) works as a top-level
  composition overlay on its own track (`data-start 0`, full duration) with GSAP targeting its child
  dots by selector; keep it small + top-right so it never collides with the top-left STEP chips/labels.

Apply next time:
- check files-on-disk + the manifest checklist, not just the prose status column, at the assets gate;
  fix stale `prompt-ready` text after compositing
- reuse the pre-staged `%TEMP%/wiw-whisper/gen-sNN.mjs` scripts for word timings; model is cached
- cover (don't crop) a central incidental brand logo with a surface-color-matched patch; verify on the
  full-res frame

Promote to shared memory:
no; render execution + environment behavior. The brand-logo-cover technique stays here.

### 2026-06-30 - Section 5 (ai-slop): Key Out Baked-Checkerboard "Transparency" + GSAP :nth-of-type vs :nth-child

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `5-why-the-internet-is-full-of-ai-slop` Section 5 ("It Already Got Out", 53.739s, 7 scenes:
music / books / kids / six-legged horse / job / payoff). Section motif = the GREY-SLUDGE FLOOD callback
from S1/S2, with the `.flood` waterline rising 13 -> 66 % across the 7 scenes and peaking at 5.7 with WIT
drowning while holding one real photo above the water. 6 generated heroes + 4 fresh bases + 2 reuse bases
+ 7 poses. Word timings generated first (159 words; whisper tail "inbox." 56.52 clamped to 53.739). Two
real defects surfaced during snapshot QA.

Lessons:
- A "transparent" generated PNG can actually be OPAQUE RGB with the transparency CHECKERBOARD baked into
  the pixels (the generator rendered its own UI backdrop). Signature: `Image.open(f).convert("RGBA")
  .getchannel("A").getextrema()` returns `(255,255)` (no real alpha) and the RGB is alternating ~254
  white / ~241-245 light-grey squares - vs a real cutout which returns `(0,255)`. Always check alpha
  extrema on every generated hero before compositing; 3 of 6 here (book / horse / polaroid) were baked,
  while the phone / document were real RGBA. Key the checkerboard out to true alpha with a tone-mask
  (light AND neutral: `mn>=200 & (mx-mn)<=28`) + `scipy.ndimage.label` connected components + keep ONLY
  border-touching components + `binary_dilation(iterations=1)` to swallow the antialiased fringe -> set
  alpha 0. This beats flood-fill-with-threshold, which leaves speckle at tonal boundaries. Back up the
  originals (here `assets/_raw-checkerboard/`).
- GSAP `:nth-of-type(n)` counts by element TYPE, not by class. `.thumb.slop:nth-of-type(1)` matched
  NOTHING because the 1st child div in the grid is a plain `.thumb` (no `.slop`) - so the tween silently
  did nothing and validate flagged "GSAP target not found". Use `:nth-child(n)` to target by sibling
  POSITION (the 4 slop tiles sit at child positions 2/4/6/9). Also give cue elements an explicit hidden
  default (`.ss { opacity:0 }`) so they don't flash before their pop.
- `snapshot` reads its positional arg as the PROJECT dir, not an output dir. Run `snapshot --at
  <comma-separated-timestamps>` with NO positional; output always lands in `snapshots/` named by
  timestamp index. Verify cue fixes with a before/after pair (here 24.5s = no SLOP stamps yet, 29.5s =
  all 4 popped).
- `duplicate_media_discovery_risk` again expected + non-blocking: `living-room-tv-1.jpg` reused 5.4/5.5
  (same room, different kid content). 0 errors is the gate; 75 contrast advisories on stylized text are
  the same class as S1-S4 and read fine.

Apply next time:
- check alpha extrema on EVERY generated hero at the assets gate; key out any baked checkerboard before compositing, back up the raw
- target GSAP child elements with `:nth-child` (sibling position), never `:nth-of-type`, when selecting by class; give animated cue elements a hidden default in CSS
- `snapshot --at <times>` with no positional dir; QA cue timing with a before/after snapshot pair

Promote to shared memory:
no; render execution mechanics + tooling. The checkerboard-keyout + selector gotchas stay here.

### 2026-06-30 - Section 6 (ai-slop): Baked Checkerboard Recurs; Don't Reinstall Over The Whisper Cache; Keep Marks Off WIT's Face

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `5-why-the-internet-is-full-of-ai-slop` Section 6 ("It's Not AI's Fault (And Not A Plot)",
38.933s, 7 scenes - the fair/calm turn). Generated word timings first (123 words; whisper tail
"incentive." end 47.96 clamped to 38.933). 3 of the 4 generate props had the SAME baked
transparency-checkerboard as S5 (`artist-easel`, `empty-villain-throne`, `uncuffable-incentive`;
`tinfoil-hat` was real RGBA), keyed out with the S5 method. Built to the standing bar; passed snapshot
QA after 3 WIT-collision fixes.

Lessons:
- The baked-checkerboard "fake transparency" is now a RECURRING delivery defect (S5: 3/6, S6: 3/4).
  Make the alpha-extrema check (`(255,255)` = opaque/baked, `(0,255)` = real) a STANDARD assets-gate
  step for every generated PNG, and key out any opaque ones before compositing (tone-mask `mn>=200 &
  (mx-mn)<=28` -> scipy connected components -> keep only BORDER-touching -> 1px dilation). Interior
  whites (an easel canvas, a coin's glow halo + sparkles) are non-border components and correctly
  survive. Back up raws to `assets/_raw-checkerboard/`.
- WHISPER CACHE TOOLING: `npm install --no-save <pkg>` in `%TEMP%/wiw-whisper` PRUNES the other
  packages (it "removed 81 packages" and wiped `@xenova/transformers` + its `.cache` model). Symptom:
  `pipeline()` dies with a hard native EXIT 127 (no catchable JS error) because the decoder
  `.onnx` only partially re-downloaded (encoder present, `decoder_model_merged_quantized.onnx` missing).
  Fixes: (1) install ffmpeg + transformers together in one `npm install --no-save @xenova/transformers@2.17.2
  @ffmpeg-installer/ffmpeg`; (2) a COMPLETE model cache survives at `%TEMP%/wiw-tools/node_modules/
  @xenova/transformers/.cache/Xenova/whisper-tiny.en` - copy it into the whisper dir's cache to restore
  the decoder instantly instead of waiting on a flaky re-download. ffmpeg path:
  `node -e "console.log(require('@ffmpeg-installer/ffmpeg').path)"`.
- KEEP MARKS/TEXT OFF WIT'S FACE (both directions, again): first snapshot put the giant red X over
  WIT's deadpan face (the deadpan IS the 6.5 joke), the "money rewards it" label on WIT's white body,
  and the payoff lines over WIT's face. All three were obvious only in the snapshot (lint/validate/
  inspect passed). Fix by moving the MARK/TEXT to clear negative space (the board, the dark floor,
  center), not by shrinking WIT. Always snapshot every scene's payoff frame and check WIT-face overlap.
- The validator's contrast advisories measure stylized text against the PHOTO BEHIND, ignoring a
  device card's own opaque background - so an AI badge / green check / cream pinnote with a solid bg
  reads fine despite a "1.15:1" advisory. 0 errors is the gate; document the advisories as non-blocking.

Apply next time:
- alpha-extrema check + checkerboard keyout is now routine for generated props; expect ~half to be baked
- never `npm install --no-save` a single pkg into `wiw-whisper` (it prunes transformers + model cache); install together, or restore the model cache from `wiw-tools`
- snapshot every payoff frame and move any mark/text off WIT's face/body into clear space

Promote to shared memory:
no; render execution mechanics + tooling.

### 2026-06-30 - Sections 7 + 8 (ai-slop): Whisper Chunk-Boundary REORDER Glitch; Build Button Icons As CSS (Emoji Don't Render); Checkerboard Recurs Again

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered the last two sections of `5-why-the-internet-is-full-of-ai-slop` in one pass. S7 ("Payoff:
Attention In, Garbage Out", 43.413s, 7 scenes - the thesis-landing payoff) on port 1007; S8 ("Outro:
Like, Share, Subscribe", 7.957s, 2 scenes - the clean warm CTA) on port 1008. Generated word timings
first for both. S7's one generate prop (`slop-wins-trophy`) had the same baked checkerboard (now S5:3/6,
S6:3/4, S7:1/1) and was keyed out. Both passed snapshot QA; S7 needed two targeted re-snaps (1.3s, 14.2s)
to confirm cue text cleared WIT.

Lessons:
- NEW WHISPER ARTIFACT - CHUNK-BOUNDARY REORDER: beyond the known tail-glitch (last word's END runs long),
  whisper-tiny.en with `chunk_length_s:30 / stride_length_s:5` can also REORDER / mistime phrases that
  straddle a chunk boundary. In S7 the closing "you keep your eyes open" was pulled forward to ~35s, out
  of spoken order. Don't trust a word-timing JSON that is non-monotonic near a chunk seam: read the JSON,
  spot the out-of-order span, and PIN those few cues from the audio tail by ear/duration instead (S7's
  final cue pinned to 42.00). Document the one estimated cue in IMPLEMENTATION.md. Most of the file is
  still real timings - only the reordered span needs manual pinning.
- BUTTON / UI ICONS = CSS SHAPES, NOT EMOJI (reconfirmed, now load-bearing): the snapshot/preview Chromium
  does not render full-color emoji (👍 🔔 come out blank), but unicode dingbats (✓ &#10003;, → &#8594;) DO.
  For LIKE/SHARE/SUBSCRIBE built the thumb (palm+thumb+cuff divs), arrow (bar + border-triangle head), and
  bell (dome+lip+clapper) as pure CSS `<div>` shapes. They render crisply and scale (settled corner stack
  in 8.2 via a `.sm` modifier). Default to CSS shapes for ANY icon that must appear in a render.
- Checkerboard keyout is now fully routine - 1 prop this run, same method, ~5 min. Alpha-extrema check
  stays a standing assets-gate step.
- Same-base reuse for continuity is fine and only produces a non-blocking `duplicate_media_discovery_risk`
  lint warning: S7 reuses the slop-engine motif 4x + machine-hall 3x + bright-window 2x (3 warns); S8
  reuses bright-window across both scenes (1 warn). Intentional; document and move on.
- Section-first port + direct-comp URL pattern held: each section its own preview project with an `assets`
  junction; verified both servers return 200 (`http://localhost:1007/`, `http://localhost:1008/`).

Apply next time:
- after generating word timings, scan the JSON for non-monotonic word starts near 30s chunk seams; pin any reordered span from the audio tail and label it the estimated cue
- build every in-render icon/button glyph as CSS shapes, never color emoji; unicode dingbats are the only safe glyphs
- keep the alpha-extrema + checkerboard-keyout step routine for every generated PNG

Promote to shared memory:
no; render execution mechanics + tooling.

### 2026-06-30 - Section 8 (ai-slop) v2: Gamified Fake-YouTube CTA (Cursor Clicks The Buttons); Watch For CSS Class Collisions

Classification: `Render lesson` / `Design lesson`

Context:
Owner rejected the first S8 outro as "so boring" - it was three static pills that just popped in. Asked
for an over-the-top, superficial-fun end-card: a YouTube-screen popup with like/subscribe buttons, a
pointer that clicks them, buttons that wiggle and flip to liked/subscribed. Rebuilt the whole section as
a single continuous scene: a parody fake-YouTube card (all CSS/SVG, our own WhyTube/Why It Works branding,
no screen-grab) + an inline-SVG mouse cursor that flies in and CLICKS LIKE (2.24) / SHARE (3.14) /
SUBSCRIBE (5.22) on their spoken words, with boing wiggles, state cross-fades (red SUBSCRIBE -> grey
SUBSCRIBED + ringing bell, white LIKE -> blue Liked), a "Link copied!" toast, a pulsing glow ring, a
confetti burst, and a count tick (1.2M -> 1,200,001 + floating "+1"). Passed snapshot QA on all 6 beats.

Lessons:
- A "click-the-button" CTA is cheap and high-impact, all in deterministic GSAP: animate an inline-SVG
  cursor's `left`/`top` to each button center, click-dip its `scale`, and `boing` the button (one combined
  scale-up + rotate + settle, single transform set - do NOT layer a separate scale tween and rotate tween
  on the same element or they fight). Cross-fade two stacked state elements (red/grey, white/blue) at the
  click time instead of restyling one element. Pin every click to the real spoken word.
- CSS CLASS COLLISION BIT ME: the confetti pieces and the thumb-icon cuff both used class `.cf`. The bare
  `.cf` confetti color rules (`.cf:nth-child(6n+3){background:green}`) have the SAME specificity as the
  scoped `.ic-thumb .cf{background:currentColor}` and come LATER in the stylesheet, so they won the cuff's
  color (green cuff bug). Fix: namespace decorative-element classes (`.cfp` for confetti) so they can't
  match structural icon parts. When two unrelated things share a short class name, the later same-specificity
  rule silently wins - grep your class names before shipping.
- `overlapping_gsap_tweens` lint warnings are EXPECTED and non-blocking for intentional rapid
  micro-sequences (boing = 4 chained scale/rotate tweens, click-dip = 2). They already carry
  `overwrite:"auto"`. 0 errors is the gate; document the warnings as intentional.
- For a busy interactive card, a SINGLE continuous scene (no hard cut) is better than splitting into
  scenes - the card holds its final liked/subscribed state through the sign-off with no rebuild.
- Parody UI is the safe way to show a "YouTube screen": rebuild it in CSS with our own channel branding
  (WhyTube logo, Why It Works) - never a real screen-grab or a real channel/person.

Apply next time:
- reach for the cursor-clicks-button pattern for any CTA/explainer that should feel interactive; it is all CSS/SVG + GSAP, no assets
- namespace decorative classes (confetti, sparkles, particles) so they never collide with structural icon/sub-element classes; grep class names before snapshot
- treat boing/click-dip `overlapping_gsap_tweens` warnings as intentional; keep the gate at 0 errors

Promote to shared memory:
no; render execution mechanics + a reusable CTA technique.

### 2026-07-07 - First Render On The Linux Box (world-cup S1): Ports <1024, Symlink Assets OK, Snapshot First-Frame Race, Strip-Prop Geometry

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `6-why-countries-fight-to-host-the-world-cup` Section 1 (Hook, 35.904s, 7 scenes) - the
first render on the new LINUX machine (prior memory entries describe the old Windows box). Built
1:1 from the visual plan; word timings pre-existed and the plan's pinned timestamps matched the
JSON exactly. All 16 assets passed the gate (all real RGBA - no baked checkerboard this time).
Lint 0 err / validate 0 err / inspect 0 issues; 4 defects found and fixed via snapshot QA.

Lessons (Linux environment - replaces the Windows habits):
- Ports 1000-1023 are PRIVILEGED on Linux: `hyperframes preview --port 1001` dies with
  `listen EACCES`. Fix that keeps the channel's fixed-port convention:
  `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=1000` (passwordless sudo works on this box).
  NOT persistent - re-run after reboot or persist in /etc/sysctl.d/.
- The preview-local `assets` as a plain SYMLINK (`ln -sfn ../../assets`) serves fine (HTTP 200 on
  deep asset paths). The Windows junction-404/hardlink workaround is NOT needed here.
- Plain `npm`/`npx` (no `npm.cmd`); no ffmpeg on PATH but none needed when word timings exist.
- Preview project id resolves to the section FOLDER name (`1-hook`) - confirm via `/api/projects`.

Lessons (render mechanics):
- SNAPSHOT FIRST-FRAME RACE: in screenshot-fallback mode (system Chrome, no chrome-headless-shell)
  the FIRST captured frame of a run can miss a late-decoding PNG (trophy absent at frame 1 in three
  separate runs; a pose missed once mid-run). It is a tool artifact, not a composition bug - verify
  by re-snapping the same timestamp NOT in first position before editing anything. Consider
  installing chrome-headless-shell for the optimized path if exports are requested.
- ROTATED STRIP PROPS (receipt "printing" from a plinth): a rotated wrapper's top corners swing out
  of the anchor object - pivot `transform-origin: top center`, place the top edge ON the plinth, and
  make the plinth tall/wide enough to cover the swing (corner y = cy - sin(a)*w/2). Animate
  `clip-path inset(0 0 92% 0) -> inset(0 0 0 0)` with ease:none for a believable printer crawl;
  z-index ABOVE podium+WIT makes it read as printing over the scene and rolling over WIT's feet.
- NEARLY-90deg-ROTATED imgs (receipt folds pile): the rotated box centers at (left+w/2, top+h/2) of
  the UNROTATED box - a 560x1120 fold set at top:430 lands its band at y~710-1270 (bottom edge!).
  Compute centers first: top = targetCenterY - h/2. For a pan-reveal, folds must center >= 1920 +
  visibleHalfWidth pre-pan or they leak into the glamour phase; that forced pan x:-1100 (not -670),
  which slides the hero almost fully out - acceptable when the revealed motif carries phase B.
- BASE PHOTO DEFECT CROP-OUT: a vertical fold seam that a podium cannot fully hide is killed with
  `transform:scale(2.09); transform-origin:0% 50%` (crop to the clean left region) + a sepia/saturate
  regrade to restore the parchment warmth the zoom loses. Scene overflow is fine (root clips).
- S7-style shoulder drape: first placement covered WIT's MOUTH - any prop crossing the torso needs a
  face-clearance snapshot check, same rule as text-over-WIT.

Apply next time:
- run the sysctl port fix before starting any preview server on this box; symlink assets directly
- re-snap a "missing element" frame in non-first position before touching the composition
- compute rotated-box centers for every strip/fold prop; pivot strips on the anchor object
- crop out base-photo defects with scale+origin and regrade, instead of patch overlays on texture

Promote to shared memory:
partial - the Linux port/symlink/tooling facts belong in a shared environment note if more skills hit
them (combine/shorts also bind ports); the strip-geometry and snapshot-race mechanics stay here.

### 2026-07-07 - Section 2 (world-cup): Pose Catalog vs Pixels Mismatch; mix-blend-mode Is Isolated; Degenerate scaleX(0) Loses Rotation

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `6-why-countries-fight-to-host-the-world-cup` Section 2 (Reframe, 33.728s, 5 scenes) on the
Linux box, port 1002. All assets pre-made (gate passed, all real RGBA). Word-timings had the known
whisper duplicate-backward-pass glitch (words 91-109) which the visual plan had already mapped -
pinning to the first pass worked directly. Three new build gotchas surfaced in snapshot QA.

Lessons:
- POSE CATALOG LIES: `rich_flex_gold_chain_sunglasses.png` in the pose-transferred library does NOT
  match its `pose.md` entry ("gray hair + gold chain + sunglasses + tank top") - the pixels are a
  plain hands-behind-back smirk. `smug_sly_smirk_leaning` is nearly the same plain figure. The
  2026-06-28 pose-transfer regenerated bodies without the costumes/props some catalog names promise.
  ALWAYS view the actual pose PNG before building a beat around its name; substitute the closest
  real-pixels pose (here `boss_suit_sunglasses_sparkle` = glasses-adjust smug flex) and document.
- `mix-blend-mode` DOES NOT SURVIVE this pipeline: a white-studio-bg JPG composited with
  `mix-blend-mode:multiply` rendered as an opaque white box (any positioned/z-indexed ancestor
  isolates the blend, and the screenshot capture path is unreliable with it anyway). For a
  white-background photo that must sit on another base, KEY the white out into a derived cutout
  (border-connected near-white BFS + 1px dilation works in pure PIL - no numpy/scipy on this box),
  save as `<name>-cutout.png`, note it in ATTRIBUTION.md, keep the original.
- DEGENERATE INLINE TRANSFORM: `transform:rotate(14deg) scaleX(0)` collapses the matrix - GSAP
  cannot decompose rotation out of a zero-scaled matrix, so the tweened element renders UNROTATED
  (the 2.2 X strokes drew near-horizontal). Keep only the rotation inline and apply `scaleX(0)` via
  `tl.set(...)` at scene start; GSAP then tracks components correctly.
- Snapshot first-frame decode race recurred (TAXPAYER card emboss "missing" at 27.9); re-snapping
  the same timestamp in non-first position rendered it fully. Re-snap before editing anything.

Apply next time:
- view every pose before first use even when the catalog name sounds right; expect name/pixels drift
- never rely on mix-blend-mode for compositing; key a cutout instead
- never combine rotate + scaleX(0)/scaleY(0) in one inline transform for a GSAP-tweened element

Promote to shared memory:
no; render execution mechanics. The pose-catalog drift may deserve a `visual-implement`/pose.md
cleanup note if it recurs.

### 2026-07-07 - Section 3 (world-cup): Check Asset Content BBox Before Sizing; Don't Fake "Behind" Crops The Photo Can't Support

Classification: `Render lesson`

Context:
Rendered `6-why-countries-fight-to-host-the-world-cup` Section 3 (Promise Machine, 60.779s,
8 scenes, port 1003). Densest section so far (~40 cues: balloon inflations, a pin pop with
scrap burst, a banknote turnstile squeeze, coin drops, a ghost-note size comparison). Three
QA rounds; all misses were geometry/content, not timing.

Lessons:
- CONTENT BBOX != CANVAS: several generated PNGs are much smaller than their canvas
  (`receipt-endless-roll.png` paper = ~37% of canvas width; `balloon-deflated-grey.png` =
  a narrow full-height hanging strip). Sizing a wrapper by canvas width made the receipt
  strip too thin to carry its cue-critical text and made the lying deflated balloons
  invisible (content off-frame). Run `Image.getbbox()` per asset BEFORE laying out any
  strip/lying/text-carrying prop, and put must-read text on a self-carried chip (white
  receipt-excerpt card) when the asset can't carry it.
- DON'T FAKE A "BEHIND" CROP: the plan wanted WIT waist-cropped behind the turnstile bar,
  but the photo has no barrier at that x - an overflow-hidden wrapper crop read as a
  floating half-body. If the base photo lacks a real occluder at the planned position,
  reposition WIT (frame-edge crop at the bottom/side) instead of wrapper-cropping mid-air.
  Wrapper crops only work when the crop line lands on a believable photo edge (S2.4's
  counter line worked; S3.7's walkway did not).
- Static connector lines (balloon strings to an anchor) break as soon as the connected
  element scales/moves - drop them or animate them with the element; the prop's own baked
  string usually suffices.
- A prop resting ON WIT's face (the thrown pushpin's rest position) is the same class of
  bug as text-over-face - check every prop's rest/hold position against WIT's head zone,
  not just its entrance.

Apply next time:
- bbox-check every strip/tall/lying asset at the assets gate alongside the alpha check
- pick WIT crop strategy from the actual photo's occluders, not the plan's wording
- give echo/restamp beats clearly separated positions (no stacked text), per the S2 rule

Promote to shared memory:
no; render execution mechanics.

### 2026-07-07 - Section 4 (world-cup): Scripted-Edit Placeholder Corrupted HTML; fromTo From-Only Props Tween Back To Current; Validator "GSAP target not found" Can Be A REAL Missing Element

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `6-why-countries-fight-to-host-the-world-cup` Section 4 (FIFA Keeps The Money, 62.101s,
9 scenes, port 1004). All 27 assets passed the gate (all real RGBA). Built to plan; four snapshot-QA
rounds. Three new reusable gotchas.

Lessons:
- SCRIPTED-EDIT PLACEHOLDER BUG (self-inflicted): a python batch-edit used 'KEEP' as a temporary
  swap token; the token matched INSIDE unrelated content ("WHAT FIFA KEEPS") and injected a broken
  `style="` attribute whose unclosed quote swallowed the next sibling element at parse time. Symptom
  chain: validate warned `GSAP target not found` for an element that WAS in the source, and the
  snapshot showed the header text truncated + the element missing. When using scripted replaces,
  pick sentinel tokens that cannot occur in the file (e.g. `@@X9@@`), and treat a "target not found"
  warning as possibly REAL - check the COMPILED comp DOM (`/api/projects/<id>/preview/comp/index.html`)
  and the snapshot before dismissing it as a tool quirk.
- GSAP fromTo: a property present ONLY in the from-vars (e.g. `fromTo(el, {opacity:1, scaleY:0},
  {scaleY:1})`) tweens that property from the from-value BACK to its pre-tween current value -
  the EXPECTS plate flashed and vanished (opacity 1 -> 0 over the tween). Set opacity with a separate
  `tl.set` and tween only the intended transform.
- Sets pinned exactly on a clip's start boundary (e.g. 4.04 for a clip starting 4.04) made the
  validator's GSAP resolution flaky for one element; nudging the hide/show sets ~0.02-0.16s into the
  clip fixed it with no visual change. Prefer cue sets slightly after the clip boundary.
- Reconfirmed: pose-catalog drift (`rich_flex_gold_chain_sunglasses` is still the plain smirk - use
  `boss_suit_sunglasses_sparkle`), adapt layouts to the real photo geometry instead of faking physics
  (4.8's "level two-pan scale" is actually a hanging pan + a flat desk disc - the sack went into the
  real hanging pan and the CSS beam tilt was dropped), and mirror poses via a wrapper (flip on the
  inner img) so GSAP tweens never touch the scaleX(-1).

Apply next time:
- unique sentinel tokens in scripted edits; verify compiled DOM when validate flags a missing GSAP target
- never put a property only in fromTo's from-vars; tl.set it separately
- keep cue sets off exact clip-start boundaries
- snapshot-check every text/prop against WIT's face zone (4.8 plate + 4.9 bang lines both needed moves)

Promote to shared memory:
no; render execution mechanics.

### 2026-07-07 - Section 5 (world-cup): Measure WIT From The Snapshot When Math Disagrees; Legibility Chips Beat Bare Text; Build Direction Devices As Real Paths

Classification: `Render lesson`

Context:
Rendered `6-why-countries-fight-to-host-the-world-cup` Section 5 (Three Drains, 55.851s, 7 scenes,
port 1005). All 26 assets pre-made and real RGBA. Six quick snapshot rounds; all fixes were
readability/geometry, not timing.

Lessons:
- BBOX MATH CAN LIE ABOUT RENDERED POSITION: the shocked pose anchored by `top` landed ~150px lower
  than the content-bbox arithmetic predicted (cause not chased). When a character lands off-target,
  don't re-derive the math - measure the offset on the snapshot and re-anchor. One measurement beat
  three recalculations.
- BARE TEXT ON BUSY PHOTOS FAILS REPEATEDLY: white numerals on confetti, white handwriting on a
  bright window, black handwriting near a white surround - all unreadable in snapshots. The reliable
  fix is the same every time: put the text on its own chip (dark circle chips on the grates, the
  standard cream chip for `bye.`). Default any free-floating cue word to a chip when the base is
  textured or high-key.
- DIRECTION DEVICES MUST BE REAL PATHS: a border-radius dome arc + stray arrowhead read as a rainbow,
  not a U-turn. Build direction gags from explicit path segments (in-line, loop, out-line, arrowhead)
  so the motion story is unambiguous even paused.
- A scripted [beat] freeze = simply NO tweens in that window; lint will demand a hard-kill set when an
  exit tween ends exactly on the clip boundary (gsap_exit_missing_hard_kill) - end the fade 0.1s early
  and add a tl.set kill.
- Mirrored-asset wrappers (flip on inner img) worked for three different asset types this section
  (pose, flock, walking bills) - now the standing pattern for any leftward-drawn asset that must face right.

Apply next time:
- snapshot-measure misplaced characters instead of re-deriving bbox math
- chip any cue text that sits on texture; keep bare handwriting for clean/dark zones only
- draw turns/loops as segmented paths; verify the arrowhead exists in the snapshot

Promote to shared memory:
no; render execution mechanics.

### 2026-07-07 - Section 6 (world-cup): clip-path Wipe Clips Protruding Children; Ground Creatures On The Photo's Ground Band; sysctl Port Fix Resets On Reboot

Classification: `Render lesson` / `Operational lesson`

Context:
Rendered `6-why-countries-fight-to-host-the-world-cup` Section 6 (The Morning After, 61.44s,
8 scenes, port 1006). All 25 assets pre-made and real RGBA (first section of this video with zero
baked-checkerboard); the plan's pinned cue times matched the word-timings JSON exactly. Two QA
rounds; lint/validate/inspect 0 errors.

Lessons:
- CLIP-PATH WIPE CLIPS PROTRUDING CHILDREN: a draw-on container revealed with
  `clip-path:inset(...)` clips its absolutely-positioned children to the ELEMENT BOX even after
  the wipe completes - a timeline year label at `left:-16px` rendered as "014". Keep every child
  inside the container's box (pad the box, shift internals) when using clip-path reveals.
- GROUND A CREATURE/PROP ON THE PHOTO'S GROUND BAND: the elephant-stadium hero was positioned by
  %-of-frame from the plan and floated in the sky - the base photo's grass band started much
  lower than the plan's nominal horizon. Anchor feet to the actual ground band measured on the
  photo (content-bbox bottom -> ground y), same class as the S5 snapshot-measure rule.
- The whisper corrupt-tail bypass worked as planned: pin the final beat to the last GOOD word's
  end (Bruno@60.86) and clamp to audio duration; never use a backward-jump timestamp.
- Linux box: `net.ipv4.ip_unprivileged_port_start` had RESET to 1024 (reboot since the last
  session) - re-run `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=1000` before starting any
  100x preview server; consider persisting in /etc/sysctl.d/ if this recurs.
- Reconfirmed standing rules that caught real defects in snapshot QA: chip any cue text on a
  bright/textured base (bare white handwriting on sky was unreadable), keep the zoom-lens inset
  on the pose's physical glass instead of near the face, and put must-read receipt text on a
  self-carried chip.

Apply next time:
- pad clip-path-wiped containers so no child sticks out of the box
- measure the base photo's ground band before placing any standing creature/prop
- re-check the sysctl port floor at the start of every render session on this box

Promote to shared memory:
no; render execution mechanics + environment note.

### 2026-07-07 - Sections 7+8+9 (world-cup) Built By THREE PARALLEL AGENTS In One Run; New Text/Type-On, Decorated-Base, And CTA-Port Mechanics

Classification: `Render lesson` / `Operational lesson`

Context:
The owner asked to render Sections 7, 8, and 9 of `6-why-countries-fight-to-host-the-world-cup` "in
parallel". The orchestrator ran all gates first (assets on disk vs manifest, word timings, ports free,
sysctl port floor re-applied - it HAD reset again since the morning session), then spawned three
concurrent agents, one section each. All three passed lint/validate 0 errors and snapshot QA
(S7: 9 scenes 66.987s port 1007; S8: 6 scenes 39.573s port 1008; S9: 2 scenes 17.877s port 1009).

Lessons:
- PARALLEL SECTION RENDERING WORKS when each agent stays inside its own `previews/<N>-*/` folder +
  its own `hyperframes/review/section-XX.html`, and ALL shared files (`05-production-board.md`,
  `asset-manifest.md`, `ATTRIBUTION.md`, this memory file) are written ONLY by the orchestrator after
  the agents finish. Give each agent the full required-reading list, the Linux environment facts, and
  an explicit do-not-touch list. Derived assets get NEW filenames and are reported up, not logged
  directly.
- CENTERED TYPE-ON CLIPS HALF-WORDS: a `clip-path` type-on/wipe across CENTERED (or multi-line) text
  reveals clipped word fragments mid-animation ("worlc/expensi"). Use per-line word-timed hard-shows
  for typed captions, or left-align a single line so the wipe follows the reading direction.
- DECORATED/HOLIDAY BASE NEUTRALIZATION: when the only good base carries seasonal decor (Christmas
  mantel), crop INTO a clean texture region (chimney breast, `transform: scale(2.35)` + origin) +
  desaturate/cool-grade to kill the palette, and rebuild the load-bearing surface (the shelf) as a
  CSS prop instead of fighting the photo's geometry.
- CSS TEXT ON IMAGE PROPS: anchor the text to the MEASURED content face (bbox) of the asset (a paper
  tag's face), never to the PNG canvas top - canvas padding puts text on the string/knot.
- BAKED-STATE PROPS ANIMATE VIA PATCH + REPLICA: to animate a needle/X/dial that is baked into a
  generated PNG, cover the baked state with a BLURRED gradient patch (a crisp cream patch reads as a
  pill) and reveal a CSS replica from the beat onward.
- DETACHED CSS EMOTION MARKS READ AS NOISE: pose-catalog descriptions still drift from pixels
  (`furious_shouting_anger_mark` has NO separate mark). If the pose already carries the emotion, drop
  the companion CSS mark entirely rather than drawing one next to the face.
- CTA KIT PORTS CLEANLY: the ai-slop S8 fake-YouTube cursor-click card adapts directly (new copy, new
  timings). Center click targets on the pill's right HALF so the cursor never sits on the button text
  at flip time; check toast/snackbar subtitle-safety at the ZOOMED position when the card gets a
  push-in (a 6% zoom drifts bottom elements ~2% down); occlusion gags whose plan wording conflicts
  with the plan's own zones resolve best as a believable frame-edge crop (rise-from-bottom) instead of
  a fake mid-air wrapper crop.
- SNAPSHOT FILENAMES TRUNCATE DECIMALS: `--at 39.65` writes `frame-NN-at-39.6s.png` - glob by prefix
  when reading QA frames, don't build the exact path from the requested timestamp.

Apply next time:
- for multi-section requests, gate centrally, fan out one agent per section, reserve shared files for
  the orchestrator
- word-timed per-line hard-shows for typed captions; bbox-anchor tag text; blurred patches over baked
  prop states; no detached emotion marks; re-check the sysctl port floor EVERY session (it keeps
  resetting)

Promote to shared memory:
no; render execution + orchestration mechanics.
