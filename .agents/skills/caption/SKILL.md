---
name: caption
description: Create five publish-ready SRT caption files from a completed HumanPrice transcript. Use after /transcript when the user asks for captions, subtitles, SRT files, translated subtitles, Spanish, Japanese, Chinese, or Hindi captions.
---

# caption

Create timed subtitle tracks from `transcribes/transcript.md`. The transcript owns the
words and timestamps. Never transcribe the audio again or invent new timing.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/caption/references/memory.md`

## Preconditions

Resolve one project and require its completed transcript:

```bash
P="projects/<n>-<slug>"
test -f "$P/transcribes/transcript.md"
test -f "$P/transcribes/offsets.json" || ls "$P"/audios/full.mp3
```

Stop if the transcript is missing or malformed. Do not derive times from the narration
script. Use `transcribes/offsets.json` when present for the final cue end time. Otherwise
read the duration of `audios/full.mp3` with the existing MP3 tooling.

## Deliverables

Write exactly these five files under `outputs/captions/`:

```text
english.srt   English
spanish.srt   Spanish
japanese.srt  Japanese
chinese.srt   Simplified Chinese
hindi.srt     Hindi
```

`Hindi` is the Indian-language track. Do not create extra language tracks unless the user
asks. Keep every source cue in every language, in the same order and at the same times.

## Workflow

1. Validate the transcript has ordered `[M:SS] narration` cues.
2. Render English directly from the transcript with `scripts/render_srt.py`.
3. Translate each cue into Spanish, Japanese, Simplified Chinese, and Hindi. Preserve
   meaning, factual values, names, and uncertainty. Use natural spoken subtitles, not
   literal word-for-word phrasing. Do not add explanations, speaker labels, or text not
   present in the narration.
4. Save each translated cue list as a JSON array in a scratch directory. The array has one
   nonempty string per transcript cue, in the exact same order. Use the renderer to apply
   the source timing.
5. Validate every resulting `.srt` with the same script. Fix translation content only. Do
   not hand-edit a timestamp.

Example commands:

```bash
P="projects/<n>-<slug>"
W=$(mktemp -d)
CAPTIONS="$P/outputs/captions"
mkdir -p "$CAPTIONS"
FINAL=$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["total"])' "$P/transcribes/offsets.json")

python3 .agents/skills/caption/scripts/render_srt.py \
  "$P/transcribes/transcript.md" \
  --final-end "$FINAL" \
  -o "$CAPTIONS/english.srt"

# Write $W/spanish.json, $W/japanese.json, $W/chinese.json, and $W/hindi.json as JSON arrays.
for lang in spanish japanese chinese hindi; do
  python3 .agents/skills/caption/scripts/render_srt.py \
    "$P/transcribes/transcript.md" \
    --texts-json "$W/$lang.json" \
    --final-end "$FINAL" \
    -o "$CAPTIONS/$lang.srt"
done

python3 .agents/skills/caption/scripts/render_srt.py --validate "$CAPTIONS"/*.srt
```

If `offsets.json` is absent, set `FINAL` to the true duration of `audios/full.mp3`. The
last caption must not extend past it.

## Quality rules

- Translate narration only. Do not translate file names, handles, or system paths.
- Keep Arabic digits when an exact number is spoken. Use the language's normal punctuation
  and typography otherwise.
- Keep a cue on one or two readable subtitle lines. Never create an empty cue.
- Preserve the transcript cue count exactly. Use the source cue start and end times in all
  five files.
- Never put Markdown, headings, comments, or cue metadata inside an SRT file.
- The renderer uses `next cue minus 10 ms` for each cue end, so adjacent captions do not
  overlap.

## Completion

Report the five paths, cue count, and final timestamp. Then say:

`Next: import the SRT track that matches the video's audience into the editor.`

## Self-improvement

Append only durable translation or subtitle-timing lessons to `references/memory.md`.
