# transcript - memory

Self-improving notes for audio to timestamps. Single canonical copy.

## Known-good settings

- **V2 dense profile, tested 2026-08-03:** `--pause 0.24 --max-dur 3.2 --min-words 2` on
  Project 1's cached 11m30s word timings produced 316 cues, median 1.8 seconds, 27.5 generated
  cues per minute, and two one-word cues. Both one-word cues were intentional verdicts: `No.`
  and `Hunger.` The V2 visual plan adds CapCut-only events to reach 28 to 32 visual states per
  minute. Nearby tests produced 327 cues at pause 0.22 and 317 at pause 0.25, with no reduction
  in one-word cues, so 0.24 was selected.

- Project 1's `transcript.txt` is 255 lines for a roughly 12 minute read, which is the
  default cut. Alternate cuts at `--max-dur 3` and `--max-dur 5` were also produced and kept.
- Always pass `--save-json`. Project 1 has `transcribes/words.json`, so its transcript can be
  re-cut at any granularity for free.

- **Project 3's transcript is 267 lines**, median 3s per line, over 12m07.2s of combined
  audio, aligned per part and merged with `--offsets`. Last cue `[12:04]`, about 3s of
  trailing silence after it, which is normal. **`[8:26]` appears twice**, at the part 2 to
  part 3 seam: "Permanent." then "Fully cross-referenced." `[8:27]` is unused, so the
  `scenes` header must say to save the second image as `[8:27]`.
- **Project 3 is a 3 part recording**: 4m45.8s, 3m42.4s, 3m39.0s, 12m07.2s combined. The
  script's part boundaries are the runs of blank lines in
  `script_why_you_are_a_different_person.md`, splitting it 852 / 645 / 661 words. That
  works out to 2.98, 2.90, and 3.02 words per second, which is the check that confirms the
  split matches the audio before paying for alignment. **2.9 to 3.1 wps is this narrator's
  range.** A part that falls outside it means the script was split in the wrong place.

## Lessons

- **Project 1 contains a duplicate timestamp**: `[3:24]` appears twice. The workaround is
  recorded in its `image-prompts.md` header, save the second image as `[3:25]` so it does not
  overwrite the first. Always check for duplicates and always pass the workaround downstream,
  because timestamps become scene file names.
- Forced alignment is worth the roughly $0.08. The Groq path is cheaper but the words drift
  from the written script, and every image prompt is derived from the wording.
- **A multi-part recording gets combined into `audios/full.mp3` before anything is
  transcribed**, via `tools/combine-audio.py`. That is what the editor scrubs against, so
  it is the timeline the transcript has to describe. No ffmpeg on this machine, and none
  needed: the tool concatenates MPEG frames and strips the tags itself.
- **A concatenated MP3 can hold every frame and still report the wrong duration.**
  Project 3's parts were exported at 256, 128, and 128 kbps. Concatenated, that is a VBR
  stream, and part 1's inherited LAME `Info` header described part 1 only. Players fell
  back to extrapolating the first frame's bitrate across all 16.2 MB and showed **8m28s
  for a 12m07s file** (16,207,201 x 8 / 256,000 = 506s). Nothing was missing: frame data
  was byte-identical to the parts and the frame walk gave 727.197s exactly.
  `combine-audio.py` now rewrites the Xing header with the true frame count plus a seek
  table, prints what a player will report, and exits non-zero rather than write a file
  whose header disagrees with its frames.
  **The lesson generalises: check the thing that actually breaks.** The tool warned on
  mixed _sample rates_, which matched across all three parts, while the mixed _bitrates_
  that caused the bug went unmentioned. A passing check on the wrong property reads as
  reassurance.
  Xing's seek table has only 100 entries, so seeks land within about 1% of the duration,
  measured at worst 3.4s on this file. Fine for scrubbing, and the only way to do better
  is re-exporting every part at one bitrate.
