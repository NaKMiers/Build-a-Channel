# cast - memory

Self-improving notes for cast derivation and reference sheets. Single canonical copy.

## 2026-08-03 - V2 sheets stay functional

Warm Editorial Storybook depth belongs in scene prompts, not in identity sheets. V2 reference
sheets stay flat, pure white, texture-free, and evenly lit. They add line-weight hierarchy,
story-specific silhouette and prop decisions, and chapter-palette compatibility only. This keeps
the sheet useful as a stable reference while allowing scenes to use CLEAN, LAYERED, or
ATMOSPHERIC rendering.

## Project 1's cast, as a shape reference not a template

`@YOU` (Toss in a modern hoodie), `@FRIEND`, `@CROWD` (group entry, the anonymous forty),
`@BAND` (group entry, the forager fire circle), `@OUTCAST`. Five entries, two of them groups.

Note what made it correct: the anthropology section is genuinely set in a forager band, so
`@BAND` and `@OUTCAST` are prehistoric. **If a future script's anthropology is a monastery or
a 1960s lab, those entries are a monk or a lab subject instead.** Do not carry this cast
forward.

## Project 2's cast (2026-07-28), and the two judgement calls it forced

`@YOU` (Toss, slate grey t-shirt, the 2am at-home look), `@OTHER` (the modern antagonist),
`@JURY` (group, the imaginary audience), `@ANCESTOR` (Arctic forager stand-in), `@KIN` (the
brother-in-law), `@BAND` (group, the band of thirty and the community that laughs). Six entries,
at the cap, two of them groups.

Nothing carried over from project 1. Different mechanism, different era, different cast.

### Judgement call 1: the ancestral stand-in cannot be Toss

`mascot-toss.md` says Toss only ever plays `@YOU`, and `scenes` rule 11 says the other-era frames
belong to a different character. But this script's anthropology section addresses the viewer
directly: "Now have an argument in there. With your brother-in-law." That reads as if Toss should
be in the ancestral scene, and he must not be. **The fix is a named ancestral counterpart**, here
`@ANCESTOR`, who plays the viewer's role in that era. Expect this whenever the script says "picture
yourself" inside the anthropology section, which is often.

### Judgement call 2: a script with two ancestral cultures, and a 6-entry cap

This script names two peoples: Gluckman's African societies for the peace in the feud, and
Hoebel's Greenlandic Inuit for the song duels. Designing both would need 8 entries.

Resolution: **build for the culture the script actually depicts on screen, not the one it only
cites in narration.** The song duel is described in detail over three paragraphs and is the
video's centrepiece anthropology visual, so the whole ancestral cast is Arctic. Gluckman appears
in narration only and is never drawn. The earlier band-of-thirty passage is culture-neutral
("a debt of meat", "the same fire", "a share of the kill"), so it absorbs the Arctic setting
without contradiction. The reasoning is written into the cast file so `scenes` does not
re-litigate it.

### Group entries need faces, and the reason is in the thumbnail memory

`@JURY` is the imaginary audience the script calls "a vague jury with no faces at all". That is a
description of a feeling, **not a drawing instruction.** Asking an image model for featureless or
blank heads produced a field of giant white eggs in the thumbnail A/B round. Both group sheets
therefore specify identical simple faces and get "no faceless or blank heads, no solid black
silhouette figures" in their NEGATIVE block. Anonymity comes from every member being identical to
every other, never from removing features.

### COLOUR: the mistake that got caught in generation, and the rule that prevents it

First pass put `@YOU` in slate grey `#6B7076` reasoning "it is 2am, he is at home". The user
generated the sheets and reported `@YOU` and `@JURY` as pale and unattractive while `@OTHER`
looked good. Both faults were real:

1. **`#6B7076` is not in the channel palette.** The palette is `#2D5FBF #3A9E3A #6EB5E8
#8B5E3C #C4965A #D94040 #F5820D #F5C518 #FFFFFF`. `mascot-toss.md` allows a free costume
   colour _from the palette_, and "at 2am so grey" is not a licence to invent one.
