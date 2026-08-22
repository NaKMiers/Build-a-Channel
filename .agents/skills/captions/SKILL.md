---
name: captions
description: Translate a finished transcript into SRT subtitle files for English, Vietnamese, Spanish, Japanese, Dutch, Hindi, Chinese, and Korean. Saves one .srt file per language to outputs/captions/. Use when the user asks for captions, subtitles, subtitle files, or to translate the transcript into another language.
allowed-tools:
  - Bash
  - Read
  - Write
---

# captions

Translate a timestamped transcript into SRT subtitle files for multiple languages. The English
SRT is always included; all others are optional and the user can specify a subset.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/skills/captions/references/memory.md`

## Supported languages

| Code | Language   | File    |
| ---- | ---------- | ------- |
| en   | English    | en.srt  |
| vi   | Vietnamese | vi.srt  |
| es   | Spanish    | es.srt  |
| ja   | Japanese   | ja.srt  |
| nl   | Dutch      | nl.srt  |
| hi   | Hindi      | hi.srt  |
| zh   | Chinese    | zh.srt  |
| ko   | Korean     | ko.srt  |

## Preconditions

```bash
P="projects/<n>-<slug>"
ls "$P"/transcribes/transcript.md
```

The transcript must exist. It is the only required input. No cast, no audio, no metadata.

## Step 1 - Parse the transcript

Read `transcribes/transcript.md` in full. Parse every line of the form:

```
[M:SS] <narration text>
```

Strip the timestamp prefix and collect the narration text as a list of cue strings.

If a language is given as a list, use exactly those. Otherwise default to all eight.

## Step 2 - Translate via LLM

Call the LLM with the full English cue list and the target language. Format the cue list
as a JSON array so the model can count entries and return exactly the same count:

```json
{
  "language": "Spanish",
  "cues": [
    "A friend calls you late at night,",
    "wrecked over a decision.",
    ...
  ]
}
```

Prompt:

```
Translate every string in the cues array into <language>. Return a JSON object with a
"translations" key mapping to an array of translated strings, one per input string, in
the same order. Do not add, remove, or reorder any entries. Do not add explanations.
Do not number the translations. The text is narration voiceover: keep the phrasing
conversational, not formal.

Input cue count: N
```

Parse the JSON response. If the model returns a different count, reject and retry once.

**Parallelize**: call all languages concurrently in the same turn. Each call is independent.

**English is skipped** for the LLM step. Copy the English cues directly into the SRT.

## Step 3 - Build each SRT file

### SRT format

```
1
00:00:00,000 --> 00:00:03,000
A friend calls you late at night, wrecked over a decision.

2
00:00:03,000 --> 00:00:06,000
In ten minutes you say the right thing. Calm, clear, kind.
```

Rules:
- One sequence number per line, starting at 1, incrementing by 1.
- Timestamps are `HH:MM:SS,mmm --> HH:MM:SS,mmm`, not `M:SS`.
- Merge consecutive cues with no gap between them into one subtitle block. A gap means
  a new block. This keeps the English and translated SRTs in structural sync.
- A gap exists when the next `[M:SS]` is more than 2 seconds after the previous
  cue's end time plus the current cue's duration.
- Minimum display time per block: 1 second. Cap duration at 7 seconds.
- Blank line between blocks.
- No HTML tags, no styling.
- UTF-8 encoding for all files, including Japanese, Chinese, and Korean.

### Timestamp conversion

Convert each `[M:SS]` in the transcript to `HH:MM:SS,000` for the SRT start time.
The end time is the start of the next cue minus 80ms (subtitle gap), minimum 1 second.

Example: `[0:00]` is `00:00:00,000`. `[0:03]` with a 3-second cue starting at 0:00
is `00:00:03,000` minus 80ms = `00:00:02,920`.

If it is the last cue, set end time to start + 3 seconds (minimum display).

### Timing calculation

```python
# transcript uses [M:SS] from 0:00
# SRT uses HH:MM:SS,mmm
# 80ms gap between consecutive blocks

def ts_to_ms(m:ss):
    parts = m_ss.split(":")
    return int(parts[0]) * 60_000 + int(parts[1]) * 1_000

def ms_to_srt(ms):
    h = ms // 3_600_000
    m = (ms % 3_600_000) // 60_000
    s = (ms % 60_000) // 1_000
    return f"{h:02d}:{m:02d}:{s:02d},000"
```

### Consecutive merge rule

Walk the cues in order. If cue[i+1].start - cue[i].end <= 2000ms, merge them.
Otherwise, close the current block and start a new one.

## Step 4 - Write the files

```bash
P="projects/<n>-<slug>"
mkdir -p "$P"/outputs/captions
```

Write one `.srt` file per language into `outputs/captions/`. UTF-8 encoding.

## Step 5 - Report

Print the list of files written, their line counts, and their byte sizes.

## Step 6 - Self-improvement

After the user reports any quality issue with a specific language, append the durable
lesson to `references/memory.md`. Do not add generic LLM temperature notes or
system prompt experiments.
