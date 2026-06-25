# Short 01 — "The Free Trial Is A Countdown"

Native portrait HyperFrames rebuild · `1080x1920` · port `1101` · comp duration `32.60s` (audio `31.381s` + payoff hold).
Source section: S5 (the free trial). Complete standalone short — **NO CTA**.

## One idea
"Free" is a hidden countdown — when it hits zero, free quietly becomes a payment most people forget, and it lives on your statement as a ghost.

## Scenes (real photo base + scrims each)
| Scene | Base | Track | Window | WIT | Hero card(s) |
|---|---|--:|---|---|---|
| A | gift.jpg | 1 | 0–7.60 | deadpan-side-eye (raised) | "START YOUR / FREE TRIAL!" splash pop 2.94 |
| B | hourglass.jpg | 3 | 7.10–14.00 | none | "FREE · 7 days" (7.66) → flips to "→ then $2.99 / mo" (12.66) |
| C | busydesk.jpg | 4 | 13.50–21.40 | hidden-fee-panic | "forgetting is the DESIGN" (15.48) |
| D | piggy.jpg | 5 | 20.80–32.60 | holding-receipt-evidence | bank statement w/ "?? UNKNOWN −$3.00" ringed (24.16) → payoff "FINANCIAL AWARENESS has expired" (28.64, holds) |

Scene bases cross-fade (`fadeScene`, blur→0) on their own track indices.

## Captions (distinct white-on-dark subtitle, vertical center, from real word timings)
- "they make it feel free" 0.05→2.40 · "just pop in your card" 4.60→5.55 · "strangers love that" 5.90→7.00
- "a countdown you can't see" 10.46→12.10
- "most people just forget" 13.80→15.30 · "a ghost in your account" 19.18→20.70
- "open your bank statement" 20.95→22.10 · "find a mystery charge" 22.90→23.95 (clears before the statement card)

Punchlines/payoff carried by the on-screen cards; captions clear before each card pops.

## WIT note
`deadpan-side-eye` and `hidden-fee-panic` sit lower in their PNG canvas, so raised with `bottom:430px` (`#witReceipt` 400px) to clear the centered caption band. Per skill memory: WIT face height is pose-dependent — snapshot a caption-over-WIT beat per pose.

## Voiceover
`voiceover/short-01.mp3` — approved voice `am_eric / 0.84 / en-us`, 31.381s. `**` joke markers and `[...]` cues stripped before TTS. Timings `voiceover/short-01-word-timings.json` (whisper-tiny.en; final word "expired." end clamped 31.68→31.381).

## QA
- `lint`/`validate`: 0 errors. Non-blocking: `overlapping_gsap_tweens` 0–0.42s (opening pop); WCAG contrast false positives.
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed guide (removed). All readable content + WIT faces inside; WIT body bleeds below the bottom edge. Payoff card font reduced so it stays inside the right action-rail edge.
- Snapshots in `snapshots/` cover every key beat.
