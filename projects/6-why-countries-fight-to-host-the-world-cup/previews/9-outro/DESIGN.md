# Section 9 Preview Design - Outro: The Cheapest Host On Earth

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 9: Outro: The Cheapest Host On Earth`
Composition: `Section09Outro` - 1920x1080, `17.877s`, port `1009`

## Concept

Warm, satisfying closer in two scenes. Scene 9.1 retires the video's receipt motif:
the hero trophy stands on a warm cafe counter like a customer settling its tab and
prints its LAST receipt line - the first green total of the entire video, `TOTAL: $0.00`,
then the stub tears off. Scene 9.2 is the channel's owner-approved animated interactive
UI device: a parody "WhyTube" card on a cozy evening desk; an SVG cursor flies in and
physically clicks LIKE (flips blue, a `$0.00` price tag swings out) and SUBSCRIBE
(flips to grey SUBSCRIBED + bell, localized confetti, `Welcome to the channel!` toast),
with a +6% push-in at the Subscribe beat. WIT makes his single Section 9 appearance -
a peace-sign peek rising beside the card on the consultant line - and the video buttons
out with a green `CONSULTANT-FREE` certification stamp on his chest.

## Scene Map (pinned to section-09-word-timings.json)

| Scene | Time | Base | Content |
|---|---|---|---|
| 9.1 | 0.00-5.66 | `cafe-counter-warm-1.jpg` | trophy (reuse) + receipt band (reuse) + CSS receipt face; prints header on channel@1.52, STADIUMS $0 on stadiums@3.24, TAXES $0 on taxes@4.24, green TOTAL $0.00 impact on receipt@5.12, tear-off 5.45 |
| 9.2 | 5.66-17.877 | `desk-cozy-evening-1.jpg` | WhyTube card pop 5.66; cursor in something@6.60; LIKE click there@8.22; $0.00 tag free@8.92; `100% ours` + arrow hundred@9.94; SUBSCRIBE click + push-in + confetti Subscribe@11.32; toast 11.62; underline money@12.86; bell wiggle goes@14.22; WIT peek consultants@15.48; stamp predict@16.66; hold to 17.877 |

## Key Devices

- CSS receipt face (dot-matrix Courier, dotted leaders, double rule, sawtooth tear edge)
  carries all print text - the receipt PNG's paper band is too narrow (content bbox 37%
  of canvas) to carry cue-critical text (S3 lesson).
- Parody card: own branding only (`Why It Works`, amber `W` avatar, `stories about money`
  where a count would sit) - ZERO numeric UI lines; only numerals on screen are the
  scripted `$0` / `$0.00` joke and the handwritten `100% ours` annotation.
- All icons CSS/SVG (thumb, bell, cursor, tag, rings) - no emoji glyphs.
- Confetti namespaced `.cfp`; boing = combined scale+rotation tweens (never layered).

## WIT

One appearance (per plan): `peace_sign_calm_open_mouth.png`, ~850px content height
(~79% frame height visible, giant), rises from below frame beside the card's right edge
at consultants@15.48; head + glasses + peace hand fully inside frame, legs crop at the
bottom edge only. Face clear of all text; stamp lands below his hand on his torso
(intentional certification-gag placement, plan-specified "below his hand, never on his face").

## Color

Warm amber wood + gold trophy both scenes; green appears exactly three times and rhymes:
receipt `$0` amounts + `TOTAL: $0.00` (9.1), `$0.00` tag and `CONSULTANT-FREE` stamp (9.2).
Blue Liked fill and red-to-grey SUBSCRIBE flip are the state-change accents.
