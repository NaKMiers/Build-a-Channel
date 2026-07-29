#!/usr/bin/env python3
"""Concatenate narration MP3 parts into one file, and report each part's duration.

A multi-part recording needs two things before the transcript stage can run:

  1. A single audio file the editor can scrub against, `audios/full.mp3`, so the
     timestamps in `transcribes/transcript.md` refer to one timeline.
  2. The exact duration of every part, so word timings aligned per part land in the
     right place on that timeline.

This does both with no external binaries. ffmpeg is not required, and neither is any
pip package: MPEG audio frames are self-contained, so a byte-level concatenation of
the frame data is a valid MP3. Tags are stripped from every part (ID3v2 at the head,
ID3v1 and APE at the tail) so no decoder trips over metadata sitting mid-stream, then
the first part's ID3v2 tag, if it had one, is written back at the front.

Durations are summed from real frame headers, so parts at different bitrates and VBR
parts are both measured correctly. See tools/mp3frames.py.

Parts recorded at different bitrates make the result a VBR stream, so the combined file
gets a rewritten Xing header carrying the true frame count and a seek table. Without
that a player reads the first frame's bitrate, extrapolates it across the whole file,
and reports the wrong length: 256 kbps followed by two 128 kbps parts showed 8m28s for
a 12m07s recording. The last line of output states what a player will report, and the
tool refuses to write a file whose header disagrees with its frames.

Examples:
    combine-audio.py projects/3-slug/audios/part-*.mp3
    combine-audio.py part-1.mp3 part-2.mp3 -o full.mp3 --json offsets.json
    combine-audio.py part-1.mp3 part-2.mp3 --dry-run
"""

import argparse
import json
import sys
from pathlib import Path

import mp3frames
from mp3frames import fmt


def main():
    p = argparse.ArgumentParser(
        description="Concatenate MP3 narration parts and report their durations.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples:")[1],
    )
    p.add_argument("audio", nargs="+", type=Path, help="MP3 parts, in read order")
    p.add_argument("-o", "--output", type=Path,
                   help="write the combined MP3 here (default: full.mp3 beside the parts)")
    p.add_argument("--json", type=Path, metavar="PATH",
                   help="also write per-part durations and cumulative offsets here, "
                        "for audio-to-timestamps.py --offsets")
    p.add_argument("--dry-run", action="store_true",
                   help="measure and report only, write nothing")
    p.add_argument("--force", action="store_true",
                   help="overwrite the output if it already exists")
    args = p.parse_args()

    for path in args.audio:
        if not path.is_file():
            sys.exit(f"error: no such file: {path}")

    output = args.output or args.audio[0].parent / "full.mp3"
    if output.resolve() in {a.resolve() for a in args.audio}:
        sys.exit(f"error: output {output} is also an input. Pick another name.")
    if output.exists() and not (args.force or args.dry_run):
        sys.exit(f"error: {output} exists. Pass --force to overwrite.")

    lead_tag, chunks, parts, offset = b"", [], [], 0.0
    rates, all_bitrates = set(), set()
    for i, path in enumerate(args.audio):
        tag, audio = mp3frames.strip_tags(path.read_bytes())
        offsets, samples, rate, bitrates = mp3frames.scan(audio, path.name)
        seconds, frames = samples / rate, len(offsets)
        rates.add(rate)
        all_bitrates |= set(bitrates)
        if i == 0:
            lead_tag = tag
        chunks.append(audio)
        parts.append({"file": str(path), "start": round(offset, 3),
                      "duration": round(seconds, 3), "frames": frames,
                      "sample_rate": rate, "bitrates": sorted(bitrates)})
        mix = "/".join(str(b) for b in sorted(bitrates))
        print(f"[{i + 1}/{len(args.audio)}] {path.name}: {fmt(seconds)}, "
              f"starts at {fmt(offset)}, {frames} frames @ {rate} Hz, {mix} kbps",
              file=sys.stderr)
        offset += seconds

    if len(rates) > 1:
        print(f"warning: mixed sample rates {sorted(rates)}. A byte concatenation still "
              "decodes, but re-encode with ffmpeg if the editor complains.",
              file=sys.stderr)
    if len(all_bitrates) > 1:
        print(f"note: parts differ in bitrate {sorted(all_bitrates)} kbps, so the result "
              "is a VBR stream. Writing a Xing header with the true duration and a seek "
              "table, otherwise players would extrapolate the first part's bitrate and "
              "report the wrong length.", file=sys.stderr)

    print(f"total: {fmt(offset)} across {len(parts)} parts", file=sys.stderr)

    if args.dry_run:
        return

    if args.json:
        args.json.write_text(
            json.dumps({"total": round(offset, 3), "parts": parts}, indent=2) + "\n",
            encoding="utf-8")
        print(f"offsets -> {args.json}", file=sys.stderr)

    stream = mp3frames.write_vbr_header(b"".join(chunks), output.name)
    output.write_bytes(lead_tag + stream)

    size = output.stat().st_size / 1_000_000
    reported = mp3frames.reported_duration(stream)
    print(f"{fmt(offset)}, {size:.1f} MB -> {output}", file=sys.stderr)
    if reported is not None:
        print(f"players will report {fmt(reported)} from the Xing header "
              f"(true length {fmt(offset)})", file=sys.stderr)
        if abs(reported - offset) > 1.0:
            sys.exit(f"error: the header says {fmt(reported)} but the frames say "
                     f"{fmt(offset)}. Refusing to leave a misleading {output.name}.")


if __name__ == "__main__":
    main()
