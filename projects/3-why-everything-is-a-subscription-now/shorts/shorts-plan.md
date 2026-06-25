# Shorts Plan — Why Everything Is a Subscription Now

Source long video: `output/3-why-everything-is-a-subscription-now.mp4` (combined, 328.06s)
Source skill: `shorts` (plan mode)
Status: `all 4 EXPORTED to output/shorts/ · ffprobe-verified 1080x1920 / h264 / 30fps / aac`

Owner selection (2026-06-24): **build all 4 — ① + ② + ③ + ④** (Tier-1 trio + the payoff insight).

## Locked rules (apply to every short)

- **Native portrait rebuild** — new `1080x1920` composition per short (`data-width="1080" data-height="1920"`). Never a crop/letterbox of the 16:9 master.
- **Complete standalone short — NO CTA.** No "watch the full video" / subscribe / channel card. Each ends on its own payoff beat.
- **Platform-safe zone `x[60..880] · y[220..1490]`** — all readable content (labels, captions, payoff cards, WIT face) inside it. WIT body may bleed off the bottom/side edges; FACE stays inside. Verify with a temporary dashed safe-guide + center line, then remove before handoff.
- **WIT big** (~1/3–1/2 frame), face ABOVE the centered caption; approved pose PNGs only; `transform-origin: center bottom`. **Per-pose face height varies** — `thinking`, `shocked`, `tiny-defeated`, `confused` tend to sit lower in their PNG canvas; raise those with a per-id `bottom` override and snapshot a caption-over-WIT beat for EACH pose used (see skill memory).
- **Captions = distinct subtitle style** — white text + dark stroke on a translucent dark pill `rgba(16,12,9,0.5)`, `border-radius:22px`, centered vertically (`left:50%; top:50%`), ~60px, 2–4 words, voice-synced. Punchline/payoff carried by the on-screen CARD (the hero text), never duplicated in a caption; captions clear before a card pops so nothing overlaps. First caption show-time clamped to ≥0.05.
- **Reuse the source section's real photo bases + WIT poses + font** (copy a minimal working set into each short's `assets/`). Every scene = a real photo base (object-fit cover) + top/bottom scrim.
- **Voiceover regenerated per short** via `hyperframes tts`, approved voice `David23 / am_eric / 0.84 / en-us`. Same words, only the subset the short needs. Strip `**` joke markers and `[...]` delivery cues before TTS. Spell out anything kokoro mis-reads (numbers as words, "shh"→"shush").
- **Captions timed from real whisper-tiny.en word timings** of the short's own audio; re-time/clamp the tail monotonically to the real audio duration. Never estimate.
- **Ports** `1100 + short number` → S01=`1101`, S02=`1102`, S03=`1103`, S04=`1104`.

## Short menu (selected)

| # | Short | Source section | Target | Port | Bases reused | WIT poses |
|--:|---|---|--:|--:|---|---|
| 01 | The Free Trial Is A Countdown | S5 | ~30s | 1101 | gift, hourglass, busydesk, piggy | deadpan-side-eye, hidden-fee-panic, thinking, holding-receipt-evidence |
| 02 | Cancelling Is A Vision Quest | S6 | ~28s | 1102 | stopwatch, maze, maze-2, contract | running-away, confused, tiny-defeated, suspicious |
| 03 | Your Free Trial Of A Warm Bottom | S3 | ~24s | 1103 | tv-room, car | shocked, deadpan-side-eye |
| 04 | The Product Is You, Not Cancelling | S7 | ~26s | 1104 | phone, phone-2, cash2, coins | thinking, shocked, holding-receipt-evidence, deadpan-side-eye |

All bases/poses confirmed present under each `section-previews/section-0X-*/assets/`. Patrick Hand font reused.

---

## Short 01 — "The Free Trial Is A Countdown"

- **Cold open (0s):** `gift` base, bright **"FREE TRIAL"** splash, WIT `deadpan-side-eye` (unconvinced).
- **One idea:** "Free" is a hidden countdown — when it hits zero, free quietly becomes a payment you forget about.
- **Payoff (no CTA):** a $3 ghost charge on your statement → card **"FREE TRIAL OF FINANCIAL AWARENESS — EXPIRED"**, WIT `holding-receipt-evidence`.

**Trimmed/assembled VO (same words):**
> Here's the genius part. To get you in, they make it feel free. Start your free trial! No charge today — just pop in your card. Strangers love holding your card. And the trial is real. For seven days. After that, a tiny countdown you can't see hits zero, and "free" quietly becomes a payment. Most people don't cancel. They forget — because forgetting is the design. So the little payment just continues. Forever. A ghost, living in your bank account. Open your bank statement and you'll probably find one. A mystery charge. Three dollars. Every month. For a thing you opened once. Your free trial of financial awareness has expired.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third hero card | WIT | Caption beats |
|---|---|---|---|---|
| A | gift | "FREE TRIAL" splash | deadpan-side-eye | "they make it feel free" / "pop in your card" |
| B | hourglass | "FREE — 7 days" → flips to "$2.99 / mo" (pop) | (none — card hero) | "a tiny countdown" / "becomes a payment" |
| C | busydesk | "forgetting is the DESIGN" | hidden-fee-panic | "they forget" / "a ghost on your statement" |
| D | piggy | bank row "?? UNKNOWN −$3.00 / every month" ring → payoff "FINANCIAL AWARENESS — EXPIRED" (pop, hold) | holding-receipt-evidence | "a mystery charge" (clears before payoff) |

## Short 02 — "Cancelling Is A Vision Quest"

