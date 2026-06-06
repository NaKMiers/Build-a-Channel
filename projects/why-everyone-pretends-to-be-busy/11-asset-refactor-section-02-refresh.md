# 11 Asset Refactor And Section 02 Refresh

Video:
`Why Everyone Pretends To Be Busy`

Classification:
`Operational lesson`

Status:
`implemented`

## Decision

Use one video-level asset library:

```text
projects/why-everyone-pretends-to-be-busy/assets
```

All section preview projects should expose this folder through a local `assets` junction, because HyperFrames validates `./assets` next to each project.

## Why

The previous structure duplicated media across:

- `assets/`
- `hyperframes/assets/`
- `section-previews/<section>/assets` junctions

That made it unclear which folder was the source of truth and made Section 2 accidentally reuse Section 1 images.

## Implementation

- Copied WIT pose PNGs and voiceover MP3 files into the video-level `assets` folder.
- Kept each `hyperframes.json` asset path as `assets` for HyperFrames compatibility.
- Replaced copied local asset folders with junctions to the video-level shared asset library.
- Added local `.gitignore` files so asset junctions and HyperFrames thumbnail caches do not get staged as duplicate files.
- Replaced Section 2's repeated Section 1 photo references with Section 2 generated images.
- Added Section 2 source notes at `assets/section-02-reframe/source-notes.md`.
- Added refreshed still-frame evidence at `renders/section02-refreshed-frames/`.
- Added refreshed contact sheet at `renders/section02-refreshed-contact-sheet.jpg`.

## Verification

Commands:

```powershell
npm run check
```

Passed in:

- `hyperframes/`
- `section-previews/section-01-hook/`
- `section-previews/section-02-reframe/`

Result:

- no validation errors
- no console errors
- `0` layout issues in all three projects

Known warnings:

- duplicate media discovery warnings from repeated static board images
- dense track warnings because each section is still kept inline for review simplicity

## Rule Going Forward

For this video:

```text
one section preview project, one port, one index.html, one shared video asset library
```

Do not copy media into section preview folders.
Do not recreate `hyperframes/assets` as a real folder unless the final assembly workflow explicitly needs a packaged export copy.
