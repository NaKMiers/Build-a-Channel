---
name: render
description: Build or update step 6 section HyperFrames previews and optional renders for a Why It Works video project. Use when the user asks for Render, HyperFrames build, create video from visual-plan, build a section preview, run section localhost, start preview servers, render section MP4, or run step 6; requires completed 00-topic-intake.md, 01-research-pack.md, 02-script.md, 04-voiceover.md, 05-visual-plan.md, selected section voiceover, selected section visual plan, explicit project selection, and explicit section selection with All as the first option; creates 06-production-board.md, section-previews/ section HyperFrames projects, hyperframes/ review copies, and optional renders while using port 1000 for unified preview and port 1000 plus section number for section previews.
---

# Render

## Purpose

Run step `6` of the `Why It Works` video workflow.

Use HyperFrames to convert one selected section visual plan into an editable, previewable video section.

This skill is section-first:

```text
Voiceover S1 -> Visual Plan S1 -> Render S1 -> Review S1
Voiceover S2 -> Visual Plan S2 -> Render S2 -> Review S2
...
```

Do not build every section inside one localhost. Each section gets its own HyperFrames preview project and its own port.

## Port Contract

Use these fixed localhost ports:

```text
Unified/final preview: http://localhost:1000
Section 1 preview:     http://localhost:1001
Section 2 preview:     http://localhost:1002
Section 3 preview:     http://localhost:1003
...
Section N preview:     http://localhost:1000 + N
```

Examples:

- `Section 1: Hook` -> `1001`
- `Section 2: Reframe` -> `1002`
- `Section 7: Payoff` -> `1007`

If the required port is occupied by the correct existing preview server, reuse it and document it.
If the required port is occupied by an unrelated process, stop and report the conflict. Do not silently choose a random port.

Port `1000` is reserved for the unified/final preview after sections are approved. Do not use port `1000` for section work.

## Pipeline Position

This is step `6` of the main video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`
- `projects/<slug>/04-voiceover.md`
- `projects/<slug>/05-visual-plan.md`
- selected section voiceover under `projects/<slug>/voiceover/`
- selected section visual plan under `projects/<slug>/visual-plan/`

Packaging is a side branch. Do not require `03-packaging.md` for render unless the selected visual plan explicitly depends on packaging assets.

Write or update:

- `projects/<slug>/06-production-board.md`
- `projects/<slug>/section-previews/section-XX-kebab-section-name/`
- `projects/<slug>/hyperframes/review/section-XX.html`
- `projects/<slug>/hyperframes/index.html` only as the current active mirror when useful
- `projects/<slug>/renders/section-XX-kebab-section-name/` only when rendering an MP4/WebM

When this skill creates, updates, or reruns section preview files, every later output for the affected section becomes stale.

List stale downstream files in chat. Do not silently delete them.

## Required Context

Read these before rendering:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`
9. `.agents/_shared/channel/production-workflow.md`
10. `.agents/_shared/channel/brand-system.md`
11. `.agents/_shared/systems/visual-production.md`
12. `.agents/_shared/systems/audio-feedback-quality.md`
13. `references/memory.md`
14. `references/render-motion-rules.md`
15. `references/output-formats.md` before writing outputs
16. the chosen project files:
    - `02-script.md`
    - `04-voiceover.md`
    - `05-visual-plan.md`

Also read active HyperFrames implementation guidance when available:

- the bundled `hyperframes` skill for composition rules
- the bundled `hyperframes-cli` skill for CLI commands
- existing project `section-previews/` and `hyperframes/` files when updating an existing section

## Project Selection Gate

Always resolve the target project before rendering.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `05-visual-plan.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find render candidates.

A render candidate has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `04-voiceover.md`
- non-empty `05-visual-plan.md`
- at least one section voiceover folder
- at least one section visual-plan folder

When multiple candidates exist or context is unclear, ask the user to choose before writing files.

Do not create a new project folder in this skill.

## Required Inputs Gate

Before section selection or writing files, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`
- non-empty `04-voiceover.md`
- non-empty `05-visual-plan.md`

If `02-script.md` does not contain parsable sections in the form:

```text
## Section N: Section Name
```

stop and ask the user to rerun `script-draft` or fix the script structure first.

If `04-voiceover.md` is missing, empty, or older than `02-script.md`, stop and ask the user to run or rerun `voiceover`.

If `05-visual-plan.md` is missing, empty, or older than `04-voiceover.md`, stop and ask the user to run or rerun `visual-plan`.

## Section Selection Gate

Render must get an explicit target section before writing files.

The target must be selected by the user as `All` or as a specific section number/name in the current request or in the section-choice response.

If no explicit section target is present, ask and stop before file edits, HyperFrames commands, server starts, or renders.

Do not infer the target section from:

- active project state
- latest reviewed section
- next unfinished section
- existing section preview
- missing preview output
- prior chat context

Preferred option order:

1. `All`
2. `Section 1: <name>`
3. `Section 2: <name>`
4. Continue through the section list

