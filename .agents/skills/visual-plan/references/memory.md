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
