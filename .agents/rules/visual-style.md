# Visual style - V1 legacy and V2 current art systems

Canonical source for how a TossExplains scene or character sheet looks. Read this before
writing any scene prompt, reference sheet, or thumbnail prompt. Thumbnail prompts preserve
the character identity rules here but use the separate rendering exception below.

## V1 LEGACY VERBATIM STRINGS

These four strings appeared 7, 7, 7, and 2 times across the retired prompt files.
That duplication is how a contradiction survived undetected. They now exist here
once. **Copy them character for character. Never paraphrase, never re-type from
memory, never "improve" the wording.** The `check` skill greps for them.

The STYLE ANCHOR and STYLE LOCK heading names are extractor keys and remain unchanged.
The thumbnail-only exception below overrides the word `thumbnail` in those historical
heading names.

### STYLE ANCHOR - opens every image and thumbnail prompt

```
Hand-drawn 2D doodle cartoon animation, flat colors, bold black outlines, slightly imperfect sketchy marker lines,
```

### STYLE LOCK - closes every image and thumbnail prompt

```
no gradients, no shadows, no textures, no photorealism, no 3D, no timestamp shown in the image, @[name] is mention syntax for reference only and must never be rendered as visible text, 16:9 aspect ratio, educational YouTube explainer doodle style.
```

### GENERATION LINE - the instruction the human adds to every generation

```
match the attached character reference exactly, no photorealism, no 3D render, no gradients, no drop shadows, no textures, no realistic faces, no anime style
```

### REFERENCE SHEET OPENING LINE - opens every character sheet prompt

```
Create a clean character reference sheet for ONE simple hand-drawn 2D doodle cartoon character.
```

These V1 strings remain valid for Projects 1 through 5 and for any project whose existing
`image-prompts.md` already uses the V1 anchor. Never rewrite those projects to V2.

## V2 CURRENT VERBATIM STRINGS

These strings apply to new projects. Their heading names are extractor keys and must not be
renamed. Copy them character for character.

### V2 STYLE ANCHOR - opens every V2 scene prompt

```
Hand-drawn 2D editorial storybook doodle animation, semi-flat colors on a warm paper-based palette, expressive charcoal outlines with subtle line-weight hierarchy,
```

### V2 STYLE LOCK - closes every V2 scene prompt

```
restrained paper grain, clear visual hierarchy, no photorealism, no 3D, no CGI, no anime, no manga, no realistic anatomy, no glossy vector finish, no busy decoration, no timestamp shown in the image, @[name] is mention syntax for reference only and must never be rendered as visible text, 16:9 aspect ratio, Warm Editorial Storybook Doodle style.
```

### V2 GENERATION LINE - the instruction the human adds to every V2 generation

```
match the attached character reference exactly, preserve the named plate composition for variants, keep saturated channel blue reserved for Toss or one semantic diagram signal, no photorealism, no 3D render, no CGI, no realistic faces, no anime style
```

### V2 REFERENCE SHEET OPENING LINE - opens every V2 character sheet prompt

```
Create a clean V2-compatible character reference sheet for ONE simple hand-drawn 2D editorial doodle cartoon character.
```

## Why the style lock repeats the no-visible-text negative

The `[MM:SS]` timestamp prefix and every `@TOKEN` are instructions for the human and
the file system, not visual content. They must never appear as rendered text in the
generated image: no timestamp, clock, or counter burned into a corner, no literal
"@NAME" caption anywhere in the frame. That is why the style lock explicitly repeats
the negative. **Never drop it when writing or editing a prompt.**

## Thumbnail-only exception

Thumbnail prompts do not use the scene STYLE ANCHOR, STYLE LOCK, or GENERATION LINE.
Thumbnails preserve the attached TossExplains character designs but use the separate
self-contained cinematic rendering system in `.agents/rules/thumbnail-rules.md` and
`.agents/skills/thumbnail/references/style-spec.json`. That system allows controlled
gradients, soft shadows, painted texture, atmospheric depth, and warm light spill.

This exception applies only to thumbnail prompts. V1 video scenes keep the legacy flat rules.
V2 video scenes use the controlled depth rules below. Character reference sheets remain clean,
flat, and texture-free in both versions so they function as identity documents.

## V1 legacy art style

- **Art style:** hand-drawn 2D doodle cartoon animation. Flat colors, bold black
  outlines, slightly imperfect sketchy lines as if drawn fast with a marker.
- **Characters:** simple stick figures with large circular heads, dot eyes,
  expressive thick brow lines. Sometimes fully colored heads or bodies (red = hot or
  embarrassed, white = neutral).
- **Animals and objects:** chunky simplified cartoon shapes. Big, bold, flat
  single-color fills with thick black outlines.
