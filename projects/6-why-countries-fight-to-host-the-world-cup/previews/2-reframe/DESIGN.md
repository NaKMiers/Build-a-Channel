# Section 2 Preview - Reframe: A Purchase, Not An Investment

Composition: `Section02Reframe` - 1920x1080, `33.728s`, port `1002`.

Built 1:1 from `visual-plan/section-02-reframe/section-02-reframe-visual-plan.md`. Every cue is
pinned to `voiceover/section-02-reframe/section-02-word-timings.json` (first-pass timestamps; the
whisper duplicate backward pass at words 91-109 is skipped exactly as the plan documents; scene 2.5
end clamped to the real audio duration 33.728s).

## Scenes

| # | Local time | Track | Base | Content |
|---|---|---:|---|---|
| 2.1 | 0.00-10.04 | 1 | `resort-pool-1.jpg` (sunny, no scrim) | WIT pool-float bottom-left; 4 postcard chips pop up a rising arc (tourists! 2.82 / hotels full! 3.70 / shops rich! 4.70 / economy UP! 5.52); teal ribbon `as told by every bidding government` hard-shows 6.70; pink `lovely!` sticker slaps 9.06 |
| 2.2 | 10.04-16.32 | 2 | `calculator-desk-1.jpg` | CSS readout: green digits flicker, snap red `-4,000,000,000` on different@10.84; CSS paper sheets; giant lecturing WIT (right, hip crop) on truth@12.30; `INVESTMENT?` writes on from 12.80; red X strokes 13.82/13.98; `PURCHASE` stamp + frame shake 15.42 |
| 2.3 | 16.32-20.88 | 3 | `showroom-floor-1.jpg` | `red-supercar-generic.png` center-right; WIT flex (boss glasses-adjust pose) left at the fender; `makes money? NO.` card 17.82; 3 camera flashes + glints + `LOOK AT ME.` on SEEN@19.64; extra glint 20.14 |
| 2.4 | 20.88-29.34 | 4 | `marble-counter-1.jpg` + CSS warm blurred boutique backdrop + counter line | car (flipped, small) left, `trophy-gold-parody.png` right, `price-tag-blank.png` w/ CSS `STATUS` on the car from cut; tag arcs to the trophy on football@23.62 (docks by 24.78); text flips red `BILLIONS...` 25.50; panic WIT rises chest-up behind the counter on And@26.14; `credit-card-taxpayer.png` slides in 26.68; `yours.` + arrow 27.48; emboss light sweep + bounce on taxpayer's@28.32 |
| 2.5 | 29.34-33.728 | 5 | `desk-darkwood-1.jpg` + `wallet-empty-cutout.png` (derived) | trophy (cooler grade) right w/ tag `PRESTIGE - price on request`; tag wiggles 29.90; giant skeptical WIT left (waist crop); `"will it pay off?"` card 30.86, red strike 31.68; `WHO PAYS?` slams 33.16, double underline |

Audio: `section-02-reframe.mp3` (copy of the approved David23/am_eric 0.81 take), track 30.

## Motion classification

- Hard-show: ribbon 2.1, WIT entrances (2.2/2.4), `makes money? NO.`, `will it pay off?` (pop), tag texts from cut.
- Impact (emphasis only): `lovely!` slap, red X, `PURCHASE` (+shake), `LOOK AT ME.` + flashes, `BILLIONS...` flip, emboss sweep + card bounce, `WHO PAYS?` slam.
- Transition (plan-specified cause-effect): tag arc car->trophy, credit-card slide-in, `INVESTMENT?` write-on.

## Notable build mechanics

- X strokes: rotation kept in inline CSS, `scaleX(0)` applied via `tl.set` (an inline `rotate() scaleX(0)` is a degenerate matrix - GSAP loses the rotation).
- 2.4 WIT chest-crop: WIT sits in an `overflow:hidden` wrapper ending at the counter line.
- 2.5 wallet: `wallet-empty-1.jpg` is a white-studio-bg photo; `mix-blend-mode:multiply` did not survive the capture path, so the white bg was keyed out (border-connected near-white BFS + 1px dilation) into the derived `assets/wallet-empty-cutout.png` and composited with a CSS warm grade + drop-shadow.
