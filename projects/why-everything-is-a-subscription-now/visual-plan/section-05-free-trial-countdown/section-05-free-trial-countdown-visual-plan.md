# Section 5 Visual Plan (Section 1 standing template, 2026-06-23)

Video: `Why Everything Is a Subscription Now`
Section: `Section 5: The Free Trial Is A Countdown`
Status: `built + review fix applied (2026-06-23) — previewing on localhost:1005`

## Review fix (2026-06-23, round 2)

Owner: the blank white-screen phone (BS1 0:00 and BS4 0:23) read as a placeholder and didn't match the
script, and the same image was reused for two scenes. Fixed: BS1 now uses a **pink gift box** (`base-gift.jpg`)
— "they make it feel FREE" = a free gift; BS4 now uses an **everyday desk** (notebook + coffee, `base-busydesk.jpg`)
— "they forget… life is loud." Two distinct descriptive bases; the phone is no longer used in this section.
The CSS devices (FREE splash, Day-7 reminder) are unchanged and still read on the new bases.

## Source Inputs

- Voiceover: `voiceover/section-05-free-trial-countdown/scratch-audio/section-05-...-david23-am_eric-0.8.mp3`
- Duration: `53.867s` (TTS `scratch-results.json`)
- Word timings: `voiceover/section-05-free-trial-countdown/section-05-word-timings.json` — GENERATED this run
  (whisper-tiny.en), clean + monotonic; tail "expired." ends ~54.62 → capped at 53.867.

## Narration

```text
Here's the genius part. To get you in, they make it feel free.
"Start your free trial!" No charge today! Just pop in your card — you know, for no reason at all. Totally normal. Strangers love holding your card.
And the trial is real. It really is free. For seven days. After that, a tiny countdown you can't see hits zero, and "free" quietly becomes a payment.
And most people don't cancel on day seven. They forget. Not because they're careless — because forgetting is the design. The charge is small, the date is fuzzy, life is loud.
So the little payment just... continues. Forever. A ghost, living in your bank account. Rent free. Well — not rent free. That's the whole problem.
Open your bank statement right now and you'll probably find one. A mystery charge. Three dollars. Every month. For a thing you opened once, in a year you cannot name.
Your free trial of financial awareness has expired.
```

## Visual Direction

- 6 big scenes for 53.9s (~9s each), one vivid OBJECT base per scene; the most real-UI-heavy section (free-trial button, countdown, bank statement) — owner-preferred real-UI built in CSS over real photo bases.
- VIVID OBJECT BASES (vary per scene, all distinct): a pink gift box (feel free = a gift) → a keyboard desk (pop in your card) → an HOURGLASS (the countdown) → an everyday desk with notebook + coffee (forget / loud life) → a leather wallet + cash (the ghost charge) → a piggy bank / finances flat-lay (the statement).
  - Every scene has its own distinct object base (no reuse); the hourglass literally IS "the free trial is a countdown."
- VARIED real-UI idea-devices per beat: a CSS `FREE` trial splash screen; a CSS credit card + "pop in your card"; a `FREE TRIAL 00:00` → `NOW CHARGING $2.99/mo` flip beside the hourglass; a `Day 7 — cancel?` notification that fades (forgotten) + `forgetting is the DESIGN`; translucent recurring `−$2.99/mo` GHOST charges over the wallet; a CSS bank statement with the `?? UNKNOWN −$3.00` row CIRCLED IN RED (meaningful — it rings the exact mystery charge) + EXPIRED running-gag banner.
- GIANT WIT, varied side/pose (4 beats; S1 + S5 breathe): deadpan-side-eye RIGHT (strangers love your card) → hidden-fee-panic LEFT (free→payment) → thinking RIGHT (forget) → holding-receipt-evidence LEFT (found the mystery charge).

## Big Scene Plan

| Big Scene | Local Time | Voice | Vivid base | Why | Base file |
|---|---:|---|---|---|---|
| BS1 feel free | 0.0–6.0 | "the genius part… make it feel free" | pink gift box | the hook: free = a gift/lure | base-gift.jpg |
| BS2 pop card | 6.0–11.9 | "just pop in your card… strangers love holding your card" | keyboard desk | you hand over the card | base-desk.jpg |
| BS3 countdown | 11.9–21.0 | "free for 7 days… countdown hits zero… becomes a payment" | hourglass | the trial is a countdown | base-hourglass.jpg |
| BS4 forget | 21.0–30.7 | "don't cancel… they forget… forgetting is the design" | everyday desk (notebook + coffee) | forgetting in a loud, busy life | base-busydesk.jpg |
| BS5 ghost | 30.7–39.5 | "continues forever… a ghost in your bank account… rent free" | wallet + cash | the charge haunts forever | base-wallet.jpg |
| BS6 statement | 39.5–53.867 | "open your statement… a mystery charge, $3 every month… EXPIRED" | piggy / finances | the evidence on your statement | base-piggy.jpg |

## Cue State Timeline (pinned to word starts)

