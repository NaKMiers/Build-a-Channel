---
name: WIW Take Note
description: Project-local memory capture for the Why It Works channel. Use when the user invokes $WIW Take Note, asks to take note of reviews, says to remember feedback, or gives useful production/review lessons that should improve future HyperFrames board videos in this workspace.
---

# WIW Take Note

## Purpose

Capture user reviews and production lessons into the right project memory files so future Codex sessions avoid repeated mistakes.

This skill is project-local. Use it only inside `C:\ME\THINGS\Build a Channel`.

## Workflow

1. Read the project memory first if it is not already loaded:
   - `README.md`
   - `.agents/_shared/channel/current-state.md`
   - `.agents/_shared/channel/channel-guardrails.md`
   - `.agents/_shared/channel/learning-log.md`
   - `.agents/_shared/channel/codex-collaboration.md`
   - `.agents/_shared/channel/production-workflow.md`

2. Identify the active scope:
   - Active video folder comes from `.agents/_shared/channel/current-state.md`.
   - Current review notes usually belong in `projects/<slug>/06-review.md`.
   - Reusable lessons belong in `.agents/_shared/channel/learning-log.md`.
   - Stable production conventions belong in the compact `.agents/_shared/systems/` docs when they affect future videos, but do not create extra docs unless needed.

3. Classify the note before writing:
   - `Operational lesson`: reusable workflow, timing, layout, QA, HyperFrames, voice-sync, or review-process lesson.
   - `Current-video review note`: specific scene, timestamp, composition, or fix for the active video.
   - `Experiment`: uncertain style or production idea that should be tested.
   - `Core`: only for stable channel identity decisions, and only after checking `.agents/_shared/channel/channel-guardrails.md`.
   - `Reject`: do not persist.

4. Write concise notes:
   - Normalize the user's review into reusable rules.
   - Preserve exact timestamps, composition names, scene IDs, and file names when they matter.
   - Avoid copying long chat text.
   - Prefer short bullets with the pattern: problem -> rule or fix -> verification expectation.

5. Update both levels when useful:
   - Add reusable lessons to `.agents/_shared/channel/learning-log.md` under the current date.
   - Add active-video checklist items or review decisions to `projects/<slug>/06-review.md`.
   - Update `.agents/_shared/channel/current-state.md` only when the latest project status actually changes.

## Review Lessons To Preserve

When recording HyperFrames board-video reviews, include these checks if relevant:

- Voice sync beats must align to the spoken cue, not only the rough sentence block.
- If a voice line ends, trim the composition or add a useful visual beat; do not leave dead visual time.
- WIT images need visible headroom, side margin, and prop margin inside the selected composition bounds.
- Do not repeat the same visual emphasis across adjacent boards unless repetition is intentional.
- Underlines should span the readable width of the emphasized word or phrase.
- Small cards, invoices, and UI mockups need internal text-overflow checks.
- Payoff phrases such as `second one` should get size, color, timing, or motion emphasis.
- If a prop is removed, rebalance the board by centering and resizing the remaining text.
- Verify exact reviewed timestamps with still frames before saying a fix is done.
- Do not render or export a new MP4 unless the user explicitly asks.

## Output

After writing notes, respond with:

- the files updated
- the kind of memory added
- any assumptions, if the active video or classification was uncertain