- **Backgrounds:** flat solid color blocks only. White is the default. Green strip
  along the bottom = ground. Blue sky plus green ground = outdoor. Solid orange =
  sunset, fire, ancient. Solid blue = underwater. Tan = desert or cave. ZERO
  gradients. ZERO shadows. ZERO textures.
- **On-screen text:** bold ALL CAPS hand-lettered marker font, placed at the top of
  the frame. Color is RED, BLACK, or YELLOW.
- **Labels and arrows:** black or yellow diagonal arrows pointing at objects, short
  ALL CAPS word beside the arrowhead.
- **Thought bubbles:** classic cloud shape with ALL CAPS text inside, for example
  "HMMMM", "?", "WAIT...".
- **Aspect ratio:** always 16:9.

## V1 legacy palette

| Color         | Hex       |
| ------------- | --------- |
| Orange        | `#F5820D` |
| Cobalt blue   | `#2D5FBF` |
| Grass green   | `#3A9E3A` |
| Golden yellow | `#F5C518` |
| Red           | `#D94040` |
| Brown         | `#8B5E3C` |
| Sky blue      | `#6EB5E8` |
| Tan           | `#C4965A` |
| White         | `#FFFFFF` |

## V1 legacy background tone map

### WHITE IS THE DEFAULT, AND THE DEFAULT IS THE MAJORITY

**Plain white is what a frame gets unless the moment earns something else.** The channel is a
light, clean doodle explainer. A dark frame is a deliberate exception, never a mood you drift
into because the script is set at night or is emotionally heavy.

This is not advisory. Project 2's first pass came back **40 percent blue and only 37 percent
white**, and the user rejected the whole set as dark and ugly. The accepted project 1 runs
**58 percent white**. Target that.

**Budget for a finished `image-prompts.md`:**

| Background                      | Share                             | When                                         |
| ------------------------------- | --------------------------------- | -------------------------------------------- |
| **plain white**                 | **55 to 75 percent**              | the default, and every modern everyday scene |
| tan `#C4965A`                   | up to 15 percent                  | ancient, prehistoric, tribal                 |
| solid orange `#F5820D`          | up to 10 percent                  | fire, ritual, the night gathering            |
| flat green ground + blue sky    | up to 10 percent                  | outdoor, nature, walking                     |
| **solid cobalt blue `#2D5FBF`** | **5 to 15 percent, hard ceiling** | **only literally inside the mind**           |

**Cobalt blue is not "night", "sad", or "serious".** It means the frame is showing the inside
of someone's head: a white doodle brain, a thought loop, a memory replaying as an object. If
there is no brain, loop, or thought-object as the subject, it is not a mind frame and it is
white. A 2am bedroom is modern everyday life and gets **plain white**, with the night carried
by a small crescent moon in a window and a caption, exactly as the accepted fixture does it.

Do not use a dark ground for the lab or the experiment frames either. Older wording said
"science, lab, experiment -> solid blue"; the accepted fixture uses that zero times. Labs are
plain white with the few objects that matter.

| Moment                                                                      | Background                                                                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Modern everyday life (phone, bed, office, sofa, street, party, shower, car) | **plain white** with only the few objects that matter                             |
| Science, lab, experiment, restaurant                                        | **plain white** with the table, chair, and apparatus drawn                        |
| Concept, diagram, chart, icon frames                                        | **plain white**                                                                   |
| Danger, threat, social fear                                                 | stark white with red text                                                         |
| Happy, triumph, discovery, relief                                           | bright white                                                                      |
| Ancient, prehistoric, tribal                                                | tan `#C4965A`                                                                     |
| Fire, night ritual, the gathering                                           | solid orange `#F5820D`                                                            |
| Outdoor, nature, walking                                                    | flat green `#3A9E3A` ground plus plain blue sky                                   |
| Inside the mind, thoughts, memory                                           | solid cobalt blue `#2D5FBF` with a white doodle brain or floating thought objects |

## On-screen text colour

The palette allows red, black, and yellow. **In practice use black and red only.** The
accepted fixture uses black 114 times, red 44 times, and yellow zero times.

- **Black is the default** for a neutral label, a number, a name, or a section marker.
- **Red is reserved** for danger, threat, failure, and negation: `PETTY?`, `NO AUDIENCE`,
  `MORE AGGRESSIVE`, `NOT A RELEASE`.
- **Never yellow on a white background.** It is unreadable. Yellow lettering belongs to
  thumbnails, where it always sits on a dark band. Four of project 2's first-pass captions were
  yellow on white before this was caught.

## Where emotion lives

