# transcript - memory

Self-improving notes for audio to timestamps. Single canonical copy.

## Known-good settings

- Project 1's `transcript.txt` is 255 lines for a roughly 12 minute read, which is the
  default cut. Alternate cuts at `--max-dur 3` and `--max-dur 5` were also produced and kept.
- Always pass `--save-json`. Project 1 has `transcribes/words.json`, so its transcript can be
  re-cut at any granularity for free.

## Lessons

- **Project 1 contains a duplicate timestamp**: `[3:24]` appears twice. The workaround is
  recorded in its `image-prompts.md` header, save the second image as `[3:25]` so it does not
  overwrite the first. Always check for duplicates and always pass the workaround downstream,
  because timestamps become scene file names.
- Forced alignment is worth the roughly $0.08. The Groq path is cheaper but the words drift
  from the written script, and every image prompt is derived from the wording.
