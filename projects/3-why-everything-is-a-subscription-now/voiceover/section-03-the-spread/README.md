# Section 3 Voiceover

Video:
`Why Everything Is a Subscription Now`

Section:
`Section 3: The Spread: From Apps To Your Car`

Status:
`final section voice generated`

## Direction

- voice: `David23` (`am_eric`)
- speed: `0.8` (video-wide unified speed; below the 0.84 channel default, set by user across all sections)
- language: `en-us`
- tone: young male ~23, clear, bright, lightly dry, learner-friendly
- learner clarity notes:
  - Authored in the approved Section 5 spacious pacing template.
  - The subscription list ("one for shows, one for movies...") is split into separate held lines so it stops rushing (commas add no pause in this engine).
  - `**bold**` joke markers and `[beat]/[deadpan]` cues are NOT spoken — stripped before TTS.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-03-the-spread-david23-am_eric-0.8.mp3`
- Duration: `54.165s` (section estimate `1:06-2:04`)
- Use: final channel voice (David23 / am_eric)
- Tool: `npx hyperframes@0.6.76 tts`
- Caveat: On this Windows machine the TTS command must prepend the real Python dir to PATH so HyperFrames does not hit the Microsoft Store `python` stub:
  `export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"`
