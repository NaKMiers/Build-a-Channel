#!/usr/bin/env python3
"""Render or validate SRT files from HumanPrice [M:SS] transcript cues."""

import argparse
import json
import re
import sys
from pathlib import Path

CUE = re.compile(r"^\[(\d+):(\d{2})\] (.+)$")
STAMP = re.compile(r"^(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})$")


def seconds(value: str) -> float:
    bits = value.strip().split(":")
    if len(bits) == 1:
        return float(bits[0])
    if len(bits) == 2:
        minutes, value_seconds = bits
        return int(minutes) * 60 + float(value_seconds)
    if len(bits) == 3:
        hours, minutes, value_seconds = bits
        return int(hours) * 3600 + int(minutes) * 60 + float(value_seconds)
    raise ValueError(f"invalid duration: {value}")


def srt_time(value: float) -> str:
    millis = round(value * 1000)
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def read_transcript(path: Path):
    cues = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = CUE.fullmatch(line)
        if not match:
            raise ValueError(f"{path}:{number}: expected [M:SS] narration")
        start = int(match.group(1)) * 60 + int(match.group(2))
        text = match.group(3).strip()
        if not text:
            raise ValueError(f"{path}:{number}: empty narration")
        if cues and start <= cues[-1][0]:
            raise ValueError(f"{path}:{number}: timestamps must increase")
        cues.append((start, text))
    if not cues:
        raise ValueError(f"{path}: no cues")
    return cues


def load_texts(path: Path, count: int):
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("cues")
    if not isinstance(data, list) or len(data) != count:
        raise ValueError(f"{path}: expected JSON array with exactly {count} strings")
    if any(not isinstance(text, str) or not text.strip() for text in data):
        raise ValueError(f"{path}: every translation must be a nonempty string")
    return [text.strip().replace("\n", " ") for text in data]


def render(args):
    cues = read_transcript(args.transcript)
    texts = load_texts(args.texts_json, len(cues)) if args.texts_json else [text for _, text in cues]
    final_end = seconds(args.final_end) if args.final_end else cues[-1][0] + 3.0
    if final_end <= cues[-1][0]:
        raise ValueError("final end must be after the last cue start")
    blocks = []
    for index, ((start, _), text) in enumerate(zip(cues, texts), 1):
        end = cues[index][0] - 0.01 if index < len(cues) else final_end
        if end <= start:
            raise ValueError(f"cue {index} has no positive duration")
        blocks.append(f"{index}\n{srt_time(start)} --> {srt_time(end)}\n{text}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"{args.output}: {len(cues)} cues, ends {srt_time(final_end)}")


def stamp_to_seconds(match, offset):
    return (int(match.group(offset)) * 3600 + int(match.group(offset + 1)) * 60 +
            int(match.group(offset + 2)) + int(match.group(offset + 3)) / 1000)


def validate(paths):
    for path in paths:
        blocks = [block.splitlines() for block in path.read_text(encoding="utf-8").strip().split("\n\n")]
        previous_end = -1.0
        for expected, block in enumerate(blocks, 1):
            if len(block) < 3 or block[0] != str(expected):
                raise ValueError(f"{path}: invalid cue number at block {expected}")
            match = STAMP.fullmatch(block[1])
            if not match:
                raise ValueError(f"{path}: invalid timestamp at block {expected}")
            start, end = stamp_to_seconds(match, 1), stamp_to_seconds(match, 5)
            if not start < end or start < previous_end:
                raise ValueError(f"{path}: overlapping or invalid timing at block {expected}")
            if not any(line.strip() for line in block[2:]):
                raise ValueError(f"{path}: empty text at block {expected}")
            previous_end = end
        print(f"{path}: valid {len(blocks)} cues")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transcript", type=Path, nargs="?")
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--texts-json", type=Path)
    parser.add_argument("--final-end", help="M:SS, H:MM:SS, or seconds")
    parser.add_argument("--validate", type=Path, nargs="+")
    args = parser.parse_args()
    try:
        if args.validate:
            validate(args.validate)
        elif args.transcript and args.output:
            render(args)
        else:
            parser.error("provide transcript and --output, or --validate")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        sys.exit(f"error: {error}")


if __name__ == "__main__":
    main()
