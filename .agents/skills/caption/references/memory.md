# Caption Skill Memory

Memory for the `caption` skill — creating accurate `.srt`/`.vtt` subtitles for one finished video by transcribing the FULL combined audio and aligning the exact script text to real word-level timestamps. Export to `projects/<slug>/output/`.

Use this file for transcription toolchain details, alignment gotchas, and recurring fixes. Use `.agents/_shared/` only for channel-wide lessons.

## Current Skill Standard

- Post-`combine` step; runs once per project, before `upload`.
- Require one project (named, smart-selected, or asked).
- Require a single full-length audio source: `hyperframes/full-video/combined-voiceover.mp3` (preferred), a full video render's audio, or a user-pointed full track. Refuse on per-section audio only — tell the user to run `combine` first.
- Timing ALWAYS from real word-level transcription of the full audio. Never estimate from word counts or documented durations.
- Displayed text ALWAYS from `02-script.md` narration (ground truth), aligned to the transcribed timestamps.
- Export `output/captions.srt` (+ `output/captions.vtt` only if asked). Keep `voiceover/combined-word-timings.json` for reuse.

## Proven Toolchain (from `why-cheap-products-keep-getting-worse`, 2026-06-22)

- No Python / ffmpeg / Whisper on PATH on this Windows box. Node v26 + bun are present.
- Decode audio with a static ffmpeg: `<ffmpeg> -y -i <audio> -ar 16000 -ac 1 -f f32le out.raw`.
  - Existing static binary: `%TEMP%/wiw-ffmpeg-static/node_modules/ffmpeg-static/ffmpeg.exe`.
  - Install if missing: `npm.cmd install --prefix %TEMP%/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static`.
  - CapCut also ships `ffmpeg.exe` under `AppData/Local/CapCut/Apps/<ver>/`.
- Transcribe with `Xenova/whisper-tiny.en` via `@xenova/transformers`, `return_timestamps:"word"`, `chunk_length_s:30`, `stride_length_s:5`, over the WHOLE audio in one pass (timestamps land on the final timeline; no offset math, no drift).
  - Ready-made setup with the model cached: `%TEMP%/wiw-whisper/` (has `node_modules/@xenova/transformers` + cached `whisper-tiny.en` onnx). Reuse it; it already produced this channel's section timings.
  - Read raw f32le into `new Float32Array(buf.buffer, buf.byteOffset, len/4)`; sample rate 16000 → duration = samples/16000.
- whisper-tiny.en transcription quality on this clean TTS voice (Kokoro `am_eric`, speed 0.84) is high — words matched the script almost verbatim. Good enough to anchor alignment.

## Alignment (the reliable approach)

- Whisper wording is NOT authoritative: it wrote `$9` for "nine dollars", dropped punctuation, and once heard "pay a checkout" for "pay at checkout". So never ship Whisper text as the caption.
- Build cues from `02-script.md` narration blocks, in order, one sentence / short clause per cue (split very long sentences for readability).
- Needleman-Wunsch align normalized tokens (lowercase, strip punctuation, `&`→`and`, map number-words ↔ digits) between cue words and Whisper words. Assign each cue word the matched Whisper time; interpolate unmatched cue words from known neighbors. Cue start = first word start, end = last word end.
- Enforce: monotonic, non-overlapping, gapless (cue ends at next cue's start), min ~0.7s, last cue end == audio duration (ffprobe / last word end).
- Helpers in this folder: `transcribe-combined.mjs` (audio → word timings JSON) and `build-srt.mjs` (timings + cues JSON → SRT). `build-srt.mjs` takes cues as an external JSON array so it is not hardcoded per video.

## Verified Result (first run)

- `why-cheap-products-keep-getting-worse`: combined audio 4:11.18 (251.18s) → 860 Whisper words → 94 cues. Validation: 0 overlaps, 0 zero-length cues, first cue `00:00:00,000`, last cue ends `00:04:11,180` (== audio). Exported to `projects/why-cheap-products-keep-getting-worse/output/captions.srt`.

## Watch Out

- The caption is tied to the SPECIFIC audio file used. If the uploaded video has different pacing (added intro/outro, silence, re-rendered audio), re-sync against that exact file or offsets shift.
- Many headless transcription runs can leave zombie node/onnxruntime processes — not observed harmful here, but watch memory on big batches.
- Helper module resolution: `transcribe-combined.mjs` imports `@xenova/transformers`, which Node ESM resolves from the SCRIPT's own folder, not cwd. Run the transcription from a folder that has the package installed (e.g. `%TEMP%/wiw-whisper/`, which also has `gen-combined.mjs`, the identical helper). Running the skill copy from elsewhere throws `ERR_MODULE_NOT_FOUND`.
- Strip spoken-vs-written mismatches from cue text: `02-script.md` narration contains bracketed stage directions (`[deadpan]`, `[beat]`, `[slower]`, `[pause]`) that are NOT spoken. Remove them when building cues, or alignment wastes tokens and the cue text shows directions.

## Whisper Tail Glitch (whisper-tiny.en)

On `why-everyone-pretends-to-be-busy` the final ~6 words got NON-MONOTONIC timestamps: "...not" stamped at 261.8s, then "lazy ... Wi-Fi" jumped BACKWARDS to 257–259s (a known whisper-tiny end-of-audio / chunk-boundary artifact). Effect: the last cue's word-derived end was wrong and the min-duration clamp left the final line showing only 262.1s while the audio ran to 265.1s — the last caption was cut short.

Fix applied: the last cue's START was still correct (right after the previous distinct word); only its END was short. Extended the final cue's end to ≈ the audio duration (held the last line through the end — standard and harmless even over a short trailing silence). Always sanity-check the LAST 1-2 cues against the audio tail; if whisper timestamps go backwards there, extend the final cue end to the audio duration rather than trusting the glitched word times.

## Feedback Log

### 2026-06-22 - Skill created from the verified SRT build

Classification: `Operational lesson`

Context:
Anh Khoa first got an ESTIMATED SRT (timing guessed from word counts) and rejected it: "you will mismatch the voiceover ... must match 100% the video." The fix was to transcribe the real combined audio for word-level timestamps and align the exact script text to them. Then asked to make it a reusable `caption` skill, positioned after `combine`, smart-selecting the project, exporting to `/output`.

Lesson:
Caption timing must be derived from the actual audio, not estimated. Transcribe the full combined audio once (whole-timeline word timestamps), keep the displayed words from the script, and align the two. This guarantees correct wording AND matching timing. Gate on a full-length audio source existing (combine output or full render); refuse on per-section audio.

Apply next time:
- always smart-select/confirm one project; require the full combined audio or full render
- transcribe the full audio (whisper-tiny.en via @xenova/transformers) → word timings JSON under `voiceover/`
- cues from `02-script.md`; NW-align to timings; enforce clean monotonic gapless cues
- export `output/captions.srt` (+ `.vtt` only if asked); note it in `06-production-board.md`
- do not continue into upload or learning

Promote to shared memory:
No; caption-skill execution practice.
