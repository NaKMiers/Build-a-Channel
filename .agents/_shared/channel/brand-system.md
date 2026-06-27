# Brand System

Classification: `Core`

Scope: `CHANNEL_WIDE`

This file consolidates the channel visual identity, WIT rules, and thumbnail visual rules.

## Channel Identity

- Name: `Why It Works`
- Format: English-first no-face explainer channel
- Audience lens: English learners, level A2–C1 (advantage: interesting English — entertainment-first; learners come for the fun and improve English as a side effect)
- Lane: money, internet, society, business, modern life, and current culture
- Tone: smart, simple, funny, dry, and allowed savage/cheeky (edge at the system/own wallet, never slurs; public figures as transformative parody) — see learning-log.md
- Default text style: handwritten labels and captions rendered through HyperFrames

Core promise:

`Explain money, the internet, and modern life in simple, funny English that English learners can enjoy without feeling like they are studying.`

## Visual Feel

Use:

- simple 2D boards
- bold flat colors
- clear silhouettes
- handwritten-looking labels, arrows, captions, and red corrections
- WIT poses as the recurring human reaction
- real or real-looking objects when they make the explanation clearer

Avoid:

- generic corporate explainer style
- over-polished mascot acting
- crowded dashboards
- copied frames from reference channels
- private data, unclear copyrighted assets, pixel-copied private screenshots, or any logo used to imply endorsement / a fake claim

## Real-UI Illustration (standing owner preference, 2026-06-22)

The channel owner explicitly loves and approves using **real recognizable UI to illustrate the
script** — phone / iPhone mockups, real app icons (Gmail, Messenger, Microsoft To Do, Google
Calendar, WhatsApp, Slack, etc.), and app/notification/chat screens — whenever the narration names
or depicts those actual apps, products, or screens. This is a PREFERRED technique, not just an
allowed exception; it overrides the older default "avoid real logos."

Use it editorially (to explain/depict, never to endorse or imply a fake claim), keep private data
out, and build the screens in CSS with real icon PNGs (icons sourced from Wikimedia Commons). Do not
pixel-copy someone's real private screenshot; mock the UI up cleanly with the real icons.

## WIT Direction

Current status: `draft replacement generated - awaiting user review`

Current WIT asset location:

```text
.agents/_shared/assets/wit/poses/
```

Keep only:

- `manifest.json`
- the `24` transparent PNG pose files listed in the manifest

The current WIT direction is the simple white round-headed character from the approved thumbnail direction:

- thick black outline
- oversized black glasses
- expressive eyebrows
- simple white body
- suspicious, betrayed, trapped, panicked, confused, or defeated reactions

Do not use the removed `original-wit-24` design as current WIT. Do not revive older hair, shirt, receipt-tie, `core-24`, or `comedy-core` directions unless the user explicitly asks for historical review.

## WIT Role

WIT is the audience surrogate.

Working rule:

`WIT is funniest when the system is happening to him.`

Production rule:

`When WIT appears, the emotion must read immediately.`

Use WIT for:

- hooks
- thumbnails
- punchlines
- reveal moments
- evidence pointing
- showing how a system feels to a normal person

Do not let WIT:

- block the main label or joke
- become the whole topic
- smile during suspicious or negative beats
- copy another creator's exact character style
- look accidentally broken through cropped face, head, shoulders, or important props

## WIT Modes

Clean WIT:

- neutral, curious, lightly skeptical, or pointing
- good for setup, explanation, and calm evidence beats

Suffering WIT:

- suspicious, betrayed, trapped, panicked, confused, defeated
- good for hooks, punchlines, thumbnails, and retention beats

For comedy-heavy videos, plan a visible Suffering WIT moment every `20-30` seconds when it helps clarity.

For render frames, WIT can be large: `1/3` to `1/2` of the frame is acceptable on emotional beats when it does not cover the label, evidence, or payoff. Prefer exaggerated, goofy, readable expressions over small neutral corner placement.

Use WIT with rhythm. In short sections, WIT should usually appear as `1-2` emotional beats per persistent big scene, not as a reaction on every cue.

## Thumbnail Rules

Thumbnail formula:

```text
one dominant object + one contradiction + one WIT emotion + 1-3 readable words
```

Rules:

- Make the topic understandable in `1` second.
- Use high contrast at mobile size.
- Title and thumbnail should not repeat the same information.
- WIT should show one clear emotion.
- Use one dominant real or real-looking object.
- Keep text to `1-3` words.
- Avoid fake claims, rage bait, and copied creator layouts.

Thumbnail WIT should answer:

`How does this topic feel to a normal person?`