This channel is psychology-first, so most scenes are one cast member feeling
something. Show the emotion in the eyebrows, the mouth line, the body posture, and
the head color. **Never in background detail.** Keep every frame down to the fewest
objects that carry the idea.

**Head color code:**

- red = embarrassed, angry, overheated
- white = neutral
- blue-tinted = sad, cold, lonely

## The nine proven frame types

Use these when appropriate rather than inventing a layout.

1. **Concept text frame** - large object (hourglass, clock, skull, phone) centered
   plus bold ALL CAPS text at top. No characters needed.
2. **Then vs now split frame** - vertical black divider. Left side tan background
   with the ancestral cast member, right side white background with `@YOU` in modern
   life, doing the emotional equivalent.
3. **Labeled diagram** - doodle brain, body, or object with a yellow diagonal arrow
   plus an ALL CAPS label word.
4. **Cast reaction** - thought bubble above a cast member's head with "?", "HMMMM",
   "!", or "WAIT...".
5. **The tribe frame** - the group entry in a ring around a fire, with one cast
   member inside, outside, or turned away. The core anthropology visual for
   belonging, status, and exile.
6. **Villain personified** - an abstract concept given an angry cartoon face: a
   phone with teeth, a brain with boxing gloves, a comparison chart with eyes.
7. **Experiment frame** - cast members in a simple lab setup (a table, two doors, a
   row of chairs, a button) with the researcher's name in ALL CAPS at the top.
8. **Status ladder** - cast members stacked on stair steps or a podium, one looking
   up at the one above.
9. **Evolution sequence** - left-to-right creature or human progression with a
   right-pointing arrow.

## Translating abstract narration into concrete visuals

If the script says "your body doesn't know the difference", show `@YOU` confused,
looking back and forth at two identical objects. If it says "millions of years",
show a large hourglass with bold red ALL CAPS text "MILLIONS OF YEARS" at the top of
the frame. Never render an abstraction as an abstraction.

## V2 current art system

### Direction and mood

The current direction is **Warm Editorial Storybook Doodle**. It is a hand-drawn editorial
illustration and infographic hybrid: curious, warm, specific, slightly imperfect, and easy to
read on a phone. Each beat should feel like a small illustrated story, a clear editorial card,
or a satisfying build toward a payoff.

The V2 system keeps Toss, simple faces, orange and cobalt brand memory, clear diagrams, and 2D
hand-drawn construction. It adds warm paper surfaces, chapter color coding, story-specific
environments, line hierarchy, planned shot variation, progressive builds, and limited depth.

### V2 palette

| Role         | Color         | Hex       | Use                                                     |
| ------------ | ------------- | --------- | ------------------------------------------------------- |
| Warm paper   | Cream         | `#FFF4DE` | default card surface and modern neutral                 |
| Ink          | Charcoal      | `#2F3133` | outlines, neutral text, diagrams                        |
| Brand 1      | Orange        | `#F5820D` | energy, ritual, key brand memory                        |
| Mascot       | Toss blue     | `#2E77C4` | Toss's default hoodie, fixed by `brand/MASCOT.jpeg`     |
| Brand 2      | Cobalt        | `#2D5FBF` | mind interiors, trust, cool diagram contrast            |
| Verdict      | Red           | `#D94040` | negation, threat, decisive conclusion                   |
| History      | Tan           | `#C4965A` | anthropology and ancestral worlds                       |
| Human warmth | Coral         | `#D96F5F` | relationships, shame, attachment, social scenes         |
| Nature       | Olive         | `#8FA35A` | landscape, regulation, belonging                        |
| Science      | Dusty teal    | `#67A6A3` | mechanisms, experiments, body systems                   |
| Memory       | Lavender      | `#B79AD9` | memory, perception, unusual cognition                   |
| Highlight    | Golden yellow | `#F2C14E` | small object highlight, never body text on light ground |

Each episode selects three chapter colors plus cream, charcoal, orange, Toss blue, cobalt, and
red. Do not use the entire extension palette in one video. Saturated channel blue is reserved for
Toss's default costume or one semantic diagram signal. Generic crowd clothing must use dusty blue
or another chapter color instead.

### V2 background budget

| Surface family                 | Target | Purpose                                              |
| ------------------------------ | -----: | ---------------------------------------------------- |
| Warm cream or off-white cards  |    30% | clean explanations, modern life, number cards        |
| Light tinted chapter cards     |    20% | topic changes, definitions, compact diagrams         |
| Illustrated story environments |    35% | hooks, experiments, anthropology, modern mismatch    |
| Cobalt mind interiors          |     7% | only literal thought, memory, or attention interiors |
| Pure white cards               |     8% | dense science or deliberate contrast pauses          |

