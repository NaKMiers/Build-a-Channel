# Section 1 Visual Plan (REMADE 2026-06-23)

Video:
`Why Everything Is a Subscription Now`

Section:
`Section 1: Hook: It's More Than You Think`

Status:
`remade after review — built + previewing on localhost:1001`

## Why remade

Owner rejected the first build: photos mundane/boring, WIT poses boring, cream label boxes repetitive
and uncreative. This remake uses vivid on-topic real bases (money + locks), dynamic WIT poses, and
varied UI devices instead of cream boxes.

## Source Inputs

- Voiceover: `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.8.mp3` (23.509s)
- Word timings: `voiceover/section-01-hook/section-01-word-timings.json`

## Narration

```text
Quick question. How many subscriptions are you paying for right now?
Whatever number you guessed... it's higher. It's always higher.
Right now, money is quietly leaving your account every month, for stuff you forgot you own. An app. A "free" trial that stopped being free. A show you watched once.
Your free trial of owning things just expired.
You don't buy things anymore. You rent your whole life. One payment at a time.
```

## Visual Direction

- 3 big scenes, vivid + kinetic; idea demonstrated by varied UI devices, not cream boxes
- Real bases: coins (BS1), cash (BS2), padlocks (BS3) — money → draining → locked
- WIT path: price-tag-suspicion → hidden-fee-panic → holding-phone-panic → trapped-by-app-screen (4 beats)
- Motion: tiles pop in waves; counter jumps; toasts pop; modal smashes; padlocks slam; payoff smashes

## Big Scene Plan

| Big Scene | Local Time | Base | What's on screen |
|---|---:|---|---|
| BS1 app grid | 0.0–7.16 | base-coins | "subscriptions you actually pay for…" headline; colorful app-tile grid fills in; counter jumps "7?" → "12+"; WIT price-tag-suspicion |
| BS2 charges | 7.16–18.54 | base-cash | notification toasts of monthly charges pop on cash (StreamFlix −$9.99, TunePass −$4.99, CloudBox −$2.99, a show −$6.99); FREE-TRIAL countdown flips to "$2.99/mo"; EXPIRED system modal; WIT hidden-fee-panic → holding-phone-panic |
| BS3 padlock wall | 18.54–23.509 | base-padlock | wall of app tiles each slamming a gold padlock; bold kinetic "YOU RENT YOUR WHOLE LIFE" + "one payment at a time"; WIT trapped-by-app-screen |

## Cue Timeline (pinned to word-timings)

| Cue | Time | Voice | What changes | Motion |
|---|---:|---|---|---|
| C1 | 0.40 | "Quick question" | headline + first tiles appear | pop waves |
| C2 | 1.26 | "how many subscriptions" | counter "7?"; WIT suspicion; grid fills | pop |
| C3 | 5.60 | "it's higher" | counter smashes to red "12+" | impact |
| C4 | 7.16/7.66 | "money quietly leaving" | cut to cash; StreamFlix −$9.99 toast | transition + pop |
| C5 | 9.04 | "your account" | TunePass −$4.99 toast | pop |
| C6 | 11.74 | "An app" | CloudBox −$2.99 toast | pop |
| C7 | 12.48→13.90 | "a free trial that stopped being free" | FREE-TRIAL countdown → flips to "$2.99/mo" | pop/swap |
| C8 | 14.48 | "a show you watched once" | −$6.99 toast | pop |
| C9 | 17.90 | "just expired" | EXPIRED system modal; WIT → holding-phone-panic | impact |
| C10 | 18.54 | "you don't buy things anymore" | cut to padlocks; locked-tile wall; WIT trapped | transition + slam |
| C11 | 20.32 | "you rent your whole life" | kinetic payoff banner | impact |
| C12 | 21.40 | "one payment at a time" | subline | hard-show |

## WIT Pose Plan

| Time | Pose | Placement | Why |
|---:|---|---|---|
| 2.10–7.1 | price-tag-suspicion | right, ~1/3 | squinting at the count |
| 7.4–15.9 | hidden-fee-panic | right, ~1/3, bills flying | charges raining |
| 15.9–18.46 | holding-phone-panic | right, ~1/3 | the "expired" gut-punch |
| 18.74–23.5 | trapped-by-app-screen | lower-right, ~1/2 | "you rent your whole life" |

WIT density: 4 beats, ≤2/scene; `money-panic` avoided (baked black bg).

## HyperFrames Guidance

- Composition `Section01Hook`, 1920x1080, 23.509s, port 1001
- All cue reveals pinned to `section-01-word-timings.json`
- Varied devices replace cream boxes: app grid, counter, toasts, countdown, modal, padlock wall, kinetic type
- Modal positioned with explicit left/top (NOT translate centering — GSAP scale would drop it); no emoji glyphs (CSS `!` circle instead of ⚠)
- Payoff is a top banner clear of the trapped WIT
- Checks: lint 0/0, validate 0 errors; snapshot QA at 1.2/5.9/8.6/13.2/18.2/21.2
- Must not invent: bases, scene order, WIT poses, device text, timings, motion

## Review-Prevention Checklist

- voice sync pinned to words: yes
- vivid/on-topic bases (not mundane): yes (coins/cash/padlocks)
- varied idea devices (no repeated cream boxes): yes
- dynamic WIT: yes (4 expressive poses)
- WIT/text collisions cleared: yes (payoff top banner; modal/WIT separated)
- lint/validate: 0 errors
