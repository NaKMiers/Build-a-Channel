# Section 3 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 3: Busy Became A Status Symbol`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.84`
- language: `en-us`
- tone: calm, lightly dry, learner-friendly; reason 1 of the four-reason system (status)
- learner clarity notes: keep "Same planet, opposite brag." deadpan and flat; steady unhurried pace on this longer section; let the final line "proving you are near the work" land as the button

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-03-busy-became-a-status-symbol-david23-am_eric-0.84.mp3`
- Duration: `45.077s`
- Use: `approved channel voice — production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: Duration (45.077s) is under the script estimate (~54s); visual production may add holds or silence.

## How To Regenerate

```bash
# from projects/why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-03-busy-became-a-status-symbol/tts-inputs/section-03-busy-became-a-status-symbol-david23-am_eric-0.84.txt" \
  --output "voiceover/section-03-busy-became-a-status-symbol/scratch-audio/section-03-busy-became-a-status-symbol-david23-am_eric-0.84.mp3" \
  --voice am_eric --speed 0.84 --lang en-us --json
```

Environment: Python 3.12.10 (winget, user scope) with `kokoro-onnx` + `soundfile`.
