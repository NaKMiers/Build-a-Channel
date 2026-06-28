# Section 1 Reference Board

## Reference Pass Status

- Status: `real CC-licensed photos sourced, viewed, classified`
- Browsed references: Openverse API + Wikimedia Commons API (Google/Bing/DDG/Pexels bot-blocked on this network)
- Real images saved: 5 (3 chosen bases + 1 hero element + 1 alt)
- Generated images: none (no image generator connected this session)
- Inspected local assets: shared WIT pose library `.agents/_shared/assets/wit/poses/`
- Prompt-only fallbacks: none
- Fallback reason: n/a - real photos were available and accepted

## Search / Browse Notes

- Openverse queries: "supermarket shelf grocery store aisle", "pile of cash money dollars", "magician top hat magic" (empty), "top hat", "empty grocery store shelves", "shopping cart supermarket", "retail shelf boxes".
- Wikimedia queries: "magician top hat", "red theater curtain stage", "stack of cash banknotes".
- Brand traps hit and avoided: snack/liquor/detergent aisles all carried recognizable brand logos → rejected for direct use per the no-incidental-logo rubric.
- The magic top hat photo is shot with white gloves + wand (NO face) - safe for the no-face channel and almost exactly the script's "pulled out of a magician's hat" beat.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| Shopping cart in store | real photo | Wikimedia `Shopping_Cart_Supermarket.jpg` (CC0) | safe asset | instantly reads "store/shopping" | grounds Scene A as a real store | Scene A base | `assets/visual-references/section-01-hook/base-a-shopping-cart.jpg` |
| USD cash pile | real photo | rawpixel `sv155879` (CC0) | safe asset | "money / store profit / five bucks" | vivid on-topic money base | Scene B base | `.../base-b-cash-usd.jpg` |
| Red theater curtain | real photo | Wikimedia `Curtain-939464.jpg` (CC0) | safe asset | "magic show / the trick is staged" | unifies the magic-trick frame | Scene C base | `.../base-c-red-curtain.jpg` |
| Magic top hat + gloves + wand | real photo | Wikimedia `Top-hat-red_01.jpg` (CC BY-SA 3.0) | safe asset (credit required) | literal "magician's hat" for the rabbit payoff | hero element WIT rises from | Scene C element | `.../base-c-magic-hat.jpg` |
| Euro cash | real photo | rawpixel `frmoney...` (CC0) | inspiration only / fallback | colorful money alt | fallback if USD reads weak | not used | `.../alt-cash-euro.jpg` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| A - store / two signs | a real store base to float two price signs on | shopping cart photo | none | direct base + CSS price-sign devices | none |
| B - profit reveal | money + a profit comparison | USD cash photo | none | direct base + CSS profit meter | none |
| C - magic trick / rabbit | magic-show backdrop + a hat WIT emerges from | red curtain + magic hat | none | direct base + hat element + giant WIT | none |

## Image Generation Prompts

Not used - no image generator is connected this session and real CC0/CC-BY-SA photos covered every big scene.

## Rejected References

- Snack aisle (Lay's / Pringles / Doritos visible) - recognizable brand logos.
- Liquor aisle (branded bottles, possible distant person) - brands + people risk.
- Detergent shelf (branded bottles) - brands.
- These were viewed then deleted from the active folder; not saved.
