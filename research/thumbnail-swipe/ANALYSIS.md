# Thumbnail teardown - @SticklyExplains vs @Simplewaysoflife

Collected 2026-07-28. 20 thumbnails per channel, ranked by view count.
Metadata pulled from YouTube's InnerTube endpoint, images from `i.ytimg.com`.
Per-channel `index.tsv` = rank, views, age, videoId, image quality, title.

- `stickly/` - @SticklyExplains ("Stickly"), 41.5K subs, ancient-humans explainers.
  **This is our direct competitor.** Same niche, same stick-figure format.
- `simplewaysoflife/` - @Simplewaysoflife ("Simple Ways of Life"), 26.2K subs, habits/self-improvement.
  Note: the handle is `Simplewaysoflife`, not `Simplewayoflife`.

---

## The two channels use OPPOSITE formulas. Both work.

|                         | Stickly                                      | Simple Ways of Life                 |
| ----------------------- | -------------------------------------------- | ----------------------------------- |
| Who carries the message | **The picture**                              | **The typography**                  |
| Text word count         | 1–4 (avg **2.4**)                            | 3–7, in 3 size tiers                |
| Text area               | ~18% of frame                                | ~45% of frame                       |
| Numbers used            | **1 of 20** (5%)                             | **12 of 20** (60%)                  |
| Text form               | Always a question, always `?`                | Statement / command                 |
| Background              | Full painted scene, dark                     | **Solid white**                     |
| Text color              | Yellow + thick black outline                 | Black + red, brush script           |
| Figure detail           | Simple face, big; co-star rendered in detail | Thin line art, no fill, small       |
| Emotional beat          | Curiosity ("what happens next?")             | Transformation ("that could be me") |

**Read that first row again.** Their top video (2M views) says only **"WHY NOT ATTACK?"** -
three words that mean nothing on their own. The picture supplies the entire question:
a stick figure asleep and defenseless, a wolf standing over him staring at the camera.

---

## Why Stickly goes viral - 6 mechanisms

Ranked by how much they matter. #1 and #2 are the whole game.

### 1. The question points at something you can SEE in the frame

Every single one of their 20 questions is about a physical object or creature present in the image:

> WHY NOT ATTACK? (a wolf) · ATE WHAT? (raw meat + berries) · FIRST SALT? (a salt pile) ·
> WHY FIGHT? (a dog and a cat) · TOOK DOWN MAMMOTHS? (a mammoth) · FOUND FIRE? (a fire) ·
> WHY NOT HUMANS? (an orca) · THUMBS = POWER? (a thumbs-up, a sabertooth backing off)

Zero abstract nouns. No "hollow", no "gap", no "belonging". A viewer scrolling at speed
never decodes a concept - they recognise a **thing**, then the 2-word question tells them
what's weird about it. Recognition is instant; concepts need a second reading, and you
don't get one.

**This is exactly why our v1 and v2 thumbnails failed.** "WHY THE HOLLOW?" and
"A 200,000-YEAR BUG?" ask about ideas that aren't visible. Nothing in the frame answers
"about what?", so no curiosity fires.

### 2. Two characters in visible conflict - a story, not a portrait

Never one figure alone. Always a **relationship with tension**:

- sleeping human ← → wolf watching (threat vs. vulnerability)
- human ← → bear with cubs (why is it not attacking?)
- human ← → dog and cat mid-snarl
- torch-holding human ← → glowing eyes in a dark cave

The tension is what makes you want the resolution. A single sad figure has no unresolved
question in it. Our v1 thumbnail was a portrait: mascot sad, crowd laughing, nothing
actually _happening between them_.

### 3. Animals do the heavy lifting

14 of 20 feature an animal: wolf, bear, orca, mammoth, sabertooth, dog, cat, mouse,
tortoise. Animals are the highest-recognition, highest-empathy objects available and they
read at 100px. **Crucially the animals are rendered in far more detail than the human** -
fur, shading, real anatomy - against the deliberately crude stick figure. That detail gap
is itself the visual hook.

### 4. Text is full-bleed, straight, and enormous

