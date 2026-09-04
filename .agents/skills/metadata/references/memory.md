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

## Project 11 (2026-08-28), false memory - title chosen for glance-clarity over hook-echo

7 chapters, 20 hashtags, 36 tags, all five titles 47 to 62 characters, 3 fenced blocks matching
projects 9 and 10. Every chapter timestamp grepped back against `transcript.md` and present
verbatim.

- **Recommended title A, "Why Do You Remember Things That Never Happened?", over E** even though
  E ("You Never Noticed Your Most Certain Memory Is Your Most Edited") is a closer echo of the
  script's actual first line, which after a hook rewrite is "The memory you trust most is your
  least reliable one." A is 47 characters against E's 62, is a question, and states the paradox in
  words a tired viewer parses at a glance, which is the standing batch 8 steer in
  `topic/references/memory.md`. E front-loads two possessive comparatives and has to be read
  twice. **Title-to-hook echo is worth less than glance-clarity when the hook resolves the
  title's claim inside 30 seconds anyway**, and this one does: the new open question at 0:33 is
  "So which of yours have been rewritten?"
- C is the search-friendly alternative and follows a form the channel already publishes under
  ("The Loneliness Effect", "The Boredom Signal Effect"). Worth an A/B if title A underperforms.
- **Chapters deliberately stop at 9:18 of a 12:01 video.** The last chapter is the shift, and
  nothing after it is mapped, so the echo, the bridge, and the end-screen CTA stay unsignposted.
  Mapping the CTA would tell a viewer exactly when the essay ends.
- Citations: all six URLs were HTTP-checked before writing, and all six returned 200 on the first
  try, unlike project 10 where a course-page full text died. The Loftus and Palmer 1974 paper
  resolved cleanly through `doi.org/10.1016/S0022-5371(74)80011-3`, so the primary study is cited
  by DOI rather than by an encyclopedia article. **Prefer the DOI when the script's central
  experiment has one**; use Wikipedia for the researcher or the named effect around it.
- The script's `FIGURE CORRECTION` in `script/references/memory.md` was honoured here: the
  description does not quote speed figures at all, so the mispaired 40.8-versus-31.8 numbers from
  topic memory had no route into a published artifact.

## Project 12 (2026-08-29), one stranger's comment - the citation list is longer than usual and every DOI was confirmed by content, not by status code

7 chapters, 20 hashtags, 36 tags, all five titles 52 to 53 characters, 3 fenced blocks. Every
chapter timestamp grepped back against `transcript.md` and present verbatim.

- **A 403 from a publisher is not a dead link, and a 200 is not proof the DOI is the right paper.**
  Project 11's note says to HTTP-check every URL first. Here the APA and PNAS DOIs both returned
  403 to curl, which is bot-blocking rather than rot, and a status check alone could not tell the
  difference. The fix that settles it in one call per DOI is the Crossref API,
  `https://api.crossref.org/works/<doi>`, which returns the title, journal and year, so the check
  becomes "does this DOI resolve to the paper the script actually cites" rather than "does the
  server answer a robot". All three confirmed: Bad is Stronger than Good, Review of General
  Psychology 2001; Negative information weighs more heavily on the brain, JPSP 1998; Emotion
  shapes the diffusion of moralized content in social networks, PNAS 2017. **Use Crossref for any
  DOI citation from now on and keep the status check only for encyclopedia and institution pages.**
- Eight sources, the longest list the channel has published, because this script names four
  studies plus two anthropologists. Gottman gets two entries on purpose: the 1992 JPSP paper for
  the dissolution prediction and his Wikipedia article for the five to one ratio itself, since the
  ratio is discussed across a body of work rather than one citeable experiment.
- **Recommended title A over C.** C is the search-friendly form the channel already publishes under
  ("The Loneliness Effect"), but the script's own hook is a count, ten against one, and A states
  the paradox as a question a tired viewer parses at a glance, which is the standing batch 8 steer.
  All five variants are within one character of each other, so the choice is entirely about shape.
- **Chapters stop at 7:31 of an 11:32 video**, the same deliberate choice as project 11. The last
  chapter is "Now open your phone", so the mismatch payoff, the shift, the echo and the end-screen
  tease all stay unsignposted rather than telling a viewer exactly when the essay ends.
- Watch the hashtag count check: `grep -o '#[a-z]*'` over the whole file reads 30 on a file with 20
  hashtags, because `*` allows zero letters and every markdown heading `#` matches. Use
  `grep -o '#[a-z]\+'` or count the hashtag line alone.

## Project 13 (2026-09-01), the psychology of being poor - ran AFTER `/thumbnail`, which inverts a standing lesson

7 chapters, 20 hashtags, 36 tags, all five titles 54 to 58 characters, 3 fenced blocks. Every
chapter timestamp grepped back against `transcript.md` and present verbatim.

- **The order was `/thumbnail` then `/metadata`, the reverse of the Lessons note below.** That note
  says to write the title first and hand it to `thumbnail` so the headline does not restate it. The
  owner invoked them the other way round, and it cost nothing here because `thumbnail` mines the
  script and the folder slug rather than the published title, and because its own rules already ban
  restating the title. The five headlines (`WHY THE BLANK BOX?`, `SAME MAN?`, `WHAT'S IN THE DARK?`,
  `REFUSING IS THE CRIME`, `WHO DO YOU ASK?`) were checked against chosen title A afterwards and
  none of them overlap. **When metadata runs second, check the existing headlines against the five
  title variants before recommending one**, and reject a title that collides with an already-written
  headline rather than rewriting the thumbnail set.
