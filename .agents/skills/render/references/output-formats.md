# Render Output Formats

Use these shapes when running the `render` skill.

## 06 Production Board

Write or update:

```text
projects/<slug>/06-production-board.md
```

````markdown
# 06 Production Board

Video: `<title>`

Status: `section render in progress`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 |  |  | reserved |

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Render file | Notes |
|---:|---|---|---:|---|---|---|---|---|

## Shared Asset Rules

- Video-level assets:
- Section asset junction rule:
- Attribution file:

## Active Section Notes

## Stale / Regeneration Notes

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
````

## Section Implementation Notes

Write when useful under:

```text
projects/<slug>/section-previews/section-XX-kebab-section-name/IMPLEMENTATION.md
```

````markdown
# Section X Render Implementation

Video:
`<title>`

Section:
`Section X: <name>`

Status:

## Result

- Preview project:
- Source:
- Port:
- Studio URL:
- Direct composition URL:
- Runtime:
- Voiceover:
- Visual plan:

## Board Plan Implemented

| Board | Local Time | Voice Cue | Visual | Key Animation | Source Plan |
|---|---:|---|---|---|---|

## Voice Sync Map

| Time | Spoken Cue | On-Screen Element | Action | Sync Status |
|---:|---|---|---|---|

## Transition Plan

| From | To | Transition | Reason | Sync Risk | Decision |
|---|---|---|---|---|---|

## Element Motion Notes

- Entrances:
- Holds:
- Emphasis:
- Exits:
- Repeated effects avoided:

## Assets

- Shared asset folder:
- Section assets:
- Attribution:

## Verification

- lint:
- validate:
- inspect:
- render:

## Notes
````

## Chat Response

````markdown
Done. I created/updated:

[06-production-board.md](<absolute path>)

Section target: `<All or Section X: name>`

Status: `<status>`

Preview servers:

| Section | Port | Studio URL | Direct URL | Checks |
|---|---:|---|---|---|

Generated:

| Section | Preview Project | Source | Render File | Notes |
|---|---|---|---|---|

Stale downstream:

- <file or none>
````