Edge to edge, left frame border to right frame border, top ~20%, **straight across - not
arced**. Cap height on the 2M thumbnail is roughly 90px of 720. An arc costs you 20–30%
of usable letter height because the curve must fit inside the same band. Their yellow +
thick black outline is the same signature as ours; the difference is purely that theirs is
**bigger and flatter**.

### 5. Dark scene under the text

Night skies, cave interiors, dusk. The top of the frame is always the darkest part, so
yellow text hits maximum contrast without needing an outline to survive. Our flat cobalt
blue is mid-value - the yellow fights it.

### 6. Eye contact with the camera

The wolf stares straight out at the viewer. So does the orca, the bear, the cave eyes.
A gaze aimed at the lens is one of the strongest known attention grabs. None of ours
has it - our mascot looks at the viewer but with a mild expression, and the crowd looks away.

---

## Why Simple Ways of Life goes viral - 5 mechanisms

### 1. The number is the largest object in the frame

`50`, `30`, `21`, `15`, `12`, `10`, `9`, `7` - set 2–3× the size of the words next to it,
in red, first thing in the reading path. This is the **number** you asked for, and note
how it's used: not as decoration next to a picture, but as the biggest graphic element
on the canvas.

### 2. Solid white background

In a feed of dark, busy, high-saturation thumbnails, pure white is the strongest possible
separator. Cheap and extremely effective. (Stickly wins the same fight from the opposite
direction - theirs are the darkest in the feed.) Either extreme beats mid-tone blue.

### 3. BEFORE → AFTER split with an arrow

6 of 20 use it: left = miserable figure (scribble cloud over head, empty pockets, bills),
arrow, right = glowing figure (sunglasses, money stacks, halo lines). Explicit
transformation. The viewer sees their current state on the left and the promise on the
right in one glance. Small black `BEFORE` / red `AFTER` tags anchor it.

### 4. Two-tier color-coded typography

Black for the setup word, **red for the emotional payload**: "BRAIN **ROT**",
"THINK **RICHER**", "10 HABITS **DESTROYING** YOUR BRAIN", "MILLIONAIRE **MODE**".
Yellow highlighter bars behind secondary lines add a third tier. Even at 100px you read
the red words first and get the gist.

### 5. One visual metaphor, universally legible

Brain melting out of a skull. Plug being yanked. Puppet strings cut by scissors. Chains
snapping. Figure on a mountain summit. No cultural knowledge needed, no text needed.

### 6. Persistent logo badge

Small circular brand mark, top-right, on all 20. Free recognition once a viewer has
watched one video. We have a logo (`brand/logo.png`) and use it on zero thumbnails.

---

## What our channel should copy

Our format (flat doodle mascot, yellow arc text, psychology/anthropology topics) is
Stickly's format. So **Stickly's mechanisms are the ones that transfer**; Simple Ways of
Life contributes the number treatment and the background-extreme lesson.

Concrete changes, in priority order:

1. **Ask about a visible object, never a concept.** Rewrite every question so the noun in
   it is drawn in the frame. Not "WHY THE HOLLOW?" but something pointing at a thing.
2. **Put two characters in tension.** Mascot + one other party, with something happening
   between them.
3. **Straighten the text and run it edge to edge.** Keep yellow + black outline (it's our
   signature) but drop the arc - it costs letter height for nothing.
4. **Darken the area under the text**, or go the other way to pure white. Stop using
   mid-value cobalt behind yellow.
5. **Make the number the biggest graphic object** if a number is used - Simple Ways of
   Life sizing, not a caption.
6. **One thing looks at the camera.**
7. **Add the logo badge** top-right, small, every time.

Open question worth noting: Stickly proves a viral thumbnail in our exact niche needs
**no number at all** - their 2M outlier has none, and only 1 of their top 20 does. The
number is Simple Ways of Life's mechanism, and it fits list-format videos ("50 habits")
better than single-idea explainers. For our loneliness video the strongest number is `40`,
because the script's opening line already makes it concrete: _surrounded by forty people_.
