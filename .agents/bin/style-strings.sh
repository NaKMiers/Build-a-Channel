#!/usr/bin/env bash

# Export the two current HumanPrice prompt strings from visual-style.md.

_hp_rules="${1:-.agents/rules/visual-style.md}"

STYLE_STRING=$(awk '/Use this exact style string/{getline; getline; gsub(/^`|`$/, ""); print; exit}' "$_hp_rules")
GENERATION_STRING=$(awk '/Use this exact generation string/{getline; getline; gsub(/^`|`$/, ""); print; exit}' "$_hp_rules")
CURRENT_STYLE_VERSION="HumanPrice-current"

export STYLE_STRING GENERATION_STRING CURRENT_STYLE_VERSION

[ -n "$STYLE_STRING" ] || echo "style-strings.sh: WARNING STYLE_STRING is empty" >&2
[ -n "$GENERATION_STRING" ] || echo "style-strings.sh: WARNING GENERATION_STRING is empty" >&2
