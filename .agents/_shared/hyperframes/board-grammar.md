# HyperFrames Board Grammar

This is the channel-wide HyperFrames board grammar for `Why It Works`.

Use it when turning future visual plans into HyperFrames compositions. It defines the reusable board style, timing discipline, and paused-frame review rules. It does not create boards for any existing video project.

## Core Model

HyperFrames should act as a board compiler and timing layer.

Default pattern:

```text
static board
cue-timed label, underline, reveal, or red markup
hard cut
next static board
```

Use GSAP for timing and small emphasis. Do not use motion to compensate for weak board ideas.

## Board Unit

A board is one timed visual idea.

Each board should define:

- `id`: stable descriptive name
- `data-start`: board start time
- `data-duration`: board duration
- `data-board-type`: situation, suspicion, correction, mechanism, evidence, reaction, or payoff
- one visual anchor: WIT or real-life object
- one main label
- optional cue-timed emphasis

Example HTML shape:

```html
<section
  class="board board--correction"
  data-board-id="free-means-later"
  data-board-type="correction"
  data-start="12.40"
  data-duration="4.20"
>
  <img class="wit wit--suspicious" src="./assets/wit/suspicious.png" alt="" />
  <div class="label label--main">FREE*</div>
  <div class="red-crossout" data-cue="13.10"></div>
  <div class="label label--correction" data-cue="13.35">PAY LATER</div>
</section>
```

This is a grammar example, not a required framework.

## Naming Rules

Use names that describe the visual idea:

- `free-means-later`
- `attention-inventory`
- `subscription-receipt`
- `checkout-moved`
- `bad-advice-factory`

Avoid names tied only to script order:

- `scene-4`
- `board-b`
- `line-18`

Script-order names make review harder after timing changes.

## Board Types

Use these board types consistently:

| Type         | Job                                          |
| ------------ | -------------------------------------------- |
| `situation`  | show the recognizable normal thing           |
| `suspicion`  | reveal the weird detail                      |
| `correction` | cross out the obvious meaning and replace it |
| `mechanism`  | show how the system works                    |
| `evidence`   | show a real or real-looking object           |
| `reaction`   | let WIT carry the emotional beat             |
| `payoff`     | land the simple insight                      |

## Layer Order

Default layer order:

1. background
2. real-life object or diagram base
3. WIT
4. primary label
5. arrows, marks, underlines, cross-outs
6. tiny footnotes or secondary jokes

Marks and arrows should point at content, not cover the readable part of the content.

## Timing Rules

Use the voiceover as the timing source.

- Board cuts should land on spoken idea changes.
- Punchline labels should be readable on the spoken cue frame.
- Underlines and red marks should be visible at the cue, then finish drawing after it.
- One frame before the cue, the cue-critical element should not be readable yet.
- Do not start cue-critical popups at zero opacity or unreadably tiny scale on the cue frame.

If the viewer pauses exactly when the word is spoken, the visual should already make sense.

## Hard Cut Rules

Prefer hard cuts when:

- the narration changes idea
- a joke lands
- a correction replaces the old meaning
- the viewer should feel a sudden reframe

Use soft transitions only when:

- the idea is continuous
- the transition itself is the joke
- the board would otherwise feel visually jarring without adding clarity

## In-Board Motion

Allowed motion:

- red marker draw
- underline draw
- small label pop
- phone buzz
- receipt print
- tiny WIT shake
- simple reveal
- quick emphasis wiggle

Avoid:

- decorative floating
- constant object movement
- long slide transitions
- complex camera moves
- animation that keeps changing while the narration is explaining something dense
- cue-by-cue prop pile-ons in short hooks
- making labels appear and disappear rapidly just because related words are spoken
- adding transition overlays before the static board rhythm has been approved

For short Casually Explained-inspired sections, build the static-board version first:

```text
one real-life image + one WIT reaction + one main label + hard cut
```

Then add only the smallest motion needed for a joke or clarity fix.
If the static contact sheet feels good, do not add motion just to make the section feel more produced.

## Text Grammar

Text should behave like labels, not subtitles.

Default text budget:

- main label: `1-3` words
- secondary label: `1-4` words
- tiny footnote: one short phrase
- full sentence: rare, only for payoff boards

Good HyperFrames labels:

- `FREE*`
- `PAY LATER`
- `not a gift`
- `attention inventory`
- `monthly pain`
- `bad idea`

Bad labels:

- a full narration sentence
- generic labels like `important information`
- three equal-size phrases fighting for attention

## Board Density

For a connected idea, keep one board and cue timed labels inside it.

Split into a new board only when:

- the visual anchor changes
- the idea changes
- the joke changes
- the evidence object changes
- the viewer needs a clean pause between thoughts

Do not make every phrase a new board.

For a `20-30s` hook, a good first pass is often `6-8` static boards.
More cue-level visual events can make the section feel busy even when each event is individually timed correctly.

## Mobile Readability

A board must still work when viewed small.

Check:

- main label readable at mobile size
- WIT emotion recognizable
- real-life object not too tiny
- arrows and red marks visible
- no text touching frame edges
- no hair, props, or cards cropped accidentally

## Paused-Frame Review

For every rough cut, review paused frames before calling it ready.

Default method:

1. Pause every `5` seconds.
2. Name the frame's joke, contradiction, or evidence.
3. If the answer is `nothing`, revise the board.
4. Check whether any board is too clean.
5. Check whether the section has WIT doing a job or a real-life object proving the idea.
6. Check whether all cue-critical labels are readable on the spoken beat.
7. Check mobile readability for dense boards.

Pass criteria:

- one main idea
- visible joke or clear evidence
- WIT emotion matches the narration
- text is readable
- marks and arrows do not cover important text
- cut or emphasis lands on the spoken beat

Fail criteria:

- empty clean board
- decorative WIT
- abstract label with no visual anchor
- unreadable footnote
- punchline visible early
- motion without explanation or joke value

## DESIGN.md Checklist

Future HyperFrames `DESIGN.md` files should include:

- section-level board count
- dominant visual object per section
- chosen visual humor pattern per section
- WIT role per section
- real-life asset needs
- cue-critical words or phrases
- paused-frame review notes

This keeps the board grammar visible before `index.html` production starts.

## Render-Ready Checklist

Before rendering a future review cut:

- all boards have stable names
- board starts and durations match the voiceover
- cue-critical elements are readable on cue frames
- no board contains too many full sentences
- WIT is not decorative
- at least one meaningful real-life texture pass was considered
- paused-frame review has no empty frames
- `npm run check` passes or all remaining warnings are documented
