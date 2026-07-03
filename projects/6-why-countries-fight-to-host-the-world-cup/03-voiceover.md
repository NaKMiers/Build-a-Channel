# 03 Voiceover

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`

Status: `all section voiceovers generated`

Source skill: `voiceover`

Source file:

- `02-script.md` (rev 2, post 3-lens review)

## Voice Direction

- Default final voice: `David23` (`am_eric`)
- Current generation voice: `David23` (`am_eric`) - approved channel voice, no scratch
- Speed: `0.81` (owner-locked for this video after A/B 0.79 -> 0.80 -> 0.81 on Section 1,
  2026-07-02; ALL sections generated at 0.81)
- Language: `en-us`
- Tone: calm person explaining something ridiculous; dry, lightly cheeky
- Voice status: `am_eric available and working on this machine` (Python 3.12 PATH-prepend
  fix applied per skill memory)
- Pacing: approved spacious style in every tts-input (standalone `...` hold lines,
  stacked `...` before reveals/punchlines, `. .` staccato resets, trailing `...` on
  setup phrases). Wording matches `02-script.md` exactly in all sections.

## Section Voiceover Index

|   # | Section | Status | Voice | Speed | Duration | Audio file | Notes |
| --: | ------- | ------ | ----- | ----: | -------: | ---------- | ----- |
| 1 | Hook: The Trophy Prints A Receipt | `generated` | David23 (am_eric) | 0.81 | 35.904s | `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.81.mp3` | owner locked 0.81 here after A/B 0.79/0.80 |
| 2 | Reframe: A Purchase, Not An Investment | `generated` | David23 (am_eric) | 0.81 | 33.728s | `voiceover/section-02-reframe/scratch-audio/section-02-reframe-david23-am_eric-0.81.mp3` | thesis "It is a purchase." isolated with holds |
| 3 | The Promise Machine | `generated` | David23 (am_eric) | 0.81 | 60.779s | `voiceover/section-03-promise-machine/scratch-audio/section-03-promise-machine-david23-am_eric-0.81.mp3` | both math payoffs isolated ("Per. Tourist." / "Two dollars fifty") |
| 4 | FIFA Keeps The Money | `generated` | David23 (am_eric) | 0.81 | 62.101s | `voiceover/section-04-fifa-keeps-the-money/scratch-audio/section-04-fifa-keeps-the-money-david23-am_eric-0.81.mp3` | "FIFA keeps..." staccato trio; Zurich gloss in place |
| 5 | The Three Drains | `generated` | David23 (am_eric) | 0.81 | 55.851s | `voiceover/section-05-three-drains/scratch-audio/section-05-three-drains-david23-am_eric-0.81.mp3` | drain labels spoken slow + isolated |
| 6 | The Morning After | `generated` | David23 (am_eric) | 0.81 | 61.440s | `voiceover/section-06-morning-after/scratch-audio/section-06-morning-after-david23-am_eric-0.81.mp3` | "Full of buses." biggest hold; Enzo deadpan spaced |
| 7 | Who Decides Is Not Who Pays | `generated` | David23 (am_eric) | 0.81 | 66.987s | `voiceover/section-07-who-decides-who-pays/scratch-audio/section-07-who-decides-who-pays-david23-am_eric-0.81.mp3` | longest section; thesis split across held lines |
| 8 | Payoff: Check The Receipt | `generated` | David23 (am_eric) | 0.81 | 39.573s | `voiceover/section-08-payoff/scratch-audio/section-08-payoff-david23-am_eric-0.81.mp3` | calm close; "Who keeps the tickets?" isolated |
| 9 | Outro: The Cheapest Host On Earth | `generated` | David23 (am_eric) | 0.81 | 17.877s | `voiceover/section-09-outro/scratch-audio/section-09-outro-david23-am_eric-0.81.mp3` | light CTA delivery, no oversell |

Total narration audio: `434.24s` (~`7:14`). Script flat-read estimate was 6:45; the
difference is the approved spacious holds. Within the channel's 6-10 minute target.

## Section Details

Per-section details (status, folder, files, duration, pacing notes) live in each
section's `README.md` and `scratch-results.json` under:

- `voiceover/section-01-hook/`
- `voiceover/section-02-reframe/`
- `voiceover/section-03-promise-machine/`
- `voiceover/section-04-fifa-keeps-the-money/`
- `voiceover/section-05-three-drains/`
- `voiceover/section-06-morning-after/`
- `voiceover/section-07-who-decides-who-pays/`
- `voiceover/section-08-payoff/`
- `voiceover/section-09-outro/`

All sections: wording matches `02-script.md` rev 2 exactly; `[beat]`/`[slower]`/
`[deadpan]` markup stripped for TTS; pacing shaped only in `tts-inputs/*.txt` (punctuation
holds), one MP3 preview per section.

Section 1 speed history: 0.79 (39.851s) -> 0.80 (37.696s) -> 0.81 (35.904s), each a
bare-number owner nudge; 0.81 locked and used for all sections.

## Stale / Regeneration Notes

- None pending. If any `02-script.md` section wording changes, regenerate only that
  section's audio at 0.81 and replace its MP3 (one preview per section).
- Hook length note for review: Section 1 is 99 words (~0:36 at the approved pacing). On
  project 5 the owner preferred a tighter hook (~60-70 words). If the owner asks to
  condense, that is a `script-draft` Update Mode change first, then regen here.

## Next Step Boundary

Next workflow step: `Visual plan`

Do not continue into visual plan, render, review, upload, or learning until the user
asks for the next skill or explicitly requests that step.
