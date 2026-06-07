# 03 Packaging

Video: `Why Cheap Products Keep Getting Worse`

Status: `draft packaging - rerun overwrite`

Source skill: `packaging`

Source files:

- `00-topic-intake.md`
- `01-research-pack.md`
- `02-script.md`

## Packaging Brief

- Core promise: Explain why some cheap products look like a bargain now but become expensive later through replacement, repair problems, short life, time, and frustration.
- Main contradiction: The visible price is low, but the invisible future of the product may have been removed.
- Audience question: Why do so many normal products feel fine at first, then break, wear out, or become not worth fixing too soon?
- Recurring motif: `future not included`
- WIT emotion: excited bargain hunter -> suspicious owner -> betrayed buyer -> locked-out repairer -> tired repeat buyer.
- First 10 seconds promise: WIT buys a cheap chair, a hidden `FUTURE NOT INCLUDED` label appears, and the chair starts wobbling before the narrator reveals it was not really cheap.
- Risk to avoid: Do not imply all cheap products are bad, every company intentionally makes products fail, old products were always better, or repair is always the right choice.

## Title Options

| # | Title | Promise | Curiosity | Risk | Score |
|---:|---|---|---|---|---:|
| 1 | Why Cheap Products Don't Stay Cheap | Shows the hidden later cost behind low prices. | Why does a cheap thing become expensive after purchase? | Slightly less direct than the project title. | 9.5 |
| 2 | Why Cheap Products Keep Getting Worse | Names the familiar viewer pain directly. | Why do normal products feel worse now? | Broad claim; keep `some` and `not always` in description and script. | 9.2 |
| 3 | The Hidden Cost Of Cheap Products | Promises a system-level explanation. | What cost is hidden from the price tag? | More generic title shape. | 8.9 |
| 4 | Why Cheap Products Have Less Future | Uses the video's central metaphor. | How can a product have less future? | Unusual phrasing may need thumbnail support. | 8.7 |
| 5 | Why Low Prices Can Get Expensive | Clear today-versus-tomorrow contrast. | Where does the later expense come from? | Less concrete to physical products. | 8.6 |
| 6 | Why Cheap Stuff Feels Temporary | Simple everyday English. | Why do cheap things feel short-lived? | `Stuff` is broad and casual. | 8.4 |
| 7 | The Strange Logic Behind Cheap Products | Signals hidden incentives. | What logic makes cheaper products feel disposable? | Softer emotional hook. | 8.4 |
| 8 | Why Good Deals Keep Breaking | Makes bargains suspicious. | Why does the good deal betray you? | Can overstate the failure claim. | 8.2 |
| 9 | Why Cheap Things Break So Fast | Very clear durability promise. | Why does failure arrive early? | Too absolute unless qualified. | 8.1 |
| 10 | Why Products Are Cheap Now And Expensive Later | Direct hidden-cost contrast. | What happens later? | Long and plain. | 8.0 |
| 11 | Why Cheap Products Come With Missing Tomorrow | Strongly on-motif. | What does `missing tomorrow` mean? | Awkward but memorable. | 7.9 |
| 12 | Why Your Cheap Chair Wasn't Really Cheap | Pays off the hook object. | What made the chair secretly expensive? | Too narrow for the full video. | 7.9 |
| 13 | Why Products Feel Disposable Now | Captures modern-life feeling. | Why do things feel temporary? | Does not clearly name cheap prices. | 7.8 |
| 14 | Why The Cheapest Thing Costs Twice | Strong replacement-cost idea. | Why would it cost twice? | Can sound like a fake exact claim. | 7.5 |
| 15 | Why The Price Tag Lies Later | Funny title-personification. | How can a price tag lie? | `Lies` may sound too accusatory. | 7.4 |

## Thumbnail Concepts

