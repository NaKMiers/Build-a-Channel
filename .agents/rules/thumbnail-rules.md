# Thumbnail rules

Canonical source for thumbnail concepts. Read this before running the `thumbnail`
skill.

The thumbnail decides whether the video is watched at all, so it is generated to a
fixed, proven pattern, not invented per video. **Every rule here was either validated
or forced by a real generation round.** The competitor teardown that produced them is
`research/thumbnail-swipe/ANALYSIS.md`, with the 40 sampled thumbnails beside it.
Do not "improve" these by reverting to flat empty frames or clever abstract wording.

## Evidence base

- `@SticklyExplains`, 41.5K subs, same niche and same stick-figure format. Their 2M
  view outlier says only "WHY NOT ATTACK?" over a sleeping figure and a wolf. Their
  top 20 average 2.4 words of thumbnail text and only 1 of 20 uses a number.
- `@Simplewaysoflife`, 26.2K subs. Opposite formula: typography carries everything,
  60 percent of their top 20 lead with a big number, solid white background.
- Our own A/B round: 5 concepts generated, 1 accepted
  (`projects/1-*/outputs/thumbnail-3-accepted.jpg`, the split-frame `LOST 110 PEOPLE?`).
  The 4 rejects produced the failure rules in section E.

## A. Layout - default to the split comparison

- **The strongest layout is a frame split in half by a thick vertical black line**,
  with a different scene on each side and a big number over each. It won the A/B round
  outright, because it puts two facts side by side and makes the viewer do arithmetic.
  Use it for any script containing two contrasting quantities, eras, or states. Build
  at least two of the five concepts this way.
- **The other layout is one big near figure plus a real scene behind him.** `@YOU`
  from the chest or waist up in one third of the frame, the thing he is reacting to
  deeper in the other two thirds.
- **Never a lone figure on an empty background.** Two parties must be visible and
  something must be happening between them.

## B. The number

- **Two different numbers that invite subtraction beat one number.** `150` on one side
  and `40` on the other, with the text asking about the difference, is the pattern
  that worked.
- **A drawn number is the largest graphic object in its half of the frame**, roughly
  half the frame height, hand-lettered, thick black outline. Never a small caption.
- **The text must never repeat a number that is already drawn.** Text `40 FRIENDS?`
  next to a giant drawn `40` printed the number twice and read as a duplication bug.
- A number is optional, not mandatory. The best-performing thumbnail in our niche has
  none. Use one when the script supplies a genuinely surprising quantity, skip it
  otherwise.

## C. The question text

- **Always a QUESTION.** 2 to 4 words, ALL CAPS, ending in a question mark. Never a
  statement, never a sentence, never more than 4 words.
- **Every noun in the question must be a physical object drawn in the frame.**
  `FIRST SALT?` works because salt is on the ground. `LOST 110 PEOPLE?` works because
  both counts are drawn. `WHY THE HOLLOW?` and `A 200,000-YEAR BUG?` failed because
  nothing in the frame answers "about what?". If the noun cannot be drawn, the
  question is dead. Rewrite it.
- **The question must never restate the title.** The title says what the video is
  about. The thumbnail asks the one thing the title leaves open.
- **Lettering spec, identical every time:** bold hand-lettered marker ALL CAPS in
  golden yellow `#F5C518` with a thick black outline, running **perfectly straight**
  across the very top of the frame, full-bleed from the left frame edge to the right
  frame edge, letters nearly touching both edges. **Not arced.** The old arc cost 20
  to 30 percent of letter height for nothing. Never change the color, never move it to
  the bottom, never add a second line.
- **The band of background behind the text is the darkest area of the image.** A
  near-black strip under yellow lettering is what makes it survive at 120 px.

## D. The scene - flat, but never empty

- **A flat solid single background color produces a dead frame.** Every generation
  built that way came back with large void areas and nothing to look at. Give the
  frame a minimal but real place: a ground line, a dark horizon or hills, and one
  environment prop the script actually contains (a fire, a cave mouth, a bed, a
  doorway).
- **One warm light source against a dark cool ground is what makes the frame pop.** A
  small bright orange fire on dark brown earth under a very dark blue sky did it. Keep
  the palette dark and cool, then put one warm accent in it.
- **Props must never use the lettering yellow `#F5C518`.** A yellow ball on the same
  frame as yellow text merged into it and read as a sun.
- Still zero gradients, zero shadows, zero textures, zero photorealism, zero 3D. Flat
  fills only.

## E. The figures - what the image model will and will not do

Each of these is a recorded failure, not a preference.

- **Co-stars need visible faces with visible expressions.** Featureless black
  silhouettes render as a black smear, and "blank white heads with no features"
  rendered as a field of giant white eggs that ate the whole frame. Never ask for
  faceless, blank, or silhouette crowds. Give the background band real small faces
  turned toward each other.