- **Cold open (0s):** `stopwatch` base, **"SIGN UP: 10 sec"** vs **"CANCEL: ???"**, WIT `running-away`.
- **One idea:** Easy in, no way out — leaving is made deliberately harder than joining (negative option billing).
- **Payoff (no CTA):** the menu maze + the phone-number gag → card **"NEGATIVE OPTION BILLING = you keep paying unless you say STOP"**, WIT `tiny-defeated`.

**Trimmed/assembled VO (same words):**
> Okay, you say. I'll just cancel. Oh, sweet child. Here's the strange law of subscriptions. Signing up takes ten seconds. Cancelling takes a vision quest. Getting in is a big, happy, glowing button. Getting out is hidden in your phone like a final boss. You tap account. Then settings. Then manage. Then "are you sure?" Then "here, have a discount." Then "we'll miss you." Then a phone number that only answers between two and two-fifteen on a Tuesday. This even has a name. Negative option billing. A fancy term for one simple trick. You keep paying unless you actively say stop.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third hero card | WIT | Caption beats |
|---|---|---|---|---|
| A | stopwatch | "SIGN UP: 10 sec" / "CANCEL: a vision quest" | running-away | "i'll just cancel" / "oh, sweet child" |
| B | maze | "FINAL BOSS" + breadcrumb account→settings→manage→are you sure?→discount→we'll miss you | confused (wandering) | "hidden like a final boss" |
| C | maze-2 | "☎ answers 2:00–2:15, Tuesdays only" (pop) | tiny-defeated | "only on a Tuesday" |
| D | contract | "NEGATIVE OPTION BILLING" stamp → "you keep paying unless you say STOP" (pop, hold) | suspicious | "you keep paying" (clears before stamp) |

## Short 03 — "Your Free Trial Of A Warm Bottom"

- **Cold open (0s):** `tv-room` base, streaming wall of generic rows, WIT `shocked`.
- **One idea:** The rent model spread past screens into hardware you already own.
- **Payoff (no CTA):** heated seats behind a padlock → card **"FREE TRIAL OF A WARM BOTTOM — EXPIRED"**, WIT `deadpan-side-eye`.

**Trimmed/assembled VO (same words):**
> The rent model didn't stop at apps. Music, movies, shows — you don't own a single one. You rent a giant library, and the second you stop paying, the whole thing vanishes. Poof. POV: you own nothing. And it didn't stop at screens. Some carmakers have tried putting heated seats — seats already sitting in the car you bought — behind a monthly fee. Your free trial of a warm bottom has expired.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third hero card | WIT | Caption beats |
|---|---|---|---|---|
| A | tv-room | streaming rows that vanish → "POV: you own nothing" (pop) | shocked | "you don't own one" / "it all vanishes" |
| B | car | "heated seats — already in your car — behind a monthly fee" + padlock on seat button | deadpan-side-eye | "behind a monthly fee" |
| C | car | payoff "FREE TRIAL OF A WARM BOTTOM — EXPIRED" (pop, hold) | deadpan-side-eye | (card carries the payoff; no caption) |

## Short 04 — "The Product Is You, Not Cancelling"

- **Cold open (0s):** `phone` base, **"the most valuable thing they sell?"**, WIT `thinking`.
- **One idea:** The product was never the app or the show — it's your forgetting; the month you meant to cancel and didn't.
- **Payoff (no CTA):** card **"CANCEL THE GHOSTS"** over a bank statement (keep the green rows, strike the ghosts), WIT `deadpan-side-eye`.

**Trimmed/assembled VO (same words):**
> So why is everything a subscription now? Because companies found something quietly genius. The most valuable thing they can sell isn't the app, or the show, or the heated seat. It's your forgetting. The month you meant to cancel, and didn't. The product was never the thing. The product is you — staying. So every so often, open your bank statement. Read the little charges out loud. Keep the ones you love. Cancel the ghosts.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third hero card | WIT | Caption beats |
|---|---|---|---|---|
| A | phone | "the most valuable thing they sell?" → "YOUR FORGETTING" (pop) | thinking | "not the app or the show" |
| B | phone-2 | barcode tag "PRODUCT: YOU" + "the product is you — staying" | shocked | "the product is you" / "staying" |
| C | cash2 | bank statement rows (keep-green vs ghost) | holding-receipt-evidence | "read them out loud" |
| D | coins | payoff "CANCEL THE GHOSTS" (pop, hold; ghost rows struck) | deadpan-side-eye | "keep the ones you love" (clears before payoff) |

---

## Build order & review

Build **one short at a time** (S01 → S02 → S03 → S04), review each on its port before the next, per the section discipline. Export only after approval → `output/shorts/short-0N-<kebab>.mp4`, ffprobe-verified `1080x1920 / h264 / aac`.

## Deliverables (filled on export)

| Short | MP4 | Duration | Size | ffprobe |
|---|---|--:|--:|---|
| 01 The Free Trial Is A Countdown | `output/shorts/short-01-the-free-trial-is-a-countdown.mp4` | 32.62s | 6.4 MB | 1080x1920 · h264 · 30/1 · aac ✓ |
| 02 Cancelling Is A Vision Quest | `output/shorts/short-02-cancelling-is-a-vision-quest.mp4` | 28.72s | 6.2 MB | 1080x1920 · h264 · 30/1 · aac ✓ |
| 03 Your Free Trial Of A Warm Bottom | `output/shorts/short-03-your-free-trial-of-a-warm-bottom.mp4` | 21.09s | 3.6 MB | 1080x1920 · h264 · 30/1 · aac ✓ |
| 04 The Product Is You, Not Cancelling | `output/shorts/short-04-the-product-is-you.mp4` | 21.22s | 4.7 MB | 1080x1920 · h264 · 30/1 · aac ✓ |
