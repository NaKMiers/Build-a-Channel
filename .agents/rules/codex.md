# Codex Rules

## Startup

Read the startup files listed in `AGENTS.md` before strategy, production planning, or persistent memory updates.

## Browsing

Use the gstack `/browse` skill for web browsing in this workspace.

Do not use `mcp__claude-in-chrome__*` tools.

## Editing

- Keep edits scoped to the current request.
- Do not delete or rewrite user work casually.
- Preserve the channel identity unless the user explicitly changes it.
- Treat `.agents/_shared/` as the shared brain.
- Treat `projects/<slug>/` as the active source of truth for one video.

## Skills

`.agents/skills/` stores executable skills only.

Do not create the sequential production skills until the user asks for the skill-creation phase.
