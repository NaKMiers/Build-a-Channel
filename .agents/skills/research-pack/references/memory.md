# Research Pack Skill Memory

This file stores memory specific to the `research-pack` skill.

Use `.agents/_shared/` for channel-wide systems and strategy.
Use this file for lessons about how this skill should select projects, research topics, verify sources, and produce useful evidence packs.

## Current Skill Standard

- Select the project before researching.
- Require a real, non-empty `projects/<slug>/00-topic-intake.md` before researching.
- If `00-topic-intake.md` is missing or empty, stop and ask the user to run `topic-intake` first.
- Smart-select a project only when context is clear or exactly one unfinished research-pack candidate exists.
- Ask the user to choose from unfinished projects when context is unclear.
- Prefer Codex option UI (`request_user_input` / AskUserOptions style) when available.
- Browse the web or YouTube every run because research facts and reference signals can change.
- Prefer the project-local vendored Browse skill at `.agents/skills/browse/`; fall back to global gstack browse only if needed.
- Write only `projects/<slug>/01-research-pack.md`.
- When `01-research-pack.md` is created, updated, or rerun, treat `02-script.md`, `03-packaging.md`, and later outputs as stale.
- Do not delete stale downstream outputs unless the user explicitly asks; otherwise tell the user to rerun downstream skills in order.
- Do not write script, packaging, visual plan, HyperFrames, voiceover, render, upload, or self-learning files.
- Treat research as evidence and specificity, not a link dump.
- Label facts, inferences, examples, and open questions clearly.
- Collect visual evidence and real-life objects, not only factual sources.
- Prioritize real internet image leads for visual references when the topic has real-world objects.
- Record source pages and visible license/source status for useful visual leads so `visual-plan` can decide direct asset, mockup target, inspiration only, or reject.
- Keep the channel influence-first and learner-friendly.

## Research Pack Output Standard

A good research pack should make the next script easy without writing it.

It should include:

- one working thesis
- source map with confidence and links
- `what people think`
- `what is actually happening`
- `why it keeps happening`
- explanation spine
- useful examples
- visual reference leads
- jokes and analogies
- English learner support
- safe claims, claims to avoid, and open questions
- clear next step boundary

## Project Selection Lesson

The user wants this skill to require a project before implementation.

Apply every run:

- If the active context clearly points to a project, use it and say why.
- If not, scan `projects/` for unfinished candidates.
- Ask the user to choose from candidate projects before browsing.
- Do not guess between multiple plausible projects.

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Created `research-pack` as step 2 of the sequential Why It Works video-production skill system.

Initial rules:

- select project first
- browse current sources
- write only `01-research-pack.md`
- include factual evidence, visual reference leads, English learner support, and safety notes
- keep skill-specific learning here and promote only reusable channel-wide lessons upward

### 2026-06-06 - Require Topic Intake And Stale Downstream

Classification: `Operational lesson`

Context:
The user clarified that each skill should require previous pipeline outputs before running, and rerunning an earlier step makes later steps stale.

Lesson:
`research-pack` must never run from a blank or implied topic. It requires `00-topic-intake.md`. Any research update makes script and later outputs stale.

Apply next time:

- require non-empty `projects/<slug>/00-topic-intake.md`
- if missing, stop and ask the user to run `topic-intake`
- after writing `01-research-pack.md`, list stale downstream outputs from `02-script.md`, `03-packaging.md`, `04-voiceover.md`, and later files through `09-self-learning.md`
- do not delete stale files unless the user explicitly asks
- otherwise tell the user to rerun downstream skills in order, starting with `script-draft`

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-07 - Research Should Feed Real Visual References

Classification: `Research pack lesson`

Context:
The user clarified that real internet images make videos feel closer to viewers, while generated-only references can feel artificial.

Lesson:
Research packs should collect real visual leads, not just factual sources. For real-world topics, gather source-page links for ordinary objects, receipts, desks, products, screens, or environments that can later anchor the visual plan.

Apply next time:

- prioritize real image leads before generated-image ideas
- record source page, creator/publisher, and visible license/source status when available
- flag logo/private-data/copyright risks early
- describe why each real image lead could become a board, mockup, or texture reference

Promote to shared memory:
no; shared visual-production rules already contain the channel-wide standard.

### 2026-06-21 - Search Engines Bot-Blocked; Fetch Known Sources Directly

Classification: `Operational lesson`

Context:
While researching `why-everyone-pretends-to-be-busy`, Google, DuckDuckGo, and Bing all served
CAPTCHA / bot challenges from this IP, so no result lists could be scraped. YouTube reference
search (used in topic-intake) still worked.

Lesson:
When general search engines are blocked, do not stall or invent sources. Navigate the browse
tool **directly** to known credible URLs for the topic and confirm each by reading its title/text.
Academic publishers (JCR/OUP, etc.) are often Cloudflare-gated (403) — cite the study through a
reachable secondary source (e.g. HBR summarizing the JCR paper) and mark the primary as medium
confidence / verify-before-quoting.

Apply next time:

- If search engines challenge, switch to direct-URL fetches of authoritative pages (HBR, official
  company research/WorkLab pages, gov/edu, reputable explainers) and confirm by title/text read.
- Mark each source `direct-fetch confirmed` vs `cited via secondary` and set confidence accordingly.
- Keep YouTube demand/reference search separate — it may still work when web search is blocked.
- Record the blocking in the pack's browsing note and set an honest overall Reference confidence.
- Never invent stats; route any number that could not be confirmed live into `Open Questions`.

Promote to shared memory:
no; this is a research-pack browsing-resilience tactic, not a channel-wide strategy change.

## Feedback Entry Template

Use this shape when updating the skill after user review:

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Research pack lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
