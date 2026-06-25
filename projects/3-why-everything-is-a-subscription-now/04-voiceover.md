# 04 Voiceover

Video: `Why Everything Is a Subscription Now`

Status: `section voiceover complete (all 7 sections)`

Source skill: `voiceover`

Source file:

- `02-script.md`

## Voice Direction

- Default final voice: `David23` (`am_eric`)
- Current generation voice: `David23` (`am_eric`)
- Speed: `0.8` (video-wide; below the 0.84 channel default, set by user across the whole video)
- Language: `en-us`
- Tone: young male ~23, clear, bright, lightly dry, learner-friendly
- Voice status: `final channel voice generated for ALL Sections 1-7 at unified speed 0.8`

## Section Voiceover Index

|   # | Section | Status | Voice | Speed | Duration | Audio file | Notes |
| --: | ------- | ------ | ----- | ----: | -------: | ---------- | ----- |
| 1 | Hook: It's More Than You Think | final section voice generated | David23 / am_eric | 0.8 | 23.509s | `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.8.mp3` | S5 pacing template |
| 2 | Reframe: You Stopped Buying, You Started Renting | final section voice generated | David23 / am_eric | 0.8 | 37.909s | `voiceover/section-02-reframe/scratch-audio/section-02-reframe-david23-am_eric-0.8.mp3` | S5 pacing template |
| 3 | The Spread: From Apps To Your Car | final section voice generated | David23 / am_eric | 0.8 | 54.165s | `voiceover/section-03-the-spread/scratch-audio/section-03-the-spread-david23-am_eric-0.8.mp3` | S5 pacing; sub-list split into held lines |
| 4 | Why Companies Love It: One Sale Becomes Forever | final section voice generated | David23 / am_eric | 0.8 | 51.093s | `voiceover/section-04-why-companies-love-it/scratch-audio/section-04-why-companies-love-it-david23-am_eric-0.8.mp3` | S5 pacing template |
| 5 | The Free Trial Is A Countdown | final section voice generated | David23 / am_eric | 0.8 | 53.867s | `voiceover/section-05-free-trial-countdown/scratch-audio/section-05-free-trial-countdown-david23-am_eric-0.8.mp3` | S5 pacing template (origin of the template) |
| 6 | Easy In, No Way Out | final section voice generated | David23 / am_eric | 0.8 | 53.013s | `voiceover/section-06-easy-in-no-way-out/scratch-audio/section-06-easy-in-no-way-out-david23-am_eric-0.8.mp3` | S5 pacing; cancel-menu staccato |
| 7 | Payoff: The Product Is You Not Cancelling | final section voice generated | David23 / am_eric | 0.8 | 54.101s | `voiceover/section-07-payoff/scratch-audio/section-07-payoff-david23-am_eric-0.8.mp3` | S5 pacing; thesis on holds |

Total narration: approx `5:28` across 7 sections.

## Voice / Pacing Standard For This Video

- All sections use the approved **Section 5 spacious pacing template**: heavy `...` holds between beats,
  trailing `...` setups before payoffs, `. .` staccato resets on punchy lines, comma-lists split into
  separate held lines.
- All sections generated at unified speed **0.8** (David23 / am_eric, en-us).
- Clean script wording is preserved in each section's `*-script.txt`; all pacing lives in the
  `tts-inputs/*.txt`.

## Section Details

Each section folder under `voiceover/section-XX-*/` holds its `README.md`, clean `*-script.txt`,
`*-marked-script.md`, `tts-inputs/*.txt`, the single `0.8` MP3 preview in `scratch-audio/`, and
`scratch-results.json` with the exact command, voice, speed (0.8), language, duration, and status.

| # | Folder | Duration |
| --: | ------ | -------: |
| 1 | `voiceover/section-01-hook/` | 23.509s |
| 2 | `voiceover/section-02-reframe/` | 37.909s |
| 3 | `voiceover/section-03-the-spread/` | 54.165s |
| 4 | `voiceover/section-04-why-companies-love-it/` | 51.093s |
| 5 | `voiceover/section-05-free-trial-countdown/` | 53.867s |
| 6 | `voiceover/section-06-easy-in-no-way-out/` | 53.013s |
| 7 | `voiceover/section-07-payoff/` | 54.101s |

## Stale / Regeneration Notes

- All 7 sections regenerated at unified speed `0.8` (previous `0.79` previews removed). No speed mismatch remains.
- All section audio is current against `02-script.md` and the S5 pacing template.
- Next pipeline step is `visual-plan` (then render -> review -> combine -> caption).

## Next Step Boundary

Next workflow step: `Visual plan`

Do not continue into visual plan, render, review, upload, or learning until the user asks for the next skill or explicitly requests that step.
