#!/usr/bin/env bash
#
# style-strings.sh - export the four verbatim prompt strings, extracted at runtime
# from their single definition in .agents/rules/visual-style.md.
#
# Skills source this instead of hard-coding the strings, so there is exactly one
# editable copy in the repo and no verification pattern can drift out of sync with
# the definition it is supposed to be checking.
#
# Usage:
#   source .agents/bin/style-strings.sh
#   grep -cF "$STYLE_LOCK" projects/1-*/prompts/image-prompts.md
#
# Exports: STYLE_ANCHOR, STYLE_LOCK, GENERATION_LINE, SHEET_OPENING_LINE

_ss_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
_ss_src="$_ss_root/.agents/rules/visual-style.md"

[ -f "$_ss_src" ] || { echo "style-strings.sh: cannot find $_ss_src" >&2; return 1 2>/dev/null || exit 1; }

# Pull the first fenced block that follows a given "### <HEADING>" line.
_ss_block() {
  awk -v h="### $1" '
    $0 == h { found = 1; next }
    found && /^```/ { fence++; if (fence == 1) next; else exit }
    found && fence == 1 { print }
  ' "$_ss_src"
}

STYLE_ANCHOR="$(_ss_block 'STYLE ANCHOR - opens every image and thumbnail prompt')"
STYLE_LOCK="$(_ss_block 'STYLE LOCK - closes every image and thumbnail prompt')"
GENERATION_LINE="$(_ss_block 'GENERATION LINE - the instruction the human adds to every generation')"
SHEET_OPENING_LINE="$(_ss_block 'REFERENCE SHEET OPENING LINE - opens every character sheet prompt')"

export STYLE_ANCHOR STYLE_LOCK GENERATION_LINE SHEET_OPENING_LINE

# Explicit checks rather than ${!var} indirection, which bash supports and zsh does not.
[ -n "$STYLE_ANCHOR" ]       || echo "style-strings.sh: WARNING STYLE_ANCHOR is empty" >&2
[ -n "$STYLE_LOCK" ]         || echo "style-strings.sh: WARNING STYLE_LOCK is empty" >&2
[ -n "$GENERATION_LINE" ]    || echo "style-strings.sh: WARNING GENERATION_LINE is empty" >&2
[ -n "$SHEET_OPENING_LINE" ] || echo "style-strings.sh: WARNING SHEET_OPENING_LINE is empty" >&2
