# Section 6 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 6: "I'm Busy" Is A Shield`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.86` (matching the user-approved Section 4-5 pace)
- language: `en-us`
- tone: calm, lightly dry; reason 4 (busy as a social shield) — WIT protected and overwhelmed, not smug
- delivery: pause-tuned (line breaks + commas + ellipses on the closing "busy... or pretending... or both")
- limitation: Kokoro has no true per-word emphasis; commas give only a slight lift

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-06-im-busy-is-a-shield-david23-am_eric-0.86.mp3`
- Duration: `37.973s`
- Use: `approved voice, 0.86 pace — production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: Duration (~38s) is under the script estimate (~48s); visual production may add holds. 0.86 to match Sections 4-5; sections 1-3 are still 0.84.

## How To Regenerate

```bash
# from projects/why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-06-im-busy-is-a-shield/tts-inputs/section-06-im-busy-is-a-shield-david23-am_eric-0.86.txt" \
  --output "voiceover/section-06-im-busy-is-a-shield/scratch-audio/section-06-im-busy-is-a-shield-david23-am_eric-0.86.mp3" \
  --voice am_eric --speed 0.86 --lang en-us --json
```

Environment: Python 3.12.10 (winget, user scope) with `kokoro-onnx` + `soundfile`.
