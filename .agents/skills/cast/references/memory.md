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

- ~~**`@YOU` wears saturated cobalt `#2E77C4`, his canonical hoodie, unless the script's setting
  genuinely forbids it.** Reusing it across modern videos is correct, not lazy.~~
  **SUPERSEDED 2026-08-12 by the channel owner.** Toss gets a NEW outfit in every video, derived
  from that script's bookend scene, changing silhouette as well as colour. Carrying the cobalt
  hoodie forward is now a failed sheet. See `mascot-toss.md`, "What changes - a NEW outfit every
  single video". The half of the old rule that still stands: **never dress him in grey, slate, or
  any desaturated tone.** Recognition comes from the head, two-peak tuft, face, and build, which is
  precisely why the outfit is free to change.
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

## Project 8 (2026-08-12), the Diderot effect - a 5-entry cast and the object-versus-prop cut

`@YOU` (Toss, golden yellow crew-neck sweatshirt `#F5C518`, no hood), `@CASE` (personified
object, grass green `#3A9E3A`), `@DIDEROT` (Paris 1769, scarlet dressing gown `#D94040`),
`@HUNTER` (Ju/'hoansi, brown hide wrap `#8B5E3C` with tan hem trim), `@CAMP` (group of six, sky
blue `#6EB5E8`). Chapter palette Lilac `#B79AD9`, Coral `#D96F5F`, Olive `#8FA35A`.

### The run that established the new-outfit-every-video rule

First pass put Toss in his canonical cobalt hoodie and wrote "the default costume is correct and
is deliberately not overridden", citing the old standing rule above. **The channel owner rejected
that and made a new outfit mandatory in every video.** The rule now lives in `mascot-toss.md`
under "What changes - a NEW outfit every single video", the old memory rule is struck through
above, and `cast/SKILL.md` Step 2 says plainly that reusing the hoodie is a failed sheet.

Two things the change taught immediately:

- **A new outfit dissolved a conflict two earlier videos had to work around.** Projects 2 and 3
  both shipped a documented exception for Toss and the ancestral group sharing a blue family.
  With Toss in yellow, `@CAMP`'s sky blue is the only blue in the cast and the exception simply
  does not arise. Changing the outfit is not just variety, it frees a palette slot every time.
- **Silhouette has to change, not only colour.** A recoloured hoodie still reads as the same
  outfit, so the crew-neck exists to drop the hood. That immediately triggered the project 3
  lesson about edit prompts inheriting what they do not override: the CHANGE block names the hood
  bump, the drawstring and the collar V notch for removal, the NEGATIVE repeats all three, and
  CONSISTENCY states that the nape is flat and empty in the back and side views.

Colour choice was constrained to what four other cast members and the coral modern ground left
free. Deep blue was too near the old cobalt to read as a change, orange collided with the coral
ground, tan is a prop colour here. Golden yellow `#F5C518` was the only saturated palette colour
that survived all three tests.

Five entries, not six. Nothing carried over: fourth video, fourth setting, and the first one
whose anthropology is a named present-day people rather than a generic band.

### The cut that mattered: a signature object can be a prop instead of a cast entry

The obvious reading gives six entries, with `@PHONE` and `@CASE` both cast, because the video is
about a new object devaluing an old one and both bookend the script. That is one too many, and
two rounded rectangles with faces would have been hard to tell apart anyway.

Resolution: **the script is about the object that lost value, not the one that arrived.** The case
carries the counter-intuitive claim ("The case really did lose value"), the mid-video callback,
and the closing line. The phone causes the effect but is never the subject, so it became `@YOU`'s
signature PROP and got its lock on his sheet instead of its own entry.

Generalisable: when two objects form a cause-and-effect pair, **cast the one the narration keeps
returning to, and give the other to whoever holds it.** Ranking by moments times spread would have
scored them nearly equally and picked wrong.

### Chapter colours have to be checked against garments, not just against each other

First pass set the 1769 chapter colour to coral `#D96F5F` because the thread is warm and
period. But Diderot's gown is scarlet `#D94040` and the script will not let it be anything else,
so the video's single most important object would have sat on a ground of nearly its own hue.

Fix: the 1769 thread is grounded in lilac `#B79AD9` and coral moved to the modern thread, where
nothing warm-red is worn. **Pick the chapter colours after the garments, or at least re-check them
against every garment before writing the header.** Project 3 learned that a garment can collide
with a background; this is the same fault caught one stage earlier.

### The `@YOU`-and-`@CAMP` blue exception, now shipped three times

Same reasoning as projects 2 and 3 and written into the cast file again: a warm group vanishes into
the warm ground its own scenes sit on, so the group takes saturated sky blue and relies on never
sharing a ground with Toss. Three videos in, this is no longer an exception to justify case by
case. **Treat cool group against warm ancestral ground as the default**, and write the one-line
reason into the cast file each time so `scenes` does not re-litigate it.

### Garment alternation extended again: `shell`

`@CASE` is a phone case, so its colour line reads `case shell in grass green (#3A9E3A)` and the
Step 5 grep printed a blank until `shell` was added to the alternation in `cast/SKILL.md`. Fourth
time the alternation has been short. The blank looks identical to "no colour assigned", which is
the failure mode the grep exists to catch.

