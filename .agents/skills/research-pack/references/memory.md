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

### 2026-06-23 - Wikipedia Is The Reliable Fallback When Search + Primary Sites Are Blocked

Classification: `Operational lesson`

Context:
While researching `why-everything-is-a-subscription-now`, Google served a CAPTCHA and `ftc.gov`
returned an automated-request block, same as the earlier `why-everyone-pretends-to-be-busy` run.
Wikipedia article pages loaded fine and gave well-sourced, quotable background (subscription
business model; negative option billing).

Lesson:
When general search and primary/regulator sites are bot-blocked, Wikipedia article bodies are the
most dependable direct-fetch source for mechanism/definition/history. Two tactics: (1) `browse text`
returns nav/sidebar chrome — instead read `document.querySelector('.mw-parser-output').innerText` and
strip `[N]` footnote markers; (2) use Wikipedia's own search (`/w/index.php?search=...&fulltext=1`)
to find the right article title when a guessed slug 404s to the "sister projects" stub.

Apply next time:
- Prefer Wikipedia for definitions/mechanism/history when search + primary sites are blocked.
- Extract `.mw-parser-output` innerText, not the whole-page `text`; keep regexes simple (complex
  grep over the full body timed out once — slice around a keyword index with JS instead).
- Still route time-sensitive facts (a current regulation status, a brand's current price) to Open
  Questions for a live re-check; Wikipedia is good for background, not for "as of today" status.

Promote to shared memory:
no; this is a research-pack browsing-resilience tactic, not a channel-wide strategy change.

### 2026-06-24 - Commons MediaSearch Is Thin For Specific Retail Signage; Treat As Mockup Target

Classification: `Research pack lesson`

Context:
Researching `why-buy-1-get-1-beats-50-off`. Wikipedia article bodies direct-fetched cleanly
again (BOGO, Loss leader, Anchoring effect, Predictably Irrational) and gave a strong, citable
mechanism (Tabarrok: shoppers value the 2nd unit less; Ariely: the FREE effect; Wedgwood
history; food-waste/overspend criticism). Investopedia returned an automated-access block.
Wikimedia Commons MediaSearch found a perfect real "50% off" tag (`Two cuts of cheese marked
down 50 percent.jpg`) and baskets/trolleys, but NO clean "buy one get one free" sign.

Lesson:
For a pricing/marketing topic, the *mechanism* grounds well from Wikipedia + a named
behavioral-econ source (Ariely/Kahneman). For specific real-world signage/POS/receipt photos,
Commons MediaSearch is hit-or-miss — do not stall hunting for a perfect real photo of a specific
sign. Record the one or two license-clear reals you do find as `safe asset (verify license)`, and
mark the rest as `mockup target / self-shot`, which suits the channel's self-made CSS-tag +
handwritten-label style anyway (the hero "two tags" motif is built, not copied).

Apply next time:
- Ground mechanism from Wikipedia bodies + a named source; ground exact stats only if verifiable
  live, else route to Open Questions (did this for category gross-margins and Ariely's numbers).
- Try Commons MediaSearch for hero real objects, but cap the effort; missing signage -> mockup target.
- Keep a "must stay honest" inheritance: carry the topic-intake math caveat into Safe Claims /
  Claims To Avoid (BOGO ~2x profit only on high margin + both units; on cheap staples it's a loss leader).

Promote to shared memory:
no; this is a research-pack browsing/visual-leads tactic, not a channel-wide strategy change.

### 2026-06-25 - One Wikipedia Article Can Carry Both The Spine AND The Honest Reversal

Classification: `Research pack lesson`

Context:
Researching `why-everything-costs-9-99` (charm pricing). Search engines bot-blocked again; the
single Wikipedia "Psychological pricing" article body direct-fetched cleanly and supplied the entire
spine: left-digit effect (Thomas & Morwitz 2005 = anchoring on the leftmost digit), the two-process
model (Stiving & Winer 1997: level effect + image effect), the "~60% of prices end in 9" stat, the
gasoline 9/10-cent example, AND the channel's needed honest counter-turn ("high-end retailers and
restaurants price in round/even numbers for brand image"). The famous Anderson & Simester (2003)
"$39 outsold $34" field experiment was NOT on the page and is paywalled → routed to Open Questions.

Lesson:
For a pricing/behavioral-econ topic, the matching Wikipedia article often carries not just the
mechanism but also the built-in reversal/caveat the channel needs for its honest back-half turn —
read the WHOLE body (including "criticism"/"controversy"/"high-end" lines), not just the intro,
before deciding the source is thin. The single most famous empirical proof of an effect frequently
has NO standalone Wikipedia article and sits behind a paywall; cite it as "a famous field study
found…" and route exact figures to Open Questions rather than stalling or inventing numbers.

Apply next time:
- Slice the full `.mw-parser-output` innerText in chunks; scan for the honest counter-turn explicitly.
- Carry the topic-intake "Must Stay Honest" guardrails straight into Safe Claims / Claims To Avoid.
- Famous named experiment + paywall → secondary framing + Open Questions, never an invented stat.

Promote to shared memory:
no; this is a research-pack sourcing tactic, the channel-wide Wikipedia-fallback rule already exists.

### 2026-06-26 - Charm-pricing re-research: Commons DID have real 99¢ tags; typography gem grounds the motif

Classification: `Research pack lesson`

Context:
Re-created `01-research-pack.md` for `why-everything-costs-9-99` (the prior folder was deleted; only
the intake had ever been committed, so no research pack existed to recover). The Wikipedia
"Psychological pricing" body direct-fetched cleanly again and was even richer than the 2026-06-25 note
recalled. Unlike the BOGO run (where Commons had no clean signage), Commons MediaSearch this time
returned several license-clear real hero objects: `Price Tag 99+TX 99 cents`, `Kiwi shoe polish tan
99 cent`, `99¢ Rocks`, plus real gas-price signs (`Union 76`, `Wawa`) that literally show the 9/10¢
ending. Keith Coulter's line ("effect may be enhanced when the cents are printed SMALLER") is direct
grounding for the channel's mouse-type `.99` visual motif — a research fact that hands the visual plan
its hero device. Routed Anderson & Simester (2003) "$39 outsold $34" to Open Questions (paywalled).

Lesson:
For a charm-pricing / `.99` topic specifically, Commons has usable real `99¢` tags and gas signs — try
it before defaulting everything to mockup. And scan the mechanism source for a line that grounds the
chosen VISUAL motif (here: smaller-cents typography), not just the verbal claim — it makes visual-plan
nearly free.

Apply next time:
- For pricing-signage topics, run a Commons MediaSearch on the exact number/word ("99 cent", "gas price
  sign"); keep the license-clear reals as `safe asset (verify license)`, rest as mockup target.
- Pull out any source line that justifies the hero visual device, not only the headline fact.
- Famous paywalled proof (Anderson & Simester) -> "a famous field study found…" + Open Questions.

Promote to shared memory:
no; this is a research-pack sourcing/visual-leads tactic, not a channel-wide strategy change.

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
