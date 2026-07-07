# Section 7 - Who Decides Is Not Who Pays - Design

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Composition: `Section07WhoDecidesWhoPays` - 1920x1080, `66.987s`, port `1007`.

## Structure (9 scenes, 1:1 from the section visual plan)

| Scene | Time | Base | Idea |
|---|---|---|---|
| 7.1 | 0.00-8.78 | `rope-tug-frayed-1.jpg` | setup: giant shrug WIT center, chalk `why still FIGHT?`, teal banner `THE OLDEST TRICK IN ECONOMICS`, torn DECIDES panel (suits trio) vs PAYS panel (receipt conveyor + 3 tiny taxpayer WITs) |
| 7.2 | 8.78-15.36 | `red-carpet-stanchions-1.jpg` | the deciders: suits trio hero + parody trophy, 3 paparazzi polaroid pops with flash blooms, gold tag `the good part - NOW`, speech bubble, smirking WIT closeup right |
| 7.3 | 15.36-21.04 | `map-atlas-colored-1.jpg` | the payers: mirrored pointing WIT + `you are here` chip + `(already)`, overdue envelope + `THE BILL` smash, `+5-10 YEARS LATER` write-on, grayscale trio slides out, `gone.` |
| 7.4 | 21.04-27.82 | `calculator-spreadsheet-1.jpg` + CSS spreadsheet grid | CITY BUDGET form card, glowing prestige crown bounces off the field, red dashed markup box, `DOES NOT FIT` tag, stamp slam `+$9.9 BILLION*`, `*number invented` footnote, gear tag `THE WHOLE MACHINE`, chin-scratch WIT right |
| 7.5 | 27.82-34.94 | `voting-booth-1.jpg` | referendums: locked ballot box, screaming WIT left, giant `NO.` stamp, 6 ballot pops, tally write-on, `OLYMPIC` red underline + `at least` |
| 7.6 | 34.94-40.32 | `auditorium-seats-1.jpg` | empty-room approval: brass applause meter (`meh` -> `APPROVED` via CSS needle sweep), plate `2034 WORLD CUP`, `BIDDERS: 1` stub, `(by acclamation)`, 2 confetti bits, deadpan WIT right |
| 7.7 | 40.32-49.36 | `palm-trees-sky-1.jpg` + CSS shelf | the LA 1984 exception: coin jar `LA 1984 - ORGANIZERS' PROFIT` + `THE OLYMPICS` pin tag, linen banner `PUBLIC VOTE: NO TAXPAYER $$`, padlocked-wallet slam + click pulse, OK-hand WIT left |
| 7.8 | 49.36-58.68 | `crt-monitor-retro-1.jpg` | the trick as a popup ad: `ECONOMISTS HATE THIS` / `ONE WEIRD TRICK` clickbait card, `100% LEGAL` starburst, wiggling X button (CSS patch), odometer bidder counter 14-9-5-2-0, country tag, smug leaning WIT right |
| 7.9 | 58.68-66.987 | `city-hall-columns-1.jpg` | payoff: shrug-smile WIT left, callback card `NEW STADIUMS: 0`, invoice stack + `US CITIES: $100M+` plate + `EACH.` smash, crossed ticket `share of ticket money: none`, torn card `BUILD NOTHING.` / `STILL PAY.`, endless receipt unrolls across the floor |

## Key render-side decisions (documented per skill rules)

- `calculator-spreadsheet-1.jpg` is a calculator on plain white (manifest note) - a CSS
  spreadsheet grid + warm grade was drawn behind it so the "budget" context reads.
- `applause-meter-dial.png` has a baked needle at `meh` - the sweep is a CSS needle
  (rotation-only, pivot at the hub) revealed under a blurred cream patch that hides the
  baked needle only from the sweep beat onward.
- `clickbait-ad-card.png` has a baked X button - the wiggle is a CSS patch drawn on top
  of the baked X, wiggled at the click beat.
- 7.5 drops the pose catalog's separate anger mark (the sourced scream pose carries the
  emotion; a detached CSS anger mark read as random red squiggles in snapshots).
- `red-carpet-stanchions-1.jpg` is stanchions+ropes only and `voting-booth-1.jpg` is
  grey booths (manifest sourcing caveats) - both accepted as-is; cards and props carry
  the meaning.
- Receipt motif reuse: `receipt-endless-roll.png` appears in 7.1 (conveyor crawl) and
  7.9 (floor unroll); tiny taxpayer WIT x3 in 7.1. The resulting
  `duplicate_media_discovery_risk` lint warnings are intentional and documented.

## Timing

All `data-start` values and every GSAP reveal are pinned to
`voiceover/section-07-who-decides-who-pays/section-07-word-timings.json`. The whisper
tail (words 206-216) jumps backward after `with@63.18-63.50`; per the plan the last
cues use the +2.99s shift interpolation (`~` values: ticket cross ~64.26, BUILD
NOTHING ~65.04, STILL PAY ~66.04, receipt unroll ~66.34) and the scene end is clamped
to the real audio duration 66.987. Hide-sets are nudged 0.02-0.16s after clip starts
(validator boundary rule).