- **Offset parts by measured duration, not by their last spoken word.** The original
  multi-part path chained each part onto the previous part's last cue, so any trailing
  silence pulled every later timestamp early. Both the single-call path and
  `--from-json ... --offsets` now use real frame-counted durations.
- **Per-part alignment runs are the multi-part default.** One failed part is retried
  alone instead of re-paying for all of them, uploads stay under Groq's 25MB cap, and the
  merge is a free `--from-json` pass. Split the script into parts in a scratch directory,
  not into the project, and verify the pieces rejoin with no words dropped.
- **Verify the split script still matches the file on disk right before aligning.** During
  project 3 the script was edited mid-session and gained `wa    s` for `was` on line 81,
  four spaces inside one word. The pre-split copies were clean so the alignment was
  correct, but `wc -w` on the script then disagreed with the word count in `words.json` by
  one. Word-diff the script against the split parts, and diff the finished transcript's
  text against the script; both must be word-for-word identical. A stray space inside a
  word is invisible on screen and would silently become two cues on the next re-align.
- **The ElevenLabs key in `.env` was refused on 2026-07-29** with
  `detected_unusual_activity`, free tier disabled, "triggered by using a proxy or VPN, or
  by creating multiple free accounts". A key being present is not a working key. There is
  no `GROQ_API_KEY` in `.env` and no local ASR installed, so with ElevenLabs blocked this
  stage cannot run at all. Report that and stop, do not silently switch engines.
- **A second, different ElevenLabs refusal on 2026-08-04**: HTTP 401
  `missing_permissions`, "The API key you used is missing the permission
  forced_alignment to execute this operation." The key authenticates fine, it just is not
  scoped for the forced-alignment endpoint, which is a workspace API-key permission
  toggle rather than an account status. **So the `grep -q ELEVENLABS_API_KEY .env`
  precondition has now failed to predict a working call twice, in two unrelated ways.**
  Treat that grep as a cheap "is it even worth trying" gate, never as evidence the call
  will succeed, and expect the real verdict only from the first API response. The fix here
  is the user's to make in the ElevenLabs dashboard, not anything the pipeline can route
  around: still no `GROQ_API_KEY`, so there is no second engine to fall back to even if
  falling back were allowed.
- **The retry minutes later hit a third refusal, also HTTP 401**: `quota_exceeded`, "You
  have 24 credits remaining, while 735 credits are required for this request", on a free
  tier at 9,976 of 10,000 credits with `allowed_to_extend_character_limit: false` and a
  reset 24 days out. **Two different failures wearing the same 401 status, so read
  `detail.code`, never the HTTP code.** `missing_permissions` is a key-scope toggle,
  `quota_exceeded` is a billing state, and the earlier `detected_unusual_activity` is an
  account ban; the fix differs each time and only the body says which.
- **Forced alignment and ElevenLabs TTS spend the same monthly credit pool.** An 11m01.7s
  alignment costs 735 credits, so the free tier's 10,000 is about 13 alignments a month if
  nothing else touches it. If the narration itself is TTS-generated on this account,
  generating an episode's voiceover and aligning it compete for one budget, and the
  alignment is the one that starves because it runs second. **Check remaining quota against
  the roughly 735 credit cost, not merely that a key exists, when a run has to succeed.**
  `GET /v1/user/subscription` with the `xi-api-key` header returns `character_count`,
  `character_limit`, and `next_character_count_reset_unix` for free, which turns a bare
  `quota_exceeded` into a date and a decision.

## Project 6 (2026-08-03) - align `full.mp3` in one call when the script has no part markers

3 parts at 256 kbps: 4m46.7s, 4m20.7s, 2m30.5s, combined 11m37.9s, header and frames agreeing.
303 cues, median 1.9s, last cue `[11:34]`, no duplicate timestamps, transcript text word-for-word
identical to the script at 1891 words. Two one-word cues, `No.` and `Maybe.`, both intentional
from "This video? No. That message? Maybe." Right on the V2 profile's predicted shape.

