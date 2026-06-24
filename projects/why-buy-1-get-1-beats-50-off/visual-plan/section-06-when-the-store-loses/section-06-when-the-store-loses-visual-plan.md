# Section 6 Visual Plan

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 6: When The Store Loses`
Status: `built to subscription bar — fresh bases + clean text; see IMPLEMENTATION.md for as-built`

## Section Goal

The honest turn: BOGO is not always a store win. On cheap staples (milk/bread/eggs) the store can lose money — so why do it? Bait: a loss leader to drag you in and fill your cart with profitable stuff. And there's a cost to you: food you can't finish becomes science experiments / a binned "free" yogurt.

## Source Inputs

- Script: `02-script.md` → Section 6
- Voiceover: `voiceover/section-06-when-the-store-loses/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-06-when-the-store-loses/section-06-word-timings.json` (one whisper duplicate ~21.8–25.5; continuous pass used)
- Section duration: `34.923s`

## Narration

```text
Okay, fair is fair. Buy one, get one free is not always a win for the store either. Sometimes they lose too. Good.
On cheap stuff, milk, bread, eggs, there is barely any profit. Give one away, and the store can actually lose money.
So why do it? Bait. It is called a loss leader. The free deal drags you through the door, betting you will fill the rest of the cart with things that do make money. Spoiler: you will.
And there is a cost on your side too. Two-for-one on food you cannot finish just turns into science experiments in the back of your fridge.
Nothing screams "I saved money" like binning a free yogurt you forgot you owned.
```

## Visual Direction (subscription bar)

- 5 big scenes, ~13 cue beats; FRESH distinct bases + giant WIT (~1280–1320px) varied per scene + one clean hero per beat (no stacked text)
- Bases: produce flat-lay → milk bottles → red fishing lure → open night fridge → litter bin
- Hero devices: "store can LOSE too" + "…good." (A); "milk·bread·eggs" tag + "barely any profit → LOSE money" chip (B); "BAIT" + "a loss leader" + "fill the cart" + "spoiler: you will" (C); "2-for-1 you can't finish → science experiments" (D); "binning a free yogurt → you forgot you owned" (E)
- WIT path: awkward-celebration → thinking → suspicious → confused → facepalm; sides R/L/R/L/R
- Motion: hard-show + impact on "LOSE too", "good", the loss chip, "BAIT", "spoiler", "science experiments"

## Big Scene Plan

| Scene | Local Time | Voice Range | Base | Hero Device | WIT |
|---|---:|---|---|---|---|
| A — fair is fair / store loses | 0.0–6.44 | "fair is fair… sometimes they lose too. Good." | produce flat-lay | "the store can LOSE too" + "…good." | awkward-celebration R |
| B — cheap staples | 6.44–12.56 | "milk, bread, eggs… can actually lose money" | milk bottles | "milk·bread·eggs" + "barely any profit → LOSE money" | thinking L |
| C — bait / loss leader | 12.56–22.56 | "Bait… a loss leader… fill the cart… spoiler, you will" | red fishing lure | "BAIT" → "a loss leader" → "fill the cart" → "spoiler: you will" | suspicious R |
| D — science experiments | 22.56–30.28 | "two-for-one you can't finish… science experiments in the fridge" | open night fridge | "2-for-1 you can't finish → science experiments" | confused L |
| E — binning a free yogurt | 30.28–34.923 | "binning a free yogurt you forgot you owned" | litter bin | "binning a 'free' yogurt → you forgot you owned" | facepalm R |

## HyperFrames Guidance

- Composition: `Section06Loses`, 1920x1080, 34.923s, port 1006
- Devices: `.hero` big labels, `.chip` (loss/tag), `.stamp`, `.cap`, side-gradient `.scrim`
- WIT giant, anchored high, legs-only crop; all devices on the half OPPOSITE the WIT; vertically spaced ≥~150px and revealed sequentially (no stacked/overlapping text)
- Must not invent: scene order, fresh bases, the bait/loss-leader/fridge/bin devices, WIT poses, word-pinned timing

## Approval Checks

- fresh distinct bases per scene (no reuse): yes
- one clean hero per beat, spaced + sequential: yes (no text-over-text)
- WIT giant + varied side/pose: yes (R/L/R/L/R)
- word-pinned: yes
- honest-turn + loss-leader + waste reads: yes
- safe for learners: yes
- ready: yes (built + validated, 0 errors)
