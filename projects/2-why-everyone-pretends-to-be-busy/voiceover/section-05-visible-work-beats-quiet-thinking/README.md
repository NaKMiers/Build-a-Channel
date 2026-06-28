# Section 5 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 5: Visible Work Beats Quiet Thinking`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.86` (matching the user-approved Section 4 pace)
- language: `en-us`
- tone: calm, lightly dry; reason 3 of the four-reason system (visibility beats thinking)
- delivery: pause-tuned (line breaks + commas + ellipsis); `[slower]` honored on the manager-survey line; "possibly blinking" is the deadpan button
- limitation: Kokoro has no true per-word emphasis; commas give only a slight lift

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-05-visible-work-beats-quiet-thinking-david23-am_eric-0.86.mp3`
- Duration: `42.859s`
- Use: `approved voice, 0.86 pace - production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: 0.86 to match Section 4; sections 1-3 are still 0.84.

## How To Regenerate

```bash
# from projects/2-why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-05-visible-work-beats-quiet-thinking/tts-inputs/section-05-visible-work-beats-quiet-thinking-david23-am_eric-0.86.txt" \
  --output "voiceover/section-05-visible-work-beats-quiet-thinking/scratch-audio/section-05-visible-work-beats-quiet-thinking-david23-am_eric-0.86.mp3" \
  --voice am_eric --speed 0.86 --lang en-us --json
```

Environment: Python 3.12.10 (winget, user scope) with `kokoro-onnx` + `soundfile`.
