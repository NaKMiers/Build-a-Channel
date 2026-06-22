---
name: caption
description: Post-combine workflow step. Create accurate YouTube subtitle/caption files (.srt) for one Why It Works video project by transcribing the FULL combined audio (or full video render) and aligning the exact script text to real word-level timestamps. Use when the user asks to create captions, subtitles, an SRT/VTT file, closed captions, caption the video, or generate subtitles for upload. Requires a full combined voiceover (`hyperframes/full-video/combined-voiceover.mp3`) or a full video render — refuses to run on per-section audio only. Requires one project; use the project the user names, or smart-select the unambiguous active project, otherwise ask. Exports to `projects/<slug>/output/`.
---

# Caption

## Purpose

Produce subtitle/caption files for ONE finished `Why It Works` video that match the spoken audio **100%**, then export them to the project's `output/` folder for YouTube upload.

The non-negotiable requirement: **captions must not drift from the voice.** Timing comes from the real audio (word-level transcription), and the displayed text comes from the project script (ground truth), so wording is exact and timing matches what is actually said.

Never estimate caption timing from word counts or documented durations. Always transcribe the real combined audio.

## Pipeline Position

This runs once per project, AFTER `combine`, BEFORE `upload`:

```text
... -> render -> auto-adjust -> review   (repeat per section)
-> combine   (once: builds the unified full-video + combined-voiceover.mp3)
-> caption   (once: subtitles from the full audio, exported to output/)
-> upload -> learning
```

Caption depends on `combine` because it needs ONE continuous full-length audio (or a full video render) on a single timeline. Per-section audio cannot produce a correctly-offset full-video SRT.

## Input Contract

Require exactly one project.

Project resolution order:

1. Use the project slug/path named by the user.
2. Use the active project only when the current chat context is unambiguous and the folder exists.
3. If exactly one project under `projects/` (excluding `_template`) has a full combined audio or full video render, smart-select it and say so.
4. Otherwise ask the user which project to caption.

## Hard Precondition: A Full-Length Audio Source Exists

Caption only runs when a single full-length audio/video source exists. In priority order:

1. `projects/<slug>/hyperframes/full-video/combined-voiceover.mp3` (preferred — the combine output).
2. A full video render (`renders/*.mp4` / `*.webm`) covering the whole video — extract its audio track.
3. Any other single continuous full-length audio the user points to.

If only per-section audio exists (`voiceover/section-XX-*/scratch-audio/*.mp3`), STOP and tell the user to run `combine` first (or point to a full render). Do not stitch a full SRT from separate section files in this skill — combine owns audio assembly.

## Required Context

Read before building:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `references/memory.md`
6. the chosen project's `02-script.md` (the source of the exact caption TEXT)
7. confirm the audio source from the precondition above

## Method (the proven recipe)

The technique that produced the verified `why-cheap-products-keep-getting-worse` captions:

### 1. Decode the full audio to PCM

Whisper needs raw mono 16 kHz float samples. Use ffmpeg:

```bash
ffmpeg -y -i <full-audio> -ar 16000 -ac 1 -f f32le out.raw
```

ffmpeg/ffprobe are not on PATH on this Windows box. Install static binaries once and reference them directly, or reuse the existing ones:

- `npm.cmd install --prefix %TEMP%/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static`
- existing path observed: `%TEMP%/wiw-ffmpeg-static/node_modules/ffmpeg-static/ffmpeg.exe`
- CapCut also ships an `ffmpeg.exe` under `AppData/Local/CapCut/Apps/<ver>/`.

### 2. Word-level transcription with Whisper (Transformers.js)

Run `Xenova/whisper-tiny.en` via `@xenova/transformers` with `return_timestamps: "word"` over the FULL audio in one pass, so timestamps land on the final video timeline (no per-section offset math, no drift). The reusable script is `references/transcribe-combined.mjs`.

