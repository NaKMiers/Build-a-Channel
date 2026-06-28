# Short 02 - "Cancelling Is A Vision Quest"

Native portrait HyperFrames rebuild · `1080x1920` · port `1102` · comp duration `28.70s` (audio `27.413s` + payoff hold).
Source section: S6 (easy in, no way out). Complete standalone short - **NO CTA**.

## One idea
Signing up takes ten seconds; cancelling is deliberately a vision quest - negative option billing keeps you paying unless you actively say stop.

## Scenes (real photo base + scrims each)
| Scene | Base | Track | Window | WIT | Hero card(s) |
|---|---|--:|---|---|---|
| A | stopwatch.jpg | 1 | 0–7.80 | running-away (running across the dial) | "SIGN UP: 10 seconds" (4.36) + "CANCEL: a vision quest" (5.76) |
| B | maze.jpg | 3 | 7.28–16.78 | confused | "FINAL BOSS" (10.80) → 6-step breadcrumb maze sliding in account→…→"we'll miss you" (11.90–15.64) |
| C | maze-2.jpg | 4 | 16.50–20.20 | tiny-defeated | gag "a phone number that answers 2:00–2:15, Tuesdays only" (16.96) |
| D | contract.jpg | 5 | 19.90–28.70 | suspicious | "NEGATIVE OPTION / BILLING" stamp (21.12) → payoff "you keep paying unless you say STOP" (24.63, holds) |

Scene bases cross-fade (`fadeScene`); breadcrumb chips use a `slide` (x:-40→0) reveal for the maze feel.

## Captions (distinct white-on-dark subtitle, vertical center, from real word timings)
- "i'll just cancel" 0.05→1.55 · "oh, sweet child" 1.66→2.55 · "getting in is one tap" 7.40→8.90 · "this even has a name…" 19.96→21.05

Punchlines/payoff carried by the cards; captions clear before a card pops.

## WIT note
`confused`/`tiny-defeated` sit lower in their PNG canvas → raised (`#witConfused` 440px, `#witDefeated` 430px). `running-away` and `suspicious` sit high - left at default `bottom:360px`. Per skill memory: WIT face height is pose-dependent.

## Voiceover
`voiceover/short-02.mp3` - approved voice `am_eric / 0.84 / en-us`, 27.413s. `**`/`[...]` stripped before TTS. Timings `voiceover/short-02-word-timings.json` (whisper-tiny.en; **tail glitch from "trick." onward - last 9 words re-timed monotonically across 24.28→27.413**; whisper had jumped them backward and overshot to 28.07).

## QA
- `lint`/`validate`: 0 errors. Non-blocking: 2× `overlapping_gsap_tweens` 0–0.42s (opening pop + slide); WCAG contrast false positives.
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed guide (removed). All content + WIT faces inside; WIT body bleeds below the bottom edge. The "NEGATIVE OPTION BILLING" stamp was stacked to two lines so it stays inside the right action-rail edge.
- Snapshots in `snapshots/` cover every key beat.
