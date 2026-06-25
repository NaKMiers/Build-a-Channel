# Section 4 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 4: Your Apps Invented Emergencies`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.86` (user-chosen: 0.84 felt slow, 0.88 felt too fast, settled on 0.86)
- language: `en-us`
- tone: calm, lightly dry; the fastest-content section, kept followable with pauses
- user delivery direction: emphasize important words; speak with pauses between commas and periods; then make it slightly faster
- how applied: Kokoro TTS has no markup/SSML; pauses come from per-line synthesis (one beat per line) + commas around key words + one ellipsis at the punchline. Word-level emphasis is approximated by comma isolation only. Speed nudged 0.84 -> 0.88 while keeping the pauses.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-04-your-apps-invented-emergencies-david23-am_eric-0.86.mp3`
- Duration: `42.133s`
- Use: `approved voice, 0.86 per-section pace — production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: Section 4 runs at 0.86 vs sections 1-3 at 0.84. If you want a uniform video, match the others to 0.86. Earlier 0.84 (43.072s) and 0.88 (41.685s) takes were removed.

## How To Regenerate

```bash
# from projects/2-why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-04-your-apps-invented-emergencies/tts-inputs/section-04-your-apps-invented-emergencies-david23-am_eric-0.86.txt" \
  --output "voiceover/section-04-your-apps-invented-emergencies/scratch-audio/section-04-your-apps-invented-emergencies-david23-am_eric-0.86.mp3" \
  --voice am_eric --speed 0.86 --lang en-us --json
```

Environment: Python 3.12.10 (winget, user scope) with `kokoro-onnx` + `soundfile`.
