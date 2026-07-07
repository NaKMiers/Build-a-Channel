# Section 4 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 4: FIFA Keeps The Money`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/4-fifa-keeps-the-money/`
- Source: `visual-plan/section-04-fifa-keeps-the-money/section-04-fifa-keeps-the-money-visual-plan.md` (built 1:1; render-side adjustments below)
- Port: `1004`
- Studio URL: `http://localhost:1004/#project/4-fifa-keeps-the-money`
- Direct composition URL: `http://localhost:1004/api/projects/4-fifa-keeps-the-money/preview/comp/index.html`
- Runtime: `62.101s`, 9 scenes (tracks 1-9), audio track 30
- Voiceover: `section-04-fifa-keeps-the-money-david23-am_eric-0.81.mp3` (copied sibling)
- Visual plan: current vs voiceover and 04-visual-plan.md

## Voice Sync

All cue `data-start` values pinned to `voiceover/section-04-fifa-keeps-the-money/section-04-word-timings.json`
(199 words, monotonic except the known tail defect). The final three tokens "keeps the money."
regressed to 53.44-54.82 (whisper monotonicity error, already flagged by the visual plan); by position
they follow `auctioneer@60.86-61.32`, so the final payoff line is pinned at ~61.40 (estimated) and the
scene end is clamped to the real audio duration 62.101s. All other cues use JSON word starts as-is.

## Render-side adjustments vs the visual plan (documented decisions)

1. **4.6 pose substitution**: `rich_flex_gold_chain_sunglasses.png` pixels are a plain hands-behind-back
   smirk (known pose-catalog drift, same finding as Section 2) - no chain, no sunglasses. Used
   `boss_suit_sunglasses_sparkle.png` (smug glasses-adjust flex, the S2-approved substitute), MIRRORED so
   the raised arm stays fully in frame. Gold-chain detail dropped; the gold bars + sign carry the gag.
2. **4.8 scale geometry**: the sourced `balance-scale-brass-1.jpg` shows the LEFT pan hanging on chains and
   the RIGHT pan lying flat on the desk (not a level two-pan scale). Adapted: money sack drops INTO the real
   hanging pan (already reads heavy/low), green chips land beside the FIFA-DOES-PAY plate on the right, red
   tags bounce off that zone into the HOST PAYS THESE tray at bottom-left. The planned CSS beam tilt was
   dropped (no fake beam over the real static beam). Base graded bright (brightness 1.42) - museum shot is dark.
3. **4.5 safe placement**: the lake photo has no lawn; the safe sits large among the foreground lupin
   flowers (shore) with doormat + chimney puffs attached, instead of mid-frame "lakeshore lawn".
   The base is Lake Tekapo NZ (accepted manifest substitution - generic alpine look, no landmark/flags/people).
4. **4.4 ink pad color**: sourced pad is dark blue, not red (accepted manifest substitution); the red ink
   story is carried by the CSS stamp mark itself.
5. **4.5 pointing pose MIRRORED** (points left in pixels; WIT stands left and must point right at the safe).
   Flip lives on the inner img inside a wrapper so GSAP tweens never touch the scaleX(-1).
6. **4.1 baked-table crop**: `wit-mayor-signing.png` bakes its own signing desk; the pose is wrapper-cropped
   at the desk's front edge so it reads as WIT signing at the boardroom table (crop line = believable table edge).
