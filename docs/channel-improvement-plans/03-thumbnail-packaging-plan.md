# Plan 03: Thumbnail And Packaging

Classification:
`Core channel upgrade plan`

Goal:
create a channel-wide thumbnail and packaging system that makes every future video create curiosity before the viewer clicks.

Scope:
`CHANNEL_WIDE`

Execution contract:
Follow `00-channel-core-upgrade-contract.md`. This plan upgrades the reusable title, thumbnail, and packaging system for the entire channel. It must not create packaging for any specific video.

Allowed outputs:

- `common/thumbnail-packaging-system.md`
- `common/thumbnail-templates/`
- `common/packaging-scorecard.md`
- `docs/branding/thumbnail-visual-rules.md`

Forbidden outputs:

- no edits to `video-projects/<slug>/03-packaging.md`
- no final title or thumbnail for any existing video project

## Problem

The current packaging is clear, but may not be clickable enough.

Weaknesses:

- Titles can sound familiar.
- Thumbnail text can be too generic.
- Images may explain the topic without creating a question.
- WIT may not show a strong enough emotional reaction.
- The thumbnail can feel clean instead of suspicious, funny, or weird.

## Target

A strong `Why It Works` thumbnail should make the viewer ask:

`What is going on here?`

It should not merely answer:

`What is the video about?`

## Thumbnail Formula

Use this default formula:

`one real object + one contradiction + one WIT emotion + one short label`

Examples:

- phone + hidden checkout + betrayed WIT + `FREE?`
- wallet + leaking bills + tired WIT + `BROKE?`
- productivity checklist + trapped WIT + `FIXED?`
- cheap product + hidden downgrade + suspicious WIT + `CHEAP?`

## Title Formula

Good title types:

- `Why X Is Not Really Y`
- `Why X Feels So Y`
- `The Hidden Cost Of X`
- `How X Quietly Became Y`
- `Why X Keeps Getting Worse`

Avoid titles that sound like generic finance or productivity advice.

Weak:

`How A System Makes Money`

Better:

`Why This "Free" Thing Is Not Really Free`

Even better if supported by thumbnail:

`The Hidden Checkout Behind "Free"`

## Thumbnail Rules

- Use `1-3` words max.
- Use one dominant object.
- Use strong color contrast.
- Make WIT's emotion obvious.
- Make the contradiction visible without reading the title.
- Prefer real or real-looking objects over clean icons.
- Avoid too many labels.
- Avoid logo clutter.
- Avoid generic locks unless the video is specifically about lock-in.

## Packaging Workflow

Before scripting:

1. Generate `10` title ideas.
2. Generate `5` thumbnail concepts.
3. Pick the strongest title-thumbnail pair.
4. Write the first `10` seconds to satisfy the thumbnail promise.
5. Define the recurring visual motif.
6. Reject concepts that are clear but boring.

Before production:

1. Make a rough thumbnail mockup.
2. Shrink it to mobile size.
3. Check whether the curiosity remains.
4. Compare it beside reference thumbnails.
5. Rewrite title if thumbnail and title repeat the same information.

## Acceptance Criteria

Packaging is ready only if:

- A stranger can understand the topic in `1` second.
- A stranger still has a question after understanding the topic.
- WIT has a strong emotion.
- The image has a visual contradiction.
- The title and thumbnail do not say the exact same thing.
- The first `10` seconds pays off the thumbnail promise.

## Red Flags

- The thumbnail looks like a clean presentation slide.
- The text explains everything.
- WIT looks neutral.
- The title could belong to any finance explainer channel.
- There is no weird object, hidden threat, or visual tension.

## Do Not Do

- Do not use fake claims.
- Do not make rage bait.
- Do not copy specific Casually Explained thumbnails.
- Do not use copyrighted brand logos unless there is a clear safe-use reason.

## Session Prompt For Future Codex

```text
Scope: CHANNEL_WIDE.
Read docs/channel-improvement-plans/03-thumbnail-packaging-plan.md.
Create or update the channel-wide thumbnail and packaging system.
Allowed outputs are common/thumbnail-packaging-system.md, common/thumbnail-templates/, and docs/branding/.
Do not edit video-projects.
Do not create title or thumbnail options for one specific video unless I explicitly ask.
```