Treat the percentages as a finished contact-sheet target with a tolerance of 5 percentage
points, except cobalt and pure white are hard ceilings of 10 and 15 percent respectively. One
near-dark hero frame may punctuate a major reveal, then the sequence must return to the light
system. Dark mode is not a chapter palette.

### V2 render tiers

Every planned beat names exactly one tier.

#### CLEAN

- Target about 40 percent of visual beats.
- Warm cream, pure white, or one light chapter tint.
- Flat fills, charcoal outlines, no atmospheric blur.
- One to four objects and generous negative space.
- Best for cards, numbers, labels, diagrams, and direct reactions.

#### LAYERED

- Target about 50 percent of visual beats.
- Three depth planes created by overlap, scale, crop, and color value.
- One restrained contact shadow may clarify grounding.
- Very subtle paper grain may unify the frame.
- At most two tonal values inside one object.
- Best for story scenes, experiments, rooms, camps, streets, and historical worlds.

#### ATMOSPHERIC

- Hard ceiling of 10 percent of visual beats.
- Reserved for hook hero shots, chapter transitions, reveals, and ending payoffs.
- One motivated gradient, glow, light spill, or softened background is allowed.
- Foreground characters and key graphics stay clearly 2D and hand-inked.
- Never use it for an ordinary narration beat.

### V2 line and character treatment

- Use charcoal rather than absolute black where possible.
- Use medium-heavy outer contours for the focal subject.
- Use thinner internal details and background lines.
- Keep a slightly imperfect hand-drawn wobble.
- Give secondary cast story-specific clothing, hair silhouettes, and props while keeping their
  faces simple.
- Do not use clothing color as the only identity system.
- Toss may narrate, participate, or observe, but must not be a static presenter for four
  consecutive beats.

### V2 visual registers

Every visual beat names exactly one register before its prompt is written.

| Register       | Job                                                   | Target share |
| -------------- | ----------------------------------------------------- | -----------: |
| STORY          | concrete action inside a place                        |    30 to 40% |
| CARD           | object, number, title, or concise editorial verdict   |    15 to 20% |
| DIAGRAM        | causal mechanism, experiment, anatomy, or flow        |    15 to 20% |
| PORTRAIT       | face, posture, emotion, or researcher                 |    10 to 15% |
| HYBRID         | story scene plus diagram overlay or question layer    |    10 to 15% |
| SPLIT_OR_SCALE | comparison, then-vs-now, crowd, distance, probability |     5 to 10% |

Change register after two or three beats on average. Four consecutive beats in one register are
legal only when they share one plate and form an intentional progressive build.

### V2 shot grammar

Every 30 second block should contain at least four of these seven shot tasks:

- wide establishing shot
- medium action shot
- character close-up
- macro object detail
- overhead or POV hands
- card or diagram
- scale or crowd metaphor

Do not use the same camera distance more than twice in a row unless the beats are a deliberate
build. New plates define a camera axis. Variants preserve that axis, cast placement, environment
geometry, object positions, palette, and line hierarchy.

### V2 progressive disclosure

A 10 to 12 minute episode should contain 5 to 8 build chains with 3 to 4 beats per chain. Each
chain has one base plate, composition-preserving variants, one information change per variant,
and a payoff that changes the meaning of the finished plate.

Valid deltas include one object, arrow, label, character, crossed-out state, changed number, or
revealed cause. Expression-only changes count only when the emotion itself is the meaning change.

### V2 text system

- Text appears on roughly 25 to 35 percent of beats.
- Use one to five words where possible.
- Neutral labels and researcher names use charcoal.
- Verdicts and negations use red.
- White text is legal only on a deliberately dark or softened hero plate.
- Golden yellow is an object highlight, not body text on a light surface.
- Use one recurring red X shape for negation across the episode.
- Check generated text letter by letter. Add exact mission-critical text in CapCut if generation
  does not preserve it.

### V2 cadence and callbacks

- First 15 seconds: 45 to 60 meaningful visual states per minute.
- 15 to 45 seconds: 36 to 45 per minute.
- Mechanisms: 28 to 34 per minute.
- Anthropology stories: 26 to 32 per minute.
- Dense evidence: 22 to 26 per minute.
- Ending: 24 to 28 per minute.
- Whole-video target: 28 to 32 per minute.
- No ordinary unchanged hold exceeds 4 seconds.
- Reuse 5 to 8 percent of plates near the ending as callbacks that change meaning.
- The final visual should echo or reuse a hook visual.

Visual rhythm does not require one unrelated generation per beat. Target 35 to 45 percent new
plates, 30 to 40 percent attached-image variants, 10 to 15 percent CapCut reframes or overlays,
5 to 10 percent callbacks, and 5 to 10 percent text or diagram updates.
