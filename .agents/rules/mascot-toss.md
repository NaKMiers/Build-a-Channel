# Toss identity lock + the character reference sheet template

Canonical source for the channel mascot and for how every cast reference sheet is
built. Read this before running the `cast` skill. Ported from the retired
`prompts/character-prompt.md` plus the character consistency system in
`prompts/master-prompt.md`.

## Why the cast system exists

The channel's one hard visual failure mode is **character drift**: the same person
looking slightly different in every frame, so the video reads as if five people drew
it. The fix is a named cast, defined once per video, before any scene image exists.

- Every video defines a small cast, and each member gets a ONE-WORD ALL-CAPS name and
  a reference sheet image saved as `characters/NAME.jpeg`.
- From then on, every image prompt refers to a character as `@NAME` and never
  re-describes them. The sheet carries the design. The prompt carries only the
  action, expression, posture, and framing.
- No `@` token may ever be used unless it exists in that video's cast table.

## HAND SHAPE - resolved conflict, read this

The retired prompt files contradicted each other. `master-prompt.md` line 62 and
`character-prompt.md` both said **small splayed line fingers**, while
`master-prompt.md` line 239 said **round mitten shapes with no separate fingers**,
and the generated `projects/1-*/prompts/image-prompts.md` says "mitten hands"
throughout.

**Splayed line fingers win.** Three reasons: `MASCOT.jpeg` shows splayed fingers, two
of the three written sources say splayed, and `character-prompt.md` lists "no mitten
hands" in its NEGATIVE block. Project 1's prompts are wrong on this point and were
generated before the conflict was noticed.

Correct: **three or four short strokes fanning off the end of the arm line.** Not
mittens, not blobs, not nubs, not detailed anatomical hands.

## @YOU is always TOSS

TossExplains has one permanent character, Toss, and he is the viewer stand-in in every
single video. He is never re-derived from the script, never redesigned, and never
swapped for a different stand-in. Every video, `@YOU` = Toss.

The canonical sheet is **`brand/MASCOT.jpeg`**. Attach it as a reference image every
time you generate a new video's `YOU` sheet.

### Fixed forever - Toss's identity (carry into every video, every era)

These are what make a returning viewer recognize him. Reproduce them exactly.

- **Head** - a large circle, flat white fill, bold even black outline. Roughly **one
  third of his total height**. This oversized head is the single strongest identity
  cue.
- **Hair** - **exactly TWO peaks. This is the signature and it is never changed.** One
  tall pointed peak leaning to the right, and one shorter peak beside it on its right.
  They are drawn as ONE single closed outlined shape with the same flat white fill as
  the head, sitting on the crown slightly right of centre, its outline merging into the
  head's outline so the tuft and the head read as one silhouette. Not three spikes, not
  four, not a fringe, not open separate strokes, not a filled black shape. Always the
  same two peaks, the same lean, the same place. Verified against `brand/MASCOT.jpeg` at
  magnification.
- **Eyes** - two solid black ovals, spaced wide, sitting low-ish on the face.
- **Brows** - two thick separate black strokes above the eyes. Bold shapes, never
  thin lines. They are his whole emotional range.
- **Mouth** - one simple curved line. Default is a small calm closed-mouth smile.
- **Face rules** - no nose, no ears, no cheeks, no chin line. Ever.
- **Neck** - a very short thin single line. The head almost sits on the garment.
- **Build** - thin single-line arms and legs with one soft bend, small splayed 3 to 4
  line fingers, tiny line feet. Slight, unimposing, never muscular or heavy.
- **Bearing** - an ordinary, mildly weary everyman. Not heroic, not comedic, not
  cute-mascot. Deliberately plain so any viewer can project onto him.

### What changes - costume and role only

Toss is an ordinary person the script drops into different worlds. Only his
**clothing, footwear, and props** change, matched to whatever setting the script's
`@YOU` section gives him.

- Modern default (as in `MASCOT.jpeg`): a plain **blue hoodie `#2E77C4`**, a simple
  filled hoodie silhouette with a small hood bump behind the neck and a shallow V
  notch at the collar, rounded bottom hem. Under it, small filled **charcoal
  `#3F3F46`** shorts.
- Modern variants: t-shirt and jeans, office shirt, pyjamas, jacket and scarf, gym
  clothes. Whatever the script actually puts him in.
