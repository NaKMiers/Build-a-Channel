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

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Operational lesson` / `Asset lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory: yes/no, with reason
```
