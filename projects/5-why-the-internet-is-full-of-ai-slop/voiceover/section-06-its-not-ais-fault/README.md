# Section 6 Voiceover

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 6: It's Not AI's Fault (And Not A Plot)`

Status:
`final section voice generated` (David23 / am_eric, approved channel voice ID)

## Direction

- voice: `am_eric` (David23)
- speed: `0.80` (consistent with Sections 1-5)
- language: `en-us`
- tone: fair, then dry; the honest turn that keeps the video from being AI-panic
- learner clarity notes:
  - "not all AI is slop" stated plainly; two clean "not slop" examples (doctor, artist)
  - the dead-internet conspiracy is named and rejected ("It's dumber than that")
  - "You cannot arrest an incentive" is the dry closer; let it land

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-06-its-not-ais-fault-david23-am_eric-0.80.mp3`
- Duration: `38.933s`
- Use: production preview / timing reference (approved David23 voice)
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.80 --lang en-us --json`
- Caveat: pacing shaped in the tts-input; canonical
  `section-06-its-not-ais-fault-script.txt` keeps exact `02-script.md` wording. On this machine,
  prepend the real Python dir to PATH before npx:
  `export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"`.

## Tuning Notes

- Speed `0.80` matches Sections 1-5. Keep all sections at one final speed.
