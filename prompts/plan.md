# TossExplains Visual Style V2 Plan

Status: PROPOSED. No implementation is authorized until the owner approves this file.

## Executive decision

Adopt a new channel art direction called **Warm Editorial Storybook Doodle**.

This is not a copy of PastTense. It keeps the Toss mascot, psychology-first storytelling,
hand-drawn character identity, simple explanations, and orange-cobalt brand memory. It changes
the part that is currently holding the channel back: white-slide repetition, low color variety,
flat staging, weak shot variation, and slow visual-beat density.

The V2 promise is:

> Every visual beat should feel like either a small illustrated story, a clear editorial card,
> or a satisfying build toward a payoff. The viewer should never feel that the narration is
> continuing while the picture has stopped thinking.

The recommended direction is a middle path between the two reference videos:

- Borrow the warm storybook environments, object specificity, and visual callbacks from
  `Why Humans Eat 3 Meals a Day`.
- Borrow the pastel chapter coding, mode rotation, scientific diagrams, scale metaphors, and
  emotional ending from `The Rarest Human Possible`.
- Keep TossExplains more controlled than either reference: one mascot system, one text system,
  one outline system, fact-checked diagrams, and a smaller palette led by Toss orange and cobalt.

## What PastTense's style actually is

The most accurate name is **hand-drawn editorial storybook explainer**, with an
**illustration-infographic hybrid** grammar.

It is not merely a 2D doodle style. The shared visual DNA across the two videos is:

- Hand-inked digital illustration with slightly imperfect dark outlines.
- Simple round-faced characters placed inside richer, story-specific environments.
- Warm paper-like or pastel color grounds instead of a default empty white canvas.
- Semi-flat rendering. Shapes stay graphic, but selected frames use tonal steps, contact
  shadows, glow, texture, depth planes, and background softening.
- Constant rotation between story scene, close-up, card, diagram, map, scale metaphor,
  character reaction, and payoff text.
- Progressive disclosure. A base composition gains one new object or label per beat.
- Editorial text used as a verdict, not as subtitles.
- Recurring objects and repeated frames that return with a new meaning.

The two videos use different surface treatments:

- `Why Humans Eat 3 Meals a Day` is a warm historical storybook cartoon. It uses cream,
  amber, terracotta, olive, muted blue, detailed period environments, and a vintage editorial
  feel.
- `The Rarest Human Possible` is a brighter pastel science storybook. It uses cream, coral,
  olive, lavender, pale blue, playful diagrams, crowds, and scale metaphors.

Their common advantage is not one palette. It is a visual decision system that keeps changing
the viewer's task: watch a story, read a card, solve a diagram, notice a build, feel a reaction,
then receive a payoff.

## Evidence from the two swipe studies

### Visual rhythm

| Video | Duration | Visual beats | Beats per minute | Mean gap | First 15 seconds |
| --- | ---: | ---: | ---: | ---: | ---: |
| Why Humans Eat 3 Meals a Day | 8:25 | 272 | 32.3 | 1.85s | 14 beats |
| The Rarest Human Possible | 6:18 | 181 | 28.7 | about 2.05s | 9 beats |
| Toss project 1 | 11:27 | 255 | 22.3 | 2.70s | 8 beats |
| Toss project 2 | 12:00 | 263 | 21.9 | 2.75s | 7 beats |
| Toss project 3 | 12:04 | 266 | 22.0 | 2.73s | 6 beats |
| Toss project 4 | 13:11 | 268 | 20.3 | 2.96s | 8 beats |

The current Toss pipeline produces roughly 20 to 22 beats per minute. The reference videos
produce roughly 29 to 32. Toss therefore asks the viewer to hold the same visual state about
35 to 45 percent longer.

The difference is more visible in long holds:

- `Why Humans Eat 3 Meals a Day` has only 6 gaps of 4 seconds or longer.
- Toss project 1 has 55.
- Toss project 4 has 76.

### Color and surface

The following measurements are mean pixel statistics across all extracted frames. They are
not prompt-background counts.

| Set | Near-white pixels | Mean saturation | Colorfulness |
| --- | ---: | ---: | ---: |
| Why Humans Eat 3 Meals a Day | 1.1% | 0.384 | 52.8 |
| The Rarest Human Possible | 4.7% | 0.335 | 51.2 |
| Toss project 1 | 39.6% | 0.269 | 41.2 |
| Toss project 4 | 47.8% | 0.168 | 36.5 |

