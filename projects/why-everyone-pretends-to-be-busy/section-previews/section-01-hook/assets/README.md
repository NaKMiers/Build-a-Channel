# Shared Video Assets

Video:
`Why Everyone Pretends To Be Busy`

Purpose:
this is the single shared asset library for this video.

## Rule

All section preview projects should read media from this folder.

HyperFrames expects each project to have a local `./assets` path, so local `assets` folders inside preview projects should be junction pointers to this folder.

Do not create copied asset folders inside:

- `hyperframes/assets`
- `section-previews/<section>/assets`

Instead, keep each `hyperframes.json` asset path as:

- `"assets": "assets"`

Then make that local `assets` path a junction to this video-level folder.

## Layout

- `section-01-hook/`: Section 1 images and source notes
- `section-02-reframe/`: Section 2 images and source notes
- `section-03-busy-status/`: Section 3 images and source notes
- `voiceover/`: section voice preview files used by HyperFrames
- `wit/`: WIT pose PNGs used by this video
- `ATTRIBUTION.md`: video-level attribution and source summary

Section-specific one-off assets should stay under their section folder.
Reusable channel-wide assets belong in `.agents/_shared/assets/`, not here.
