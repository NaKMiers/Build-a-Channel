# transcript - memory

Self-improving notes for audio to timestamps. Single canonical copy.

## Known-good settings

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
  mixed *sample rates*, which matched across all three parts, while the mixed *bitrates*
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