- **Recommended title A over C**, the same call as projects 11 and 12 and for the same reason: A is
  a question a tired viewer parses at a glance, and it is a near quote of the script's first line,
  which the hook resolves inside 30 seconds. C ("The Scarcity Effect: ...") is the search-friendly
  form the channel already publishes under and is the A/B alternative.
- Citations: four DOIs, all confirmed by content through the Crossref API per the project 12 rule,
  not by status code. Mani 2013 and Shah 2012 are both Science, Woodburn 1982 is the same
  `10.2307/2801707` project 10 used, and Peterson 1993 resolves through
  `10.1525/aa.1993.95.4.02a00050`. **Nicolas Peterson has no English Wikipedia article, it 404s**,
  so the DOI is the only citation route for demand sharing. Sahlins is cited through the
  `Original_affluent_society` article rather than his biography page, because the script uses the
  argument and not the man.
- The script names "bandwidth" as a term researchers use but never names the book it comes from, so
  Mullainathan and Shafir's `Scarcity` is cited as a sixth source for the vocabulary itself. Six
  sources for five named researchers.
- **Chapters stop at 8:17 of an 11:47 video**, the third project running with this deliberate cut.
  The fee loop, the shift, the echo and the tease all stay unsignposted.

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

## Project 14 (2026-09-04), the psychology of being ugly - the Crossref rule caught a WRONG paper, not just a blocked one

7 chapters, 20 hashtags, 36 tags, all five titles 40 to 56 characters, 3 fenced blocks. Every
chapter timestamp grepped back against `transcript.md` and present verbatim exactly once.

- **The project 12 Crossref rule earned itself here.** Every previous run used it to prove a
  403 was bot-blocking rather than rot. This run it caught an outright wrong citation. The
  Anderson 1992 body-shape review was first written as `10.1016/0162-3095(92)90032-Y`, which
  returns HTTP 200 and resolves to Boyd and Richerson, "Punishment allows the evolution of
  cooperation (or anything else) in sizable groups", same journal and same year. The correct DOI
  is `10.1016/0162-3095(92)90033-z`. **Sequential article suffixes inside one journal issue are
  the trap**: `90032` and `90033` differ by one character and both resolve, so a status check,
  a link checker, and a human eye all pass it. Only the returned title catches it.
- **Do not construct a DOI suffix from a pattern. Search Crossref by title instead.**
  `https://api.crossref.org/works?query.bibliographic=<words+from+the+title>&rows=5` returned
  the right paper as hit one with authors Anderson, Crawford, Nadeau and Lindberg. That is one
  call and it removes the guess entirely. Confirmed the other three the same way: Gilovich 2000
  JPSP, Mita 1977 JPSP, Langlois 1990 Psychological Science.
- **Judith Langlois has no English Wikipedia article, it 404s**, so the 1990 paper's DOI is the
  only citation route for the composite-face finding. Same situation as Nicolas Peterson on
  project 13. Six sources for six named researchers plus the named effect.
- **The obvious title A violated the guardrail, and so did its rewrite.** "Why Do You Think You
  Look Worse Than You Do?" and "Why Do You Think You Are Uglier Than You Are?" both name the
  takeaway, and worse, they name a takeaway **this script explicitly refuses**: "This is not a
  promise that you are secretly flawless and only need better lighting, and anyone selling you
  that is selling you something." A title that promises the reassurance the script spends a
  paragraph withholding is a clickbait failure even though it sounds like the channel's voice.
  **When the script names the false promise in order to reject it, the title cannot make that
  promise.** Resolved by picking a concrete lived moment instead: "Why Do You Hate Your Own Face
  In Photos?", 40 characters, the shortest primary title the channel has published.
- **Recommended title A over C**, the fourth project running, same reasoning: a question a tired
  viewer parses at a glance, naming a moment the viewer physically lived through this month. The
  script delivers it three separate ways, so a narrow-sounding title is under-promising rather
  than over-promising. C ("The Spotlight Effect: ...") is the search-friendly A/B alternative and
  the form the channel already publishes under.
- **Metadata ran after `/thumbnail` again, and the collision check needs a second question.**
  Project 13 established "check the existing headlines against the five title variants before
  recommending one". That catches restatement. It does not catch the fault found here: title E
  ("You Never Noticed Your Reflection Is The Wrong Way Round") states outright the mechanism that
  thumbnail 3 (`WHICH ONE IS YOU?`) exists to withhold, so pairing them would spoil the thumbnail
  before a viewer clicks. **Ask both questions: does the title restate a headline, and does the
  title answer one.** E is otherwise a strong variant, so it is kept in the table with the
  pairing noted rather than removed. Chosen title A collides with none of the five headlines and
  pairs especially well with thumbnail 3, which shows two prints without saying which is real.
- **Softened the emoji set for a tender topic, but only the one that had a soft equivalent.**
  `SKILL.md` says to pick a warmer set for unsettling subjects, so the call-to-action label is
  a white heart rather than the light bulb. Chapters kept the world-map icon, because the emoji
  has to signal what the section is before it is read. A mirror emoji would have been on-topic for this video and useless as a
  chapters marker. **Soften the register, never the function.**
- **Chapters stop at 7:45 of an 11:07 video**, the fourth project running with this deliberate
  cut. The scroll passage, the broken-measurement summary, the shift, the echo and the tease all
  stay unsignposted.
