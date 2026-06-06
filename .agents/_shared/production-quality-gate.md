# Production Quality Gate

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
prevent future `Why It Works` videos from entering full production when the topic angle, package, hook, humor, motif, visual identity, voice, or learner clarity is not strong enough.

This is a reusable channel-wide gate. It does not audit or approve any existing video by itself.

## Core Rule

Do not produce in this order:

```text
script -> full render -> thumbnail
```

Use this order:

```text
angle -> package -> hook -> motif -> script -> board plan -> prototype -> full render
```

The video must earn production time before production starts.

## Pass/Fail System

Most gates have three possible decisions:

```text
PASS: continue to the next gate
FIX: revise the weak area, then review this gate again
FAIL: stop and restart from the last strong strategic choice
```

Gate 0 also allows:

```text
EXPERIMENT: continue only with explicit user approval and a clear reason for testing a lower-confidence angle
```

Use this score scale when a numeric decision helps:

```text
90-100: Strong. Continue.
80-89: Pass with minor notes.
70-79: Fix before continuing.
0-69: Fail. Do not continue.
```

Hard fails override the score.

## Hard Fail Rules

A future video must stop if any of these are true:

- the title is generic
- the thumbnail has no curiosity tension
- WIT is neutral, decorative, or emotionally unclear
- the first `10` seconds do not pay off the title-thumbnail promise
- the topic angle scores under `30/40` without explicit experiment approval
- the topic angle has no contradiction, repeated visual metaphor, WIT role, or real-life object
- the topic only feels educational, with no real-life pressure or contradiction
- the script sounds like a lesson instead of a person explaining a weird system
- a section has no visual joke, real-life texture, or WIT reaction
- the rough cut has long clean-board stretches with no reason to keep watching
- the voice, captions, or labels are not learner-friendly
- copyrighted, copied, unclear, private, or unsafe assets are required

## Gate Order

| Gate | Required Before | Main Question | Decision |
| --- | --- | --- | --- |
| 0. Topic Angle | Research, packaging, scripting | Is this a sharp, visual, creator-led angle instead of a broad topic? | `PASS / FIX / FAIL / EXPERIMENT` |
| 1. Packaging | Scripting | Would a stranger click this for a reason beyond education? | `PASS / FIX / FAIL` |
| 2. Hook | Script lock | Does the first `10` seconds prove the package? | `PASS / FIX / FAIL` |
| 3. Motif | Full script | Does the video have a repeatable visual idea? | `PASS / FIX / FAIL` |
| 4. Script | Voiceover | Is every section clear, funny, and non-generic? | `PASS / FIX / FAIL` |
| 5. Visual Board | Animation/render | Does every board carry one thought and one visual job? | `PASS / FIX / FAIL` |
| 6. Prototype | Full render | Does the first `30-60` seconds feel like a real upload? | `PASS / FIX / FAIL` |
| 7. Full Cut Review | Final polish | Does the full rough cut hold attention and stay readable? | `PASS / FIX / FAIL` |
| 8. Upload Review | Upload | Is the final package safe, clear, and aligned? | `PASS / FIX / FAIL` |
| 9. Post-Upload Review | Next video | What should change in the next video? | `LESSON / NO SIGNAL` |

## Gate 0: Topic Angle

Required before research, packaging, or scripting:

```text
[ ] raw topic has been turned into a sharp angle
[ ] main contradiction
[ ] recurring metaphor
[ ] thumbnail tension
[ ] first 10 second situation
[ ] WIT emotional role
[ ] real-life object or UI evidence options
[ ] final insight
[ ] topic angle score
```

Pass criteria:

- score is at least `30/40`
- `Curiosity`, `Visual motif`, `Explanation depth`, and `Packaging strength` are each at least `3/5`
- the angle creates a thumbnail image immediately
- the angle supports at least `5` visual jokes
- the angle gives WIT a job
- no hard-fail rejection rule is triggered

Use:

- [topic-angle-selection-system.md](topic-angle-selection-system.md)
- [topic-angle-scorecard.md](topic-angle-scorecard.md)

## Gate 1: Packaging

Required before scripting:

```text
[ ] final or near-final title
[ ] thumbnail concept
[ ] first 10 second promise
[ ] recurring visual motif candidate
[ ] dominant object or situation
[ ] clear WIT emotion
```

Pass criteria:

- thumbnail creates curiosity
- title is specific, simple, and not generic
- title and thumbnail do not repeat the same information
- WIT has a strong emotion
- the concept is not only educational
- the first `10` seconds can pay off the package

Use:

- [thumbnail-packaging-system.md](thumbnail-packaging-system.md)
- [packaging-scorecard.md](packaging-scorecard.md)
- [hook-system.md](hook-system.md)

## Gate 2: Hook

Required before full script lock:

```text
[ ] first 10 second board plan
[ ] hook narration
[ ] visible contradiction
[ ] WIT reaction
[ ] no-audio clarity check
[ ] mobile readability check
```

Pass criteria:

- topic is clear without audio by second `3`
- contradiction appears by second `5`
- WIT's emotional position is clear by second `8`
- viewer has a reason to continue by second `10`
- opening is a situation, not an introduction

Hard fail:
the first board is only a title card, branding moment, or abstract definition.

## Gate 3: Motif

Required before full script:

```text
[ ] one recurring visual motif
[ ] motif appears in the hook
[ ] motif can return in at least 3 sections
[ ] motif supports both explanation and jokes
[ ] motif works at mobile size
```

Good motif examples:

- receipt keeps printing
- app keeps adding small charges
- progress bar moves backward
- WIT gets buried under labels
- fake dashboard exposes the real rule
- red marker keeps correcting the promise

Pass criteria:

