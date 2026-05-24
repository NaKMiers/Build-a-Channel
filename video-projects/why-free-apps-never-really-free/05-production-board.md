# 05 Production Board

Status: `full board rough cut v1 ready for review`

This board converts the detailed visual storyboard into a practical Remotion production plan.

Do not render a full new cut until:

- this board is approved
- a voice test is generated
- timing is checked against the target runtime

## Production Decision

Use one reusable Remotion system with:

- `8` macro-scenes
- `64` first-pass micro-beats
- reusable visual components
- voiceover-driven timing
- simple graphics with frequent small changes

Working rule:

`Simple style, many beats.`

## Runtime Guardrail

Target runtime:

`3:00-4:00`

Current script length:

`about 745 words`

Risk:
the script may exceed `4:00` depending on narrator pacing.

Production rule:

If the voice test suggests the video will exceed `4:00`, trim the script before building the full rough cut.
Do not stretch scenes just to fit a long voiceover.

## Build Order

1. Create a voice test using the first `45-60` seconds of script.
2. Confirm narrator voice and pacing.
3. Estimate full runtime from the voice test.
4. Trim script if needed.
5. Create Remotion scene data from this production board.
6. Generate full voiceover.
7. Build a `45-60s` visual prototype from the first section. `Done: 45s prototype rendered`
8. Review the prototype for style, density, and pacing. `Current`
9. Build reusable components for the full rough cut.
10. Run timing pass from actual audio durations.
11. Render rough cut.
12. Review rough cut before polishing.

## Prototype Rule

Before building the full `3:59.91` video, create a `45-60s` visual prototype.

Purpose:

- confirm the visual language
- test Wit on screen
- check whether micro-beats feel alive enough
- confirm that text is readable
- avoid spending time implementing a full cut in the wrong style

Recommended prototype range:

- start: `free-gifts`
- continue into the beginning of `pricing-reframe`

This should cover:

- app gifts
- suspicious free offer
- hidden invoice
- first appearance of the pricing reframe

## Prototype Result

Rendered:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-45s.mp4
```

Revised render:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-45s-v2.mp4
```

WIT Core 12 opening test:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-10s-wit-opening.mp4
```

WIT Core 12 opening v2:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-10s-wit-opening-v2.mp4
```

WIT Core 12 opening v3:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-10s-wit-opening-v3.mp4
```

Board opening v1:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-10s-board-opening-v1.mp4
```

Board opening 30s v1:

```text
video-projects/why-free-apps-never-really-free/renders/prototype-first-30s-board-opening-v1.mp4
```

Full board rough cut v1:

```text
video-projects/why-free-apps-never-really-free/renders/full-board-rough-cut-v1.mp4
```

Details:

- composition: `WhyItWorksPrototype`
- runtime: `45s`
- frame range: `0-1349` at `30fps`
- source scenes: `free-gifts` and the beginning of `pricing-reframe`
- voice: existing `George` scene voiceovers

Caveat:
the prototype is cut at exactly `45s`, so it may end during the second scene rather than on a fully natural sentence.
ElevenLabs quota was exhausted, so a newly shortened custom prototype voiceover was not generated.

Revision note:
`v2` keeps the same simple style but adds more sequential visual reveals in the first two scenes before any full rough cut work.

WIT opening note:
the `10s` WIT Core 12 test uses a dedicated Remotion composition, `WhyFreeAppsWitOpening10`, to test whether the opening feels more alive when WIT changes poses and the screen is staged as fast visual beats instead of a large text/card layout.

V2 note:
the revised `10s` pass removes internal test labels, aligns app-example cards to the spoken `Free video / Free maps / Free messaging` list, varies the layout across stages, and uses WIT poses based on context rather than as generic decoration.

V3 note:
the latest `10s` pass keeps the v2 timing and WIT pose logic but moves the opening closer to the channel's handwritten visual language. It uses handwritten-looking labels, a scribble underline, cleaner stage transitions, and a small `zero dollars*` joke while preventing the app-example cards from cluttering the organizer/language beat.

Board opening v1 note:
after reviewing `analysis.md`, the active `10s` composition was restarted from scratch as a simple board-based opening. It uses four hard-cut boards: title, free phone, red correction, and late invoice. The goal is to match the Casually Explained reference grammar: static drawing, handwritten text, red markup, one joke per board, and WIT as a reaction anchor instead of a constantly moving actor.

Board opening 30s v1 note:
the next pass expands the same board grammar to the first `30s` of the script. It uses the full `free-gifts` voiceover plus the beginning of `pricing-reframe`, enlarges WIT so he reads as a real screen anchor, and removes the early invoice-late board because that joke does not arrive in the audio before the 30s cut ends.

