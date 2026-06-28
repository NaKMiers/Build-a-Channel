# Section 7 Voiceover

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 7: Payoff: Activity Is Not Value`

Status:
`final section voice generated`

## Direction

- voice: `David23`
- id: `am_eric`
- speed: `0.86` (matching the user-approved Section 4-6 pace)
- language: `en-us`
- tone: calm, deliberate payoff - calmer than the chaotic middle sections
- delivery: pause-tuned (line breaks + comma before "with value"); `[slower]` on the insight line; final line "trapped in a calendar with Wi-Fi" is the closing dry button
- limitation: Kokoro has no true per-word emphasis; commas give only a slight lift

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-07-payoff-activity-is-not-value-david23-am_eric-0.86.mp3`
- Duration: `46.72s`
- Use: `approved voice, 0.86 pace - production preview`
- Tool: `hyperframes@0.6.76 tts` (Kokoro)
- Caveat: Duration (~47s) is under the script estimate (~60s); visual production may add holds. 0.86 to match Sections 4-6; sections 1-3 are still 0.84.

## How To Regenerate

```bash
# from projects/2-why-everyone-pretends-to-be-busy/
# NOTE: the Microsoft Store python alias hijacks PATH; prepend the real Python dir first.
export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"
npx hyperframes@0.6.76 tts \
  "voiceover/section-07-payoff-activity-is-not-value/tts-inputs/section-07-payoff-activity-is-not-value-david23-am_eric-0.86.txt" \
  --output "voiceover/section-07-payoff-activity-is-not-value/scratch-audio/section-07-payoff-activity-is-not-value-david23-am_eric-0.86.mp3" \
  --voice am_eric --speed 0.86 --lang en-us --json
```

Environment: Python 3.12.10 (winget, user scope) with `kokoro-onnx` + `soundfile`.
