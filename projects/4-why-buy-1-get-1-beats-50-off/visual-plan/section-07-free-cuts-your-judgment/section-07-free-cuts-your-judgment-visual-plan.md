# Section 7 Visual Plan

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 7: Payoff: Free Cuts Your Judgment`
Status: `built to full bar (kinetic, fresh bright bases) - see IMPLEMENTATION.md for as-built`

## Section Goal

The payoff: the two signs play different games - 50% off cuts the PRICE, "free" cuts your JUDGMENT. Stay fair (sometimes you want two; sometimes free is free), but see the second sign before "free" switches off your inner accountant. Stinger: "buy 1 get 1 50% off" is just 25% off in a costume. Sign-off: same shelf, same product, different game - go be slightly harder to trick.

## Source Inputs

- Script: `02-script.md` → Section 7
- Voiceover: `voiceover/section-07-free-cuts-your-judgment/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-07-free-cuts-your-judgment/section-07-word-timings.json` (clean)
- Section duration: `38.912s`

## Narration

```text
So why does buy one, get one free beat fifty percent off?
Because the two signs are playing different games.
Fifty percent off cuts the price. Buy one, get one free cuts your judgment.
One asks your brain a question. The other hands it a gift and says, shh, relax.
This does not mean never take the deal. Sometimes you genuinely want two. Sometimes free really is free money. Just see the second sign coming before "free" switches off your inner accountant.
Oh, one last thing. Next time you see "buy one, get one fifty percent off"? That is not free anything. That is twenty-five percent off, in a costume.
Same shelf. Same product. Completely different game. Now go be slightly harder to trick.
```

## Visual Direction (full subscription bar)

- 5 big scenes, ~14 cue beats; FRESH bright distinct bases + giant WIT (~1320px) alternating R/L/R/L/R + kinetic devices + clean spaced text (light text-side scrim, no dark overlay)
- Bases: chess → scissors → calculator → carnival mask → playing cards
- Hero devices: FREE vs 50% OFF face-off + "different GAMES" (A); the thesis "cuts the PRICE" / "cuts your JUDGMENT" smash (B); a calculator that computes "5−4=?" → caveat checks → flips to "switched off" (C); "BUY 1 GET 1 50% OFF" → unmask → "= 25% OFF / in a costume" (D); "different GAME" + "go be slightly harder to trick" payoff (E)
- WIT path: thinking → suspicious → talking-front → betrayed → pointing-right
- Motion: hard-show + impact on JUDGMENT, the calc on→off flip, the 25%-off reveal, the costume stamp, the final "harder to trick"

## Big Scene Plan

| Scene | Local Time | Voice Range | Base | Hero Device | WIT |
|---|---:|---|---|---|---|
| A - different games | 0.0–6.52 | "why does free beat 50%?… different games" | chess | FREE vs 50% OFF + "two different GAMES" | thinking R |
| B - the thesis | 6.52–10.72 | "cuts the price… cuts your judgment" | scissors | "cuts the PRICE" / "free cuts your JUDGMENT" | suspicious L |
| C - inner accountant | 10.72–25.48 | "asks your brain a question… free is free money… switches off your inner accountant" | calculator | calc "5−4=?" + caveat ✓✓ → "switched off" | talking-front R |
| D - 25% in a costume | 25.48–33.84 | "buy 1 get 1 50% off… not free… 25% off in a costume" | carnival mask | "BUY 1 GET 1 50% OFF" → "= 25% OFF" + "in a costume" | betrayed L |
| E - sign-off | 33.84–38.912 | "same shelf, same product, different game… harder to trick" | playing cards | "different GAME" + "go be slightly harder to trick" | pointing-right R |

## HyperFrames Guidance

- Composition: `Section07Payoff`, 1920x1080, 38.912s, port 1007
- Devices: `.sign`/`.vs` face-off, `.hero` thesis lines, `.calc`(live)+`.calc.off` flip, `.chip.ok` caveats, `.stamp` reveals
- WIT giant, anchored high, legs-only crop; devices OPPOSITE WIT; spaced + sequential
- Must not invent: scene order, fresh bases, the thesis/calc-flip/unmask/payoff devices, WIT poses/sides, word-pinned timing

## Approval Checks

- fresh distinct bright bases per scene (no reuse, no dark overlay): yes
- kinetic hero device per beat: yes
- WIT giant + varied side/pose: yes (R/L/R/L/R)
- thesis ("cuts price vs cuts judgment") lands: yes
- "25% off in a costume" stinger lands on the mask: yes
- fair caveat kept (sometimes 2 / free is free): yes
- word-pinned: yes
- safe for learners: yes
- ready: yes (built + validated, 0 errors)
