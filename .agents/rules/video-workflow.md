# Video Workflow Rules

`Why It Works` uses a numbered video lifecycle. As of `2026-06-26`, `packaging` left the numbered
set (it now writes `output/packaging.md` and runs after `caption`), so the numbered main-pipeline
steps shifted up by one for **new** projects. Existing projects keep their original numbers.

As of `2026-06-28`, a new main-pipeline step `visual-implement` runs between `visual-plan` and
`render`. It is **unnumbered** (its deliverable is the project `assets/` library plus a manifest), so
it does NOT renumber any markdown files. `render` keeps `05-production-board.md`.

## Steps (new-project numbering)

0. Topic intake -> `00-topic-intake.md`
1. Research pack -> `01-research-pack.md`
2. Script draft -> `02-script.md`
3. Voiceover -> `03-voiceover.md`
4. Visual plan -> `04-visual-plan.md`
4.5. Visual implement (unnumbered) -> `assets/` + `assets/asset-manifest.md`
5. Render -> `05-production-board.md`
6. Review -> `06-review.md`
7. Upload -> `07-upload.md`
8. Learning -> `08-self-learning.md`

Unnumbered deliverable steps:

- `Visual implement` -> per-scene assets in `assets/` (+ `assets/asset-manifest.md`); runs after `visual-plan`, before `render`
- `Combine` -> `output/<slug>.mp4` (+ `hyperframes/full-video/`)
- `Caption` -> `output/captions/<language>.srt`
- `Packaging` -> `output/packaging.md` (+ `output/thumbnails/`); runs after `caption`
- `Shorts` (side sub-workflow after combine) -> `output/shorts/*.mp4`

Main production chain:

```text
TopicIntake -> ResearchPack -> ScriptDraft -> Voiceover -> VisualPlan -> VisualImplement -> Render -> Review -> Combine -> Caption -> Packaging -> Upload -> Learning
```

`Shorts` branches from `Combine` and does not block caption/packaging/upload/learning.

## Plan / Implement / Render separation (2026-06-28)

The visual pipeline is split into three jobs with clean responsibilities:

- `visual-plan` — **describes** every scene in extreme detail and lists the ASSETS each scene needs
  (type, filename, layout). It does NOT write image-generation prompts and does NOT create images.
- `visual-implement` — **creates the assets**: for each `generate` asset it writes the detailed
  image prompt and generates an isolated element (transparent/plain background); for each `browse`
  asset it finds a license-safe real photo / captures a real screenshot; it reuses any asset already
  produced (by filename) and never recreates it. All assets land in the project `assets/` library.
- `render` — **composites** the mascot + the pre-made assets from `assets/` into each scene's layout
  (HyperFrames). It pulls assets by the filenames the plan specified; it does not re-source images
  unless an asset is genuinely missing (documented fallback).

Rationale: generating a full composed scene per beat makes a recurring character (e.g. the same
person) look different every time. Generating ISOLATED assets once and reusing them by filename keeps
every character identical across scenes.

## File Numbering Rule (legacy-tolerant)

Multiple numbering schemes exist. **Always resolve a step's file by its name SUFFIX, never by a
hard-coded numeric prefix.** For example, find the voiceover index by matching `*-voiceover.md`, the
visual plan by `*-visual-plan.md`, the production board by `*-production-board.md`.

| Step | New project (created on/after 2026-06-26) | Legacy project (created before) |
| --- | --- | --- |
| Voiceover | `03-voiceover.md` | `04-voiceover.md` |
| Visual plan | `04-visual-plan.md` | `05-visual-plan.md` |
| Visual implement | `assets/asset-manifest.md` (unnumbered) | `assets/asset-manifest.md` (unnumbered) |
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
| 4 | `visual-plan` | `04-visual-plan.md` (legacy `05`), `visual-plan/` | voiceover file + selected section voiceover |
| 4.5 | `visual-implement` | `assets/` isolated assets + `assets/asset-manifest.md` | `04-visual-plan.md` + selected section visual plan |
| 5 | `render` | `05-production-board.md` (legacy `06`), `section-previews/`, `hyperframes/`, `renders/` | visual plan + the section's implemented assets in `assets/` |
| 6 | future review skill | `06-review.md` (legacy `07`) | rendered or previewable video sections |
| 6.5 | `combine` | `hyperframes/full-video/` unified preview + `combined-voiceover.mp3`; final video exported to `output/<slug>.mp4` | ALL sections rendered |
| 6.8 | `caption` | `output/captions/<language>.srt` for all 22 languages (+ compatibility `output/captions.srt`, optional `.vtt`) | full combined audio or full video render |
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

Rerunning `visual-plan` for a section makes that section's implemented assets and render stale: rerun
`visual-implement` then `render` for the affected section.

Packaging rule:

Packaging depends only on `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`.
Its recommended position is after `caption`. Rerunning packaging makes only `upload`/`learning`
potentially stale, not earlier production outputs.

## Current Skill Coverage

- Step 0 `Topic intake` -> `.agents/skills/topic-intake/`.
- Step 1 `Research pack` -> `.agents/skills/research-pack/`.
- Step 2 `Script draft` -> `.agents/skills/script-draft/`.
- Step 3 `Voiceover` -> `.agents/skills/voiceover/`.
- Step 4 `Visual plan` -> `.agents/skills/visual-plan/`.
- Step 4.5 `Visual implement` -> `.agents/skills/visual-implement/`.
- Step 5 `Render` -> `.agents/skills/render/`.
- Project-level `Combine` -> `.agents/skills/combine/`.
- Post-combine `Caption` -> `.agents/skills/caption/`.
- Post-caption `Packaging` -> `.agents/skills/packaging/`.
- `Shorts` side sub-workflow -> `.agents/skills/shorts/`.
- The remaining lifecycle steps (review, upload, learning) do not have executable project-local skills yet.

## Section Production Branch

After the voiceover file, production can branch by section.

The `voiceover`, `visual-plan`, `visual-implement`, and `render` skills all follow the same
section-first behavior: ask which section to work on, offer `All` first, then each script section,
and produce separate outputs per selected section.

Per-section voiceover outputs:

```text
projects/<slug>/voiceover/section-XX-kebab-section-name/
```

Per-section visual-plan outputs:

```text
projects/<slug>/visual-plan/section-XX-kebab-section-name/
```

Visual-implement assets (one shared video-level library; assets are named per the plan and reused
across scenes/sections):

```text
projects/<slug>/assets/
projects/<slug>/assets/asset-manifest.md
```

Per-section render preview projects:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/
```

The mascot pose library the plan/implement steps draw from (starting palette; the plan may invent new
poses, which implement then generates and adds back):

```text
.agents/_shared/assets/wit/poses/
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
- `assets/` (incl. `assets/asset-manifest.md` from visual-implement)
- `hyperframes/`
- `renders/`
- `section-previews/`
- `visual-plan/`
- `voiceover/`
- `output/` (final deliverables for upload)

## Gate Rule

Do not rush into HyperFrames.

Production starts only after the idea, script, voiceover, visual plan, and implemented assets are
strong enough to build.

## Review Rule

When a review creates a reusable lesson, update the project review file first, then promote the lesson
into shared memory or future skill memory.