- **Write the sad expression as an explicit eyebrow geometry, and say it is not
  anger.** "Brows pinched upward at their inner edges" is read as angry V-brows about
  half the time. Write: *eyebrows angled so the inner ends sit clearly higher than the
  outer ends, worried and dismayed, not angry, not frowning*, plus a downturned mouth
  and one blue sweat drop.
- **Never modify the mascot's body.** A hole through the chest rendered as a dark
  stain on his hoodie. Emotions go on the face and in the posture, never into anatomy.
- **Never ask for an exact count above five.** A request for five figures produced
  four, which broke the text that depended on it. Use "a dense block" or "a tight row"
  and never let the wording of the question depend on a count the model has to get
  right.
- `@YOU` is the hook figure in almost every concept, head tinted pale blue for lonely
  or red for embarrassed. Thumbnail expressions are pushed harder than scene
  expressions. His design is still locked: exaggerate the feeling, never restyle the
  head, eyes, or proportions.
- **Exactly one figure looks straight out of the frame at the viewer.** Eye contact
  with the lens is one of the strongest attention hooks available, and it must be a
  figure that has eyes.

## F. Framing and packaging

- **The bottom-right corner stays empty.** YouTube stamps the video duration over it.
- **The logo badge is added in the editor, not by the image model**, small,
  bottom-left. Asking the model to draw the logo garbles it.
- **Generate five distinct concepts**, each built on a different moment from the
  script (the opening feeling, the named experiment, the ancestral scene, the
  then-vs-now split, the counterintuitive number), so the channel can A/B test instead
  of betting on one frame.
- Every thumbnail prompt uses the same STYLE ANCHOR and STYLE LOCK as the image
  prompts, and refers to cast members by `@TOKEN` only.

## The two layout templates

Fill the bracketed slots from the script. Keep everything outside the brackets
verbatim.

### Split comparison

```
[thumb-a] Hand-drawn 2D doodle cartoon animation, flat colors, bold black outlines, slightly imperfect sketchy marker lines, a thick vertical black divider line splitting the frame exactly in half, left half [SCENE ONE: flat dark ground + flat very dark sky + the script's environment prop + a tight group with visible small faces turned toward each other] and the numeral [N] hand-lettered enormous in white with a thick black outline standing over them at roughly half the frame height, right half [SCENE TWO: flat dark background + @YOU drawn large from the chest up, head tinted pale blue, eyebrows angled so the inner ends sit clearly higher than the outer ends, worried and dismayed, not angry, not frowning, mouth downturned] and the numeral [M] hand-lettered enormous in golden yellow #F5C518 with a thick black outline standing over him at roughly half the frame height, @YOU looking straight out of the frame directly at the viewer, bold hand-lettered ALL CAPS text "[2-4 WORD QUESTION?]" in golden yellow #F5C518 with a thick black outline running perfectly straight across the very top of the frame from the left frame edge to the right frame edge at very large size with the letters nearly touching both edges, text not arced and not curved, the band of background behind that text is the darkest area of the whole image, no other text anywhere, bottom-right corner of the frame left completely empty, no gradients, no shadows, no textures, no photorealism, no 3D, no timestamp shown in the image, @[name] is mention syntax for reference only and must never be rendered as visible text, 16:9 aspect ratio, educational YouTube explainer doodle style.
```

### Near figure plus scene

```
[thumb-b] Hand-drawn 2D doodle cartoon animation, flat colors, bold black outlines, slightly imperfect sketchy marker lines, @YOU drawn large in the [left|lower left] of the frame from the waist up [expression written as explicit eyebrow geometry + "not angry"], his eyes aimed at [THE ONE OBJECT THE QUESTION NAMES] drawn in the [opposite third] of the frame, [a tight row or dense block of small figures with visible faces and readable expressions] behind it, [flat dark ground line + dark horizon + ONE environment prop from the script + one small warm orange light source], one figure looking straight out of the frame directly at the viewer, bold hand-lettered ALL CAPS text "[2-4 WORD QUESTION?]" in golden yellow #F5C518 with a thick black outline running perfectly straight across the very top of the frame from the left frame edge to the right frame edge at very large size with the letters nearly touching both edges, text not arced and not curved, the band of background behind that text is the darkest area of the whole image, no other text anywhere, bottom-right corner of the frame left completely empty, no gradients, no shadows, no textures, no photorealism, no 3D, no timestamp shown in the image, @[name] is mention syntax for reference only and must never be rendered as visible text, 16:9 aspect ratio, educational YouTube explainer doodle style.
```

## Post-generation review, tell the user this

Shrink the favourite to 120 px wide and look at it. If the question is not readable
and the emotion is not obvious in half a second, regenerate. Do not rescue a weak
thumbnail with more text. If the model garbles the lettering, generate the frame with
the text clause deleted and add the words in the editor. If a frame comes back with
large empty areas, the background was too flat: add a ground line, a horizon, and one
warm light source, then regenerate.