Full board rough cut v1 note:
the full script now has a dedicated Remotion composition, `WhyFreeAppsFullBoardRoughCut`. It uses the existing eight George scene voiceovers, simple handwritten board scenes, WIT pose anchors, short crossfade/paper-sweep transitions, and a total runtime of `3:59.98`.

## Remotion Data Model

Use data instead of hardcoding every beat.

Recommended shape:

```ts
type VideoProject = {
  id: string;
  title: string;
  targetRuntimeSeconds: [number, number];
  scenes: MacroScene[];
};

type MacroScene = {
  id: string;
  label: string;
  narration: string;
  visualSystem: string;
  beats: MicroBeat[];
};

type MicroBeat = {
  id: string;
  cue: string;
  text?: string;
  action: string;
  wit?: "none" | "neutral" | "suspicious" | "deadpan" | "pulled" | "tangled";
  priority: "must" | "nice";
  timing: {
    startPercent: number;
    endPercent?: number;
  };
};
```

Reason:
macro-scene duration can follow voiceover length, while micro-beats are placed as percentages inside the scene.

This keeps timing adjustable after the real audio exists.

## Scene Data Plan

| Scene ID | Label | Visual System | Target Share | Micro-Beats | Main Job |
|---|---|---|---:|---:|---|
| `free-gifts` | Suspicious Free Gifts | Free gifts and hidden invoice | 12% | 10 | Hook the viewer and establish the contradiction. |
| `pricing-reframe` | Free Is Pricing | Free door and hidden checkout | 13% | 12 | Reframe free as easier entry, not no cost. |
| `attention-ads` | Attention Becomes Inventory | Attention factory | 18% | 15 | Explain ads and retention clearly. |
| `behavior-habit` | Apps Train Behavior | Habit loop | 15% | 13 | Show routine and repeated behavior. |
| `freemium-pain` | Freemium Sells Relief | Free path vs premium path | 16% | 14 | Explain paid relief from friction. |
| `lock-in` | Leaving Gets Annoying | Cables and dependency | 14% | 14 | Show why paying can become easier than leaving. |
| `label-stack` | Not Always The Product | Label stack | 7% | 8 | Summarize the different ways users create value. |
| `hidden-checkout` | Payoff | Hidden checkout reveal | 5% | 15 | Deliver the final thesis and outro. |

Target share is a starting estimate only.
Actual scene lengths should follow voiceover duration.

## Scene Data Result

Created:

```text
remotion-studio/src/data/why-free-apps-never-really-free.json
```

Result:

- macro-scenes: `8`
- first-pass micro-beats: `64`
- voiceover IDs match generated MP3 filenames
- Remotion still render check passed

Reason for `64` instead of around `100`:
the first production pass should prioritize strong visual beats that are realistic to implement.
More micro-beats can be added after the rough cut reveals where the screen feels too static.

## Macro-Scene Production Notes

### 1. `free-gifts`

Narration range:
opening through `very suspicious business plan`.

Must show:

- phone drops in
- generic free app gifts fall in
- `STREAK!` notification joke
- split between progress and invoice
- Wit becomes suspicious

Reusable components:

- `PhoneFrame`
- `AppGift`
- `Wit`
- `ReceiptTie`
- `SplitSuspicion`

### 2. `pricing-reframe`

Narration range:
`Because normally...` through `financial future later`.

Must show:

- gift boxes becoming an invoice
- software icons fading into a pricing system
- `no cost` vs `easy entry`
- `FREE` door removing friction
- hidden checkout waiting in the back

Reusable components:

- `FreeDoor`
- `PriceTag`
- `HiddenCheckout`
- `Wit`
- `ReceiptTie`

### 3. `attention-ads`

Narration range:
`So if free apps...` through `scalable business model`.

Must show:

- ad card
- scrolling feed
- attention eye
- minutes turning into ad boxes
- retention meter
- inventory shelf
- `20 min later` joke

Reusable components:

- `PhoneFrame`
- `AdCard`
- `AttentionFactory`
- `Timer`
- `InventoryShelf`
- `WitDeadpan`

### 4. `behavior-habit`

Narration range:
`But ads are only...` through `charging you gets much easier`.

Must show:

- `ADS` as level 1
- attention becoming behavior
- habit loop
- open, feed, tap, streak, repeat
- notification pulling Wit
- checkout moving closer

Reusable components:

- `HabitLoop`
- `NotificationBubble`
- `WitPulled`
- `ReceiptTie`
- `MovingCheckout`

