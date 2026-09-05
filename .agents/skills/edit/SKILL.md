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

## Inputs it needs

| Input                        | Written by      |
| ---------------------------- | --------------- |
| `scenes/[M-SS].jpg`          | you, from `/scenes` |
| `transcribes/transcript.md`  | `/transcript`   |
| `audios/full.mp3`            | `/transcript`   |

Run `/check` and `/scene-polish verify` first. A scene image missing for a cue is not an
error here, the previous image simply holds through it, but it is almost always a gap
worth filling before the edit starts.

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

- `--force` overwrites an existing project file. Without it the tool refuses, because
  hand edits made in Kdenlive cannot be rebuilt from the transcript.
- `--out PATH` writes a second file beside the first instead of replacing it.
- `--profile` picks the project profile, `qhd_1440p_30` by default. `--fps` overrides its
  frame rate.
- `--fit cover|stretch` maps the 1376x768 scene images onto the 16:9 frame instead of
  letterboxing them. Default `contain`, which is what the hand-built projects do.
- `--logo`, `--logo-size`, `--logo-margin` place a held image on V2.
- `--audio PATH` for a narration that is not `audios/full.mp3`.

## After it opens

The tool builds the assembly, not the edit. Still to do by hand in Kdenlive: audio
ducking and level rides, any music bed, transitions, and the render profile.

Never re-run the tool over a project the user has already worked on. Ask first, then use
`--out` to write a fresh file so the hand work survives.
