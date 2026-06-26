# Video Workflow Rules

`Why It Works` uses a numbered video lifecycle. As of `2026-06-26`, `packaging` left the numbered
set (it now writes `output/packaging.md` and runs after `caption`), so the numbered main-pipeline
steps shifted up by one for **new** projects. Existing projects keep their original numbers.

## Steps (new-project numbering)

0. Topic intake -> `00-topic-intake.md`
1. Research pack -> `01-research-pack.md`
2. Script draft -> `02-script.md`
3. Voiceover -> `03-voiceover.md`
4. Visual plan -> `04-visual-plan.md`
5. Render -> `05-production-board.md`
6. Review -> `06-review.md`
7. Upload -> `07-upload.md`
8. Learning -> `08-self-learning.md`

Unnumbered deliverable steps (write into `output/`):

- `Combine` -> `output/<slug>.mp4` (+ `hyperframes/full-video/`)
- `Caption` -> `output/captions/<language>.srt`
- `Packaging` -> `output/packaging.md` (+ `output/thumbnails/`); runs after `caption`
- `Shorts` (side sub-workflow after combine) -> `output/shorts/*.mp4`

Main production chain:

```text
TopicIntake -> ResearchPack -> ScriptDraft -> Voiceover -> VisualPlan -> Render -> Review -> Combine -> Caption -> Packaging -> Upload -> Learning
```

`Shorts` branches from `Combine` and does not block caption/packaging/upload/learning.

## File Numbering Rule (legacy-tolerant)

Two numbering schemes exist. **Always resolve a step's file by its name SUFFIX, never by a hard-coded
numeric prefix.** For example, find the voiceover index by matching `*-voiceover.md`, the visual plan
by `*-visual-plan.md`, the production board by `*-production-board.md`.

| Step | New project (created on/after 2026-06-26) | Legacy project (created before) |
| --- | --- | --- |
| Voiceover | `03-voiceover.md` | `04-voiceover.md` |
| Visual plan | `04-visual-plan.md` | `05-visual-plan.md` |
| Render board | `05-production-board.md` | `06-production-board.md` |
| Review | `06-review.md` | `07-review.md` |
| Upload | `07-upload.md` | `08-upload.md` |
| Learning | `08-self-learning.md` | `09-self-learning.md` |
| Packaging | `output/packaging.md` (unnumbered) | legacy `03-packaging.md` may still exist |

A writer skill creates the **new** number when starting a fresh file, but writes back to whatever
suffix-matched file already exists (so it never duplicates a legacy file under a new number). Do not
renumber files in existing projects unless the user explicitly asks. The project template
(`projects/_template/`) ships the new numbering, so new projects start correct automatically.

## Pipeline Dependency Rule

Skills must run in workflow order. Before running a step, verify every required previous output exists
and is non-empty inside the same `projects/<slug>/` folder (resolved by suffix per the rule above).

If a required previous output is missing, stop and tell the user exactly which skill must run first.
Do not create placeholder upstream files from a later skill.

Current dependency chain (new-project numbers; legacy in parentheses):

| Step | Skill | Output | Required Before Running |
| ---: | --- | --- | --- |
| 0 | `topic-intake` | `00-topic-intake.md` | none |
| 1 | `research-pack` | `01-research-pack.md` | `00-topic-intake.md` |
| 2 | `script-draft` | `02-script.md` | `00-topic-intake.md`, `01-research-pack.md` |
| 3 | `voiceover` | `03-voiceover.md` (legacy `04`) + `voiceover/` | `02-script.md` |
| 4 | `visual-plan` | `04-visual-plan.md` (legacy `05`), `visual-plan/`, optional `assets/visual-references/` | voiceover file + selected section voiceover |
| 5 | `render` | `05-production-board.md` (legacy `06`), `section-previews/`, `hyperframes/`, `renders/` | visual-plan file + selected section visual plan |
| 6 | future review skill | `06-review.md` (legacy `07`) | rendered or previewable video sections |
| 6.5 | `combine` | `hyperframes/full-video/` unified preview + `combined-voiceover.mp3`; final video exported to `output/<slug>.mp4` (via `renders/` staging, then moved; `renders/` removed if empty) | ALL sections rendered |
| 6.8 | `caption` | `output/captions/<language>.srt` for all 22 languages (+ compatibility `output/captions.srt`, optional `.vtt`), `voiceover/combined-word-timings.json` + `_segments.json` | full combined audio or full video render |
| 6.9 | `packaging` | `output/packaging.md` + `output/thumbnails/` | `00-topic-intake.md`, `01-research-pack.md`, `02-script.md` (recommended after caption) |
| 7 | future upload skill | `07-upload.md` (legacy `08`) | approved review, captions, packaging |
| 8 | future learning skill | `08-self-learning.md` (legacy `09`) | upload or review results |

