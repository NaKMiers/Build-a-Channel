# Video Workflow Rules

`Why It Works` uses a 10-step video lifecycle.

## Steps

1. Topic intake
2. Research pack
3. Script draft
4. Packaging: title, thumbnail, and YouTube description
5. Voiceover
6. Visual plan
7. HyperFrames build
8. Review
9. Upload
10. Self-learning

## Pipeline Dependency Rule

Skills must run in order: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10`.

Before running step `N`, verify every previous required output exists and is non-empty inside the same `projects/<slug>/` folder.

If a required previous output is missing, stop and tell the user exactly which skill must run first. Do not create placeholder upstream files from a later skill.

Current dependency chain:

| Step | Skill | Output | Required Before Running |
| ---: | --- | --- | --- |
| 1 | `topic-intake` | `00-topic-intake.md` | none |
| 2 | `research-pack` | `01-research-pack.md` | `00-topic-intake.md` |
| 3 | `script-draft` | `02-script.md` | `00-topic-intake.md`, `01-research-pack.md` |
| 4 | `packaging` | `03-packaging.md` and optional `assets/thumbnails/` | `02-script.md` |
| 5 | `voiceover` | `04-voiceover.md` and `voiceover/` | `03-packaging.md` |
| 6 | future visual plan skill | `05-visual-plan.md` | `04-voiceover.md` |
| 7 | future HyperFrames skill | `06-production-board.md`, `hyperframes/`, `renders/` | `05-visual-plan.md` |
| 8 | future review skill | `07-review.md` | rendered or previewable video sections |
| 9 | future upload skill | `08-upload.md` | approved review |
| 10 | future self-learning skill | `09-self-learning.md` | upload or review results |

## Stale Downstream Rule

When a step is created, updated, or rerun, every later step output in the same project becomes stale.

Apply this every time:

- list any downstream files that now need removal or rerun
- do not trust stale downstream files as current source of truth
- do not silently delete downstream files
- remove stale downstream files only when the user explicitly asks for removal
- otherwise rerun downstream skills in order so each step rebuilds from the latest previous output

If an upstream file has a newer modified time than a downstream file, treat the downstream file as stale.

## Current Skill Coverage

- Step 1 `Topic intake` is implemented by `.agents/skills/topic-intake/`.
- Step 2 `Research pack` is implemented by `.agents/skills/research-pack/`.
- Step 3 `Script draft` is implemented by `.agents/skills/script-draft/`.
- Step 4 `Packaging` is implemented by `.agents/skills/packaging/`.
- Step 5 `Voiceover` is implemented by `.agents/skills/voiceover/`.
- The remaining lifecycle steps do not have executable project-local skills yet.

## Section Voiceover Branch

After `03-packaging.md`, production can branch by section.

The `voiceover` skill should ask which script section to generate. It should offer `All` first, then each script section. `All` means generate separate voiceover outputs for every section, not one stitched full-video audio file.

Per-section voiceover outputs belong in:

```text
projects/<slug>/voiceover/section-XX-kebab-section-name/
```

The project-level voiceover index belongs in:

```text
projects/<slug>/04-voiceover.md
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
- `voiceover/`

## Gate Rule

Do not rush into HyperFrames.

Production starts only after the idea, script, packaging, and visual plan are strong enough to build.

## Review Rule

When a review creates a reusable lesson, update the project review file first, then promote the lesson into shared memory or future skill memory.