| # | Concept | Dominant object | Label | WIT emotion | Visual contradiction | Prompt / Production notes |
|---:|---|---|---|---|---|---|
| 1 | Cheap chair, missing future | Cheap chair with a sale tag | `FUTURE?` | suspicious-betrayed | The chair looks normal, but a screw falls out and a hidden `not included` tag appears. | Best match for the script hook and title. Use bright sale colors, one object, WIT large on the right. |
| 2 | Broken cheap charger | Cheap charger and huge price tag | `CHEAP?` | betrayed | The low price looks friendly while repair and support pieces fall away. | Strong WIT emotion and mobile read, but narrower than the full script. |
| 3 | Two weeks later | Before/after chair | `2 WEEKS?` | shocked | One side is new and clean; the other is broken after a short time. | Very clear, but risks overclaiming speed unless framed as metaphor. |
| 4 | Later charges receipt | Fake checkout screen and long receipt | `LATER?` | trapped | `$9 today` hides replacement, repair, and time costs later. | Strong hidden-cost angle. Generated render needs cleanup because it added unwanted variant and brand text. |
| 5 | Missing future box | Cheap product box with broken part | `MISSING?` | suspicious-deadpan | The product box is cheap, but a key part is missing or broken. | Clean mobile read, but the label is less specific than `FUTURE?`. |

## Thumbnail A/B Test

| Variant | Style | Image / Path | Prompt ref | Label | WIT emotion | Score | Strength | Risk | Decision |
|---|---|---|---|---|---|---:|---|---|---|
| A | Real Object Close-Up | `assets/thumbnails/variant-a-generated.png` | Variant A | `FUTURE?` | suspicious-betrayed | 92 | Best match to hook; strong object, emotion, and visual question. | Generated price changed to `$19.99`; use layout but revise price if finalizing. | Winner |
| B | WIT Reaction | `assets/thumbnails/variant-b-generated.png` | Variant B | `CHEAP?` | betrayed | 84 | WIT emotion reads fast and charger is relatable. | Too charger-specific; happy price tag may distract from product-quality idea. | A/B backup |
| C | Before / After Lie | `assets/thumbnails/variant-c-generated.png` | Variant C | `2 WEEKS?` | shocked | 86 | Extremely clear before/after contrast. | `2 weeks` can feel like an unsupported exact claim. | Strong alternate if title stays broad |
| D | Trap Interface | `assets/thumbnails/variant-d-generated.png` | Variant D | `LATER?` | trapped | 76 | Hidden receipt logic is useful for the video promise. | Generated render added unwanted `Variant D` and channel text; too cluttered for final. | Concept only, needs clean remake |
| E | Minimal Bold Label | `assets/thumbnails/variant-e-generated.png` | Variant E | `MISSING?` | suspicious-deadpan | 80 | Very readable and simple at mobile size. | Label is vague; box does not show enough of the cheap-product system. | Backup simplification |

## Thumbnail Generation Prompts

### Variant A: `Real Object Close-Up`

Prompt:

```text
Create a YouTube thumbnail draft, 1280x720, for a no-face explainer channel called Why It Works. Variant A: Real Object Close-Up. A generic bright cheap chair dominates the left side with a big red/yellow sale price tag. One leg is wobbling, one screw is falling out, and a small red hidden tag says "not included". Large handwritten label near the chair: "FUTURE?". On the right, WIT is a simple white stick-figure character with black glasses, suspicious and betrayed, reacting to the chair. Simple high-contrast flat background, dry funny tone, no brand logos, mobile-readable composition.
```

Negative prompt / avoid:

```text
No real brand logos, no store names, no product brand marks, no photoreal human faces, no long text, no tiny label text, no cluttered background, no extra title text, no channel logo, no copied creator composition.
```

Use notes:

- Use as the main direction.
- If remaking, set the sale price to `$9` to match the script hook.
- Keep WIT large and readable on the right.

### Variant B: `WIT Reaction`

Prompt:

```text
Create a YouTube thumbnail draft, 1280x720, for a no-face explainer channel called Why It Works. Variant B: WIT Reaction. WIT is a simple white stick-figure character with black glasses, large on the right, looking betrayed and holding a cracked phone charger cable. On the left, a cheerful price tag says "$5" and hides small falling pieces labeled "repair" and "support" as tiny background details. Large handwritten label: "CHEAP?". High contrast, simple flat background with sale yellow and repair blue accents, no brand logos, mobile-readable, dry funny tone.
```

