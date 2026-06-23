# Section 1 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 1: Hook: You're The Rabbit`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (lowered from 0.84 by request for learner clarity)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; open on a shock claim, then a curiosity gap
- learner clarity notes: short lines; the shock claim ("a store can give it free and make MORE than half price") must land before the reveal; "Same product. Same shelf." land as separate beats.

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). Real pacing lives only in `tts-inputs/section-01-hook-tts.txt`;
the canonical `section-01-hook-script.txt` keeps the clean wording that matches `02-script.md`.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-01-hook-david23-am_eric-0.82.mp3`
- Duration: `23.019s` (speed 0.82; was 22.613s @ 0.84)
- Use: final approved channel voice for Section 1
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
