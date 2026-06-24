# Caption Skill Memory

Memory for the `caption` skill — creating accurate `.srt`/`.vtt` subtitles for one finished video by transcribing the FULL combined audio and aligning the exact script text to real word-level timestamps. Export to `projects/<slug>/output/`.

Use this file for transcription toolchain details, alignment gotchas, and recurring fixes. Use `.agents/_shared/` only for channel-wide lessons.

## Current Skill Standard

- Post-`combine` step; runs once per project, before `upload`.
- Require one project (named, smart-selected, or asked).
- Require a single full-length audio source: `hyperframes/full-video/combined-voiceover.mp3` (preferred), a full video render's audio, or a user-pointed full track. Refuse on per-section audio only — tell the user to run `combine` first.
- Timing ALWAYS from real word-level transcription of the full audio. Never estimate from word counts or documented durations.
- English displayed text ALWAYS from `02-script.md` narration (ground truth), aligned to the transcribed timestamps.
- **Multi-language (since 2026-06-24):** export ALL 22 supported languages as `output/captions/<language>.srt`. Timing is derived ONCE for English, emitted as `_segments.json` (`[{index,start,end,text}]`) by `build-srt.mjs`. Every other language is a per-cue translation of the English cue table (exact same count/order) and reuses `_segments.json` timing via `write-translated-srt.mjs` — never re-transcribed or re-timed. So all 22 tracks are frame-identical to the video by construction.
- Translate WHOLE cues, never word-by-word, never split/merge a cue. `write-translated-srt.mjs` hard-fails on a count mismatch or empty cue.
- MOST IMPORTANT gate: re-check that every `<language>.srt` has identical cue count and byte-identical timestamps to `english.srt`.
- Export to `output/captions/` (22 files); also keep compatibility `output/captions.srt` (English) at output root. `.vtt` only if asked. Keep `voiceover/combined-word-timings.json` + `_segments.json` for reuse.
- 22 languages: Arabic, Bangla, Chinese (Simplified→`chinese-simplified`), Chinese (Traditional→`chinese-traditional`), English, French, German, Hindi, Indonesian, Italian, Japanese, Korean, Malayalam, Polish, Portuguese, Russian, Spanish, Tamil, Telugu, Thai, Turkish, Vietnamese.

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
- Helpers in this folder: `transcribe-combined.mjs` (audio → word timings JSON), `build-srt.mjs` (timings + cues JSON → English SRT; pass arg 6 to also emit `_segments.json`), and `write-translated-srt.mjs` (`_segments.json` + translated-cues JSON → `<language>.srt`, reusing English timing). All take external JSON so nothing is hardcoded per video.

## Verified Results

- `why-cheap-products-keep-getting-worse` (first run): combined audio 4:11.18 (251.18s) → 860 Whisper words → 94 cues. 0 overlaps, 0 zero-length, first `00:00:00,000`, last ends `00:04:11,180` (== audio).
- `why-everything-is-a-subscription-now` (2026-06-23): combined audio 327.989s (combine cap 328.056s) → 1021 Whisper words → 132 cues. 0 overlaps / 0 zero-neg / monotonic / gapless; first `00:00:00,000`, last ends `00:05:28,056` (== cap). Tail clean (no whisper backward-jump this run). 1016 script tokens aligned vs 1021 hyp.
- `why-cheap-products-keep-getting-worse` 22-language run (2026-06-24): reused the already-verified English `output/captions.srt` (94 cues, last `00:04:11,180`) as the timing base instead of re-transcribing — parsed it into `_segments.json` with a tiny SRT parser, then translated the 94 cues into 21 languages (one subagent per language, each writing a `<lang>-cues.json` of exactly 94 strings) and built each SRT via `write-translated-srt.mjs`. Verified all 22 files = 94 cues with byte-identical timestamp lines vs `english.srt` (0 mismatches). Efficient pattern: when a verified English SRT already exists, parse it for both cues + timing rather than re-running whisper. Parallel translator subagents (1 per language) + the count-guard in `write-translated-srt.mjs` make the 21-language fan-out fast and safe; "WIT" mascot must be flagged to translators as a keep-verbatim proper noun.

## Cross-Check Cue Times Against The Combine Section Offsets (cheap, high-signal)

When the project was combined, `06-production-board.md` records each section's cumulative ACTUAL-mp3 offset (start of section N on the full timeline). After building the SRT, grep the first cue of each section's narration and confirm its timestamp ≈ that section offset. On subscription: S2 cue `00:00:23.62` vs offset 23.568s; S5 `00:02:47.00` vs 166.896s; S7 `00:04:33.96` vs 273.888s — all near-exact. If a section's first cue is off by more than ~0.3s, alignment drifted there (or the cue text doesn't match what's spoken). Faster and more reliable than listening to spot-checks.

## Watch Out

- The caption is tied to the SPECIFIC audio file used. If the uploaded video has different pacing (added intro/outro, silence, re-rendered audio), re-sync against that exact file or offsets shift.
- Many headless transcription runs can leave zombie node/onnxruntime processes — not observed harmful here, but watch memory on big batches.
- Helper module resolution: `transcribe-combined.mjs` imports `@xenova/transformers`, which Node ESM resolves from the SCRIPT's own folder, not cwd. Run the transcription from a folder that has the package installed (e.g. `%TEMP%/wiw-whisper/`, which also has `gen-combined.mjs`, the identical helper). Running the skill copy from elsewhere throws `ERR_MODULE_NOT_FOUND`.
- Strip spoken-vs-written mismatches from cue text: `02-script.md` narration contains bracketed stage directions (`[deadpan]`, `[beat]`, `[slower]`, `[pause]`) that are NOT spoken. Remove them when building cues, or alignment wastes tokens and the cue text shows directions.

## Whisper Tail Glitch (whisper-tiny.en)

On `why-everyone-pretends-to-be-busy` the final ~6 words got NON-MONOTONIC timestamps: "...not" stamped at 261.8s, then "lazy ... Wi-Fi" jumped BACKWARDS to 257–259s (a known whisper-tiny end-of-audio / chunk-boundary artifact). Effect: the last cue's word-derived end was wrong and the min-duration clamp left the final line showing only 262.1s while the audio ran to 265.1s — the last caption was cut short.

Fix applied: the last cue's START was still correct (right after the previous distinct word); only its END was short. Extended the final cue's end to ≈ the audio duration (held the last line through the end — standard and harmless even over a short trailing silence). Always sanity-check the LAST 1-2 cues against the audio tail; if whisper timestamps go backwards there, extend the final cue end to the audio duration rather than trusting the glitched word times.

## Feedback Log

### 2026-06-24 - Extended to 22-language captions

Classification: `Operational lesson`

Context:
Anh Khoa asked caption to stop producing only English and instead export captions in 22 languages, each named `<language>.srt` in `output/captions/`, and stressed the re-check that every track matches the video timing as the most important step.

Lesson:
Derive timing exactly ONCE (English, against the real audio) and reuse it for all languages. Translation is per-cue (one line per cue, same count/order) so cue index → timing is shared; `write-translated-srt.mjs` reuses `_segments.json` and refuses on any count mismatch. This guarantees all 22 tracks are frame-identical to the video — translation can never introduce drift. Always re-verify cue count + byte-identical timestamps vs `english.srt` before handoff.

Apply next time:
- build English SRT + `_segments.json`, translate each other language cue-for-cue, write via `write-translated-srt.mjs`
- export 22 files to `output/captions/` + compatibility `output/captions.srt`
- re-check timestamps match across all languages (the hard gate)

Promote to shared memory:
No; caption-skill execution practice.

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
