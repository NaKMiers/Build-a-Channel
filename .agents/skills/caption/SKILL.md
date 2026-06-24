---
name: caption
description: Post-combine workflow step. Create accurate multi-language YouTube subtitle/caption files (.srt) for one Why It Works video project by transcribing the FULL combined audio (or full video render), aligning the exact English script text to real word-level timestamps, then translating that one timed cue set into all 22 supported languages while reusing the exact same timing. Use when the user asks to create captions, subtitles, an SRT/VTT file, closed captions, caption the video, or generate subtitles for upload. Requires a full combined voiceover (`hyperframes/full-video/combined-voiceover.mp3`) or a full video render — refuses to run on per-section audio only. Requires one project; use the project the user names, or smart-select the unambiguous active project, otherwise ask. Exports one `<language>.srt` per language to `projects/<slug>/output/captions/`.
---

# Caption

## Purpose

Produce subtitle/caption files for ONE finished `Why It Works` video in **all 22 supported languages** that match the spoken audio **100%**, then export one `<language>.srt` per language to the project's `output/captions/` folder for YouTube upload.

The non-negotiable requirement: **captions must not drift from the voice.** Timing is derived ONCE from the real audio (word-level transcription) against the English script, producing a single timed cue table. Every other language reuses that exact same cue table — only the displayed text is translated, never the timing. This makes all 22 tracks match the video by construction.

Two ground-truth rules:

- **Timing** comes from the real audio (whole-timeline word-level transcription). Never estimate from word counts or documented durations. Always transcribe the real combined audio.
- **English text** comes from the project `02-script.md` (exact wording shown to viewers). Translated text is a per-cue translation of that English cue, one line per cue, never word-by-word and never re-split.

## Pipeline Position

This runs once per project, AFTER `combine`, BEFORE `upload`:

