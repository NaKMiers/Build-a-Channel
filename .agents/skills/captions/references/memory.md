# captions - memory

Durable lessons for the captions skill. Keep this file source-independent.

## Standing rules

- Timing comes from `transcribes/words.json`, never from `transcript.md`. The transcript
  is quantised to whole seconds and is up to a second early on every block.
- `transcript.md` is still required: it proves `words.json` is the same take, and it is the
  context a translator reads.
- `English.srt` is built first and written before any translation starts.
- Every other language is poured into `blocks.json`, the English timing spine, so all files
  are frame-identical by construction.
- All 25 languages, every time, unless the user names a subset in that turn.
- Output directory is `outputs/captions/`, created if absent.
- `check` must exit clean before reporting done.
- Since 2026-09-06, `.srt` files are named by full language name (`English.srt`,
  `Vietnamese.srt`, `Chinese Simplified.srt`, ...), not by BCP-47 code. The code still
  exists inside `tools/captions-srt.py` (`LANGUAGES`, `NAMES`, `CODES`) for script
  classification and for the working `<code>.json` translation payloads, and it is the tag
  to pick in the YouTube Studio UI on upload. Only the on-disk `.srt` stem changed.

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

### 2026-09-06, project 13, a given name at the start of a sentence is not auto-allowed

Issue: `check` failed 12 of 13 non-Latin files on the first run, all four hits the same
class: `Anandi Mani`, `Anuj Shah`, `James Woodburn`, `Nicolas Peterson`. Every surname
passed (mid-sentence capitals are recognised fine); every given name failed, because each
one opens the sentence right after the previous one's closing period, and `proper_nouns`
treats a sentence-opening capital as an ordinary word, not a name. The translations were
correct: every translator kept the full name in Latin script, exactly as instructed.

Fix applied this run: `--allow Anandi,Anuj,James,Nicolas` on the check command. This is
the documented escape hatch, not a new mechanism.

**Generalisable, sharpening the project 12 lesson: the auto-derived allowlist has a
structural blind spot at sentence starts**, because it needs the *previous* token to tell
a name from an opener and the first mention of any person is usually right after a period.
Expect this on every project that introduces a researcher by full name, and check for it
before assuming a real leak: if the flagged word is a given name immediately followed by
a capitalised surname that already passed, it is this gap, not a translator's mistake.

### 2026-09-06, all projects, filenames switched from BCP-47 code to language name

Change: the owner asked for `outputs/captions/*.srt` to be named by full language name
(`English.srt`, `Vietnamese.srt`) instead of code (`en.srt`, `vi.srt`), so the folder reads
without decoding a tag, and asked for the skill and tool to produce that going forward.

`tools/captions-srt.py` was updated: `build` writes `English.srt`, `assemble` looks up
`NAMES[code]` to name its output file, and `check` reverse-looks-up a filename to a code
via the new `CODES` map for script classification (`NON_LATIN` membership) and falls back
to reporting an unrecognised filename outright rather than silently skipping its checks.
The working translation payloads (`<code>.json`, written by each translating subagent
before it runs `assemble`) are untouched, still keyed by code; only the final `.srt` stem
changed.

Project 13's 25 files were renamed in place and re-verified with `check`, clean.

Tradeoff flagged to the owner before making the change: nothing in this repo automates
caption *upload* to YouTube (`tools/youtube-api.py` only has a `transcript` subcommand,
which downloads), so a human always picks the language explicitly in YouTube Studio's
upload UI regardless of local filename. The BCP-47-as-stem convention this replaces was
therefore a documented preference, not a load-bearing dependency. If an automated caption
upload is ever wired up, check whether it expects the code as the filename and reintroduce
a lookup there rather than reverting this.

### 2026-09-09, project 14, the "mid-sentence" build stat overstates real bad cuts

Issue: `build` printed "mid-sentence 61 blocks (38%), split by the caps" for project 14
(159 blocks, 11:08 total), far above the "under 15 percent ending on neither a sentence
nor a clause" benchmark in the Expected shape section. That reads like the run is well
outside the calibrated band and the flags need retuning.

