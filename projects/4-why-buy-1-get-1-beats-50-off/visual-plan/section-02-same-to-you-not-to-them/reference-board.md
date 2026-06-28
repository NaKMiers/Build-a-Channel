# Section 2 Reference Board

## Reference Pass Status

- Status: `real CC-licensed photos sourced, viewed, classified`
- Browsed references: Openverse API + Wikimedia Commons API
- Real images saved: 4 bases (register reused for Scene D callback)
- Generated images: none (no generator connected)
- Inspected local assets: shared WIT poses; reused S1's USD cash base
- Prompt-only fallbacks: none

## Search / Browse Notes

- Found actual **Josiah Wedgwood blue jasperware** on Wikimedia (CC0, Chazen Museum) - the exact maker the script names; ideal for the Wedgwood beat.
- Vintage cash register (CC BY 2.0) is a clean, brand-free "behind the counter" base with numbered keys that suit a math section.
- Rising coin stacks (CC0) literally show "double," reinforcing the BOGO profit beat.
- Rejected the Konsum storefront (crowd of real faces) per the no-face rule.

## References

| Ref | Type | Source | Classification | Why useful | Use in production | Saved path |
|---|---|---|---|---|---|---|
| Old cash register | real photo | Wikimedia CC BY 2.0 | safe asset (credit) | "behind the counter" | Scene A + D base | `base-a-counter-register.jpg` |
| Pink piggy bank | real photo | rawpixel CC0 | reject (tried then reverted 2026-06-24; owner: "even worse") | - | not used | `base-a-piggy-bank.jpg` |
| USD cash pile | real photo | rawpixel CC0 | safe asset | money / 50% off math | Scene B base | `base-b-cash-usd.jpg` |
| Rising coin stacks | real photo | Wikimedia CC0 | safe asset | profit doubling | Scene C base | `base-c-coins-rising.jpg` |
| Wedgwood jasperware | real photo | Wikimedia CC0 | safe asset | the literal Wedgwood reference | Scene E base | `base-e-wedgwood.jpg` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real Reference | Production Decision | Remaining Gap |
|---|---|---|---|---|
| A - behind counter | a real counter/register | cash register | direct base + CSS sells/cost tags | none |
| B - 50% off math | money | USD cash | direct base + CSS subtraction card | none |
| C - BOGO doubling | money that grows | rising coins | direct base + CSS subtraction + DOUBLE stamp | none |
| D - verdict / unchanged sign | counter callback | register (reused) | direct base + CSS $10 tag + you/store split | none |
| E - Wedgwood / old trick | antique pottery | Wedgwood jasperware | direct base + CSS "1700s" + sucker ticket | none |

## Rejected References

- Konsum storefront - crowd of real people (no-face channel).
- Misc vase series - generic; superseded by the actual Wedgwood piece.
