# Visual style - art DNA, the verbatim strings, tone map, frame types

Canonical source for how a TossExplains scene or character sheet looks. Read this before
writing any scene prompt, reference sheet, or thumbnail prompt. Thumbnail prompts preserve
the character identity rules here but use the separate rendering exception below.

## THE FOUR VERBATIM STRINGS (single source of truth)

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

This exception applies only to thumbnail prompts. Video scenes and character sheets keep
the flat rendering rules below.

## Art style

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

## Palette

| Color | Hex |
| --- | --- |
| Orange | `#F5820D` |
| Cobalt blue | `#2D5FBF` |
| Grass green | `#3A9E3A` |
| Golden yellow | `#F5C518` |
| Red | `#D94040` |
| Brown | `#8B5E3C` |
| Sky blue | `#6EB5E8` |
| Tan | `#C4965A` |
| White | `#FFFFFF` |

## Background tone map

### WHITE IS THE DEFAULT, AND THE DEFAULT IS THE MAJORITY

**Plain white is what a frame gets unless the moment earns something else.** The channel is a
light, clean doodle explainer. A dark frame is a deliberate exception, never a mood you drift
into because the script is set at night or is emotionally heavy.

This is not advisory. Project 2's first pass came back **40 percent blue and only 37 percent
white**, and the user rejected the whole set as dark and ugly. The accepted project 1 runs
**58 percent white**. Target that.

**Budget for a finished `image-prompts.md`:**

| Background | Share | When |
| --- | --- | --- |
| **plain white** | **55 to 75 percent** | the default, and every modern everyday scene |
| tan `#C4965A` | up to 15 percent | ancient, prehistoric, tribal |
| solid orange `#F5820D` | up to 10 percent | fire, ritual, the night gathering |
| flat green ground + blue sky | up to 10 percent | outdoor, nature, walking |
| **solid cobalt blue `#2D5FBF`** | **5 to 15 percent, hard ceiling** | **only literally inside the mind** |

**Cobalt blue is not "night", "sad", or "serious".** It means the frame is showing the inside
of someone's head: a white doodle brain, a thought loop, a memory replaying as an object. If
there is no brain, loop, or thought-object as the subject, it is not a mind frame and it is
white. A 2am bedroom is modern everyday life and gets **plain white**, with the night carried
by a small crescent moon in a window and a caption, exactly as the accepted fixture does it.

Do not use a dark ground for the lab or the experiment frames either. Older wording said
"science, lab, experiment -> solid blue"; the accepted fixture uses that zero times. Labs are
plain white with the few objects that matter.

| Moment | Background |
| --- | --- |
| Modern everyday life (phone, bed, office, sofa, street, party, shower, car) | **plain white** with only the few objects that matter |
| Science, lab, experiment, restaurant | **plain white** with the table, chair, and apparatus drawn |
| Concept, diagram, chart, icon frames | **plain white** |
| Danger, threat, social fear | stark white with red text |
| Happy, triumph, discovery, relief | bright white |
| Ancient, prehistoric, tribal | tan `#C4965A` |
| Fire, night ritual, the gathering | solid orange `#F5820D` |
| Outdoor, nature, walking | flat green `#3A9E3A` ground plus plain blue sky |
| Inside the mind, thoughts, memory | solid cobalt blue `#2D5FBF` with a white doodle brain or floating thought objects |

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
