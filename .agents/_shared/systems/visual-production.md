# Visual Production System

Classification: `Core production system`

Scope: `CHANNEL_WIDE`

Use this file for reference boards, real-life visual assets, UI mockups, WIT use, scene grammar, visual humor, and HyperFrames board checks.

## Core Rule

Static drawing -> narration twist -> red markup or hard cut -> next static drawing.

Start simple. Make paused frames clear before adding motion.

## Visual Plan Handoff Rule

Visual planning is the critical handoff into HyperFrames.

For each section, the visual plan must answer:

- what appears on screen
- when it appears against the voiceover
- how it moves, cuts, reveals, or changes
- why it holds attention
- what assets or references HyperFrames needs

The renderer should not need to invent the main scene, timing, joke, object, asset list, or reference logic.

## One-Board Contract

Each board should carry:

- one thought
- one joke or evidence object
- one WIT reaction or real-life object
- one readable label
- one clean timing beat

If a board needs three explanations, it is probably three boards.

## Board Types

Use these repeatedly:

- Situation board: show the normal thing.
- Suspicion board: reveal the weird detail.
- Correction board: cross out the naive explanation.
- Mechanism board: show how the system works.
- Evidence board: show concrete object, number, or example.
- Reaction board: let WIT show how it feels.
- Payoff board: make the final insight visible.

## Motion Rule

Use hard cuts by default.

Add motion only when it has a job:

- reveal
- emphasis
- joke timing
- visual cause/effect
- helping the viewer follow a change

Do not animate labels, props, WIT, and transitions all at once unless the user has approved the static frame.

Sequential timing does not mean every block should animate. Ordinary labels, notes, and supporting props can simply hard-show on the spoken beat. Reserve smash, stamp, snap, shake, or pop motion for true emphasis beats: prices, contradiction labels, proof marks, and payoff phrases.

## Reference Board Rule

Before full visual production, ask:

`What does this topic look like in real life, and what would make it funny if paused?`

Every normal section visual plan should include a real visual reference pass. Start with real internet images, self-shot images, or inspected local assets whenever the topic has real-world objects. Use generated images after that to fill gaps, create safer controllable mockups, remove logos/private data, or test composition. Prompt-only references are a fallback only when browsing, generation, or local inspection is unavailable, fails, or would create unsafe assets.

Good reference boards collect:

- real-life objects
- real internet/self-shot/local images that make the video feel close to the viewer
- UI patterns or self-made mockups
- visual metaphors
- thumbnail tension
- WIT emotion
- color and contrast references
- source notes

References must be classified:

- safe asset
- mockup target
- inspiration only
- reject

Do not copy another creator's exact frame, thumbnail, screenshot, or joke layout.

## Real-Life Asset Rule

Use real-life assets as evidence, not decoration.

Prefer:

- self-shot images
- licensed or public-domain images
- real internet images with clear source and license notes
- generated images for support, cleanup, or missing-safe-asset cases
- self-made UI mockups
- simple object cutouts
- paper, receipts, bills, phones, desks, product boxes

Avoid:

- private data
- unclear copyrighted images
- pixel-copied app screens
- real logos used to imply endorsement or a fake claim, or pixel-copied private screenshots

Standing technique (owner-approved 2026-06-22): real recognizable UI is a PREFERRED illustration
device - phone/iPhone mockups, real app icons (Gmail, Messenger, To Do, Google Calendar, etc.), and
app/notification/chat screens - whenever the script depicts those actual apps/products/screens. Build
them in CSS with real icon PNGs (from Wikimedia Commons), used editorially. See `brand-system.md` →
"Real-UI Illustration."
- generic stock images that do not explain the point

Channel-wide reusable assets should be rare and high-value. Most video-specific assets belong inside `projects/<slug>/assets/`.

