# Section 8 Render Implementation

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 8: Outro - Like, Share, Subscribe`

Status:
`built (v2 gamified CTA rebuild), ready for review` (preview only; no MP4 export requested)

## Result

- Preview project: `section-previews/section-08-outro-like-share-subscribe/`
- Source: `visual-plan` S8 + REAL word timings (`voiceover/section-08-outro-like-share-subscribe/section-08-word-timings.json`)
- Port: `1008`
- Studio URL: `http://localhost:1008/`
- Direct composition URL: `http://localhost:1008/api/projects/section-08-outro-like-share-subscribe/preview/comp/index.html`
- Runtime: `7.957s` (root `data-duration`, matches the section voiceover)
- Voiceover: `section-08.mp3` (am_eric / David23 / 0.80), wired as `<audio data-track-index="30">`
- Visual plan: `visual-plan/section-08-outro-like-share-subscribe/section-08-outro-like-share-subscribe-visual-plan.md`
- Composition id: `Section08Outro`

## v2 rebuild - why

The first build was a flat, static CTA (three pills that just popped in) and read as boring. The owner
asked for an over-the-top, gamified end-card: a fake YouTube screen popup with a mouse cursor that flies
in and CLICKS the like and subscribe buttons, the buttons wiggle/boing and flip to "Liked" / "Subscribed",
the bell rings, and confetti pops. This rebuild replaces the whole section with that interactive CTA.

## Word Timings (generated, not estimated)

Per the Voice-Sync Timing Contract, the CTA actions are pinned to the GENERATED real word timings
(`voiceover/.../section-08-word-timings.json`, transformers.js / whisper-tiny.en). Root clamped to the
real `7.957s`.

## Choreography (single continuous scene, deterministic GSAP)

One scene/track keeps the YouTube card persistent for the whole 7.957s (no hard cut), so the card holds
its liked + subscribed state into the sign-off.

| t (s) | Voice cue | Action |
|---:|---|---|
| 0.30 | (open) | fake YouTube card pops in (back.out); enthusiastic-point WIT shown |
| 1.42 | "if this helped" | "if this helped..." handwritten caption |
| 1.62 | - | cursor flies in from bottom-right, moves to the LIKE pill |
| 2.24 | "like the video" | cursor click-dip + LIKE pill BOING; flips to blue "Liked" (thumb + count 247 -> 248) |
| 2.50 | - | cursor moves to the SHARE pill |
| 3.14 | "share it" | cursor click-dip + SHARE pill BOING; "Link copied!" green toast pops |
| 3.60-5.20 | - | gold glow ring PULSES around SUBSCRIBE (3 pulses) to pull the eye |
| 4.55 | - | cursor moves to the SUBSCRIBE button |
| 5.22 | "subscribe" | cursor click-dip + SUBSCRIBE BOING; red "SUBSCRIBE" morphs to grey "SUBSCRIBED" + bell that RINGS; confetti bursts (12 pieces); the channel line flips to "Welcome to the channel!"; green "Thanks!" floats up (no fake count) |
| 5.80 | - | cursor drifts off-screen and fades |
| 6.40 | - | WIT cross-fades from enthusiastic-point to calm peace sign |
| 6.66 | "see you in the next one" | "see you in the next one." caption + WHY IT WORKS wordmark |

GSAP helpers: `boing` (combined scale-up + rotate wiggle + settle, single transform set so no overwrite
fight), `clickdip` (cursor scale dip), `moveTo` (animates `left`/`top` px), `popIn`, `show`, `fadeIn/Out`.

## The fake YouTube card (all CSS, no new assets)

- App bar: red play-logo box (rounded red rect + white triangle) + "WhyTube" wordmark + a search-bar stub
  (parody UI; our own channel branding, not a real YouTube screen-grab).
