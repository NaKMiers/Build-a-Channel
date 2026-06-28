# Section 4 Voiceover

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 4: The Machine That Feeds Itself`

Status:
`final section voice generated` (David23 / am_eric, approved channel voice ID)

## Direction

- voice: `am_eric` (David23)
- speed: `0.80` (consistent with Sections 1-3)
- language: `en-us`
- tone: deliberate, explanatory; the incentive chain spoken step by step
- learner clarity notes:
  - five numbered steps each land separately - this is the mechanism, must be followable by ear
  - "engagement" glossed inline (clicks, likes, time spent)
  - the pivot line "It rewards attention, not quality" gets extra hold
  - "The machine feeds itself" is the loop closing; closing trio is staccato into "Of course it floods"

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-04-the-machine-that-feeds-itself-david23-am_eric-0.80.mp3`
- Duration: `52.971s`
- Use: production preview / timing reference (approved David23 voice)
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.80 --lang en-us --json`
- Caveat: pacing shaped in the tts-input; canonical
  `section-04-the-machine-that-feeds-itself-script.txt` keeps exact `02-script.md` wording. On this
  machine, prepend the real Python dir to PATH before npx:
  `export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"`.

## Tuning Notes

- Longest section so far (~53s) because it carries the full mechanism. If the owner wants it tighter,
  trim wording in `02-script.md` Section 4 and regenerate.
- Speed `0.80` matches Sections 1-3. Keep all sections at one final speed.