A working setup with the model already cached exists at `%TEMP%/wiw-whisper/` (`node_modules/@xenova/transformers` + cached `whisper-tiny.en`). Reuse it when present; otherwise `npm install @xenova/transformers` in a temp dir (first run downloads the ~tiny model).

Output a JSON `{ text, words:[{word,start,end}] }`. Save it to `projects/<slug>/voiceover/combined-word-timings.json` so it can be reused.

### 3. Align exact script text to real timestamps

Whisper transcription is close but not authoritative for wording (it may write `$9` for "nine dollars", drop punctuation, mishear a word). So:

- Take the **caption text from `02-script.md`** narration blocks (this is the exact wording shown to viewers), split into ordered cue lines (one sentence or short clause per cue; split very long sentences).
- Take the **timestamps from the Whisper words**.
- Align the two word sequences with Needleman-Wunsch (normalize: lowercase, strip punctuation, map number-words ↔ digits, `&`→`and`). Assign each script word the matched Whisper word's time; interpolate timing for any unmatched script word from its known neighbors.
- Per cue: start = first word's start, end = last word's end.

The reusable builder is `references/build-srt.mjs` — it reads a cues file + the timings JSON and writes the SRT. Provide the cues as a JSON array of strings derived from `02-script.md`.

### 4. Enforce clean cue timing

- monotonic, non-overlapping cues
- gapless (each cue ends at the next cue's start) for smooth reading
- minimum cue duration ~0.7s
- last cue end clamped to the audio duration (ffprobe it)
- timestamps in `HH:MM:SS,mmm` SRT format

### 5. Export

Write the caption file(s) to `projects/<slug>/output/`:

- `output/captions.srt` (required)
- `output/captions.vtt` (optional, only if the user asks — same cues, WebVTT header + `.` decimal separator)

Also keep `voiceover/combined-word-timings.json` for reuse.

## Workflow

1. Resolve exactly one project (Input Contract).
2. Verify the full-length audio source precondition; stop and ask for `combine` (or a full render) if missing.
3. Read required context, including `02-script.md`.
4. Decode audio → raw PCM (ffmpeg).
5. Transcribe full audio → word timings JSON (`transcribe-combined.mjs`); save under `voiceover/`.
6. Derive ordered cue text from `02-script.md`; align to the timings and build the SRT (`build-srt.mjs`).
7. Run the Self-Check.
8. Export to `projects/<slug>/output/captions.srt` (+ `.vtt` if asked).
9. Write a short status note in `06-production-board.md`.
10. Respond with the Caption report (file path, cue count, total duration, sync source). Do not continue into upload or learning.

## Self-Check (must pass before handoff)

- audio decodes; reported sample count / duration matches the source (ffprobe).
- Whisper returns word timestamps spanning the whole timeline (last word end ≈ audio duration).
- cue count > 0; every cue has a non-empty line of text taken from the script.
- 0 overlapping cues, 0 zero-or-negative-duration cues, timestamps monotonic.
- first cue starts at/near `00:00:00,000`; last cue end == audio duration (within ~0.2s).
- spot-check 2-3 cues against the audio/script wording.
- file written to `projects/<slug>/output/captions.srt` and is valid UTF-8 SRT.

## Hard Fails

Stop and report if:

- no project is named and none can be unambiguously smart-selected.
- no full-length combined audio or full video render exists (tell the user to run `combine` first).
- the produced SRT has overlaps, gaps that imply drift, or a last-cue end that does not match the audio duration, and the cause cannot be fixed.
- the caption would be built from estimated timing instead of real transcription (never allowed).
- the audio source is not the one used in the video the user will upload (offsets would shift — re-sync against the exact file).

## Self-Improvement

Read `references/memory.md` every run. Update it when:

- the transcription toolchain changes (model, package, decode path).
- alignment needs sharper handling (numbers, quotes, repeated phrases).
- a new audio source type (full render extraction) needs a documented recipe.

Do not promote to `.agents/_shared/` unless the lesson is channel-wide.
