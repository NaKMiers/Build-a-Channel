# captions - memory

Durable translation lessons for the captions skill. Keep this file source-independent.

## Standing rules

- Always parse from `transcribes/transcript.md`, never from the script.
- English SRT is a direct copy, no LLM call needed.
- Translate all other languages in parallel in the same turn.
- Merge consecutive cues with no more than 2 seconds gap into one subtitle block.
- UTF-8 encoding for every file, including CJK languages.
- Output directory is `outputs/captions/`, created if absent.

## Future entries

After a reported quality issue, append:

```markdown
### YYYY-MM-DD, project N, <language>

Issue: <observable problem>

Fix: <durable lesson>
```

### 2026-08-25, project 10, blocking

Issue: the skill's blocking rule as written (merge until a gap over 2 seconds, cap at 7
seconds) produced 112 blocks that cut mid-sentence, for example "Your mind never scores
your" then "life against your life." This narration has no silence longer than 1.3
seconds, so the gap rule never fires and the 7 second cap becomes the only thing that
closes a block, which lands the cut at an arbitrary word.

That is bad for reading and unusable for translation. Japanese, Korean and Hindi reorder
the clause, so a fragment like "Your mind never scores your" cannot be translated at all
without the rest of its sentence, and translating it in isolation produces text that
cannot be reassembled.

Fix: add a preference for sentence boundaries inside the existing cap. Close a block when
the last cue ends on a period, question mark or exclamation mark AND the block already
runs 2.5 seconds or longer. Keep the 7 second cap and the 2 second gap rule as the outer
limits. On this script that gave 146 blocks, mean 4.7 seconds, with only 28 not ending on
a sentence, and those 28 are long sentences the cap genuinely has to split.

**Translate the blocks, never the raw cues.** The transcript's cues are sub-second phrase
fragments cut by the forced aligner, not sentences. Build the blocks first, then translate,
then write every language from the one shared block list so timestamps are identical by
construction rather than by luck.

### 2026-08-25, project 10, all eight languages

The project 9 sync check now runs as code and passed on the first assembly: 146 blocks in
every file, zero sequence or timestamp mismatches against `en.srt`, zero empty texts, zero
consecutive-identical texts, zero overlapping or zero-length blocks, no em dash, UTF-8
throughout. The consecutive-identical count is worth keeping alongside the block-by-block
diff: a translation that silently repeats the previous line is the other shape a content
drift takes, and it passes both a count check and a timestamp check.

Also spot-read blocks 1, 38, 87 and 146 across all eight files side by side before
reporting. The structural check proves alignment of the containers; only a read proves the
right sentence is inside the right container.

### 2026-08-28, project 11, blocking cap

Issue: the project 10 sentence-boundary fix was applied as written and still produced **18
blocks over the 7 second cap, up to 9.9 seconds.** Cause: the cap was tested as
`dur >= 7000` on the block as it already stands, so a block sitting at 6.5 seconds still
accepts one more 3 second cue and lands at 9.5. The cap closed the block after it had
already been breached.

Fix: test the cap **against what the block would become**, not what it is.
`would = ends[i+1] - start; close = ... or would > 7000`. That took 142 blocks at max 9.9s
to **153 blocks, mean 4.6s, max 6.9s**, and zero over the cap. Compare project 10's 146
blocks at mean 4.7s: the shape is the same, and the look-ahead form is strictly the correct
one. Non-sentence blocks went 18 to 30, which is the honest trade, and matches project 10's
28: a tighter cap has to split more long sentences.

Generalisable beyond captions: **a ceiling checked after the fact is not a ceiling.** Any
accumulate-until-limit loop must test the candidate state, not the committed state.

### 2026-08-28, project 11, all eight languages

All eight languages written and sync-checked: en, vi, es, ja, nl, hi, zh, ko. 153 blocks in
every file, zero sequence errors, zero timestamp mismatches against `en.srt`, zero empty
texts, zero consecutive duplicates, zero em dashes, UTF-8 throughout. Spot-read blocks 1, 22,
87, 143 and 153 across all eight side by side.

**An initial pass shipped only en and vi as a scope call and the owner rejected it: they want
all eight, every time.** Do not offer a subset. Budget for eight from the start; the
translation itself is the whole cost, and the assembler makes each extra language cheap.

### Two defects that only a targeted scan catches

1. **Unit conversion breaks the on-screen text.** The Spanish pass helpfully converted 41 and
   32 miles per hour into 66 and 51 km/h. But the scene prompts render the numerals **41** and
   **32** as on-screen text, so the caption would have contradicted the image it sits under.
   **Never localise a unit that appears as generated on-screen text.** Keep miles, keep the
   numerals, keep any figure the visual plan carries in its Text column. Check the plan's Text
   column before translating a number.
2. **A source-language word can leak into a non-Latin script and pass every structural
   check.** Japanese block 72 came out as `ロダガー people と長年暮らし`, with a stray English
   word inside the Japanese. Block count, timestamps, emptiness and duplicate checks all
   passed. The scan that catches it is one regex per CJK and Devanagari file:

   ```python
   leak = sum(len(re.findall(r'[A-Za-z]{3,}', t)) for _, _, t in blocks)   # must be 0
   ```

   Run it for ja, zh, ko and hi on every assembly. Latin-script languages cannot use it, so
   for es, nl and vi the spot-read is the only guard.

### 2026-08-22, project 9, vi

Issue: vi.srt had drifted out of sync with en.srt for roughly the first half of
the file (blocks 4-82): each block's text was offset from the block before it,
compounding until block 82's timestamp carried the video's final line instead
of its own. Blocks 83-164 were correct. Root cause unknown (likely a bad
merge during an earlier generation run), but the file had never been checked
against en.srt after writing.

Fix: after writing all language SRTs, always run a structural sync check
before reporting done: same block count as en.srt, and every block's sequence
number + timestamp pair identical across all language files (only the text
should differ). A silent per-block content drift will not show up as a count
mismatch, so diff block-by-block, not just count totals.