Negative prompt / avoid:

```text
No real phone brand logos, no Apple-style connectors as the main claim, no complex wires, no extra text, no tiny technical labels, no dark unreadable background, no angry rage-bait face.
```

Use notes:

- Use if the hook object changes from chair to charger.
- Keep repair/support pieces as visual texture, not the main read.

### Variant C: `Before / After Lie`

Prompt:

```text
Create a YouTube thumbnail draft, 1280x720, for a no-face explainer channel called Why It Works. Variant C: Before / After Lie. One generic product, a simple chair or household stool, split down the center. Left side is shiny and normal with a tag "TODAY". Right side is broken, wobbling, faded, and missing screws with a tag "LATER". WIT, a simple white stick-figure with black glasses, stands small in the middle looking shocked. Large handwritten label: "2 WEEKS?". Clear before/after contrast, high contrast, simple background, no brand logos, no clutter, mobile-readable.
```

Negative prompt / avoid:

```text
No real furniture brands, no detailed room background, no tiny dates, no exact durability claim beyond the thumbnail joke, no long explanation text, no neutral WIT.
```

Use notes:

- Strongest clarity alternate.
- Replace `2 WEEKS?` with `LATER?` if we want a safer, less exact promise.

### Variant D: `Trap Interface`

Prompt:

```text
Create a YouTube thumbnail draft, 1280x720, for a no-face explainer channel called Why It Works. Variant D: Trap Interface. A fake checkout/product listing screen becomes a trap. Big simple product card: "$9 TODAY". Behind it, a long receipt snakes out with hidden lines: "replace", "repair", "time" as small details. The receipt curls around WIT, a simple white stick-figure with black glasses, who looks trapped and nervous. Large handwritten label: "LATER?". Simple flat interface, no real logos, high contrast, mobile-readable, funny dry tone.
```

Negative prompt / avoid:

```text
No variant label text, no channel logo, no "Why It Works" text inside the thumbnail, no real e-commerce UI, no real payment logos, no detailed receipt totals, no tiny unreadable text, no cluttered checkout page.
```

Use notes:

- Good concept, but the generated version failed by adding `Variant D` and channel text.
- Remake from the SVG layout if this direction is selected.

### Variant E: `Minimal Bold Label`

Prompt:

```text
Create a YouTube thumbnail draft, 1280x720, for a no-face explainer channel called Why It Works. Variant E: Minimal Bold Label. One simple generic product box in the center labeled "$9" with a small broken chair leg sticking out and a single loose screw on the floor. WIT, a simple white stick-figure with black glasses, stands in the lower right with a deadpan suspicious face. Large handwritten label: "MISSING?". Very simple mobile-first composition, only 3-4 visual elements, strong contrast, clean flat background, no brand logos, no channel logo, no variant label text.
```

Negative prompt / avoid:

```text
No real brand logos, no delivery company logos, no extra labels, no tiny text, no complex background, no generic warning signs, no neutral or smiling WIT.
```

Use notes:

- Most mobile-safe backup.
- If selected, change label to `FUTURE?` or add a small `not included` tag so the click question is more specific.

## Title-Thumbnail Packages

| Rank | Title | Thumbnail concept | Why it works | Score | Decision |
|---:|---|---|---|---:|---|
| 1 | Why Cheap Products Don't Stay Cheap | Variant A: Cheap chair, missing future | The title names the hidden later cost while the thumbnail shows the weird situation: a bargain chair losing its future before WIT understands the deal. | 92 | Recommended |
| 2 | Why Cheap Products Keep Getting Worse | Variant A: Cheap chair, missing future | Clear and close to the project title. The thumbnail adds the specific `future` question so the pair is not just `cheap + worse`. | 89 | Strong alternate |
| 3 | The Hidden Cost Of Cheap Products | Variant D: Later charges receipt | Clean hidden-cost logic, but the generated thumbnail is too cluttered and needs a remake before final use. | 85 | Usable after visual cleanup |
| 4 | Why Cheap Products Have Less Future | Variant E: Missing future box | Most distinctive title-metaphor pair, but the idea may be slightly harder for English learners before the video explains it. | 83 | Test only |
| 5 | Why Cheap Things Break So Fast | Variant C: Two weeks later | Very clear at a glance, but it risks promising only breakage and making the timeline too exact. | 82 | Backup |