This confirms the contact-sheet impression. Toss frames are not only simpler. They are far
more often dominated by near-white space and have much lower color saturation.

### Mechanisms that repeat across the successful references

1. **Story before explanation.** Both hooks start with a concrete body, place, object, or
   relationship before presenting the abstract question.
2. **One focal point per frame.** Detailed frames still have one obvious place for the eye to
   land first.
3. **Progressive builds.** The meal video has eight major build chains and seven text-over-image
   verdict payoffs. The rarest-human video repeatedly adds icons, people, genes, cones, and
   probability factors one at a time.
4. **Register rotation.** The meal video changes visual register after about 2.26 beats. The
   rarest-human video alternates story scenes, portraits, diagrams, calculations, and scale
   metaphors.
5. **Shot variation.** Wide establishing shots, medium action shots, close-ups, macro object
   views, overhead views, and POV hands all appear inside the first few minutes.
6. **Chapter color coding.** A background family announces a new subject before the narration
   finishes introducing it.
7. **Text hierarchy.** Neutral information is dark. Verdicts, negations, and pivots are red.
   Text is large and sparse.
8. **Functional detail.** A period kitchen, laboratory apparatus, ship ration, book cover, or
   receptor diagram carries evidence. Detail is not random decoration.
9. **Asset reuse with changed meaning.** About 5.5 percent of the meal video's beats reuse an
   earlier frame. The ending recap and final callback cost almost no new art.
10. **Emotional convergence.** The ending turns the information back toward the viewer and
    visually echoes the hook.

## Why current TossExplains visuals feel less engaging

The current system is coherent, but it is over-constrained in the wrong places.

1. **Pure white is a channel-wide default, not a deliberate pause.** Consecutive frames often
   read like slides from the same deck even when the objects change.
2. **The frame library is too card-heavy.** Centered character, centered diagram, top caption,
   and empty white background recur more often than story staging or camera changes.
3. **Bold uniform outlines flatten depth.** A foreground hand, a character, and a background
   object often have equal visual weight.
4. **The render lock bans every controlled depth tool.** No texture, shadow, tonal step,
   gradient, or atmosphere means the prompt cannot request the exact qualities that make the
   PastTense scenes feel illustrated rather than assembled.
5. **Every transcript cue is treated as the natural visual unit.** Current cues average close
   to 3 seconds. PastTense often creates a new visual event inside that interval.
6. **Held scenes are usually expression swaps, not information builds.** The viewer sees a new
   face, but does not always receive a new object, relation, label, or question.
7. **There is no enforced shot sequence.** A script can spend a long section at the same camera
   distance even when the frame content changes.
8. **Background color currently signals mood more than chapter structure.** PastTense uses a
   controlled color family to mark conceptual movement.
9. **The current source-of-truth rules optimize consistency before interest.** V2 must protect
   both.

## The V2 visual system

### 1. Aesthetic

**Direction:** Warm Editorial Storybook Doodle.

**Mood:** curious, human, clever, warm, slightly imperfect, emotionally observant, and visually
specific. It should feel drawn by one illustrator with an editorial eye, not generated by a
different model for every timestamp.

**Memorable thing:** Toss explains a difficult inner mechanism through a tiny illustrated world
that keeps revealing new meaning.

### 2. What stays locked

- Toss remains the primary mascot and must match `brand/MASCOT.jpeg`.
- The channel stays 2D and hand-drawn.
- No photorealism, CGI, plastic 3D, realistic faces, or anime styling.
- Characters keep readable brows, mouth lines, poses, and simple proportions.
- Orange and cobalt remain the two strongest brand colors.
- Black or charcoal remains the default information color.
- Red remains reserved for danger, failure, negation, and decisive pivots.
- The image stays readable at mobile size.
- Each frame has one dominant focal point.
- Science and historical claims must be fact-checked independently of the script.

### 3. What changes

- Pure white stops being the majority background.
- Warm cream and light chapter tints become the default card surfaces.
- Story frames gain foreground, midground, and background planes.
- Outline weight becomes hierarchical instead of uniformly bold.
- Controlled paper grain, one contact shadow, one tonal step, and rare motivated glow become
  legal in named render tiers.
- The system gains explicit shot planning and register rotation.
- Visual beats become finer than narration cues when the meaning changes inside a cue.
- Progressive variants and callbacks become planned production assets, not improvised extras.

