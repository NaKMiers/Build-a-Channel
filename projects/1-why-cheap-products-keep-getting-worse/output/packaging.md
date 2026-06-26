# Packaging — `Why Cheap Products Keep Getting Worse`

Source skill: `packaging`
Generated from: `00-topic-intake.md`, `01-research-pack.md` (reuses approved decisions in `03-packaging.md`)
Shorts included: `yes — 3 shorts`

Thumbnails live in `output/thumbnails/`. Each main title ships with its paired thumbnail (locked A/B pairs).

## Main Video

### A/B Pairs (title ships with its paired thumbnail)


| Pair | Title                                 | Thumbnail                           | Label    | Hypothesis                          | Decision                |
| ---- | ------------------------------------- | ----------------------------------- | -------- | ----------------------------------- | ----------------------- |
| 1    | Why Cheap Products Don't Stay Cheap   | `output/thumbnails/main-pair-1.png` | FUTURE?  | Hidden later cost on the hero chair | **Winner (92)**         |
| 2    | Why Cheap Products Keep Getting Worse | `output/thumbnails/main-pair-2.png` | 2 WEEKS? | Before/after degradation comparison | A/B #2 (86)             |
| 3    | The Hidden Cost Of Cheap Products     | `output/thumbnails/main-pair-3.png` | LATER?   | Receipt-trap / pay-later            | A/B #5 — ⚠️ remake (76) |
| 4    | Why Cheap Products Have Less Future   | `output/thumbnails/main-pair-4.png` | MISSING? | Minimal metaphor box                | A/B #4 (80)             |
| 5    | Why Good Deals Keep Breaking          | `output/thumbnails/main-pair-5.png` | CHEAP?   | WIT emotional reaction (charger)    | A/B #3 (84)             |


Recommended A/B order: `1 -> 2 -> 5 -> 4 -> 3 (remake D first)`

Pairing notes:

- Pair 2 is the comparison thumbnail; its `2 WEEKS?` label is a slight exact-timing risk — relabel to `LATER?` if you regenerate it.
- Pair 3's image was generated with unwanted variant/channel text — remake from `PROMPTS.md` before using it live.
- Locked-pair rule: if you change a thumbnail, change its paired title (and vice-versa).

### Description

```text
Cheap products do not always save money.
Sometimes the missing part is the future.

This video explains why some normal products feel cheaper, weaker, harder to fix, or not worth repairing anymore. The point is not that cheap things are always bad. The point is that the price you see today can hide the cost you meet later: replacement, repair, time, and frustration.

We look at why the price tag speaks first, why boring parts like stronger material and spare parts matter, why extra features can create more tiny failure points, and why repair can feel harder than buying again.

The better question is not only: "How much does this cost?"
It is: "How much future is included?"

Sources and useful reading:
- Vox: Your stuff is actually worse now
- European Parliament: Right to repair
- European Commission: Smartphones and tablets durability and repairability rules
- iFixit: Right to repair
- Repair.org: Right to repair
- Ellen MacArthur Foundation: A New Textiles Economy
- NYT Wirecutter: The Real Reasons Your Appliances Die Young

Subscribe for simple, funny English explainers about money, the internet, business, society, and modern life.
```

### Chapters

```text
00:00 Future not included
00:32 Cheap is not the villain
01:03 The price tag speaks first
01:49 The boring parts disappear
02:39 More features, more tiny deaths
03:23 Repair gets a security system
04:19 Replacement becomes normal
04:57 How much future is included?
```

### Tags / Keywords

`cheap products`, `product quality`, `why products are worse`, `hidden cost`, `repairability`, `right to repair`, `consumer behavior`, `modern life`, `planned obsolescence explained`, `cheap vs durable`, `replacement cost`, `product design`, `disposable products`, `simple English explainer`, `Why It Works`

### Hashtags

`#WhyItWorks #ConsumerBehavior #RightToRepair`

### Pinned Comment

```text
What cheap product did you have to replace too soon?

Mine is emotionally still a phone charger.
```

## Shorts

Each short is a complete standalone short — no "watch the full video" CTA. Captions are burned in, so no SRT upload is needed. Covers are prompt-only this session (see `output/thumbnails/PROMPTS.md`); S01 also has a ready frame at `shorts/short-01-the-9-dollar-chair/snapshots/frame-00-at-25.5s.png`.

### Short 01 — The $9 chair (source: Section 1 + Section 8 button)

- Thumbnail: `output/thumbnails/short-01.png` (prompt-only / or the S01 snapshot frame)
- Title: `Why a $9 Chair Isn't Actually Cheap`

Description:

```text
A $9 chair looks like a bargain… until the future falls off it.
Here's the hidden cost the price tag never shows you. 🪑

#WhyItWorks #CheapProducts #Shopping
```

### Short 02 — You own me, but not enough to open me (source: Section 6)

- Thumbnail: `output/thumbnails/short-02.png` (prompt-only)
- Title: `Why You Can't Fix Your Own Stuff`

Description:

```text
Sometimes fixing a thing costs more than replacing it — so you don't.
That's "repairability," and it quietly decides what survives. 🔒

#WhyItWorks #RightToRepair #Repairability
```

### Short 03 — A subscription with extra steps (source: Section 7)

- Thumbnail: `output/thumbnails/short-03.png` (prompt-only)
- Title: `Why Cheap Stuff Is Basically a Subscription`

Description:

```text
You didn't subscribe to anything — but you keep paying for the same thing again.
When replacing is easier than repairing, cheap quietly becomes a subscription. 🧾

#WhyItWorks #ConsumerBehavior #ModernLife
```

## Thumbnail Prompts

Ready-to-paste prompts for regenerating any thumbnail. Each block is self-contained. Images are already generated and reused as-is — regenerate only to refresh one.

