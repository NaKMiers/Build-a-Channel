# Section 8 Visual Plan - Outro: Like, Share, Subscribe

Video: `Why The Internet Is Full Of Garbage Now`
Section: `Section 8: Outro: Like, Share, Subscribe`
Status: `draft visual plan for approval (short outro end-card)`

> Timing note: NO `section-08-word-timings.json` yet (audio is 7.957s). Local times are ESTIMATED.
> `render` must GENERATE word-timings and re-pin the icon reveals.

## Video-Level Direction (for context - keep identical to master)

- Audience: A2-C1 English learners (interesting-English advantage).
- Renderer: HyperFrames (composites pre-made ISOLATED assets + transparent WIT poses).
- Visual grammar: real/real-looking base + giant WIT + handwritten labels. Generate-forward elsewhere; this
  short outro is intentionally LIGHT (no new generated/browsed assets - it reuses the calm S7 base and a
  tiny engine callback, and builds the YouTube-style buttons in render CSS).
- Mascot: WIT - round bald white head, thick black outline, big glasses, flat white body. Transparent
  cutouts in `assets/poses/`. Big + high.
- Tone on screen: calm, warm, dry - a quick friendly sign-off, NOT a frantic "smash the button" outro.

## Section Overview

- Section goal: a short, straightforward like/share/subscribe close, then a calm "see you next time" sign-off.
  It continues the calm, clear-eyed mood of the S7 payoff (deliberate continuity - same calm base).
- Duration: `7.957s`. Timing ESTIMATED (no word-timings yet).
- Scene count: `2` (an outro end-card; kept to two calm beats rather than rapid cuts).
- Scene-type rotation: CTA end-card / sign-off.
- Mascot arc: warm/offering -> chill sign-off.

## Scenes

### Scene 8.1 - "That's it for today. If this helped, like the video, share it with one person who needs it, and subscribe for more."

