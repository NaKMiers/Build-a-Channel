# captions - memory

Durable lessons for the captions skill. Keep this file source-independent.

## Standing rules

- Timing comes from `transcribes/words.json`, never from `transcript.md`. The transcript
  is quantised to whole seconds and is up to a second early on every block.
- `transcript.md` is still required: it proves `words.json` is the same take, and it is the
  context a translator reads.
- `en.srt` is built first and written before any translation starts.
- Every other language is poured into `blocks.json`, the English timing spine, so all files
  are frame-identical by construction.
- All 25 languages, every time, unless the user names a subset in that turn.
- Output directory is `outputs/captions/`, created if absent.
- `check` must exit clean before reporting done.

## The tool carries the arithmetic

`tools/captions-srt.py` exists because both defects this skill has ever shipped were hand
arithmetic: a duration cap tested after the fact, and a per-block content drift nobody
diffed. The rules below are enforced in code now. Do not re-derive them by hand, and do not
hand-edit `en.srt` or `blocks.json`.

| Lesson                          | Enforced by                            |
| ------------------------------- | -------------------------------------- |
| look-ahead duration cap         | `cut_blocks`, `would_run > max_dur`    |
| cut on a translatable boundary  | `best_split`                           |
| identical timings per language  | `assemble` pours into `blocks.json`    |
| block-by-block sync vs `en.srt` | `check`                                |
| Latin leak in a non-Latin file  | `check`, `LATIN_RUN` over `NON_LATIN`  |
| em dash ban                     | `assemble` and `check`                 |
| stale `words.json`              | `build`, `check_against_transcript`    |

## Calibration

Defaults are `--max-dur 7.0 --min-dur 2.5 --sentence-min 2.0 --gap 0.5 --max-chars 96`,
calibrated on projects 1, 11 and 12. They give **167 to 176 blocks, mean 3.6 to 3.8s, max
under 6.5s**, with 8 to 12 percent of blocks ending on neither a sentence nor a clause.

The character cap, not the duration cap, is what actually closes most blocks at this
narration pace. At 84 characters it fired on 66 of 172 blocks in project 12 and cut at
whatever word happened to fit, leaving 40 percent of blocks ending mid-clause. Raising it to
96 and adding the clause rewind took that to 10 percent. Raising it further to 120 buys
little and puts 120 characters on screen for 4 seconds, which is past comfortable reading
speed.

## Dated entries

### 2026-08-29, project 12, the skill prescribed concurrency it could not reach

Issue: Step 3 said "run the languages concurrently, in batches of up to 6." One agent cannot
run its own generation concurrently. Packing six languages into one reply is still serial,
just with fewer round trips. The full set took **1h53m of wall clock**, effectively all of it
token generation, and every one of the ~250,000 translated characters also went through the
main context.

The mechanical stages were free by comparison: `build` was instant, and 25 `assemble` calls
plus `check` were milliseconds each. **The translation is the entire cost.**

It also got steadily slower down the list, because scripts differ in how they tokenise. Same
176 blocks: `en.srt` 17.4KB, `ja.srt` 20.9KB, `ta.srt` 40.9KB, `ml.srt` 40.7KB. Latin pairs
ran about 4 minutes, the last Indic pair took 30.

Fix: one subagent per language, all spawned in a single message. Each reads `blocks.json`,
writes its own `<code>.json`, runs `assemble` itself, and replies with one line. Wall clock
becomes the slowest single language rather than the sum, and the translations never enter
the parent context.

**Generalisable: "do these concurrently" is not a thing a single agent can follow.** If a
skill wants parallelism it has to name the mechanism that provides it. An instruction with
no mechanism behind it reads as satisfied and quietly does nothing.

Corollary worth keeping: the win is context as much as latency. Work whose output the parent
never needs to read should be done where the parent will not have to hold it.

### 2026-08-29, project 12, the leak scan flagged every correct file

Issue: the Latin-run scan shipped as an unconditional regex, and the first real run failed
all seven non-Latin files at once. Every hit was legitimate: `Baumeister`, `Gottman`,
`Briggs`, `Utku`, `Van Bavel`, and the paper title `Bad Is Stronger Than Good`, which a
Japanese or Hindi subtitle is supposed to keep in Latin script.

**A check that fires on correct output is worse than no check**, because the reviewer
learns to skim past it and the one real leak goes with it.

Fix: `proper_nouns` derives the allowlist from `en.srt` itself. A capital that is not
opening a sentence is a name, so the allowed set is exactly the proper nouns the narration
already contains. On project 12 that is 27 words, and the scan then ran clean on all seven
non-Latin files while still catching an injected `people`. `--allow` remains for a name the
heuristic misses.

**Generalisable: derive the exception list from the source, do not hand-maintain it.** The
legitimate Latin words in a translation can only have come from the English, so the English
is the authority on what is allowed.

### 2026-08-29, project 12, the character cap was cutting blind

Issue: with word-level timings the **character cap**, not the duration cap, became the
dominant block-closer, firing on 66 of 172 blocks and cutting at whatever word happened to
fit. That left 40 percent of blocks ending mid-clause, which is the project 10 defect back
in a new form.