- Other eras, if the script's `@YOU` section is set there: a hide wrap and bare feet
  for prehistory, a robe for a monastery, a plain sweater for a lab study.

**Costume color is free.** Toss is not tied to cobalt blue. Recognizability comes
from the head, hair tuft, face, and build, never from a color.

### Two hard limits on the costume

- **Never alter the identity list to fit a costume.** A hood may sit behind his head,
  but the head circle, the two-peak tuft, eyes, brows, and proportions stay exactly as
  specified. No hat or helmet that hides the hair tuft, no mask, no beard, no
  glasses, no hair color or style change.
- **Toss only ever plays `@YOU`.** He is the viewer stand-in and nothing else. The
  figure carrying the script's other era or setting is a genuinely different
  character with its own design, never Toss in a costume. If `@YOU` and that
  character share a frame, they must be clearly two different people.

## V2 scene compatibility without identity drift

Reference sheets remain clean flat model sheets on pure white in both V1 and V2. Do not add
paper grain, room scenery, atmospheric light, or cast shadows to a sheet. Those scene-level
effects belong to the V2 prompt tier, not to character identity.

For casts created for a V2 project:

- Use the V2 REFERENCE SHEET OPENING LINE for every non-`@YOU` sheet.
- Keep the existing BODY CONSTRUCTION, REFERENCE LAYOUT, ABSOLUTELY NO TEXT, CONSISTENCY, and
  NEGATIVE blocks. They are identity controls and do not change with rendering style.
- Specify a medium-heavy outer contour, thinner internal detail lines, and thin accessory lines.
  This prepares the design for V2 line hierarchy without adding scene depth to the sheet.
- Give every non-Toss character a silhouette, story-specific garment, and signature prop that
  still read when the later scene uses a tinted card or layered environment.
- Choose garment colors from the episode's three chapter colors or the core palette. Do not use
  saturated channel blue on a generic crowd, background group, or minor character when Toss
  wears his default blue hoodie.
- Include one sentence that the flat sheet defines identity and that attached-image V2 scene
  prompts may add only the render tier named in the scene prompt.
- For `@YOU`, the attached `brand/MASCOT.jpeg` still wins over every written description.

V2 changes surface treatment around a character. It never changes Toss's two-peak tuft, head
ratio, eyes, brows, mouth, proportions, limb construction, or splayed fingers.

## The sheet template - identical for every character

Every reference sheet prompt contains these blocks, in this order, as plain labeled
paragraphs. Open with the REFERENCE SHEET OPENING LINE from
`.agents/rules/visual-style.md`.

### BODY CONSTRUCTION (most important, get this exactly right)

The character is a **hybrid**: a stick figure's limbs on a big cartoon head, with ONE
filled piece of clothing standing in for the torso. It is not a pure line stickman,
and it is not a fully-drawn cartoon person.

- **Head** - a large circle, clearly the biggest element. Head height is roughly
  **one third of the character's total height**. Bold black outline of even, thick
  weight. Flat white fill.
- **Hair** - the character's own hair shape, drawn as one simple closed outlined shape
  sitting on the crown. For `@YOU` this is Toss's locked two-peak tuft above and is never
  altered. For every other character it is that character's own distinct silhouette (a
  flat fringe, a bob, a mane, a plain cap), chosen so no two cast members are told apart
  by facial detail alone.
- **Face** - two solid black oval eyes, spaced wide. Above them, two **thick separate
  black brow strokes**. The brows are the main emotional instrument and are always
  drawn as bold shapes, never thin hairlines. One simple curved line mouth. Nothing
  else: no nose, no ears, no cheeks.
- **Neck** - a very short, thin single line. Barely visible. The head almost sits on
  the garment.
- **Torso = one filled garment.** The body is a single simple filled clothing shape
  in the character's accent color (a hoodie, a tunic, a shirt) with a bold black
  outline and a rounded bottom edge. It is a garment silhouette, NOT an anatomical
  torso: no shoulders, no chest, no waist taper, no muscles, no body shape
  underneath.
- **Hips** - directly under the garment, one small filled dark shape (shorts or a
  hem) in a darker neutral, where the legs attach.
