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
- Every selected section must run a visual reference pass before finalizing the plan.
- Real internet, self-shot, or existing local images are the default first layer for the reference pass because they make the video feel closer to the viewer.
- Generated images are support assets, controlled mockups, cleanup/fallback images, or composition tests after real references are understood.
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
- board-level timing mapped to voiceover
- visual resource usage map with what / when / how / where for each important asset
- reference and asset plan with source status
- HyperFrames guidance that names what the renderer must not invent

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
Scene and board plans are not enough if individual assets remain ambiguous. Each important visual resource needs a usage map: what it contributes, when it appears, how it is animated or transformed, where it sits or crops on screen, and whether it is a direct asset, mockup target, support base, inspiration only, or rejected.

Apply next time:

- include `Visual Resource Usage Map` in every section visual plan
- map each important resource to boards and local time ranges
- name crop/placement and overlay relationship
- tell HyperFrames what not to use directly

Promote to shared memory:
no; keep as visual-plan output contract unless repeated render failures show this belongs channel-wide.

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