7. **4.2 row-1 timing**: clause row 1 shows at 4.20 (vs cut 4.04) - sets pinned exactly on the clip-start
   boundary made the validator's GSAP resolution flaky; visually identical.

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice cue | What happens | Motion |
|---:|---:|---|---|---|
| 4.1 | 0.00 | (cut) | boardroom + mayor-WIT signing, pen scribble loop | static + loop |
| | 0.82 | contract | stack SLAMS + GOVERNMENT GUARANTEES + dust + 1% nudge | impact |
| | 2.32 | sign | SIGN HERE tab flips out | small impact |
| | 3.32 | together | (he did not read it) sticky + aim arrow | hard-show |
| 4.2 | 4.04 | FIFA | TV-wall + clause card + row 1 (+0.16) | hard-show |
| | 4.64/6.14/7.92 | TV/sponsor/ticket | green highlighter swipes 1-3 | draw |
| | 4.84/6.40/7.96 | money. x3 | cash bundle flies into safe, safe jiggles | flight |
| | 5.56/7.18 | FIFA 2/3 | clause rows 2/3 | hard-show |
| | 9.24 | spot | 3 red circles + shaky link + `spot the pattern` | pop |
| | 9.68 | pattern | green arrow draws + MONEY -> FIFA | impact |
| 4.3 | 10.14 | The host | construction base + WIT + red arrow draws | draw |
| | 10.54 | pays | BILLS -> HOST label | impact |
| | 11.16-14.02 | stadiums..zones | 4 bill chips slide down arrow; receipt unrolls + `16x STADIUM (RETROFIT) ......... $???` prints | slides + print |
| 4.4 | 15.00/15.64 | guarantee/three | header + red circle on No. 3 | hard-show/pop |
| | 16.72/17.92 | promises/exemption | clause types + yellow highlighter | type/draw |
| | 20.28 | none | PAYS: $0 grunge stamp + frame shake | impact |
| | 21.10/22.08/22.56 | some/All/them | 3 TAX tags; double red X sweep; `ALL of them.` | hard-show/impact/pop |
| 4.5 | 23.20 | by the way | postcard frame + lake + WIT pointing | hard-show |
| | 23.90/24.50 | lives/Zurich | FIFA lives here tag; caption types | hard-show/type |
| | 26.80 | non-profit | NON-PROFIT rosette stamps + flutter | impact |
| 4.6 | 27.76 | sits | chessboard + empty sign swings in | reveal |
| | 30.04/31.18/33.22 | chess/chess(2)/reserves | CHESS CLUB paints; strike + red FIFA + kick; $4B IN RESERVES | draw/impact/draw |
| | 32.12-32.42 | $4 billion | 4 gold bars pile up | bounce |
| 4.7 | 34.18 | The four years | vault + WIT + arrow + bundle stream flowing | ambient |
| | 35.42/36.34 | Qatar/brought | sub-chip; LED panel + REVENUE plate | hard-show |
| | 37.56-39.12 | $7.5B/revenue | digits tick to $7.5B; arrow widens step 1 | tick |
| | 40.72/41.76 | this/expects | sub-chip swap; plate flips to EXPECTS | flip |
| | 42.56-43.04 | $13/billion. | digits re-tick to $13B; arrow widens step 2 | tick |
| 4.8 | 44.82/45.14 | payday/ever | gold banner unfurls; sack drops into hanging pan + shake | impact |
| | 46.16/46.66 | fair/does | to be fair... aside; FIFA DOES PAY: plate | hard-show |
| | 48.46/49.08 | prize/running | green chips bounce in | bounce |
| | 51.62/52.18/52.94 | police/trains/stadium | red tags bounce OFF into the HOST PAYS THESE tray | arc bounce |
| 4.9 | 53.70 | So | full auction tableau present at cut | static |
| | 54.82/56.44 | revenue/bills | mini green/red recap arrows + labels | draw/impact |
| | 58.30 | auction | LOT tag + GAVEL BANG lines + shake | impact |
| | 58.86-61.3 | earth.. | auctioneer rake sweep (subtle rock) | loop |
| | 59.84 | pays | `the WINNER pays` | impact |
| | ~61.40 (est) | keeps the money | `the AUCTIONEER keeps the money` | impact |

## Render Review-Prevention Pass

- voice cue map completed: yes (word-timings JSON; tail regression handled per plan)
- big-scene sanity: 9 persistent bases, one idea each
- cue density: 1-2 changes per beat; lists staggered per word
- motion density: hard-show default; impact only on slam/stamp/X/banner/gavel/payoffs
- WIT density: exactly 1 pose per scene, held (device scenes let the device carry beats)
- WIT crop/collision: all 9 scenes snapshot-checked; 4.8 plate/chips moved off WIT's face; 4.9 payoff kept off face/paddle; face never cropped
- markup targets: red circles ring the three FIFAs on a CSS card (controlled); No. 3 circle on the header words; X sweeps cross the TAX tags
- scene differentiation: 9 distinct fresh bases, none reused
- HyperFrames mechanics: per-scene tracks 1-9, audio track 30, deterministic GSAP, hidden-at-cue-start sets, allow-overflow + overflow:visible on off-canvas WIT wrappers
- decisions beyond plan: 7 documented adjustments above

## Verification

- lint: 0 errors, 16 warnings (intentional duplicate bundle/bar/pose media reuse; chained boing/click micro-tween overlaps with overwrite:auto; file-size + Georgia-font advisories) - non-blocking
- validate: 0 errors, 0 warnings, 20 contrast advisories (validator measures text vs the photo BEHIND, ignoring the elements' own solid backgrounds: NON-PROFIT rosette core, HOST PAYS THESE tray face, gold em words in payoff lines) - non-blocking
- inspect: 0 layout issues across 54 samples
- snapshot QA: 4 rounds, all 9 scenes verified at ~50 cue timestamps; defects found+fixed: parser-corrupted 4.2 header (self-inflicted scripted-edit bug), EXPECTS plate vanish (fromTo opacity gotcha), 4.8 plate/chips on WIT's face, tags invisible in tray, receipt floating in sky (4.3), safe floating in lake + detached chimney puffs (4.5), gavel-bang lines on white WIT body (4.9), circle misalignment (4.2), small bars/bundles
- export: none (not requested)

## Notes

- Whisper tail regression (final 3 tokens) documented; only the last payoff cue is estimated (~61.40).
- Preview server started with `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=1000` in effect (not persistent across reboots).
