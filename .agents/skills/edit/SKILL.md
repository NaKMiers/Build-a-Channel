---
name: edit
description: Build the Kdenlive project for a TossExplains video, with every scene image already cut onto the timeline at its transcript timestamp and the narration on its own track. Use when the user says "edit", "kdenlive", "build the timeline", "assemble the video", or "join the scenes".
---

# edit

Read `.agents/rules/house-rules.md` and `.agents/rules/file-formats.md` first, then
`references/memory.md`.

This skill replaces dragging 300-plus images onto a timeline by hand. It writes a
`.kdenlive` file whose timeline is already cut, so the editing session starts at the
polish, not at the assembly.

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

```bash
python3 tools/kdenlive-build.py projects/<n>-<slug> --logo brand/logo.png
```

Writes `projects/<n>-<slug>/edit/<n>-<slug>.kdenlive`. Report the scene count, the total
duration, and every `note:` line the tool prints.

Preview the cut list without writing anything:

```bash
python3 tools/kdenlive-build.py projects/<n>-<slug> --dry-run
```

## Where the cut times come from

The scene image file name is only a join key. `[1-17].jpg` came from the `[1:17]` prompt
stamp, which is `tsfmt.to_mss()` of the transcript's `[01:17.240]`, and truncation threw
the milliseconds away. So the tool joins the image to its transcript line by that key and
then cuts on the line's own timestamp, not on the whole second in the file name. On a
legacy whole-second transcript the two are the same and the cut lands on the second.

Each image is held until the next cue starts. The last one runs out the narration, so the
video track and the audio track end together.

## Flags worth knowing

- `--allow-gaps` builds despite cues with no scene image. Only after the user has seen
  the list and asked for it.
- `--force` overwrites an existing project file. Without it the tool refuses, because
  hand edits made in Kdenlive cannot be rebuilt from the transcript.
- `--out PATH` writes a second file beside the first instead of replacing it.
- `--profile` picks the project profile, `qhd_1440p_30` by default. `--fps` overrides its
  frame rate.
- `--fit cover|stretch` maps the 1376x768 scene images onto the 16:9 frame instead of
  letterboxing them. Default `contain`, which is what the hand-built projects do.
- `--logo`, `--logo-size`, `--logo-margin` place a held image on V2.
- `--audio PATH` for a narration that is not `audios/full.mp3`.

## Verifying

`melt` accepting the document proves the MLT is valid, nothing more. Kdenlive's own
validator is stricter and there is no way to test it offscreen: every signal tried returns
the same verdict for a known-good project as for a broken one. `references/memory.md` lists
what was tried and why each fails.

So never tell the user the project opens. Say it is built, and ask them to open it. If it
does not, build a three-scene version from the same skeleton with `--out` and have them try
both: both failing puts the fault in the skeleton, only the full one failing puts it in the
clip data.

## After it opens

The tool builds the assembly, not the edit. Still to do by hand in Kdenlive: audio
ducking and level rides, any music bed, transitions, and the render profile.

Never re-run the tool over a project the user has already worked on. Ask first, then use
`--out` to write a fresh file so the hand work survives.
