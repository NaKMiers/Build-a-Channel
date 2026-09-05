#!/usr/bin/env bash
#
# cue-times.sh - derive the [M:SS] stamps that image prompts and scene file names use
# from a transcript, whichever shape that transcript is in.
#
# transcribes/transcript.md carries [MM:SS.SSS], because forced alignment returns real
# onsets to the millisecond and the editor cuts at that resolution. prompts/image-prompts.md
# carries [M:SS], because the scene images on disk are named from it ([3:20] -> [3-20].jpg)
# and those names must not move. The derivation between the two is plain truncation.
#
# Skills source this instead of writing their own awk or sed, for the same reason they
# source style-strings.sh: a check that drifts from the thing it is checking is worse
# than no check. tools/tsfmt.py to_mss() is the Python side of this same rule.
#
# Usage:
#   source .agents/bin/cue-times.sh
#   cue_stamps "$P/transcribes/transcript.md"            # one [M:SS] per cue, in order
#   diff <(cue_stamps "$T") <(grep -o '^\[[0-9:]*\]' "$F")
#   cue_stamps "$T" | sort | uniq -d                     # collisions after truncation
#
# Legacy whole-second transcripts (projects 1 through 13) pass through unchanged, so
# the same command works on every project in the repo.
#
# Exports: cue_stamps, cue_dups

# Emit the [M:SS] stamp of every cue line, one per line, in file order.
# A line that is not a well-formed cue emits [MALFORMED] and warns, so the stream stays
# the same length as the transcript and a diff points straight at the offending line.
cue_stamps() {
  [ -f "$1" ] || { echo "cue_stamps: no such file: $1" >&2; return 1; }
  awk '
    {
      if (match($0, /^\[[0-9]+:[0-9][0-9](\.[0-9]+)?\] ./)) {
        end = index($0, "]")
        ts = substr($0, 2, end - 2)          # 00:03.480  or  0:03
        c = index(ts, ":")
        printf "[%d:%s]\n", substr(ts, 1, c - 1), substr(ts, c + 1, 2)
      } else if (NF) {
        printf "[MALFORMED]\n"
        printf "cue_stamps: %s line %d is not a cue: %s\n", FILENAME, FNR, $0 > "/dev/stderr"
      }
    }
  ' "$1"
}

# Stamps that more than one cue truncates to. These are the collisions /scenes has to
# remap when it names an image, and they are invisible in the transcript itself.
cue_dups() {
  cue_stamps "$1" | sort | uniq -d
}

export -f cue_stamps cue_dups 2>/dev/null || true