- motif gives the video a visual spine
- motif is simple enough for HyperFrames production
- motif can create at least one joke and one insight
- motif does not require unsafe copyrighted material

## Gate 4: Script

Required before voiceover:

```text
[ ] one main metaphor
[ ] one repeated phrase
[ ] one visual joke per section
[ ] learner-friendly clarity pass
[ ] ending insight
[ ] voice markup for timing and deadpan beats
```

Pass criteria:

- each section has explanation and visual joke
- each section has a clear boardable idea
- the ending lands a real insight
- no section sounds like a generic lesson
- useful English is natural, not classroom-like
- jokes work from context, not only obscure slang

Use:

- [script-tone-system.md](script-tone-system.md)
- [voice/script-markup-guide.md](voice/script-markup-guide.md)
- [voice/narration-system.md](voice/narration-system.md)

## Gate 5: Visual Board

Required before animation or render:

```text
[ ] board list
[ ] WIT role per board
[ ] real-life asset per section where useful
[ ] timing cues
[ ] on-screen labels
[ ] red markup purpose
[ ] source notes for non-original assets
```

Pass criteria:

- one thought per board
- no overloaded screens
- real-life texture appears regularly
- red markup has a purpose
- WIT is doing a job, not filling space
- each board has joke value, evidence value, or transition value

Use:

- [scene-grammar-system.md](scene-grammar-system.md)
- [visual-humor-patterns.md](visual-humor-patterns.md)
- [real-life-visual-asset-system.md](real-life-visual-asset-system.md)
- [hyperframes/board-grammar.md](hyperframes/board-grammar.md)

## Gate 6: Prototype

Required before full render:

```text
[ ] first 30-60 seconds rendered
[ ] thumbnail mockup visible beside or reviewed against the prototype
[ ] voice test synced
[ ] captions or key labels visible
[ ] no-audio first 10 seconds check
[ ] mobile-size check
```

Pass criteria:

- first `10` seconds are strong
- WIT is funny or useful
- voice sounds deadpan enough
- visuals are not too clean or generic
- captions and labels are readable
- the title-thumbnail promise appears in the opening
- the prototype feels like `Why It Works`, not a school slide deck

Hard fail:
do not continue to full render if the prototype only proves that the explanation is understandable. It must also prove click tension, visual identity, and watchability.

## Gate 7: Full Cut Review

Required before final polish:

```text
[ ] full rough cut
[ ] paused-frame review
[ ] mobile readability check
[ ] audio clarity check
[ ] hook-to-ending promise check
[ ] section-by-section retention check
```

Pass criteria:

- every `5-10` seconds has a reason to watch
- every section has a visual idea
- no long dead clean-board stretches
- WIT has multiple memorable reactions
- real-life assets or real-looking evidence appear where useful
- final insight is memorable
- narration remains the clearest layer

Use:

- [audio-mixing-checklist.md](audio-mixing-checklist.md)
- [final-review-checklist.md](final-review-checklist.md)

## Gate 8: Upload Review

Required before upload:

```text
[ ] final title
[ ] final thumbnail
[ ] final render
[ ] final captions or readable on-screen text
[ ] source and licensing check
[ ] no-copycat reference check
[ ] final learner-friendly pass
```

Pass criteria:

- title and thumbnail match
- first `10` seconds pays off the thumbnail
- WIT has memorable reactions
- real-life assets appear where useful
- music supports, not dominates
- video remains learner-friendly
- no copied reference material
- no unsafe copyrighted assets

## Gate 9: Post-Upload Review

Required after future upload, when analytics or qualitative feedback are available:

```text
[ ] post-upload review created from [post-upload-review-template.md](post-upload-review-template.md)
[ ] available metrics recorded
[ ] qualitative signals recorded if metrics are too small
[ ] CTR diagnosis completed
[ ] first 30s retention diagnosis completed
[ ] mid-video retention diagnosis completed
[ ] comment/confusion diagnosis completed
[ ] production effort diagnosis completed
[ ] lessons labeled High / Medium / Low confidence
[ ] at least one next-video rule written, or `No reusable lesson yet` recorded
```

Use:

- [publishing-feedback-loop.md](publishing-feedback-loop.md)
- [post-upload-review-template.md](post-upload-review-template.md)
- [channel-learning-rules.md](channel-learning-rules.md)

Decision options:

```text
LESSON: one or more reusable next-video rules found
NO SIGNAL: not enough evidence yet; keep current channel system
```

Hard fail:
do not rewrite channel foundation from one upload without explicit user confirmation.

## Review Record Template

Use this template in future per-video work only after a video project is explicitly active.

```text
Production quality gate review

Video:
Date:
Reviewer:

Gate 0 Topic Angle: PASS / FIX / FAIL / EXPERIMENT
Score:
Notes:

Gate 1 Packaging: PASS / FIX / FAIL
Notes:

Gate 2 Hook: PASS / FIX / FAIL
Notes:

Gate 3 Motif: PASS / FIX / FAIL
Notes:

Gate 4 Script: PASS / FIX / FAIL
Notes:

Gate 5 Visual Board: PASS / FIX / FAIL
Notes:

Gate 6 Prototype: PASS / FIX / FAIL
Notes:

Gate 7 Full Cut Review: PASS / FIX / FAIL
Notes:

Gate 8 Upload Review: PASS / FIX / FAIL
Notes:

Gate 9 Post-Upload Review: LESSON / NO SIGNAL
Next-video rules:

Final decision:
PASS / FIX / FAIL

Required fixes before next step:
1.
2.
3.
```

## Final Standard

A `Why It Works` video is not ready because it is technically finished.

It is ready when the package creates curiosity, the hook proves the promise, the script explains one weird system clearly, WIT gives the viewer an emotional shortcut, the boards stay readable, and the final cut feels simple, funny, dry, and worth watching.
