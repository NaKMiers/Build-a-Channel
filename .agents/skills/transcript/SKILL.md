---
name: transcript
description: Turn a recorded TossExplains narration into transcribes/transcript.md, the timestamped [M:SS] cue list that the scenes skill consumes. Combines multi-part recordings into audios/full.mp3 first, then transcribes each part and merges onto that one timeline. Wraps tools/combine-audio.py, tools/audio-to-timestamps.py, and tools/srt-to-timestamps.py with the right paths and flags. Use when the user says "transcript", "timestamps", "align the audio", or has just recorded a voiceover.
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
ls "$P"/audios/part-*.mp3 2>/dev/null | wc -l      # more than 1 means combine first
```

- **Look in `audios/` first.** That is the project's home for the recorded narration. If
  exactly one audio file is there, use it without asking. If several are there, they are
  consecutive parts of one recording, so sort them by name and pass them in that order.
  Ignore `full.mp3` when collecting the parts, it is this skill's own output.
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

## Step 1 - Combine the parts first, always

**If `audios/` holds more than one part, build `audios/full.mp3` before transcribing
anything.** Do this without being asked. The transcript is a single timeline and the
editor scrubs against a single file, so that file has to exist and every timestamp has to
refer to it. Doing this first also fixes the part order and hands you the exact duration
of each part, which is what the later steps offset by.

```bash
P="projects/<n>-<slug>"
python3 tools/combine-audio.py "$P"/audios/part-*.mp3 \
  -o "$P"/audios/full.mp3 --json "$P"/transcribes/offsets.json
```

No ffmpeg needed, it concatenates frames and strips the tags itself. It prints each
part's duration and cumulative start; read those back to the user. Pass `--force` only to
rebuild an existing `full.mp3` deliberately. A single-part recording needs none of this,
skip straight to Step 2.

**Then open `full.mp3` in a player, or at least trust the tool's last line, and confirm
the duration it reports matches the total.** The tool prints `players will report ...` for
exactly this reason. A file can hold every frame and still announce the wrong length: if
the parts were exported at different bitrates the result is a VBR stream, and a player
that finds no valid Xing header falls back to extrapolating the first frame's bitrate
across the whole file. Project 3's parts were 256, 128, and 128 kbps, and before the tool
wrote a correct Xing header the 12m07s file showed as 8m28s. `combine-audio.py` now
refuses to write a file whose header disagrees with its frames, so a silent mismatch is
not possible, but the readout is still worth a glance.

If the user reports a wrong duration anyway, do not re-cut the transcript to match it. The
frames are the truth. Re-run `combine-audio.py --force`, and if the player still disagrees
the durable fix is re-exporting every part at the same bitrate.

**Sanity-check the part boundaries against the script before spending an API call.**
Divide each part's word count by its duration. Every part should land near the same words
per second, roughly 2.9 to 3.1 for this channel. A part that is well off means the script
was split in the wrong place, and forced alignment against a mismatched script produces
silently wrong timings, not an error.

## Step 2 - Choose the engine

**Case A, audio plus script. The default.** Forced alignment via ElevenLabs, roughly
$0.08 for a 12 minute video.

Single part:

```bash
python3 tools/audio-to-timestamps.py "$P"/audios/<audio> \
  --script "$P"/script_<short_slug>.md \
  --save-json "$P"/transcribes/words.json \
  -o "$P"/transcribes/transcript.md
```

**Multiple parts: align each part in its own run**, one part of audio against the matching
part of the script, then merge the caches onto `full.mp3`'s timeline. Per-part runs keep
each upload small, let a single failed part be retried on its own without re-paying for
the others, and keep the merge free and repeatable.

Split the script at its part boundaries first. The blank-line gaps in
`script_<short_slug>.md` mark where the recording stopped. Write the pieces to a working
directory, not into the project: they are scaffolding, not artifacts. Verify that the
pieces rejoin to the original with no words dropped.

```bash
W=<scratch dir>
for i in 1 2 3; do
  python3 tools/audio-to-timestamps.py "$P"/audios/part-$i.mp3 \
    --script "$W"/script-part-$i.md \
    --save-json "$W"/words-part-$i.json \
    -o "$W"/transcript-part-$i.md
done

