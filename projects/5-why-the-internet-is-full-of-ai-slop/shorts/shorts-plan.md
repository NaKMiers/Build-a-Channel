# Shorts Plan

Video: `Why The Internet Is Full Of Garbage Now` (`5-why-the-internet-is-full-of-ai-slop`)

Source skill: `shorts` (side sub-workflow from `combine`)

Status: `approved selection (3 shorts); building one at a time`

Owner selection (2026-06-30): build **3 shorts** - S1 Shrimp Jesus, S3 Six fingers & Coca-Coola, S6 You cannot arrest an incentive.

## Locked Rules (channel, owner-confirmed)

- Native portrait REBUILD `1080x1920`, never a crop/letterbox of the 16:9 master.
- COMPLETE standalone short, **NO CTA** / no "watch the full video" / no subscribe card. End on the short's own payoff.
- Platform-safe zone `x[60..880] y[220..1490]`: all readable content + WIT face inside it. WIT body may bleed off edges. Verify with a temporary `.safe-guide` overlay, then DELETE it before handoff.
- WIT big (~1/3-1/2 frame), face ABOVE the centered caption; approved pose PNGs only.
- Captions = distinct SUBTITLE style (white text + dark stroke on translucent dark pill `rgba(16,12,9,0.5)`), centered vertically (`top:50%`), 2-4 words, voice-synced. Punchline/payoff carried by cards, NOT duplicated in captions; captions clear before a card pops.
- Reuse each source section's real photo bases + WIT poses + Patrick Hand font (copy a minimal working set into the short's `assets/`; Windows junctions fail).
- VO regenerated per short in the approved voice (`am_eric / 0.84 / en-us`); captions from real whisper-tiny.en word timings of the short's OWN audio, tail re-timed monotonically.
- Ports `1100 + short number` (S01 -> 1101, S02 -> 1102, S03 -> 1103). Export to `output/shorts/short-0N-<kebab>.mp4`; ffprobe-verify `1080x1920` h264/aac.

## Short 01 - "Is any of this real?" (Shrimp Jesus)

- Source: Section 1 (Hook). Target ~30s. Port `1101`. Folder `shorts/short-01-is-any-of-this-real/`.
- One idea: your feed is quietly filling with fakes, and nobody ordered it.
- Cold open (hook on word 1): WIT holding a phone, "open any feed, scroll for 10 seconds."
- VO (trimmed/assembled from S1, exact script wording):
  > Pick up your phone, open any feed, and scroll for ten seconds. Now be honest: how much of that was actually made by a human? Somewhere in that feed there is a photo of a shrimp shaped like Jesus, a news story about an event that never happened, and a hit song by a band that does not exist. The internet is filling up with garbage. Cheap, fake, mass-produced garbage. And the strange part is - nobody told it to.
- Scene-by-scene (portrait):
  1. Phone feed + WIT `holding_phone_pointing_smile` (right), label "SCROLL FOR 10s". Hook caption.
  2. "How much is REAL?" - WIT `skeptical_side_eye_doubtful`, "% HUMAN?" chip on "human".
  3. Shrimp Jesus post card (`shrimp-jesus.jpg`, "AMEN 47K") pops on "shrimp shaped like Jesus"; WIT `cringe_uneasy_drool`.
  4. Fake-news card (`fake-news-card.png`) + red "DIDN'T HAPPEN" on "never happened".
  5. Fake-band card (`fake-band-card.png`) + "0 REAL MEMBERS" on "does not exist".
  6. Payoff: grey-sludge tint rising (`grey-sludge-flood-1.jpg`), big "GARBAGE" smash + "cheap / fake / mass-produced" chips; WIT `worried_uneasy_wide_eyes`. Final card "NOBODY TOLD IT TO." Hold.
- Signature device reused: feed-of-fakes (the 3 absurd posts) pinned to their spoken words, Shrimp Jesus hero, grey-sludge payoff (S1/S8 motif).
- Payoff (no CTA): "nobody told it to."
- Assets: `shrimp-jesus.jpg`, `fake-news-card.png`, `fake-band-card.png`, `grey-sludge-flood-1.jpg`, bases `couch-phone-evening-1.jpg` / `dark-room-phone-glow-1.jpg` / `social-scroll-livingroom-1.jpg`; poses above; `patrick-hand-latin.woff2`.

## Short 02 - "Six fingers & Coca-Coola" (how to spot slop)

- Source: Section 3 (What Slop Actually Is). Target ~30s. Port `1102`. Folder `shorts/short-02-six-fingers-coca-coola/`.
- One idea: slop looks fine for half a second - here are the tells.
- Cold open: "So what actually counts as slop?" WIT `pondering_skeptical_hand_on_chin`, the SLOP MACHINE motif.
- VO (trimmed/assembled from S3, exact script wording):
  > So what actually counts as slop? It looks fine for half a second. Quick glance, looks normal. Look closer, and it falls apart. The hand has six fingers. The words are gibberish. A giant brand spends millions on a holiday ad and misspells its own name as "Coca-Coola." That really happened. Looks fine, costs them nothing, made by the thousand. That is slop.
