# Short 02 — "The Hostage Shampoo"

Native portrait HyperFrames rebuild · `1080x1920` · port `1102` · comp duration `23.85s` (audio `22.632s` + payoff hold).
Source section: S4 (the magic word "FREE"). Complete standalone short — **NO CTA**.

## One idea
"Free" is a feeling, not a number — it switches off your math, so BOGO sells you a word with a full-price purchase stapled on. Payoff: you didn't get a free shampoo, you got a full-price shampoo with a hostage.

## Scenes (real photo base + top/bottom scrim each)
| Scene | Base | Track | Window | WIT | Hero card(s) |
|---|---|--:|---|---|---|
| A | brain.jpg | 1 | 0–5.95 | confused (show 0.0) | red stamp "THE MAGIC WORD / FREE" pops on "free" (1.10) |
| B | gift.jpg | 3 | 5.40–11.70 | none (cards are hero) | "50% off = a NUMBER" (7.94) + "FREE = a FEELING" (10.54) |
| C | cash.jpg | 4 | 11.30–18.40 | awkward-celebration (11.34) | "just YELLS YES & grabs" (11.90) → "it's selling you a WORD" (15.66) + "…full-price purchase stapled on" (16.46) |
| D | prop-shampoo.jpg | 5 | 18.10–23.85 | betrayed (18.14, trapped in the bottle) | payoff "FULL-PRICE / SHAMPOO / + 1 HOSTAGE" pops on "with a hostage" (21.30), holds to end |

Cues sequential; scene bases cross-fade (`fadeScene`, blur→0) on their own track indices.

## Captions (distinct white-on-dark subtitle, vertical center, from real word timings)
- "The magic word…" 0.05→1.00 · "your brain goes stupid" 1.98→3.45 · "you stop doing math" 3.55→5.30
- "do you even want two?" 5.60→7.80 (clears before the contrast cards)
- (Scene C punchline carried by cards — no caption duplication)
- "you didn't get a free shampoo" 18.30→19.66 · "you got a full-price one…" 19.88→21.10 (clears before the payoff card)

Punchline/payoff carried by the on-screen cards, never duplicated in a caption; captions clear before each card pops.

## Voiceover
`voiceover/short-02.mp3` — approved voice `am_eric / 0.84 / en-us`. Timings `voiceover/short-02-word-timings.json` (whisper-tiny.en; tail "shampoo with a hostage" re-timed monotonically 20.84→22.632 to fix the whisper end-of-audio glitch).

## QA
- `lint`/`validate`: 0 errors. Non-blocking: `overlapping_gsap_tweens` 0–0.42s (intentional opening pop); WCAG contrast false positives (colored key text sampled while cards are hidden).
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed guide (removed). All readable content + WIT faces inside; WIT body bleeds below the bottom edge (allowed). Payoff card stacked to 2 lines so it stays inside the right action-rail edge.
- Snapshots in `snapshots/` cover every key beat.