Important:

- `All` means build each section as its own preview project and start each on its own section port.
- `All` does not mean one unified preview on port `1000`.
- Unified/final assembly is a separate mode and should run only when the user explicitly asks to unify approved sections.

Fallback selection text:

```markdown
Choose render target:

0. All sections
1. Section 1: <name>
2. Section 2: <name>
   ...
```

## Section Readiness Gate

For each selected section, verify:

- matching section voiceover folder exists under `voiceover/`
- matching section visual-plan folder exists under `visual-plan/`
- section visual-plan file exists and is non-empty
- section voiceover includes an audio file or clearly documented TTS status
- required visual assets or reference prompts are available

If selected section voiceover is stale versus `02-script.md`, stop and ask the user to rerun `voiceover`.

If selected section visual plan is stale versus the section voiceover or `05-visual-plan.md`, stop and ask the user to rerun `visual-plan`.

If assets are missing but can be generated or created safely from the visual plan, create them and document source notes.
If assets are missing and cannot be created safely, stop and report the exact missing assets.

## Request Modes

### Section Preview Build Mode

Default mode.

Create or update:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/
projects/<slug>/section-previews/section-XX-kebab-section-name/index.html
projects/<slug>/section-previews/section-XX-kebab-section-name/DESIGN.md
projects/<slug>/section-previews/section-XX-kebab-section-name/package.json
projects/<slug>/section-previews/section-XX-kebab-section-name/hyperframes.json
projects/<slug>/section-previews/section-XX-kebab-section-name/assets -> junction to ../../assets
projects/<slug>/hyperframes/review/section-XX.html
projects/<slug>/06-production-board.md
```

Start or reuse the section preview server on port `1000 + section number`.

### Section MP4 Render Mode

Use only when the user asks to render/export video, or when review needs an MP4.

Run HyperFrames checks first:

```text
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
```

Then render to:

```text
projects/<slug>/renders/section-XX-kebab-section-name/
```

Use draft quality for iteration unless the user asks for final quality.

### All Sections Mode

Use when the user chooses `All`.

Build each section as a separate section preview project.
Start each selected section on its own port:

```text
Section 1 -> 1001
Section 2 -> 1002
Section 3 -> 1003
```

Do not combine sections into one preview.

### Unified Preview Mode

Use only when the user explicitly asks to unify, assemble, combine, or preview the whole video.

Prerequisites:

- all required section previews exist
- sections intended for assembly are approved or the user explicitly asks for a rough assembly

Use port `1000`.

Do not run unified preview on any section port.

### Improve Memory Mode

Use when the user reviews render/build behavior and gives reusable lessons.

Update in this order:

1. affected project `06-production-board.md` or section implementation notes
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves the whole channel

## HyperFrames Build Rules

Use the active HyperFrames skill guidance.

Core rules:

- HTML is the source of truth.
- Use simple board scenes first.
- Build the static hero frame before animation.
- Wire voiceover audio as a proper `<audio>` clip.
- Use `data-start`, `data-duration`, and `data-track-index` correctly.
- Register GSAP timelines synchronously.
- Keep all motion deterministic.
- Do not use `Math.random()`, `Date.now()`, async timeline construction, or infinite repeats.
- Do not call media `play()`, `pause()`, or `seek()`.
- Do not hide standalone compositions inside `<template>`.
- Do not use real private data, real app logos, or unsafe copyrighted screenshots.

Channel-specific rules:

- Use WIT as the audience surrogate, not a presenter.
- Use real-life assets as evidence, not decoration.
- When the visual plan includes real-world references, inspect those images and source notes before using generated support assets.
- Treat generated images as support or clean production bases unless the visual plan explicitly approves them as the primary asset.
- Use hard cuts by default.
- Use red markup for corrections and punchlines.
- Labels must be readable when paused.
- Cue-critical visuals must be readable on the cue frame.
- Voice sync comes first.

If HyperFrames global guidance conflicts with the current channel rules, preserve the channel's approved simple-board style unless the user explicitly asks for a different render style.

## Voice Sync And Motion Rules

Read `references/render-motion-rules.md` before implementing animation or transitions.

Non-negotiable summary:

- everything on screen must describe the voiceover at that moment
- build a hard-cut timing pass before adding transitions
- choose transitions per scene boundary, not one default effect everywhere
- remove or simplify transitions that damage voice sync
- design every meaningful element's entrance, hold, emphasis, and exit against spoken cues

## Asset Rules

Use one video-level shared asset library:

```text
projects/<slug>/assets/
```

Each section preview project should expose that folder through a local `assets` junction:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/assets
```

Do not copy the full assets folder into each section preview.

On Windows, create a junction only after verifying the target path resolves inside the current project:

```powershell
New-Item -ItemType Junction -Path ".\assets" -Target "..\..\assets"
```

If a local `assets` path already exists:

- if it is the correct junction, keep it
- if it is a wrong junction or copied folder, stop and report it before changing

Document every production asset in:

```text
projects/<slug>/assets/ATTRIBUTION.md
```

Before direct production use, read the selected section's visual reference board and `assets/visual-references/.../source-notes.md` when present.

Use real-image references as follows:

- `safe asset`: may be used directly with required attribution/source notes
- `mockup target`: use as a model for a recreated/cropped/covered asset; do not expose risky source text
- `inspiration only`: inspect for texture/composition, but do not copy into the final render
- `reject`: do not use

If the section has a `real-world/` reference folder, inspect those assets before generating or choosing replacement visuals.

If a real source has attribution, share-alike, logo, private-data, or unclear-copyright risk, either handle the requirement in `ATTRIBUTION.md` or use a generated/self-made replacement that preserves the real-world texture without copying unsafe material.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Parse `02-script.md` sections.
4. Run the Section Selection Gate.
5. Run the Section Readiness Gate for selected sections.
6. Read required shared context, skill memory, output formats, and HyperFrames guidance.
7. For each selected section:
   - compute the fixed port: `1000 + section number`
   - create or update the section preview project
   - create or verify the local `assets` junction
   - create a voice cue map from the section voiceover and visual plan
   - implement `index.html` from the section visual plan
   - wire selected voiceover audio
   - implement a hard-cut timing pass first
   - add per-boundary transitions only after voice sync is working
   - design element entrances, holds, emphasis, and exits against spoken cues
   - create or update `DESIGN.md`
   - create or update `package.json` and `hyperframes.json`
   - copy or mirror the canonical standalone section into `hyperframes/review/section-XX.html`
   - run `lint`, `validate`, and `inspect`
   - fix blocking issues
   - start or reuse the preview server on the fixed section port
   - record Studio and direct composition URLs
8. Write or update `projects/<slug>/06-production-board.md`.
9. Run the Downstream Stale Gate.
10. Respond with the Chat Response Format.
11. Stop before review, upload, or learning unless explicitly asked.

## Server Rules

Preview servers are long-running processes.

When starting a server on Windows, use a hidden background process and keep it alive:

```powershell
Start-Process -WindowStyle Hidden -FilePath "powershell" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"Set-Location '<section-preview-dir>'; npx --yes hyperframes@<version> preview --port <port> *> preview.log`""
```

Use the HyperFrames version already used by the project when present. If no project precedent exists, use the currently available HyperFrames CLI and record the version.

After starting, verify the server responds and report:

```text
http://localhost:<port>/#project/<section-preview-folder-name>
http://localhost:<port>/api/projects/<section-preview-folder-name>/preview/comp/index.html
```

Do not leave an interactive foreground server blocking the turn.

## Output Formats

Use `references/output-formats.md` for:

- `06-production-board.md`
- section implementation notes
- chat response

## Downstream Stale Gate

After creating, updating, or rerunning a section preview, check for downstream files:

- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`
- unified preview/render files when they exist

If any exist for the affected section or full video, list them as stale in chat.

Do not delete downstream files unless the user explicitly asks.

## Quality Bar

A section render is ready for review when:

- the selected section was explicitly chosen
- section voiceover and visual plan are current
- section preview project exists separately from other sections
- section uses fixed port `1000 + section number`
- `index.html` implements the visual plan without requiring review to infer missing boards
- audio is wired and synchronized to visual cues
- every visible scene and element matches the current voiceover beat
- transitions are chosen per boundary and do not damage voice sync
- key labels enter/emphasize on the spoken word they support
- `lint`, `validate`, and `inspect` pass, or remaining warnings are documented and non-blocking
- labels are readable
- WIT emotion is visible and useful
- assets are referenced through the shared project asset library
- source notes and attribution are updated
- `06-production-board.md` records paths, commands, checks, and URLs
- preview server is running or a clear failure reason is reported

## Hard Fails

Reject or stop before finishing if:

- the project lacks `05-visual-plan.md`
- the selected section lacks voiceover
- the selected section lacks visual plan
- the user has not explicitly selected `All` or a specific section
- the target section is inferred instead of selected
- scene content does not match the current voiceover beat
- transitions are added before hard-cut timing works
- the same transition effect is applied everywhere without per-boundary reasoning
- emphasized spoken words have no visual emphasis when the section depends on that cue
- the section preview tries to share one localhost with all sections
- a section uses port `1000`
- a section uses a random fallback port without explicit user approval
- unified preview is built when the user only asked for a section
- assets are copied into each section instead of linked/junctioned without a reason
- HyperFrames checks fail with blocking errors
- the preview server is claimed running without verification
- generated or browsed assets are used without source notes
- the skill creates review, upload, or learning files

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- a port rule changes
- HyperFrames CLI commands or versions change
- section preview structure changes
- a render later fails review because of sync, labels, WIT, assets, or server setup
- a transition choice causes voiceover mismatch
- a repeated animation pattern makes the video feel boring or disconnected from narration
- the user approves or rejects a build pattern

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify promoted lessons as `Core`, `Experiment`, `Operational lesson`, or `Reject`.
