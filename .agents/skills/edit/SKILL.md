---
name: edit
description: Build the editing project for a TossExplains video, for Kdenlive and for CapCut, with every scene image already cut onto the timeline at its transcript timestamp and the narration on its own track. Use when the user says "edit", "kdenlive", "capcut", "build the timeline", "assemble the video", or "join the scenes".
---

# edit

Read `.agents/rules/house-rules.md` and `.agents/rules/file-formats.md` first, then
`references/memory.md`.

This skill replaces dragging 300-plus images onto a timeline by hand. It writes a Kdenlive
project and a CapCut draft, both already cut, so the editing session starts at the polish
rather than at the assembly. Both come from one plan in `tools/cuts.py`, so they cut on
identical frames.

## Stop unless both preconditions hold

**1. The user has named the project.** Never infer it. Not the newest folder, not the one
most recently touched, not the one discussed earlier in the conversation. This skill
writes into a project and refuses to overwrite afterwards, so building the wrong one
costs the user a real file. If the user said "edit" or "build the timeline" without
naming a project, list the projects that have a `scenes/` folder and ask which one.

**2. The scenes are fully generated.** Run this first and require PASS:

```bash
python3 .agents/skills/scene-polish/scripts/scene_images.py verify projects/<n>-<slug>
```

On FAIL, report what is missing and stop. Do not build. A cue with no scene image is a
hole in the video, and the image before it stretches to cover the hole, which is the kind
of thing that is only noticed after an hour of editing. `tools/kdenlive-build.py` enforces
this too and exits rather than building; `--allow-gaps` overrides it and is only for a
user who has been told what is missing and said to build anyway.

## Inputs it needs

| Input                        | Written by      |
| ---------------------------- | --------------- |
| `scenes/[M-SS].jpg`          | you, from `/scenes` |
| `transcribes/transcript.md`  | `/transcript`   |
| `audios/full.mp3`            | `/transcript`   |

`/check` is worth running too, but the two gates above are the ones that block.

## Build

Always build both. One project, one `edit/` folder, one timeline in two editors:

```bash
python3 tools/kdenlive-build.py projects/<n>-<slug> --logo brand/logo.png
python3 tools/capcut-build.py   projects/<n>-<slug> --logo brand/logo.png
```

```
projects/<n>-<slug>/edit/
  kdenlive/<n>-<slug>.kdenlive    the timeline
  kdenlive/open.sh                opens it in Kdenlive
  capcut/<n>-<slug>/              the draft folder
  capcut/install-mac.command      installs it on a Mac
  capcut/install-windows.bat      installs it on Windows
```

Each folder carries its own launcher, so opening an edit is one click and never a path
typed out by hand. Both are generated with the project; do not write them by hand.
Both CapCut installers are written every time; there is nothing to choose.

Never build only one. The user edits on whichever machine is free, and a missing half is
found at the moment it is needed. If one exporter fails, say so and still build the other.

Report the scene count, the total duration, and every `note:` line either tool prints.

Preview the cut list without writing anything, from either tool, they agree:

```bash
python3 tools/kdenlive-build.py projects/<n>-<slug> --dry-run
```

### Getting the CapCut draft into CapCut

```
edit/capcut/<n>-<slug>/          the draft
edit/capcut/install-mac.command  run this on a Mac
edit/capcut/install-windows.bat  run this on Windows
```

One draft, two ways to install it. On a Mac, double-clicking the `.command` in Finder is
enough. It copies the draft into CapCut's folder, fills in the paths, and opens CapCut.

