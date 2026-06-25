# Short 03 — "25% Off In A Costume"

Native portrait HyperFrames rebuild · `1080x1920` · port `1103` · comp duration `21.30s` (audio `19.989s` + payoff hold).
Source section: S7 (free cuts your judgment — the payoff). Complete standalone short — **NO CTA**.

## One idea
The two signs play different games: 50% off cuts the PRICE, "free" cuts your JUDGMENT. So "buy one, get one 50% off" isn't free anything — it's 25% off, in a costume.

## Scenes (real photo base + top/bottom scrim each)
| Scene | Base | Track | Window | WIT | Hero card(s) |
|---|---|--:|---|---|---|
| A | chess.jpg | 1 | 0–6.05 | thinking (show 0.0, raised) | "FREE vs ½ OFF?" (0.70) |
| B/C | cutmoney.jpg | 3 | 5.55–16.50 | talking-front (7.40) | "50% off cuts the PRICE" (6.30) → "FREE cuts your JUDGMENT" (8.28) |
| D | mask.jpg | 4 | 16.00–21.30 | shocked (16.10, raised) | payoff "~~BOGO 50% off~~ = 25% OFF …in a costume" pops on "25% off" (18.06), holds to end |

B and C share the cutmoney base (the scissor-cut €50 note literally illustrates "cuts"); cards + WIT swap within the one base. Scene bases cross-fade (`fadeScene`, blur→0) on their own track indices.

## Captions (distinct white-on-dark subtitle, vertical center, from real word timings)
- "why does FREE win?" 0.05→1.90 · "different games" 4.04→5.45
- "shush… relax" 11.90→12.75 · "buy 1, get 1, 50% off?" 14.40→15.95
- "that's not free anything" 16.20→17.40 (clears before the payoff card)

Punchlines ("cuts the PRICE/JUDGMENT", the payoff) carried by the on-screen cards, never duplicated in a caption; captions clear before each card pops.

## WIT note
The `thinking` and `shocked` pose PNGs sit lower in their canvas than `talking-front`, so the centered caption clipped the chin. Fixed with per-pose overrides `#witThinking{bottom:540px}` / `#witShocked{bottom:520px}` to lift the head clear of the caption band (body bleeds below the bottom edge, which is allowed). **General lesson: WIT face height is pose-dependent — always snapshot a caption-over-WIT beat per pose.**

## Voiceover
`voiceover/short-03.mp3` — approved voice `am_eric / 0.84 / en-us`, 19.989s. "shush" spelled out (not "shh") so kokoro speaks the word. Timings `voiceover/short-03-word-timings.json` (whisper-tiny.en; final word "costume." end clamped 22.44→19.989 to fix the whisper end-of-audio glitch).

## QA
- `lint`/`validate`: 0 errors. Non-blocking: `overlapping_gsap_tweens` 0–0.42s (intentional opening pop); WCAG contrast false positives (colored key text sampled while cards are hidden).
- Safe zone `x[60..880] · y[220..1490]` verified with a temporary dashed guide (removed). All readable content + WIT faces inside; WIT body bleeds below the bottom edge (allowed).
- Snapshots in `snapshots/` cover every key beat.
