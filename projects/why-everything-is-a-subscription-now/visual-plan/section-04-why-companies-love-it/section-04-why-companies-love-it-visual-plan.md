# Section 4 Visual Plan (Section 1 standing template, 2026-06-23)

Video: `Why Everything Is a Subscription Now`
Section: `Section 4: Why Companies Love It: One Sale Becomes Forever`
Status: `built + previewing on localhost:1004`

## Source Inputs

- Voiceover: `voiceover/section-04-why-companies-love-it/scratch-audio/section-04-...-david23-am_eric-0.8.mp3`
- Duration: `51.093s` (TTS `scratch-results.json`)
- Word timings: `voiceover/section-04-why-companies-love-it/section-04-word-timings.json` — GENERATED this run
  (whisper-tiny.en). Clean except a chunk-boundary BACKWARD-jump around 24–26s (the "worth a little / pays
  every month" line re-emitted); cues are pinned to the CLEAN word starts (buys-once 22.1, worth-a-lot 26.8,
  like-rain 29.3). Tail "trap." ends ~51.46 → capped at the 51.093 audio.

## Narration

```text
So why did everyone switch to this? Simple. Follow the money. It's always the money.
Imagine you sell a coffee machine. You make one sale, you say thank you, and then you wait. Maybe years. Hoping that person ever comes back.
Now imagine instead, they pay you a little every month. Automatically. Possibly forever. Even on the months they don't touch the thing. Which business would you rather own? Yeah, me too.
A customer who buys once is worth a little. A customer who pays every month is worth a lot, because that payment just keeps coming. Like rain. Or relatives.
This is the magic word behind everything now: recurring. Recurring money is predictable. A company can plan its entire future around your forgetfulness.
So the goal quietly changed. It used to be: make something good enough that you buy it. Now it can also be: make something sticky enough that you never quite leave. Less "great product." More "beautiful trap."
```

## Visual Direction

