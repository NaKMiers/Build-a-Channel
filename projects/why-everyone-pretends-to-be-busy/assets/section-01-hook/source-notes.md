# Section 01 Hook Asset Source Notes

Video: `Why Everyone Pretends To Be Busy`

Section: `01 Hook`

Purpose:
add real-world texture in the spirit of `Casually Explained`, where simple drawings and labels are supported by recognizable real-life objects.

## Local Real-World Assets

### `real-world/home-office-laptop-real-cc0.jpg`

Classification:
`real-world photo / primary production asset`

Page:
https://commons.wikimedia.org/wiki/File:Home-office-336377.jpg

Source:
Pixabay, hosted on Wikimedia Commons.

Observed license:
`Creative Commons CC0 1.0 Universal Public Domain Dedication`

Safe-use decision:
`safe to use and crop`

Production crops:

- `real-world/home-office-laptop-desk-crop-real-cc0.jpg`
- `real-world/phone-laptop-desk-crop-real-cc0.jpg`

Recommended Section 1 uses:

| Board | Use |
|---|---|
| `hook-real-work-desk` | real desk/laptop opening background |
| `hook-fake-emergency-stack` | real phone/laptop desk crop with fictional notification overlays |
| `hook-looking-busy` | return to real desk/laptop background with fake busyness overlays |

### `real-world/desk-laptop-calculator-real-cc0.jpg`

Classification:
`real-world photo / backup production asset`

Page:
https://commons.wikimedia.org/wiki/File:Desktop_with_laptop_and_calculator_(Unsplash).jpg

Source:
Unsplash pre-2017 CC0 import, hosted on Wikimedia Commons.

Observed license:
`Creative Commons CC0 1.0 Universal Public Domain Dedication`

Safe-use decision:
`safe to use and crop`

Recommended use:
backup calm desk texture if the primary home-office photo feels too warm or too recognizable as a laptop product shot.

### `real-world/wall-calendar-real.jpg`

Classification:
`real-world photo / restricted crop-only production asset`

Page:
https://commons.wikimedia.org/wiki/File:WMDE_Event_Wall_Calendar.jpg

Source:
Own work by `Arjunaraoc`, hosted on Wikimedia Commons.

Observed license:
`Creative Commons Attribution-ShareAlike 3.0 Unported`

Safe-use decision:
`use only if attribution/share-alike requirements are acceptable for the final project`

Restriction:
the original photo contains a visible person. Do not use the full image in the video.

Production crops:

- `real-world/wall-calendar-cropped-no-person-real-cc-by-sa.jpg`
- `real-world/wall-calendar-board-crop-real-cc-by-sa.jpg`

Recommended Section 1 use:
calendar-wall texture for boards `hook-calendar-closes-in` and `hook-professional-badge`, with WIT and handwritten labels layered on top.

## Local Generated Support Assets

### `generated/section-01-real-world-reference-contact-sheet.png`

Classification:
`generated raster reference / fallback production texture candidate`

Created:
`2026-06-02`

Source:
AI-generated raster image created in this Codex session.

Prompt summary:
2x2 contact sheet showing:

- messy desk with laptop, coffee, sticky notes, and blank task card
- calendar/planner cage made from paper calendar and meeting cards
- smartphone with generic notification bubbles
- quiet task card surrounded by judgment arrows and sticky notes

Safe-use decision:
`safe to use as generated image or to crop into production textures, but prefer real-world assets above when possible`

Restrictions:

- do not treat any text in the image as final video text
- add channel handwritten labels in HyperFrames
- crop panels as needed instead of showing the full contact sheet unless the contact-sheet format is intentional
- do not add real app logos on top

Recommended Section 1 uses:

| Board | Use |
|---|---|
| `hook-real-work-desk` | fallback if real desk photos do not fit |
| `hook-calendar-closes-in` | fallback or composite layer if real calendar crop is too literal |
| `hook-fake-emergency-stack` | fallback or notification reference layer |
| `hook-quiet-thinking-judged` | generated support, because real photos rarely show judgment arrows cleanly |

Generated crop files:

| File | Use |
|---|---|
| `generated/desk-laptop-task-card-generated.png` | boards `1` and `8` desk/laptop texture |
| `generated/calendar-cage-generated.png` | boards `2` and `3` calendar pressure texture |
| `generated/phone-notifications-generated.png` | board `4` phone notification texture |
| `generated/quiet-task-judgment-generated.png` | boards `6` and `7` judgment/task-card texture |

## Web References Checked With gstack Browse

These were first discovered through gstack browse. Direct Wikimedia upload URLs initially returned `429 Too many requests`, but the files were later downloaded successfully through `Special:Redirect/file/...` with a proper user agent.

### `Desktop with laptop and calculator (Unsplash).jpg`

Page:
https://commons.wikimedia.org/wiki/File:Desktop_with_laptop_and_calculator_(Unsplash).jpg

Observed source/license:
Wikimedia Commons page states this file is from Unsplash, published before the 2017 Unsplash license change, and made available under `Creative Commons CC0 1.0 Universal Public Domain Dedication`.

Observed direct media URL:
https://upload.wikimedia.org/wikipedia/commons/2/23/Desktop_with_laptop_and_calculator_%28Unsplash%29.jpg

Use decision:
`safe reference candidate / retry download later`

Recommended use:
desk/laptop background texture for boards `1-3`.

### `Home-office-336377.jpg`

Page:
https://commons.wikimedia.org/wiki/File:Home-office-336377.jpg

Observed source/license:
Wikimedia Commons page states this file is from Pixabay and released under `Creative Commons CC0 1.0 Universal Public Domain Dedication`.

Observed direct media URL:
https://upload.wikimedia.org/wikipedia/commons/3/38/Home-office-336377.jpg

Use decision:
`safe reference candidate / retry download later`

Recommended use:
home-office/laptop real-world texture if the generated desk crop feels too artificial.

## Search Notes

`Unsplash` and `Pexels` search pages were blocked by bot/security protection in the headless browser, so they were not used for collection.

Wikimedia Commons search was usable for source discovery, but direct media downloads were rate-limited during this pass.

## Section 1 Asset Rule

The hook should mix:

```text
real-world raster texture + WIT + handwritten labels + red markup
```

It should not become:

```text
clean vector-only UI boards
```

The real-world image layer should act as evidence/texture, while WIT and handwritten labels carry the joke.
