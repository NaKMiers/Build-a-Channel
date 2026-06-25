# Short 04 — "The Product Is You, Not Cancelling"

Native portrait HyperFrames rebuild · `1080x1920` · port `1104` · comp duration `21.20s` (audio `19.861s` + payoff hold).
Source section: S7 (payoff). Complete standalone short — **NO CTA**.

## One idea
The product was never the app or the show — it's your forgetting, the month you meant to cancel and didn't. So read your statement and cancel the ghosts.

## Scenes (real photo base + scrims each)
| Scene | Base | Track | Window | WIT | Hero card(s) |
|---|---|--:|---|---|---|
| A | phone.jpg | 1 | 0–10.00 | thinking | "what do they REALLY sell?" (5.06) → "the real product is YOUR FORGETTING" (8.90) |
| B | phone-2.jpg | 3 | 9.55–14.05 | shocked | barcode tag "PRODUCT: YOU" (11.34) |
| C | cash2.jpg | 4 | 13.60–18.10 | holding-receipt-evidence | statement: ✓ keep "The one you love" / ghost rows struck (15.12) |
| D | coins.jpg | 5 | 17.70–21.20 | deadpan-side-eye | payoff "CANCEL THE GHOSTS / keep what you love" (19.00, holds) |

Scene bases cross-fade (`fadeScene`).

## Captions (distinct white-on-dark subtitle, vertical center, from real word timings)
- "why is it ALL a subscription?" 0.05→2.00 · "not the app. not the show." 6.92→8.50
- "the product is you… staying" 12.60→13.55 · "read them out loud" 16.22→17.55 · "keep the ones you love" 17.94→18.95 (clears before payoff)

Punchlines/payoff carried by the cards; captions clear before a card pops. Ends on "Cancel the ghosts" (the actionable payoff), NOT the long video's "your salary. for now." closer.

## WIT note
`thinking` raised to `bottom:450px`, `shocked` 420px, `deadpan-side-eye` 430px, `holding-receipt-evidence` 400px — all sit lower in their PNG; raised so the centered caption clears the face.

## Voiceover
`voiceover/short-04.mp3` — approved voice `am_eric / 0.84 / en-us`, 19.861s. Timings `voiceover/short-04-word-timings.json` (whisper-tiny.en; final word "ghosts." end clamped 22.16→19.861).

## QA
- `lint`/`validate`: 0 errors. Non-blocking: `overlapping_gsap_tweens` 0–0.42s (opening pop); WCAG contrast false positives.
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed guide (removed). All content + WIT faces inside; WIT body bleeds below the bottom edge. Statement rows set to `nowrap` so the "The one you love" line stays on one line inside the safe zone.
- Snapshots in `snapshots/` cover every key beat.
