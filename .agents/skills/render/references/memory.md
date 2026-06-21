# Render Skill Memory

This file stores memory specific to the `render` skill.

Use `.agents/_shared/` for channel-wide visual rules, audio rules, WIT identity, and HyperFrames-first production strategy.
Use this file for section preview structure, port behavior, HyperFrames CLI habits, server handling, and lessons about making section builds easier to review.

## Current Skill Standard

- Run after `visual-plan`.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, `02-script.md`, `04-voiceover.md`, and `05-visual-plan.md`.
- Require matching section voiceover output and matching section visual-plan output.
- Do not require `03-packaging.md`; packaging is a side branch.
- Require explicit user section selection: `All` or a specific section.
- Build one HyperFrames preview project per section under `section-previews/section-XX-kebab-section-name/`.
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

For each selected section, create or update:

- `section-previews/section-XX-kebab-section-name/index.html`
- `section-previews/section-XX-kebab-section-name/DESIGN.md`
- `section-previews/section-XX-kebab-section-name/package.json`
- `section-previews/section-XX-kebab-section-name/hyperframes.json`
- `section-previews/section-XX-kebab-section-name/assets` junction to `../../assets`
- `hyperframes/review/section-XX.html`
- `06-production-board.md`

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
Use section port `1000 + section number`, reserve `1000` for unified preview, and write section build status into `06-production-board.md`.

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
Keep `projects/<slug>/assets/` as the source of truth, but if HyperFrames CLI checks fail to serve a section preview's junction-backed `assets/` folder on this Windows setup, materialize a minimal preview-local hardlinked asset working set for only the files used by that section and document the exception in `06-production-board.md`.

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
The user rejected the second Section 1 replacement for `why-everyone-pretends-to-be-busy` because the rendered WIT was not the channel's WIT and the section still felt messy. The user pointed to the complete WIT pose library in `projects/why-cheap-products-keep-getting-worse/assets/wit` and asked for a complete remake.

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
- record the override, checks, render path, and stale downstream notes in `06-production-board.md`

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
- hand any WIT face/glass/tag collision QA points to Review/Auto-Adjust rather than redesigning during a restore

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
- `object-fit: cover` from a frame-width source only crops vertically — pick a different image if a side-edge element must go

Promote to shared memory:
no; the upstream prevention lives in `visual-plan/SKILL.md` (Real Scene Base Rule + sourcing recipe). Keep render-side enforcement here.

### 2026-06-21 - Generate Word Timings With transformers.js (Don't Estimate)

Classification: `Render lesson`

Context:
Sections 4 and 7 of `why-cheap-products-keep-getting-worse` were first built with estimated cue timing because no `word-timings.json` existed and `hyperframes transcribe` needs whisper-cpp (not installed; no Python/faster-whisper either). The estimates drifted badly — for Section 4 the voice rattled the parts list out ~4s earlier than estimated (e.g. "a hinge" spoken at 5.66s but shown at 9.5s), so Anh Khoa reported "the text doesn't match the voice again." Generating real word timings and re-pinning every cut/reveal fixed it.

Lesson:
Estimating cue timing is unreliable and keeps producing "text doesn't match the voice" review hits. When a section lacks `word-timings.json`, generate it. Whisper via `transformers.js` (`@xenova/transformers@2.17.2`, `Xenova/whisper-tiny.en`) runs in WASM with NO native deps — it works on this Windows box where whisper-cpp/Python do not.

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
The first two runs threw `Error: Unsupported model type: whisper` — caused by an earlier
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
- ESM ignores NODE_PATH — run the gen script from inside the `--prefix` dir where node_modules resolves

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
base — it is NOT the "bare gradient" the hard-fail rule forbids. This is usually cleaner AND more
on-brand than dingy stock. Keep cue timing/WIT unchanged; only swap the base layer.

Apply next time:
- confirm no image generator, then build flat-illustrated bases instead of re-searching stock
- a packed calendar reads "overbooked" via many small colored event chips in the cells
- reuse the same illustrated base for an intentional bookend (Scene A bright, Scene C cool+cage bars)
- keep the photo refs on disk as `inspiration only`; document the base swap in IMPLEMENTATION.md + visual plan
- expect many non-blocking contrast warnings from a grid of small cells; 0 errors is the gate

Promote to shared memory:
no; render execution behavior. (If image generation becomes available, prefer generated clean bases.)

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