It is not what it looks like. The printed stat (`unfinished` in `cmd_build`) counts every
block whose last word fails `tsfmt.ends_sentence`, which includes blocks that correctly
end on a clause boundary (a comma) via `best_split`'s fallback, the second-best and
intentional cut point, not a defect. Computing the actual benchmark metric directly from
`blocks.json` (last word ends neither `ends_sentence` nor `ends_clause`) gave 11%, inside
band. The block count (159, slightly under the 165-190 typical range) and mean/max
durations were also in band; the video is just a little shorter than projects 1, 11, 12.

Fix: nothing to the tool, this is a reading error, not a code defect. Before concluding a
run needs retuned flags because the printed mid-sentence percentage looks high, recompute
the neither-sentence-nor-clause rate from `blocks.json` (last word passes neither
`tsfmt.ends_sentence` nor `ends_clause`) and compare that number to the benchmark, not the
raw print.

**Generalisable: a printed diagnostic and a documented benchmark can silently measure
different things.** The printed line is named the same thing the skill's Expected shape
section discusses, but the sets differ, so the fix is not to change the number the tool
reports (that would be a bigger diff for a real quality signal), it is to know which
metric the benchmark actually refers to before reacting to the print.

### 2026-09-12, project 15, a name with internal punctuation can never enter the allowlist

Issue: `check` failed 10 of the 10 non-Latin files on the first run, every one on the same
three words: `Nicholas`, `Lorna`, `hoansi`. Two are the known sentence-start gap. The third
is a new cause.

- `Nicholas` and `Lorna` are the **project 13 blind spot**, unchanged: both are given names
  opening a sentence right after the previous one's period ("It is simply not tuned. Nicholas
  Epley and...", "Lorna Marshall spent years..."), so `proper_nouns` reads them as sentence
  openers rather than names. `Epley`, `Juliana`, `Schroeder` and `Marshall` all passed, which
  is the signature project 13 says to look for.
- **`hoansi` is new, and it is not a sentence-start problem at all.** The English says
  `Ju/'hoansi`, mid-sentence, so `proper_nouns` does add it, but it adds the **whole token**
  `ju/'hoansi`. `LATIN_RUN` scanning the translated file matches maximal runs of Latin
  **letters**, so it finds `Ju` and `hoansi` as two separate runs, and `hoansi` alone is in no
  allowlist. **A proper noun containing any non-letter character can therefore never match**,
  because the allowlist stores one shape and the scanner produces another. `proper_nouns`
  already splits on hyphens for exactly this reason; apostrophes and slashes were not covered.

**Generalisable, third refinement of the project 12 rule:** deriving the allowlist from the
source is right, but the derived entries must be tokenised the same way the scanner tokenises
the target. Splitting an allowlist entry on every non-letter and adding each fragment would
close this without a new mechanism. Until then, expect `--allow` to be needed for any name
carrying a click letter, an apostrophe, or a slash, which for this channel means every
ethnonym it has used: `Ju/'hoansi` here, and the same shape would hit `!Kung` or `Hadza-!ko`.

Fix applied this run: `--allow Nicholas,Lorna,hoansi`, the documented escape hatch, after
confirming all three by reading the English source blocks. Re-check: 25 files clean, all in
sync with `English.srt`.

Run shape: 156 blocks, mean 3.8s, min 1.7s, max 6.2s, total 10:30, 14.8 blocks per minute.
Block count is under the 165 to 190 band in the Expected shape section purely because the
video is 10:30 rather than 11 to 12 minutes; the per-minute rate is mid-band. The printed
"mid-sentence 33%" is the project 14 overstatement again, and the real neither-sentence-nor-
clause rate computed from `blocks.json` is **10%**, inside the under-15 benchmark. Second run
in a row that stat has looked alarming and been fine, so **compute the real metric before
reaching for a flag.**

**Concurrency ceiling hit for the first time.** The host caps concurrent subagents at 20, so
12 of the 24 launched, then 8, then the last 4 were refused outright with
`Concurrent subagent limit reached`. The fix is not to retry: launch what fits, then launch
each remaining language as a completion notification frees a slot. Total wall clock was about
13 minutes for all 24, against the roughly two hours the skill quotes for the inline path.
**The skill says "all in a single message"; with more than 20 languages that is now the first
batch plus a drip.** Worth stating in `SKILL.md` so the refusal is not read as a failure.

## Future entries

After a reported quality issue, append:

```markdown
### YYYY-MM-DD, project N, <language or stage>

Issue: <observable problem>

Fix: <durable lesson, and where it is now enforced>
```