| Cue | Time | Voice | Scene | What changes | Motion | WIT |
|---|---:|---|---|---|---|---|
| C1 | 0.4 / 2.9 | "the genius part / feel free" | BS1 | headline; CSS `FREE` trial splash | hard-show / pop | — |
| C2 | 6.3 | "pop in your card" | BS2 | headline; CSS credit card slides in | hard-show / smash | — |
| C3 | 10.5 | "strangers love holding your card" | BS2 | cream aside; deadpan WIT | hard-show | deadpan-side-eye R |
| C4 | 11.9 / 16.4 | "free for 7 days / countdown hits zero" | BS3 | headline; `FREE TRIAL 00:00` card by the hourglass | hard-show | — |
| C5 | 18.7 / 19.1 / 19.8 | "free becomes a payment" | BS3 | flip to red `NOW CHARGING $2.99/mo`; panic WIT; label | impact | hidden-fee-panic L |
| C6 | 21.5 → 23.5 | "don't cancel… they forget" | BS4 | `Day 7 — cancel?` notification appears, then fades (ignored) | hard-show → dim | thinking R @23.2 |
| C7 | 26.0 / 27.6 | "forgetting is the design / small·fuzzy·loud" | BS4 | `forgetting is the DESIGN`; `small · fuzzy · life is loud` | impact / hard-show | thinking holds |
| C8 | 30.8 / 34.0–35.2 | "continues forever / a ghost in your bank account" | BS5 | `forever` headline; 3 translucent `−$2.99/mo` ghost charges pop | hard-show / pop | — |
| C9 | 37.0 | "rent free. well, not rent free." | BS5 | cream aside | hard-show | — |
| C10 | 39.7 / 40.2 | "open your bank statement" | BS6 | headline; CSS bank statement card | hard-show | — |
| C11 | 43.3 | "a mystery charge" | BS6 | red ring around the exact `?? UNKNOWN −$3.00` row; WIT enters | impact | holding-receipt-evidence L |
| C12 | 44.5 | "$3 every month… a thing you can't name" | BS6 | red label | impact | holds |
| C13 | 50.2 | "free trial of financial awareness has expired" | BS6 | EXPIRED system banner (headline hidden) | impact | holds |

## WIT Pose Plan (giant, varied)

| Time | Pose | Side / scale | Why |
|---:|---|---|---|
| 10.5–11.9 | wit-pose-deadpan-side-eye.png | RIGHT, width 1240, bottom:-330 | dry "strangers love holding your card" |
| 18.7–21.0 | wit-pose-hidden-fee-panic.png | LEFT, width 1220, bottom:-330 | "free" quietly becomes a payment |
| 23.2–30.7 | wit-pose-thinking.png | RIGHT, width 1200, bottom:-330 | trying to remember to cancel (forgetting) |
| 43.3–53.8 | wit-pose-holding-receipt-evidence.png | LEFT, width 1200, bottom:-330 | found the mystery charge on the statement |

WIT density: 4 beats / 6 scenes; BS1 (FREE splash) and BS5 (ghost charges) breathe. All verified transparent.
AVOID `typing-on-laptop` + `money-panic` (baked black bg).

## Reference And Asset Plan

| Asset | Type | Source / status | Use |
|---|---|---|---|
| base-gift.jpg | real CC0 | safe asset; rawpixel (Openverse) pink gift box | BS1 (free = a gift) |
| base-busydesk.jpg | real CC0 | safe asset; StockSnap (Openverse) desk w/ notebook + coffee | BS4 (forget / loud life) |
| base-desk.jpg | real CC0 | safe asset; StockSnap (Openverse) keyboard on wood | BS2 |
| base-hourglass.jpg | real CC0 | safe asset; rawpixel (Openverse) hourglass | BS3 |
| base-wallet.jpg | real CC0 | safe asset; rawpixel (Openverse) leather wallet + cash | BS5 |
| base-piggy.jpg | real CC0 | safe asset; StockSnap (Openverse) piggy bank + calculator + ledger | BS6 |
| FREE splash / card / flip / notification / ghost charges / statement + ring / EXPIRED | self-made CSS real-UI | build in render | the idea-devices |
| WIT poses | local PNG | shared manifest | emotion |

All bases sourced via Openverse / Wikimedia + viewed. Rejected: a person-holding-card photo (no-face), Apple-device flat-lays, ID-cards-with-faces, illustration-on-white. See `reference-board.md`.

## HyperFrames Guidance

- Composition `Section05Trial`, 1920x1080, 53.867s, port 1005.
- Scenes on tracks 1/3/4/5/6/7 (cross-fades at 6.0/11.9/21.0/30.7/39.5); cues on track 2.
- All 6 scenes use distinct base files (no media reuse, so no `duplicate_media_discovery_risk`).
- No emoji glyphs — ghost is a translucent CSS card (not 👻); checks/warn are CSS shapes.
- The S6 red ring must align to the exact `?? UNKNOWN −$3.00` row (verified by snapshot at 51.5 — it rings that row, not a neighbor).
- Snapshot QA: 4.0 / 10.8 / 17.0 / 19.6 / 27.0 / 35.0 / 44.0 / 51.5.
- Must not invent: scene order/bases, WIT poses/sides, label/device text, cue + stagger timing, motion types, ring alignment.

## Review-Prevention Checklist

- voice sync pinned to generated word starts: yes
- 6 distinct vivid object bases (~9s each; phone reuse non-consecutive): yes
- varied real-UI idea-devices, not repeated cream boxes: yes
- giant WIT, varied side/pose (R/L/R/L), 4 beats, S1+S5 breathe: yes
- the one red ring targets a REAL element (the exact mystery-charge row), not empty space: yes
- no text-on-text; S6 "$3 every month" moved below the statement clear of WIT; EXPIRED banner hides the headline: yes
- impact reserved for the price flip, the ring, the labels, the payoff banner: yes
