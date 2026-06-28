# Section 3 Render Implementation (v2 - generate-forward rebuild)

Video: `Why The Internet Is Full Of Garbage Now`
Section: `Section 3: What Slop Actually Is`
Status: `built (v2 from scratch), ready for review`

> v2 rebuild (owner-directed 2026-06-28): v1 over-reused `grey-sludge-flood` and leaned on old browsed
> photos. v2 throws out the sludge for this section and is GENERATE-FORWARD: 10 bespoke generated heroes
> + 7 fresh real bases + 9 transparent WIT poses. The SLOP MACHINE replaces sludge as the section motif.

## Result

- Preview project: `section-previews/section-03-what-slop-actually-is/`
- Composition: `Section03Slop` (1920x1080, 40.704s)
- Port: `1003` - Studio: `http://localhost:1003/#project/section-03-what-slop-actually-is`
- Audio: `section-03.mp3` (am_eric / 0.80)
- Source: `visual-plan/section-03-what-slop-actually-is/...-visual-plan.md` (v2) + real word timings

## Scenes (9, pinned to word timings)

| Scene | Start | Voice cue (word @ s) | Base (real photo) | Hero (generated) | WIT (side/pose) |
|---|---:|---|---|---|---|
| 3.1 | 0.00 | "three things" @1.98 | factory-interior | slop-machine | right / announcing |
| 3.2 | 2.96 | "looks fine" @3.74; "half a second" @4.36 | studio-backdrop | ai-influencer-perfect (post card) | left / delighted |
| 3.3 | 6.80 | "falls apart" @7.60; "six fingers" @9.00 | studio-backdrop (decayed) | ai-influencer-melting (glitch card) + red circle | right / panic |
| 3.4 | 9.80 | "gibberish" @10.44 | night-storefront | gibberish-melting-sign (card) | left / confused shrug |
| 3.5 | 11.10 | "holiday ad" @12.92; "Coca-Cola" @15.54; "really happened" @16.62 | holiday-street | coca-coola-ad-fail (card) + red circle | right / howling laugh |
| 3.6 | 17.48 | "almost nothing" @18.88; "costs you everything" @20.40; time/attn/trust @23.28/24.00/25.10 | server-room | cost-crush-pile (clocks/hearts avalanche, radial-masked) | bottom / crushed (X-eyes) |
| 3.7 | 25.94 | "made by the thousand" @26.70; "10,000" @29.24; "fire hose" @32.34 | pipes-industrial | slop-firehose (multiply) + 8 slop-clone post tiles | center-right / shocked |
| 3.8 | 33.22 | checks @33.48/34.20/34.66; "that is slop" @35.96 | factory-interior (callback) | slop-machine (reuse) + certified-slop-stamp (multiply slam) | right / smug |
| 3.9 | 37.26 | "a person" @38.80; "full volume" @39.78 | dark-stage-mic | robot-human-mask (screen blend) + VU meter to MAX | bottom-left / deadpan (dwarfed) |

## Compositing techniques (heroes came on white/grey/black, not all transparent)

- `.post` white card frame: white-bg AI heroes presented AS social posts/ads (influencer perfect+melting, gibberish sign, coca-coola ad) - the white reads as the post, on-concept.
- `.ink` (mix-blend-mode:multiply): red/grey ink heroes on white drop their white bg over the base (certified-slop-stamp, slop-firehose).
- `.clonetile`: each slop-clone in a tiny white post card, clustered as a spray = literal "10,000 identical fake posts" (multiply made the bare clones vanish on the busy pipe base; tiles read far better).
- `.lit` (mix-blend-mode:screen + bottom mask): the black-bg robot drops its black onto the dark stage; the mask crops the source watermark.
- `.pile` (radial mask): the grey-bg crush pile fades its rectangular edges so the avalanche blends onto the server room.

## Render Review-Prevention Pass

- voice cue map: built from `voiceover/section-03-what-slop-actually-is/section-03-word-timings.json` (whisper-tiny.en)
- generate-forward: 10 bespoke generated heroes (no recycled sludge crutch); each scene a distinct bold concept
- contrast: bright bases dimmed (b-dim) for big-text scenes; big words yellow + dark outline; cards/marks/chips have own backgrounds
- WIT: one per scene, varied side/scale/pose/emotion; faces uncropped (verified in snapshot)
- safety: "Coca-Coola" is a generic parody can/santa (no real Coca-Cola logo); AI influencer is a non-existent person
- HyperFrames mechanics: per-scene tracks, audio clip, deterministic GSAP, registered timeline `Section03Slop`

## Verification

- lint: 0 errors (warnings: `duplicate_media_discovery_risk` from the intended slop-clone tile reuse)
- validate: 0 errors; WCAG contrast warnings are false positives (dark-on-white card text + shadowed tags the checker ignores text-shadow on; same pattern S1/S2 passed)
- snapshots: 9-frame contact sheet -> `snapshots/contact-sheet.jpg`; scenes 6 + 7 re-snapped after polish
- export: not requested (preview only)

## Post-snapshot polish

- 3.7: switched bare-multiply clones (invisible on busy pipes) to white `.clonetile` post tiles + added 2 more (8 total) - the fake-post torrent now reads.
- 3.6: raised the crushed WIT into frame (bottom -330) and repositioned time/attention/trust onto the lower pile so none clip.

## Notes

- Poses copied directly from the transparent library (no chroma-key step).
- Manual-edit preservation: if the owner edits this `index.html` in Studio, treat it as canonical next run.
