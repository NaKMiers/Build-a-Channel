# Section 1 Visual Plan

Video:
`Why Everything Is a Subscription Now`

Section:
`Section 1: Hook: It's More Than You Think`

Status:
`draft visual plan for approval`

## Section Goal

Open a curiosity gap about the viewer's own money in the first ~5s, pay the title promise ("you rent everything") by ~second 18, and tease the device motif. WIT is the suspicious audience surrogate.

## Source Inputs

- Script: `02-script.md` Section 1
- Voiceover: `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.8.mp3`
- Script promise: you are paying for more subscriptions than you can name; you rent your whole life
- Section duration: `23.509s` (David23 / am_eric / 0.8)

## Narration

```text
Quick question. How many subscriptions are you paying for right now?
Whatever number you guessed... it's higher. It's always higher.
Right now, money is quietly leaving your account every month, for stuff you forgot you own. An app. A "free" trial that stopped being free. A show you watched once.
Your free trial of owning things just expired.
You don't buy things anymore. You rent your whole life. One payment at a time.
```

## Visual Direction

- Big-scene/cue rhythm: 3 big scenes, 7 cue states (hook density)
- Big scene rhythm: phone bank-app → screens that own you → rent-your-life payoff
- Cue-state count: 7
- Main visual metaphor: glowing screens silently charging you; one circled mystery charge
- WIT emotional path: suspicious → shocked → deadpan → trapped
- WIT density: 4 beats total (BS1 ×1, BS2 ×2, BS3 ×1)
- Motion density: hard-show labels; impact only on the red circle, the EXPIRED stamp, and the payoff
- Real-life texture: real CC0 phone-in-hand + real lived-in desk bases
- Real image references: base-phone-blank-inhand.jpg, base-desk-devices.jpg
- Generated/support assets: none (bank-app + device screens built in CSS — real-UI illustration)
- Viewer attention strategy: a question about THEIR money + a red mystery charge they cannot identify
- Retention risk: a generic "subscriptions" intro that feels like an ad
- Visual fix: make it personal and specific fast (a bank statement that looks like theirs, one charge circled with a glowing `?`)
- Red markup: one red circle + glowing `?` on a mystery charge; one EXPIRED stamp
- Motion rule: ordinary labels hard-show on the spoken word; impact reserved for the circle, stamp, payoff

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|
| BS1 Phone bank-app | 0.0–7.5s | "Quick question…it's always higher." | Real phone (blank screen) holding a CSS bank-statement list of small monthly charges on a softly-blurred real surface | Pay the title promise personally; plant the mystery charge | When narration moves from "how many" to "money leaving for stuff you forgot" | base-phone-blank-inhand.jpg + CSS bank UI | assets/visual-references/section-01-hook/base-phone-blank-inhand.jpg |
| BS2 Screens that own you | 7.5–17.0s | "Right now, money is quietly leaving…just expired." | Real desk; laptop + TV + smartwatch + car screen (CSS) flick on one by one, each with a tiny charge | Show the spread from one phone to all devices; land the deadpan gag | When narration turns to the thesis ("you don't buy things anymore") | base-desk-devices.jpg + CSS device screens | assets/visual-references/section-01-hook/base-desk-devices.jpg |
| BS3 Rent-your-life payoff | 17.0–23.509s | "You don't buy things anymore…One payment at a time." | Same desk darkened; giant WIT trapped among floating padlock/charge chips; payoff label | Land the thesis as an emotional gut-punch | End of section | base-desk-devices.jpg (darkened) + WIT + CSS chips | assets/visual-references/section-01-hook/base-desk-devices.jpg |

## Cue State Timeline

