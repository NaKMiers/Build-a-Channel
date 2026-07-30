# Thumbnail rules

Canonical operational rules for TossExplains thumbnail concepts. Read this file and
`.agents/skills/thumbnail/references/style-spec.json` before writing any thumbnail prompt.

The style specification is self-contained. Never require competitor thumbnails, research
images, or external style references. Attach only the project character sheets used by a
prompt.

## A. Thumbnail-only rendering

Video scene prompts remain locked to the flat doodle style in `visual-style.md`. Thumbnails
use a separate rendering system because they must compete at feed size:

- Keep the attached TossExplains characters recognizable and faithful to their sheets.
- Draw characters as expressive 2D doodles with bold black outlines and slightly imperfect
  hand-drawn linework.
- Render the environment as a polished painterly cartoon with cinematic depth.
- Use controlled gradients, soft shadows, atmospheric haze, painted texture, and warm light
  spill when they improve depth and focus.
- Never use photorealistic people, 3D rendering, anime, or generic stock illustration.

Do not add the scene STYLE ANCHOR or STYLE LOCK to a thumbnail prompt. They prohibit the
lighting and depth this thumbnail-only style requires.

## B. Headline

- Use 1 to 4 words. Prefer 2 to 3.
- Use one straight line across the top whenever possible.
- Use uppercase heavy rounded sans-serif lettering.
- Use saturated golden yellow `#FFD900`, a very thick smooth black `#050505` outline, and a
  soft black shadow.
- Let the headline occupy roughly 85 to 94 percent of the canvas width.
- Integrate the headline directly into the illustrated environment. Treat it as part of the
  same full-frame composition, not a separate graphic layer.
- Reserve the top 22 percent for readable local contrast inside the same continuous scene.
  Continue the environment, atmospheric depth, and lighting behind, around, and below the
  letters.
- Allow one or two low-contrast environmental forms, such as haze, smoke, mountains, walls,
  branches, or machinery, to rise behind or between the letters without obscuring them.
- Never create a separate text band, header strip, banner, rectangle, solid-color panel, empty
  bar, border, or hard horizontal division.
- Render no other text.

The headline is a second hook, not a shortened title. It may be a question or an extremely
short statement. Prefer one of these functions:

- danger or consequence
- scarcity or time pressure
- visible contradiction
- social exposure or discovery
- shocking or forbidden behavior
- an urgent command tied to a fragile object or action
- unresolved outcome
- one physical mistake
- surprising behavior

Connect the words to something visible in the frame. Avoid abstract jargon and complete
explanations.

### Headline-image contract

Write one viewer question before composing the thumbnail. The headline and image must pursue
that same question from two directions:

- The headline asks, warns, commands, or predicts something involving a visible subject.
- The image confirms the premise with physical evidence and makes the stakes legible.
- The image withholds the decisive cause, identity, explanation, escape, or outcome.
- The combined effect must create more curiosity than either element creates alone.

The image should answer enough of the headline to orient the viewer, then introduce one new
piece of evidence that makes the unanswered part more urgent. If the headline can be swapped
for an unrelated phrase without changing the image, reject the concept.

## C. One cinematic story

Default to one full-frame story, not a split comparison:

- Start from a specific event in the script, not merely its topic or theory.
- Show the instant a character discovers the problem, one second before the consequence.
- Use one protagonist, one visible physical problem, and 1 to 3 supporting subjects.
- Make the main character roughly 45 to 60 percent of the frame height.
- Let the environment span the full canvas while keeping the main action in the middle and
  lower area. Do not crop the story into a panel beneath the headline.
- Keep no more than two focal points.
- Leave the bottom-right corner visually quiet for the duration badge.

Use a split comparison only when the script contains a genuinely useful contrast in
numbers, eras, temperatures, or states. Never force two split concepts into every set.

Prefer literal script incidents with a clear subject, action, witness or threat, physical
evidence, and imminent consequence. A concrete experiment or mechanism is valid when its
action is instantly understandable. Use a metaphor only when no script event can carry the
idea physically.

