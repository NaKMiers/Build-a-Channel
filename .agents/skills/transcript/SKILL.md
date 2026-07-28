---
name: transcript
description: Turn a recorded TossExplains narration audio file into transcribes/transcript.md, the timestamped [M:SS] cue list that the scenes skill consumes. Wraps tools/audio-to-timestamps.py and tools/srt-to-timestamps.py with the right paths and flags. Use when the user says "transcript", "timestamps", "align the audio", or has just recorded a voiceover.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# transcript

Bridge between the recorded voiceover and the image prompt stage. This skill is mostly
deterministic: it picks the right tool, the right engine, and the right paths, then
validates the output shape.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/file-formats.md` - the `transcribes/transcript.md` section
- `.agents/skills/transcript/references/memory.md`

## Preconditions

```bash
P="projects/<n>-<slug>"
ls -d projects/*/ 2>/dev/null
ls "$P"/script_*.md 2>/dev/null
ls "$P"/audios/ 2>/dev/null                       # the voiceover lives here
```

- **Look in `audios/` first.** That is the project's home for the recorded narration. If
  exactly one audio file is there, use it without asking. If several are there, they are
  consecutive parts of one recording, so sort them by name and pass them in that order.
- Only ask the user for a path if `audios/` is empty and they did not give one. If they give
  a path outside the project, offer to move the file into `audios/` so the project stays
  self-contained.
- The script file is strongly recommended, not strictly required. With `--script` the tool
  does forced alignment, so **the words are yours and only the timing comes from the
  API**. Without it, the words come from a speech-to-text model and can drift from what
  you wrote. Always prefer forced alignment.
- Check the key exists before spending a call:

```bash
grep -q ELEVENLABS_API_KEY .env 2>/dev/null && echo "elevenlabs key present" || echo "no elevenlabs key"
grep -q GROQ_API_KEY .env 2>/dev/null && echo "groq key present" || echo "no groq key"
```

## Step 1 - Choose the path

**Case A, audio plus script. The default.** Forced alignment via ElevenLabs, roughly
$0.08 for a 12 minute video.

```bash
P="projects/<n>-<slug>"
python3 tools/audio-to-timestamps.py "$P"/audios/<audio> \
  --script "$P"/script_<short_slug>.md \
  --save-json "$P"/transcribes/words.json \
  -o "$P"/transcribes/transcript.md
```

Always pass `--save-json`. It caches the API result so the transcript can be re-cut at a
different granularity for free with `--from-json`.

**Case B, audio only, no script.** Plain transcription via Groq, under a cent, but warn
the user that wording and punctuation can drift from the script.

```bash
python3 tools/audio-to-timestamps.py "$P"/audios/<audio> --engine groq \
  --save-json "$P"/transcribes/words.json \
  -o "$P"/transcribes/transcript.md
```

**Case C, the user already has subtitles.** No API call at all.

```bash
python3 tools/srt-to-timestamps.py "$P"/audios/part-1.srt "$P"/audios/part-2.srt \
  -o "$P"/transcribes/transcript.md
```

**Multiple audio or subtitle files are consecutive parts of one recording**, so part 2
continues where part 1 ended. Pass one `--script` per audio part in the same order.

## Step 2 - Validate the output

```bash
T="$P/transcribes/transcript.md"
wc -l "$T"
head -3 "$T"
grep -cvE '^\[[0-9]+:[0-9]{2}\] .' "$T"   # must be 0: every line is a well-formed cue
awk '{print $1}' "$T" | sort | uniq -d     # duplicate timestamps, note them
```

Interpret the line count:

- **Fewer than 20 lines** means the transcript is incomplete. Tell the user exactly:
  "This looks incomplete. A 10 to 14 minute video should have 80 to 120 timestamp lines."
  Then stop.
- **Around 230 lines of roughly 3 seconds** is normal for a 12 minute script with the
  default settings.
- **More lines than the user wants to pay to illustrate**: re-cut for free from the cache
  rather than re-calling the API.

```bash
python3 tools/audio-to-timestamps.py --from-json "$P"/transcribes/words.json \
  --max-dur 5 -o "$P"/transcribes/transcript-min5.md
```

Only write an alternate cut if the user asks for one.

## Step 3 - Report duplicate timestamps

If two cues share a timestamp, say so explicitly and state the disambiguation the
`scenes` skill must record in its header, for example: `[3:24] appears twice; save the
second one as [3:25] so it does not overwrite the first`. Project 1 has exactly this
case. It matters because timestamps become scene image file names.

## Step 4 - Report and hand off

Give the line count, the total duration from the last timestamp, any duplicates, and the
first 3 lines. Then:

> Transcript saved to `<path>`.
>
> Next: **`/scenes`** to write one image prompt per timestamp. It also needs the cast, so
> run **`/cast`** first if you have not.

## Guardrails

- Never hand-write or hand-edit a transcript. Run the tool. Timestamps that do not come
  from real audio will not line up in the editor.
- Never drop `--save-json`. Re-cutting without the cache costs another API call.
- Never reformat the `[M:SS]` timestamps the tool produces. They become file names.
- Never commit the audio file. `*.mp3`, `*.wav`, and `*.mp4` are gitignored on purpose, so
  `audios/` keeps only a `.gitkeep` in git. The recording is reproducible from the script.

## Self-improvement

Read `.agents/skills/transcript/references/memory.md` at the start of every run. Append
when a flag combination produces a better cut for this channel's pacing, when an engine
misbehaves, or when the user states a preferred lines-per-video target.
