# Section 1 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 1: Hook: The Busy Trap`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.84`
- language: `en-us`
- tone: calm, lightly dry, learner-friendly; a person explaining something ridiculous without acting surprised
- learner clarity notes: short sentences, common words; the dry button "There is a difference." needs a small beat before it

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-01-hook-the-busy-trap-david23-am_eric-0.84.mp3`
- Duration: `21.056s`
- Use: `approved channel voice — production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: Duration (21.056s) is a little under the script estimate (~27s); visual production may add short holds or silence to fill timing.

## How To Regenerate

```bash
# from projects/why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-01-hook-the-busy-trap/tts-inputs/section-01-hook-the-busy-trap-david23-am_eric-0.84.txt" \
  --output "voiceover/section-01-hook-the-busy-trap/scratch-audio/section-01-hook-the-busy-trap-david23-am_eric-0.84.mp3" \
  --voice am_eric --speed 0.84 --lang en-us --json
```

Environment: Python 3.12.10 (installed via winget, user scope) with `kokoro-onnx` + `soundfile`.
