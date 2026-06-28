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
  - `pose` → copy the pose PNG from the library into `assets/poses/`. Library poses are TRANSPARENT
    RGBA cutouts (keyed in place 2026-06-28) - copy DIRECTLY, no chroma-key step, no `poses-keyed` folder.
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

### 2026-06-28 - Pose library is now TRANSPARENT (keyed in place); copy poses directly

Classification: `Asset lesson`

Context:
The whole green-screen pose library was chroma-keyed to transparent in place and committed
(`.agents/_shared/assets/wit/poses/*.png` are RGBA cutouts now). The owner found maintaining BOTH a
green `poses/` and a keyed `poses-keyed/` redundant.

Lesson:
For `pose` assets, just copy the library PNG into `projects/<slug>/assets/poses/` and reference it
directly - no green screen, no chroma-key, no `poses-keyed/`. The white mascot fill is already opaque.
The two entries below (green-screen white-fill survival, green-screen + ffmpeg-key fallback) are now
HISTORICAL - they only apply if a future pose is ever delivered on green again.

Apply next time: copy poses straight into `assets/poses/`; if you ever generate a NEW pose, prefer a
transparent output (or key it once before adding it to the library, so the library stays all-transparent).

Promote to shared memory: recorded in `pose.md`, `brand-system.md`, `current-state.md`, `learning-log.md`.

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

### 2026-06-28 - First browse/source run (Section 1, ai-slop): pose-catalog drift, Openverse preview-res, people/brand checks

Classification: `Operational lesson`

Context:
First real sourcing run of `visual-implement` (project `5-why-the-internet-is-full-of-ai-slop`, Section 1).
No image generator connected, so `generate` cards were handled as render-CSS real-UI + a PNG-fallback
prompt in the manifest. Sourced 8 CC0 photo bases via Openverse + 2 Public-Domain AI-slop images from
Wikimedia Commons, copied 9 library poses.

Lessons (apply next time):
- POSE-CATALOG DRIFT: `pose.md` listed poses that are NOT on disk (`holding_phone_looking_content`,
  `ok_hand_sign_content_relaxed`). Always `ls` the real pose dir and reuse-check each filename before
  copying; substitute the closest real pose (used `holding_phone_pointing_smile`,
  `ok_hand_sign_content_closeup`) and then SYNC the substitution back into the section plan + master so
  render never points at a missing file.
- OPENVERSE `url` IS PREVIEW-RES (~960-1024px), not the declared original. For full-HD bases prefer
  Wikimedia Commons (its `url` is full-res; e.g. the sludge base came back 4000x3000). Flag preview-res
  bases in the manifest as "swap if soft at 1920".
- COMMONS AI-SLOP IMAGES are easy and safe: Shrimp Jesus + "AI generated hand" are Public Domain;
  fetch direct URL + license via the imageinfo API (`prop=imageinfo&iiprop=url|extmetadata`) then curl.
- VERIFY PIXELS with the Read tool on the downloaded image - it catches what the API can't: the first
  music pick ("concert crowd") was full of PEOPLE (owner rejects real-people backgrounds), re-sourced to
  a studio mixing console (people-free, but has SSL/XLogic branding - flagged to blur/crop at render).
  Eyeball at least the people/brand-risk bases (interiors, crowds, devices) before finalizing.
- TOOLING ON THIS BOX: git-bash `/tmp` != node's `C:\tmp` - write temp files to the scratchpad dir.
  `node` (global `fetch`) + `curl` are available; no python needed for sourcing.

Promote to shared memory:
no; visual-implement sourcing/tooling behavior. The Openverse-vs-Commons resolution + people/brand
pixel-check already align with the shared visual-production reference rules.

### 2026-06-28 - Generate-forward batch (S3 v2) + stock queries surface PEOPLE and NAMED FIGURES

Classification: `Asset lesson`

Context:
S3 was rebuilt generate-forward (owner wants wild bespoke imagery, not reused photos). Implemented = copy
poses + source 8 fresh bases + write 10 detailed generate prompts (no image tool connected -> status
`prompt-ready / awaiting generation`; owner generates in ChatGPT + drops PNGs into `assets/`). While
sourcing bases, blind "best match" picks repeatedly pulled rejects: a concert CROWD, a Korean street with
people, and - worst - **Jimmy Carter at a UN podium** (a real, identifiable public figure) for "microphone
dark background". Re-sourced each people-free/figure-free and VERIFIED with the Read tool.

Lesson:
- For generate-forward sections, write each prompt fully standalone (Attach line, channel-cartoon vs
  photoreal-uncanny per asset, isolated transparent bg, explicit "do NOT: real logo / real person /
  background / text"), and mark `prompt-ready / awaiting generation`. Render's asset-ready gate will block
  until the owner drops the real PNGs in - say so clearly.
- ALWAYS eyeball sourced bases. Stock/Openverse "microphone/stage/street/concert" queries frequently
  return real people AND named public figures (politicians, celebrities). Add a name/role denylist to the
  picker (carter|president|obama|trump|singer|player|crowd|...) AND still Read-verify; never ship a base
  with an identifiable real person.
- Keep a brand-free bias on object queries too (the earlier SSL console, Robby-the-Robot tin toy).

Apply next time: budget for 1-2 re-sources per base batch; verify every base; prefer clean object/texture
bases that won't contain incidental people.

Promote to shared memory: no; visual-implement sourcing tactic (the unlimited-imagination/generate-forward
direction itself is already promoted via visual-plan memory + learning-log).

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Operational lesson` / `Asset lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory: yes/no, with reason
```
