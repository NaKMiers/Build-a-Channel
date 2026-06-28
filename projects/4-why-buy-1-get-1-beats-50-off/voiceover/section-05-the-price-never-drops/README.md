# Section 5 Voiceover

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 5: The Price Never Drops`

Status:
`final section voice generated`

## Direction

- voice: `David23 / am_eric`
- speed: `0.82` (unified video speed, matching Sections 1-4)
- language: `en-us`
- tone: young, clear, lightly dry, learner-friendly; the sneakiest trick - anchoring - plus the deliberate-design close
- learner clarity notes: the anchoring idea is the job - 50% off makes the thing "only really worth five bucks... cheap, forever" (heaviest, slowest hold) vs BOGO keeping "that proud ten-dollar price." Dry shrug on "eh, not really." Close lands the on-purpose design ("charge full for the first").

## Pacing

Authored in the approved spacious template (heavy `...` holds, trailing `...` on setups, `. .`
staccato on punchy short lines). The `[slower]` "looks cheap... forever" beat gets the heaviest
hold, shaped with stacked `...`, not a speed change (the whole video stays at `0.82`). Real pacing
lives only in `tts-inputs/section-05-the-price-never-drops-tts.txt`; the canonical
`section-05-the-price-never-drops-script.txt` keeps the clean wording that matches `02-script.md`.

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File: `scratch-audio/section-05-the-price-never-drops-david23-am_eric-0.82.mp3`
- Duration: `36.416s` (speed 0.82)
- Use: final approved channel voice for Section 5
- Tool: `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.82 --lang en-us --json`
- Caveat: prepend the real Python dir to PATH before npx so Kokoro does not hit the Windows Store python stub.
