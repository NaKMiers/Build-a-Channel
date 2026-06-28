---
name: combine
description: Project-level assembly + export step. Combine all completed section renders of one Why It Works video project into a single unified HyperFrames preview on localhost:1000 with one continuous combined voiceover, then export the final full video (MP4) to the project's output/ folder. Use when the user asks to combine, combine sections, unify, assemble the full video, build the full render, merge sections into one video, make the whole video, export the final video, or run on localhost:1000. Requires every section already rendered (one preview per script section); refuses to run if any section is missing. Reuses the existing per-section renders and assets and only assembles them - it never re-renders, edits, or creates section content. The final video is rendered through renders/ as a staging area, then moved to output/, and renders/ is removed if it is left empty. Requires one project; use the project the user names, or smart-select the unambiguous active project, otherwise ask.
---

# Combine

## Purpose

Run the project-level assembly + export step of the `Why It Works` video workflow: stitch every completed section render of ONE project into a single continuous video on `localhost:1000`, played with ONE combined voiceover instead of each section's separate audio, then export that unified video to a final MP4 in the project's `output/` folder.

This skill reuses the approved per-section renders and their assets and combines them. It must not re-render, re-time, restyle, or otherwise change any section content. The only new artifact it produces beyond the unified preview is the final exported video, which is rendered via a `renders/` staging area and then moved into `output/` (see Final Video Export).

## Pipeline Position

This runs once per project (not per section), after every section is reviewed and before `caption`:

```text
... -> render -> review   (repeat per section)
-> combine   (once, after ALL sections are done: assemble preview + export final MP4 to output/)
-> caption -> upload -> learning
```

Combine writes:

- `projects/<slug>/hyperframes/full-video/` (the unified project: `index.html`, `compositions/section-XX.html`, consolidated `assets/`, `combined-voiceover.mp3`, `package.json`, `hyperframes.json`)
- `projects/<slug>/output/<slug>.mp4` (the final exported video - the deliverable)
- a status note in `projects/<slug>/05-production-board.md`

