# HumanPrice Visual Style

Read this file before writing character, scene, or thumbnail prompts.

## Identity

HumanPrice is a cinematic 2D editorial explainer. Images make invisible prices,
incentives, and behavioral pressure visible through ordinary people and familiar
transactions.

Use this exact style string in every image prompt:

`cinematic 2D editorial illustration, clean bold charcoal outlines, simplified expressive human characters, tactile paper texture, soft directional lighting, restrained depth, clear visual hierarchy, 16:9 composition`

Use this exact generation string in every image prompt:

`match the attached character reference exactly, preserve the named plate composition for variants, keep saturated Toss blue reserved for the recurring protagonist or one semantic diagram signal, use olive and terracotta only for HumanPrice economic meaning, no photorealism, no 3D render, no CGI, no realistic faces, no anime style`

The style string and generation string must appear verbatim. The scripts in
`.agents/bin/style-strings.sh` expose the canonical copies.

## Palette

- Toss blue `#2E77C4`: permanent master brand color across every channel, recurring
  protagonist, trust, and one important diagram signal.
- Olive green `#6F7D3C`: HumanPrice choices, systems, and positive economic emphasis.
- Terracotta `#C86B3C`: HumanPrice prices, friction, urgency, and human cost.
- Warm cream `#F5EBD8`: default ground and breathing space.
- Charcoal `#252522`: outlines, type-like marks, and structural contrast.
- Muted gold `#D5A84B`: money and value.
- Dusty teal `#4F8580` and muted blue `#6883A3`: supporting information only.
- Muted red `#B84F43`: loss, warning, or negative movement only.

Toss blue is the cross-channel visual-style anchor. Use it prominently in recurring
characters, scene accents, diagrams, and thumbnail focal points, but do not turn generic
crowds or whole backgrounds uniformly blue. Olive and terracotta are HumanPrice semantic
accents, not replacements for the master style color. Logo and banner design are separate
from this rule and do not need to be regenerated when a channel adopts the style.

## Surface families

Choose one surface family per base plate:

1. Warm cream editorial card.
2. Light olive system card.
3. Light terracotta pressure card.
4. Illustrated real-world environment.
5. Pure white evidence card.

Do not change surface family inside a build chain.

## Density tiers

- `CLEAN`, about 40 percent: one focal action and one supporting object.
- `LAYERED`, about 50 percent: one focal action plus two to four explanatory elements.
- `ATMOSPHERIC`, at most 10 percent: a richer environment used only for emotional turns.

## Registers

- `STORY`: a person making or feeling a decision.
- `CARD`: one claim, comparison, or definition.
- `DIAGRAM`: a mechanism, feedback loop, or flow.
- `TRANSACTION`: money, receipt, price, subscription, bill, or exchange.
- `PORTRAIT`: an emotional reaction or identity consequence.
- `HYBRID`: character plus a legible economic mechanism.
- `SPLIT_OR_SCALE`: before/after, individual/system, or small/large contrast.

Each scene prompt must name its register, tier, and surface family.

## Frame grammar

- One frame makes one claim.
- Start with a readable human action, then reveal the mechanism around it.
- Use receipts, price tags, coins, carts, phones, homes, clocks, and energy bars as
  recurring economic symbols. They are symbols, not mascots.
- Show causality spatially: arrows, queues, funnels, layers, scales, or repeated units.
- Avoid decorative charts. Every chart or number must advance the narration.
- Keep faces and hands readable on a phone screen.
- Leave intentional negative space for visual emphasis and optional thumbnail copy.
- Never rely on generated text for factual labels. Use short symbolic marks or add text
  during editing.

## Pacing for an 8 to 12 minute video

Target 180 to 320 visual states, including build variants.

- First 15 seconds: 42 to 55 visual states per minute.
- 15 to 45 seconds: 34 to 44 per minute.
- Mechanism sections: 26 to 32 per minute.
- Dense evidence: 22 to 26 per minute.
- Ending: 24 to 28 per minute.

Use 4 to 7 build chains. A chain reuses one locked base plate and adds or removes one
meaningful element per variant. Separate chains with `---` as specified in
`image-generation.md`.

## Prohibited defaults

- No photorealism, glossy 3D, stock-photo staging, or corporate vector art.
- No floating icon soup.
- No wall of numbers.
- No literal coin character or brand mascot.
- No random palette shifts between neighboring frames.
- No copied competitor compositions.
