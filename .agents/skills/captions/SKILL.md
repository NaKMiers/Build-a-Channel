---
name: captions
description: Build word-accurate SRT subtitle files for a TossExplains video from the forced-aligned words.json, then translate them into up to 25 languages. Writes one .srt per language to outputs/captions/. Runs after /transcript. Use when the user says "captions", "subtitles", "srt", "translate the transcript", or names a language to subtitle into.
allowed-tools:
  - Bash
  - Read
  - Write
  - Agent
---

# captions

Turn a recorded narration into subtitle files. Runs **after `/transcript`**, because it is
built on `transcribes/words.json`, the word-level forced alignment that `/transcript`
saves with `--save-json`.

English is built first, from the audio timings alone. Every other language is poured into
that same timing spine, so all 25 files are frame-identical to each other by construction.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/skills/captions/references/memory.md`

## Why words.json and not the transcript

The transcript is a **line**-level file. `transcribes/words.json` carries the real onset
and offset of every **word**:

```json
{ "start": "00:00.100", "end": "00:00.300", "text": "Ten" }
```

Subtitle blocks are not transcript cues. `cut_blocks` closes a block on a duration cap, a
character cap, a real pause, or a sentence boundary, and `best_split` then walks backward
through individual words to find a cut a translator can actually work with. All of that
needs per-word timings. A transcript line gives one start and nothing inside it, so cutting
from the transcript means every block boundary lands on whichever line happened to be
nearby, and every subtitle inherits that line's start rather than the frame its own first
word arrives on.

Note that `transcript.md` now carries milliseconds itself, `[00:00.180]` rather than the old
`[0:00]`. That closes the *rounding* gap but not the *granularity* one, and the granularity
one is the reason this skill exists. Do not read the finer stamps as permission to build
captions from the transcript.

The transcript is still required, for two things: it proves `words.json` belongs to this
take, and it is the reference a translator reads for context. It is never the timing source.

## Preconditions

```bash
P="projects/<n>-<slug>"
ls "$P"/transcribes/words.json "$P"/transcribes/transcript.md
```

Both must exist. If `words.json` is missing, stop and say:

> `words.json` is missing. Run **`/transcript`** first. If the transcript was made without
> `--save-json`, re-run it with that flag, or re-cut from the cache with `--from-json`.

Do not improvise a transcript-only fallback. A caption track that is a second early on
every line is worse than no caption track, because nobody re-checks a file that exists.

The build stage verifies that `words.json` and `transcript.md` describe the same audio and
refuses to run if they diverge. A stale `words.json` from an earlier take aligns without
error and drifts against the video with nothing on screen to show for it.

Legacy projects 1 through 5 may use `transcribes/transcript.txt`. Pass whichever exists.

## Languages

25 files, one per language. The stem is the BCP-47 tag YouTube expects when the file is
uploaded as a caption track, so `outputs/captions/vi.srt` uploads as Vietnamese with no
renaming.

| Code      | Language            | Code | Language   | Code | Language   |
| --------- | ------------------- | ---- | ---------- | ---- | ---------- |
| `ar`      | Arabic              | `fr` | French     | `pl` | Polish     |
| `bn`      | Bangla              | `de` | German     | `pt` | Portuguese |
| `zh-Hans` | Chinese Simplified  | `hi` | Hindi      | `pa` | Punjabi    |
| `zh-Hant` | Chinese Traditional | `id` | Indonesian | `ru` | Russian    |
| `en`      | English             | `it` | Italian    | `es` | Spanish    |
| `fil`     | Filipino            | `ja` | Japanese   | `ta` | Tamil      |
| `ml`      | Malayalam           | `ko` | Korean     | `te` | Telugu     |
| `mr`      | Marathi             | `th` | Thai       | `tr` | Turkish    |
|           |                     |      |            | `vi` | Vietnamese |

**Default to all 25.** Project 11 shipped `en` and `vi` as a scope call and the owner
rejected it: they want the full set every time. Only cut the list when the user names a
subset in this turn. English is always included, whatever subset is named.

## Files written

```
projects/<n>-<slug>/outputs/captions/
  blocks.json      the shared timing spine, English text plus start and end in ms
  en.srt           built from words.json
  ar.srt  bn.srt  zh-Hans.srt  ...  vi.srt
```

`blocks.json` is a real artifact, not scratch. It is what makes every language file
identical in timing, and it is what lets a single language be re-translated later without
rebuilding or re-timing anything.

## Step 1 - Build en.srt

```bash
P="projects/<n>-<slug>"
python3 tools/captions-srt.py build \
  --words      "$P"/transcribes/words.json \
  --transcript "$P"/transcribes/transcript.md \
  --out        "$P"/outputs/captions
