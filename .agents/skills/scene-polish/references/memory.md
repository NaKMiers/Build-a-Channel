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