## Recommended Package

- Title: `Why Cheap Products Don't Stay Cheap`
- Thumbnail concept: Variant A, a cheap chair with a sale tag, a falling screw, a hidden `not included` tag, and suspicious-betrayed WIT.
- Thumbnail label: `FUTURE?`
- Dominant object: cheap chair with sale price tag
- WIT emotion: suspicious-betrayed
- Visual contradiction: The product looks affordable now, but its future is already falling out.
- First 10 seconds payoff: The script hook immediately shows the same cheap chair and reveals `future not included`.
- Packaging score: `92/100`
- Decision: `recommended draft package`

## Thumbnail Comparison Notes

- Best thumbnail: Variant A, because it matches the actual hook object and creates the cleanest visual question.
- Best prompt to reuse manually: Variant A, with price corrected to `$9`.
- Most clickable: Variant A for curiosity; Variant C for instant before/after clarity.
- Clearest for mobile: Variant C, then Variant E.
- Biggest risk: Variant D, because the generated draft added unwanted branding/variant text and too much receipt detail.
- Recommended A/B order: A -> C -> B -> E -> D remake only.

## YouTube Description

### Final Description

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

`#WhyItWorks` `#ConsumerBehavior` `#RightToRepair`

### Links

- Channel link: `[add channel link]`
- Vox source: `https://www.vox.com/the-goods/23529587/consumer-goods-quality-fast-fashion-technology`
- European Parliament right to repair: `https://www.europarl.europa.eu/topics/en/article/20220331STO26410/right-to-repair-eu-action-to-make-repairs-more-attractive`
- European Commission smartphones and tablets: `https://energy-efficient-products.ec.europa.eu/product-list/smartphones-and-tablets_en`
- iFixit right to repair: `https://www.ifixit.com/Right-to-Repair`
- Repair.org: `https://www.repair.org/stand-up`
- Ellen MacArthur Foundation: `https://www.ellenmacarthurfoundation.org/a-new-textiles-economy`
- Wirecutter source: `https://www.nytimes.com/wirecutter/reviews/modern-appliances-short-lifespan/`
- Creator portfolio: `https://anhkhoa.info`

### Pinned Comment

```text
What cheap product did you have to replace too soon?

Mine is emotionally still a phone charger.
```

## Scorecard Notes

- 1-second clarity: `14/15` - Variant A has one obvious object, a readable label, and a clear WIT reaction.
- Curiosity gap: `19/20` - `FUTURE?` asks a strong question without explaining the whole mechanism.
- Visual contradiction: `15/15` - The cheap chair looks like a bargain while its future visibly falls out.
- WIT emotion: `9/10` - WIT reads suspicious and betrayed; keep the final face large.
- Title strength: `15/15` - `Don't Stay Cheap` names the hidden later cost in simple English.
- Title-thumbnail contrast: `10/10` - The title explains the hidden logic; the thumbnail shows the weird chair situation.
- First 10 seconds promise: `10/10` - The script hook already pays off the chair and `future not included` idea.
- Learner-friendly clarity: `5/5` - Title and label use common words, and the metaphor is explained immediately.
- Hard fails: `none for recommended package`; Variant D generated draft is not final-ready because of extra branding/variant text.

## Next Step Boundary

Next workflow step: `Voiceover`

Do not continue into voiceover, visual plan, HyperFrames, renders, upload, or self-learning until the user asks for the next skill or explicitly requests that step.