**Aligned `audios/full.mp3` against the whole script in a single ElevenLabs call rather than per
part, because this script has no part boundary to find.** `script_why_you_feel_more_tired.md` is
single-blank-line separated throughout, so there is no run of blank lines marking where the
recording stopped, and the words-per-second check could not pick a split: proportional word counts
wanted boundaries at cum 777 and 1483, and the nearest paragraph ends gave a 10 percent wps spread
whichever pair was chosen (2.65 / 2.85 / 2.58 at 760+743+388, 2.65 / 2.65 / 2.92 at 760+692+439).
A 10 percent spread is exactly the condition the skill warns about, and a mismatched split aligns
without raising an error.

Per-part alignment buys retry granularity and stays under Groq's 25MB cap. Neither is a
correctness argument, and ElevenLabs forced alignment has no size guard in
`audio-to-timestamps.py`, only Groq does, so a 22.3 MB `full.mp3` uploads fine. **When the split
point is a guess, one call on the combined file is the safer trade.** No `--offsets` pass is
needed either, since the timeline is already the combined one. Both seams came back continuous,
cues at `[4:46]` and `[9:05]` straddling the 4m46.7s and 9m07.4s joins with no gap over 4s
anywhere in the file, which is the check that confirms no part was dropped.

**This narrator reads V2 scripts at about 2.71 wps, not 2.98.** 1891 words over 697.9s. Project 3
established 2.9 to 3.1 from a V1 script. Do not treat 2.7 as a failed split on its own: check
whether the parts agree with each other, not whether they hit the older number.

## Project 8 (2026-08-12) - a wps anomaly that turned out to be a fast read, and how to tell

3 parts at 256 kbps: 4m51.9s, 3m27.6s, 1m24.5s, combined **9m44.0s**, header and frames agreeing
(Xing reports 9m43.9s, a rounding difference, not a mismatch). Single ElevenLabs call on
`full.mp3` against the whole script, same as projects 5 and 6, because
`script_why_your_new_phone_looks_cheap.md` is single-blank-line separated with no run of blank
lines marking where the recording stopped.

**268 cues**, median 1.8s, last cue `[9:41]` against 583.6s of aligned speech, no duplicate
timestamps, no malformed lines, transcript text word-for-word identical to the script at 1873
words. 27.5 cues per minute, exactly the V2 profile's predicted rate.

### 3.21 wps breaks the established band, and it was still correct

1873 words over 584.0s is **3.21 wps**. Projects 5 and 6 put this narrator at 2.71 to 2.87, and
the seven published videos average 2.81. At 2.80 the script should have run 11.1 minutes, so the
recording looked about 230 words short, and the skill's own warning is that a mismatched script
aligns without raising an error.

It was a faster read. Nothing was missing. **The check that proves it is a rolling word-rate
window over `words.json`, and it costs nothing:**

```bash
python3 - <<'PY'
import json,bisect
ws=[x for x in json.load(open("<P>/transcribes/words.json"))["words"] if x.get("end") is not None]
starts=[x["start"] for x in ws]; win=30.0; rates=[]; worst=(0,0)
for t in range(0,int(ws[-1]["end"])-int(win),5):
    r=(bisect.bisect_left(starts,t+win)-bisect.bisect_left(starts,t))/win
    rates.append(r); worst=max(worst,(r,t))
rates.sort(); print(f"median {rates[len(rates)//2]:.2f} max {worst[0]:.2f} at {worst[1]}s")
PY
```

Here it returned median 3.17 and max 4.03, the max sitting at 0m05s inside the deliberately fast
hook. **A uniform rate means a uniform read.** Missing content produces one of two signatures and
neither appeared: a local rate spike far above the file median where the aligner crams orphaned
words, or a silence much longer than the read's natural pauses. The largest silence in the whole
file was 1.5 seconds.

