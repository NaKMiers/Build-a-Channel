# Section 3 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 3: The Receipt Knows`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (unified video speed, matching Sections 1-2)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; the "what you actually spend" reveal, then the smaller-price-vs-bigger-basket parallel
- learner clarity notes: the spend contrast is the job - "five" (50% off) vs "the full ten" (BOGO) must land as clearly separated numbers so the doubling is heard. "You spent twice as much. In one trip." are short reset lines; hold before "a second one you did not need." Ends handing into Section 4's "magic word."

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). Real pacing lives only in
`tts-inputs/section-03-the-receipt-knows-tts.txt`; the canonical
`section-03-the-receipt-knows-script.txt` keeps the clean wording that matches `02-script.md`.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-03-the-receipt-knows-david23-am_eric-0.82.mp3`
- Duration: `32.235s` (speed 0.82; owner hand-tuned the tts-input, was 31.829s)
- Use: final approved channel voice for Section 3
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