```text
... -> render -> review   (repeat per section)
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

The reusable builder is `references/build-srt.mjs` — it reads a cues file + the timings JSON and writes the SRT. Provide the cues as a JSON array of strings derived from `02-script.md`. Pass the optional 5th/6th args so it ALSO emits the per-cue timing table that the translation step reuses:

```bash
node build-srt.mjs <timings.json> <english-cues.json> <out>/english.srt <audioDur> <out>/_segments.json
```

`_segments.json` is `[{ index, start, end, text }]` — the single source of timing for every language. Keep it under `voiceover/` (or the captions output dir); it is the only thing translated SRTs read for timing.

### 4. Enforce clean cue timing

- monotonic, non-overlapping cues
- gapless (each cue ends at the next cue's start) for smooth reading
- minimum cue duration ~0.7s
- last cue end clamped to the audio duration (ffprobe it)
- timestamps in `HH:MM:SS,mmm` SRT format

### 5. Translate into all 22 languages (reuse the exact timing)

For every language in the **Supported Languages** list below other than English, translate the English cue table into that language, ONE line per cue, keeping the cue **count and order identical** to `_segments.json`. Then write the SRT by reusing the English timing — never re-transcribe or re-time per language.

- Translate **whole cues**, not words. Natural, fluent translation of each cue's meaning; preserve the channel's smart/simple/dry tone. Reorder words within a cue as the target language requires — the cue still keeps its English start/end.
- Keep the count exact: do NOT split one English cue into two target lines or merge two into one. If a translation would naturally be very long, keep it as one cue anyway (it inherits that cue's duration).
- Keep untranslatables intact where appropriate: numbers, currency, brand/proper nouns, and code/UI identifiers (per the language rule) unless the language convention localizes them.
- Produce a `<lang>-cues.json` array of strings (same length as `_segments.json`), then:

```bash
node write-translated-srt.mjs <out>/_segments.json <lang>-cues.json <out>/<language>.srt
```

`write-translated-srt.mjs` refuses to write if the translated cue count ≠ segment count or any cue is empty — that guard is what keeps every language frame-aligned to the video. English uses its own `build-srt.mjs` output directly (no translation pass).

Batch the translation efficiently (translate many cues per model turn), but always re-emit the FULL array for each language so lengths stay exact.

### 6. Export

Write all language caption files to `projects/<slug>/output/captions/`:

- `output/captions/english.srt` plus one `<language>.srt` for every other supported language (22 files total).
- Filenames are lowercase, spaces→hyphens, parentheticals flattened — see the **Supported Languages** table for the exact basenames.
- `.vtt` variants only if the user asks (same cues, WebVTT header + `.` decimal separator).

Keep backward compatibility: also write `output/captions.srt` (the English track) at the project `output/` root so existing upload tooling still finds it.

Also keep `voiceover/combined-word-timings.json` and `_segments.json` for reuse.

## Supported Languages

All 22 are exported every run. English is built from the script; the rest are per-cue translations of the English cue table.

| Language | File |
| --- | --- |
| Arabic | `arabic.srt` |
| Bangla | `bangla.srt` |
| Chinese (Simplified) | `chinese-simplified.srt` |
| Chinese (Traditional) | `chinese-traditional.srt` |
| English | `english.srt` |
| French | `french.srt` |
| German | `german.srt` |
| Hindi | `hindi.srt` |
| Indonesian | `indonesian.srt` |
| Italian | `italian.srt` |
| Japanese | `japanese.srt` |
| Korean | `korean.srt` |
| Malayalam | `malayalam.srt` |
| Polish | `polish.srt` |
| Portuguese | `portuguese.srt` |
| Russian | `russian.srt` |
| Spanish | `spanish.srt` |
| Tamil | `tamil.srt` |
| Telugu | `telugu.srt` |
| Thai | `thai.srt` |
| Turkish | `turkish.srt` |
| Vietnamese | `vietnamese.srt` |

## Workflow

1. Resolve exactly one project (Input Contract).
2. Verify the full-length audio source precondition; stop and ask for `combine` (or a full render) if missing.
3. Read required context, including `02-script.md`.
4. Decode audio → raw PCM (ffmpeg).
5. Transcribe full audio → word timings JSON (`transcribe-combined.mjs`); save under `voiceover/`.
6. Derive ordered English cue text from `02-script.md`; align to the timings and build `english.srt` AND the `_segments.json` timing table (`build-srt.mjs` with the segments arg).
7. For each of the other 21 languages: translate the English cue table cue-for-cue (exact count/order), then write `<language>.srt` from `_segments.json` (`write-translated-srt.mjs`).
8. Run the Self-Check (including the multi-language timing re-check — the most important gate).
9. Export all 22 files to `projects/<slug>/output/captions/`, plus the compatibility `output/captions.srt` (English). Add `.vtt` only if asked.
10. Write a short status note in `06-production-board.md` (languages exported, cue count, duration).
11. Respond with the Caption report (output dir, languages, cue count, total duration, sync source). Do not continue into upload or learning.

## Self-Check (must pass before handoff)

English / timing base:

- audio decodes; reported sample count / duration matches the source (ffprobe).
- Whisper returns word timestamps spanning the whole timeline (last word end ≈ audio duration).
- cue count > 0; every English cue has a non-empty line of text taken from the script.
- 0 overlapping cues, 0 zero-or-negative-duration cues, timestamps monotonic.
- first cue starts at/near `00:00:00,000`; last cue end == audio duration (within ~0.2s).
- spot-check 2-3 English cues against the audio/script wording.

Multi-language timing re-check (MOST IMPORTANT — captions must match the video):

- exactly 22 files exist in `output/captions/`, one per Supported Language, named per the table.
- every `<language>.srt` has the **same cue count** as `english.srt`.
- every `<language>.srt` cue's start/end timestamps are **byte-identical** to the corresponding `english.srt` cue (they came from the one `_segments.json`). Verify programmatically: extract the timestamp lines from each file and diff them against `english.srt`'s — any difference is a hard fail.
- cross-check first cue of each section's narration against the combine section offsets in `06-production-board.md` (English track), confirming the shared timing actually lands on the video timeline.
- spot-check 2-3 cues per a few languages: the translated line is a faithful, fluent translation of the matching English cue (right meaning, right cue).
- every file is valid UTF-8 SRT (non-Latin scripts — Arabic, CJK, Indic, Thai — render correctly, no mojibake).
- compatibility `output/captions.srt` (English) also written.

## Hard Fails

Stop and report if:

- no project is named and none can be unambiguously smart-selected.
- no full-length combined audio or full video render exists (tell the user to run `combine` first).
- the produced SRT has overlaps, gaps that imply drift, or a last-cue end that does not match the audio duration, and the cause cannot be fixed.
- the caption would be built from estimated timing instead of real transcription (never allowed).
- the audio source is not the one used in the video the user will upload (offsets would shift — re-sync against the exact file).
- any `<language>.srt` cue count or timestamps differ from `english.srt` (translation split/merged/dropped a cue — re-translate that language to exactly one line per cue; never hand-edit timestamps to paper over it).
- a translation pass changed cue boundaries instead of only the text.

## Self-Improvement

Read `references/memory.md` every run. Update it when:

- the transcription toolchain changes (model, package, decode path).
- alignment needs sharper handling (numbers, quotes, repeated phrases).
- a new audio source type (full render extraction) needs a documented recipe.
- the supported-language set changes, or a language needs special handling (script direction, line-length, transliteration, font/encoding).
- a better batching or verification approach for the 22-language translation pass is found.

Do not promote to `.agents/_shared/` unless the lesson is channel-wide.