Transferable rule: **a whole-file wps figure outside the narrator's band is a question, not a
verdict.** Compare the rolling median against the whole-file figure. If they agree, the narrator
changed pace; if the rolling max spikes somewhere, that timestamp is where the audio and script
part company. This can run before alignment only if a cache already exists, so in practice it is
the first thing to run after the call, before reporting success.

The band itself now spans 2.71 to 3.21 across five measured recordings. Treat it as read-dependent
rather than fixed, and do not reject a split on the older narrower numbers alone.

### Duration is below the channel-dna 10 to 14 minute spec

9m44.0s against a rule that says 10 to 14 minutes. Flagged to the user rather than corrected: the
retention analysis on 2026-08-11 pointed toward shorter videos, since average view duration sits
near 2m10s regardless of length, so a shorter file raises average view percentage for the same
watch time. **If short videos become the norm, `channel-dna.md`'s duration line needs updating**
rather than every project quietly violating it.

## Project 9 (2026-08-21) - single-call align, uniform read, and a words.json shape gotcha

3 parts at 256 kbps (uniform, so no VBR header risk): 4m29.6s, 3m45.2s, 1m52.0s, combined
**10m06.9s**, Xing header agreeing with the frames. Single ElevenLabs forced-alignment call on
`audios/full.mp3` against the whole script, same as projects 5, 6 and 8, because
`script_advice_you_never_take.md` is single-blank-line separated throughout with no run of blank
lines marking where the recording stopped.

**273 cues**, median 1.8s, last cue `[10:04]` against 606.9s of audio, no duplicate timestamps,
no malformed lines, transcript text word-for-word identical to the script at 1875 words. About
27 cues per minute, right on the V2 profile's shape. Duration 10m06.9s is inside the channel-dna
10 to 14 minute spec (project 8 at 9m44s was below it).

Whole-file rate 1875 / 606.9 = **3.09 wps**, and the rolling 30s window returned median 3.10, max
3.70 at 575s, largest silence 1.6s at 119s. Rolling median equals the whole-file figure, so the
read was uniform and nothing was dropped. This narrator's measured band is now 2.71 to 3.21 across
six recordings; 3.09 is unremarkable.

Quota was checked before spending via `GET /v1/user/subscription`: free tier, 5811 of 10000 used,
4189 remaining, plenty for the ~600 credit call. The key authenticated and was in-scope on the
first try this time, unlike projects 4 and 5.

### GOTCHA: words.json is a top-level LIST here, not a dict with a "words" key

The rolling word-rate snippet in the project 8 note opens with `json.load(open(...))["words"]`,
which assumes a dict. `audio-to-timestamps.py --save-json` on this run wrote a **bare JSON list**
of `{"start","end","text"}` objects, so `["words"]` raised `TypeError: list indices must be
integers`. Make the snippet shape-tolerant:

```python
data=json.load(open(f"{P}/transcribes/words.json"))
ws=[x for x in (data if isinstance(data,list) else data.get("words",data)) if x.get("end") is not None]
```

Do not assume the cache schema. Check `type()` first, or use the tolerant line above.

## Project 10 (2026-08-25) - a part saved to the wrong folder, caught by arithmetic

3 parts at 256 kbps (uniform, no VBR risk): 4m32.0s, 4m45.3s, 2m09.2s, combined **11m26.5s**,
Xing header agreeing with the frames. Single ElevenLabs forced-alignment call on `audios/full.mp3`
against the whole script, same as projects 5, 6, 8 and 9.

**304 cues**, median 1.9s, last cue `[11:25]`, aligned speech ending at 686.2s of 686.5s audio,
transcript text word-for-word identical to the script at 2070 words, no malformed lines. 26.6 cues
per minute, on the V2 profile's shape. Duration is inside the channel-dna 10 to 14 minute spec.

Whole-file rate 2070 / 686.5 = **3.02 wps**; rolling 30s window returned median 3.00, max 3.77 at
210s, largest silence 1.3s. Rolling median equals the whole-file figure, so the read was uniform.
Quota checked first: free tier, 2138 of 10000 used, 7862 remaining against a roughly 760 credit
call. Key authenticated and was in scope on the first try.