2. **`#6B7076` is the exact colour project 1 gives the anonymous `@CROWD`'s trousers.** The
   protagonist was wearing crowd grey, so he could not separate from the group he exists to
   stand against. `@OTHER` only looked better because red `#D94040` was the sole saturated
   garment on any sheet.

Then the first fix introduced a second collision: recolouring `@JURY` to tan made the modern
imaginary jury share `@KIN`'s exact Arctic hide palette, in a video whose whole point is
modern versus ancestral. Caught by a grep, not by eye.

**Run this before finishing any cast file:**

```bash
F=projects/<n>-*/prompts/character-prompts.md
# every garment colour must be distinct
for t in $(grep -oE '^\| @[A-Z]+' "$F" | tr -d '| @'); do
  printf '%-10s %s\n' "@$t" "$(sed -n "/^## $t.jpeg/,/^## [A-Z]*.jpeg/p" "$F" \
    | grep -oE '(hoodie|shirt|parka|tunic)[^,]*\(#[0-9A-F]{6}\)' | head -1)"
done
# nothing off palette
grep -oE '#[0-9A-F]{6}' "$F" | sort -u
```

A third sheet had the same fault and I missed it on the first fix: `@BAND` was "muted grey brown
`#7A6A55`", also off-palette, also desaturated. The user asked for it to be redone. **When one
colour fault is found, audit all six sheets in the same pass** rather than fixing only the ones
named. Now every sheet carries `no pale washed-out fills` in its NEGATIVE block.

`@BAND` is now saturated sky blue `#6EB5E8`, the only palette colour no other character wears.
It also buys the warm-against-cool contrast with the orange fire they gather around, which is
the pairing that made the accepted thumbnail work.

Standing rules that came out of it:

- **`@YOU` wears saturated cobalt `#2E77C4`, his canonical hoodie, unless the script's setting
  genuinely forbids it.** Reusing it across modern videos is correct, not lazy: it is how a
  returning viewer recognises Toss. Never dress him in grey, slate, or any desaturated tone.
- **No two cast members share a garment colour**, and the modern cast and the ancestral cast
  must not share a colour family at all. Modern here is blue, red, green over charcoal
  `#3F3F46`. Ancestral is brown, tan, grey-brown over hide `#5C4030` with tan skin `#D9A15B`.
- **Anonymous does not mean pale.** A group entry stays anonymous by every member being
  identical, at full saturation. Add `no pale washed-out fills, no muted palette` to its
  NEGATIVE block alongside the existing no-faceless rules.
- Grass green `#3A9E3A` was the only saturated palette colour unclaimed in project 2. Check
  what is free before assigning, rather than reaching for a neutral.

### THE HAIR IS TWO PEAKS. The rule file was wrong for the first two videos.

`mascot-toss.md` said "a tuft of 3 to 4 short spikes at the top-left of the head, drawn as open
spiky strokes". All three parts of that were wrong, confirmed by cropping `brand/MASCOT.jpeg`
and viewing the head at magnification:

| Was written        | Actually                                                                |
| ------------------ | ----------------------------------------------------------------------- |
| 3 to 4 spikes      | **exactly 2 peaks**, one tall leaning right, one shorter beside it      |
| at the top-left    | on the crown **slightly right of centre**                               |
| open spiky strokes | **one closed outlined shape** with the same flat white fill as the head |

The user caught this from a generated sheet. It had propagated into project 1's and project 2's
cast files. **Verify a mascot detail against the image before writing it into a prompt.** The
crop is cheap:

```python
from PIL import Image
im = Image.open("brand/MASCOT.jpeg"); w,h = im.size
im.crop((int(w*0.60), 0, int(w*0.76), int(h*0.26))).resize((900,900)).save("/tmp/head.png")
```

### The `@YOU` sheet is an EDIT prompt, not a description prompt

