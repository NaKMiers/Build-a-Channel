# Section 2 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 2: Same To You, Not To Them`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (unified video speed, matching Section 1)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; calm reveal of the store-side math, then a dry Wedgwood roast
- learner clarity notes: rev 2.1 - owner found the original confusing because the profit numbers were stated without the subtraction. The math is now SPOKEN aloud ("Five minus four... the store keeps one dollar" / "Ten minus eight... two dollars"). Each operation gets the heaviest holds so numbers land one at a time. "you" = shopper, "the store" = seller throughout (no pronoun flip). "Double." lands alone as the payoff. Hold before "You are just the latest."

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). The subtraction lines get the heaviest holds - the operation hangs,
then the result lands - shaped with stacked `...`, NOT a speed change (the whole video stays at
`0.82`). Real pacing lives only in `tts-inputs/section-02-same-to-you-not-to-them-tts.txt`; the
canonical `section-02-same-to-you-not-to-them-script.txt` keeps the clean wording that matches
`02-script.md` rev 2.1.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-02-same-to-you-not-to-them-david23-am_eric-0.82.mp3`
- Duration: `40.469s` (speed 0.82; rev 2.1 clarity rewrite, was 36.075s on rev 2 wording)
- Use: final approved channel voice for Section 2
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