```

This writes `en.srt` and `blocks.json`, and prints the block count, the mean, minimum and
maximum duration, the character statistics, and how many blocks the caps had to split
mid-sentence.

### How blocks are cut

Words accumulate into a block until one of four things closes it:

| Closer            | Fires when                                               |
| ----------------- | -------------------------------------------------------- |
| duration cap      | adding the next word would pass **7.0s**                  |
| character cap     | adding the next word would pass **96 characters**         |
| real silence      | **0.5s** or more of measured silence, block already **2.5s** |
| sentence boundary | the block ends a sentence and already runs **2.0s**       |

Both caps are tested against **what the block would become** if the next word joined, not
against what it already is. A ceiling checked after the fact is not a ceiling: a cap tested
on the committed block once let a 6.5s block accept a 3s word and ship at 9.5s.

The two natural closers land on a boundary by definition. When a **cap** forces the close
instead, the block rewinds to its last sentence or clause boundary and the leftover words
open the next block. Without that rewind the cap cuts at whatever word happened to fit, and
produces fragments like `Your mind never scores your`, which Japanese, Korean and Hindi
cannot translate at all because they reorder the clause.

Timings come straight off the words: start is the first word's onset, end is the last
word's offset held **300ms** longer for readability, clamped to leave a **80ms** gap before
the next block and a **1.0s** minimum on screen.

### Expected shape

A 11 to 12 minute episode gives **165 to 190 blocks, mean 3.5 to 4.0s, max under 7s**, with
under 15 percent of blocks ending on neither a sentence nor a clause. Projects 1, 11 and 12
all land in that band. Well outside it means the narration pace changed or a flag was wrong.

Only pass the tuning flags (`--max-dur`, `--min-dur`, `--sentence-min`, `--gap`,
`--max-chars`) if the user asks for longer or shorter subtitles. The defaults are
calibrated against this channel's pace; read `references/memory.md` before changing one.

## Step 2 - Read en.srt before translating

Open the file. Read the first three blocks, three from the middle, and the last two.
Confirm each one reads as a unit somebody could translate on its own. This is the only
stage where a bad cut is cheap to fix. Every later stage multiplies it by 24.

If the cut is wrong, re-run Step 1 with adjusted flags. Do not hand-edit `en.srt`, and
never hand-edit `blocks.json`. They must stay derived from the audio.

## Step 3 - Translate, one subagent per language

24 languages of 176 blocks is roughly a quarter of a million characters. **Written inline
by one agent that is two hours of wall clock**, measured on project 12, and every one of
those characters also lands in your context. Both problems have the same fix: give each
language its own agent.

Spawn **one subagent per non-English language, all in a single message** so they actually
run at once. Each one reads `blocks.json`, translates, writes its own JSON, and assembles
its own `.srt`. The 176 translations never pass through your context; you get back one line.

Send every agent this task, substituting the project path, language, and code:

```
Translate subtitles into <language> for a TossExplains video essay about psychology.

1. Read <P>/outputs/captions/blocks.json. It holds a "blocks" array; each entry has a
   "text" field. Those texts, in order, are what you translate. Ignore every other field.

2. The blocks are consecutive subtitles of one continuous narration, so read all of them
   before you start and keep pronouns, tense, register, and terminology consistent across
   the whole set. The narration is conversational second person, spoken aloud, not written
   prose. Do not lift it into a formal or literary register.

   - Never use the em dash character. Use a comma, a hyphen, or a period.
   - Keep every number as a numeral and every unit exactly as written. Never convert
     miles to kilometres or rewrite a figure.
   - Keep researcher names, place names, and study titles in Latin script if that is
     normal for <language>. Everything else must be translated; a stray English word
     inside a non-Latin script is a defect.
   - Each string stands alone on screen for a few seconds. Keep it readable at that length.

3. Write <OUT>/<code>.json with exactly this shape, UTF-8:
   {"code": "<code>", "language": "<language>", "translations": [...]}
   The array must have exactly <count> entries, one per block, in the same order. Do not
   add, remove, reorder, merge, or split entries. Count them before writing.

4. Run, from the repo root:
   python3 tools/captions-srt.py assemble \
     --blocks <P>/outputs/captions/blocks.json \
     --translation <OUT>/<code>.json \
     --out <P>/outputs/captions

   It refuses a wrong count, an empty string, or an em dash. If it refuses, fix your JSON
   and run it again. Do not pad or trim to make the count fit.

5. Reply with one line only: the code, the block count, and whether assemble succeeded.
   Do not include the translations in your reply.