Never use a lone neutral portrait, a generic social tableau, a theory label presented as the
hook, a flat empty background, or several unrelated actions.

## D. Emotion and character identity

- Attach only the sheets for the `@TOKENS` used in the prompt.
- Preserve every attached character's head, hair, face geometry, proportions, clothing, and
  recognizable design. Change only expression, pose, placement, and lighting.
- Make one face emotionally dominant and readable at phone size.
- Describe the eyes, eyebrows, mouth, hands, and body direction explicitly.
- For sadness or worry, write: `eyebrows angled so the inner ends sit clearly higher than
  the outer ends, worried and dismayed, not angry, not frowning`.
- Give co-stars visible faces and distinct reactions.
- Do not modify the mascot's body or identity.
- Do not request an exact crowd count above five.
- Exactly one figure may look directly at the viewer.

## E. Environment, color, and light

Build a real place around the story:

- Use a foreground, midground, and background.
- Keep the main face, physical problem, and important animal or object sharpest.
- Use deep navy, storm blue, charcoal, forest green, ice blue, and earth brown as the
  dominant environment families.
- Use one warm orange or golden visible light source.
- Illuminate the main face clearly.
- Keep distant colors quieter and nonessential corners darker.
- Keep faces, tools, and bright highlights away from the headline, but carry low-contrast
  environmental forms and the same scene lighting behind it.

The preferred formula is a cool dark environment plus a concentrated warm focal light. A
bright setting is allowed when the script requires it, but the headline still needs a dark
quiet upper portion of the same continuous scene.

## F. Packaging

- Render at `1280x720`, 16:9.
- Add the logo later in an editor, small at bottom-left. Never ask the model to draw it.
- Keep the bottom-right corner quiet.
- If the model garbles the headline, generate the art without text and add the headline in
  an editor.
- Test the result at 120 pixels wide.

## Concept diversity

When writing five prompts, use five different script moments. Prefer:

1. the opening physical situation
2. the named experiment or mechanism made concrete
3. the ancestral or anthropological scene
4. a modern-versus-ancestral contrast
5. the strongest number, consequence, or counterintuitive fact

Do not make five camera-angle variants of one idea.

## Single-scene prompt template

Fill every bracketed slot. The generated prompt is one unbroken line.

```text
Create a beautiful, high-impact YouTube thumbnail illustration in 16:9 format, 1280x720. Use the attached character sheets as strict identity references for [TOKENS]. Preserve their exact head shapes, hair, faces, proportions, clothing, colors, and recognizable designs while changing only their expressions, poses, lighting, and placement. Render the exact headline "[HEADLINE]" in one straight line across the top, using huge uppercase rounded golden-yellow letters with a very thick smooth black outline and a soft black shadow. Make the letters occupy approximately [85 TO 94] percent of the canvas width. Integrate the headline directly into the illustrated environment so the typography and artwork feel like one continuous composition. Reserve the top 22 percent for headline readability inside that same continuous scene, but do not create a separate text band, header strip, banner, rectangle, solid-color panel, empty bar, border, or hard horizontal division. Continue the same environment, atmospheric depth, and lighting uninterrupted behind, around, and below the letters. Allow one or two low-contrast environmental forms to rise behind or between the letters without covering them. Show [MAIN TOKEN AND ACTION] large in the [POSITION], experiencing extreme [EMOTION] because of [VISIBLE PHYSICAL PROBLEM]. Capture the exact moment the problem is discovered, one second before the consequence, with the outcome unresolved. [EXPLICIT EYES, EYEBROWS, MOUTH, HANDS, AND BODY POSE]. Include [SUPPORTING TOKENS, ANIMAL, OBJECT, OR THREAT] to create conflict, danger, scale, or emotional contrast. Set the scene in [SETTING FROM SCRIPT], using [FOREGROUND], [MIDGROUND], and [BACKGROUND] to create cinematic depth. Use a cool dark palette of deep navy, storm blue, charcoal, forest green, ice blue, and earth brown, with one concentrated warm orange or golden visible light source illuminating the main face and problem. Keep the background atmospheric but subordinate to the faces. The visual hierarchy must be headline first, main emotional face second, visible problem third, supporting subject fourth, and environment last. Use expressive doodle-like characters with bold black outlines and slightly imperfect hand-drawn linework inside a richly painted cinematic 2D cartoon environment with atmospheric depth, controlled gradients, soft shadows, painted texture, cohesive dramatic lighting, beautiful color grading, and strong mobile readability. Exactly one figure looks directly at the viewer. Leave the bottom-right corner visually quiet for the YouTube duration badge. Spell "[HEADLINE]" exactly and render no other text. No logos, watermarks, detached headline panels, unnecessary arrows, extra limbs, duplicated faces, weak expressions, tiny subjects, unrelated actions, photorealistic people, 3D rendering, anime styling, generic stock illustration, flat lighting, or empty background.
```

