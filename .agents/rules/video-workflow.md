# Video Workflow Rules

`Why It Works` uses a `0-9` video lifecycle.

## Steps

0. Topic intake
1. Research pack
2. Script draft
3. Packaging: title, thumbnail, and YouTube description
4. Voiceover
5. Visual plan
6. Render
7. Review
8. Upload
9. Learning

Packaging is outside the main production pipeline.

Main production chain:

```text
TopicIntake -> ResearchPack -> ScriptDraft -> Voiceover -> VisualPlan -> Render -> AutoAdjust -> Review -> Upload -> Learning
```

Packaging side branch:

```text
ResearchPack -> Packaging
```

## Pipeline Dependency Rule

Skills must run in order: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10`.

Before running step `N`, verify every previous required output exists and is non-empty inside the same `projects/<slug>/` folder.

If a required previous output is missing, stop and tell the user exactly which skill must run first. Do not create placeholder upstream files from a later skill.

Current dependency chain:

| Step | Skill                 | Output                                                                    | Required Before Running                              |
| ---: | --------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------- |
|    0 | `topic-intake`        | `00-topic-intake.md`                                                      | none                                                 |
|    1 | `research-pack`       | `01-research-pack.md`                                                     | `00-topic-intake.md`                                 |
|    2 | `script-draft`        | `02-script.md`                                                            | `00-topic-intake.md`, `01-research-pack.md`          |
|    3 | `packaging`           | `03-packaging.md` and optional `assets/thumbnails/`                       | `00-topic-intake.md`, `01-research-pack.md`          |
|    4 | `voiceover`           | `04-voiceover.md` and `voiceover/`                                        | `02-script.md`                                       |
|    5 | `visual-plan`         | `05-visual-plan.md`, `visual-plan/`, optional `assets/visual-references/` | `04-voiceover.md` and selected section voiceover     |
|    6 | `render`              | `06-production-board.md`, `section-previews/`, `hyperframes/`, `renders/` | `05-visual-plan.md` and selected section visual plan |
|  6.5 | `auto-adjust`         | targeted section preview fixes, review mirror sync, production-board notes | selected rendered section preview                    |
|    7 | future review skill   | `07-review.md`                                                            | rendered or previewable video sections               |
|    8 | future upload skill   | `08-upload.md`                                                            | approved review                                      |
|    9 | future learning skill | `09-self-learning.md`                                                     | upload or review results                             |

## Stale Downstream Rule

When a step is created, updated, or rerun, every later step output in the same project becomes stale.

Apply this every time:

- list any downstream files that now need removal or rerun
- do not trust stale downstream files as current source of truth
- do not silently delete downstream files
- remove stale downstream files only when the user explicitly asks for removal
- otherwise rerun downstream skills in order so each step rebuilds from the latest previous output

If an upstream file has a newer modified time than a downstream file, treat the downstream file as stale.

Packaging side-branch rule:

Packaging depends only on `00-topic-intake.md` and `01-research-pack.md`.
Packaging is not a prerequisite for `script-draft`, `voiceover`, `visual-plan`, render, review, upload, or learning.
Rerunning packaging does not make main pipeline outputs stale.

## Current Skill Coverage

- Step 0 `Topic intake` is implemented by `.agents/skills/topic-intake/`.
- Step 1 `Research pack` is implemented by `.agents/skills/research-pack/`.
- Step 2 `Script draft` is implemented by `.agents/skills/script-draft/`.
- Step 3 `Packaging` side branch is implemented by `.agents/skills/packaging/`.
- Step 4 `Voiceover` is implemented by `.agents/skills/voiceover/`.
- Step 5 `Visual plan` is implemented by `.agents/skills/visual-plan/`.
- Step 6 `Render` is implemented by `.agents/skills/render/`.
- Post-render `Auto Adjust` is implemented by `.agents/skills/auto-adjust/`.
- The remaining lifecycle steps do not have executable project-local skills yet.

## Section Production Branch

After `04-voiceover.md`, production can branch by section.

The `voiceover` skill should ask which script section to generate. It should offer `All` first, then each script section. `All` means generate separate voiceover outputs for every section, not one stitched full-video audio file.

The `visual-plan` skill should follow the same section-first behavior after `04-voiceover.md`. It should ask which section to plan, offer `All` first, and create separate visual-plan outputs for every selected section.

The `render` skill should follow the same section-first behavior after `05-visual-plan.md`. It should ask which section to build, offer `All` first, and create separate HyperFrames preview projects for every selected section.

The `auto-adjust` skill runs after `render` and before `review`. It should require one selected project and one selected section, preserve the current section preview as canonical, apply review-prevention fixes, and never offer or accept `All`.

Per-section voiceover outputs belong in:

```text
projects/<slug>/voiceover/section-XX-kebab-section-name/
```

The project-level voiceover index belongs in:

```text
projects/<slug>/04-voiceover.md
```

Per-section visual-plan outputs belong in:

```text
projects/<slug>/visual-plan/section-XX-kebab-section-name/
```

The project-level visual-plan index belongs in:

```text
projects/<slug>/05-visual-plan.md
```

Per-section render preview projects belong in:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/
```

Render ports are fixed:

```text
Unified/final preview -> localhost:1000
Section N preview -> localhost:1000 + N
```

## Project Outputs

Each new video should start from `projects/_template/` and produce:

- `00-topic-intake.md`
- `01-research-pack.md`
- `02-script.md`
- `03-packaging.md`
- `04-voiceover.md`
- `05-visual-plan.md`
- `06-production-board.md`
- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`
- `assets/`
- `hyperframes/`
- `renders/`
- `section-previews/`
- `visual-plan/`
- `voiceover/`

## Gate Rule

Do not rush into HyperFrames.

Production starts only after the idea, script, voiceover, and visual plan are strong enough to build.

## Review Rule

When a review creates a reusable lesson, update the project review file first, then promote the lesson into shared memory or future skill memory.