### 4. Palette

The palette is led by existing Toss colors and extended with muted chapter colors.

| Role | Color | Hex | Use |
| --- | --- | --- | --- |
| Warm paper | Cream | `#FFF4DE` | default card surface and modern neutral |
| Ink | Charcoal | `#2F3133` | outlines, neutral text, diagrams |
| Brand 1 | Orange | `#F5820D` | energy, ritual, key brand memory |
| Brand 2 | Cobalt | `#2D5FBF` | mind interiors, trust, cool contrast |
| Verdict | Red | `#D94040` | negation, threat, decisive conclusion |
| History | Tan | `#C4965A` | anthropology and ancestral worlds |
| Human warmth | Coral | `#D96F5F` | relationships, shame, attachment, social scenes |
| Nature | Olive | `#8FA35A` | tribe, landscape, regulation, belonging |
| Science | Dusty teal | `#67A6A3` | mechanisms, experiments, body systems |
| Memory | Lavender | `#B79AD9` | memory, perception, unusual cognition |
| Highlight | Golden yellow | `#F2C14E` | small object highlight, never body text on light ground |

Each video should choose three chapter colors plus cream, charcoal, orange, cobalt, and red.
It should not use the full extension palette in every episode.

### 5. Background budget

Replace the current majority-white rule with this target:

| Surface family | Target | Purpose |
| --- | ---: | --- |
| Warm cream or off-white cards | 30% | clean explanations, modern life, number cards |
| Light tinted chapter cards | 20% | topic changes, definitions, compact diagrams |
| Illustrated story environments | 35% | hooks, experiments, anthropology, modern mismatch |
| Cobalt mind interiors | 7% | only when literally inside thought, memory, or attention |
| Pure white cards | 8% | maximum clarity for dense science or contrast pauses |

One near-dark hero frame may be used for a major reveal. It must immediately return to the
light system. Dark mode is punctuation, not a chapter palette.

### 6. Three render tiers

#### CLEAN

- Target: about 40 percent of beats.
- Warm cream, pure white, or one light chapter tint.
- Flat fills, charcoal outlines, no atmospheric blur.
- One to four objects, generous negative space.
- Best for numbers, labels, diagrams, and direct reactions.

#### LAYERED

- Target: about 50 percent of beats.
- Three flat depth planes created with overlap, scale, and color value.
- One hard-edged or restrained contact shadow may clarify grounding.
- Very subtle paper grain may unify the whole frame.
- At most two tonal values inside one object.
- Best for story scenes, experiments, rooms, camps, streets, and period worlds.

#### ATMOSPHERIC

- Target: 10 percent maximum.
- Reserved for hook hero shots, major chapter transitions, reveals, and ending payoffs.
- One motivated gradient, glow, light spill, or softened background is allowed.
- Foreground characters and key graphics remain clearly 2D and hand-inked.
- Never use it for an ordinary narration beat.

### 7. Line and character treatment

- Use dark charcoal rather than absolute black where possible.
- Use medium-heavy outer contours for the focal subject.
- Use thinner internal detail lines and background lines.
- Keep the slightly imperfect hand-drawn wobble.
- Give secondary cast period-specific clothing, hair silhouettes, and props, while keeping
  their faces simple.
- Do not use clothing color as the only identity system. Silhouette, hair, prop, and posture
  should also carry identity.
- Toss may appear as narrator, participant, or observer, but not as a static presenter for
  four consecutive beats.

### 8. Visual registers

Every beat is assigned one register before a prompt is written.

| Register | Job | Target share |
| --- | --- | ---: |
| STORY | concrete action inside a place | 30 to 40% |
| CARD | object, number, title, or concise editorial verdict | 15 to 20% |
| DIAGRAM | causal mechanism, experiment, anatomy, or flow | 15 to 20% |
| PORTRAIT | face, posture, emotion, or researcher | 10 to 15% |
| HYBRID | story scene plus diagram overlay or question layer | 10 to 15% |
| SPLIT_OR_SCALE | comparison, then-vs-now, crowd, distance, probability | 5 to 10% |

Change register after two or three beats on average. A four-beat run is legal only when it is
an intentional progressive build on one base plate.

### 9. Shot grammar

Every 30-second block should contain at least four of the following:

- Wide establishing shot.
- Medium action shot.
- Character close-up.
- Macro object detail.
- Overhead or POV hands.
- Card or diagram.
- Scale or crowd metaphor.

Do not use the same camera distance more than twice in a row unless the frame is a deliberate
build. New plates should define a camera axis. Variants must preserve that axis.

### 10. Progressive disclosure

Each 10 to 12 minute video should contain:

- 5 to 8 build chains.
- 3 to 4 beats per chain.
- One base plate plus delta-only variants.
- One new information unit per variant.
- A final payoff that changes the meaning of the completed plate.

Good deltas include one object, one arrow, one label, one character, one crossed-out state,
one changed number, or one revealed cause. Expression-only deltas do not count unless the
emotion itself is the meaning change.

### 11. Text system

- Text appears on roughly 25 to 35 percent of beats, not every beat.
- Neutral labels and researcher names use charcoal.
- Verdicts and negations use red.
- White text is legal only on a deliberately dark or softened hero plate.
- Golden yellow is an object highlight, not body text on a light background.
- Use one to five words when possible.
- Generated text must be checked letter by letter before editing.
- Use one recurring red X shape for visual negation across the whole channel.

### 12. Motifs, evidence, and callbacks

- Give every episode one recurring object motif tied to the central mechanism.
- Reuse 5 to 8 percent of frames or plates near the ending.
- A callback must change meaning, not merely fill time.
- The final visual should echo or reuse a hook visual.
- Draw named researchers as people, books, papers, or experiment objects when useful.
- Turn sources into visible evidence objects, but keep formal citations in metadata or the
  description rather than rendering unreadable fine print.

## Visual-beat production target

### Cadence

| Section | Target beats per minute | Typical gap |
| --- | ---: | ---: |
| First 15 seconds | 45 to 60 | 1.0 to 1.3s |
| 15 to 45 seconds | 36 to 45 | 1.3 to 1.7s |
| Psychology and mechanisms | 28 to 34 | 1.8 to 2.1s |
| Anthropology story work | 26 to 32 | 1.9 to 2.3s |
| Dense reading or evidence | 22 to 26 | 2.3 to 2.7s |
| Ending | 24 to 28 | 2.1 to 2.5s |

Whole-video target: **28 to 32 visual beats per minute**.

No ordinary hold should exceed 4 seconds. A longer hold must contain text to read, an
intentional emotional pause, or an edit motion that creates a new visual event.

### Production economics

The target is not 360 unrelated generations for a 12 minute video. A recommended beat mix is:

- 35 to 45 percent new base plates.
- 30 to 40 percent delta variants from an attached base plate.
- 10 to 15 percent reframes, crops, or overlays in CapCut.
- 5 to 10 percent exact callbacks or repeated assets.
- 5 to 10 percent text-only, icon-only, or diagram updates.

This produces PastTense-level visual rhythm without requiring PastTense-level unique-scene
count.

## Important causal caveat

PastTense's visual system is stronger, but visuals do not explain all of its performance.

The channel page checked on 2026-08-03 showed 16 videos and 15.6K subscribers. Four videos had
roughly 1M, 531K, 315K, and 156K views, while many others were between about 2.8K and 20K.
The same channel style appears on both hits and misses.

Therefore:

- Better visuals should improve retention and perceived quality.
- Topic selection, title, thumbnail, promise, and audience fit still decide whether the video
  receives the first large wave of impressions.
- Do not judge V2 only by one video's views. Evaluate click-through rate, first-30-second
  retention, average percentage viewed, and comment language about the visuals across at least
  three uploads.

## Implementation plan after approval

### Phase 1: Build a controlled visual pilot

Goal: prove the art direction before changing the global pipeline.

1. Select a 45 to 60 second sequence from the accepted project 1 hook.
2. Leave every existing project file untouched.
3. Create a separate research pilot with 16 to 24 planned beats.
4. Produce three small directions from the same narration and cast:
   - Conservative: cream cards plus flat depth.
   - Recommended: CLEAN, LAYERED, and limited ATMOSPHERIC tiers.
   - Aggressive: full colored storybook treatment close to PastTense intensity.
5. Render representative wide, medium, close, macro, card, diagram, build, and payoff frames
   with the actual Google Flow workflow.
6. Build a side-by-side contact sheet against the current project 1 frames.
7. Approve one direction based on coherence, readability, attractiveness, and cast stability.

Pilot pass criteria:

- The 24-up sheet no longer looks like repeated white slides.
- Toss is still recognizable without reading the channel name.
- At least 80 percent of delta variants preserve the base composition closely enough to edit.
- Text remains readable at 25 percent scale.
- No frame looks photorealistic, 3D, anime, or like a different channel.
- The recommended direction feels richer than V1 without becoming visually noisy.

### Phase 2: Version the style system

Do not overwrite the accepted V1 system in place.

1. Keep V1 style strings available for legacy project validation.
2. Add V2 scene anchor and lock definitions in `.agents/rules/visual-style.md`.
3. Update `.agents/bin/style-strings.sh` to export both legacy and current scene strings.
4. Make `/check` accept one internally consistent style version per project.
5. Make `/scenes` use V2 for new projects only.
6. Do not rewrite project 1 or any published project.

This avoids breaking the regression fixture and avoids touching the owner's current uncommitted
work in project 5.

### Phase 3: Upgrade cast generation

1. Update the cast skill and mascot rules with V2 line-weight hierarchy, storybook costume
   specificity, and chapter-palette compatibility.
2. Keep Toss identity fixed to `brand/MASCOT.jpeg`.
3. Add a cast-sheet check for silhouette, hair, signature prop, and neutral-color separation.
4. Keep old character sheets valid for V1 projects.

### Phase 4: Add lean visual-beat planning

Do not restore the deleted project-5 visual-plan system wholesale. Its schema is too heavy for
the core need.

Add a lean planning pass before prompt writing with only these fields:

- beat id and time
- narration meaning change
- register
- shot
- render tier
- plate id
- source beat for variants
- delta
- motif or callback
- text, if any

The plan may be an internal scenes-work artifact or a small validated file. Choose the smallest
shape that still lets `/check` verify cadence, register runs, source links, and delta chains.

### Phase 5: Retune transcript segmentation

Current transcript cues average close to 3 seconds. Use cached word timings to test denser,
meaningful cuts without another API call.

Test configurations around:

- pause threshold: 0.22 to 0.25 seconds
- maximum cue duration: 3.0 to 3.2 seconds
- minimum fragment size: 2 words, with the existing fragment healer retained

Pick the configuration that reaches the target rhythm without creating one-word junk cues or
splitting names and scientific terms. Visual beats may still subdivide a cue when a planned
build requires it.

### Phase 6: Upgrade scene prompt generation

Update `/scenes` so it:

1. Assigns register, shot, render tier, plate, and delta before writing prose.
2. Creates base plates before variants.
3. Tells the user which prior image to attach for each variant.
4. Preserves camera axis, object positions, cast identity, palette, and line hierarchy across
   a chain.
5. Enforces one information change per beat.
6. Plans chapter colors, motif callbacks, researcher receipts, and ending reuse.
7. Reports generation economics: new plates, variants, callbacks, CapCut-only beats, and hero
   frames.

### Phase 7: Extend validation

Add mechanical checks for:

- V1 or V2 style-string coverage, never mixed inside one project.
- Background-family totals equal prompt totals.
- Render-tier totals equal prompt totals.
- ATMOSPHERIC does not exceed 10 percent.
- Cobalt does not exceed 10 percent and is used only for literal mind interiors.
- Pure white stays near the 8 percent target rather than becoming the default.
- No register run exceeds three beats unless all beats share one plate and form a valid build.
- 5 to 8 valid build chains in a 10 to 12 minute episode.
- Every variant points to an earlier base or variant source.
- Every variant names exactly one planned delta.
- No ordinary hold exceeds 4 seconds.
- Overall rhythm lands between 28 and 32 beats per minute.
- Text colors and word counts follow the V2 text system.
- Every callback resolves to an earlier plate and changes meaning.
- Prompt count, timestamp order, cast tokens, file naming, and project layout still pass existing
  checks.

### Phase 8: Roll out to future projects

1. Apply V2 to the next new episode, not retroactively to published projects.
2. Generate the hook first and review it before generating the body.
3. Generate all base plates before their variants.
4. Review one contact sheet per chapter for register and palette drift.
5. Run `/check` before importing prompts and after scene files are generated.
6. Publish three V2 videos before making another large art-direction change.
7. Compare analytics against the last three V1 uploads.

## Files expected to change after approval

