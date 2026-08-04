# scene-polish - memory

Validate before any rename. A mismatched count, non-contiguous numbered sequence, existing timestamp file, or root-level collision means no rename occurs.

Never use directory listing order. Map `1_2k.jpg` through `N_2k.jpg` to prompt timestamps in order only after the range check passes.

Move only timestamp-named JPG files. Refuse to move when a range has another entry, two folders have the same name, or `scenes/` already has that name.

The completed `scenes/` folder must have exactly one timestamp-named JPG per `image-prompts.md` timestamp, with no extras or duplicate timestamps.

Scene image names use `[M-SS].jpg`, never `[M:SS].jpg`, because Windows forbids `:` in
file names. The migration command must check every destination before renaming.

## Range folders carry the same Windows constraint (2026-08-03, project 5)

A range folder cannot contain `:` either. Project 5's folders are `0.00 - 7.03` and
`7.07 - 13.49`, dot separated. The script built the folder name from the endpoints with
colons only, so every `check-range` on that project failed with "Missing scene range
folder" before it read a single image. `range_folder()` now tries `:`, `.`, and `-` and
prints the names it tried plus the folders actually present. Project 3's `6:45 - 9:57`
and `10:01 - 12:04` are empty leftovers from the colon era, not a live convention.

The download tool also emitted one `132_2k.jpeg` among 277 `_2k.jpg` files, which the
numbered pattern counted as an unexpected entry and failed the range on. `NUMBERED` now
accepts both extensions. The rename always writes `.jpg`, so this normalises itself.

## A batch boundary can silently drop one prompt

Project 5 was generated in two batches, folders labelled `0.00 - 7.03` and `7.07 - 13.49`.
The first folder holds 145 images but its labelled range covers 146 prompts: its content
actually stops at `[7:01]`, and `[7:03]` was never generated. The second batch started at
`[7:07]`. The prompt on the boundary fell through the gap between the two runs.

**A folder name is a claim, not evidence.** Check the count against the prompts in the
labelled range every time. When they disagree by one, find out *where* before renaming:
a gap anywhere but the end shifts every image after it and renames them all wrong.

Locating the gap does not need all N images opened. The V1 background tone map is a
fingerprint: build the index-to-background list from `image-prompts.md`, then read images
only at the colour-block boundaries and bisect. Project 5 took six image reads to prove
images 1 through 145 were unshifted and the missing frame was the last one. Colour blocks
alone bracketed it to nine white prompts; the final step compared the named delta in each
prompt against the checklist drawn in the image.

## Project 6 (2026-08-03), 303 images in 4 batches, clean end to end

Folders `0.00 - 2.58`, `3.02 - 6.11`, `6.14 - 8.46`, `8.48 - 11.34`, dot separated like project 5,
so `range_folder()`'s dot support carried it with no edits. 81 + 81 + 65 + 76 equals 303, all four
`check-range` calls PASS, `move` flattened 303 files and removed 4 folders, `verify` PASS with zero
missing, extra, duplicate, or unexpected entries.

### Add one pre-rename test: prompts that fall BETWEEN two labelled ranges

Project 5's dropped `[7:03]` would not be caught by per-range checks even today. Each folder can
match the count of prompts inside its own label while a prompt sitting in the gap between two labels
was never generated at all, and every `check-range` still says PASS. Only `verify`, after all the
renames, reports it. The cheap test is one pass over the prompt timestamps:

```python
between = [t for t in ts if sec(prev_end) < sec(t) < sec(next_start)]   # must be empty
```

Project 6 returned empty for all three seams. Run this before the first `rename-range`, not after.

### V2 has no tone map, so use the text and the motif as the alignment fingerprint

Project 5's bisect recipe leans on the V1 background colour blocks. V2 frames are warm cream, tinted
chapter cards, story environments, and cobalt interiors, which do not partition the timeline the way
the V1 tone map did. What does fingerprint a V2 frame is the exact one-to-five-word on-screen text
and the episode motif, both named in `image-prompts.md` and in `visual-plan.md`'s Text and Motif
columns.

**When every folder's count matches its label, three image reads are enough**: the first image of the
first batch, one distinctive frame partway into a different batch, and the last image of the last
batch. An intra-folder shift cannot happen without changing that folder's count, so the only
remaining risk is a whole batch being mislabelled or swapped, which a probe in a second folder
rules out. Project 6 used `[0:00]` SIX O'CLOCK, `[7:28]` the Hadza establishing shot, and `[11:34]`
the full battery over Toss beside the dead one on the phone.

### The generator leaves a watermark in the bottom-right corner of every frame

Every sampled project 6 image carries a pale four-pointed sparkle in the bottom-right corner, the
image model's own watermark, at roughly 60 px on a 1376 px wide frame. It survives into `scenes/`
and has to be cropped or covered in the edit, and a crop costs frame edge on a 16:9 timeline.

Sampling is cheap and worth doing once per episode, because a corner artifact is easy to miss when
reviewing full frames:

```python
crops=[Image.open(S+n).crop((w-150,h-150,w,h)) for n in sample]   # paste into one contact sheet
```

Report it to the owner as an edit-stage task. It is not a file-management fault and no rename or
move fixes it.

### Shell note: this repo's shell is zsh, which does not word-split unquoted parameters

`for r in "3:02 6:11" ...; do set -- $r; script "$1" "$2"; done` passes empty arguments in zsh and
the tool exits on "requires START and END". Run the range commands as separate lines, or use
`${=r}`. One operation at a time is the skill's rule anyway.

## Project 5 (2026-08-05), V2, 293 images in 2 batches, clean end to end

Folders `0.00 - 4.03` and `4.06 - 10.59`, dot separated like the earlier V2 runs, so `range_folder()`
dot support carried it with no edits. 110 + 183 equals 293, both `check-range` calls PASS, `move`
flattened 293 files and removed 2 folders, `verify` PASS with zero missing, extra, duplicate, or
unexpected entries. No prompt sat in the gap between the labels (`[4:03] < sec < [4:06]` was empty).

The downloader now emits `N_I_2k.jpg` (with an `_I` infix) on every image, not the legacy `N_2k.jpg`.
The old `NUMBERED` regex `^(\d+)_2k\.jpe?g$` rejected every file in the folder as "Unexpected entries"
and failed the range on. The regex was loosened to `^(\d+)(?:_I)?_2k\.jpe?g$` so it accepts both
shapes; the rename always writes `.jpg` so this normalises itself. Project 4 still uses the old
`N_2k.jpg` and project 6 uses `_I_2k.jpg` - the new regex matches both.

Three V2 fingerprint frames confirmed the two batches are not mislabelled: `[0:00]` is the theater
with @CROWD standing around @YOU still seated, `[7:32]` is the cream "10,000 LIKES" heart card, and
`[10:59]` is the calm seated ending with @YOU composed inside the applauding @CROWD. None of the
project 5 frames sampled show the corner watermark that hit project 6.