- Scene-by-scene (portrait):
  1. SLOP MACHINE / influencer-perfect post; "LOOKS FINE FOR HALF A SECOND". WIT `pondering_skeptical_hand_on_chin`.
  2. "Look closer" - magnify; WIT `skeptical_side_eye_doubtful`.
  3. Six-finger hand (`ai-extra-fingers-hand.png`) + red "6 FINGERS" circle on "six fingers".
  4. Gibberish sign (`gibberish-melting-sign.png`) on "gibberish".
  5. "Coca-Coola" ad fail (`coca-coola-ad-fail.png`) + red ring on the misspelling on "Coca-Coola"; WIT `annoyed_disgusted_open_frown`; "THAT REALLY HAPPENED" beat.
  6. Payoff card: "LOOKS FINE · COSTS THEM NOTHING · MADE BY THE THOUSAND" -> stamp "THAT IS SLOP"; WIT `unimpressed_smirk_closeup`. Hold.
- Signature device reused: the SLOP MACHINE motif + the three tells (six fingers / gibberish / Coca-Coola) pinned to their words; CERTIFIED-SLOP-style stamp on the payoff.
- Payoff (no CTA): "that is slop."
- Assets: `ai-extra-fingers-hand.png`, `gibberish-melting-sign.png`, `coca-coola-ad-fail.png`, `ai-influencer-perfect.png`, `slop-machine.png`, `certified-slop-stamp.png`, bases `cozy-laptop-desk-1.jpg` / `social-scroll-livingroom-1.jpg` / `holiday-street-1.jpg`; poses above; font.

## Short 03 - "You cannot arrest an incentive"

- Source: Section 6 (It's Not AI's Fault, And Not A Plot). Target ~28s. Port `1103`. Folder `shorts/short-03-arrest-an-incentive/`.
- One idea: it isn't a conspiracy - it's an incentive, and you cannot arrest one.
- Cold open: "This is not a secret plot." WIT `skeptical_side_eye_doubtful`, conspiracy corkboard.
- VO (trimmed/assembled from S6, exact script wording):
  > This is not a secret plot. There is a popular idea online called "dead internet theory," which says the government is secretly filling the web with bots to control your mind. Relax. It's dumber than that. Nobody is in charge. No villain pressed a button. The garbage spreads on its own, because the money rewards it. And that is the uncomfortable part. You cannot arrest an incentive.
- Scene-by-scene (portrait):
  1. "NOT A SECRET PLOT" - conspiracy corkboard (`corkboard-redstring-1.jpg`); WIT `skeptical_side_eye_doubtful`.
  2. "DEAD INTERNET THEORY" title + tinfoil hat (`tinfoil-hat.png`) on "dead internet theory".
  3. "Relax. It's dumber than that." - giant red X over the board; WIT `deadpan_unimpressed_half_lidded`.
  4. Empty villain throne (`empty-villain-throne.png`) on "nobody is in charge / no villain".
  5. "the money rewards it." - glowing gold $ (`uncuffable-incentive.png`); WIT `presenting_open_palm_talking`.
  6. Payoff: "YOU CANNOT ARREST AN INCENTIVE" over the gold $ with open handcuffs; WIT `pointing_at_viewer_serious_accusing`. Hold.
- Signature device reused: conspiracy corkboard named then crossed out (S6 "name it, then puncture it"), empty villain throne, the uncuffable gold-$ incentive.
- Payoff (no CTA): "you cannot arrest an incentive."
- Assets: `corkboard-redstring-1.jpg`, `tinfoil-hat.png`, `empty-villain-throne.png`, `uncuffable-incentive.png`, bases `courtroom-1.jpg` / `empty-boardroom-1.jpg` / `dark-spotlight-stage-1.jpg`; poses above; font.

## Build / Export Log

- DONE short-01 built (port 1101): VO 20.651s, root 21.85s, 6 scenes, 0 lint errors (1 reuse warn). Clean whisper timings (no tail glitch). Safe-guide QA passed + removed.
- DONE short-02 built (port 1102): VO 18.325s, root 19.5s, 6 scenes, 0 lint errors (1 reuse warn). Tail glitch on "slop." end (start 17.92 correct) - stamp pinned to 17.92, root clamped. Scene-2 post centered + scene-3 circle nudged after snapshot QA.
- DONE short-03 built (port 1103): VO 19.051s, root 20.3s, 6 scenes, 0 lint errors (2 reuse warns). Tail glitch on "incentive." end (start 18.5 correct) - payoff pinned to 18.5, root clamped. Dropped duplicate scene-1 label; safe-guide QA passed + removed.
- DONE export (owner-approved 2026-07-01) to `output/shorts/`, all ffprobe-verified `1080x1920` / h264 / 30fps / aac:
  - `short-01-is-any-of-this-real.mp4` - 21.89s, 4.6 MB
  - `short-02-six-fingers-coca-coola.mp4` - 19.52s, 4.2 MB
  - `short-03-arrest-an-incentive.mp4` - 20.32s, 4.1 MB

Status: `3 shorts exported; complete`. Preview servers ran on 1101/1102/1103. No long-form content was edited. Does not block caption (done) / packaging / upload / learning.
