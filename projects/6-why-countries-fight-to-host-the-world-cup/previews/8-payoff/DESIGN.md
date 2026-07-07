# Section 8 - Payoff: Check The Receipt - Design

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Composition: `Section08Payoff` - 1920x1080, `39.573s`, port `1008`.

## Structure (6 calm scenes, 1:1 from the section visual plan)

| Scene | Time | Base | Idea |
|---|---|---|---|
| 8.1 | 0.00-9.82 | `mantel-livingroom-1.jpg` (hard grey-blue grade + stone crop) | trophy demoted to shelf decor, receipt roll still printing, `SOLD AS: INVESTMENT` struck red, three hang tags: ATTENTION / STATUS / CENTER OF THE WORLD |
| 8.2 | 9.82-14.76 | `office-empty-chair-1.jpg` | accountability gag: PUBLIC MONEY coin jar, `the planner` arrow at the empty chair, `OUT OF OFFICE` stamp, the receipt slides onto the empty seat |
| 8.3 | 14.76-20.22 | `overlook-railing-dusk-1.jpg` | object hero: selfie-stick WIT (NEW pose, mirrored), giant phone with parody camera UI photographing the trophy, `cost: billions` sticker, shutter blink |
| 8.4 | 20.22-26.46 | `cash-counter-machine-1.jpg` (euro notes) | honesty turn: `MADE MONEY:` tally card (3 red strokes), `every time counted.` hedge, green `MONEY -> FIFA` arrow (S4 callback) |
| 8.5 | 26.46-34.34 | `coffee-table-lamp-1.jpg` | THE THESIS FRAME: receipt close-up - ghost lines, `1x GLOBAL PRESTIGE ... price on request`, `1x FEELING OF BEING ON TV ... $11,000,000,000?`, red scrawl `WHO KEEPS THE TICKETS?` writes on, marker beside |
| 8.6 | 34.34-39.573 | `mantel-livingroom-1.jpg` (closer crop, darker) | callback closer: question block pops, trophy + hanging receipt with circled `NAME: ..........`, deflated grey balloon, giant resigned-nod WIT (NEW pose) with ticket stub; end clamped to 39.573 |

## Key render-side decisions (documented per skill rules)

- CHRISTMAS-MANTEL NEUTRALIZATION (manifest caveat): the base is bow/garland-decorated, so
  both mantel scenes crop INTO the stone chimney breast (`scale(2.35)` origin `47% 26%`;
  8.6 `scale(2.6)` origin `42% 30%`) - all bows, garlands, the candy tree and the mantel
  greenery fall outside the window; grade `saturate(0.35)` + cool tint kills the palette;
  a bottom-right corner shade hides the girl-figurine sliver; the shelf itself is a CSS
  floating board (the photo's real shelf sits too high in frame to carry the trophy).
- The receipt asset's paper is ~37% of its canvas width (S6 lesson), so all 8.5 cue text
  sits on a self-carried white receipt PANEL (the strip's flat section on the table); the
  asset strip feeds into it from the top edge. Red scrawl deliberately overflows the paper.
- The "office" base has its chair at the RIGHT edge, so WIT peeks from the LEFT (pose
  mirrored so the side-eye looks into the room) and the receipt lands ON the empty seat.
- The "cash counter machine" base is actually scattered euro notes (manifest substitution);
  the tally card + green arrow carry the count/direction beats over the money texture.
- `wit-selfie-stick-calm.png` is drawn with the stick up-LEFT; mirrored via wrapper so the
  stick points up-right at the giant phone. Camera caption shows as two hard-show lines
  (a clip-path type-on across centered text clipped mid-word - rebuilt after snapshot QA).
- `MONEY -> FIFA` label sits on a white chip (green handwriting on busy notes fails the
  chip rule); red markup (strike, OUT OF OFFICE, NAME circle) lands on CSS targets only.
- Motif reuse by design: receipt in 8.1/8.2/8.5/8.6, trophy in 8.1/8.3/8.6, mantel base in
  8.1/8.6 (planned open/close callback) - the 3 `duplicate_media_discovery_risk` lint
  warnings are intentional and documented.

## Timing

All `data-start` values and every GSAP reveal are pinned to
`voiceover/section-08-payoff/section-08-word-timings.json` (monotonic; plan times matched
the JSON exactly). Whisper's final token "receipt." runs to 42.30 - the scene end is
clamped to the real audio duration `39.573s` per the plan. Hide-sets are nudged
0.02-0.16s after clip starts (validator boundary rule). Calm-section motion budget:
hard-shows by default; impact only on the red strike, OUT OF OFFICE stamp, strike+NEVER
line, sticker slap, shutter blink, FIFA arrow sweep, 8.6 question pop and NAME circle.
