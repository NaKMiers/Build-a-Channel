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

## CapCut

CapCut has no timeline import, so `tools/capcut-build.py` writes its draft folder
directly. Times are microseconds, not frames.

Do not hand-write the JSON. Every object is cloned from
`templates/capcut-9.1-mac.json`, extracted from a draft CapCut itself wrote, because the
format is undocumented and the fields that matter are not the ones that look important.
A segment carries seven `extra_material_refs`, in this order: speeds, placeholder_infos,
canvases, sound_channel_mappings, material_colors, loudnesses, vocal_separations. Audio
takes five: speeds, placeholder_infos, beats, sound_channel_mappings, vocal_separations.
Each ref must point at a material that actually exists, and each segment gets its own
copies. `hsl` and `material_animations` appear only on clips a person later touched, so
generated segments carry neither.

The timeline is written twice, byte-identical, at `draft_info.json` and
`Timelines/<timeline id>/draft_info.json`. `Timelines/project.json` names the main
timeline. `draft_meta_info.json` carries the draft name and its folder path on the target
machine.

Media paths are absolute and belong to the machine that opens the draft, which is why
`--media-root` is required and has no default. Canvas follows the scene images: width
1920, height from their aspect, which is how CapCut derived 1920x1072 from 1376x768.

The template's `platform` block keeps os and app version but has `device_id`,
`hard_disk_id` and `mac_address` blanked, because it is committed to a public repo.

One `edit/` folder per project, with `kdenlive/` and `capcut/` inside it. Not a sibling
folder per editor: it is one edit of one video, and splitting it at the top level makes
the project look like it holds two unrelated things. Build both every time, because the
user moves between machines and only finds the missing half when they need it.

`--media-root` for CapCut is configuration, not a default. It lives in
`.agents/skills/edit/media-roots.json`, keyed by platform, because the path belongs to
another machine and nothing here can derive it.

A CapCut segment boundary must come from the microsecond position of the next cue, never
from a separately rounded duration. `round(a) + round(b)` is not `round(a + b)`, and at
30fps a frame is 33333.33us, so rounding each duration on its own left a gap at 80 of the
288 boundaries in project 14. A legacy whole-second project hides this completely, because
its cuts land on exact microseconds; test the fix on a `[MM:SS.SSS]` project.

The logo box lives in `cuts.py` as fractions of the frame, not in either exporter, so the
two agree. The channel's setting is a 100px square at 2330,1200 on 2560x1440, which is
130px of clearance to its right and 140px below.

Kdenlive states that box directly in the qtblend `rect`. CapCut does not: it fits the
image to the canvas first and its `scale` multiplies that fitted size, so a scale of 1 is
the fitted image, never the source pixels. `displayed = scale * source_width * fit`, where
`fit = min(canvas_w / source_w, canvas_h / source_h)`. Confirmed against a real draft:
scale 0.07092 on a 1254px logo in a 1920x1072 canvas renders 76px. `clip.transform` is the
centre of the box, normalised to -1..1 from the middle of the frame, with y pointing up.

Each editor folder ships its own launcher, generated with the project: `open.sh` beside
the Kdenlive file, `install-mac.command` or `install-windows.bat` beside the CapCut draft.
The CapCut one sits next to the draft folder, never inside it, or it would be copied into
CapCut's own directory along with the timeline.

The installer must refuse rather than half-work. It stops when CapCut is running, because
CapCut reads its draft list at startup and rewrites drafts on quit, so a copy underneath a
running CapCut is either invisible or overwritten. It stops when the media root is absent,
which is the difference between a clear message and a timeline of offline clips. It asks
before replacing a draft of the same name.

Resolve the draft directory inside the script with `$HOME` or `%LOCALAPPDATA%`, never a
username baked in at build time; only `draft_meta_info.json` needs a literal path, and
that one is derived from the media root.

In a `.bat`, `if cond echo A & pause & exit /b 1` guards only the `echo`; the rest runs
unconditionally. Use `goto` and labels. Write it with CRLF endings.

## The draft must not carry any machine's paths

CapCut stores absolute paths, so a draft built with a real path only opens on the machine
that path describes, and anywhere else every clip is offline. Do not solve this by
configuring the path: it cannot be known from here, and a guess fails silently.