- **Local time:** `0:00-0:06.0` (est)
- **Role:** The CTA. A clean, calm end-card; the three asks appear one at a time on their words. Continues the calm S7 mood.
- **Composition / layout:** The calm bright-window base (reuse from S7.6/7.7). WIT center-left at ~1/2 frame, warm and offering. On the right, three YouTube-style buttons stack and pop in on their words: a `LIKE` button (thumb), a `SHARE` button (arrow), a red `SUBSCRIBE` button (bell). A tiny `slop-engine-loop` icon sits small in a bottom corner as a quiet callback ("the weird machine" we'll keep explaining). Buttons kept above the subtitle-safe bottom zone.
- **Elements:**
  - *Base:* `bright-window-calm-1.jpg` (reuse S7) - the same calm plant-by-a-bright-window, light and clean.
  - *Right (CSS):* three stacked buttons - `LIKE` (thumb), `SHARE` (arrow), red `SUBSCRIBE` (bell). YouTube-style, clean, well spaced.
  - *Bottom corner:* `slop-engine-loop.png` (reuse S4) - tiny, low-key, as a small brand callback.
- **Mascot:** pose `cheerful_presenting_fullbody`; center-left, ~1/2 frame, high; facing the buttons; expression warm, friendly "if this helped..."
- **On-screen text:** the three buttons carry the words; a small handwritten `"if this helped..."` upper-left on "if this helped".
- **Emotion:** warm, genuine, low-pressure.
- **Insight / joke:** a friendly, no-nonsense ask - not begging.
- **Linkage / eye path:** WIT (left, offering) -> the three buttons popping in order on the right.
- **Show-as-you-say:** base + WIT at 0:00; `"if this helped..."` on "if this helped"; `LIKE` pops on "like the video"; `SHARE` pops on "share it with one person who needs it"; red `SUBSCRIBE` pops on "subscribe for more"; tiny engine icon fades in low-corner.
- **Sound:** three soft UI "pops" (one per button); a gentle warm bed.
- **Color / contrast:** bright calm light; the red `SUBSCRIBE` button is the one strong color pop.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `bright-window-calm-1.jpg` | reuse | the calm S7 plant/window base (continuity) | base | reuse (S7) |
| `slop-engine-loop.png` | reuse | tiny "weird machine" brand callback, low corner | bottom corner, small | reuse (S4) |
| `cheerful_presenting_fullbody.png` | pose | WIT warm, offering the asks | center-left, ~1/2 frame | pose (library) |

(The `LIKE` / `SHARE` / `SUBSCRIBE` buttons and `"if this helped..."` are render CSS. Build the thumb /
arrow / bell as CSS shapes or tiny icon PNGs - do NOT rely on emoji glyphs; the 👍 emoji does not render in
the snapshot Chromium.)

### Scene 8.2 - "See you in the next one."

- **Local time:** `0:06.0-0:07.957` (est)
- **Role:** The calm sign-off. WIT gives a chill wave/peace; the three buttons settle; end the video on a warm, clear note.
- **Composition / layout:** Same calm bright-window base (continuity). WIT center at ~1/2 frame, relaxed sign-off. The three buttons settle smaller to the side; a friendly `"see you in the next one"` lands center/lower (subtitle-safe). Optional small `Why It Works` wordmark.
- **Elements:**
  - *Base:* `bright-window-calm-1.jpg` (reuse, continuation of 8.1).
  - *Side (CSS):* the three buttons from 8.1, settled/smaller (continuity).
  - *CSS:* `"see you in the next one"` handwritten; optional small `Why It Works` wordmark.
- **Mascot:** pose `peace_sign_calm_open_mouth`; center, ~1/2 frame, high; expression relaxed, friendly "see ya."
- **On-screen text:** `"see you in the next one"` on the line; optional small `Why It Works` wordmark.
- **Emotion:** calm, warm close.
- **Insight / joke:** a clean, dry sign-off - no hard sell.
- **Linkage / eye path:** WIT center (peace sign) -> the sign-off line.
- **Show-as-you-say:** WIT peace pose at 0:06; `see you in the next one` on the line; buttons settle.
- **Sound:** a soft closing chime; warm bed fades.
- **Color / contrast:** bright calm light; cream sign-off text.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `bright-window-calm-1.jpg` | reuse | the calm base (continuation of 8.1) | base | reuse (8.1/S7) |
| `peace_sign_calm_open_mouth.png` | pose | WIT relaxed sign-off | center, ~1/2 frame | pose (library) |

(The settled `LIKE`/`SHARE`/`SUBSCRIBE` buttons, `"see you in the next one"`, and the optional `Why It Works`
wordmark are render CSS.)

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `bright-window-calm-1.jpg` | reuse | 8.1 | 8.2 | the calm S7 base (continuity through the outro) |
| `slop-engine-loop.png` | reuse | 8.1 | - | tiny low-corner "weird machine" callback (S4) |
| `cheerful_presenting_fullbody.png` | pose | 8.1 | - | warm offering pose (library) |
| `peace_sign_calm_open_mouth.png` | pose | 8.2 | - | chill sign-off pose (library) |

Generate count: `0`. Browse bases: `0` new (reuses `bright-window-calm-1.jpg` from S7 for both scenes -
justified: the outro is one continuous calm moment continuing the S7 payoff, not a crutch). Cross-section
reuse: `slop-engine-loop.png` (S4) as a tiny callback. Poses: 2 library (`cheerful_presenting_fullbody`,
`peace_sign_calm_open_mouth`). Render-CSS: the `LIKE` / `SHARE` / `SUBSCRIBE` buttons (thumb / arrow / bell),
`"if this helped..."`, `"see you in the next one"`, and the optional `Why It Works` wordmark.

## Approval Checks

- each scene picturable from text alone: yes
- short outro kept to 2 calm beats (CTA card / sign-off), not rapid cuts or one dead static frame: yes
- every scene has a real/real-looking base (the calm window photo, reused for continuity): yes
- mascot big/high with a specific pose+expression per scene, varied (cheerful offering / peace sign-off): yes
- show-as-you-say: the three buttons reveal one per word (like / share / subscribe): yes
- every asset has type + description + filename + layout: yes
- no new generate or browse assets - reuses S7 base + S4 engine + 2 library poses; buttons are render-CSS: yes
- buttons avoid emoji glyphs (CSS shapes or tiny icon PNGs), subtitle-safe placement: yes
- tone stays calm/warm, not begging: yes
- no image-generation prompts here (handoff to visual-implement): yes
- timing ESTIMATED (no word-timings) - render must generate + re-pin: flagged
- in sync with master `04-visual-plan.md`: yes
