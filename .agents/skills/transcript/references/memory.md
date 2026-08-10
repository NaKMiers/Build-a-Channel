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