### THE FIND: part 3 was in `outputs/`, not `audios/`, and had no file extension

`audios/` held only `part-1.mp3` and `part-2.mp3`. A 4.1 MB file named `part-3`, no extension, sat
in `outputs/`. Taking `audios/` at face value would have produced a transcript covering 9m17s of a
11m26s recording, silently missing the entire ending including the end-screen call to action, and
**forced alignment would not have raised an error**, it would have compressed the script's last 400
words into the wrong timestamps.

**The check that caught it costs nothing and should run every time, before any API call:** divide
the script's word count by the measured audio duration and compare against the narrator's band.

- 2070 words / 557.3s (two parts) = **3.71 wps**, far outside the measured band of 2.71 to 3.21.
- 2070 words / 686.5s (three parts) = **3.02 wps**, mid-band.

`file` confirmed the stray was MPEG layer III at 256 kbps 44.1 kHz mono, the identical encode
profile to the other two parts, and its mtime sat three minutes after part 2. The file was moved to
`audios/part-3.mp3` and the run proceeded normally.

Transferable rules:

- **Do not trust `audios/` to be complete. Verify it with the wps arithmetic.** The skill already
  says a mismatched split aligns without error; the same is true of a missing part, and a missing
  part is easier to end up with because export dialogs remember the last folder used.
- **Sweep the whole project folder for stray audio before concluding what the parts are**, not just
  `audios/`. `find <P> -type f` plus `file` on anything unrecognised is enough.
- A wps figure far ABOVE the band means audio is missing. A figure far below means the script is
  short of the recording, or a part was duplicated. Project 8 established that a figure moderately
  outside the band can still be a genuine fast read, so confirm with the rolling window; but 3.71
  against a 3.21 ceiling was too far out to be pace.

### Two duplicate timestamps, both with the next second free

`[5:09]` appears twice, "In it," then "only one comparison". `[6:27]` appears twice, "Richard Lee,"
then "who lived for years among the". `[5:10]` and `[6:28]` are both unused, so the `scenes` header
must say to save the second image of each pair as `[5:10]` and `[6:28]` respectively.

## Project 11 (2026-08-28) - textbook clean run, and the first check of a hook prediction against real audio

3 parts at 256 kbps 44.1 kHz mono (uniform, so no VBR header risk): 4m57.5s, 2m10.6s, 4m53.4s,
combined **12m01.5s**, Xing reporting 12m01.4s which is rounding, not a mismatch. Single
ElevenLabs forced-alignment call on `audios/full.mp3` against the whole script, same as projects
5, 6, 8, 9 and 10, because `script_things_that_never_happened.md` has **zero runs of 2+ blank
lines** across its 32 paragraphs, so there is no part boundary to find.

**332 cues**, median 1.7s, last cue `[12:00]`, aligned speech ending at 721.3s of 721.5s audio,
**no duplicate timestamps at all**, no malformed lines, transcript text word-for-word identical to
the script at 2076 words. 27.6 cues per minute against the V2 profile's predicted 27.5. One
one-word cue, `None.`, an intentional verdict from "There was no broken glass in that film. None."
Duration is inside the channel-dna 10 to 14 minute spec.

Pre-flight checks all passed first time, in this order, which is the order worth keeping:

1. **Folder sweep before trusting `audios/`** (the project 10 lesson): `find <P> -type f` showed
   exactly three parts and no stray. Nothing hiding in `outputs/` this time.
2. **wps arithmetic before any API call:** 2076 words / 721.5s = **2.88 wps**, mid-band against
   the measured 2.71 to 3.21. No part missing.
3. **Quota before spending:** free tier, 4830 of 10000 used, 5170 remaining against a roughly 780
   credit call. Key authenticated and was in scope on the first try.
