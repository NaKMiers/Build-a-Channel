# Codex Rules

## Startup

Read the startup files listed in `AGENTS.md` before strategy, production planning, or persistent memory updates.

## Browsing

Use the project-local `/browse` skill in `.agents/skills/browse/` for web browsing in this workspace when available.

If the project-local browse skill is missing or cannot run, fall back to the global gstack `/browse` skill.

Do not use `mcp__claude-in-chrome__*` tools.

## Editing

- Keep edits scoped to the current request.
- Do not delete or rewrite user work casually.
- Preserve the channel identity unless the user explicitly changes it.
- Treat `.agents/_shared/` as the shared brain.
- Treat `projects/<slug>/` as the active source of truth for one video.

## Skills

`.agents/skills/` stores executable skills only.

`topic-intake` and `research-pack` now exist as the first two sequential video-production skills.

Do not create additional sequential production skills until the user asks for the next skill-creation phase.