python3 tools/audio-to-timestamps.py \
  --from-json "$W"/words-part-1.json \
  --from-json "$W"/words-part-2.json \
  --from-json "$W"/words-part-3.json \
  --offsets "$P"/transcribes/offsets.json \
  --save-json "$P"/transcribes/words.json \
  -o "$P"/transcribes/transcript.md
```

`--offsets` shifts each part by its measured start from Step 1, so silence at the end of a
part still occupies the timeline. Without it the parts butt-joined at the last spoken
word and every later timestamp ran early.

Always pass `--save-json`. It caches the result so the transcript can be re-cut at a
different granularity for free with `--from-json`. The merged `words.json` is the one the
project keeps; the per-part caches stay in the working directory.

**Case B, audio only, no script.** Plain transcription via Groq, under a cent, but warn
the user that wording and punctuation can drift from the script.

```bash
python3 tools/audio-to-timestamps.py "$P"/audios/<audio> --engine groq \
  --save-json "$P"/transcribes/words.json \
  -o "$P"/transcribes/transcript.md
```

Groq's free tier rejects uploads over 25MB, which is another reason to transcribe per
part rather than feeding it `full.mp3`.

**Case C, the user already has subtitles.** No API call at all.

```bash
python3 tools/srt-to-timestamps.py "$P"/audios/part-1.srt "$P"/audios/part-2.srt \
  -o "$P"/transcribes/transcript.md
```

**Multiple audio or subtitle files are consecutive parts of one recording**, so part 2
continues where part 1 ended.

### If the engine is unavailable

Both engines need a key in `.env`, and a key that exists can still be refused. Check
before spending time on the script split, and if the API rejects the call, stop and say so
plainly with the provider's own message. Do not fall back to the other engine without
asking: Groq changes the wording, and every image prompt downstream is derived from the
wording. Do not hand-write timestamps to fill the gap.

## Step 3 - Validate the output

```bash
T="$P/transcribes/transcript.md"
wc -l "$T"
head -3 "$T"
tail -1 "$T"                               # last cue must land near full.mp3's duration
grep -cvE '^\[[0-9]+:[0-9]{2}\] .' "$T"   # must be 0: every line is a well-formed cue
awk '{print $1}' "$T" | sort | uniq -d     # duplicate timestamps, note them
```

For a multi-part recording, the last cue must sit within a few seconds of the total
duration Step 1 printed. A last cue that falls well short means a part was dropped or the
offsets were not applied.

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

## Step 4 - Report duplicate timestamps

If two cues share a timestamp, say so explicitly and state the disambiguation the
`scenes` skill must record in its header, for example: `[3:24] appears twice; save the
second one as [3:25] so it does not overwrite the first`. Project 1 has exactly this
case. It matters because timestamps become scene image file names.

## Step 5 - Report and hand off

Give the line count, the total duration from the last timestamp, any duplicates, and the
first 3 lines. For a multi-part recording also name `full.mp3` and its duration, since
that is the file the editor loads. Then:

> Transcript saved to `<path>`, timed against `audios/full.mp3`.
>
> Next: **`/scenes`** to write one image prompt per timestamp. It also needs the cast, so
> run **`/cast`** first if you have not.

## Guardrails

- Never hand-write or hand-edit a transcript. Run the tool. Timestamps that do not come
  from real audio will not line up in the editor.
- Never transcribe the parts of a multi-part recording without building `full.mp3` first.
  The timestamps would refer to a timeline no single file has.
- Never pass `full.mp3` back in as a part. Collect `part-*.mp3` and exclude it.
- Never split the script by eyeballed word count alone. Check words per second against
  each part's measured duration first, because a mismatched script aligns without error.
- Never drop `--save-json`. Re-cutting without the cache costs another API call.
- Never reformat the `[M:SS]` timestamps the tool produces. They become file names.
- Never commit the audio file. `*.mp3`, `*.wav`, and `*.mp4` are gitignored on purpose, so
  `audios/` keeps only a `.gitkeep` in git. The recording is reproducible from the script,
  and `full.mp3` is reproducible from the parts.

## Self-improvement

Read `.agents/skills/transcript/references/memory.md` at the start of every run. Append
when a flag combination produces a better cut for this channel's pacing, when an engine
misbehaves, or when the user states a preferred lines-per-video target.
