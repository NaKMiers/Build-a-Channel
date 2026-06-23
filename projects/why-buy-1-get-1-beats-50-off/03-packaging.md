# 03 Packaging

Video: `Why Buy 1 Get 1 Free Beats 50% Off`

Status: `draft packaging`

Source skill: `packaging`

Source files:

- `00-topic-intake.md`
- `01-research-pack.md`

## Packaging Brief

- Core promise: two deals look like the exact same $5-per-item deal, but "Buy 1 Get 1 Free" usually doubles the store's profit and makes you spend more.
- Main contradiction: same per-item price on both signs, opposite outcome — the store wins, you spend double, and you smile while doing it.
- Audience question: "Wait — if both signs come to $5 an item, how is one a better deal for the store?"
- Recurring motif: two identical-looking price tags (`50% OFF` vs `BUY 1 GET 1 FREE`) + a hidden store-profit meter.
- WIT emotion: confident math face → suspicious squint → grinning/hypnotized by "FREE" → betrayed.
- First 10 seconds promise: two shelf signs, both come to $5/item, WIT says "so they're the same, right?", the register rings up 2× behind him — "...right?"
- Risk to avoid: dishonest math ("BOGO is ALWAYS double profit") or preachy anti-store framing. Keep the condition (high margin + shopper takes both units) and stay curious, not accusatory.

## Title Options

| # | Title | Promise | Curiosity | Risk | Score |
|---:|---|---|---|---|---:|
| 1 | Why "Buy 1 Get 1 Free" Beats "50% Off" | Names the hidden winner | High — two deals, one secretly better | Low | 92 |
| 2 | Same Deal. Double Profit. | Sharp contradiction | High — how can same be double? | Low | 90 |
| 3 | The $5 Deal That Makes You Spend $10 | Concrete money pain | High — the spend twist | Low | 89 |
| 4 | Why Stores Love "Free" More Than "Half Price" | Store-side logic | High | Low | 86 |
| 5 | "Free" Doesn't Cut the Price. It Cuts Your Judgment. | Names the insight | Med-High | Low | 85 |
| 6 | "50% Off" and "Buy 1 Get 1 Free" Are NOT the Same Deal | Direct myth-break | High | Low | 84 |
| 7 | The Word That Switches Off Your Math Brain | Curiosity-led | High — which word? | Med (vague topic) | 82 |
| 8 | Why "Buy 1 Get 1 Free" Is a Profit Machine | Store-side reveal | Med-High | Low | 81 |
| 9 | How "Free" Quietly Doubles Your Spending | Spend pain | Med-High | Low | 80 |
| 10 | Two Signs, Same Price, Double the Profit | Restates contradiction | Med-High | Low | 80 |
| 11 | Why Shops Prefer "Free" to "Half Price" | Store-side | Med | Low | 78 |
| 12 | The Hidden Math Behind "Buy 1 Get 1 Free" | Explainer promise | Med | Low (generic) | 76 |
| 13 | Why "Free" Always Costs You More | Pain-led | Med | Med (slight over-claim feel) | 75 |
| 14 | You Didn't Get It Free. You Got a Hostage. | Funny/edgy | Med | Med (joke as title risks clarity) | 72 |
| 15 | Why "Buy 1 Get 1 Free" Was Invented 250 Years Ago | History hook | Med | Med (buries the core hook) | 70 |

## Thumbnail Concepts

Intensity: MAX shock / clickbait / outrage / curiosity (owner-requested). Honesty line kept — real numbers ($5/$10/$1/$2), curiosity-question hooks, no fake urgency, no fake stat, no hateful brand targeting.

| # | Concept | Dominant object | Label | WIT emotion | Visual contradiction | Prompt / Production notes |
|---:|---|---|---|---|---|---|
| A | Split screen: `50% OFF` half vs `BUY 1 GET 1 FREE` half, both "$5/item" circled red | Two shelf price tags | `A TRICK?!` | Furious / betrayed scream | Identical $5 price, two different signs | Comparison style; attach comparison layout ref |
| B | Split screen: store profit meter low (`50% OFF`) vs exploding 2× high (`BOGO`) | Store-profit gauge | `ROBBED?!` | Enraged, hands thrown up | Same deal to you, double profit to store | Store-side hypothesis; comparison style |
| C | WIT drowning in an avalanche of duplicate "FREE"-stickered units | Overflowing basket of duplicates | `FREE?!` | Screaming panic | "Free" pile = a $10 receipt, not savings | Trap/dramatic single scene |
| D | Face-zoom meltdown: WIT screaming, two crushed bottles, giant red `$10` receipt | Receipt with red `$10` | `$10?!` | Maximum screaming shock | Expected $5, total says $10 | Shock face-zoom; one shocking element |
| E | Giant "FREE" sticker blindfolds a manic WIT while his wallet erupts | Glowing `FREE` sticker | `FREE = TRAP` | Hypnotized glee → drained | Looks ecstatic while money explodes out | Dramatic metaphor (free cuts judgment) |

