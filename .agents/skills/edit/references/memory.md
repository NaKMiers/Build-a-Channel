# edit - memory

The transcript is the only place the real cut time still exists. `prompts/image-prompts.md`
and the scene file names both carry the truncated `[M:SS]`, so never derive a cut from a
file name when `transcribes/transcript.md` is present.

MLT counts a clip as `out - in + 1` frames. A clip meant to last N frames has `in="0"` and
`out=` frame `N-1`. Getting this wrong shifts every cut after it by one frame per clip.

Kdenlive's timecode is `HH:MM:SS.mmm` and the milliseconds must be derived from the frame
(`round(frame * 1000 / fps)`), never the other way round, or a frame lands one off.

An image producer's `length` must cover its longest timeline use. Kdenlive's own default
is five seconds; a cue that holds longer needs a longer producer or the clip truncates.

The generated project is `<project>/edit/`, not `outputs/`. `outputs/` is published
packaging, and a `.kdenlive` file full of absolute machine paths is not that.

Verified against the hand-built `~/Videos/11.kdenlive`: same MLT structure, same profile,
same track layout. Cuts confirmed frame-exact by rendering through `melt` and hashing the
frames around each boundary.

Join the images to the cues **by position** against `prompts/image-prompts.md`, not by
matching the `[M:SS]` stamp. That file is where the scene file names came from, and its
stamps can disagree with `to_mss()` of the transcript in two ways that stamp matching
handles wrongly:

1. A rounded stamp. Project 14 wrote `[10:11]` for a line at `[10:10.980]` instead of
   truncating to `[10:10]`. Stamp matching stranded `[10-11].jpg` and dropped its cut.
2. A de-duplication bump. A legacy whole-second transcript can put two cues in the same
   second (`[2:49] Same farmer.` then `[2:49] Same field.`), so the prompt file bumped the
   later ones to `[2:50] [2:51] [2:52]`, shifting the run until it resynced. Those stamps
   are unique file names, not times.

Case 2 means several cues can share one transcript timestamp. Spread such a run evenly
across the second it shares. Stacking them on one frame produces one-frame clips, and
dropping the extras loses images the user rendered. A `[MM:SS.SSS]` transcript never hits
this, because every line has its own onset.

Fall back to stamp matching only when the prompt file is absent or its count does not
match the transcript's, and say so in the report.

Report every disagreement rather than silently reconciling it. A prompt stamp that drifted
is a real defect in `image-prompts.md`, and a missing scene image is a real gap in the
render, so both belong in the output the user reads.

## Four things Kdenlive requires that MLT does not

`melt` accepting a document proves nothing about Kdenlive accepting it. All four of these
parsed clean through MLT and still made Kdenlive report "Could not recover corrupted file"
and open an empty project:

1. **`xml_retain=1` on `main_bin`.** Without it MLT discards the bin playlist as an
   unreferenced producer, so Kdenlive loads a document with no bin at all.
2. **Every id must end in a number.** Kdenlive takes the integer off the end of each id,
   so `filterN`, `tractorN`, `producerN`, `playlistN`, `transitionN`, `chainN` only.
   `f_logo` or `tractor_project` is not a style difference, it is a document that will not
   open.
3. **No `<blank>`.** No project Kdenlive has written here contains one, so there is no
   format to copy. When the first cue starts late, hold the first image from frame zero
   instead. That also removes a black flash at the head of the video.
4. **`avformat`, never `avformat-novalidate`.** Novalidate means "do not probe this file,
   trust the properties given", and is only safe alongside the whole `meta.media.*` stream
   description Kdenlive writes with it. Supplying the service without the metadata builds
   the producer blind and the audio track never constructs.

## There is no offscreen way to test whether Kdenlive accepts a document

Four methods were tried and every one returns the same verdict for a known-good project as
for a broken one, so none can tell them apart:

- `timeout N kdenlive ...` inside the snap: `/usr/bin/timeout` is permission-denied there,
  so Kdenlive never runs and a grep over the empty output looks like success. This one is
  actively dangerous, it manufactures a false pass.
- A `.backup` copy appearing: not written on open.
- `QT_LOGGING_RULES` debug output: Kdenlive prints nothing offscreen.
- A cache directory named after `kdenlive:docproperties.documentid`: not created offscreen.

So do not claim a generated project opens. Say it is built and unverified, and ask the
user to open it. When something is wrong, hand them a three-scene version built from the
same skeleton alongside the full one: if both fail the skeleton is at fault, if only the
full one fails the clip data is, and either way it is one ten-second test rather than a
guess. Always run the same test against a project Kdenlive already opens before trusting
any verdict.

## Two gates before building

Never infer which project to build. The skill writes a file it then refuses to overwrite,
so guessing wrong costs the user real work. If no project was named, list the ones with a
`scenes/` folder and ask.

Never build on incomplete scenes. `scene_images.py verify` must PASS first. A cue with no
image does not fail loudly, the previous image simply stretches over the hole, and that is
discovered an hour into the edit. `kdenlive-build.py` refuses on its own and names the
missing cues; `--allow-gaps` exists only for a user who has seen that list and said build
anyway.