`dressing gown` needs no new word: the existing `dress` alternative matches it. Worth knowing
before adding a redundant `gown`.

### A phone case is more text-prone than it looks

Not as bad as project 3's gauge, but close enough to need enumerated negatives rather than the
standard block alone. Named individually: brand name, manufacturer logo, model number, camera
lettering, regulatory marks, barcode, price sticker, embossed wordmark, moulded lettering, plus
the usual screen suppressions for the phone visible inside the shell.

### Non-graphic kill

The insulting-the-meat scene is the video's centrepiece anthropology visual and it is about a dead
animal. `@HUNTER`'s prop is a carrying pole with an abstract wrapped bundle, explicitly negated
for animal, fur, head, legs and blood. The mockery reads from the camp's faces and gestures, which
is where the script puts it anyway.

## Project 9 (2026-08-19), advice you never take - a 4-entry cast and a token-leak trap

`@YOU` (Toss, grass green `#3A9E3A` crew-neck sweatshirt, no hood, evening-at-home), `@FRIEND`
(the modern person he advises, golden yellow `#F5C518` long-sleeve shirt, rounded chin-length
bob), `@SOLOMON` (ancient king, scarlet `#D94040` robe, white hair-and-beard on tan skin
`#D9A15B`, small gold crown), `@CAMP` (Ju/'hoansi group of six, sky blue `#6EB5E8` wraps,
charcoal `#2F3133` hair caps, campfire prop in orange `#F5820D`). Chapter palette Coral
`#D96F5F`, Lavender `#B79AD9`, Tan `#C4965A`. Four entries. Nothing carried over.

- **`@FRIEND` locked over `@SOLOMON`-style one-section figures because it bookends.** The person
  Toss advises appears in the hook, the mid "somebody you love calls you in the dark" beat, and
  the closing echo. Highest drift exposure on the cast, so it earned the lock even though it is
  visually plain.
- **`@SOLOMON` is the origin figure, cast on the project 8 Diderot precedent.** One section, but
  four contrasting beats inside it (consult, judgment, chaotic house, split kingdom) is enough
  intra-section drift to lock a single historical figure.
- **No blue exception, again, because Toss is not blue.** With Toss in green, `@CAMP` sky blue is
  the only blue on the sheet, exactly the clean shape project 8 first got by moving Toss off cobalt.
- **`sweatshirt` is caught by the garment grep via the `shirt` substring.** The alternation prints
  `shirt in ...` for a `crew-neck sweatshirt` line, which still confirms the hex. No need to extend
  the alternation for sweatshirt.

### TOKEN-LEAK TRAP: reusing a prior cast file as a structural template