4. **Rolling 30s window after the call:** whole-file 2.88, rolling median 2.90, max 3.60 at 645s,
   largest silence 1.5s at 0m54.2s. Rolling median agrees with the whole-file figure, so the read
   was uniform and nothing was dropped.

The `words.json` cache was again a **bare top-level list**, matching projects 9 and 10. The
shape-tolerant loader is now the only sensible default; do not write `["words"]`.

### The 169 wpm hook estimator is slightly conservative, and that is now measured

Project 11's hook was engineered beat by beat against the 169 wpm figure in
`.agents/skills/script/references/memory.md`. This is the first time those predictions could be
checked against a real recording, and every beat landed **1 to 2 seconds early**:

| Beat | Predicted at 169 wpm | Real audio |
| ---- | -------------------- | ---------- |
| contradiction, "your least reliable one" | 0:03 | **0:01** |
| formal "but" | 0:20 | **0:18** |
| mechanism named, "It is reconstruction" | 0:26 | **0:25** |
| new open question, "which of yours have been rewritten?" | 0:35 | **0:33** |
| beat 4 promise, "By the end you will know" | 0:38 | **0:37** |

Cause is simply that this read came in at 2.88 wps, which is 172.8 wpm against the 169 the
estimator uses. **Treat 169 wpm as a safe upper bound on timing: a beat engineered to land at
second N will land at or slightly before N.** That is the right direction for the error to point,
so do not recalibrate the script skill's figure on one recording. Recheck after another two.

## Project 5 rebuild (2026-08-04) - three key failures before one clean align

The project 5 folder was retopiced to `5-why-do-people-follow-the-crowd` and its cast file
says `Visual style version: V2`, so it takes the V2 dense profile despite the older note that
projects 1 through 5 keep V1 defaults. **Read the project's own cast header for the style
version, do not infer it from the project number.**

3 parts at 256 kbps: 4m49.5s, 5m10.8s, 1m01.3s, combined 11m01.7s, header and frames agreeing.
`audios/full.mp3` and `transcribes/offsets.json` are written and correct.

**293 cues**, median 1.9s, last cue `[10:59]` against 11m01.7s of audio, transcript text
word-for-word identical to the script at 1854 words, no malformed lines. Two one-word cues,
`Trending.` and `You.`, both intentional verdicts. Largest gap anywhere is 5s, and nothing
unusual sits at the 4m49.5s or 10m00.3s part joins, which is the check that no part was dropped.
Right on the V2 profile's shape.

**`[5:15]` appears twice**, "soak it," then "squeeze it, wait,". `[5:16]` and `[5:17]` are
unused, so the `scenes` stage saves the second image as `[5:16]`.

Three consecutive key failures preceded that one clean run, in three unrelated ways: 401
`missing_permissions`, then 401 `quota_exceeded` after the key was re-scoped, then success on a
replacement key. **Nothing was billed on the failures and nothing was hand-written.** Because
`full.mp3` and `offsets.json` survive a failed align, each retry cost exactly one alignment call
and no rework, which is the argument for doing the combine and the arithmetic first and letting
the API call be the last and only expensive step.

Like project 6, `script_why_people_follow_the_crowd.md` is single-blank-line separated
throughout with no run of blank lines marking where the recording stopped. 1854 words over
661.7s is 2.80 wps, in this narrator's V2 band. Proportional boundaries wanted cum 811 and
1682; the nearest paragraph ends are 831 and 1680, giving 831 / 849 / 174 words at 2.87 /
2.73 / 2.84 wps, a 5.1 percent spread. That is much tighter than project 6's rejected 10
percent, and boundary 2 lands 2 words off its prediction, but boundary 1 is still a 20 word
guess, so the single call on `full.mp3` remains the right trade. Every other candidate split
is far worse: the next paragraph end back for boundary 1 gives 16.9 percent, and moving
boundary 2 back gives over 130 percent. **Record the arithmetic even when the split is not
used, so a retry does not redo it.**