## Thumbnail A/B Test

| Variant | Style | Image / Path | Prompt ref | Label | WIT pose / emotion | WIT consistency | Score | Strength | Risk | Decision |
|---|---|---|---|---|---|---|---:|---|---|---|
| A | Comparison split-screen (shopper) | `prompt only / image not generated` (`assets/thumbnails/variant-a-generated.png`) | Variant A | `A TRICK?!` | Furious/betrayed scream on divider | Pending (verify on-model after generation) | 90 | Cleanest 1-second contradiction + outrage; mirrors approved comparison style | Two-tag idea must read instantly at mobile size | Generate (A/B test 2) |
| B | Comparison split-screen (store) | `prompt only / image not generated` (`assets/thumbnails/variant-b-generated.png`) | Variant B | `ROBBED?!` | Enraged, hands up, glaring at exploding meter | Pending | 88 | Tests our unique store-profit edge with rage hook | "Profit meter" is slightly more abstract than tags | Generate (A/B test 3) |
| C | Trap / dramatic scene | `prompt only / image not generated` (`assets/thumbnails/variant-c-generated.png`) | Variant C | `FREE?!` | Screaming panic, drowning | Pending | 84 | High drama, strong "system happens to WIT" | Avalanche could get cluttered; keep duplicates clean | Backup / drama test |
| D | Shock face-zoom | `prompt only / image not generated` (`assets/thumbnails/variant-d-generated.png`) | Variant D | `$10?!` | Screaming meltdown, two crushed bottles | Pending | 88 | Loudest single emotional face; best mobile shock read | Face-zoom risks generic-shock if `$10` not huge | Generate (A/B test 1) |
| E | Dramatic metaphor | `prompt only / image not generated` (`assets/thumbnails/variant-e-generated.png`) | Variant E | `FREE = TRAP` | Hypnotized glee, blindfolded, wallet erupting | Pending | 83 | Best at carrying the payoff insight | More conceptual; needs the wallet-explosion to read fast | Higher-risk swing |

WIT consistency note: every prompt uses the current draft thumbnail-WIT (white round head, thick black outline, oversized black glasses, expressive eyebrows, simple white body) and explicitly bans the removed `original-wit-24` details (hair, shirt, receipt-tie, shoes). Mark any generated output that adds hair/shirt-tie/shoes as off-model and re-roll before recommending.

## Thumbnail Generation Prompts

> No image-generation tool is available in this environment, so all five are prompt-only. Generate in ChatGPT/DALL·E using the self-contained blocks in `assets/thumbnails/PROMPTS.md` (WIT reference image attached; comparison layout ref attached for A & B). The blocks below are the same MAX-intensity prompts with an explicit negative/avoid list for reuse in other image platforms.
>
> Intensity dialed to MAX shock / clickbait / outrage / curiosity (owner request). Honesty line held: real numbers ($5/$10/$1/$2), curiosity-question hooks (`?!`), NO fake urgency ("only today"), NO fabricated stats, NO hateful real-brand targeting.

### Variant A: `Comparison split-screen — "A TRICK?!"`

Prompt:

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon
figure with thick imperfect black outline, oversized black glasses, expressive eyebrows, small black
dot eyes, simple white body, clean bold silhouette. WIT should match the character style from the five
restored Why Cheap Products Keep Getting Worse thumbnails. WIT emotion: FURIOUS and betrayed —
bulging eyes, mouth wide open mid-shout, eyebrows slammed down, sweat flying, red rage glow and
comic shock-burst lines behind his head.

