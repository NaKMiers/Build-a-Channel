# Section 7 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 7: Payoff: Free Cuts Your Judgment`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (unified video speed, matching Sections 1-6)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; the payoff that lands the insight, stays fair, and ends on a warm cheeky sign-off
- learner clarity notes: THE thesis line is "Fifty percent off cuts the price. Buy one, get one free cuts your judgment." — let "cuts your judgment" land, then the section's longest hold. Soft "shh... relax." "25% off in a costume" is the memorable stinger; hold before it. "Same shelf. Same product." is a staccato callback to the hook.

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). The longest hold of the section follows "cuts your judgment" (the
`[pause]` cue), shaped with stacked `...`, not a speed change (the whole video stays at `0.82`). Real
pacing lives only in `tts-inputs/section-07-free-cuts-your-judgment-tts.txt`; the canonical
`section-07-free-cuts-your-judgment-script.txt` keeps the clean wording that matches `02-script.md`.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-07-free-cuts-your-judgment-david23-am_eric-0.82.mp3`
- Duration: `38.912s` (speed 0.82; was 39.381s before the "shh" -> "shush" fix)

## TTS Divergence

- The canonical `section-07-free-cuts-your-judgment-script.txt` keeps "shh" (matches `02-script.md`).
- The tts-input uses "shush" because Kokoro reads the letter cluster "shh" as "s-h-h" (spelling it out)
  instead of the shushing sound. "shush" is a real word, so it is pronounced correctly and carries the
  same intent ("the seductive voice of free quieting your math").
- Use: final approved channel voice for Section 7
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