Timing is `estimated` (no word-timings JSON yet — render should generate `section-01-word-timings.json` via the whisper prefix and re-pin these cues).

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | Motion Type | WIT Pose / Size / Safe Crop | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|---|
| C1 | 0.0–2.0 | "Quick question." | BS1 | Phone + bank-app list fades in; handwritten "HOW MANY?" | phone base | hard-show | none | "HOW MANY?" (top-left, subtitle-safe) | CSS bank UI | establish the personal frame |
| C2 | 2.0–4.5 | "How many subscriptions are you paying for right now?" | BS1 | WIT leans in big from right, squinting at the screen | phone + list | hard-show | wit-pose-suspicious, ~1/3 frame, right side peek, head+torso in frame | — | WIT png | suspicion = audience surrogate |
| C3 | 4.5–7.5 | "it's higher. It's always higher." | BS1 | One charge row gets a red circle + glowing `?`; the list quietly scrolls one more row in | phone + WIT | impact (stamp circle) | wit-pose-suspicious holds | red circle + glowing `?` on ONE charge row | CSS | plant the mystery charge |
| C4 | 7.5–11.5 | "money is quietly leaving…for stuff you forgot you own." | BS2 | Cut to desk; laptop + TV screens flick on, each a tiny "−\$" chip | desk base | hard-show | none | small "−\$" chips on each screen | CSS device screens | show the spread |
| C5 | 11.5–13.5 | "An app. A 'free' trial… A show you watched once." | BS2 | Three quick item chips hard-show in rhythm: `an app` · `a "free" trial` · `a show` | desk + screens | hard-show (staccato) | wit-pose-shocked, ~1/3 frame, left edge, head+torso safe | `an app` / `a "free" trial` / `a show` | CSS | staccato list = the pile-up |
| C6 | 13.5–17.0 | "Your free trial of owning things just expired." | BS2 | Deadpan pop-up card stamps on: `FREE TRIAL OF OWNING THINGS — EXPIRED` | desk + screens | impact (stamp) | wit-pose-deadpan-side-eye, ~1/3 frame, beside the pop-up | `FREE TRIAL OF OWNING THINGS · EXPIRED` | CSS | the running-gag punchline |
| C7 | 17.0–23.509 | "You don't buy things anymore. You rent your whole life. One payment at a time." | BS3 | Desk darkens; GIANT WIT trapped among floating padlock + charge chips; payoff label rises (subtitle-safe) | desk dim | impact (payoff) then static | wit-pose-trapped-by-app-screen, ~1/2 frame, high+centered, only legs cropped | `YOU RENT YOUR WHOLE LIFE` / small `one payment at a time` | WIT + CSS chips | land the thesis emotionally |

## WIT Pose Plan

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop / Margin | Why WIT Is Needed |
|---|---:|---|---|---|---|---|
| C2–C3 | 2.0–7.5 | suspicion | wit-pose-suspicious.png | right side, leaning toward phone, ~1/3 frame | head+glasses+torso in frame; only legs/edge cropped | audience surrogate squinting at the mystery charge |
| C5 | 11.5–13.5 | shock | wit-pose-shocked.png | left edge, ~1/3 frame | head+shoulders safe | reaction to screens lighting up everywhere |
| C6 | 13.5–17.0 | dry | wit-pose-deadpan-side-eye.png | beside the pop-up, ~1/3 frame | face/glasses clear of the card | sell the deadpan gag |
| C7 | 17.0–23.5 | trapped | wit-pose-trapped-by-app-screen.png | high + centered, ~1/2 frame | only legs cropped; face never covered by payoff text | emotional gut-punch of "you rent your whole life" |

WIT density note:

- Total WIT beats: 4
- WIT beats per big scene: BS1 ×1 (suspicious holds across C2–C3), BS2 ×2 (shocked, deadpan), BS3 ×1 (trapped)
- Any big scene above `2` WIT beats, and why: none
- Cue states intentionally without WIT: C1 (establish phone), C4 (show device spread)

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion Type | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|---|
| C1 | 0–2 | `HOW MANY?` | hard-show | top-left near phone | frames the question | not over the bank list |
| C3 | 4.5–7.5 | red circle + glowing `?` | impact | ONE charge row | plants the mystery charge | no extra red marks on other rows |
| C5 | 11.5–13.5 | `an app` · `a "free" trial` · `a show` | hard-show staccato | each device chip | the pile-up rhythm | don't animate each with fly-ins |
| C6 | 13.5–17 | `FREE TRIAL OF OWNING THINGS · EXPIRED` | impact stamp | pop-up card | running-gag punchline | card must not cover WIT face |
| C7 | 17–23.5 | `YOU RENT YOUR WHOLE LIFE` + small `one payment at a time` | impact then static | lower band, subtitle-safe, away from WIT face | lands the thesis | text must not cover WIT's face/expression |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|
| base-phone-blank-inhand.jpg | real photo | CC0, saved | BS1 base / phone texture | safe (hands only, blank screen) | assets/visual-references/section-01-hook/base-phone-blank-inhand.jpg |
| base-desk-devices.jpg | real photo | CC BY, saved | BS2/BS3 base | safe (people/brand-free) | assets/visual-references/section-01-hook/base-desk-devices.jpg |
| CSS bank-app statement | self-made UI | build in render | BS1 list of charges + circled mystery row | safe (no private data, fake names) | render CSS |
| CSS device screens | self-made UI | build in render | BS2 laptop/TV/watch/car charge screens | safe | render CSS |
| WIT poses | local PNG | shared library | emotional subject each scene | safe | .agents/_shared/assets/wit/poses/ |

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|
| base-phone-blank-inhand.jpg | BS1 / C1–C3 | real phone + surface | 0–7.5s | center, phone fills ~50% | host CSS bank-app on the blank screen | direct asset |
| base-desk-devices.jpg | BS2–BS3 / C4–C7 | real desk + devices | 7.5–23.5s | full-frame, darkened in BS3 | float CSS screens + chips; WIT on top | direct asset |
| CSS bank-app | BS1 | statement rows + mystery charge | 0–7.5s | inside phone screen | scroll + red circle | self-made |
| CSS device screens | BS2 | laptop/TV/watch/car charge UIs | 7.5–17s | over each real device | flick-on + −\$ chips | self-made |
| WIT poses | all | emotion | per WIT plan | per WIT plan | layered PNG, big+high | direct asset |

