# 04 Voiceover

Video: `Why Buy 1 Get 1 Free Beats 50% Off`

Status: `section voiceover in progress`

Source skill: `voiceover`

Source file:

- `02-script.md`

## Voice Direction

- Default final voice: `David23 / am_eric`
- Current generation voice: `am_eric`
- Speed: `0.82` (Section 1; lowered from 0.84 by request for learner clarity)
- Language: `en-us`
- Tone: young (~23), clear, bright, lightly dry, learner-friendly
- Voice status: `final channel voice generating successfully on this machine` (Python path prepend required)

## Section Voiceover Index

|   # | Section | Status | Voice | Speed | Duration | Audio file | Notes |
| --: | ------- | ------ | ----- | ----: | -------: | ---------- | ----- |
| 1 | Hook: You're The Rabbit | final section voice generated | David23 / am_eric | 0.82 | 23.019s | `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.82.mp3` | rev 2 cheeky hook @ 0.82 |
| 2 | Same To You, Not To Them | not generated | — | — | — | — | — |
| 3 | The Receipt Knows | not generated | — | — | — | — | — |
| 4 | The Magic Word | not generated | — | — | — | — | — |
| 5 | The Price Never Drops | not generated | — | — | — | — | — |
| 6 | When The Store Loses | not generated | — | — | — | — | — |
| 7 | Payoff: Free Cuts Your Judgment | not generated | — | — | — | — | — |

## Section Details

### Section 1: Hook: You're The Rabbit

- Status: `final section voice generated`
- Section folder: `voiceover/section-01-hook/`
- Clean script: `voiceover/section-01-hook/section-01-hook-script.txt`
- Marked script: `voiceover/section-01-hook/section-01-hook-marked-script.md`
- TTS input: `voiceover/section-01-hook/tts-inputs/section-01-hook-tts.txt`
- Audio file: `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.82.mp3`
- Duration: `23.019s` (speed 0.82; was 22.613s @ 0.84)
- Voice: `David23 / am_eric`
- Speed: `0.82`
- Language: `en-us`
- Tool: `npx hyperframes@0.6.76 tts`
- Use: final approved channel voice
- Notes: rev 2 shock-plus-joke hook ("...and you are the rabbit"). Pacing shaped only in the tts-input via `...`, `.`, and `. .`. Matches `02-script.md` rev 2.

## Stale / Regeneration Notes

- Section 1 audio matches `02-script.md` rev 2 (shorter, funnier, cheeky hook). Regenerated 27.157s → 22.613s.
- Sections 2-7 in `02-script.md` were also rewritten in rev 2 (shorter/funnier); they were never generated, so nothing to regenerate yet — generate them fresh from rev 2 wording.
- If `02-script.md` is edited again, regenerate the affected section(s) and reset their index status.

## Next Step Boundary

Next workflow step: `Visual plan`

Do not continue into visual plan, render, review, upload, or learning until the user asks for the next skill or explicitly requests that step.