The user's second correction, and it is the more important one. Every other cast member is a new
character, so their sheet describes a person from scratch. **Toss already exists.** Describing
him from scratch and hoping the model rebuilds him identically is precisely how two peaks became
four spikes.

The `YOU` block is now structured as an image edit: lead with "the attached image is the
character, reproduce it exactly", then a KEEP block listing what must not move, then a CHANGE
block with only what the script justifies, then the new expressions and poses. **No BODY
CONSTRUCTION paragraph for `@YOU`** - it competes with the attached reference, and when a
description and an image disagree the model blends them. State explicitly that the image wins.

Full shape is in `.agents/rules/mascot-toss.md` under "The `@YOU` sheet is an EDIT prompt".

### Distinguishing three same-era figures

`@ANCESTOR`, `@KIN`, and `@BAND` share one skin tone and one garment type, so they are separated by
silhouette and by trim, never by facial detail: flat level fringe with tan trim, shaggy mane plus
beard with reversed dark trim, and a plain short cap with no trim at all. The no-trim parka is what
marks an ordinary band member apart from the two named ancestral characters.

## Project 3's cast (2026-07-29), and what it added

`@YOU` (Toss, canonical cobalt hoodie, modern), `@WORK` (group, red, the work friends), `@GYM`
(group, grass green, the gym people), `@METER` (personified object, the sociometer as a gauge),
`@FORAGER` (Kalahari Ju/'hoansi forager, brown hide wrap with tan hem trim), `@CAMP` (group, sky
blue, the camp of thirty). Six entries, three of them groups, one an object.

Nothing carried over. Third video, third setting: forager band, Arctic band, now a Kalahari
camp, and the derivation gave a different figure each time.

### Three groups in one cast is correct when the script is about audiences

This script's subject is literally having six or seven separate audiences, and the party where
two of them collide is the opening image and the closing image. One group entry could not carry
a collision, so `@WORK` and `@GYM` are both cast. They are the two the script names most often
(lines 27, 35, 79, 97), and line 97 gives each of them a specific instruction, so they were
already the two doing the work.

### A recurring abstraction beats a vivid one-off for a cast slot

The cut was between `@METER` and a `@STRANGER` for Tory Higgins's ambiguous person. The stranger
is more vivid and gets four paragraphs, but they are four **contiguous** paragraphs, so drift is
bounded and `scenes` can carry it with generic figures. The sociometer recurs at lines 11, 13, 15,
83 and 99, spanning the entire video, which is the highest drift exposure on the whole cast. **Rank
candidates by moments times spread, not by vividness.** A signature object threaded through every
act needs the lock more than a memorable figure confined to one section.

### The gauge is the most text-prone sheet the channel has produced

A real gauge has numerals printed on its face and every model will supply them. The dial carries
plain tick marks and nothing else, and the `ABSOLUTELY NO TEXT` block names the specific
temptations: no numerals, no scale values, no min or max labels, no percent sign, no degree marks,
no brand name on the casing. **Any object with a readable face needs its own enumerated text
negatives**, not just the standard block. Flag it in the Generating section too, so the human
checks that sheet first.

### Warm ancestral backgrounds rule out warm ancestral garments

Same collision as project 2 and the same resolution. Every camp scene sits on tan `#C4965A` or
solid orange `#F5820D`, so a tan or brown **group** disappears into its own background. `@CAMP` is
saturated sky blue `#6EB5E8` for the cool-against-warm read, and `@FORAGER` keeps brown
`#8B5E3C` so the ancestral colour family still reads in a split frame. This means `@YOU` and
`@CAMP` are both blue, which contradicts the "modern and ancestral never share a colour family"
rule below. It is a deliberate exception: they never share a background, Toss is on white and the
camp is on tan or orange. Project 2 shipped the same exception for the same reason. **Write the
reasoning into the cast file so `scenes` does not re-litigate it.**

### The two verification greps were both wrong, and both said "pass"

