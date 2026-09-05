#!/usr/bin/env python3
"""Convert SRT/VTT subtitles into the [MM:SS.SSS] transcript format.

Reads one or more subtitle files and prints lines like:

    [00:00.120] Your hand is already moving.
    [00:01.480] You didn't decide to do it.

Subtitle files already carry millisecond cue times, so nothing is invented here.
Pass --no-ms for the older whole-second [M:SS] form.

Multiple files are treated as consecutive parts of one recording, so part 2
continues where part 1 ended (override with --offset).

Examples:
    srt-to-timestamps.py part-1.srt part-2.srt part-3.srt -o t.txt
    srt-to-timestamps.py caption.vtt --min-dur 5 --max-chars 180
    srt-to-timestamps.py part-2.srt --offset 4:12
"""

import argparse
import re
import sys
from pathlib import Path

import tsfmt

ARROW_RE = re.compile(r"-->")


def parse_subtitles(path):
    """Parse an SRT or VTT file into [(start, end, text)], in file order."""
    raw = Path(path).read_text(encoding="utf-8-sig", errors="replace")
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    cues = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not ARROW_RE.search(line):
            i += 1
            continue

        left, _, right = line.partition("-->")
        start = tsfmt.parse_timecode(left)
        # VTT cue settings ride along after the end time: "00:02.000 align:start"
        end = tsfmt.parse_timecode(right.strip().split()[0]) if right.strip() else None
        if start is None or end is None:
            i += 1
            continue

        i += 1
        body = []
        while i < len(lines) and lines[i].strip():
            if ARROW_RE.search(lines[i]):  # malformed file: next cue started early
                break
            body.append(lines[i])
            i += 1

        text = tsfmt.clean(" ".join(body))
        if text:
            cues.append((start, end, text))

    if not cues:
        sys.exit(f"error: no subtitle cues found in {path}")
    return cues


def main():
    p = argparse.ArgumentParser(
        description="Convert SRT/VTT subtitles into [MM:SS.SSS] transcript lines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples:")[1],
    )
    p.add_argument("files", nargs="+", type=Path, help="SRT or VTT files, in order")
    p.add_argument("-o", "--output", type=Path, help="write here instead of stdout")
    p.add_argument(
        "--offset",
        action="append",
        default=[],
        metavar="TIME",
        help="start time for a file (M:SS or seconds); repeat per file. "
        "Default: each file continues from the previous file's last cue.",
    )
    p.add_argument(
        "--min-dur",
        type=float,
        default=0,
        metavar="SEC",
        help="merge cues until a line spans at least this long (0 = no merging)",
    )
    p.add_argument(
        "--max-chars",
        type=int,
        default=0,
        metavar="N",
        help="never let a merged line exceed this many characters (0 = no limit)",
    )
    p.add_argument(
        "--no-ms",
        action="store_true",
        help="drop milliseconds: [0:05] instead of [00:05.480]",
    )
    p.add_argument(
        "--pad",
        action="store_true",
        help="with --no-ms, zero-pad minutes: [00:05] instead of [0:05]",
    )
    p.add_argument(
        "--keep-repeats",
        action="store_true",
        help="keep rolling-caption duplicates instead of collapsing them",
    )
    args = p.parse_args()

    if len(args.offset) > len(args.files):
        sys.exit("error: more --offset values than files")

    offsets = []
    for i in range(len(args.files)):
        if i < len(args.offset):
            value = tsfmt.parse_offset(args.offset[i])
            if value is None:
                sys.exit(f"error: bad --offset value {args.offset[i]!r}")
            offsets.append(value)
        else:
            offsets.append(None)  # resolved below

    cues = []
    running_end = 0.0
    for path, offset in zip(args.files, offsets):
        if not path.is_file():
            sys.exit(f"error: no such file: {path}")
        part = parse_subtitles(path)
        shift = running_end if offset is None else offset
        cues.extend((start + shift, end + shift, text) for start, end, text in part)
        running_end = cues[-1][1]

    cues.sort(key=lambda c: c[0])
    if not args.keep_repeats:
        cues = tsfmt.dedupe(cues)
    cues = tsfmt.merge(cues, args.min_dur, args.max_chars)

    body = tsfmt.render(cues, args.pad, ms=not args.no_ms)
    if args.output:
        args.output.write_text(body, encoding="utf-8")
        total = cues[-1][1]
        print(
            f"{len(cues)} lines, {int(total // 60)}m{int(total % 60):02d}s "
            f"-> {args.output}",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(body)


if __name__ == "__main__":
    main()