16:9, 1280x720 YouTube thumbnail, EXTREME clickbait energy. Split the frame down the middle with a
thick jagged vertical divider like a lightning crack. LEFT half cool-blue: a huge yellow shelf price
tag "50% OFF" with small handwritten "$5 / item" beneath. RIGHT half angry warm-orange/red: a huge
yellow shelf price tag "BUY 1 GET 1 FREE" with the same small "$5 / item". BOTH "$5 / item" prices are
aggressively circled in thick rough red marker with a fat red arrow between them. Small black angled
corner tag top-left "HALF PRICE", top-right "FREE". Center hook over the divider: a GIANT rough
red-and-white handwritten "A TRICK?!" with a violent red double-underline. Furious WIT stands on the
divider. High contrast, bold flat colors, readable at tiny mobile size.
```

Negative prompt / avoid:

```text
no hair, no shirt, no tie, no shoes, no extra clothing or accessories on WIT; no real brand logos; no
photographic backgrounds; no extra products or clutter; no paragraphs of text; no "only today" or other
fake-urgency text; no text other than the labels described; not low-contrast; not tiny WIT face.
```

Use notes:

- Attach `wit-pose-neutral-front.png` + the comparison layout ref `variant-c-generated.png`.
- Save as `variant-a-generated.png`. Shopper-facing curiosity+outrage comparison.

### Variant B: `Comparison split-screen — "ROBBED?!"`

Prompt:

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon
figure with thick imperfect black outline, oversized black glasses, expressive eyebrows, small black
dot eyes, simple white body, clean bold silhouette, matching the restored Why Cheap Products thumbnail
WIT. WIT emotion: ENRAGED and robbed — jaw on the floor, eyes popping, hands thrown up, sweat flying,
red rage glow and shock-burst lines behind him.

16:9, 1280x720 YouTube thumbnail, EXTREME clickbait energy. Split frame with a thick jagged vertical
divider. LEFT half cool-blue: a "store profit" gauge filled to ONE tiny low bar, big handwritten "50%
OFF" above, a small "+$1" tag. RIGHT half angry red: the SAME gauge exploding TWICE as high to two
towering bars glowing hot red and overflowing with cartoon dollar signs, big handwritten "BUY 1 GET 1
FREE" above, a fat "+$2" tag, a thick red arrow blasting straight up. Small black angled corner tag
top-left "YOU", top-right "THE STORE". Center hook over the divider: a GIANT rough red-and-white
handwritten "ROBBED?!" with a violent red double-underline. Enraged WIT on the divider glaring at the
towering right meter. High contrast, bold flat colors, readable at tiny mobile size.
```

Negative prompt / avoid:

```text
no hair, no shirt, no tie, no shoes, no accessories on WIT; no real brand logos; no photographic
backgrounds; no clutter; no fake-urgency text; no text other than the labels described; keep the gauge
a simple two-bar-vs-one-bar meter; not low-contrast.
```

Use notes:

- Attach `wit-pose-neutral-front.png` + comparison layout ref `variant-c-generated.png`.
- Save as `variant-b-generated.png`. Tests the store-profit hypothesis with a rage hook.

### Variant C: `Trap / dramatic scene — "FREE?!"`

Prompt:

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon
figure with thick imperfect black outline, oversized black glasses, expressive eyebrows, small black
dot eyes, simple white body, matching the restored Why Cheap Products thumbnail WIT. WIT emotion: full
SCREAMING panic — eyes bulging out, mouth stretched wide, sweat spraying, arms flailing, comic motion
lines and a red danger glow.

16:9, 1280x720 YouTube thumbnail, EXTREME clickbait energy. One chaotic scene: WIT buried up to his
screaming face and drowning inside a wildly overflowing shopping basket, swallowed by a giant avalanche
of identical duplicate products (the same bottle repeated dozens of times) toppling onto him, each
slapped with a loud yellow "FREE" sticker. Blasting in from the upper corner, a glowing receipt with a
HUGE bold red total "$10" and a tiny crossed-out "$5", a fat red arrow stabbing the "$10". One GIANT
rough handwritten label "FREE?!" with a violent red double-underline. Hot red danger lighting, tight
crop so WIT's screaming face dominates. Bold flat colors, very high contrast, readable at tiny mobile
size.
```

Negative prompt / avoid:

```text
no hair, no shirt, no tie, no shoes on WIT; no real brand logos; no photographic backgrounds; no
readable paragraphs; no fake-urgency text; no text other than the labels described; keep duplicates
clean and obviously identical, not unreadable mush; don't crop WIT's head or glasses out of frame.
```

Use notes:

- Attach `wit-pose-neutral-front.png`. Save as `variant-c-generated.png`.
- Drama/backup test; keep the duplicate avalanche clean enough to read.

### Variant D: `Shock face-zoom — "$10?!"`

Prompt:

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon
figure with thick imperfect black outline, oversized black glasses, expressive eyebrows, small black
dot eyes, simple white body, matching the restored Why Cheap Products thumbnail WIT. WIT emotion:
SCREAMING meltdown — eyes bulging huge out of the glasses, jaw ripped wide open, eyebrows flying off,
sweat spraying, trembling, comic shock-burst lines and a hot red rage glow.

16:9, 1280x720 YouTube thumbnail, MAXIMUM shock clickbait. Extreme tight close-up: WIT's round head and
glasses BLOW UP to fill the whole LEFT half of the frame, clutching two identical bottles crushed one
in each hand. On the RIGHT, ONE giant shocking element: a glowing white receipt with a MASSIVE bold red
total "$10" and a tiny crossed-out "$5" above it, a fat red arrow slamming from WIT's face into the
"$10", and a red circle around it. One tiny handwritten label "WAIT". Strong red glow behind the
receipt, motion lines everywhere, extreme contrast, readable at tiny mobile size.
```

