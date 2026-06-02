# WIT Comedy-Core Pose Set

Classification: `Core channel asset structure`

Scope: `CHANNEL_WIDE`

This folder is the reusable comedy WIT layer for future `Why It Works` videos.
It does not apply to any existing video project.

## Purpose

The `comedy-core` pose set makes WIT work as:

- a funny reaction device
- a modern-life victim
- a suspicious viewer surrogate
- a reusable thumbnail character
- a punchline support system for money, internet, business, society, and modern-life explainers

Use this folder when WIT needs to look betrayed, suspicious, trapped, panicked, confused, defeated, or physically affected by the topic.

## Contact Sheet

- `contact-sheet.png`

The current contact sheet shows:

- `12` seeded poses copied from compatible `core-24` assets
- `4` required draw targets that do not yet have PNG assets

## Current Pose Inventory

| Required pose | Current file | Status | Source or next step |
|---|---|---|---|
| `deadpan-front` | `wit-pose-deadpan-front.png` | seeded | from `core-24/wit-pose-neutral-default.png`; refine later for stronger deadpan |
| `deadpan-side-eye` | `wit-pose-deadpan-side-eye.png` | seeded | from `core-24/wit-pose-smug-side-eye.png` |
| `suspicious-phone` | `wit-pose-suspicious-phone.png` | seeded / refine | from `core-24/wit-pose-suspicious-detective.png`; future redraw should include phone |
| `betrayed-by-phone` | `wit-pose-betrayed-by-phone.png` | seeded | from `core-24/wit-pose-phone-bill-panic.png` |
| `financially-attacked` | `wit-pose-financially-attacked.png` | seeded | from `core-24/wit-pose-money-panic.png` |
| `buried-in-receipts` | `wit-pose-buried-in-receipts.png` | seeded / redraw | from `core-24/wit-pose-receipt-evidence.png`; future redraw should bury WIT more clearly |
| `subscription-panic` | `wit-pose-subscription-panic.png` | seeded | from `core-24/wit-pose-phone-bill-panic.png` |
| `tiny-defeated` | `wit-pose-tiny-defeated.png` | seeded | from `core-24/wit-pose-tiny-defeated.png` |
| `fake-confident` | `wit-pose-fake-confident.png` | seeded / refine | from `core-24/wit-pose-awkward-celebration.png`; future redraw should feel more naively confident |
| `confused-math` | `wit-pose-confused-math.png` | seeded | from `core-24/wit-pose-confused.png`; add generic math marks in scene, not baked into character unless needed |
| `staring-at-viewer` | `wit-pose-staring-at-viewer.png` | seeded / refine | from `core-24/wit-pose-neutral-default.png`; future redraw should face camera more directly |
| `pointing-at-evidence` | `wit-pose-pointing-at-evidence.png` | seeded | from `core-24/wit-pose-pointing-right.png` |
| `holding-red-marker` | no PNG yet | draw required | WIT holds red marker for correction, underlines, crossed-out claims |
| `dragging-data-box` | no PNG yet | draw required | WIT drags a heavy generic data box or file archive |
| `trapped-in-app` | no PNG yet | draw required | WIT stuck inside a generic app frame, no real logos |
| `receipt-printer-victim` | no PNG yet | draw required | WIT attacked by a long receipt printer strip |

## Asset Requirements

Every final PNG in this folder should have:

- transparent background
- consistent WIT identity
- clear full-body or strong upper-body silhouette
- readable emotion at `25%` screen size
- no readable brand names
- no third-party logos
- no baked-in full scene background
- enough transparent margin for shake, bounce, and slight rotation
- filename format: `wit-pose-[pose-name].png`

Preferred export:

- `2048x2048 PNG`
- transparent background
- centered character

## Draw Requirements For Missing Poses

### `holding-red-marker`

WIT holds a red marker like he is about to correct a suspicious claim.
Expression: dry, skeptical, slightly annoyed.
Use for crossed-out labels, correction jokes, and evidence boards.

### `dragging-data-box`

WIT drags an oversized generic box labeled only with abstract marks or `DATA`.
Expression: tired and resentful.
Use for privacy, lock-in, switching costs, exports, backups, and platform dependency.

### `trapped-in-app`

WIT is stuck inside a generic rounded app window or phone frame.
Expression: trapped, annoyed, not smiling.
Use for habit loops, subscription traps, lock-in, and app dependency.

### `receipt-printer-victim`

WIT is being hit, wrapped, or overwhelmed by a long receipt strip.
Expression: betrayed or financially attacked.
Use for hidden fees, confusing pricing, subscriptions, and checkout reveals.

## Usage

Use with:

- `docs/branding/wit-channel-system.md`
- `common/assets/wit/usage-rules.md`

Do not copy these assets into `video-projects/` unless the user explicitly asks to apply the channel-wide system to a specific video project.
