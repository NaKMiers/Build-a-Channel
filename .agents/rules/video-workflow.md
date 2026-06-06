# Video Workflow Rules

`Why It Works` uses a 10-step video lifecycle.

## Steps

1. Topic intake
2. Research pack
3. Script draft
4. Voice revision and voiceover
5. Title and thumbnail packaging
6. Visual plan
7. HyperFrames build
8. Review
9. Upload
10. Self-learning

## Current Skill Coverage

- Step 1 `Topic intake` is implemented by `.agents/skills/topic-intake/`.
- Step 2 `Research pack` is implemented by `.agents/skills/research-pack/`.
- Step 3 `Script draft` is implemented by `.agents/skills/script-draft/`.
- The remaining lifecycle steps do not have executable project-local skills yet.

## Project Outputs

Each new video should start from `projects/_template/` and produce:

- `00-topic-intake.md`
- `01-research-pack.md`
- `02-script.md`
- `03-voiceover.md`
- `04-packaging.md`
- `05-visual-plan.md`
- `06-production-board.md`
- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`
- `assets/`
- `hyperframes/`
- `renders/`
- `voiceover/`

## Gate Rule

Do not rush into HyperFrames.

Production starts only after the idea, script, packaging, and visual plan are strong enough to build.

## Review Rule

When a review creates a reusable lesson, update the project review file first, then promote the lesson into shared memory or future skill memory.