Fix: `best_split`. A cap-forced close rewinds to the last sentence boundary, then the last
clause boundary, before settling for the last word that fit, with a 40 percent floor so the
rewind cannot gut the block. Blocks ending on neither a sentence nor a clause went from 40
percent to 10. Raising the cap alone did not fix it: it only moved which word dangled.

About 10 percent of blocks still end on a dangling word, and those are long clauses with no
internal boundary to rewind to. They are unavoidable; the translator handles them by reading
the neighbouring blocks.

### 2026-08-29, project 12, all 25 languages

176 blocks in every file, mean 3.7s, max 6.2s. Zero sequence or timestamp mismatches against
`en.srt`, zero empty blocks, zero consecutive duplicates, zero overlaps, zero em dashes,
zero Latin leaks. Spot-read blocks 1, 44, 88, 122 and 176 across all 25 side by side.

The narration carries the years 2001, 1998, 1960s and 2017, plus seventeen months, half a
million tweets and twenty percent. All kept as written in every language. This project has
no `prompts/visual-plan.md`, so there was no on-screen Text column to check the figures
against; when one exists, check it.

### 2026-08-29, all projects, timing source

The skill was rebuilt on `words.json`. Before this it parsed `[M:SS]` lines out of
`transcript.md` and hardcoded `,000` for every millisecond field, so every subtitle in every
language started on a whole second. Project 12's first word actually begins at `0.100`; its
first sentence ends at `1.12`. Neither number was reachable from the transcript.

**Generalisable: when a precise source and a rounded derivative of it both sit in the same
folder, check which one the consumer is reading.** The rounded file was easier to parse, and
that was the only reason it had been chosen.

### 2026-08-25, project 10, blocking

Issue: merging until a gap over 2 seconds, capped at 7 seconds, produced 112 blocks that cut
mid-sentence, for example "Your mind never scores your" then "life against your life." The
narration has no silence longer than 1.3 seconds, so the gap rule never fired and the cap
became the only thing closing a block, landing the cut at an arbitrary word.

Japanese, Korean and Hindi reorder the clause, so a fragment like "Your mind never scores
your" cannot be translated at all, and translating it in isolation produces text that cannot
be reassembled.

Fix: prefer sentence boundaries inside the cap. Now generalised further, in `best_split`: a
cap-forced close rewinds to the last sentence boundary, then to the last clause boundary,
before settling for the last word that fit.

**Translate the blocks, never the raw cues.** The transcript's cues are sub-second phrase
fragments cut by the aligner, not sentences.

### 2026-08-28, project 11, blocking cap

Issue: the sentence-boundary fix was applied as written and still produced **18 blocks over
the 7 second cap, up to 9.9 seconds.** Cause: the cap was tested as `dur >= 7000` on the
block as it already stood, so a block sitting at 6.5 seconds still accepted one more 3
second word and landed at 9.5. The cap closed the block after it had already been breached.

Fix: test the cap **against what the block would become**, not what it is.

**Generalisable beyond captions: a ceiling checked after the fact is not a ceiling.** Any
accumulate-until-limit loop must test the candidate state, not the committed state.

### 2026-08-28, project 11, scope

An initial pass shipped only `en` and `vi` as a scope call and **the owner rejected it: they
want every language, every time.** Do not offer a subset. Budget for the full set from the
start; the translation is the whole cost, and the assembler makes each extra language cheap.

### 2026-08-28, project 11, two defects only a targeted scan catches

1. **Unit conversion breaks the on-screen text.** The Spanish pass converted 41 and 32 miles
   per hour into 66 and 51 km/h. The scene prompts render the numerals **41** and **32** as
   on-screen text, so the caption contradicted the image it sat under. **Never localise a
   unit or figure that appears as generated on-screen text.** Check the Text column of
   `prompts/visual-plan.md` before translating a number.
2. **A source-language word can leak into a non-Latin script and pass every structural
   check.** Japanese block 72 came out as `ロダガー people と長年暮らし`. Count, timestamps,
   emptiness and duplicate checks all passed. `check` now runs a Latin-run regex over every
   non-Latin file. Latin-script languages cannot use that guard, so for the Latin set the
   spot-read is the only defence.

### 2026-08-22, project 9, vi

Issue: `vi.srt` had drifted out of sync with `en.srt` for roughly the first half of the file
(blocks 4 to 82): each block's text was offset from the block before it, compounding until
block 82's timestamp carried the video's final line. Blocks 83 to 164 were correct. The file
had never been checked against `en.srt` after writing.

Fix: `assemble` now makes this class of drift unrepresentable, because the text is poured
into a shared spine rather than re-emitted per language. `check` still diffs block by block,
because a silent per-block content drift never shows up as a count mismatch.

## Reading the files

Structural checks prove the containers line up. Only a read proves the right sentence is
inside the right container. Spot-read blocks 1, a quarter in, half in, three quarters in,
and the last, across every language side by side before reporting done.

## Future entries

After a reported quality issue, append:

```markdown
### YYYY-MM-DD, project N, <language or stage>

Issue: <observable problem>

Fix: <durable lesson, and where it is now enforced>
```