- **Arms** - thin single black lines coming out of the sides of the garment, with one
  soft bend. Pure lines: no sleeve volume, no thickness, no shoulder joint.
- **Hands** - small **splayed line fingers**, three or four short strokes fanning off
  the end of the arm line. Not mittens, not blobs, not nubs, not detailed anatomical
  hands.
- **Legs** - thin single black lines, same weight as the arms, with one soft bend at
  the knee.
- **Feet** - tiny simple line shoes: one short stroke with a small upturn at the toe.

Read it as: **big expressive head + one colored garment + four thin lines + small
splayed hands.**

### RENDERING QUALITY

- Bold black outline of even, confident, slightly rounded weight throughout. Clean
  and deliberate, like a good vector marker pen. Lively, but not scratchy, wobbly, or
  sketchy.
- Flat solid color fills. ONE slightly darker tone of the same hue is allowed along
  the bottom edge of a filled shape to give it a little weight. Nothing more.
- No gradients, no soft shading, no glow, no ambient occlusion, no paper or canvas
  texture.
- Crisp high-resolution linework. Every panel sharp and clean, no blur, no
  compression mush.

### REFERENCE LAYOUT (follow exactly)

- Wide 16:9 landscape canvas (animation model-sheet proportion), never square.
- Canvas split into a large top-left block, a top-right block, a bottom-left block,
  and a bottom-right prop block.
- Top-left: 3 full-body turnaround panels, left to right: front view, true side
  view, back view. All three stand on the same invisible baseline at identical
  height.
- Top-right: first row has 3 head close-ups (front, three-quarter, side). Second row
  has 4 face-only expression panels.
- Bottom-left: 4 full-body pose panels, from this character's POSES block.
- Bottom-right: oversized close-up of this character's signature PROP. If the block
  lists two props, draw both side by side at large scale.
- Draw subtle straight pale-grey panel-divider lines (`#D9D9D9`, 1 to 2 px) between
  EVERY panel: a vertical divider between top-left and top-right, a horizontal
  divider between top and bottom rows, and a vertical divider between bottom-left and
  bottom-right.
- Inside top-left add TWO pale-grey vertical dividers so front, side, and back each
  get an equal panel.
- Inside the top-right expression row add THREE pale-grey vertical dividers (four
  equal panels).
- Inside the bottom-left pose row add THREE pale-grey vertical dividers (four equal
  panels).
- Pure flat white background everywhere. No grid, no paper tone, no border, no frame
  around the sheet, no colored margin.
- Generous even whitespace around every figure. Nothing crops or touches a divider.

### ABSOLUTELY NO TEXT (hard rule, highest priority, overrides every other instruction)

Image models love to label model-sheet panels "FRONT / SIDE / BACK". Every such label
has to be suppressed explicitly. Do not shorten this block.

- The image must contain ZERO written characters of any kind. Not one letter, digit,
  word, symbol, or glyph anywhere on the canvas.
- Do NOT label the panels. No "FRONT", "SIDE", "BACK", "3/4", no view names, no pose
  names, no expression names, no character name, no "@YOU" or "@FRIEND".
- Do NOT add a title, header, footer, caption, legend, key, colour-swatch label, hex
  code, measurement, ruler mark, height chart, arrow, callout, signature, logo, or
  watermark.
- Do NOT write anything on the prop. A phone screen stays blank and dark: no icons,
  no time, no notification text.
- Do NOT render fake, garbled, or decorative pseudo-text as a design element.
- Panels are separated ONLY by the pale-grey divider lines described above. Dividers
  replace labels entirely. If a panel would feel ambiguous without a label, leave it
  unlabeled anyway.
- If the layout seems to "need" a label to be readable, that is wrong. Keep it blank.

### CONSISTENCY

Every panel is the identical design: same head circle size, same hair shape and peak
count, same eye spacing, same brow weight, same garment shape and color, same
limb length, same line weight. Do not redesign between views.

- Side view is a true profile: one eye visible, the hair tuft reads from the side,
  the garment keeps its silhouette.
- Back view has NO face. Just the back of the head, the hair tuft, and the garment
  from behind.
- The four expression panels change ONLY the brows and mouth. Head, hair, and eyes
  stay identical.
- Hands stay small splayed line fingers in every single panel.

### NEGATIVE