**The draft belongs to no machine.** Absolute paths are not stored at all: it ships with
`@@MEDIA_ROOT@@`, `@@DRAFT_ROOT@@`, and `@@SEP@@` for the separator, and the installer
substitutes all three as it copies, using `/` on a Mac and `\` on Windows. It works out
the repo by walking four levels up from itself, so it never has to be told where anything
is, and it rewrites only the installed copy, so the one in the repo stays portable.

Never build a second draft per platform. They differ by nothing but the separator, and
the separator is a token.

The one requirement is that the repo, with `scenes/` and `audios/`, is on the machine that
opens the draft. CapCut needs those files.

The installer refuses rather than half-working: it stops if CapCut is running, since
CapCut reads its draft list at startup and rewrites drafts on quit; it stops if it cannot
find the project's media from where it sits; it asks before replacing a draft of the same
name; and if any `@@` token survives the substitution it deletes what it copied, rather
than leaving a timeline of offline clips.

## Where the cut times come from

The scene image file name is only a join key. `[1-17].jpg` came from the `[1:17]` prompt
stamp, which is `tsfmt.to_mss()` of the transcript's `[01:17.240]`, and truncation threw
the milliseconds away. So the tool joins the image to its transcript line by that key and
then cuts on the line's own timestamp, not on the whole second in the file name. On a
legacy whole-second transcript the two are the same and the cut lands on the second.

Each image is held until the next cue starts. The last one runs out the narration, so the
video track and the audio track end together.

## Flags worth knowing

Both tools:

- `--allow-gaps` builds despite cues with no scene image. Only after the user has seen
  the list and asked for it.
- `--force` overwrites an existing project. Without it the tool refuses, because hand
  edits made in an editor cannot be rebuilt from the transcript.
- `--out PATH` writes somewhere else instead of replacing what is there.
- `--audio PATH` for a narration that is not `audios/full.mp3`, `--duration` to override
  its length, `--fps` for the frame rate.
- `--logo` holds an image on the track above the scenes. Its box is defined once in
  `tools/cuts.py` as fractions of the frame, so both editors place it identically: at
  2560x1440 that is a 100px square at 2330,1200. Adjust with `--logo-size`,
  `--logo-right`, `--logo-bottom`.

Kdenlive only:

- `--profile` picks the project profile, `qhd_1440p_30` by default.
- `--fit cover|stretch` maps the 1376x768 scene images onto the 16:9 frame instead of
  letterboxing them, default `contain`.
- `--logo-rect "X Y W H"` sets the transform in project pixels directly.

CapCut only:

- `--width` and `--height` for the canvas, which otherwise follows the scene images
  rather than a profile. That is how 1376x768 becomes 1920x1072.
- `--draft-root` if CapCut's draft folder is not in its usual place, `--name` for the
  draft's name in CapCut.

## Never let a formatter touch the generated files

An XML formatter moves a `<property>` value onto its own indented line. MLT then reads the
scene path with the indentation attached, and Kdenlive opens reporting every clip missing,
with nothing on screen saying why. VS Code's `editor.formatOnSave` is enough to do this to
a `.kdenlive` that gets opened and saved.

`.vscode/settings.json` in this repo marks the generated files read-only and maps
`.kdenlive` to plaintext so no XML formatter claims it. `open.sh` also refuses to launch a
project whose clip paths have been broken this way, and names the rebuild command.

Pretty-printed JSON is harmless, because JSON ignores whitespace between tokens, so a
CapCut draft survives the same treatment. Only the XML is fragile.

## Verifying

`melt` accepting the document proves the MLT is valid, nothing more. Kdenlive's own
validator is stricter and there is no way to test it offscreen: every signal tried returns
the same verdict for a known-good project as for a broken one. `references/memory.md`
lists what was tried and why each fails. There is no way at all to test CapCut from here.

So never tell the user a project opens. Say it is built, and ask them to open it.

When they report a failure, read it before changing anything:

| What they see | Where to look |
| --- | --- |
| Kdenlive lists N missing clips | The file was reformatted. Rebuild with `--force`. |
| Kdenlive: "Could not recover corrupted file" | The document itself. Diff it against a project Kdenlive already opens. |
| CapCut clips all offline | The repo is not on that machine, or is somewhere the installer could not find. |
| CapCut does not list the draft | It was copied while CapCut was running. Quit it and run the installer again. |

If a Kdenlive document is rejected outright, build a three-scene version from the same
skeleton with `--out` and have them try both: both failing puts the fault in the skeleton,
only the full one failing puts it in the clip data.

## After it opens

The tool builds the assembly, not the edit. Still to do by hand in Kdenlive: audio
ducking and level rides, any music bed, transitions, and the render profile.

Never re-run either tool over a project the user has already worked on. Ask first, then
use `--out` to write a fresh copy so the hand work survives. The one exception is a file a
formatter has broken: that one is already unusable, and rebuilding is the repair.