Negative prompt / avoid:

```text
no hair, no shirt, no tie, no shoes on WIT; no real brand logos; no photographic backgrounds; no
clutter; no fake-urgency text; no text other than the labels described; make "$10" enormous and bold so
it isn't a generic shocked face; don't crop the glasses or head edge awkwardly.
```

Use notes:

- Attach `wit-pose-neutral-front.png`. Save as `variant-d-generated.png`.
- Loudest single emotional face; lead A/B test.

### Variant E: `Dramatic metaphor — "FREE = TRAP"`

Prompt:

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon
figure with thick imperfect black outline, oversized black glasses, expressive eyebrows, small black
dot eyes, simple white body, matching the restored Why Cheap Products thumbnail WIT. WIT emotion:
hypnotized maniac grin (totally blind to the danger) — dark dramatic irony.

16:9, 1280x720 YouTube thumbnail, EXTREME clickbait energy. One bold metaphor: a HUGE glowing yellow
"FREE" sticker slapped across WIT's glasses like a blindfold so he's totally blind, grinning like a
hypnotized maniac, both arms greedily lunging to grab a second product. On his other side, hidden from
him, his wallet ERUPTS — a fountain of coins and bills blasting out and vanishing into a dark void,
with a red downward arrow and a "−$10" tag. Brutal contrast: ecstatic while being drained. One GIANT
rough handwritten hook "FREE = TRAP" with a violent red double-underline. Hot red warning glow at the
exploding wallet, dramatic shadow, warm retail-yellow palette, tight composition, extreme contrast,
readable at tiny mobile size.
```

Negative prompt / avoid:

```text
no hair, no shirt, no tie, no shoes on WIT; no real brand logos; no photographic backgrounds; no
clutter; no fake-urgency text; no text other than the labels described; keep the wallet-explosion
obvious and fast to read; not low-contrast; don't crop WIT's head.
```

Use notes:

- Attach `wit-pose-neutral-front.png`. Save as `variant-e-generated.png`.
- Higher-risk conceptual swing that best carries the payoff insight.

## Title-Thumbnail Packages

| Rank | Title | Thumbnail concept | Why it works | Score | Decision |
|---:|---|---|---|---:|---|
| 1 | `Why "Buy 1 Get 1 Free" Beats "50% Off"` | Variant D — `$10?!` face-zoom meltdown | Title names the hidden winner; loudest single-face shock + the $10 receipt pays it off — zero title-text repeat, max contrast | 93 | Recommended |
| 2 | `The $5 Deal That Makes You Spend $10` | Variant A — `A TRICK?!` split screen | Title sets the $5→$10 pain; comparison shows the "same price" trap + outrage | 91 | Strong A/B alt |
| 3 | `Same Deal. Double Profit.` | Variant B — `ROBBED?!` profit meter | Strongest store-side contradiction; thumbnail proves the "double" visually with a rage hook | 90 | Strong A/B alt |
| 4 | `"Free" Doesn't Cut the Price. It Cuts Your Judgment.` | Variant E — `FREE = TRAP` blindfold | Title + metaphor both land the payoff insight; most "smart" pairing | 84 | Test if A/B plateaus |
| 5 | `Why Stores Love "Free" More Than "Half Price"` | Variant C — `FREE?!` trap scene | Store-side title + chaos drama; good for a comedy-forward cut | 84 | Backup |

## Recommended Package

- Title: `Why "Buy 1 Get 1 Free" Beats "50% Off"`
- Thumbnail concept: Variant D — face-zoom meltdown, WIT screaming with two crushed bottles next to a giant red `$10` receipt (crossed-out `$5`)
- Thumbnail label: `$10?!`
- Dominant object: receipt with a massive red `$10` total
- WIT emotion: screaming shock / betrayal
- Visual contradiction: he grabbed the "free" one expecting $5, the receipt screams $10
- First 10 seconds payoff: two shelf signs → both = $5/item → "so they're the same, right?" → register rings up 2× → "...right?" (pays the title-thumbnail promise by second 10)
- Packaging score: `93/100`
- Decision: `Recommended`. Lead thumbnail D (loudest, no title-text repeat); run A/B as D vs A vs B.

