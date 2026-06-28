# Visual Implement Skill Memory

Memory specific to the `visual-implement` skill (created 2026-06-28).

Use `.agents/_shared/` for channel-wide visual systems, tone/safety rules, and the mascot pose library.
Use this file for asset-creation behavior: prompt-writing patterns for `generate` assets, sourcing
habits for `browse`/`screenshot` assets, the reuse/dedupe mechanism, the awaiting-drop handoff, and the
asset-manifest shape.

## Current Skill Standard

- Run after `visual-plan`; require a completed `04-visual-plan.md` and the selected section's
  visual-plan file with an ASSET list. Section-first; `All` offered first; never infer the section.
- Walk each scene's ASSET list; build a de-duplicated worklist grouped by filename.
- Per asset type:
  - `reuse` → verify the file exists; do nothing (consistency mechanism).
  - `pose` → copy the pose PNG from the library into `assets/poses/`.
  - `generate` → write a detailed image prompt (ISOLATED element, transparent/plain bg, channel
    flat-cartoon style + thick black outline; caricature = obvious parody + name-free fallback) and
    create the image if an image tool is connected; otherwise record the prompt and mark
    `prompt-ready / awaiting generation` and tell the user to generate + drop the file in.
  - `browse-real-photo` → `/browse` for a license-safe real photo; download; record attribution.
  - `screenshot/web-capture` → `/browse` capture of a public page/UI; never private data.
- Save all assets into the project `assets/` library; track every one in `assets/asset-manifest.md`;
  record browsed/real licenses in `assets/ATTRIBUTION.md`.
- Never recreate an existing file. Never produce a full composed scene (isolated elements only).
- Never claim an image exists when only a prompt was written.
- Enforce copyright/law/YouTube community standards; public figures only as transformative
  caricature/parody, punching up; no slurs, no private data, no false-as-fact.
- Stop before render; mark the affected section's render stale.

## Output Standard

- `projects/<slug>/assets/<filename>` and `projects/<slug>/assets/poses/<pose-files>`
- `projects/<slug>/assets/asset-manifest.md` (one row per filename: type, scenes, description, prompt
  if generate, source/license if browse, status)
- `projects/<slug>/assets/ATTRIBUTION.md` for browsed/real assets

## Feedback Log

### 2026-06-28 - Skill Created

Classification: `Core operational capability`

Context:
The owner split the visual pipeline into describe (`visual-plan`) → create assets (`visual-implement`)
→ composite (`render`). Generating full composed scenes made recurring characters inconsistent, so the
asset step must produce ISOLATED, reusable elements named by filename, and reuse them across scenes.

Lesson:
visual-implement owns prompt-writing and asset creation/sourcing. It reuses by filename for
consistency, produces isolated elements only, and supports the "write prompt → user generates in
ChatGPT → drop file into assets/" handoff when no image tool is connected.

Apply next time:
- de-dupe the worklist by filename; reuse-check before producing anything
- isolated element on transparent/plain bg; never a composed scene
- caricature for public figures with a name-free fallback; license capture for browse
- keep the manifest complete and honest about generation status

Promote to shared memory: pipeline architecture already recorded in `_shared/channel/learning-log.md`.

### 2026-06-28 - Pose-transfer prompt pattern (build the channel pose library from `_origin_`)

Classification: `Asset lesson`

Context:
The owner builds the channel mascot (WIT) pose library by giving ChatGPT TWO images - `_origin_` (the
mascot neutral pose = canonical identity) and a reference pose from another character (e.g. the Vui Vẻ
poses) - and asking for the SAME pose/emotion redrawn as the channel mascot. Reference poses are often
cropped at the chest/waist, but the owner wants FULL BODY output (crop later in render).

Lesson (canonical pose-transfer prompt - reuse for every pose):
- Attach order: Image 1 = `_origin_` (the ONLY identity to draw), Image 2 = the pose/emotion reference.
- Copy from Image 2 ONLY: pose, gesture, head tilt, facial emotion, and any clothing/props/accessories.
  Do NOT copy Image 2's character design (hair/colors/face/body).