`renders/` is used only as a temporary staging area for the export and is removed if it ends up empty (see Final Video Export). `output/` is the single home for all final deliverables (final video, and later `caption`'s `captions.srt`, etc.).

Combine does NOT create or modify: `section-previews/`, `hyperframes/review/`, `02-script.md`, `03-voiceover.md`, `04-visual-plan.md`, any section `index.html`, or any voiceover audio. It only reads them.

## Port Contract

The unified preview always runs on `localhost:1000` (the reserved unified/final port). Section ports `1000 + N` are never touched by this skill.

If `1000` is occupied by the existing unified server, restart it. If occupied by an unrelated process, stop and report the conflict.

## Input Contract

Require exactly one project.

Project resolution order:

1. Use the project slug/path named by the user.
2. Use the active project only when the current chat context is unambiguous and the folder exists.
3. If exactly one project under `projects/` (excluding `_template`) has all sections rendered, smart-select it and say so.
4. Otherwise ask the user which project to combine before building.

There is no per-section selection and no `All` prompt - Combine always assembles every section of the chosen project.

## Hard Precondition: All Sections Completed

Combine only runs when every section is finished.

1. Parse `02-script.md` for sections (`## Section N: Name`). This is the required section set.
2. For each section, require a current rendered build: `projects/<slug>/section-previews/section-XX-*/index.html` (or the surviving mirror `projects/<slug>/hyperframes/review/section-XX.html`).
3. For each section, require its voiceover audio (`voiceover/section-XX-*/scratch-audio/*.mp3`, or the mirror's section mp3).

If any section has no rendered build or no audio, STOP and list the missing sections. Tell the user to finish those sections (render) first. Do not assemble a partial video unless the user explicitly asks for a rough partial assembly.

## Required Context

Read before assembling:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `references/memory.md`
6. the chosen project's `02-script.md`, `03-voiceover.md`, and `05-production-board.md`
7. the surviving section builds under `hyperframes/review/section-XX.html` (preferred source - the approved mirror) and/or `section-previews/section-XX-*/index.html`

## What Combine Reuses (never creates)

- section composition HTML: copied verbatim from the approved per-section builds, with only the per-section `<audio>` element removed
- section assets (photos, WIT poses, fonts): copied from the existing project/section assets
- section voiceover mp3s: concatenated into one combined track
- nothing is drawn, generated, re-timed, or restyled

## Build Mechanics (the proven recipe)

Build under `projects/<slug>/hyperframes/full-video/`.

### 1. Source the approved section builds

Use `hyperframes/review/section-XX.html` as the source when present (the approved mirror); else `section-previews/section-XX-*/index.html`. Copy each into `full-video/compositions/section-XX.html`.

### 2. Strip per-section audio

Remove the per-section `<audio>` element from each `compositions/section-XX.html` (e.g. delete the line matching `<audio ... voiceover-section ...>`). The sections become silent visuals; the unified composition carries one combined audio. (This is the fix for "messy / overlapping" audio.)

### 3. One combined voiceover

Measure each section mp3's ACTUAL duration with `ffprobe` (the real mp3 runs slightly longer than the documented voiceover duration - using documented values drifts ~0.4s by the last section). Concatenate the section mp3s in section order with `ffmpeg` using the concat demuxer and stream copy (preserves exact boundaries):

```bash
# write concat-list.txt: one `file '<section mp3>'` line per section, in order
ffmpeg -y -f concat -safe 0 -i concat-list.txt -c copy combined-voiceover.mp3
```

Save `combined-voiceover.mp3` at the `full-video/` root. ffprobe it for the total duration.

ffmpeg/ffprobe on this Windows box are not on PATH - install static binaries once and reference them directly:
`npm.cmd install --prefix %TEMP%/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static` → `ffmpeg-static/ffmpeg.exe`, `ffprobe-static/bin/win32/x64/ffprobe.exe`.

### 4. Parent composition (`full-video/index.html`)

- root `<div id="..." data-composition-id="UnifiedWhyCheap..." data-start="0" data-duration="<total>" data-width="1920" data-height="1080">`
- one host clip per section: `<div class="clip" data-composition-id="mount-sN" data-composition-src="compositions/section-XX.html" data-start="<cumulative offset>" data-duration="<that section's actual mp3 duration>" data-track-index="N">`
  - offsets are the cumulative sum of ACTUAL section mp3 durations (first = 0)
  - give each host its OWN `data-track-index` (1..N) so the lint never flags same-track overlap, and `class="clip"` so only the active section shows
  - each host needs a unique `data-composition-id`
- one `<audio id="voiceover-full" data-start="0" data-duration="<total>" data-track-index="10" data-volume="1" src="./combined-voiceover.mp3">`
- load GSAP and register an empty paused timeline for the parent: `window.__timelines["<parent id>"] = gsap.timeline({ paused: true });`
- watch floating-point boundaries (e.g. `a+b` overflowing the next offset); trim a hundredth if lint reports `overlapping_clips_same_track`.

### 5. Assets resolve at the PROJECT ROOT

Mounted sub-compositions resolve their relative `./assets/...` and `./*.mp3` paths against the project root (the `index.html` location), NOT their own `compositions/` folder. So put the consolidated `assets/` (all sections' `section-XX/` image folders + `fonts/` + every used WIT pose under `wit/`) at `full-video/` root, and the `combined-voiceover.mp3` at root too. Copy WIT poses from the project `assets/wit/` so all sections' poses are present.

### 6. Project files

- `full-video/package.json` with `"dev": "npx --yes hyperframes@<ver> preview --port 1000"`
- `full-video/hyperframes.json` (standard paths block)
- `index.html` must be the only root-level composition (sub-comps live under `compositions/`), or the linter flags `multiple_root_compositions` / duplicate audio.

## Final Video Export

After the unified preview is built and verified, export the full video to MP4 and place the deliverable in `output/`.

Destination rule: the FINAL video lives in `projects/<slug>/output/`. `renders/` is only a temporary staging area for the render tool's raw output. Never leave the final deliverable in `renders/`.

Procedure:

1. Render the unified composition (`hyperframes/full-video/index.html`) to MP4 with the HyperFrames renderer, writing into the project's `renders/` folder as staging (keep `renders/` exactly as-is during the render - do not pre-clean or move anything mid-render):
   ```bash
   npx --yes hyperframes@<ver> render <full-video composition> --output projects/<slug>/renders/<slug>.mp4
   ```
   HyperFrames render needs Chrome + ffmpeg. ffmpeg/ffprobe are not on PATH here - reuse the static binaries (`%TEMP%/wiw-ffmpeg-static/...`) or `hyperframes browser` / `doctor` to provision Chrome.
2. Only AFTER the render finishes successfully, MOVE the resulting video file from `renders/` to `projects/<slug>/output/<slug>.mp4` (create `output/` if missing). Do not copy-and-leave; move it.
3. After the move, if `renders/` is now empty, remove the `renders/` directory. If `renders/` still contains other files (e.g. earlier section renders the user kept), leave it in place and only report what was moved.
4. Never delete or move anything from `renders/` other than the video this run produced. If the render fails, leave `renders/` untouched and report the failure - do not move a partial file and do not delete the folder.

WebM: only if the user explicitly asks; same staging → move → cleanup flow, with the `.webm` landing in `output/`.

## Workflow

1. Resolve exactly one project (Input Contract).
2. Run the All-Sections-Completed precondition; stop and list any missing section.
3. Read required context and the approved section builds.
4. Create/refresh `hyperframes/full-video/`:
   - copy each approved section build to `compositions/section-XX.html` and strip its `<audio>`
   - ffprobe each section mp3; compute cumulative offsets and total
   - concatenate the section mp3s (stream copy) to `combined-voiceover.mp3`
   - write `index.html` (mounts + single combined audio + timeline registry), `package.json`, `hyperframes.json`
   - consolidate `assets/` (section image folders + fonts + all WIT poses) and the combined mp3 at the project root
5. Verify the preview (Self-Check below).
6. Start/restart the preview server on port 1000; confirm `HTTP 200`.
7. Export the final video (Final Video Export): render to `renders/` staging, move the result to `output/<slug>.mp4`, then remove `renders/` if it is left empty.
8. Write the status note in `05-production-board.md` (note the `output/` deliverable path).
9. Respond with the Combine report, including the exported `output/` path. Do not continue into caption, upload, or learning.

## Self-Check (must pass before handoff)

- `hyperframes lint` on `full-video/`: 0 errors.
- `hyperframes compositions` lists the unified composition with N section elements + 1 audio.
- exactly ONE `<audio>` in `index.html`; ZERO `<audio>` across `compositions/*.html`.
- parent `data-duration` == combined mp3 duration (ffprobe).
- `hyperframes snapshot --at <one timestamp inside each section>`: every section renders at its offset with its real bases, WIT, and labels (assets resolve).
- server answers on `localhost:1000`.
- final video exported: `projects/<slug>/output/<slug>.mp4` exists, is non-empty, and ffprobe duration ≈ combined mp3 duration.
- `renders/` no longer holds this run's video (it was moved, not copied); if `renders/` is empty it was removed, otherwise it was left intact.

If a section renders blank in the snapshot, its assets did not resolve - confirm the consolidated `assets/` and the section's image folder are at the project root.

## Hard Fails

Stop and report if:

- no project is named and none can be unambiguously smart-selected
- any section is missing a rendered build or audio (assemble nothing partial without explicit approval)
- the skill would modify a section preview, review mirror, script, voiceover, or any section content (Combine only assembles + exports; it never changes section content)
- the final render fails (leave `renders/` untouched, do not move a partial file, do not delete the folder, report the failure)
- moving the export would overwrite an unrelated existing file in `output/` without the user's intent, or `renders/` cleanup would remove files this run did not create
- port 1000 is held by an unrelated process
- lint shows blocking errors, more than one audio clip survives, or a section renders blank and the cause cannot be fixed by re-consolidating assets at the root

## Self-Improvement

Read `references/memory.md` every run. Update it when:

- the HyperFrames mounting/asset-resolution behavior changes
- a section structure breaks the assembly (e.g. new asset path scheme)
- the combined-audio or offset math needs sharper handling

Do not promote to `.agents/_shared/` unless the lesson is channel-wide. Never rewrite section content from a combine run.