Real background behind EVERY scene, including UI scenes (owner-confirmed 2026-06-22). A section
made of full-frame CSS UI / labels on flat gradients reads as "no background / not lively" and gets
sent back. Every scene - even a real-UI scene (Meet grid, chat, Trello, spreadsheet, calendar) or a
stylized one - must sit on a REAL, people-free photo. Float the crisp UI as a drop-shadowed `.screen`
over a real desk/office photo (with a light scrim), and prefer a photo that literally echoes the line
(empty meeting room for "this meeting could've been a message", sticky-note wall for "overloaded",
real theater curtain for "the star of the show", a packed calendar app for "a calendar with Wi-Fi").
"Hands at a keyboard" photos are fine (no-face rule allows hands). Keep adjacent scene bases distinct.

## Visual Humor Patterns

Use a small set per video:

- red cross-out
- bad arrow
- fake diagram
- real object with stupid label
- WIT physically suffering
- hidden thing revealed behind clean thing
- list that gets more absurd
- tiny legal footnote
- suspicious asterisk
- impossible receipt
- progress bar of bad decisions

Do not throw every pattern into one video.

## Animated Interactive UI Mockup (owner-confirmed 2026-06-30)

A high-impact device the owner specifically loves and asked to use across future videos: instead of a
static screenshot, make the UI PERFORM the action. Reach for it whenever a beat depicts using an
app/site or asks the viewer to DO something (subscribe/like/share, tap, toggle, search, buy, swipe,
fill a form, watch a number move).

- The kit: a drawn SVG mouse cursor (or a tap-ripple) that moves and clicks; buttons that boing/wiggle
  and FLIP STATE (SUBSCRIBE->SUBSCRIBED, Like turns blue, a toggle slides on); counters/badges that
  tick; progress bars that fill; toasts + confetti on the click.
