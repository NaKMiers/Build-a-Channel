# Section 6 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 6: When The Store Loses`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (unified video speed, matching Sections 1-5)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; the honest turn that keeps the video fair, then two payoff jokes
- learner clarity notes: "loss leader" introduced as the plain-English term (the free deal as bait to fill the cart). Dry satisfied "Good." after a hold. "milk, bread, eggs" rushes as one comma-run; "Bait." lands alone. Hold before the closing yogurt button.

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). Contrast the fast comma-run ("milk, bread, eggs") against the
choppy hard-stop lines. Real pacing lives only in
`tts-inputs/section-06-when-the-store-loses-tts.txt`; the canonical
`section-06-when-the-store-loses-script.txt` keeps the clean wording that matches `02-script.md`.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-06-when-the-store-loses-david23-am_eric-0.82.mp3`
- Duration: `34.923s` (speed 0.82)
- Use: final approved channel voice for Section 6
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
