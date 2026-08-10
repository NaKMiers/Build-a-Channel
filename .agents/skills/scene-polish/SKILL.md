---
name: scene-polish
description: Safely check, rename, move, and verify TossExplains scene images against image-prompts.md timestamps. Use when the user asks to manage scene-image files, timestamp names, range folders, or scene-image validation.
---

# scene-polish

Read `.agents/rules/house-rules.md`, `.agents/rules/file-formats.md`, and `references/memory.md` first.

Use one operation at a time. Scene image files are Windows-safe `[M-SS].jpg` names,
derived from their `[M:SS]` prompt timestamps by replacing `:` with `-`. Never rename
or move files unless its safety checks pass.

## Migrate Windows-incompatible image names

Use this only to repair existing scene image files containing `:` in their names:

```bash
python3 .agents/skills/scene-polish/scripts/scene_images.py migrate-windows projects/<n>-<slug>
```

The command inspects every scene image recursively, checks for duplicate destinations
and existing-file collisions, then replaces `:` with `-`. On any conflict it exits
without renaming. Run `verify` afterward.

## Check a numbered range

Identify the project and inclusive range endpoints from the folder name, for example `0:00 - 4:58`. Run:

```bash
python3 .agents/skills/scene-polish/scripts/scene_images.py check-range projects/<n>-<slug> <START> <END>
```

Report prompt timestamps, numbered images, existing timestamp images, unexpected entries, root-level destination collisions, and PASS or FAIL. Do not rename anything. On FAIL, name the mismatch and stop.

## Rename a checked range

```bash
python3 .agents/skills/scene-polish/scripts/scene_images.py rename-range projects/<n>-<slug> <START> <END>
```

The command checks equal counts, a complete `1` through `N` sequence, unexpected files, and destination collisions before changing any name. On a mismatch it exits without renaming.
It saves each image as `[M-SS].jpg`, replacing the prompt timestamp colon with a
hyphen.

## Flatten range folders

```bash
python3 .agents/skills/scene-polish/scripts/scene_images.py move projects/<n>-<slug>
```

The command refuses to move files if a range folder has a non-timestamp entry, a timestamp name is duplicated, or a root destination already exists. It removes only folders proven empty.

## Verify the completed scenes folder

```bash
python3 .agents/skills/scene-polish/scripts/scene_images.py verify projects/<n>-<slug>
```

Report prompt timestamps, scene images, duplicate prompt timestamps, missing images, extra timestamp images, unexpected files, and PASS or FAIL. Do not modify files.
