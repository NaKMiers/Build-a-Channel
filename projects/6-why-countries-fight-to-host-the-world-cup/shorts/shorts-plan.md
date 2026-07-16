# Shorts Plan

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)` (`6-why-countries-fight-to-host-the-world-cup`)

Source skill: `shorts` (side sub-workflow from `combine`)

Status: `auto-selected 3 shorts - owner delegated full autonomy (2026-07-16, "just do it yourself"); building + exporting all`

Owner selection (2026-07-16): the owner asked to run shorts on video 6, export, then packaging, autonomously without questions. Auto-selected **3 shorts** (one per source section for variety): S1 the Ferrari reframe (Section 2), S2 the only auction where the winner pays (Section 4), S3 the stadium full of buses (Section 6).

## Linux-adapted toolchain note (2026-07-16)

This box is Linux, not the original Windows box in skill memory. Two adaptations, both preserving the locked rules:

- **Voiceover:** kokoro TTS is not installed here (no pip). Instead each short's VO is **sliced from the real recorded combined voiceover** (`hyperframes/full-video/combined-voiceover.mp3`) at sentence boundaries using `voiceover/combined-segments.json`. This is literally the same approved voice and same words - cleaner than re-generating - and gives exact caption timings for free (no whisper, no tail-glitch re-timing). Contiguous spans are one slice; assembled shorts concat a few sentence slices at their silent boundaries.
- **Captions timed from the real segment boundaries** in `combined-segments.json` (already aligned to the real audio), not estimated.
- ffmpeg via `@ffmpeg-installer/ffmpeg`; ffprobe via `ffprobe-static`; render via `npx hyperframes@0.6.76` + system `google-chrome` (same path the v6 final MP4 used on this box). Preview-local `assets` is a **symlink** to the shared `../../assets` (symlinks work on this box; verified by the section renders).

## Locked Rules (channel, owner-confirmed)

- Native portrait REBUILD `1080x1920`, never a crop/letterbox of the 16:9 master.
- COMPLETE standalone short, **NO CTA** / no "watch the full video" / no subscribe card. End on the short's own payoff.
- Platform-safe zone `x[60..880] y[220..1490]`: all readable content + WIT face inside it. WIT body may bleed off edges. Verify with a temporary `.safe-guide` overlay, then DELETE it before handoff.
- WIT big (~1/3-1/2 frame), face ABOVE the centered caption; approved pose PNGs only.
- Captions = distinct SUBTITLE style (white text + dark stroke on translucent dark pill `rgba(16,12,9,0.5)`), centered vertically (`top:50%`), 2-4 words, voice-synced. Punchline/payoff carried by cards, NOT duplicated in captions; captions clear before a card pops.
- Reuse each source section's real photo bases + WIT poses + Patrick Hand font.
- Ports `1100 + short number` (S01 -> 1101, S02 -> 1102, S03 -> 1103). Export to `output/shorts/short-0N-<kebab>.mp4`; ffprobe-verify `1080x1920` h264/aac.

## Short 01 - "It's Not An Investment. It's A Ferrari." (source: Section 2)

- Source: Section 2 (Reframe). Combined segments `22-30` (contiguous). Target ~21s. Port `1101`. Folder `shorts/short-01-not-an-investment/`.
- One idea: hosting the World Cup is not an investment, it is a purchase - and the real question is who pays.
- Cold open (hook on word 1): "Hosting the World Cup is not an investment. It is a purchase."
- VO (exact script wording, sliced from the combined audio):
  > Hosting the World Cup is not an investment. It is a purchase. Nobody buys a Ferrari to make money. You buy a Ferrari to be SEEN in a Ferrari. Countries do the same. Except the Ferrari is a football tournament, the price is billions... and the credit card is yours. The taxpayer's. So the real question is never "will it pay off". It is "who pays".
- Scene-by-scene (portrait):
  1. `desk-darkwood-1.jpg` base; `INVESTMENT` red cross-out -> `PURCHASE` stamp; WIT `skeptical_side_eye_doubtful`.
  2. `showroom-floor-1.jpg` base; `red-supercar-generic.png` hero + `price-tag-blank.png` ("PRESTIGE"); WIT `boss_suit_sunglasses_sparkle`; label "to be SEEN" on "SEEN".
  3. `marble-counter-1.jpg` base; `credit-card-taxpayer.png` hero; WIT `panic_hands_on_cheeks_scream`; label "the card is YOURS".
  4. Payoff `desk-darkwood-1.jpg` base; big payoff card `WHO PAYS?`; WIT `lecturing_finger_raised_eyes_closed`. Hold.
- Payoff (no CTA): "who pays".
- Assets: `desk-darkwood-1.jpg`, `showroom-floor-1.jpg`, `marble-counter-1.jpg`, `red-supercar-generic.png`, `price-tag-blank.png`, `credit-card-taxpayer.png`, `trophy-gold-parody.png`; poses above; font.

## Short 02 - "The Only Auction Where The Winner Pays" (source: Section 4)

- Source: Section 4 (FIFA Keeps The Money). Combined segments `54-58` + `64-65` + `72-74` (assembled). Target ~22s. Port `1102`. Folder `shorts/short-02-winner-pays/`.
- One idea: FIFA keeps every revenue stream, the host pays every bill - the only auction where the winner pays.
- Cold open: "FIFA keeps the TV money. FIFA keeps the sponsor money. FIFA keeps the ticket money."
- VO (exact script wording, assembled from the combined audio):
  > FIFA keeps the TV money. FIFA keeps the sponsor money. FIFA keeps the ticket money. Feel free to spot the pattern. The host pays for the stadiums. The security. The transport. The fan zones. It sits in the same legal category as a local chess club. A chess club with around four billion dollars in reserves. So one side gets the revenue. The other side gets the bills. FIFA invented the only auction on Earth where the winner pays... and the auctioneer keeps the money.
- Scene-by-scene (portrait):
  1. `vault-door-1.jpg` base; `gold-safe-fat.png` + `cash-bundle-generic.png`; chips "TV / SPONSOR / TICKETS" -> "FIFA KEEPS IT"; WIT `deadpan_unimpressed_half_lidded`.
  2. `stadium-construction-crane-1.jpg` base; `contract-stack-guarantees.png` + `receipt-endless-roll.png`; red chips "STADIUMS / SECURITY / TRANSPORT"; WIT `shocked_sweating_dismayed`.
  3. `chessboard-closeup-1.jpg` base; `wood-sign-hanging-blank.png` ("CHESS CLUB"); big "$4,000,000,000"; WIT `mildly_surprised_hand_at_chin`.
  4. Payoff `auction-gavel-1.jpg` base; `auctioneer-at-podium.png` + `wit-auction-winner-paddle.png`; payoff card "WINNER PAYS. AUCTIONEER KEEPS IT." Hold.
- Payoff (no CTA): "and the auctioneer keeps the money".
- Assets: `vault-door-1.jpg`, `stadium-construction-crane-1.jpg`, `chessboard-closeup-1.jpg`, `auction-gavel-1.jpg`, `gold-safe-fat.png`, `cash-bundle-generic.png`, `contract-stack-guarantees.png`, `receipt-endless-roll.png`, `wood-sign-hanging-blank.png`, `auctioneer-at-podium.png`, `wit-auction-winner-paddle.png`; poses above; font.

## Short 03 - "The Stadium Was Full Of Buses" (source: Section 6)

- Source: Section 6 (The Morning After). Combined segments `97-106` (contiguous). Target ~29s. Port `1103`. Folder `shorts/short-03-full-of-buses/`.
- One idea: after the party the host keeps a "white elephant" - and one stadium ended up full of buses.
- Cold open: "Then the tournament ends. The fans fly home. And the stadiums stay."
- VO (exact script wording, sliced from the combined audio):
  > Then the tournament ends. The fans fly home. And the stadiums stay. English has a perfect phrase for what happens next: a "white elephant". A huge, expensive thing you cannot really use - but you must keep feeding. Brasilia built a stadium that cost at least five hundred fifty million dollars. Beautiful. Enormous. One problem: the city has no big football club. So by 2015, its parking lot was being used... by city buses. Rows of them. The stadium was finally full. Full of buses.
- Scene-by-scene (portrait):
  1. `stadium-empty-seats-dawn-1.jpg` base; label "THE STADIUMS STAY"; WIT `sleepy_yawning_open_mouth`.
  2. `stadium-modern-exterior-1.jpg` base; `elephant-stadium-pet.png` + `feeding-bowl-maintenance.png`; label "WHITE ELEPHANT" + gloss "huge. useless. keep feeding."; WIT `mildly_surprised_hand_at_chin`.
  3. `stadium-empty-seats-dawn-1.jpg` base; big "$550,000,000"; chip "NO BIG CLUB"; WIT `shrug_both_hands_up_smile`.
  4. Payoff `stadium-parking-lot-1.jpg` base; `bus-row-parked.png`; payoff card "FULL OF BUSES."; WIT `deadpan_unimpressed_half_lidded`. Hold on the laugh.
- Payoff (no CTA): "Full of buses."
- Assets: `stadium-empty-seats-dawn-1.jpg`, `stadium-modern-exterior-1.jpg`, `stadium-parking-lot-1.jpg`, `elephant-stadium-pet.png`, `feeding-bowl-maintenance.png`, `bus-row-parked.png`; poses above; font.

## Build / Export Log

Status: `3 shorts built + exported; complete`. No long-form section content was edited. Does not block caption (done) / packaging / upload / learning.

- DONE short-01 built: VO 21.06s (segs 22-30 sliced from combined audio), root 22.3s, 4 scenes, `lint` 0 err (1 benign `duplicate_media_discovery_risk` reuse warn on the bookend desk base), `validate` 0 err (5 WCAG contrast warns = false positives on gold bigword + dark-on-tag "PRESTIGE"). Snapshot QA passed: WIT faces above centered captions, payoff `WHO PAYS?` card clears the caption, all content in the safe zone.
- DONE short-02 built: VO 25.84s (segs 54-58 + 64-65 + 72-74 assembled), root 27.1s, 4 scenes, `lint` 0 err 0 warn, `validate` 0 err (5 contrast false positives). Two review fixes applied: replaced the clipped CHESS-CLUB wooden-sign text with a clean `$4B` + `...in reserves` chip on the chessboard base; removed a scene-4 hand label that duplicated its caption verbatim ("one side gets the bills" is carried by the caption only).
- DONE short-03 built: VO 28.81s (segs 97-106 sliced), root 30.1s, 4 scenes, `lint` 0 err (1 benign reuse warn on the dawn-seats base), `validate` 0 err (10 contrast false positives on gold text). Snapshot QA passed; white-elephant-stadium hero + `FULL OF BUSES.` payoff card land cleanly.
- Audio: sliced from `hyperframes/full-video/combined-voiceover.mp3` via ffmpeg using `voiceover/combined-segments.json` (same approved voice, exact caption timings). `voiceover/short-0N.mp3` + `short-0N-cues.json` saved per short.
- Export: `hyperframes@0.6.76 render` (system google-chrome, screenshot capture path) to silent MP4, then muxed the short's own voiceover in with ffmpeg (`-c:v copy -c:a aac`, no `-shortest`, so the payoff hold is preserved). Native mux was skipped because the render-time comp server does not proxy the `voiceover/` path in this env (served fine standalone; harmless here). All ffprobe-verified `1080x1920` / h264 + aac / 30fps:
  - `output/shorts/short-01-not-an-investment.mp4` - 22.30s, ~3.4 MB
  - `output/shorts/short-02-winner-pays.mp4` - 27.10s, ~4.7 MB
  - `output/shorts/short-03-full-of-buses.mp4` - 30.10s, ~4.8 MB
- Short cover frames captured from each payoff beat -> `output/thumbnails/short-01.png` / `short-02.png` / `short-03.png` (1080x1920) for packaging.
- Preview ports 1101-1103 available on demand via each short's `npm run dev`; not left running.