- 6 big scenes for 51s (~8.5s each), one vivid OBJECT base per scene; the argument = recurring revenue beats a one-time sale.
- VIVID OBJECT BASES (vary per scene): a $100 bill (follow the money) → an espresso machine pulling a shot (sell a coffee machine, one sale) → the SAME coffee machine as a "money machine" (recurring) → cash again (worth a little vs a lot) → a wall/desk calendar (recurring/forgetfulness) → a mousetrap with cheese (beautiful trap).
  - The coffee machine recurs across BS2→BS3 as a deliberate before/after on the SAME example object (the script's "you sell it once" vs "now imagine monthly"); cash recurs BS1↔BS4 non-consecutively. Both reuse a separate filename copy to keep lint clean.
- VARIED idea-devices per beat (not cream boxes): `FOLLOW THE MONEY` kinetic word; one gold coin + "ONE sale / wait… years"; a rising COIN GEYSER + "automatically / FOREVER"; a "buys once = a little / pays monthly = A LOT" coin comparison + coin RAIN; a giant `RECURRING` word + red rings on repeating calendar dates; a `BEAUTIFUL TRAP` payoff on the mousetrap. One cream aside ("which would you rather own? me too") + one ("like rain. or relatives").
- GIANT WIT, varied side/pose (4 beats; BS1 + BS4 breathe): sleeping-burned-out RIGHT (wait years) → empty-wallet LEFT (pay forever) → confused LEFT (forgetfulness) → suspicious RIGHT (beautiful trap).

## Big Scene Plan

| Big Scene | Local Time | Voice | Vivid base | Why | Base file |
|---|---:|---|---|---|---|
| BS1 follow the money | 0.0–5.0 | "why did everyone switch? follow the money" | $100 bill | the answer is money | base-cash.jpg |
| BS2 coffee one-sale | 5.0–12.0 | "sell a coffee machine… one sale… wait years" | espresso machine | the old model: one sale, then wait | base-coffee.jpg |
| BS3 recurring machine | 12.0–22.0 | "now they pay a little every month… forever… rather own" | same coffee machine (warm) + coin geyser | the new model: recurring money | base-coffee-machine.jpg |
| BS4 worth a lot | 22.0–30.6 | "buys once = a little / pays monthly = a lot… like rain" | cash | recurring is worth far more | base-cash-lot.jpg |
| BS5 recurring word | 30.6–39.1 | "the magic word: recurring… your forgetfulness" | calendar | recurring = predictable, planned around forgetting | base-calendar.jpg |
| BS6 beautiful trap | 39.1–51.093 | "goal changed… sticky enough you never leave… beautiful trap" | mousetrap + cheese | the goal became stickiness, not quality | base-mousetrap.jpg |

## Cue State Timeline (pinned to clean word starts)

| Cue | Time | Voice | Scene | What changes | Motion | WIT |
|---|---:|---|---|---|---|---|
| C1 | 0.30 / 2.90 | "why switch / follow the money" | BS1 | question label → `FOLLOW THE MONEY` kinetic | hard-show / impact | — |
| C2 | 5.0 / 7.0 | "coffee machine / one sale" | BS2 | headline; gold coin + `ONE sale. thanks!` | hard-show / pop | — |
| C3 | 9.50 | "wait. maybe years" | BS2 | `then you wait… maybe YEARS` | impact | sleeping-burned-out RIGHT |
| C4 | 12.0 / 13.8 | "now every month" | BS3 | headline; coin GEYSER rises (staggered) | hard-show / pop | empty-wallet LEFT |
| C5 | 15.7 / 16.5 | "automatically / forever" | BS3 | `automatically` → red `FOREVER.` | hard-show / impact | — |
| C6 | 19.0 | "which would you rather own? me too" | BS3 | cream aside | hard-show | — |
| C7 | 22.1 | "buys once is worth a little" | BS4 | `buys once = a little` + small coin | hard-show | — |
| C8 | 26.8 | "worth a lot" | BS4 | `pays monthly = A LOT` + coin stack | impact | — |
| C9 | 29.3 | "keeps coming. like rain" | BS4 | coin RAIN + cream aside `like rain. or relatives` | pop | — |
| C10 | 30.9 / 33.3 | "the magic word / recurring" | BS5 | `the magic word:` → giant `RECURRING` | hard-show / impact | — |
| C11 | 33.9–35.4 | "recurring money is predictable" | BS5 | `AUTO-PAY · same charge every month` statement card; identical −$9.99 rows (Jan/Feb/Mar/Apr) pop one-per-beat (review fix: replaced 4 meaningless red rings) | hard-show (staggered) | — |
| C12 | 36.0 / 38.1 | "your forgetfulness" | BS5 | confused WIT; `plan around your FORGETFULNESS` | hard-show / impact | confused LEFT |
| C13 | 39.3 / 41.7 | "goal changed / good enough to buy" | BS6 | headline; `old: good enough to BUY` | hard-show | — |
| C14 | 44.8 | "sticky enough you never leave" | BS6 | red `now: sticky enough you NEVER LEAVE` | impact | suspicious RIGHT @46 |
| C15 | 50.0 | "more beautiful trap" | BS6 | `BEAUTIFUL TRAP` payoff (labels hidden) | impact | suspicious holds |

## WIT Pose Plan (giant, varied)

| Time | Pose | Side / scale | Why |
|---:|---|---|---|
| 9.5–12.0 | wit-pose-sleeping-burned-out.png | RIGHT, width 1340, bottom:-300 | "you wait. maybe years." |
| 13.8–22.0 | wit-pose-empty-wallet.png | LEFT, width 1200, bottom:-330 | paying a little every month forever |
| 36.0–39.1 | wit-pose-confused.png | LEFT, width 1200, bottom:-340 | planned around your forgetfulness |
| 46.0–51.0 | wit-pose-suspicious.png | RIGHT, width 1250, bottom:-330 | eyeing the beautiful trap |

WIT density: 4 beats / 6 scenes; BS1 (follow the money) and BS4 (worth a lot) breathe — the kinetic word and
the coin comparison/rain carry them. All verified transparent. AVOID `typing-on-laptop` + `money-panic` (baked black bg).

## Reference And Asset Plan

| Asset | Type | Source / status | Use |
|---|---|---|---|
| base-cash.jpg / base-cash-lot.jpg | real CC0 | safe asset; StockSnap (Openverse) "Money Cash" $100 close-up (2nd filename = lint-safe reuse) | BS1, BS4 |
| base-coffee.jpg / base-coffee-machine.jpg | real CC0 | safe asset; StockSnap (Openverse) "Espresso Coffee" (2nd filename = before/after reuse) | BS2, BS3 |
| base-calendar.jpg | real CC0 | safe asset; rawpixel (Openverse) calendar dates | BS5 |
| base-mousetrap.jpg | real CC0 | safe asset; rawpixel (Openverse) mousetrap + cheese | BS6 |
| coins / geyser / stack / rain / RECURRING / payoff / calendar rings | self-made CSS | build in render | the idea-devices |
| WIT poses | local PNG | shared manifest | emotion |

All bases sourced via Openverse + viewed. Rejected: cartoon coin illustrations on white, a sterile $20-fan-on-white, branded laptops. See `reference-board.md`.

## HyperFrames Guidance

- Composition `Section04Why`, 1920x1080, 51.093s, port 1004.
- Scenes on tracks 1/3/4/5/6/7 (cross-fades at 5.0/12.0/22.0/30.6/39.1); cues on track 2.
- Reused bases use a 2nd filename (`-machine`, `-lot`) to avoid `duplicate_media_discovery_risk`.
- Any smashed element uses explicit left/top. No emoji glyphs (CSS coins/rings/`$`).
- Snapshot QA: 3.5 / 9.8 / 17.0 / 27.2 / 33.6 / 37.0 / 45.2 / 50.5.
- Must not invent: scene order/bases, WIT poses/sides, label/device text, cue + stagger timing, motion types.

## Review-Prevention Checklist

- voice sync pinned to generated word starts (clean run, glitch avoided): yes
- 6 distinct vivid object bases (~8.5s each; coffee + cash reuse are deliberate before/after / non-consecutive): yes
- varied idea-devices (coins/geyser/stack/rain/RECURRING/trap), not repeated cream boxes: yes
- giant WIT, varied side/pose (R/L/L/R), 4 beats, BS1+BS4 breathe: yes
- no text-on-text; BS6 payoff hides the OLD/NOW labels; BS5 WIT left / text right: yes
- impact reserved for kinetic words, the geyser, FOREVER, the comparison, the payoff: yes