## Split comparison template

Use only for a real comparison. The generated prompt is one unbroken line.

```text
Create a beautiful, high-impact YouTube thumbnail illustration in 16:9 format, 1280x720. Use the attached character sheets as strict identity references for [TOKENS]. Preserve their exact designs while changing only expressions, poses, lighting, and placement. Divide the story into two clearly readable halves with a strong central separation created by composition and lighting, not a decorative border. Render the exact headline "[HEADLINE]" in one straight line across the top, using huge uppercase rounded golden-yellow letters with a very thick smooth black outline and a soft black shadow. Integrate the headline directly into the illustrated environment so the typography and artwork feel like one continuous composition across both halves. Reserve the top 22 percent for headline readability inside that same continuous scene, but do not create a separate text band, header strip, banner, rectangle, solid-color panel, empty bar, border, or hard horizontal division. Continue the environments, atmospheric depth, and lighting uninterrupted behind, around, and below the letters. Allow one or two low-contrast environmental forms to rise behind or between the letters without covering them. On the left, show [FIRST STATE WITH A VISIBLE NUMBER, ERA, OR CONDITION]. On the right, show [SECOND STATE WITH A VISIBLE NUMBER, ERA, OR CONDITION]. Make the contrast understandable without the video title. Give each visible character a readable face and reaction, with one emotionally dominant character looking directly at the viewer. Use a cool dark palette with one concentrated warm orange or golden visible light source and a richly painted cinematic 2D cartoon environment with atmospheric depth, controlled gradients, soft shadows, painted texture, bold black doodle outlines, and strong mobile readability. Leave the bottom-right corner visually quiet for the YouTube duration badge. Spell "[HEADLINE]" exactly and render no other text beyond the essential comparison numerals or units. No logos, watermarks, detached headline panels, unnecessary arrows, extra limbs, duplicated faces, weak expressions, tiny subjects, unrelated actions, photorealistic people, 3D rendering, anime styling, generic stock illustration, flat lighting, or empty background.
```

## Rejection gate

Reject and rewrite a concept when any answer is no:

1. Is the headline four words or fewer?
2. Does the headline add information instead of repeating the title?
3. Does the scene depict a specific event, action, object, relationship, or consequence from
   the script?
4. Do the headline and image pursue one shared viewer question?
5. Does the image partially answer the headline with visible physical evidence?
6. Is a decisive cause, explanation, identity, escape, or outcome still withheld?
7. Is the physical problem visible?
8. Is one emotion obvious in half a second?
9. Are there no more than two focal points?
10. Is the outcome unresolved one beat before the consequence?
11. Would changing the headline require changing the scene?
12. Is the headline readable inside the same continuous scene, with no detached panel?
13. Are only project cast sheets required?
14. Is the bottom-right corner quiet?
15. Will the design still read at 120 pixels wide?