```
no pure line-only stickman with a single-line spine, no rubber-hose cartoon body, no anatomical torso, no shoulders, no chest, no muscles, no realism, no photorealism, no 3D render, no CGI, no gradients, no drop shadows, no cast shadows, no texture, no anime, no manga, no comic-book rendering, no detailed anatomy, no five-finger realistic hands, no mitten hands, no small head, no adult body proportions, no extra limbs, no busy background, no background scenery, no frame or border around the sheet, no inconsistent design between panels, no blur, no low resolution. NO text, NO letters, NO words, NO typography, NO lettering, NO handwriting, NO calligraphy, NO panel labels, NO view names, NO character names, NO titles, NO headers, NO captions, NO subtitles, NO annotations, NO callouts, NO arrows, NO numbers, NO digits, NO hex codes, NO colour swatches with labels, NO legend, NO key, NO signature, NO logo, NO watermark, NO garbled or gibberish pseudo-text, NO text on the prop or phone screen.
```

## Per-entry variations on the template

- **Group entries** (`TRIBE`, `CROWD`, `OFFICE`, `BAND`) get a sheet showing the group
  as a unit: the formation the script uses, 5 to 7 identical simplified figures
  dressed for that script's setting, plus panels for the group turned inward, turned
  away, and with one figure excluded. Use the four pose panels to show the GROUP, not
  one figure.
- **Prop or personified-concept entries** (`PHONE`, `BRAIN`, `FIRE`) skip the
  turnaround and expression logic that does not apply, and instead show 3 angles, 4
  emotional face states, and 4 states of use.
- **The `YOU` sheet is not a generation. It is an EDIT of `brand/MASCOT.jpeg`.** See the
  next section. This is the single most important rule for keeping Toss consistent
  across the channel.

## The `@YOU` sheet is an EDIT prompt, never a description prompt

Every other cast member is a new character, so their sheet describes a person from
scratch. **Toss already exists.** Describing him from scratch and hoping the model
rebuilds him identically is how the two-peak tuft turns into four spikes, how the head
shrinks, and how he stops looking like himself between videos.

So the `YOU` sheet prompt is written as an **image edit** against `brand/MASCOT.jpeg`:
keep this exact character, change only what the script requires.

**Shape of the prompt:**

1. Open by naming the attached image as the character and stating that it is preserved
   exactly. Something of the form: _"The attached image is the character. Reproduce this
   exact character with no redesign. Change ONLY what is listed under CHANGE below."_
2. **KEEP block** - an explicit list of what must not move: the two-peak tuft, the head
   circle and its one-third proportion, the wide black oval eyes, the two thick brow
   strokes, the single curved line mouth, no nose or ears, the short neck, the thin
   line limbs with splayed fingers, the line weight, the flat fill style.
3. **CHANGE block** - the short list the script actually justifies. Normally only the
   garment. Sometimes footwear or a prop. Nothing else.
4. **NEW EXPRESSIONS and NEW POSES** - the four and four this script needs. Expressions
   change the brows and mouth only. Poses change the limbs only.
5. The layout, rendering, no-text, consistency and negative blocks as usual.

**Do not write a BODY CONSTRUCTION paragraph for `@YOU`.** That paragraph exists to
build a character that does not exist yet. For Toss it competes with the attached
reference, and when a description and an image disagree the model blends them, which is
exactly the drift this system exists to prevent. Replace it with the KEEP block.

State plainly in the prompt that if the description and the attached image ever
disagree, **the image wins.**

The negative block for `@YOU` must include: _no redesign of the head, no change to the
hair, no extra hair spikes, no fringe, no different face, no new proportions._

## Distinguishability

- Every character's design is built from the channel's locked palette and doodle DNA:
  stick-figure build, large round head, dot eyes, thick black marker brows. Only the
  clothing, prop, hair, and posture change between characters.
- Make the cast visually distinguishable at a glance: give each member a different
  clothing color from the palette, plus one silhouette difference (hair tuft, hat,
  beard, build, posture). **Two characters must never be told apart by facial detail
  alone.**
- The character carrying the script's other era or setting must be visibly a
  different person, with its own head shape, hair, build, and clothing. Never Toss in
  different clothes. If the two share a split frame, the difference must be obvious
  at a glance.
