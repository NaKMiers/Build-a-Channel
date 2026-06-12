# Visual Plan Skill Memory

This file stores memory specific to the `visual-plan` skill.

Use `.agents/_shared/` for channel-wide visual systems, WIT identity, HyperFrames grammar, reference safety rules, and reusable production lessons.
Use this file for section-selection behavior, section visual-plan output shape, reference-board habits, asset planning notes, and lessons about making plans easier to build in HyperFrames.

## Current Skill Standard

- Run after `voiceover`.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, `02-script.md`, and `04-voiceover.md`.
- Packaging is outside the main pipeline and must not block visual planning.
- If voiceover is older than script, stop and ask for `voiceover`.
- Require matching section voiceover output for each selected section.
- Require the user to explicitly select `All` or a specific section before creating or editing visual-plan files.
- Put `All` at the top of section choices.
- Interpret `All` as separate visual-plan outputs for every section, not one giant full-video board table.
- Write `05-visual-plan.md` as the project-level visual-plan index.
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
- `05-visual-plan.md`

`05-visual-plan.md` should act as the project-level index for generated and not-yet-generated section visual plans.

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
Use the section list from `02-script.md`, verify matching `04-voiceover.md` section output, and do not infer the target section from existing work.

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
