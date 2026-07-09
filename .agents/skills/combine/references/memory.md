# Combine Skill Memory

Memory for the `combine` skill - assembling all completed section renders of one project into a unified preview on `localhost:1000`.

Use this file for assembly mechanics, HyperFrames mounting/asset-resolution behavior, combined-audio handling, and recurring gotchas. Use `.agents/_shared/` only for channel-wide lessons.

## Current Skill Standard

- Project-level assembly + export step; runs once per project after ALL sections are rendered, before `caption`.
- Require one project (named, smart-selected, or asked). No per-section selection.
- Refuse to run if any script section lacks a rendered build or audio.
- Reuse approved section builds + assets; never re-render, re-time, restyle, or create section CONTENT; never touch the section previews folder (`previews/` new / `section-previews/` legacy) or `hyperframes/review/` section files.
- Section-preview folder convention (changed 2026-06-30): NEW projects = `previews/<N>-kebab-section-name/` (unpadded, e.g. `1-hook`); LEGACY = `section-previews/section-XX-kebab-section-name/`. Resolve a section by checking the new path first, then legacy. Projects `1-`…`5-…ai-slop` are legacy.
- Always port 1000.
- PREVIEW-ONLY BY DEFAULT (changed 2026-06-30, owner Anh Khoa): a plain combine run assembles + verifies the unified preview on `localhost:1000` and STOPS. It does NOT render or export an MP4. Outputs of a default run: `hyperframes/full-video/` + a `05/06-production-board.md` note. Never export on assumption; if unsure whether export is wanted, ask.
- EXPORT ONLY ON EXPLICIT REQUEST: when the user explicitly asks to export ("export", "render the mp4", "export the final video"), render the unified comp to MP4 into `renders/` staging, then MOVE it to `output/<slug>.mp4`. On render failure leave `renders/` untouched. `output/` is the single home for all final deliverables.
- `.gitkeep` RULE (added 2026-06-30): a `.gitkeep` only holds an EMPTY tracked folder. When a folder gains real content, delete its `.gitkeep`. So after moving a real deliverable into `output/`, remove `output/.gitkeep`. Keep/restore `.gitkeep` only in folders with no real content. (`renders/` staging: keep its `.gitkeep` if only the `.gitkeep` remains after the move.)

## Proven Mechanics (from `why-cheap-products-keep-getting-worse`, 2026-06-21)

- Build at `projects/<slug>/hyperframes/full-video/`. `index.html` is the parent and the ONLY root composition; the 8 sections live under `compositions/section-XX.html` (else lint flags `multiple_root_compositions` + duplicate-audio risk).
- Mount sections with `<div class="clip" data-composition-id="mount-sN" data-composition-src="compositions/section-XX.html" data-start=<offset> data-duration=<actual mp3 dur> data-track-index=N>`. Unique track per section avoids same-track overlap lint; `.clip` keeps only the active one visible.
- Parent needs `window.__timelines["<parent id>"] = gsap.timeline({paused:true})` (load GSAP) or lint flags `missing_timeline_registry`. Each host needs `data-composition-id` (else `host_missing_composition_id`).
- ASSET RESOLUTION IS PROJECT-ROOT-RELATIVE: a mounted sub-comp's `./assets/...` and `./*.mp3` resolve against the parent `index.html` location, not the sub-comp's folder. Put consolidated `assets/` and `combined-voiceover.mp3` at `full-video/` ROOT. (First attempt put them under `compositions/` → `audio_src_not_found`; moving to root fixed it.)
- Copy ALL WIT poses from the project `assets/wit/` into `full-video/assets/wit/` - remade sections introduce poses the older mirror's wit folder lacked (e.g. awkward-celebration, confused, money-panic, thinking, betrayed). Missing poses = blank WIT.

## Combined Voiceover