- Video thumbnail: dark gradient + big play triangle + "WHY IT WORKS" + a "10:42" duration chip.
- Title: "Why The Internet Is Full Of Garbage Now".
- Channel row: the REAL channel avatar (`channel-avatar.png` from `_shared/assets/brand`, yellow circle),
  "Why It Works", a non-numeric channel line, and the SUBSCRIBE button (two stacked states cross-faded:
  red `SUBSCRIBE` -> grey `SUBSCRIBED` + bell).
- No fake subscriber count (the channel is small): the line reads "Subscribe for more" and flips to
  "Welcome to the channel!" on subscribe, with a floating green "Thanks!" - no invented numbers.
- Action row: LIKE pill (two stacked states: white "247" -> blue "248" liked, a humble count that ticks)
  and a SHARE pill.
- Mouse cursor: inline SVG arrow (white fill, dark stroke, drop-shadow) animated via `left`/`top`.
- Confetti: 12 CSS squares bursting from the subscribe button on click (function-based per-piece x/y).
- Icons are inline-SVG (filled thumbs-up / share-arrow / notification bell, fill currentColor so they
  inherit each button's color), NOT emoji - emoji do not render in snapshot Chromium.
- Video duration chip reads "5:00" (realistic for the channel).

## Render Review-Prevention Pass

- voice cue map completed: yes (each click lands on its spoken word: like 2.24, share 3.14, subscribe 5.22)
- motion density checked: the cursor + boing + confetti are the intentional "loud" payoff the owner asked for; everything settles by the sign-off
- WIT density: 1 WIT, cross-fading enthusiastic-point (presenting the card) -> calm peace sign for the sign-off; on the left, clear of the card
- WIT/card collision checked: yes - card occupies the right 2/3 (left:720), WIT on the far left, no overlap; cursor lands on each button (verified in snapshots at 2.3 / 3.2 / 4.6 / 5.5)
- markup target checked: captions + wordmark top-left clear of WIT's head and the card
- HyperFrames mechanics checked: single track, deterministic GSAP, audio clip, synchronous timeline registration

## Render decisions beyond the visual plan

- Full creative rebuild into an interactive fake-YouTube CTA (owner request to make it less boring / more superficial-fun).
- No new generated or browsed assets - the entire card, cursor, buttons, and confetti are CSS/SVG; only the two WIT poses and the base photo are reused from the library.
- Class-collision fix during build: the confetti pieces and the thumb-icon cuff both used `.cf`, so the confetti color rules bled into the thumb (green cuff). Renamed confetti to `.cfp`.

## Assets

- Shared asset folder: `projects/5-why-the-internet-is-full-of-ai-slop/assets/`
- Section assets: local `assets` junction -> `../../assets` (verified resolves)
- New assets: `channel-avatar.png` (copied in from `.agents/_shared/assets/brand/`); the rest is CSS/SVG
- Reused: `bright-window-calm-1` (base), poses `enthusiastic_point_big_smile` (CTA) + `peace_sign_calm_open_mouth` (sign-off)
- Attribution: `assets/ATTRIBUTION.md`

## Verification

- lint: `0 error(s), 6 warning(s)` - all `overlapping_gsap_tweens` on the intentional boing/click micro-sequences (they carry `overwrite:"auto"`) and the glow fade-out overlapping its last pulse. Non-blocking.
- validate: `0 error(s), 0 warning(s)` (5 contrast advisories, all the gold "W" avatar glyph - false positive; the avatar reads fine)
- inspect: `0 layout issues across 7 sample(s)`
- direct preview snapshots: full pass (card pop 0.6, like-click 2.3, share-toast 3.2, glow pulse 4.6, subscribed+confetti 5.5, sign-off 7.0) - cursor lands on each button, states fire correctly
- server: `http://localhost:1008/` responds `200`
- export/render: not requested (preview only)

## Notes

- No MP4/WebM exported (not requested).
- The "YouTube" card is a parody UI with our own branding (WhyTube logo, Why It Works channel) - no real YouTube screen-grab, no real channel.
- Button icons + cursor are CSS/SVG by design (emoji do not render in snapshot Chromium).
- Word-timings file is the source of truth; if S8 wording changes, regenerate timings and re-pin the click beats.