### 5. `freemium-pain`

Narration range:
`That is why freemium...` through `tiny landlord`.

Must show:

- free vs premium paths
- locked feature block
- ads/limits/delay on free path
- repeated `PAY` beat
- artificial limit at `99%`
- `$9/mo`
- app becoming tiny landlord

Reusable components:

- `FreemiumGate`
- `PremiumPath`
- `ProgressLimit`
- `PayButton`
- `WitSuspicious`

### 6. `lock-in`

Narration range:
`Then there is the long game...` through `business model gets very smooth`.

Must show:

- lock-in title
- phone growing cables
- photos/files/playlists/friends/habits attach
- uninstall button moves away
- moving house joke
- annoying exit path vs smooth pay path

Reusable components:

- `LockInCables`
- `UninstallButton`
- `MovingBoxes`
- `PayInsteadPath`
- `WitTangled`

### 7. `label-stack`

Narration range:
`So when people say...` through `modern feelings available`.

Must show:

- `you are the product` quote gets stamped `not the whole story`
- labels stack: product, future customer, trained behavior, free user
- six tiny subscriptions pile up
- deadpan pause

Reusable components:

- `LabelStack`
- `SubscriptionCards`
- `WitDeadpan`

### 8. `hidden-checkout`

Narration range:
`The point is not...` through outro.

Must show:

- not fake / useful
- gift becomes strategy
- less friction, scale, habit
- payment pipes: money, attention, behavior, dependence
- checkout disappears from front
- hidden checkout reveal behind `FREE`
- final `WHY IT WORKS` end card

Reusable components:

- `StrategyBoard`
- `PaymentPipes`
- `HiddenCheckout`
- `EndCard`
- `Wit`

## Component Priority

Build these first:

1. `Wit`
2. `ReceiptTie`
3. `PhoneFrame`
4. `AppGift`
5. `HiddenCheckout`
6. `AttentionFactory`
7. `HabitLoop`
8. `FreemiumGate`
9. `LockInCables`
10. `LabelStack`
11. `EndCard`

Reason:
these components cover most scenes and can become reusable for future videos.

## Voiceover Plan

Current default voice:

`George`

Status:

`experiment, not locked`

Voice test:

- generate only the opening through `financial future later`
- check runtime, pronunciation, warmth, and dry humor
- estimate full runtime from words per second

Pacing target:

- calm
- dry
- conversational
- not trailer voice
- slight pause after punchlines

If too slow:

- trim script first
- then adjust voice settings

If too flat:

- try one alternate narrator before committing to full production

## Scene Timing Plan

Before audio:

- use target share percentages
- use micro-beat `startPercent`
- keep all timings editable

After audio:

- calculate each macro-scene duration from its voiceover file
- add a small buffer of `0.3-0.6s`
- align micro-beats to voice cues by percentage
- manually adjust punchline beats where needed

Do not set final timing until the full voiceover exists.

## Output Paths

Planning source:

```text
video-projects/why-free-apps-never-really-free/
```

Future Remotion scene data:

```text
remotion-studio/src/data/why-free-apps-never-really-free.json
```

Future voiceover:

```text
video-projects/why-free-apps-never-really-free/voiceover/
```

Current Remotion voiceover compatibility path:

```text
remotion-studio/public/voiceover/why-free-apps-never-really-free/
```

Future renders:

```text
video-projects/why-free-apps-never-really-free/renders/
```

Current Remotion output compatibility path:

```text
remotion-studio/out/
```

## Rough Cut Standard

The first new rough cut should prove:

- the hook works visually within 5 seconds
- visual beats change often enough
- Wit supports the idea without taking over
- the hidden checkout metaphor is clear
- text is readable
- the narrator pace fits the video
- runtime stays close to `3-4 minutes`

It does not need:

- final thumbnail
- final sound design
- perfect character animation
- perfect transitions
- music bed

## QA Checklist

- [ ] Script runtime is tested before full render
- [ ] Scene data follows the approved storyboard
- [ ] All real app logos are avoided
- [ ] On-screen text stays short
- [ ] Macro-scenes are not static slides
- [ ] Micro-beats are frequent but not chaotic
- [ ] Wit appears moderately, not constantly
- [ ] Receipt tie grows as hidden cost increases
- [ ] Final payoff matches thumbnail promise
- [ ] Rough cut is reviewed before polish

## Next Step

Step 10 should be:

`Voice Test`

Recommended test section:

from:

`Here's the fun part about modern life`

through:

`We'll discuss your financial future later.`

Decision after the test:

- keep George and continue
- adjust voice settings
- try another narrator
- trim the script before production
