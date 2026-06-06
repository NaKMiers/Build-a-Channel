# Video Creation Pipeline

Use this workflow for every long-form `Why It Works` video.

## Steps

1. Idea selection
2. Topic score
3. Research brief
4. Video structure
5. Script draft
6. Script revision
7. Packaging
8. Visual plan
9. Production board
10. Voice test
11. Rough cut
12. Review pass
13. Final cut
14. Shorts extraction
15. Post-upload review

## Rule

Do not produce before the idea, script, and packaging are strong.

Production starts only after:

- script is approved
- packaging is approved
- visual plan is approved
- production board is ready

## Visual Density Rule

A short video still needs many visual beats.

For `3-4 minute` explainers, do not treat each section as one static scene.
Plan:

- macro-scenes: the main explanation sections
- micro-scenes: the smaller screen changes, reactions, labels, transitions, and visual jokes inside each section

Working rule:

`Simple style, many beats.`

## Handwritten Text Rule

Every long-form video should default to handwritten-looking text for:

- labels
- arrows
- cross-outs
- corrections
- joke punchlines
- useful English phrases

Use HyperFrames to render the handwritten style through CSS text, SVG text, rough underline/cross-out shapes, or exported hand-drawn text images.

Working rule:

`Handwritten text is the main visual language.`

## HyperFrames Production Rule

New production should happen in:

```text
projects/<slug>/hyperframes/
```

Each HyperFrames video needs:

- `DESIGN.md`
- `index.html`
- local audio/assets in `assets/`
- `npm run check` before review
- rendered MP4s in `projects/<slug>/renders/`

## Per-Video Storage

All work for a video belongs in:

```text
projects/<slug>/
```

Use the numbered files there to preserve decisions.
