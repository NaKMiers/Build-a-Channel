# HumanPrice research standards

Canonical source for evidence quality. Read this before running `research`, `script`,
`metadata`, or `check`.

## Evidence target

Each episode uses 6 to 10 relevant sources. At least 3 must be primary or official, such as a
regulator, law, company filing, official dataset, original research paper, or recognized
industry body. More sources do not rescue weak sources.

## Source order

Prefer sources in this order:

1. Laws, regulators, official statistics, company filings, and first-party policy pages.
2. Original research papers and recognized research institutions.
3. Industry reports with a disclosed method.
4. High-quality reporting that links to its evidence.
5. Secondary explainers used only for orientation.

Do not use search snippets, unsourced listicles, anonymous AI summaries, or a competitor video as
the final authority for a factual claim.

## Claim types

Every material claim in the research brief is one of:

- `FACT` - directly reported by a source.
- `ESTIMATE` - a source's modeled or surveyed estimate.
- `INFERENCE` - a conclusion derived from two or more sourced facts.
- `ILLUSTRATION` - hypothetical math used to explain a mechanism.

Never present an estimate, inference, or illustration as a reported fact.

## Required context for numbers

Every exact number records:

- source
- source date or fiscal year
- geography
- population or market definition
- unit and currency
- nominal or inflation-adjusted status when relevant
- whether it is a fact, estimate, inference, or illustration

If any field materially changes the meaning and is unknown, do not use the number.

## Exact-number titles

An exact number may appear in a title only when:

1. The claim ledger contains the same number.
2. A primary or official source supports it directly.
3. The script explains its scope and definition.
4. The number is not a fragile extrapolation from unrelated averages.
5. The claim remains true at packaging time.

Otherwise use a contradiction title.

## Behavioral research

- Name the actual mechanism, not a pop-psychology label.
- Record the study population and setting when they limit generalization.
- Do not turn correlation into causation.
- Do not use one laboratory result as proof of a universal law.
- Prefer meta-analyses, replications, field studies, or converging evidence when available.

## Financial and legal boundaries

- Explain systems, incentives, and tradeoffs, not personalized advice.
- Date laws and platform policies because they change.
- State the jurisdiction.
- When a rule differs by region, say so rather than universalizing one market.
- For high-stakes claims, verify again when metadata is produced.

## Research brief contract

`projects/<n>-<slug>/research/research-brief.md` contains:

1. Working title and central question.
2. Familiar moment.
3. Common belief.
4. Contradiction.
5. One-sentence reframe.
6. Unit economics.
7. Incentive map.
8. Behavioral engine.
9. Hidden system and mid-video reveal.
10. Case study.
11. Counterargument and boundary conditions.
12. Human price.
13. Claim ledger.
14. Source list.

The script may simplify the brief, but may not add a material fact or exact number that is absent
from its claim ledger.

## Citation format

Use Markdown links in the source list. The claim ledger uses stable source IDs such as `S01`.
Link to the supporting page, report, filing, dataset, or paper, not a search results page.

## Final evidence check

Before approving a brief:

- every material factual claim has a source ID
- every exact number has full context
- all arithmetic recomputes correctly
- totals and percentages use the same denominator
- rounding is disclosed when components do not sum exactly
- facts, estimates, inferences, and illustrations are labeled
- the counterargument is represented fairly
- no source is cited for a claim it does not support
