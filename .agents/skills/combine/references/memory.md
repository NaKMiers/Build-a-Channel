# Combine Skill Memory

Memory for the `combine` skill — assembling all completed section renders of one project into a unified preview on `localhost:1000`.

Use this file for assembly mechanics, HyperFrames mounting/asset-resolution behavior, combined-audio handling, and recurring gotchas. Use `.agents/_shared/` only for channel-wide lessons.

## Current Skill Standard

- Final workflow step; runs once per project after ALL sections are rendered.
- Require one project (named, smart-selected, or asked). No per-section selection.
- Refuse to run if any script section lacks a rendered build or audio.
- Assembly-only: reuse approved section builds + assets; never re-render, re-time, restyle, or create section content; never touch `section-previews/` or `hyperframes/review/` section files.
- No MP4/WebM export. Preview only.
- Always port 1000.
- Output only `hyperframes/full-video/` + a `06-production-board.md` note.

## Proven Mechanics (from `why-cheap-products-keep-getting-worse`, 2026-06-21)

- Build at `projects/<slug>/hyperframes/full-video/`. `index.html` is the parent and the ONLY root composition; the 8 sections live under `compositions/section-XX.html` (else lint flags `multiple_root_compositions` + duplicate-audio risk).
- Mount sections with `<div class="clip" data-composition-id="mount-sN" data-composition-src="compositions/section-XX.html" data-start=<offset> data-duration=<actual mp3 dur> data-track-index=N>`. Unique track per section avoids same-track overlap lint; `.clip` keeps only the active one visible.
- Parent needs `window.__timelines["<parent id>"] = gsap.timeline({paused:true})` (load GSAP) or lint flags `missing_timeline_registry`. Each host needs `data-composition-id` (else `host_missing_composition_id`).
- ASSET RESOLUTION IS PROJECT-ROOT-RELATIVE: a mounted sub-comp's `./assets/...` and `./*.mp3` resolve against the parent `index.html` location, not the sub-comp's folder. Put consolidated `assets/` and `combined-voiceover.mp3` at `full-video/` ROOT. (First attempt put them under `compositions/` → `audio_src_not_found`; moving to root fixed it.)
- Copy ALL WIT poses from the project `assets/wit/` into `full-video/assets/wit/` — remade sections introduce poses the older mirror's wit folder lacked (e.g. awkward-celebration, confused, money-panic, thinking, betrayed). Missing poses = blank WIT.

## Combined Voiceover

- Strip each section's `<audio>` from its `compositions/section-XX.html`. The "messy / overlapping" voice bug was 8 per-section audios all playing; the fix is one combined track + silent section visuals.
- Concatenate the section mp3s in order with `ffmpeg -f concat -safe 0 -i list -c copy combined-voiceover.mp3` (stream copy preserves exact section boundaries, so each section's voice starts exactly at its mount offset).
- Offsets = cumulative ACTUAL mp3 durations (ffprobe each). Real mp3s run ~0.05s longer than the documented voiceover durations; using documented values drifts ~0.4s by the last section.
- ffmpeg/ffprobe are not on PATH here — install static binaries to temp: `npm.cmd install --prefix %TEMP%/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static`.
- If a section's render is later changed, re-copy it (audio-stripped) and refresh assets; only regenerate `combined-voiceover.mp3` + offsets if that section's AUDIO changed (visual/cue-timing edits don't change the audio).

## Self-Check That Caught Real Issues

- `lint` 0 errors; `compositions` shows the unified comp; exactly 1 `<audio>` in index, 0 in sub-comps; parent duration == combined mp3 duration (ffprobe); `snapshot --at` one frame per section shows real bases + WIT (blank = assets didn't resolve at root); server `HTTP 200` on 1000.

## Float Boundary

Watch `data-start + data-duration` overflowing the next offset by ~1e-15 → `overlapping_clips_same_track`. Trim a hundredth of a second when it triggers (e.g. section host or a cue duration `7.38 -> 7.37`).

## Feedback Log

### 2026-06-21 - Skill Created From The Unified Full-Video Build

Classification: `Operational lesson`

Context:
Anh Khoa asked for a `Combine` skill codifying the unified full-video assembly: combine all completed sections into one render on `localhost:1000`, reuse existing section results/assets (create nothing new, change no section), no MP4 export, run only when all sections are complete, require a project but smart-select by context.

Lesson:
Combine is the final, project-level, assembly-only step. The reliable recipe is: copy approved section builds into `compositions/` (audio stripped), one combined voiceover (ffmpeg stream-copy concat) at root, mount each section at cumulative ACTUAL-duration offsets on its own track with `.clip` + `data-composition-id`, register an empty parent timeline, and put all assets + the combined mp3 at the project root because mounted sub-comps resolve relative paths from the root. Verify 1 audio / 0 in sub-comps / duration match / per-section snapshot / lint 0 / port 1000.

Apply next time:
- gate on every script section having a rendered build + audio
- never modify section sources; only assemble
- never export video
- reserve port 1000

Promote to shared memory:
No; this is combine-skill execution practice.
