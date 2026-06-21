# Section 1 Reference Board

## Reference Pass Status

- Status: `completed (real images sourced + viewed)`
- Browsed references: Wikimedia Commons API (4 search passes)
- Real images saved: 4 (`assets/visual-references/section-01-hook-the-busy-trap/`)
- Generated images: none (no image-generation tool available this session)
- Inspected local assets: shared WIT pose PNGs (`.agents/_shared/assets/wit/poses/`)
- Prompt-only fallbacks: none
- Fallback reason: n/a — real public-domain bases secured for every big scene

## Search / Browse Notes

- Google/DuckDuckGo/Bing are bot-blocked from this IP (seen in earlier steps), so the reference pass used the Wikimedia Commons API recipe directly (curl + `node -e`; no python/jq on this box).
- Searched: "cluttered desk smartphone", "minimalist desk notebook", "wall calendar", "busy office desk papers", "smartphone notification screen", "stack of paperwork documents", "home office desk papers work".
- Phone-screen results were all branded devices (Blackview, LG) → rejected.
- Each selected base was downloaded and VIEWED before committing (brand/people/sterility check), per the selection rubric.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| Wall calendar (3-month grid, red-boxed day) | Real photo | Commons, PD (Claudio Elias) | `safe asset` | Real month grid; lines read as cells now, cage bars later | Core motif; bookend (full calendar -> cage) | Direct base, Scene A + Scene C | `assets/visual-references/section-01-hook-the-busy-trap/sceneC-wall-calendar.jpg` |
| Minimalist desk (pencils, notebook, cup, small device) | Real photo | Commons, PD (US Virgin Islands gov) | `safe asset` | Calm, empty, quiet — the opposite of busy | Contrast scene for "sit quietly and think" | Direct base, Scene B | `assets/visual-references/section-01-hook-the-busy-trap/sceneB-minimal-desk.jpg` |
| Cluttered desk (papers, sticky notes, calculator, receipts) | Real photo | Commons, PD (EFTA) | `inspiration only` | Great "busy work" overload mood/composition | Mood only — informs the overlay density of Scene A | Do NOT use directly (Logitech + Casio brands, readable receipts) | `assets/visual-references/section-01-hook-the-busy-trap/sceneA-cluttered-desk.jpg` |
| Legal contract + pen | Real photo | Commons, CC BY 2.0 | `inspiration only` | Paper texture | Reads "legal contract", dark — not "overload" | Do NOT use directly | `assets/visual-references/section-01-hook-the-busy-trap/sceneA-alt-papers.jpg` |
| Channel topic-intake reference videos (Wonny, After Skool, Folks of Yore) | Video packaging | YouTube (recorded in `00-topic-intake.md`) | `inspiration only` | Demand/packaging for busyness explainers | Hook pacing/tone only | Do NOT copy any frame/layout | n/a |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| A — The overload | Full calendar overwhelmed by urgency | sceneC-wall-calendar.jpg (PD) | none | Direct base + HyperFrames red-dot/URGENT/inbox overlays | none |
| B — Sit quietly and think | Calm empty desk, room to breathe | sceneB-minimal-desk.jpg (PD) | none | Direct base + THINKING / LAZY? labels | none |
| C — The calendar cage | Calendar grid lines become cage bars | sceneC-wall-calendar.jpg (PD, callback) | none | Direct base, cooler grade + HyperFrames cage bars over the grid | none |

Differentiation note: Scenes A and C intentionally share the calendar base as a bookend callback (full calendar -> prison). They are differentiated by treatment: A is bright/red/overloaded (cells filling, dots swarming); C is cooler/darker with vertical cage bars and a trapped WIT. Scene B is a deliberately calm, distinct base in between.

## Image Generation Prompts

None generated this session (no image-generation tool). If support art is wanted later, prompts should be text-free, logo-free, 16:9, with empty label-safe areas.

## Rejected References

- Blackview / LG phone-screen photos — branded devices (no-logo rule).
- Historic/people desk photos from "home office" search (Maserati brothers, portraits) — people + off-topic (no-face channel).
