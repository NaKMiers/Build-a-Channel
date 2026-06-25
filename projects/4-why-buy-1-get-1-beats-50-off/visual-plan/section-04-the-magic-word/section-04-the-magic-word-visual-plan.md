# Section 4 Visual Plan

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 4: The Magic Word`
Status: `built to subscription vivid-hook bar — see IMPLEMENTATION.md for as-built`

## Section Goal

Show how the word "FREE" switches off your math. Giant glowing FREE, the brain going stupid, the zero-price effect (Ariely), the NUMBER-vs-FEELING contrast, and the hostage-shampoo punchline ("a full-price purchase stapled to a word").

## Source Inputs

- Script: `02-script.md` → Section 4
- Voiceover: `voiceover/section-04-the-magic-word/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-04-the-magic-word/section-04-word-timings.json`
- Section duration: `37.099s`

## Narration

```text
That magic word is "free." And "free" makes your brain go a little stupid.
When something is free, you stop doing math. You forget the boring question: do I even want a second one?
A scientist named Dan Ariely said it best. When something is free, we forget the downside. Free feels like a gift, so we grab it and switch our brains off.
"Fifty percent off" is a number. Your brain checks numbers. "Free" is a feeling. Your brain just yells "yes" and grabs.
So buy one, get one free is not selling you a discount. It is selling you a word, and quietly stapling a full-price purchase to it.
You did not get a free shampoo. You got a full-price shampoo, with a hostage.
```

## Visual Direction (subscription vivid-hook bar)

- 5 big scenes, ~12 cue beats; vivid dark object bases + giant kinetic devices + GIANT WIT varied per scene
- Bases: brain → coins → gift → cash → coins (dark dramatic grades brightness ~0.42–0.6 + heavy scrim)
- Hero devices: giant glowing FREE (Scene A), BRAIN OFF badge + math (B), ZERO-PRICE/gift (C), NUMBER-vs-FEELING split + "YES!" (D), hostage shampoo photo + ransom (E)
- WIT path: holding-phone-panic → confused → awkward-celebration → suspicious → betrayed (~980–1180px)
- Motion: hard-show + impact (smash/pop) on FREE, BRAIN OFF, GIFT, the FEELING "YES!", the hostage reveal
- Retention risk: abstract idea (zero-price effect); fix with the concrete NUMBER-vs-FEELING split + the literal hostage shampoo

## Big Scene Plan

| Scene | Local Time | Voice Range | Base | Hero Device | WIT |
|---|---:|---|---|---|---|
| A — FREE / brain stupid | 0.0–4.14 | "magic word is free… brain go a little stupid" | brain (dark) | giant glowing FREE | holding-phone-panic R |
| B — stop doing math | 4.14–9.42 | "stop doing math… do I even want a second one?" | coins (dark) | math + BRAIN OFF badge + "?" toast | confused L |
| C — Ariely / free = gift | 9.42–17.82 | "Dan Ariely… free feels like a gift… brains off" | gift boxes | ZERO-PRICE caption + GIFT + brains OFF | awkward-celebration C |
| D — number vs feeling | 17.82–25.32 | "a number, brain checks… a feeling, yells yes" | cash (dark) | blue NUMBER card vs red FEELING "YES!" card | suspicious R |
| E — selling a word / hostage | 25.32–37.099 | "not a discount, a word… full-price… a hostage" | coins (dark red) | "a WORD" + stapled FULL-PRICE + hostage shampoo photo + ransom | betrayed R |

## Cue Timeline (word-pinned — see IMPLEMENTATION.md for exact data-starts)

- FREE smash @1.12 ("free"); "a little stupid" @3.06
- math @5.32; BRAIN OFF @5.84; "?" @7.78
- Ariely @9.66; GIFT @14.34; brains OFF @16.48
- NUMBER card @17.95; FEELING "YES!" @21.36
- "a WORD" @26.66; stapled full-price @30.28; shampoo photo @33.24; rope @35.36; HOSTAGE ransom @36.50

## HyperFrames Guidance

- Composition: `Section04Magic`, 1920x1080, 37.099s, port 1004
- Reuses the S3/subscription CSS kit (payoff, stamp, toast, giant WIT) + new devices (matheq/offbadge, number-vs-feeling `.scol`, `.photoframe` hostage + `.rope`)
- WIT giant (~980–1180px), anchored high, legs-only crop; devices arranged opposite WIT
- Must not invent: scene order, vivid bases, the giant FREE / number-vs-feeling / hostage devices, WIT poses, word-pinned timing

## Approval Checks

- vivid dark bases per scene: yes
- giant kinetic hero device per beat: yes
- WIT giant + varied: yes (5 poses; sides r/l/c/r/r — D/E share right with different poses/scales)
- word-pinned: yes
- hostage punchline lands: yes
- safe for learners: yes (number vs feeling is the clear teach)
- ready: yes (built + validated)
