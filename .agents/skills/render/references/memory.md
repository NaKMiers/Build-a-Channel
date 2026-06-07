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
- Do not use `inspiration only` or `reject` real images directly in final render output.
- Require a voice cue map before animation: every scene and on-screen element must match the current voiceover beat.
- Build hard-cut timing first. Add transitions only after the section matches the voiceover.
- Choose transitions per scene boundary. Do not reuse one default transition everywhere.
- If a transition damages voice sync, simplify it or use a hard cut.
- Design element entrance, hold, emphasis, and exit against spoken cues.
- Emphasized spoken words such as `FREE`, `URGENT`, or `BUSY` should get matching visual emphasis when they are important to the beat.
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

Optional MP4/WebM section renders belong under:

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