## HyperFrames Guidance

- Composition target: `1920x1080`, `Section01Hook` composition, preview on `localhost:1001`
- Big scene count: 3
- Cue state count: 7
- Scene components: real photo base (`cover`), CSS phone + bank-app, CSS device screens, WIT PNG layer, handwritten labels, red markup, payoff band
- Timing notes: estimated; generate `section-01-word-timings.json` (whisper) and re-pin C1–C7 to real word starts before final
- Motion density rule: hard-show labels; impact only for the red circle (C3), EXPIRED stamp (C6), payoff (C7)
- Text style: channel handwritten labels/captions
- Asset paths: `assets/visual-references/section-01-hook/` + shared WIT poses
- Audio sync notes: bank-app on "Quick question"; red circle on "it's higher"; pop-up on "just expired"; payoff on "you rent your whole life"
- WIT pose files: wit-pose-suspicious, wit-pose-shocked, wit-pose-deadpan-side-eye, wit-pose-trapped-by-app-screen
- WIT density: 4 beats (≤2 per scene)
- WIT scale and crop guards: emotional beats ~1/3 frame; payoff ~1/2 frame, high; never crop face/glasses/head/shoulders; only legs/edge
- No-WIT breathing beats: C1, C4
- Suggested inspect timestamps: 1.0, 3.0, 6.0, 9.5, 12.5, 15.5, 20.0
- Suggested screenshot/contact-sheet QA timestamps: 3.0 (phone+suspicious), 6.0 (red circle), 12.5 (staccato items + shocked), 15.5 (EXPIRED + deadpan), 20.0 (trapped payoff)
- Suggested MP4 QA frame timestamps, only if export is explicitly requested: n/a (export not requested)
- Build risks: phone bank-app readability; device screens too busy; payoff text covering WIT face
- Must not invent: scene order, base images, WIT poses/placement, label text, red-mark target, motion types, payoff layout

## Review-Prevention Checklist

- voice sync mapped to phrase cues: yes (cue→phrase pinned; render to refine with word-timings)
- big-scene rhythm avoids unrelated rapid boards: yes (3 scenes for 23.5s)
- cue density stays readable: yes (7 cues, one change each)
- motion density uses hard-show by default: yes
- impact motion reserved for emphasis: yes (circle, stamp, payoff)
- WIT rhythm not overused: yes (4 beats, ≤2/scene)
- WIT size readable: yes (1/3–1/2 frame)
- WIT crop safe: yes (only legs/edge)
- WIT does not cover text/evidence: yes (cleared zones specified)
- red markup targets exact objects: yes (one charge row)
- scene bases visually differentiated: yes (phone vs desk vs darkened desk)
- render does not need to invent timing/layout/assets: timing is estimated but bases/poses/labels/motion are specified; render only re-pins to word-timings

## Approval Checks

- visual reference pass completed: yes (Openverse, viewed)
- what/when/how clear: yes
- big scenes grouped, not one full scene per sentence: yes
- cue states low enough for section duration: yes (7 for 23.5s)
- attention reason per big scene / cue state: yes
- label readable: yes (short)
- WIT has a clear job: yes
- WIT pose files named: yes
- WIT facial emotion large enough: yes
- WIT face/head/shoulder crop safe: yes
- WIT density counted and justified: yes (4)
- no-WIT breathing beats planned: yes (C1, C4)
- red markup points to exact object: yes
- ordinary labels hard-show unless emphasis needs impact motion: yes
- impact animation reserved for emphasized spoken beats: yes
- real-life asset explains, not decorates: yes (real phone + desk)
- title-thumbnail promise still being paid off: yes (you rent everything)
- safe for English learners: yes (short lines, on-screen glosses)
- ready for HyperFrames: yes (pending word-timing re-pin)