Build with `@@MEDIA_ROOT@@` and `@@DRAFT_ROOT@@` in place of the absolute parts, and let
the installer substitute them as it copies. It finds the repo by walking four levels up
from its own location, `<repo>/projects/<slug>/edit/capcut/`, so it needs no
configuration and works wherever the repo has been put. Rewrite only the installed copy,
never the one in the repo, or the repo's copy stops being portable after the first install.

The separator is a token as well, `@@SEP@@`, which is what lets a single draft serve both
machines: a mac draft and a windows draft are otherwise byte-identical once ids are
normalised. Never build one folder per platform. It also keeps both installers down to
three plain string replacements, with no regex and no PowerShell script block.

On Windows the substitution runs through PowerShell and must double the backslashes,
because the paths land inside JSON strings. Set `TARGET` in the batch before referring to
`$env:TARGET` in the PowerShell line.

Shell and batch templates are full of braces, so `str.format` cannot be used on them.
Substitute with plain `<<TOKEN>>` replacement.

Check for a surviving `@@` rather than for the individual token names. The first version
checked only two of the three and shipped a draft where every separator was still a token,
which the check passed happily.

## Batch traps the mac script does not have

`cd /d` fails on a UNC path: cmd refuses one as a working directory. Use `pushd`, which
maps a drive letter for it, and `popd` on every exit path.

`echo Installed to %REPO%` with an unquoted variable runs whatever follows an `&` in the
path as a command. Quote every path in `echo`.

Both were found by reading the batch rather than by testing, since there is no cmd here.
The mac installer is exercised for real against paths with spaces, Vietnamese diacritics,
apostrophes, ampersands, brackets and parens, plus every refusal path. The windows one can
only have its rewrite simulated and its control flow audited, so read it carefully.

## Never let a formatter touch a generated timeline

An XML formatter moves a `<property>` value onto its own indented line. MLT then reads the
scene path with the indentation attached, and Kdenlive opens with every clip missing:
290 of them, with nothing on screen explaining why. VS Code's `editor.formatOnSave` is on
globally on this machine, so opening a `.kdenlive` and saving it is enough to destroy it.

Three defences, all needed. `.vscode/settings.json` marks `edit/` generated files
read-only and maps `.kdenlive` to plaintext so no XML formatter claims it. `open.sh`
refuses to launch when it finds `name="resource">` at end of line, and names the rebuild
command, so the failure is one clear sentence rather than a dialog full of missing clips.
And a rebuild is always the repair, since these files are reproducible.

Pretty-printed JSON is harmless by comparison, because JSON ignores whitespace between
tokens, so the CapCut draft survives the same treatment. Only the XML is fragile.

## draft_meta_info's draft_materials is the Media bin

Leaving it empty leaves CapCut's Media panel empty, so there is nothing to re-drag and the
draft looks broken even when the timeline is right. One `type: 0` entry per media file,
carrying `file_Path`, `extra_info` (the file name), `metetype` (`photo` or `music`),
`duration`, `width`, `height`. A photo gets 5000000 and `roughcut_time_range` of
`{-1, -1}`; the audio gets its real length and `{duration, 0}`. The audio material in
draft_info links to its bin entry through `local_material_id`; photos leave that empty.

## Check the files, not the folder

The installer checking that `scenes/` exists passes on a repo that is present but out of
date, and CapCut then shows every clip red with no explanation. Check every path the draft
actually references, in both JSON files, and refuse when any is missing, naming a few.

Write that check with no backslash escapes at all. The installer templates are non-raw
Python strings, so `\n` becomes a real newline and breaks the perl one-liner across lines,
and `\s` raises a SyntaxWarning and survives only by accident. `perl -nE` with `say`
supplies the newline, and `[ ]*` covers the single space `json.dumps` puts after a colon.

## A prompt in a double-clicked .command needs the terminal, not stdin

Finder can start a `.command` with stdin detached, and `read -r reply` then returns an
empty string immediately. The script cannot tell that apart from the user declining, so it
printed "Nothing was copied" and exited without ever waiting, which reads as the installer
doing nothing at all.

Pick the source by what stdin actually is: `[ -t 0 ]` or a pipe or a file means read
stdin, otherwise open `/dev/tty` read-write on a spare descriptor and use that, and if
neither exists say so and exit rather than treating silence as an answer. Checking
`/dev/tty` first instead would work on the Mac but silently ignore piped input, which
makes the thing untestable.

Accept `y` as well as `yes`, and prompt `[y/N]` so the safe answer is the obvious one. A
confirmation nobody can satisfy is worse than no confirmation.