```

`<OUT>` is a scratch directory outside the project. The `.json` files are working files, not
artifacts; only the `.srt` belongs under `outputs/captions/`.

Concurrent agents are safe here: they read one shared file and each writes a different one.

**English is never sent to a translator.** `en.srt` is already written.

If an agent fails or returns a count mismatch, re-spawn that one language. A failure costs
one language, never the run.

### If the host has no subagent mechanism

Codex reads this same file. Where subagents are unavailable, do the translations inline,
writing and assembling each language before starting the next so a crash costs one language.
Say up front that this will take about two hours for the full set, and do not claim the
languages are running concurrently. One agent writing 24 translations is serial no matter
how many are packed into a single reply.

### Translation rules

- **Never localise a unit or a number that appears as on-screen text.** A Spanish pass once
  helpfully converted 41 and 32 miles per hour to 66 and 51 km/h, while the scene prompts
  rendered the numerals **41** and **32** on screen. The caption contradicted the image it
  sat under. Check the Text column of `prompts/visual-plan.md` before translating any
  figure, and keep the numerals and units the visuals carry.
- **Keep the register conversational.** This narration talks to one person. Do not lift it
  into formal or literary register, which is the default failure in Japanese, Korean, Hindi
  and Marathi.
- **Keep proper nouns, study names and researcher names in Latin script** inside non-Latin
  languages. That is correct, and it is the one legitimate reason a Latin run appears in a
  CJK or Devanagari file. Everything else Latin in those files is a leak.
- **No em dash**, in any language. House rules. The assemble stage refuses the file.

## Step 4 - Assemble

Each translating agent runs this itself as its last step. Run it yourself only to repair a
language whose agent failed, or when working without subagents:

```bash
python3 tools/captions-srt.py assemble \
  --blocks      "$P"/outputs/captions/blocks.json \
  --translation /path/to/<code>.json \
  --out         "$P"/outputs/captions
```

The translated text is poured into the English timing spine, so the sequence numbers and
timestamps are identical to `en.srt` by construction. The stage refuses a translation whose
count does not match the block count, an empty string, or an em dash. On a count mismatch,
re-translate that language. Never pad, trim, merge, or split to make the count fit.

Never trust an agent's report that it succeeded. Step 5 is what establishes that, and it
reads the files on disk.

## Step 5 - Check

```bash
python3 tools/captions-srt.py check --dir "$P"/outputs/captions
```

Every file is compared against `en.srt` for block count, sequence numbers and timestamps,
and scanned for empty blocks, verbatim repeats of the previous block, overlaps, zero-length
blocks, and em dashes. Files in a non-Latin script are also scanned for runs of Latin
letters, which is the one defect that passes every structural check: Japanese block 72 once
shipped as `ロダガー people と長年暮らし` with an English word inside it, and count, timing,
emptiness and duplicate checks all read clean.

A count check alone does not catch content drift. `vi.srt` once drifted one block against
`en.srt` for the first half of a file, compounding until a block carried the video's closing
line, and the block count matched perfectly the whole way. The check diffs block by block
for exactly that reason.

**The check must exit clean before reporting done.** It reports which of the 25 languages
are not yet written, so use it to confirm the set is complete as well as correct.

Then read blocks 1, a quarter in, half in, three quarters in, and the last one across every
file side by side. The check proves the containers line up. Only a read proves the right
sentence is inside the right container.

## Step 6 - Report and hand off

Give the block count, the total duration, the languages written, and the check result.
Then:

> Captions saved to `<path>/outputs/captions/`, timed against `audios/full.mp3`.
>
> Next: **`/metadata`** if the video is not packaged yet, or upload the tracks with
> **`/youtube`**.

## Never

- Never build captions from `transcript.md` when `words.json` exists. Line-level timings
  cannot cut a block, and its milliseconds do not change that.
- Never hand-write or hand-edit an `.srt` or `blocks.json`. Run the tool.
- Never compute SRT timestamps by hand. Both defects this skill guards against, the
  breached duration cap and the drifted `vi.srt`, were hand arithmetic.
- Never translate a language without assembling it through `blocks.json`. Timings must be
  identical by construction, not by luck.
- Never ship a subset of the 25 languages unless the user named the subset this turn.
- Never localise a number or unit that the visual plan renders as on-screen text.
- Never write the translations inline when subagents are available. It is serial, it costs
  about two hours, and it fills your context with text you never need to read.
- Never let a translating agent return its translations to you. It writes the file.
- Never report done before `check` exits clean.

## Self-improvement

Read `references/memory.md` at the start of every run. After the user reports a quality
issue with a specific language or a specific cut, append the durable lesson there. Record
what was observably wrong and the rule that prevents it. Do not add generic LLM temperature
notes or system prompt experiments.
