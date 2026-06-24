# Shorts Plan — Why Buy 1 Get 1 Free Beats 50% Off

Source long video: `output/why-buy-1-get-1-beats-50-off.mp4` (combined, 243.56s)
Source skill: `shorts` (plan mode)
Status: `awaiting owner approval to build`

Owner selection (2026-06-24): **A + B + C** (the recommended Tier-1 trio).

## Locked rules (apply to every short)

- **Native portrait rebuild** — new `1080x1920` composition per short (`data-width="1080" data-height="1920"`). Never a crop/letterbox of the 16:9 master.
- **Complete standalone short — NO CTA.** No "watch the full video" / subscribe / channel card. Each ends on its own payoff beat.
- **Platform-safe zone `x[60..880] · y[220..1490]`** — all readable content (labels, captions, payoff cards, WIT face) inside it. WIT body may bleed off the bottom/side edges; FACE stays inside. Verify with a temporary dashed safe-guide + center line, then remove before handoff.
- **WIT big** (~1/3–1/2 frame), face ABOVE the centered caption; approved pose PNGs only; `transform-origin: center bottom`.
- **Captions = distinct subtitle style** — white text + dark stroke on a translucent dark pill `rgba(16,12,9,0.5)`, `border-radius:22px`, centered vertically (`left:50%; top:50%`), ~60px, 2–4 words, voice-synced. Punchline/payoff carried by the on-screen CARD (the hero text), never duplicated in a caption; captions clear before a card pops so nothing overlaps.
- **Reuse the source section's real photo bases + WIT poses + font** (copy a minimal working set into each short's `assets/`). Every scene = a real photo base (object-fit cover) + top/bottom scrim.
- **Voiceover regenerated per short** via `hyperframes tts`, approved voice `David23 / am_eric / 0.84 / en-us`. Same words, only the subset the short needs. Spell "shh" as "shush" (kokoro reads letter clusters).
- **Captions timed from real whisper-tiny.en word timings** of the short's own audio; re-time the tail monotonically. Never estimate.
- **Ports** `1100 + short number` → S01=`1101`, S02=`1102`, S03=`1103`.

## Short menu (built)

| # | Short | Source section(s) | Target | Port | Assets reused |
|--:|---|---|--:|--:|---|
| 01 | You're The Rabbit | S1 (hook) + 1 compressed S2 math beat | ~26s | 1101 | magic-hat, red-curtain, profit-coins; WIT suspicion/shocked/betrayed; Patrick Hand |
| 02 | The Hostage Shampoo | S4 (the magic word) | ~30s | 1102 | brain, gift, prop-shampoo, cash; WIT confused/awkward-celebration/betrayed; Patrick Hand |
| 03 | 25% Off In A Costume | S7 (payoff) | ~24s | 1103 | cards, mask, cutmoney; WIT thinking/talking-front/shocked; Patrick Hand |

---

## Short 01 — "You're The Rabbit"

- **Cold open (0s):** Hard on `magic-hat` base, label **"Sounds impossible…"**, WIT `price-tag-suspicion` peeking, smug.
- **One idea:** A store can give it free and still out-earn half price — because "free" doubles its profit. (Self-contained; the math beat resolves the hook inside the short, so it is not a teaser.)
- **Payoff (no CTA):** "That's a magic trick — and you are the rabbit." Card: **"YOU'RE THE RABBIT 🐇"** with WIT `betrayed`/blinking; ends on the hold.

**Trimmed/assembled VO (same words):**
> Here's something that sounds impossible. A store can give you a product for free — and still make more than if it sold it at half price. Same product, same shelf — you pay five bucks an item either way. But the "free" sign doubles the store's profit. Half price, the store keeps a dollar. Free, it keeps two. Double. That's not generosity — it's a magic trick. And you are the rabbit.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third label (hero card) | WIT (pose · side · ~size) | Caption beats |
|---|---|---|---|---|
| A | magic-hat | "Sounds impossible…" | price-tag-suspicion · center-low · ~820px | "sounds impossible" / "free… still earns more" |
| B | profit-coins | "Same $5 / item" → "50% off: keeps $1" | (none — card hero) | "same five bucks" / "either way" |
| C | profit-coins (proud) | "FREE: keeps $2 → DOUBLE" (pop) | shocked · center-low · ~860px | "free doubles it" / "Double." |
| D | red-curtain | "YOU'RE THE RABBIT 🐇" (pop, hold) | betrayed · center-low · ~900px | "a magic trick" (clears before card) |

