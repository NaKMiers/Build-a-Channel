# Section 3 What Slop Actually Is - Design (v2 generate-forward)

Composition: `Section03Slop` (1920x1080, 40.704s). Audio: `section-03.mp3` (am_eric / 0.80).

## Look
- Channel grammar: a distinct vivid base per scene + a bespoke GENERATED hero + giant varied transparent WIT + handwritten labels. No recycled base as a crutch.
- Defines slop in 3 marks: (1) looks flawless then GLITCHES/melts - the perfect AI influencer becomes a six-finger meltdown; gibberish neon sign; the "Coca-Coola" holiday-ad fail; (2) costs the maker nothing but CRUSHES you - a clock/eyeball/heart avalanche flattens WIT; (3) made by the thousand - a firehose spraying identical fake-post clones. Verdict: a "CERTIFIED SLOP" stamp, then the killer button - a chrome robot holding a human mask, screaming at full volume.
- NEW section motif (replaces sludge): THE SLOP MACHINE - a grotesque content-grinder that opens (3.1) and stamps the section shut (3.8).

## Timing
All reveals pinned to real word timings (`../../voiceover/section-03-what-slop-actually-is/section-03-word-timings.json`).

## Assets
Shared library via `./assets` junction; poses are transparent cutouts in `assets/poses/` (library pre-keyed).
- Generated heroes (10): slop-machine, ai-influencer-perfect, ai-influencer-melting, gibberish-melting-sign, coca-coola-ad-fail, cost-crush-pile, slop-firehose, slop-clone, certified-slop-stamp, robot-human-mask.
- Fresh real bases (7): factory-interior, studio-backdrop, night-storefront, holiday-street, server-room, pipes-industrial, dark-stage-mic.
- Compositing: white-bg heroes framed as `.post` cards (on-concept "posts/ads"); stamp + firehose via `multiply`; the black-bg robot via `screen` on the dark stage; the grey-bg crush pile radial-masked; clones as white post tiles.
- CSS-only: hazard sign, mark cards, the maker chip, red tell-circles, check rows, "COSTS YOU EVERYTHING" / "AT FULL VOLUME" big words, "10,000+" counter, VU meter.
- Safety: "Coca-Coola" is generic parody (no real logo); the AI influencer is a non-existent person.