- Sync: pin every click and state-change to the real word-timings, exactly like any other reveal.
- Build: CSS/SVG, on a single continuous scene so the card holds its final state. Use SVG/CSS icons +
  an SVG cursor, NEVER emoji glyphs (they don't render in the snapshot Chromium). Namespace decorative
  classes (confetti/particles) so they don't collide with structural icon parts.
- Honesty + safety: parody UI with our own / editorially-approved branding (e.g. "WhyTube", "Why It
  Works") - never a real screen-grab, never a real channel/person, and NO fake inflated metrics (use a
  non-numeric line like "Subscribe for more" -> "Welcome to the channel!" and a humble tick).
- Proven reference: the `5-why-the-internet-is-full-of-ai-slop` Section 8 subscribe-popup outro. Treat
  it as a go-to for CTAs, "how it works" demos, before/after toggles, and any tap/scroll/click beat;
  reserve it for beats that genuinely depict interaction (don't force it onto every scene). Pairs with
  the standing Real-UI Illustration preference.

## WIT Use

Use `.agents/_shared/channel/brand-system.md` for the current WIT direction.

WIT is useful when:

- the system needs a human victim
- the board needs emotional clarity
- the joke needs a dry reaction
- a thumbnail needs instant feeling

WIT should not block labels or replace the explanation. The reverse also matters: if WIT is the emotional subject, labels, payoff tags, stamps, and cards must not cover WIT's face, eyes, mouth, or key prop.

When WIT appears, treat it as the emotional subject of the beat, not a small corner sticker. For strong emotional beats, WIT can occupy roughly `1/3` to `1/2` of the frame when it does not cover labels or evidence. Prefer goofy, readable poses such as panic, facepalm, suspicion, betrayal, confusion, shock, or defeated reactions over neutral filler poses.

WIT size + vertical anchor (owner-confirmed 2026-06-22). Two complementary defaults the owner asked for:
- **Big (default to GIANT)**: the owner has repeatedly said "I love giant WIT", so default to the LARGE end - about `1/2` of the frame (giant), not a cautious `1/3`. A small WIT reads as a sticker. If a bigger WIT would cover a label, board, chat bubble, or other content, RE-ARRANGE the other items (move them to the opposite side / up / down) rather than shrinking or lowering WIT. WIT is the emotional subject; the supporting content makes room for it. (Concrete sizing that worked at 1920x1080: side-anchored WIT `width ~1340–1380`, centered WIT `width ~1140`.)
- **High**: do NOT anchor a bottom-edge WIT so low that only the head peeks (e.g. CSS `bottom:-540…-600px` bled most of the body off-canvas and the owner said it looked "too low / covered by the frame"). Anchor higher (`bottom ≈ -250…-340px`, even for a giant figure) so head + glasses + torso + arms sit inside the frame and only the legs crop. Verify in a snapshot that the head is comfortably inside the top edge too.

Do not overuse WIT. WIT is emotional punctuation, not a reaction requirement for every cue. For short sections, start with about `1-2` WIT beats per persistent big scene, then adjust based on voice rhythm. Let labels, props, and markup carry explanatory beats between WIT moments.

WIT crop guard:

- face, head, shoulders, and important props should not look accidentally cut off
- intentional edge peeks are fine only when the expression still reads clearly
- payoff text/stamps/cards should not sit on top of WIT's face or expression; create separate text and WIT zones
- if no approved pose fits the beat, create or request a new approved WIT pose in shared/project assets instead of forcing a weak pose

## Subtitle-Safe Lower Area

YouTube subtitles can cover elements placed too close to the bottom edge.

Plan and render with a small subtitle-safe margin:

- important labels, receipts, stamps, arrows, boxes, and payoff props should usually sit a bit above the bottom edge
- do not put cue-critical text in the lower subtitle zone just because the frame has empty space there
- only background or nonessential decorative elements should live very close to the bottom edge
- when WIT rises from the bottom edge, keep the emotional read clear while moving nearby text and props upward into the safe zone

## HyperFrames Board Guidance

Use:

- simple HTML/CSS scenes
- stable board dimensions
- large readable text
- handwritten-looking fonts or rough labels
- hard cuts
- cue-timed popups only when needed
- cue-timed hard-shows for ordinary labels

Check:

- text fits on desktop and mobile review sizes
- labels are readable when paused
- WIT emotion is visible at small size
- real-life assets are not muddy or decorative
- cue-critical elements are readable on the cue frame, not only starting animation there
- WIT-heavy frames have safe crop and readable emotion in runtime screenshots/contact sheets
- final/payoff frames preserve WIT emotion: text can support the rhythm, but it must not cover WIT's face/expression

## Short Hook Simplicity Rule

For a `20-30s` hook, start with about `3` persistent big scenes and `6-8` cue states/static boards:

- one real-life image or object
- one WIT reaction
- one main label
- hard cuts

Do not add transition overlays, rapid pop-ins, object pile-ons, or WIT shake unless the static version is approved and the motion has a clear joke or clarity job.

For connected object hooks, keep the same base scene while the voice describes the same object or situation. Add one or two voice-timed cue elements inside that scene instead of cutting to a new full-screen board for every sentence.

## Vivid Hook Template (owner-confirmed 2026-06-23)

The approved `why-everything-is-a-subscription-now` Section 1 remake is the standing template for vivid
sections (and the bar to match for new sections). Three rules:

- VIVID ON-TOPIC OBJECT BASES: dramatize the line with concrete brand/people-free objects (money/coins/cash,
  padlocks, glowing screens), not mundane desks/hands. If clean topical photos are scarce, use a strong
  object + CSS real-UI. Keep each scene's base distinct.
- VARIED IDEA-DEVICES (not one repeated label box): vary how each idea is shown - app-grid tiles, a kinetic
  number/counter, notification toasts, a free-trial countdown, a full-width system/EXPIRED banner, a padlock
  wall, bold kinetic headline type, badges, a chat bubble, a stamp. Reserve the handwritten cream label for
  the occasional aside.
- GIANT, VARIED WIT: WIT is the soul of each scene - keep it giant (~1/2 frame) with an expressive on-topic
  pose, and VARY it across scenes in side (left/center/right), scale, vertical anchor, and pose. Never park
  WIT on the same side every scene with text always opposite; flip the text/UI to the side WIT isn't using
  and rearrange items around WIT. (Current WIT poses are TRANSPARENT RGBA cutouts as of 2026-06-28 - composite them directly; no chroma-key step.)