- Strip each section's `<audio>` from its `compositions/section-XX.html`. The "messy / overlapping" voice bug was 8 per-section audios all playing; the fix is one combined track + silent section visuals.
- Concatenate the section mp3s in order with `ffmpeg -f concat -safe 0 -i list -c copy combined-voiceover.mp3` (stream copy preserves exact section boundaries, so each section's voice starts exactly at its mount offset).
- Offsets = cumulative ACTUAL mp3 durations (ffprobe each). Real mp3s run ~0.05s longer than the documented voiceover durations; using documented values drifts ~0.4s by the last section.
- ffmpeg/ffprobe are not on PATH here - install static binaries to temp: `npm.cmd install --prefix %TEMP%/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static`.
- On Linux boxes (no `ffmpeg`/`ffprobe`, no `chromium`, but `google-chrome`/`google-chrome-stable` present): `npm install --prefix <scratchpad>/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static` (the npm postinstall script that fetches the real binary runs even under `allow-scripts` restrictions - verify with `file` that the resulting `ffmpeg`/`ffprobe` paths are real ELF binaries, not JS stubs). The `render` CLI shells out to `ffmpeg`/`ffprobe` by bare name (no path flag), so symlink both into a small `bin/` dir and prepend it to `PATH` for the render command: `ln -sf .../ffmpeg-static/ffmpeg bin/ffmpeg; ln -sf .../ffprobe-static/bin/linux/x64/ffprobe bin/ffprobe; export PATH="bin:$PATH"`. `hyperframes doctor` finds system Chrome automatically - no extra setup needed there.
- If a section's render is later changed, re-copy it (audio-stripped) and refresh assets; only regenerate `combined-voiceover.mp3` + offsets if that section's AUDIO changed (visual/cue-timing edits don't change the audio).

## Self-Check That Caught Real Issues

- `lint` 0 errors; `compositions` shows the unified comp; exactly 1 `<audio>` in index, 0 in sub-comps; parent duration == combined mp3 duration (ffprobe); `snapshot --at` one frame per section shows real bases + WIT (blank = assets didn't resolve at root); server `HTTP 200` on 1000.

## Float Boundary

Watch `data-start + data-duration` overflowing the next offset by ~1e-15 → `overlapping_clips_same_track`. Trim a hundredth of a second when it triggers (e.g. section host or a cue duration `7.38 -> 7.37`).

### 2026-06-22 - The review mirror can lag the live section file - source/refresh from live

Classification: `Operational lesson`

Context:
On `why-everyone-pretends-to-be-busy`, the first combine sourced `hyperframes/review/section-XX.html`
(the mirror). But several sections had later edits (user/linter CSS tweaks; a giant-WIT change that
landed AFTER the first combine) that were not re-synced to the mirror, so the combined video shipped
stale section code. The owner caught it ("use the latest code … previously outdated").

Lesson:
The mirror is only as current as the last sync. Before combining, DIFF each
`section-previews/<section>/index.html` (the live, server-served file = source of truth) against its
`hyperframes/review/section-XX.html`; if any differ, refresh the mirror from live first (or source the
compositions directly from `section-previews`). Then build `compositions/section-XX.html` from the
current file (audio stripped). Cheap one-liner: `diff -q live mirror` per section.

Audio note: if only visuals/WIT/layout changed (no voiceover regenerated), the section mp3 durations
are unchanged - keep the existing `combined-voiceover.mp3` and offsets; only re-copy the compositions
and re-consolidate assets. Regenerate the combined audio only when a section's AUDIO actually changed.

Apply next time:
- diff live vs mirror for all sections at the start of combine; refresh stale mirrors from live
- prefer the live `section-previews` file as the composition source when in doubt
- keep combined audio/offsets if no audio changed; just refresh comps + assets
- watch for zombie `chrome-headless-shell` processes after many snapshots - they exhaust memory and
  make `snapshot` hit "Navigation timeout"; kill them (`Stop-Process`) and retry

Promote to shared memory:
No; combine-skill execution practice.

### 2026-06-30 - Benign render warning + no review mirror (project 5 ai-slop)

Classification: `Operational lesson`

Context:
Combined `5-why-the-internet-is-full-of-ai-slop` (8 sections). There was NO `hyperframes/review/`
mirror at all, so I sourced compositions straight from the live `section-previews/<section>/index.html`
(which is the source of truth anyway - matches the 2026-06-22 mirror-lag lesson). Recipe worked verbatim:
8 mounts, audio stripped, one stream-copy combined mp3 (306.168s), consolidated assets at root
(107/107 resolved). Exported `output/<slug>.mp4` (306.219s, ~82 MB).

Lesson:
During `hyperframes render` of the unified comp, calibration logs a WARNING:
`Sub-composition timelines not registered after 45000ms: mount-s1..mount-sN`. This is BENIGN - the
mount host divs carry no timeline; each inner section registers its own `window.__timelines["Section0XName"]`.
Frames extracted from the final mp4 (ffmpeg `-ss`) confirmed every reveal/animation baked in correctly.
Do not chase this warning. Verify by extracting mp4 frames, not by trusting the warning.

Also: `renders/` may hold a tracked `.gitkeep` - after moving the mp4, `renders/` is NOT empty, so
LEAVE it in place (don't rmdir). The renderer cleans up its own `renders/work-*` scratch folder.

Apply next time:
- if no review mirror exists, source from live `section-previews/<section>/index.html`
- ignore the `Sub-composition timelines not registered` render warning; verify via extracted mp4 frames
- leave `renders/` when it still holds `.gitkeep`

Promote to shared memory:
No; combine-skill execution practice.

### 2026-07-09 - Export render worker count matters on this Linux box (auto-16 stalls, 4 can timeout)

Classification: `Assembly mechanics - render export gotcha`

Context:
Exported the MP4s for `4-why-buy-1-get-1-beats-50-off` (7 sections, 243.5s, 7306 frames) and
`5-why-the-internet-is-full-of-ai-slop` (8 sections, 306.2s, 9186 frames) on the Linux box
(16 cores, 14Gi RAM). Both full-video builds already existed from prior combine runs; this was
export-only.

What broke:
- `hyperframes render` with DEFAULT auto workers picked 16 (one per core) → ~79 Chrome procs, and the
  run STALLED during/after the 45s warmup: log went silent, 0 frames captured after 3+ min. RAM was
  fine (10Gi free), so it's worker/Chrome CONTENTION, not memory. Had to kill and restart.
- `--workers 4` fixed video 4 (captured cleanly, ~20 fps, done in ~7 min). But on the longer video 5,
  4 workers FAILED near ~73% with `Worker 3: Runtime.evaluate timed out` (CDP protocol timeout under
  contention), `RENDER_EXIT=1`, no mp4.
- `--workers 2 --protocol-timeout 600000 --player-ready-timeout 120000` completed video 5 reliably
  (~17 min wall clock). Slower but no stall/timeout.

Lesson / apply next time (EXPORT RECIPE):
- NEVER use default/auto workers for the unified full-video export on this box - it over-subscribes.
- Use `--workers 4` as the default; if a worker hits `Runtime.evaluate timed out` / capture fails,
  retry with `--workers 2 --protocol-timeout 600000 --player-ready-timeout 120000`.
- Run the render fully DETACHED so it survives Claude session teardown: `setsid bash -c '...'`. Two
  gotchas that bit me: (1) a bare `setsid` subshell does NOT inherit the interactive PATH, so node/npx
  are missing (`exit 127`) - export PATH with the nvm node bin dir explicitly
  (`/home/nakmiers/.nvm/versions/node/<ver>/bin`) AND the ffmpeg static `bin/`, and call npx by its
  absolute path. (2) append `echo "RENDER_EXIT=$?"` to the log so a file-watch Monitor can detect
  done/fail without a live parent.
- Track progress by tailing the log (`Capturing frame N/TOTAL`) and detect completion by the mp4
  file existing AND `RENDER_EXIT=0` in the log (the mp4 appears during "Assembling final video" while
  still muxing - wait for the exit code before verifying/moving).
- The render's final summary line shows WALL-CLOCK time (e.g. "17m 0.8s"), NOT video duration - verify
  real duration with ffprobe (video 5 = 306.219s ≈ the 306.168s combined mp3).
- When killing a stalled/failed render, `pgrep -fc <pattern>` counts your OWN command line as a match
  (self-match) - don't trust a non-zero count; check `renders/work-*` is gone and Chrome procs by pid.

Promote to shared memory:
No; combine-skill export execution practice.

### 2026-06-30 - Parent `.clip` CSS leaks into mounted sections (Section 4 HUD went full-screen dark)

Classification: `Assembly mechanics - HIGH IMPACT gotcha`

Context:
On `5-why-the-internet-is-full-of-ai-slop`, Section 4 looked perfect standalone on `localhost:1004`
but in the combined video (`localhost:1000`) the WHOLE section was washed dark and its "THE LOOP" HUD
jumped from top-right to a vertically-centered mid-left blob. Every other section was fine.

Root cause:
The mounted sub-composition's `<style>` and the parent `index.html`'s `<style>` share ONE CSS scope
(HyperFrames does NOT isolate sub-comp styles in a shadow DOM / iframe). The parent declared a BARE
`.clip { position:absolute; inset:0; width:100%; height:100%; }` to lay out the 8 section mount hosts.
Section 4 is the only section whose composition contains a NON-scene element carrying class `clip` -
its persistent loop-ring HUD: `<div id="hud" class="hud clip" ...>`. The parent's `.clip` rule leaked
onto that HUD and stretched it to full-frame (`inset:0; width/height:100%`), turning the HUD's compact
dark pill background (`rgba(8,9,14,0.74)`, `z-index:12`) into a full-screen 74%-dark scrim over the
whole section, and (via `display:flex; align-items:center`) re-centering its text mid-left. Sections
1-3/5-8 only use `clip` on full-frame `.scene` elements, where `.clip`'s rule is harmless, so they
were unaffected.

Fix:
Do NOT use a bare `.clip` style rule in the parent. Give each mount host an extra class (`mount`) and
style THAT: `.mount { position:absolute; inset:0; width:100%; height:100%; }`, hosts become
`class="clip mount"` (keep `clip` for the HyperFrames visibility runtime). The bare `.clip` rule is
gone, so it can never leak onto a section's inner `.hud.clip` (or any future non-scene `.clip`).
Verified: HUD back top-right, darkening gone, lint still 0 errors.

Apply next time (BUILD RECIPE UPDATE):
- the parent `index.html` MUST style mount hosts via a dedicated class (`.mount`), NEVER a bare `.clip`
- mount hosts = `class="clip mount"`
- before trusting a combine, snapshot any section that has a persistent/full-span overlay element
  (HUD, watermark, progress bar) - those are the ones a leaked parent rule will wreck
- remember: sub-comp + parent CSS is ONE scope; any generic selector in the parent hits sub-comp DOM

Promote to shared memory:
No; combine-skill build mechanics.

## Feedback Log

### 2026-06-30 - Combine is PREVIEW-ONLY again; export only on explicit request; `.gitkeep` rule

Classification: `Core workflow change`

Context:
Anh Khoa changed the contract again: `/combine` must NOT render/export an MP4 by default - it only
assembles + verifies the unified preview on `localhost:1000`. Export to `output/<slug>.mp4` happens
ONLY when the user explicitly asks to export. Also a new `.gitkeep` rule: when a folder gains real
content, delete its `.gitkeep` (it only exists to track an empty folder). This partly reverses the
2026-06-22 "combine now always exports" change.

Lesson:
Default combine = preview only (assemble `hyperframes/full-video/`, verify, serve on 1000, write the
board note, stop). Export (render to `renders/` staging -> move to `output/<slug>.mp4`) is gated on an
explicit user request. After moving a real deliverable into a folder, remove that folder's `.gitkeep`;
keep `.gitkeep` only where no real content remains.

Apply next time:
- never auto-render the MP4; if unsure whether export is wanted, ask
- on export: after the move, `rm output/.gitkeep` (folder now has real content); keep `renders/.gitkeep`
  if only the `.gitkeep` remains
- a pre-existing exported MP4 that predates a section fix is STALE/buggy - do not silently ship it

Promote to shared memory:
No; combine-skill execution practice.

### 2026-06-22 - Combine now exports the final MP4 to output/ (reversed the no-export rule)

Classification: `Core workflow change`

Context:
Anh Khoa changed the contract: combine should now export the final video and consolidate ALL deliverables under `projects/<slug>/output/`. The video must render via `renders/` as a staging area (keep `renders/` as-is during the render), then MOVE the result to `output/`; if `renders/` is empty after the move, remove it. This reverses the long-standing "combine is preview-only, never exports MP4/WebM" rule (confirmed by the owner before editing).

Lesson:
Combine = assemble preview (localhost:1000) + export final MP4 to `output/`. Render to `renders/<slug>.mp4` staging, then move (not copy) to `output/<slug>.mp4`, then `rmdir renders/` only if empty. Never delete/move files in `renders/` this run didn't create. On render failure leave `renders/` untouched and report. `output/` is the single deliverables home (shares it with `caption`'s `captions.srt`, future thumbnails, etc.).

Apply next time:
- after preview verify, render the unified comp to MP4 (needs Chrome + ffmpeg; reuse `%TEMP%/wiw-ffmpeg-static`)
- move the result to `output/`; clean up empty `renders/`
- verify exported mp4 exists, non-empty, ffprobe duration ≈ combined mp3 duration
- note the `output/` path in `06-production-board.md`; then stop (caption is the next step)

Promote to shared memory:
No; combine-skill execution practice.

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