Project 9's sheets were modelled on project 8's file for exact V2 shape. A derivation note read
"same judgement as project 8's `@DIDEROT`", which put a stray `@DIDEROT` into the token set. The
Step 5 `grep -oE '@[A-Z]+'` caught it. **Any `@TOKEN` in prose is indistinguishable from a cast
token to the scanner, and `check` will flag it as not in the cast table.** When referring to a
character from another project in a derivation note, write the plain name ("the Diderot figure in
project 8"), never the `@` token. Re-run the token grep after writing the header notes, not only
after the sheets.

## Project 10 (2026-08-25), third vs second - a 6-entry cast and a concept drawn as a person

`@YOU` (Toss, open zip-up track jacket in orange `#F5820D` over a charcoal `#3F3F46` tee, no
hood), `@SILVER` (red `#D94040` racerback singlet, flat swept fringe, white medal disc),
`@BRONZE` (grass green `#3A9E3A` round-neck singlet, high topknot, tan `#C4965A` medal disc),
`@RIVAL` (personified concept, fully lavender `#B79AD9` including the head, dashed contour),
`@HUNTER` (Ju/'hoansi, brown `#8B5E3C` hide wrap with tan hem trim), `@CAMP` (group of six,
sky blue `#6EB5E8` wraps, no trim). Chapter palette Dusty teal `#67A6A3`, Tan `#C4965A`,
Lavender `#B79AD9`. Six entries, at the cap. Nothing carried over.

### Two individuals, not one podium group, when the video's claim IS the comparison

The obvious compression is a single `@PODIUM` group entry covering both medalists. It is wrong.
The thesis is a difference between two people two steps apart, and a group entry cannot hold a
comparison between two of its own members. Same shape as the two friend groups in project 3.
**When the script's central claim is A versus B, both A and B are cast, and the 6-entry budget
gets planned around that from the start.**

### A personified concept can be person-shaped, and the unreality goes in the construction

`@RIVAL` is the invented life the mind scores you against. It had to be a person shape, and it
could not be Toss in ghost form, because Toss only ever plays `@YOU`. Three decisions made it work:

- **Fully filled, head included, in one flat saturated colour.** Every other character on this
  channel has a flat white head. Breaking that one rule is the instant read of "not a real person",
  and it costs nothing else.
- **Broken dashed outer contour, thin solid internal lines.** The dash carries the unreality; the
  solid internals keep the design legible.
- **A complete face, always.** The project 2 white-egg failure applies directly here. The NEGATIVE
  enumerates no faceless head, no blank head, no egg-shaped blank head, no solid black silhouette,
  and additionally no transparency, no fade, no glow, no ghost trail, no sheet-ghost shape, because
  every model's first instinct for "a person who is not there" is a translucent ghost.
- Its four states of use are the script's own arc rather than generic poses: standing beside a real
  figure, holding up the phantom medal, being pointed at by a bare charcoal arrow with no word, and
  being crossed out by the episode's recurring red X while the contour opens up.

### A cast member may carry a chapter colour, as a written exception

`@RIVAL` is lavender and lavender is a chapter colour, which normally means the figure vanishes into
its own ground. It is allowed here because @RIVAL **is** the embodiment of that chapter rather than a
figure standing inside it. The exception is written into the cast file with its rule: @RIVAL never
stands on a lavender ground, and lavender cards are reserved for the @RIVAL-absent card and diagram
beats. Same shape as the group-blue exception shipped in projects 2, 3 and 8.

### The colour cascade ran medalists-first, and that forced Toss off the obvious choice

Assigning `@SILVER` red and `@BRONZE` green first, because that pair is the thesis in two colours,
made coral `#D96F5F` unusable for Toss: coral and red `#D94040` are the same family and the two
share frames. Toss took orange `#F5820D` instead, the only remaining saturated colour that also
holds against green and lavender on a cream ground. **Assign the colours that carry the argument
before the colours that carry the protagonist.** Project 8 assigned Toss last for a similar reason
and it worked there too.

### Silhouette separation for two same-era, same-costume figures

`@SILVER` and `@BRONZE` are the same era in the same kind of kit, so per the project 2 rule they are
separated three ways and never by facial detail: flat swept fringe versus high round topknot, narrow
racerback singlet versus boxy round-neck singlet with broad shoulder panels, and a white medal disc
versus a tan one. Build is also differentiated, taller and leaner versus shorter and stockier.

### Medals are a text trap AND a trademark trap

A medal disc invites an engraved numeral, a year, and five interlocking rings. Every medal panel
across three sheets enumerates: no numeral, no 1, no 2, no 3, no year, no date, no engraved
lettering, no interlocking rings, no Olympic rings, no Olympic emblem, no national flag, no team
badge, no brand logo, no maker mark. The rings negative is doing double duty, keeping the sheet
text-free and keeping a real trademark out of the render. Athletics kit adds two more: no athlete
number bib and no sponsor mark.

### THE ACCEPTED SHEET DROPPED EVERY FOOT, and that is now the first thing to check

The user generated `YOU.png`, kept it, and asked for the other five prompts again. Reading the
accepted render against its own prompt is the cheapest calibration available and it should be done
before rewriting anything, because it says what THIS renderer actually honours.

Held, first time, no fixes needed: the two-peak tuft, the flat-white head at roughly one third of
height, solid black oval eyes with thick brows, splayed line fingers, the two-contour white-filled
tube limbs, the hood removed with no bump and no drawstring, the stand collar, the open jacket with
the charcoal tee showing, the panel layout with pale-grey dividers, and zero text anywhere.

Dropped: **every foot, in all ten full-body panels.** Each leg ends in a bare rounded tube tip. The
prompt asked for feet twice, once in the KEEP block and once inside LIMB CONSTRUCTION, and it was
still not enough. This is the same failure project 6 recorded on `@FORAGER`, which means the fix
that worked there (a sentence inside a larger block) does not hold on its own.

**The fix that replaces it: give feet their own labeled block with a shape, a size, a fail test and
a COUNT.** The count is the part that is new and the part that matters, because a model that will
not honour an adjective will often honour an arithmetic check:

> FEET, its own rule, check this LAST and check it by counting: EVERY leg in EVERY full-body panel
> ends in a small closed outlined FOOT ... about one third of the head's width ... clearly wider
> than the leg tube. A leg that simply ends in a bare rounded tube tip is a FAILED SHEET. There are
> three full-body turnaround panels and four full-body pose panels, so before finishing count
> FOURTEEN feet on the canvas.

`no missing feet` and `no leg ending in a bare tube tip` also went into every NEGATIVE. Generalise
the project 6 rule: a construction detail that has now failed twice needs its own block AND a
countable target, not just a measurement.

Also crept in: faint grey shading on the jacket and a soft gradient on the phone prop, despite
`no gradients` and `no drop shadows` already being in the NEGATIVE. Each sheet now carries a
dedicated `FLAT FILL, strictly enforced` block naming soft shading, grey gradient across a fill,
airbrushed edge, drop shadow, contact shadow, prop shading, highlight and sheen individually.
**A negative buried in a 40-item list is weaker than a three-line positive block.**

Two design changes made in the same pass, both risk reduction rather than redesign:

- **`@CAMP` went from six figures to five.** Six identical figures across three group angles plus
  four group panels is a lot of small marks; five keeps each one large enough to read.
- **`@RIVAL`'s non-white head got its own numbered instruction with a fail test.** Every other
  character on this channel has a flat-white head, so that is the renderer's prior and a lavender
  head is the single instruction most likely to be silently ignored. It is now stated as the first
  of two mandatory construction choices, repeated in CONSISTENCY, and negated as `no white head, no
  white fill anywhere on this figure`.

The generated file is `characters/YOU.png`, not `.jpeg`. Same mismatch project 5 recorded. Flagged
in the Generating section rather than renamed.

### Garment alternation extended again: `jacket` and `singlet`

Fifth and sixth time the Step 5 alternation has been short. `track jacket` and `singlet` both
printed blank, which is indistinguishable from "no colour assigned". Both added to
`cast/SKILL.md`. The alternation is now
`hoodie|shirt|parka|tunic|robe|vest|wrap|coat|dress|jacket|singlet|casing ring|shell`.

### The non-graphic kill, reused verbatim from project 8

Line 25 is the insulting-the-meat scene again, a different script reaching the same ethnography.
`@HUNTER`'s prop is a carrying pole plus an abstract wrapped bundle, negated for animal, animal
form, fur, hide pattern, head, horns, legs, hooves, tail, face, eyes, blood, red marks, meat, bone
and carcass. This is now a settled channel solution, not a per-video judgement call.

## Project 12 (2026-08-29), one stranger's comment - a 6-entry cast and a speech bubble with a face

`@YOU` (Toss, short-sleeve round-neck t-shirt in orange `#F5820D`, bare forearms, no hood),
`@COMMENT` (personified object, a speech bubble, red `#D94040`), `@NINE` (group of five, olive
`#8FA35A` knitted jumpers), `@STRANGER` (lavender `#B79AD9` zip-front top, bowl-cut fringe),
`@BRIGGS` (Jean Briggs, sky blue `#6EB5E8` fieldwork parka, round glasses, blunt-fringed bob),
`@UTKU` (group of five, brown `#8B5E3C` hide parkas with tan `#C4965A` hem and cuff trim).
Chapter palette Coral `#D96F5F`, Dusty teal `#67A6A3`, Tan `#C4965A`. Six entries, at the cap.
Nothing carried over.

### The first real named person the channel has drawn from a documented likeness

Project 11 cast Bartlett and gave him a receding hairline and a bow tie, but this is the first
run where the likeness rule was applied deliberately and written down as an identity lock rather
than as costume. Three features carry Jean Briggs at doodle scale: round glasses as two thin
circles joined by a bridge stroke, a short blunt-fringed bob, and the 1960s Arctic fieldwork
parka with the hood DOWN. The hood-down instruction is load-bearing, because a hood up erases
both of the other two features at once, so it is stated in the garment block, repeated in
CONSISTENCY, and negated as `no hood pulled up over the head, no hood covering the hair or the
glasses`. **A likeness carried by the head is only as safe as the instruction keeping headgear
off it.**

### A speech bubble is the most text-prone design the channel has ever specified

Worse than project 3's gauge and project 8's phone case, because a speech bubble does not merely
invite text, it exists to hold it. The `ABSOLUTELY NO TEXT` block for `@COMMENT` enumerates the
temptations individually rather than relying on the standard block: letters, words, quotation
marks, apostrophe, full stop, comma, question mark, exclamation mark, ellipsis, dashes,
asterisks, scribbled wavy lines standing in for handwriting, ruled lines, lorem ipsum, emoji,
smiley icon, thumbs up or down, heart, star, rating marks, notification badge, red dot with a
number, counter, timestamp, username, avatar circle. Flag this sheet first when checking the
generated set.

Two more decisions kept it a character rather than a monster: the face is the channel's ordinary
face (solid black oval eyes, thick brows, one curved mouth) on a flat red field, and the NEGATIVE
kills the obvious escalations, `no monster, no fangs, no horns, no knife, no blade, no weapon, no
flame, no lightning bolt`. The video's argument is that this is an ordinary sentence carrying
more weight than its size, so a menacing design would contradict the script.

### The hollow counterpart trick, for a group whose defining feature is silence

`@NINE`'s prop is an EMPTY white speech bubble with no face, which is the exact hollow twin of
`@COMMENT`'s filled red bubble with a face. The script's line is that being liked has never made
a sound, and a prop that is visibly the same object minus its contents says that in one shape.
The risk is the two reading as the same asset, so the difference is stated on both sheets as a
rule: red plus a face versus white plus no face, never one without the other.

### Cast the sentence, not the phone, and cast both halves of a count

Two prior rules did the work here. Project 8: when two objects form a cause-and-effect pair, cast
the one the narration keeps returning to. The phone causes the sting but the script returns to
the sentence, quoting it in the hook and rewriting it in the tease, so the phone became `@YOU`'s
PROP. Project 10: when the central claim is A versus B, both are cast, which is why `@NINE` and
`@STRANGER` are separate entries rather than one modern group.

### A group sheet may define fewer figures than the script counts

The script's number is nine and nine figures per panel do not read at doodle scale. The sheet
defines FIVE identical figures as the identity unit and says explicitly that the scene prompt
sets the count, with every added figure identical to these. Project 10 cut a group from six to
five for readability; this extends that to a case where the count is semantically load-bearing.
The fourth group panel then uses a sixth identical figure walking out of frame, so the ten-versus-
nine idea is on the sheet without ever drawing ten.

### Colour cascade, argument-first again, and the one collision it left

`@COMMENT` red and `@NINE` olive were assigned first because they are the thesis, then
`@STRANGER` lavender, then the two Arctic entries where the only pairing that truly matters is
Briggs against the camp, so she took sky blue against their brown. Toss was assigned last and
took orange `#F5820D`, which is adjacent to the coral chapter colour. **Unresolved by colour and
resolved by ground instead**, on the project 3 precedent: modern frames Toss occupies use cream
or a LIGHT coral tint, never a saturated coral fill. Written into the cast file so `scenes` does
not re-litigate it. Cobalt and Toss blue are unused by any garment, so the reserved-blue rule is
respected without an exception.

### The Step 5 garment grep never matched the current file shape, and printed blanks for every entry

`file-formats.md` specifies a BOLD file-name label before each fenced sheet, and projects 9, 10,
11 and 12 all use it, but the Step 5 grep took its range with `sed -n "/^## $t.jpeg/,..."`, a
heading form the format spec does not use. Against a current cast file that range matches nothing
and every entry prints blank, which is exactly the failure the check exists to catch and is
indistinguishable from "no colour assigned". Replaced in `SKILL.md` with an awk range between
bold labels. **The blank-means-broken warning recorded three times in this file was itself being
produced by the checker, not by the files.** Re-run it on any older cast file before trusting a
past pass.

Alternation extended again, seventh time: `jumper`, `top`, and `bubble body` were all short.
`t-shirt` needs nothing because `shirt` matches it.

## Project 13 (2026-08-29), the psychology of being poor - a 5-entry cast and an envelope instead of a bill

`@YOU` (Toss, buttoned long-sleeve work shirt in grass green `#3A9E3A`, sleeves rolled, no
hood), `@BILL` (personified object, a sealed envelope, red `#D94040`), `@FARMER` (present-day
Tamil Nadu sugarcane farmer, golden yellow `#F5C518` short-sleeve shirt, tan `#C4965A` waist
wrap, white shoulder cloth), `@FORAGER` (illustrative mobile forager, brown `#8B5E3C`
single-shoulder hide wrap with tan trim), `@BAND` (group of five, sky blue `#6EB5E8` untrimmed
two-shoulder wraps). Chapter palette Coral `#D96F5F`, Dusty teal `#67A6A3`, Tan `#C4965A`. Five
entries. Nothing carried over.

### Draw the container, not the document

`@BILL` is the unpaid number, and the obvious design is a printed statement. That is close to
unrenderable under the no-text rule: a statement is a blank rectangle without its printed lines,
so the model has to invent lettering to make the object legible, and it will. **A SEALED
ENVELOPE is the same idea with an inherently textless silhouette**: a rectangle plus a triangular
flap plus a diagonal seam reads as post from across the room with zero glyphs. The script also
hands it over directly, "the letter you have not opened". Generalisable: **when an object's
meaning normally comes from words printed on it, cast its container or its closed state
instead.** The gauge in project 3 and the phone case in project 8 were solved by enumerating
negatives; this one was solved by changing the object.

It still needs the enumerated block. Named individually because an envelope exists to carry
writing: address, address block, ruled address lines, window panel, stamp, postmark, franking
mark, barcode, QR code, account number, reference number, currency symbols, amounts, digits,
date, due date, overdue stamp, urgent or final-notice mark, letterhead, tick boxes, signature
line, columns, table, and squiggles standing in for handwriting. Check this sheet first.

Kept ordinary rather than menacing, on the project 12 precedent: the face is the channel's
normal face on a flat red field, and the NEGATIVE kills fangs, horns, flames, lightning and
cracks. The script's argument is that a dull small object carries more weight than its size, so
a threatening design would contradict it.

### The recurring motif was considered for a cast slot and correctly refused

The tunnel is the script's most repeated image and spans every pillar, which by moments-times-
spread is the strongest cast candidate on the page. It is still not a cast entry, because it is
a framing device rather than a character or a handheld object: there is nothing to turn around,
no face to give it, and no hands to put it in. **Moments times spread ranks candidates that are
already depictable as a character. It does not promote a composition into one.** It went to
`scenes` as a cobalt `#2D5FBF` mind interior with a hard vignette, written into the cast file so
the next stage inherits the decision.

That also freed the chapter budget. Cobalt is a base episode colour, not one of the three
chapter colours, so the video's most-used visual thread costs nothing from the three-colour
allowance and coral, dusty teal and tan could each go to a world.

### The colour cascade ran argument-first again, and it forced Toss into the tunnel test

`@BILL` red first (verdict and threat, and it is the antagonist), then `@FARMER` yellow, then
the settled ancestral pair of brown individual against sky blue group. Toss last. The new
constraint this script added: **he stands inside cobalt mind-interior frames repeatedly**, so
the costume colour had to survive cobalt as well as cream and a light coral tint. Orange failed
on coral, the same collision projects 3 and 12 both hit. Grass green `#3A9E3A` was the only free
saturated palette colour that held against all three. Project 9 also dressed Toss in green, which
is allowed: the rule is a new outfit per video and a colour no other member of THIS cast wears,
and the silhouette here is a buttoned collared work shirt rather than a crew-neck sweatshirt.

### Culture-neutral is the honest answer when a script cites three ethnographies and depicts none

Sahlins, Woodburn and Peterson worked with different peoples on different continents, and the
script names none of them on screen, describing only "a group of a few dozen people" that "moves
camp several times a year". So `@FORAGER` and `@BAND` are an illustrative small mobile camp and
are explicitly not dressed as any identifiable living people, with no face paint, feathers, bone
ornaments or headdress. The project 2 rule was "build for the culture the script actually depicts
rather than the one it cites"; **when the script depicts none, build none, and say so in the file
so a later stage does not attach an ethnonym.**

### A present-day non-Western character keeps the standard flat white head

`@FARMER` is a living person in a named 2013 study, not an ancestral figure, so he takes the
channel's default flat white head like every other modern character and is separated by garment,
hair cap, white shoulder cloth and props. Tan skin `#D9A15B` stays on the ancestral pair, where
it has been the convention since project 2. **Do not let skin tone become the thing that tells a
modern Indian farmer apart from the modern protagonist**; the distinguishability rule already
demands garment colour plus a silhouette difference, and here that is the shoulder cloth.

He also needed an explicit anti-default paragraph, because "farmer" is the exact word that pulls
the banned early-Neolithic figure: no hoe, no sickle, no scythe, no wheat, no straw or conical
hat, no sackcloth tunic, no medieval setting. His cane stalk is script-derived (the script says
sugarcane) and is not the banned stalk of wheat, which is worth stating so a later reader does
not "correct" it.

### The Step 5 garment grep was case-sensitive and every declaration was shouted

First pass wrote the garment word in caps for emphasis inside the prompt, `work SHIRT in
saturated grass green (#3A9E3A)`, and the grep is `grep -oE` with a lowercase alternation, so
all five entries printed blank. Same blank-means-broken failure the file has now recorded five
times, from a fifth distinct cause. Two fixes applied: the alternation in `SKILL.md` is now
`grep -oiE`, and the declaration lines are lowercase. **Do not shout the garment word.**

Alternation extended again, eighth time: `envelope body`. Plain `envelope` was not used, because
the sheet's phrase is "the envelope body is one simple filled rectangle in ...".

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

## Project 6 (2026-08-03) - @FORAGER regenerated, and the eight ways a sheet drifts

Cast is `@YOU` (Toss, canonical cobalt hoodie), `@PHONE` (personified object, dusty teal
`#67A6A3`), `@FORAGER` (illustrative small-camp adult, brown `#8B5E3C`), `@HADZA` (present-day
Tanzanian research group, coral `#D96F5F`). First V2 cast in the repo.

The user rejected the generated `characters/FORAGER.jpeg` and asked for the prompt again. Comparing
the render to the prompt, every fault was something the prompt had asked for in prose but not
enforced, so the model quietly chose the easier drawing:

| Rendered                                     | Prompt had said                        | What fixed it                                                                   |
| -------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------- |
| single-stroke wire arms and legs             | two-contour white-filled tubes         | own `LIMB CONSTRUCTION` block, named the second priority after the head, with a width (one eighth of head diameter) and a fail test ("if it reads as a wire the sheet is wrong") |
| legs ending in bare stroke tips              | small bare outlined line feet          | "in every single panel", plus "a figure missing one or both feet is a failed sheet" |
| head about a quarter of the height           | roughly one third                      | a `PROPORTION LOCK` block placed FIRST, in head-heights: 3 total, torso 1, legs 1.25, arms 1 |
| shaggy hair mass, fully black head from back | one compact closed crown shape         | "covers only the top third of the head circle", and the back view keeps the white head visible |
| eyes with white highlights                   | solid black ovals                      | "no highlight, no catchlight, no pupil ring, no iris, no outline ring"           |
| hands rubbing an eye and touching a chin in the expression row | expressions change brows and mouth only | "head and neck only in this row, no hands, fingers, arms, shoulders, props, sweat drops, or tears" |
| dirt speckles, grass tufts, a drawn trail    | no scenery                             | negated per item on the POSE block itself, not only in `NEGATIVE`               |
| tall angular stone slab                      | flat chipped oval                       | "wider than it is tall", "no upright standing stone, no faceted knapping flakes" |

Three transferable rules:

- **A construction detail that keeps coming back wrong needs its own labeled block with a
  measurement and a fail test.** Buried inside `BODY CONSTRUCTION`, the limb sentence lost to the
  model's stickman prior three panels in. As its own block with a number, it held.
- **Put the negative where the temptation is.** "No scenery" in `NEGATIVE` did not stop ground
  speckles under a crouching figure; naming them inside the pose block did.
- **Referring to `brand/MASCOT.jpeg` in prose does nothing for a non-`@YOU` sheet.** The mascot is
  not attached for those generations, so "matching the limbs in brand/MASCOT.jpeg" is a note to a
  human. Describe the construction in full or attach nothing.

Two Step 5 grep notes, both false alarms that cost a pass each:

- `never a mitten` slips the mitten grep, because the alternation only excludes `never mittens`
  with no article between. Write `never mittens, blobs, or nubs`.
- The garment grep needs garment-word-then-hex. `brown (#8B5E3C) work wrap` prints blank, which
  reads as "no colour assigned". Write `work wrap in brown (#8B5E3C)`.

`MASCOT.jpeg` settles one open contradiction: `mascot-toss.md` says arms and legs are "thin single
black lines", but the image shows bare limbs as **narrow white-filled tubes with two contours** and
small outlined feet. Only the hoodie sleeves read as solid. Every bare-limbed cast member follows
the image, not the sentence.

## Project 13 (2026-09-01), @BILL rejected as an envelope and rebuilt as a bill

The sheet named the object `@BILL` and then drew a sealed envelope, on the reasoning that an
envelope has an inherently textless silhouette while a printed statement is a rectangle that means
nothing without ruled lines. The owner rejected the generated sheet with "it looks like an envelope
instead of a bill". The reasoning was sound and the conclusion was still wrong.

- **A personified object has to read as the thing the token names, not as its container.** The
  textless-silhouette argument is a real constraint, but it was allowed to pick the object. When a
  textless design and the named object disagree, keep the object and find a different textless
  route to it.
- **The route that works is silhouette markers, not print.** Three of them carried "bill" with zero
  glyphs: portrait proportion, about 3 wide to 4 tall, which is the one shape an envelope can never
  be; a torn zigzag bottom edge, a sheet off a pad, and the only broken edge anywhere in the cast;
  a folded-down top corner plus a deliberately EMPTY white header band, which is where a real bill
  puts its letterhead. An empty letterhead band says "document" louder than filling it would.
- **When a design is replaced, put the old design in the NEGATIVE, first and by name.** The old
  sheet is the drift attractor: the model has already been rewarded for drawing an envelope here.
  The new NEGATIVE opens with no envelope, no flap, no triangular flap, no diagonal seam, no
  window panel, no stamp, no landscape rectangle, no shape wider than it is tall.
- **Check the SHAPE before the text on the reprint.** The generating checklist now says so
  explicitly for this sheet: a returned image that is wider than tall is the old design, and no
  amount of text checking matters after that.
- **Replacing a personified object is never a one-file edit.** `@BILL` was described physically in
  `image-prompts.md` (about 20 places), `visual-plan.md` (3), and `thumbnail-prompts.md` (12),
  because `scenes` and `thumbnail` both write the object's appearance into prose rather than
  relying on the token alone. Grep the object's noun across every prompt file, not just the token.
  Watch for a same-noun different-object collision while doing it: this project also has a "pay
  envelope" wage packet in four scene prompts, which is a separate object and correctly stayed an
  envelope.
- The `@YOU` sheet also had to change, because his pose one rests a hand on a stack of these
  objects. A cast member holding another cast member's object inherits that object's redesign.
- Step 5's garment grep needed `bill body` added to its alternation, exactly the extension the
  skill tells you to make. Written as "The bill body is one simple filled rectangle in saturated
  red (#D94040)" so the garment-word-then-hex pattern matches.

## Project 14 (2026-09-04), the psychology of being ugly - a 6-entry cast and casting the mechanism itself

`@YOU` (Toss, buttoned short-sleeve pyjama top in lavender `#B79AD9`, notched lapel collar,
chest patch pocket, no hood), `@SCORER` (personified object, a handheld rating paddle, red
`#D94040`), `@WEARER` (the 2000 spotlight-effect subject, golden yellow `#F5C518` t-shirt with a
doodle face printed on it, high rounded coiled hair dome), `@PEERS` (group of five, present-day,
grass green `#3A9E3A` crew-neck tops, flat level fringe, shoes), `@ANCESTOR` (illustrative
prehistoric woman, brown `#8B5E3C` belted hide wrap, long single plait), `@BAND` (group of five,
same era, sky blue `#6EB5E8` untrimmed wraps, plain high cap, bare feet). Chapter palette Dusty
teal `#67A6A3`, Tan `#C4965A`, Coral `#D96F5F`. Six entries, at the cap. Nothing carried over.

### The script's central mechanism was the strongest cast candidate, ahead of every person in it

The word "scorer" appears nine times across all five sections. Nothing else in the script came
close on moments times spread, including the mirror, and it is the first time the top-ranked
candidate has been the video's abstract mechanism rather than a person or a handled object.
**When a script names its mechanism repeatedly and consistently, that name is a cast entry**,
because a mechanism drawn three different ways splits one argument into three unrelated claims.
The script itself calls it "A tool built to rank a few hundred known faces", which settled
personified object over the person-shaped concept route project 10 used.

### A pose can carry a sentence that no silhouette can

The pillar turn is "It was built to point outward. At other people. For almost the entire span
of human existence, it never once got a clear look at the face it belonged to." A card on a
rigid straight handle physically cannot turn back on its own holder, so state of use three draws
that sentence directly: the paddle facing a row of three small plain heads while a fourth stands
behind it unlooked-at. **Pick the object whose mechanics encode the claim**, then say in the
sheet that the handle never bends, hinges or telescopes, because a model handed a handle will
articulate it.

### Solve a number trap by removing the number, not by substituting for it

A rating paddle exists for no purpose except to show a number, which made this the most
text-prone design on the cast. Project 13's bill was solved by keeping the object and finding a
textless route to it. Here the route is that there is no rating on it at all: the verdict reads
from the paddle's pose, and the bare red field is the script's own point, "So how much of your
verdict is a measurement, and how much is just repetition?" **When the thematic answer and the
no-text constraint agree, take the constraint literally rather than looking for a substitute
marking.** The NO TEXT block still enumerates every numeral temptation individually, plus tick,
cross, star, dot rating, bar, meter, dial, gauge, needle, thumbs, heart and letter grade.

Landscape proportion, 5 wide to 4 tall, is the load-bearing shape marker on the project 13
precedent. It keeps the card out of document, sign, sheet and phone territory, and a card taller
than wide is called a failed sheet in the prompt.

### A real person printed on a garment becomes a doodle face inside a circle

The script's shirt is "printed with an outdated singer's face", which is a likeness problem and
not only a text problem. The print is ONE plain doodle face, the channel's own eyes, brows and
mouth inside a thin circle on a flat white field, drawn clearly smaller than his own head. Two
rules make it survive: **the printed face holds a fixed neutral expression in every panel and
never mirrors his own**, because a model given two faces on one figure will sync them, and the
back view has no print at all. Enumerated negatives cover band name, artist name, song title,
tour dates, arc of lettering around the circle, and the record label and copyright marks.

### Two five-figure groups in one cast need a stated three-way separation on both sheets

First time this cast shape has appeared: a present-day group and a same-era ancestral group, five
identical figures each. They are separated by head fill, hair shape and footwear, and both sheets
carry the same paragraph naming the other group's markers as forbidden. White head plus low flat
level fringe plus green crew-neck plus shoes, against tan head plus plain high rounded cap plus
hide wrap plus bare feet. **State the pairing on both sheets, not once**, on the project 12
precedent for the two speech bubbles. Each group's NEGATIVE also names the other's markers.

### The ancestral figure is a woman, and that was derived rather than defaulted

The pillar's emotional centre is Hrdy's line that "a woman's standing among the other women ran
partly on exactly this kind of comparison". Her markers are a long single plait and a corded
belt, deliberately re-derived rather than the single-shoulder trimmed wrap projects 8, 10 and 13
used. Gender reads from hair and garment only, and the sheet says so explicitly: no chest shape,
no waist taper, no hips, no anatomy under the wrap, because the channel's construction rules
forbid all of it and a model told "a woman" will otherwise add it.

"Prehistoric woman" pulls two cliches at once, so the anti-default paragraph names both: the
banned early-Neolithic farmer set (hoe, sickle, wheat, sackcloth tunic, straw hat, village) and
the caveman set (fur pelt, club, spear, bone ornament, feathers, headdress, face paint, cave).
Project 13 only needed the first.

### The empty prop, when the video's point is that you cannot see yourself

Both of `@ANCESTOR`'s props are deliberately blank: the polished stone sliver and the oval of
still water show nothing reflected, no face, no head shape, no shine marks. The temptation is
enormous and it would leak an identity into a prop panel. `no reflected face` leads the NEGATIVE
and the generating checklist says to check that sheet for a reflection. **A prop that exists to
fail at its job has to say so, twice.**

### The mirror was refused as a cast entry and handed to the continuity ledger

Second-highest spread in the script and still not a character: it is a surface and a relationship,
there is nothing to turn around, and giving it a face contradicts the mechanism, because the face
in a mirror is supposed to be yours. It also appears as five different surfaces, a bathroom
mirror, a shop window, a lift door, a front camera and a laptop preview, which is a
`visual-plan.md` continuity-ledger job. Same shape as the tunnel refusal on project 13, with one
addition: **the cast file writes the canonical locked description anyway** (upright rounded
rectangle, charcoal outline, flat cream glass field, one thin diagonal highlight, no ornament), so
`scenes` inherits a design without a sheet. The scroll of strangers was refused the same way and
sent to the CARD register as a grid of small heads.

### The colour cascade forced a chapter colour swap, then Toss into lavender

Argument first: red for the scorer, green for the peers. Coral was rejected for the peers because
coral and red share frames constantly; olive was rejected because it is too near the light
dusty-teal study card their frames sit on. Then the ancestral pair took the settled brown and sky
blue. Toss last, and every obvious choice failed: orange collides with coral, green collides with
the peers, dusty teal is a chapter colour, cobalt and Toss blue are reserved and read as the old
hoodie. **Lavender was available only because the chapter palette had been re-cut earlier in the
same pass**: lavender first looked like the natural chapter colour for the perception thread, and
coral was moved into that slot instead, which freed lavender for the one garment that had run out
of options. Project 8's lesson was to re-check chapter colours against garments; this extends it
to trading a chapter colour away when the protagonist has nothing left.

The residual collision is lavender against a cobalt mind interior, one hue family separated only
by value. Resolved by ground rule rather than by colour, on the project 3 and 12 precedent: he
either stands outside the interior looking in, or keeps a cream pool around him with cobalt as the
outer field.

Also new: the episode's recurring red X cannot be drawn on `@SCORER`, whose body is that same red.
The negation of the scorer is its face-down fourth state of use instead. **Check the episode's
negation mark against the antagonist's garment colour**, the same test as garment against ground.

### Two Step 5 failures, both already recorded here from different causes

- **`@ROOM` leaked as a token from a derivation note explaining why the token is `@PEERS`.**
  Exactly the project 9 trap, from a new direction: the leak came from justifying a name rather
  than from citing another project. Any `@TOKEN` in prose is a cast token to the scanner, so the
  rejected name has to be written plain. Rewritten as "deliberately not the script's own word".
- **`@ANCESTOR`'s garment grep printed her skin tone.** The CHARACTER preamble said "the hair
  silhouette and the belted wrap. Head is a large circle with a flat TAN skin fill (#D9A15B)",
  so the alternation matched `wrap` and ran to the first hex, which was the head. Sixth distinct
  cause of a misleading garment-grep line. The project 3 rule is "declare the garment first"; the
  wider form is **do not let the garment word appear anywhere before its declaration**, even in a
  summary phrase. Fixed by changing the preamble to "the corded belt".

Alternation extended again, ninth time: `card body`.
