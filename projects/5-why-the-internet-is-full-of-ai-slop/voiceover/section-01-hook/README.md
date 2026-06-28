# Section 1 Voiceover

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 1: Hook: Is Any Of This Real?`

Status:
`final section voice generated` (David23 / am_eric, approved channel voice ID)

## Direction

- voice: `am_eric` (David23)
- speed: `0.80`
- language: `en-us`
- tone: calm, dry, lightly cheeky; a curiosity-gap open, not a scene-setter
- learner clarity notes:
  - "slop / garbage" is the topic word and is glossed visually later; hook just plants the feeling
  - the three-item reveal (shrimp Jesus / fake news / fake band) lands one beat at a time
  - numbers/spelling tells come later; hook stays simple

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-01-hook-david23-am_eric-0.80.mp3`
- Duration: `31.253s`
- Use: production preview / timing reference (approved David23 voice)
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.80 --lang en-us --json`
- Caveat: pacing is shaped in the tts-input (periods + ellipses + `. .`); the canonical
  `section-01-hook-script.txt` keeps the exact `02-script.md` wording. On this machine, prepend the
  real Python dir to PATH before the npx call (Store python stub otherwise shadows it):
  `export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"`.

## Tuning Notes

- Speed `0.80` follows this owner's comfortable slow end (last video settled at 0.79). One-step A/B
  options: `0.79` (slower) or `0.82` (slightly faster). Keep all sections at one final speed.
- Hook is 31.3s. This owner often asks to condense the hook; a tighter ~20-22s version is available on
  request, which would update `02-script.md` Section 1 wording and regenerate this audio.