- Caption source: `voiceover/short-01.mp3` → `short-01-word-timings.json` (tail re-timed). Opening caption show-time clamped to ≥0.05.
- Emoji note: 🐇 may not render in snapshot Chromium → if it drops, fall back to the word "RABBIT" only (carry the bunny in the card text, no emoji).

## Short 02 — "The Hostage Shampoo"

- **Cold open (0s):** `brain` base, label **"The magic word: FREE"**, WIT `confused`.
- **One idea:** "Free" is a feeling, not a number — it switches off your math, so BOGO sells you a word with a full-price purchase stapled on.
- **Payoff (no CTA):** "You didn't get a free shampoo. You got a full-price shampoo — with a hostage." Card over `prop-shampoo`: **"FULL-PRICE SHAMPOO + 1 HOSTAGE"**, WIT `betrayed`.

**Trimmed/assembled VO (same words):**
> The magic word is "free." And free makes your brain go a little stupid. When something's free, you stop doing math — you forget the boring question: do I even want a second one? Fifty percent off is a number, and your brain checks numbers. Free is a feeling — your brain just yells "yes" and grabs. So buy one, get one free isn't selling you a discount. It's selling you a word — with a full-price purchase stapled to it. You didn't get a free shampoo. You got a full-price shampoo… with a hostage.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third label (hero card) | WIT (pose · side · ~size) | Caption beats |
|---|---|---|---|---|
| A | brain | "The magic word: FREE" | confused · center-low · ~840px | "the magic word" / "free" |
| B | gift | "FREE = a feeling" vs "50% off = a number" | (none — card hero) | "stop doing math" / "number vs feeling" |
| C | cash | "yells YES and grabs" (pop) | awkward-celebration · center-low · ~880px | "just yells yes" / "and grabs" |
| D | prop-shampoo | "FULL-PRICE SHAMPOO + 1 HOSTAGE" (pop, hold) | betrayed · center-low · ~900px | "with a hostage" (clears before card) |

- Caption source: `voiceover/short-02.mp3` → `short-02-word-timings.json` (tail re-timed).

## Short 03 — "25% Off In A Costume"

- **Cold open (0s):** `chess` base, label **"Free vs Half off"**, WIT `thinking`.
- **One idea:** The two signs play different games — 50% off cuts the price, "free" cuts your judgment.
- **Payoff (no CTA):** "'Buy one get one 50% off' isn't free anything — it's 25% off, in a costume." Card over `mask`: **"= 25% OFF (in a costume)"**, WIT `shocked`.

**Trimmed/assembled VO (same words):**
> So why does buy one, get one free beat fifty percent off? Because the two signs are playing different games. Fifty percent off cuts the price. Buy one, get one free cuts your judgment. One asks your brain a question. The other hands it a gift and says: shush, relax. And one last thing — next time you see "buy one, get one fifty percent off"? That's not free anything. That's twenty-five percent off… in a costume.

**Scene-by-scene portrait layout:**

| Scene | Base | Upper-third label (hero card) | WIT (pose · side · ~size) | Caption beats |
|---|---|---|---|---|
| A | chess | "Free vs Half off" | thinking · center-low · ~840px | "different games" |
| B | cutmoney | "50% off → cuts the PRICE" | (none — card hero) | "cuts the price" |
| C | cutmoney | "FREE → cuts your JUDGMENT" (pop) | talking-front · center-low · ~860px | "cuts your judgment" / "shush, relax" |
| D | mask | "BOGO 50% off = 25% OFF (in a costume)" (pop, hold) | shocked · center-low · ~900px | "in a costume" (clears before card) |

- Caption source: `voiceover/short-03.mp3` → `short-03-word-timings.json` (tail re-timed).
- TTS: write "shush, relax" (not "shh") so kokoro speaks the word.

---

## Build order & review

Build **one short at a time** (S01 → S02 → S03), review each on its port before the next, per the section discipline. Export only after approval → `output/shorts/short-0N-<kebab>.mp4`, ffprobe-verified `1080x1920 / h264 / aac`.

## Deliverables (filled on export)

| Short | MP4 | Duration | Size | ffprobe |
|---|---|--:|--:|---|
| 01 You're The Rabbit | `output/shorts/short-01-youre-the-rabbit.mp4` | — | — | — |
| 02 The Hostage Shampoo | `output/shorts/short-02-the-hostage-shampoo.mp4` | — | — | — |
| 03 25% Off In A Costume | `output/shorts/short-03-25-off-in-a-costume.mp4` | — | — | — |
