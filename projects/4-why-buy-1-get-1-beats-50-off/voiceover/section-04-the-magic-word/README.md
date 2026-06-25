# Section 4 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 4: The Magic Word`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (unified video speed, matching Sections 1-3)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; the "free switches off your math" reveal, soft Ariely cite, hostage punchline
- learner clarity notes: the number-vs-feeling contrast is the core — ""Fifty percent off" is a number / your brain checks numbers" vs ""Free" is a feeling / your brain yells yes and grabs." Build as a clean A-vs-B parallel with a reset between halves. Dry hold on "a little stupid." Hold before the "hostage" payoff.

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). Real pacing lives only in
`tts-inputs/section-04-the-magic-word-tts.txt`; the canonical
`section-04-the-magic-word-script.txt` keeps the clean wording that matches `02-script.md`.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-04-the-magic-word-david23-am_eric-0.82.mp3`
- Duration: `37.099s` (speed 0.82)
- Use: final approved channel voice for Section 4
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