## Thumbnail Comparison Notes

- Best thumbnail: Variant D (loudest single-face shock; no title-text repeat; carries max clickbait energy)
- Best prompt to reuse manually: Variant A (most controlled comparison layout; reusable for any "two signs, same price" beat)
- Most clickable: Variant D (biggest screaming face + giant `$10`) closely followed by A (`A TRICK?!`) and B (`ROBBED?!`)
- Clearest for mobile: Variant D (one huge face + one huge number)
- Biggest risk: Variant E (conceptual — the wallet-explosion must read instantly or it's just a grinning WIT)
- Recommended A/B order: D → A → B → C → E

## YouTube Description

### Final Description

```text
"50% off" and "Buy 1 Get 1 Free" can cost you the exact same $5 per item — so they feel like the same
deal. They're not.

One of them quietly doubles the store's profit and gets you to spend more, while you walk out smiling.
In this video we do the honest math on both signs, show why "free" beats "50% off" for the store, and
explain the one word that switches off the part of your brain that does math.

You'll learn:
• Why the per-item price can be identical but the deals are not
• How "Buy 1 Get 1 Free" can roughly double a store's profit (and when it doesn't)
• Why "free" feels better than "half price" — even when it costs you more
• The hidden "Buy 1 Get 1 50% off" trick that's really only 25% off
• When 50% off is actually the smarter choice for YOU

A discount cuts the price. "Free" cuts your judgment.

This is "Why It Works" — money, the internet, and modern life, explained in simple English without the
boring part.

#WhyItWorks #BuyOneGetOneFree #MoneyTips
```

### Alternate First Two Lines

```text
You see "50% OFF" on one shelf and "BUY 1 GET 1 FREE" on the next. Same $5 an item. Same deal, right?
Wrong — and the store is counting on you believing it.
```

### Chapters

```text
draft until script
```

(Provisional chapters from the explanation spine, to be timed after the voiceover step:)

```text
0:00 Two signs, same price
0:xx Same to you isn't same to them
0:xx The receipt: spend $5 vs spend $10
0:xx The word FREE
0:xx Why the price still looks "real" (anchoring)
0:xx When BOGO is NOT a store win (loss leaders)
0:xx A discount cuts the price; free cuts your judgment
```

### Tags / Keywords

```text
why it works, buy one get one free, bogo, 50 percent off, half price, is bogo a good deal,
buy one get one free vs 50 off, retail psychology, pricing psychology, zero price effect,
power of free, price anchoring, loss leader, money tips, how stores make money, shopping psychology,
spend less money, deal psychology, learn english money, simple english explainer
```

### Hashtags

```text
#WhyItWorks #BuyOneGetOneFree #MoneyTips
```

### Links

```text
▶ More money & modern-life explainers: [playlist link placeholder]
🔔 Subscribe to Why It Works: [channel link placeholder]
📩 [optional newsletter/contact placeholder]
```

### Pinned Comment

```text
Quick honest note: "Buy 1 Get 1 Free" only roughly doubles the store's profit when the item is
high-margin AND you actually take both units. On cheap staples (milk, bread) it's often a "loss leader"
— the store loses a little to get you in the door. And if you only needed ONE, 50% off is the better
deal for you. What's the most pointless "free" thing a BOGO ever talked you into? 👇
```

## Scorecard Notes

- 1-second clarity (`/15`): 14 — two tags + "SAME?" reads instantly at mobile size
- Curiosity gap (`/20`): 19 — "same $5, but one beats the other" is a clean "wait, that's true"
- Visual contradiction (`/15`): 14 — identical price, two signs; the core motif is built in
- WIT emotion (`/10`): 9 — suspicious math face, one clear readable emotion
- Title strength (`/15`): 14 — names the hidden winner, learner-simple, specific
- Title-thumbnail contrast (`/10`): 9 — title names the logic, thumbnail shows the situation; no phrase repeat
- First 10 seconds promise (`/10`): 9 — hook beats pay off the click by second 10
- Learner-friendly clarity (`/5`): 4 — high-frequency shopping English ("free", "half price", "$5")
- Hard fails: none triggered
- Total: `92/100`

## Next Step Boundary

Next workflow step: `independent side branch`

Do not continue into script, voiceover, visual plan, render, review, upload, or learning until the user asks for that step.
