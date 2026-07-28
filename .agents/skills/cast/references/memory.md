# cast - memory

Self-improving notes for cast derivation and reference sheets. Single canonical copy.

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
   colour *from the palette*, and "at 2am so grey" is not a licence to invent one.
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

| Was written | Actually |
| --- | --- |
| 3 to 4 spikes | **exactly 2 peaks**, one tall leaning right, one shorter beside it |
| at the top-left | on the crown **slightly right of centre** |
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