## Stale Downstream Rule

When a step is created, updated, or rerun, every later step output in the same project becomes stale.

Apply this every time:

- list any downstream files that now need removal or rerun
- do not trust stale downstream files as current source of truth
- do not silently delete downstream files
- remove stale downstream files only when the user explicitly asks for removal
- otherwise rerun downstream skills in order so each step rebuilds from the latest previous output

If an upstream file has a newer modified time than a downstream file, treat the downstream file as stale.

Packaging rule:

Packaging depends only on `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`.
Its recommended position is after `caption` so the finished video, real chapters, and any built shorts
are available. Rerunning packaging makes only `upload`/`learning` potentially stale, not earlier
production outputs.

## Current Skill Coverage

- Step 0 `Topic intake` -> `.agents/skills/topic-intake/`.
- Step 1 `Research pack` -> `.agents/skills/research-pack/`.
- Step 2 `Script draft` -> `.agents/skills/script-draft/`.
- Step 3 `Voiceover` -> `.agents/skills/voiceover/`.
- Step 4 `Visual plan` -> `.agents/skills/visual-plan/`.
- Step 5 `Render` -> `.agents/skills/render/`.
- Project-level `Combine` -> `.agents/skills/combine/`.
- Post-combine `Caption` -> `.agents/skills/caption/`; derives timing once from the full combined audio and exports all 22 languages as `output/captions/<language>.srt` (plus a compatibility `output/captions.srt`).
- Post-caption `Packaging` -> `.agents/skills/packaging/`; writes `output/packaging.md` + `output/thumbnails/`.
- `Shorts` side sub-workflow -> `.agents/skills/shorts/`.
- The remaining lifecycle steps (review, upload, learning) do not have executable project-local skills yet.

## Section Production Branch

After the voiceover file, production can branch by section.

The `voiceover` skill should ask which script section to generate. It should offer `All` first, then
each script section. `All` means generate separate voiceover outputs for every section, not one
stitched full-video audio file.

The `visual-plan` skill should follow the same section-first behavior after the voiceover file. It
should ask which section to plan, offer `All` first, and create separate visual-plan outputs for every
selected section.

The `render` skill should follow the same section-first behavior after the visual-plan file. It should
ask which section to build, offer `All` first, and create separate HyperFrames preview projects for
every selected section.

Per-section voiceover outputs belong in:

```text
projects/<slug>/voiceover/section-XX-kebab-section-name/
```

The project-level voiceover index belongs in (new projects):

```text
projects/<slug>/03-voiceover.md
```

Per-section visual-plan outputs belong in:

```text
projects/<slug>/visual-plan/section-XX-kebab-section-name/
```

The project-level visual-plan index belongs in (new projects):

```text
projects/<slug>/04-visual-plan.md
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

Each new video starts from `projects/_template/` and produces:

- `00-topic-intake.md`
- `01-research-pack.md`
- `02-script.md`
- `03-voiceover.md`
- `04-visual-plan.md`
- `05-production-board.md`
- `06-review.md`
- `07-upload.md`
- `08-self-learning.md`
- `assets/`
- `hyperframes/`
- `renders/`
- `section-previews/`
- `visual-plan/`
- `voiceover/`
- `output/` (final deliverables for upload: the final `.mp4`, `captions/<language>.srt` for all 22 languages, `packaging.md`, and `thumbnails/`)

## Gate Rule

Do not rush into HyperFrames.

Production starts only after the idea, script, voiceover, and visual plan are strong enough to build.

## Review Rule

When a review creates a reusable lesson, update the project review file first, then promote the lesson
into shared memory or future skill memory.