| File | Planned change |
| --- | --- |
| `.agents/rules/visual-style.md` | add the V2 art direction, palette, render tiers, registers, shot grammar, background budget, and current style strings |
| `.agents/rules/house-rules.md` | document V1 and V2 style-string authority without allowing stray copies |
| `.agents/rules/file-formats.md` | define the lean visual-beat plan only if it becomes a saved artifact |
| `.agents/rules/mascot-toss.md` | add V2 line hierarchy and compatibility rules without changing Toss identity |
| `.agents/bin/style-strings.sh` | export legacy and current scene strings safely |
| `.agents/skills/cast/SKILL.md` | produce V2-ready character sheets for new projects |
| `.agents/skills/scenes/SKILL.md` | add register, shot, tier, plate, variant, motif, and cadence planning |
| `.agents/skills/scenes/references/memory.md` | record the accepted pilot settings and generation failures |
| `.agents/skills/transcript/SKILL.md` | expose the approved dense-cue profile and reporting |
| `tools/tsfmt.py` | change only if the existing flags cannot produce clean dense cues |
| `.agents/skills/check/SKILL.md` | validate V1 and V2 projects plus cadence and variant integrity |
| `.agents/skills/check/references/memory.md` | document style-version and pilot regression behavior |

Potential pilot artifacts, created only after approval, should live under a new research folder
and must not modify project 1.

## Safe choices and deliberate risks

### Safe choices

- Keep Toss, orange, cobalt, hand-drawn 2D, clear diagrams, and mobile readability.
- Keep text sparse and semantic.
- Keep flat illustration as the base language.
- Keep old projects frozen and version the new style.
- Pilot on existing narration before changing the pipeline.

### Deliberate risks

#### Risk 1: End the majority-white rule

Gain: stronger chapter identity, higher colorfulness, fewer repeated-slide contact sheets.

Cost: a real chance of returning to the dark, ugly failure that project 2 exposed.

Mitigation: use light cream and pastel tints, cap cobalt, allow only one near-dark reveal, and
measure every contact sheet.

#### Risk 2: Allow controlled depth tools

Gain: scenes feel illustrated and atmospheric rather than like isolated stickers.

Cost: gradients, texture, shadow, and blur can quickly drift into generic generated art.

Mitigation: permit them only inside named render tiers, cap ATMOSPHERIC at 10 percent, and ban
photorealistic materials, 3D volume, and unrestricted surface texture.

#### Risk 3: Raise visual-beat density

Gain: the image keeps advancing with the narration and the hook feels expensive.

Cost: more planning, more variant management, more render review, and more CapCut edits.

Mitigation: generate fewer unique base plates, use delta variants, reuse callbacks, and count
CapCut reframes as beats when they create a real new focal event.

#### Risk 4: Give secondary characters more specificity

Gain: better story scenes, historical credibility, and more emotional attachment.

Cost: cast drift and a weaker mascot hierarchy.

Mitigation: keep faces simple, lock silhouettes and props in reference sheets, and reserve the
most detailed design for recurring characters only.

## What will not be copied

- PastTense character designs, narrator avatar, exact palettes, composition assets, or text
  treatments.
- Their arithmetic errors, probability assumptions, modern political borders on prehistoric
  maps, capitalization drift, or inconsistent number formatting.
- Constant texture, constant glow, constant blur, fake film grain, or uncontrolled painterly
  rendering.
- Detailed environments that do not explain place, mechanism, status, or emotion.
- High beat density created from meaningless mouth shapes, blinks, or camera jitter.
- A style change used as an excuse to ignore topic, title, thumbnail, and script promise.

## Approval defaults

Approving this plan means approving these defaults unless the owner edits them first:

1. Art direction: Warm Editorial Storybook Doodle.
2. Pure white is no longer the majority background.
3. CLEAN, LAYERED, and capped ATMOSPHERIC render tiers are allowed.
4. Whole-video target is 28 to 32 meaningful visual beats per minute.
5. V1 remains valid for legacy projects. V2 applies only to future projects.
6. The first implementation deliverable is a controlled visual pilot, not a bulk rewrite.
7. Project 5's current uncommitted changes remain untouched.
8. Thumbnail rendering and channel topic strategy are out of scope for the first V2 rollout.

## Approval gate

Implementation starts only after the owner replies that this plan is approved, or edits this
file and asks for the revised version to be implemented.

After approval, the next work item is **Phase 1: build the controlled visual pilot**.