How to use (ChatGPT / DALL·E):

- Attach the WIT reference pose `.agents/_shared/assets/wit/poses/wit-pose-neutral-front.png` and open with: "use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression."
- For the comparison pair (Pair 2), also attach `output/thumbnails/main-pair-2.png` as a layout reference.
- Ask for 16:9, 1280x720. Reject any output with hair / shirt-tie / shoes (off-model WIT).

### Pair 1 — `Why Cheap Products Don't Stay Cheap` · `main-pair-1.png`

```text
Create a YouTube thumbnail, 1280x720, for a no-face explainer channel called Why It Works. A generic bright cheap chair dominates the left side with a big red/yellow sale price tag reading "$9". One leg is wobbling, one screw is falling out, and a small red hidden tag says "not included". Large handwritten label near the chair: "FUTURE?". On the right, use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — suspicious and betrayed, reacting to the chair. Simple high-contrast flat background, dry funny tone, mobile-readable. Do NOT include: real brand logos, store names, photoreal human faces, long text, tiny label text, cluttered background, extra title text, channel logo, hair/shirt/tie/shoes on WIT.
```

### Pair 2 — `Why Cheap Products Keep Getting Worse` · `main-pair-2.png` (comparison)

```text
Create a YouTube thumbnail, 1280x720, for a no-face explainer channel called Why It Works. Before/after split down the center. Left side, cool blue, a small black corner tag "TODAY": one generic chair, shiny and normal. Right side, warm orange/red, a small black corner tag "LATER": the same chair broken, wobbling, faded, missing screws. Use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — standing small in the middle, shocked. Large handwritten center label: "2 WEEKS?" with a rough red underline. High contrast, simple background, mobile-readable. Do NOT include: real brand logos, photorealism, tiny dates, exact durability claims, long explanation text, neutral WIT, hair/shirt/tie/shoes on WIT.
```

### Pair 3 — `The Hidden Cost Of Cheap Products` · `main-pair-3.png`  ⚠️ remake before final

```text
Create a YouTube thumbnail, 1280x720, for a no-face explainer channel called Why It Works. A fake checkout/product card reading "$9 TODAY". Behind it, a long receipt snakes out with faint hidden lines: "replace", "repair", "time". The receipt curls around the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — who looks trapped and nervous. Large handwritten label: "LATER?". Simple flat interface, high contrast, mobile-readable, dry funny tone. Do NOT include: any variant label text, channel logo, "Why It Works" text inside the image, real e-commerce UI, real payment logos, detailed receipt totals, tiny unreadable text, hair/shirt/tie/shoes on WIT.
```

Note: current `main-pair-3.png` was generated with unwanted variant/channel text — remake from this prompt before using it live.

### Pair 4 — `Why Cheap Products Have Less Future` · `main-pair-4.png`

```text
Create a YouTube thumbnail, 1280x720, for a no-face explainer channel called Why It Works. One simple generic product box in the center labeled "$9" with a small broken chair leg sticking out and a single loose screw on the floor. Use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — standing lower-right, deadpan and suspicious. Large handwritten label: "MISSING?". Very simple mobile-first composition, only 3-4 visual elements, strong contrast, clean flat background. Do NOT include: real brand logos, delivery logos, extra labels, tiny text, complex background, generic warning signs, neutral or smiling WIT, hair/shirt/tie/shoes on WIT.
```

### Pair 5 — `Why Good Deals Keep Breaking` · `main-pair-5.png`

```text
Create a YouTube thumbnail, 1280x720, for a no-face explainer channel called Why It Works. Use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — large on the right, looking betrayed and holding a cracked phone charger cable. On the left, a cheerful price tag reads "$5" with tiny falling pieces labeled "repair" and "support" as background detail. Large handwritten label: "CHEAP?". High contrast, simple flat background with sale-yellow and repair-blue accents, mobile-readable, dry funny tone. Do NOT include: real phone brand logos, complex wires, extra text, tiny technical labels, dark unreadable background, angry rage-bait face, hair/shirt/tie/shoes on WIT.
```

### Shorts — portrait covers (1080x1920, prompt-only this session)

Reuse each short's source-section real photos + WIT pose. S01 also has a ready cover frame at `shorts/short-01-the-9-dollar-chair/snapshots/frame-00-at-25.5s.png`.

**Short 01 (`short-01.png`)**

```text
Vertical 1080x1920 cover for a YouTube Short. Real cheap-chair-on-wood-floor photo base with a top/bottom dark scrim. A cream handwritten tag reads "HOW MUCH FUTURE?". Use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — big and centered, arms crossed, deadpan-suspicious. A small kraft "$9" price tag hangs at the side. High contrast, mobile-readable, keep all text and WIT face inside the central safe zone. Do NOT include: real brand logos, long text, hair/shirt/tie/shoes on WIT.
```

**Short 02 (`short-02.png`)**

```text
Vertical 1080x1920 cover for a YouTube Short. Real opened-phone/repair-bench photo base with a dark scrim. A padlock sits over the device. A cream handwritten tag reads "YOU OWN ME?". Use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — big and centered, trapped/betrayed. High contrast, mobile-readable, all text and WIT face inside the central safe zone. Do NOT include: real brand logos, long text, hair/shirt/tie/shoes on WIT.
```

**Short 03 (`short-03.png`)**

```text
Vertical 1080x1920 cover for a YouTube Short. Real checkout/receipt photo base with a dark scrim, a long receipt printing. A cream handwritten tag reads "A SUBSCRIPTION?". Use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression — big and centered, tired/deadpan. High contrast, mobile-readable, all text and WIT face inside the central safe zone. Do NOT include: real brand logos, long text, hair/shirt/tie/shoes on WIT.
```

