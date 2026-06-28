# Section 2 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 2: Reframe: Looking Busy vs Doing Work`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.84`
- language: `en-us`
- tone: calm, lightly dry, learner-friendly; correct the "lazy people" idea, then land the real reframe
- learner clarity notes: the three short "looks like nothing" beats stay matter-of-fact; slow down on the closing line "the real work usually hides in the part you cannot see"

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-02-reframe-looking-busy-vs-doing-work-david23-am_eric-0.84.mp3`
- Duration: `28.949s`
- Use: `approved channel voice - production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: Duration (28.949s) is just under the script estimate (~31s); visual production may add a short hold.

## How To Regenerate

```bash
# from projects/2-why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-02-reframe-looking-busy-vs-doing-work/tts-inputs/section-02-reframe-looking-busy-vs-doing-work-david23-am_eric-0.84.txt" \
  --output "voiceover/section-02-reframe-looking-busy-vs-doing-work/scratch-audio/section-02-reframe-looking-busy-vs-doing-work-david23-am_eric-0.84.mp3" \
  --voice am_eric --speed 0.84 --lang en-us --json
```

Environment: Python 3.12.10 (winget, user scope) with `kokoro-onnx` + `soundfile`.
