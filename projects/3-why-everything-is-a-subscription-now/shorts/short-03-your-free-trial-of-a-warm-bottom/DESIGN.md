# Short 03 - "Your Free Trial Of A Warm Bottom"

Native portrait HyperFrames rebuild · `1080x1920` · port `1103` · comp duration `21.05s` (audio `19.648s` + payoff hold).
Source section: S3 (the spread - heated seats). Complete standalone short - **NO CTA**.

## One idea
The rent model spread past screens into hardware you already own - like heated seats you bought, now behind a monthly fee.

## Scenes (real photo base + scrims each)
| Scene | Base | Track | Window | WIT | Hero card(s) |
|---|---|--:|---|---|---|
| A | tv-room.jpg | 1 | 0–10.30 | shocked | streaming wall (5 colored rows) pops 4.62, **poofs away** 7.62 → "POV: YOU OWN NOTHING" stamp 9.14 |
| B | car.jpg | 3 | 9.85–21.05 | deadpan-side-eye | "the heated seats / already in YOUR car / now: a monthly fee" 12.80 → payoff "A WARM BOTTOM has expired" 17.24 (holds) |

Two bases (the heated-seat beat is short, so scene A sets up "you own nothing" first to make a complete idea). Scene B holds the car base and swaps paywall→payoff card.

## Captions (distinct white-on-dark subtitle, vertical center, from real word timings)
- "you don't own a single one" 0.05→2.20 · "stop paying - it all vanishes" 5.98→7.40 · "wait… my own car?" 13.56→15.10

Punchline/payoff carried by the cards; captions clear before a card pops.

## WIT note
`shocked` raised to `bottom:420px`, `deadpan-side-eye` to `430px` (both sit low in their PNG) so the centered caption clears the face.

## Voiceover
`voiceover/short-03.mp3` - approved voice `am_eric / 0.84 / en-us`, 19.648s. Timings `voiceover/short-03-word-timings.json` (whisper-tiny.en; final word "expired." end clamped 22.14→19.648).

## QA
- `lint`/`validate`: 0 errors. Non-blocking: `overlapping_gsap_tweens` 0–0.45s (opening pop + the streaming-wall poof); WCAG contrast false positives.
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed guide (removed). All content + WIT faces inside; WIT body bleeds below the bottom edge. **Bug fixed:** the paywall "monthly fee" badge was inline (overflowed right) → set `display:block` so it stacks centered.
- Snapshots in `snapshots/` cover every key beat.