- **`grep -c mitten` counts the fix as the fault.** Every NEGATIVE block correctly says `no mitten
hands`, so the old grep read 11 on project 2 and 8 on project 1's cast file, both of which are
  correct files. The corrected form strips occurrences preceded by no, never, or not:
  `grep -oiE '(no|never|not) +mittens?|mittens?' "$F" | grep -civE '^(no|never|not) '`. Only
  project 1's `image-prompts.md` genuinely fails, at 30. Fixed in both `cast` and `check`.
- **The garment-colour grep only knew hoodie, shirt, parka, tunic, robe.** Project 3 introduced a
  vest, a wrap, and a casing ring, so three of six entries printed an empty line, which reads as
  "no colour assigned" rather than "the grep cannot see this word". A blank is indistinguishable
  from a pass, which is how two characters would come to share a colour. Extend the alternation
  whenever a cast introduces a new garment word.

Also: `grep -ciE 'muted|desaturated|washed.out'` is **expected** to equal the cast size in a
finished file, because every NEGATIVE block carries `no pale washed-out fills` and `no muted
palette`. Zero would mean the negatives are missing. Read where the hits sit.

### Costuming Toss off cobalt, when the user asks for it

The user asked for @YOU's clothes to match the topic, so project 3 puts him in a saturated orange
`#F5820D` short-sleeve camp-collar going-out shirt over his usual charcoal shorts, dressed for the
party that bookends the script. Three things this run established:

- **Pick the costume from the script's bookend scene**, not from an average of its settings. The
  sheet locks ONE outfit, so the right one is whichever room carries the video's opening and
  closing image.
- **An edit prompt inherits everything it does not override, so removing a feature needs its own
  instruction.** `brand/MASCOT.jpeg` has a hood. Simply describing a shirt leaves the model free to
  draw a hooded shirt, so the CHANGE block says REMOVE THE HOOD COMPLETELY and names the hood bump,
  the drawstring and the V notch, and the NEGATIVE repeats them. The same applies to any KEEP-block
  feature being dropped rather than replaced.
- **Check what the colour is free of, not just who else wears it.** Orange was the only free
  saturated palette colour, but solid orange `#F5820D` is also the tone map's fire background. A
  garment can collide with a background as easily as with another character. Noted in the cast file
  so `scenes` keeps @YOU off warm grounds.

Write a one-line revert into the sheet's prose when overriding a standing design rule. The costume
touches only the CHANGE, CONSISTENCY and NEGATIVE blocks, so saying that plainly is cheaper than
re-deriving it later.

**Watch the garment grep when a sheet mentions two garments.** The first pass opened with "replace
the hoodie with a plain short-sleeve shirt in orange", and the Step 5 grep reported
`@YOU hoodie with a plain short-sleeve going-out shirt in saturated orange (#F5820D)`, because the
alternation matches the first garment word on the line. The hex was right, the label was misleading.
Declare the garment first and mention the one being replaced afterwards.

### Do not paraphrase the opening line for a non-person entry

First pass opened `@METER` with "...for ONE simple hand-drawn 2D doodle cartoon **object with a
face**", which broke the verbatim REFERENCE SHEET OPENING LINE and dropped the count to 4 of 5.
Caught by the grep, not by eye. The verbatim line goes first unchanged, then a following sentence
says it is a personified object with no body, arms or legs.

## Resolved conflict: hand shape

The retired prompts contradicted each other. Splayed line fingers win, `mitten` is banned. The
full reasoning is in `.agents/rules/mascot-toss.md`. Project 1's `image-prompts.md` still says
"mitten hands" throughout because it predates the resolution, so `check` reports that as a
grandfathered INFO.

## Lessons

- The Era / setting column in the cast table is not decoration. It is the forcing function: if
  you cannot cite the script line that puts a character in that time and place, the character
  does not belong.
- Group entries are one cast entry, not one per figure. `@CROWD` and `@BAND` each cover a whole
  formation and get a group sheet showing the formation, plus turned inward, turned away, and
  one figure excluded.