- Keep the mascot 100% on-model (round bald white head, thick uniform black outline, big rectangular
  glasses + dot eyes, eyebrows, flat white no-color no-shading body); convey emotion via eyebrows,
  mouth, eyes, posture, and small marks (sweat, motion lines, sparkles); keep the glasses on.
- ALWAYS request FULL BODY head-to-feet even if Image 2 is cropped; center with generous margin.
- Output: single PNG, fully TRANSPARENT background, no ground shadow, no text, no logos, no extra elements.
- For "eyes become a shape" poses, add: "Replace the dot eyes with <shape> as shown in Image 2."
- Consistency: keep `_origin_` attached every time; generate a batch in one session when possible.

Apply next time: when producing channel-mascot pose assets, use this two-image pose-transfer prompt and
always demand full body + transparent bg; record each prompt + its `Attach:` line in `asset-manifest.md`.

Promote to shared memory: no; this is visual-implement asset-creation behavior.

### 2026-06-28 - White-filled mascot: protect the white fill from the transparency tool

Classification: `Asset lesson`

Context:
The pose-transfer prompt asked for a "transparent background". The channel mascot is white-filled with a
black outline. ChatGPT's transparency removal keyed out the white EVERYWHERE, including the mascot's
white head/body interior, and the dark-suit (boss) pose then read as a solid black silhouette on a
checkerboard. The mascot lost its identity (white head gone).

Lesson (fix the prompt for any white-filled character):
- State the fill colors explicitly: HEAD + body + hands are SOLID BRIGHT WHITE (#FFFFFF) with a black
  outline; ONLY clothing takes the reference's color. Keep glasses + dot eyes as `_origin_`.
- Add a hard rule: "DO NOT render the character as a black/grey silhouette; white areas stay bright,
  fully OPAQUE white."
- Background instruction must distinguish bg-transparency from the character's white fill: "transparent
  ONLY outside the black outline; the white INSIDE the outline is opaque and must NOT be made
  transparent."
- Fallback if transparency still eats the white: generate on a SOLID FLAT GREEN (#00B140) background
  (no transparency), keep head white + suit dark, then chroma-key the green out at render with ffmpeg
  `colorkey` (the green is not present on the mascot, so the white fill survives).

Apply next time: for white-filled mascot assets, never give a bare "transparent background" instruction;
always pin the white fill as opaque + ban silhouettes, and offer the green-screen + ffmpeg-key fallback.

Promote to shared memory: no; visual-implement asset-creation behavior.

### 2026-06-28 - Pose-transfer: do NOT inherit the reference character's default outfit

Classification: `Asset lesson`

Context:
With the green-screen prompt the white fill was preserved, but the output copied the Vui Vẻ reference's
DEFAULT everyday outfit (yellow/orange shirt + purple crossbody bag) onto our mascot. Our mascot has NO
default clothes (plain white body); the shirt+bag are the reference character's identity, not ours.

Lesson:
In a pose-transfer prompt, separate "default outfit" from "defining costume":
- Copy from the reference ONLY: pose, gesture, head tilt, facial emotion.
- Explicitly IGNORE the reference's default outfit (name it: yellow/orange shirt + crossbody bag) and
  its character design. Our mascot stays a plain white body by default.
- Add clothing/props ONLY when they are a DISTINCT COSTUME that defines the pose's meaning (business
  suit, doctor coat, sunglasses, gold chain, held object). An everyday shirt/bag is not such a costume.

Apply next time: pose-transfer prompts must say "do not copy the reference's default shirt/bag; plain
white body unless a distinct costume defines the pose."

Promote to shared memory: no; visual-implement asset-creation behavior.

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Operational lesson` / `Asset lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory: yes/no, with reason
```
