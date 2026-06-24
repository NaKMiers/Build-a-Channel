---
name: caption
description: Post-combine workflow step. Create accurate multi-language YouTube subtitle/caption files (.srt) for one Why It Works video project by transcribing the FULL combined audio (or full video render), aligning the exact English script text to real word-level timestamps, then translating that one timed cue set into all 22 supported languages while reusing the exact same timing. Use when the user asks to create captions, subtitles, an SRT/VTT file, closed captions, caption the video, or generate subtitles for upload. Requires a full combined voiceover (`hyperframes/full-video/combined-voiceover.mp3`) or a full video render — refuses to run on per-section audio only. Requires one project; use the project the user names, or smart-select the unambiguous active project, otherwise ask. Exports one `<language>.srt` per language to `projects/<slug>/output/captions/`.
---

# Caption (Claude wrapper)

This is the Claude discovery wrapper for the **caption** skill. The canonical
definition — full purpose, gates, method, workflow, self-check, and
self-improving memory — lives under `.agents/` so Codex and Claude share one source of truth.

When this skill runs:

1. Read and follow `.agents/skills/caption/SKILL.md` exactly.
2. Read the references it points to, including `.agents/skills/caption/references/memory.md`, and reuse the helper scripts `transcribe-combined.mjs`, `build-srt.mjs`, and `write-translated-srt.mjs`.
3. Apply the workspace rules in `CLAUDE.md` and `.agents/rules/`.
4. Write any skill self-improvement back to `.agents/skills/caption/references/memory.md` (the single canonical copy), never a Claude-side duplicate.

Do not duplicate the skill logic here. If this wrapper and the canonical file ever
disagree, `.agents/skills/caption/SKILL.md` wins.

Key guarantees this skill must honor:

- Runs after `combine`, before `upload`; once per project.
- Require one project (named, smart-selected, or asked).
- Require a full-length audio source (combined voiceover or full render); refuse on per-section audio — tell the user to run `combine` first.
- Timing ALWAYS from real word-level transcription of the full audio; never estimated. Derived ONCE for English and reused for every language.
- English displayed text ALWAYS from `02-script.md`, aligned to the transcribed timestamps. Other languages are per-cue translations (same cue count/order) reusing the English timing.
- Export ALL 22 supported languages as `projects/<slug>/output/captions/<language>.srt` (e.g. `english.srt`, `vietnamese.srt`, `japanese.srt`), plus a compatibility `output/captions.srt` (English). `.vtt` only if asked.
- MOST IMPORTANT: re-check that every `<language>.srt` has identical cue count and byte-identical timestamps to `english.srt` before handoff.
