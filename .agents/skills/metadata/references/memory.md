# metadata - memory

Self-improving notes for title, description, and tags. Single canonical copy.

## Project 10 (2026-08-25), third vs second - the run that unblocked the note below

7 chapters, 21 hashtags, 35 tags, all five titles 48 to 51 characters. Every chapter timestamp
was grepped back against `transcript.md` and exists there verbatim, which is worth doing because
a chapter pointing at a second with no cue is invisible until a viewer clicks it.

- **Title A was recommended over the punchier question forms because it carries the shock.** The
  script's whole hook is one counterintuitive verifiable claim, and the title is the first place
  that claim can land. A question title ("Why Do You Feel Worse Coming Second Than Third?") tests
  slightly punchier in isolation but restates the curiosity gap the thumbnail wants to own.
- **Chapter 6 sits on `[6:27]`, which is one of this transcript's duplicate timestamps.** That is
  harmless for chapters, which address a time rather than a file, but it will matter at `scenes`
  where the same timestamp becomes a filename. Do not "fix" a chapter to avoid a duplicate.
- Citations: all five were verified live rather than pattern-guessed, and one candidate died in
  the process. The university-hosted full text of Lee's "Eating Christmas in the Kalahari" at
  `laulima.hawaii.edu` refused the connection, so the citation fell back to Lee's Wikipedia article
  with the essay named and dated in the reference text. **A course-page URL hosting a full text is
  the least durable kind of citation on this list; prefer a DOI, PubMed, or the researcher's own
  institution.** Woodburn resolved cleanly through `doi.org/10.2307/2801707` to JSTOR, and Roese
  through his own Kellogg faculty page.

## PRECONDITION CONTRADICTION IN THE REPO, hit on 2026-08-25 (project 10), NOW RESOLVED IN PRACTICE

`/metadata` was invoked straight after `/cast`, before any voiceover existed, and correctly
refused. Two files disagree about this skill's inputs and the disagreement is real, not a
reading error:

- `AGENTS.md` says "After `/script` the branches run in parallel: `/transcript`, `/cast`, and
  `/metadata` depend only on the script."
- `.agents/skills/metadata/SKILL.md` says "**This skill must run after `/transcript`.** The
  chapters in the description are derived from the transcript's timestamp structure."

**SKILL.md is right and AGENTS.md is stale.** The description now carries a required 5 to 7
entry chapters block with real `M:SS` timestamps, and there is no way to derive those from a
script: the script has no timing, and the pace varies 152 to 177 wpm across the seven recorded
videos, so estimating them would put every chapter marker in the wrong place. AGENTS.md's line
predates chapters being added to the description.

The stale line should be corrected to put `/metadata` after `/transcript`, leaving only
`/transcript` and `/cast` as the true script-only branches. Flagged to the channel owner on
2026-08-25; not edited unasked because `AGENTS.md` is a source-of-truth file. The project 10 run
then went `/transcript` first and `/metadata` second with no friction, which is the order
SKILL.md prescribes.

**Everything except the chapters block is genuinely script-only** (five titles, hook, summary,
call to action, sources, hashtags, tags). Do not be tempted to ship a partial `metadata.md` with
a placeholder chapters block anyway: the file is meant to be pasted straight into YouTube, and a
half-file invites exactly that paste. Stop, say why, and name `/transcript` as the unblock.

## Lessons

- The published title and the folder slug do not have to match, and often should not. The
  folder slug is fixed at scaffold time and the `script_<short_slug>.md` name derives from it,
  which `character-prompts.md` references, so never rename the folder to match a better final
  title. (This previously said "referenced by every prompt file header"; from project 3 onward
  `image-prompts.md` has no header at all, so it is not affected either way.)
- The thumbnail question must not restate the title, so write the title first and hand it to
  the `thumbnail` skill. Project 1's title is "Why You Feel Lonelier In A Crowd Than Alone In
  Your Room", which is exactly why the accepted thumbnail asks about the 150-to-40 gap instead
  of repeating the loneliness framing.
