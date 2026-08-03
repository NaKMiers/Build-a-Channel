#!/usr/bin/env python3
"""Safely inspect, rename, move, and verify TossExplains scene images."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

STAMP = re.compile(r"^\[(\d+):(\d{2})\]", re.MULTILINE)
NUMBERED = re.compile(r"^(\d+)_2k\.jpe?g$")
TIMESTAMPED = re.compile(r"^\[\d+-\d{2}\]\.jpg$")


def image_name(stamp: str) -> str:
    """Return the Windows-safe filename for a transcript or prompt timestamp."""
    return f"[{stamp.replace(':', '-')}].jpg"


def fail(message: str, code: int = 2) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(code)


def seconds(value: str) -> int:
    try:
        minute, second = map(int, value.split(":"))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid timestamp: {value}") from exc
    if minute < 0 or not 0 <= second < 60:
        raise argparse.ArgumentTypeError(f"Invalid timestamp: {value}")
    return minute * 60 + second


def prompt_stamps(project: Path) -> list[str]:
    prompt = project / "prompts" / "image-prompts.md"
    if not prompt.is_file():
        fail(f"Missing prompt file: {prompt}")
    return [f"{match.group(1)}:{match.group(2)}" for match in STAMP.finditer(prompt.read_text(encoding="utf-8"))]


def range_folder(project: Path, start: str, end: str) -> Path:
    """Resolve a range folder by name, tolerating Windows-safe colon replacements."""
    scenes = project / "scenes"
    if not scenes.is_dir():
        fail(f"Missing scenes directory: {scenes}")
    names = list(dict.fromkeys(
        f"{start.replace(':', sep)} - {end.replace(':', sep)}" for sep in (":", ".", "-")
    ))
    for name in names:
        folder = scenes / name
        if folder.is_dir():
            return folder
    present = sorted(item.name for item in scenes.iterdir() if item.is_dir())
    fail(f"Missing scene range folder. Tried {names}. Present: {present or 'none'}")


def range_data(project: Path, start: str, end: str):
    folder = range_folder(project, start, end)
    lower, upper = seconds(start), seconds(end)
    expected = [stamp for stamp in prompt_stamps(project) if lower <= seconds(stamp) <= upper]
    entries = list(folder.iterdir())
    numbered = sorted((item for item in entries if item.is_file() and NUMBERED.fullmatch(item.name)), key=lambda item: int(NUMBERED.fullmatch(item.name).group(1)))
    timestamped = sorted(item.name for item in entries if item.is_file() and TIMESTAMPED.fullmatch(item.name))
    unexpected = sorted(item.name for item in entries if item not in numbered and item.name not in timestamped)
    return folder, expected, numbered, timestamped, unexpected


def inspect(project: Path, start: str, end: str) -> bool:
    folder, expected, numbered, timestamped, unexpected = range_data(project, start, end)
    indices = [int(NUMBERED.fullmatch(item.name).group(1)) for item in numbered]
    root = project / "scenes"
    collisions = [stamp for stamp in expected if (root / image_name(stamp)).exists()]
    passed = len(expected) == len(numbered) and indices == list(range(1, len(expected) + 1)) and not timestamped and not unexpected and not collisions
    print(f"Range: {folder.name}")
    print(f"Prompt timestamps: {len(expected)}")
    print(f"Numbered images: {len(numbered)}")
    print(f"Existing timestamp images: {len(timestamped)}")
    print(f"Unexpected entries: {len(unexpected)}")
    print(f"Destination collisions: {len(collisions)}")
    if expected:
        print(f"Expected span: {image_name(expected[0])} through {image_name(expected[-1])}")
    print("PASS" if passed else "FAIL")
    return passed


def rename(project: Path, start: str, end: str) -> None:
    if not inspect(project, start, end):
        fail("Range was not renamed. Resolve every mismatch first.")
    folder, expected, numbered, _, _ = range_data(project, start, end)
    for source, stamp in zip(numbered, expected, strict=True):
        source.rename(folder / image_name(stamp))
    print(f"Renamed {len(expected)} images in {folder.name}.")


def move(project: Path) -> None:
    scenes = project / "scenes"
    folders = sorted(item for item in scenes.iterdir() if item.is_dir())
    if not folders:
        fail("No scene range folders found.")
    sources, unexpected = [], []
    for folder in folders:
        for item in folder.iterdir():
            if item.is_file() and TIMESTAMPED.fullmatch(item.name):
                sources.append(item)
            else:
                unexpected.append(item.relative_to(scenes))
    names = [item.name for item in sources]
    duplicates = {name for name in names if names.count(name) > 1}
    root_names = {item.name for item in scenes.iterdir() if item.is_file()}
    collisions = set(names) & root_names
    if unexpected or duplicates or collisions:
        print(f"Unexpected range entries: {len(unexpected)}")
        print(f"Duplicate image names: {len(duplicates)}")
        print(f"Root collisions: {len(collisions)}")
        fail("No images moved. Resolve every conflict first.")
    for source in sources:
        source.rename(scenes / source.name)
    for folder in folders:
        folder.rmdir()
    print(f"Moved {len(sources)} images and removed {len(folders)} folders.")


def migrate_windows(project: Path) -> None:
    """Replace colons in scene image names after checking every destination."""
    scenes = project / "scenes"
    if not scenes.is_dir():
        fail(f"Missing scenes directory: {scenes}")
    sources = sorted(item for item in scenes.rglob("*") if item.is_file() and ":" in item.name)
    destinations = [source.with_name(source.name.replace(":", "-")) for source in sources]
    duplicate_destinations = {path for path in destinations if destinations.count(path) > 1}
    collisions = [path for path in destinations if path.exists() and path not in sources]
    if duplicate_destinations or collisions:
        print(f"Invalid image names: {len(sources)}")
        print(f"Duplicate destinations: {len(duplicate_destinations)}")
        print(f"Destination collisions: {len(collisions)}")
        fail("No images renamed. Resolve every destination conflict first.")
    for source, destination in zip(sources, destinations, strict=True):
        source.rename(destination)
    print(f"Renamed {len(sources)} image files for Windows compatibility.")


def verify(project: Path) -> None:
    scenes = project / "scenes"
    expected = [image_name(stamp) for stamp in prompt_stamps(project)]
    actual = sorted(item.name for item in scenes.iterdir() if item.is_file() and TIMESTAMPED.fullmatch(item.name))
    unexpected = sorted(item.name for item in scenes.iterdir() if item.is_file() and item.name != ".gitkeep" and not TIMESTAMPED.fullmatch(item.name))
    duplicate_prompts = {name for name in expected if expected.count(name) > 1}
    missing, extra = set(expected) - set(actual), set(actual) - set(expected)
    passed = not duplicate_prompts and not missing and not extra and not unexpected and len(expected) == len(actual)
    print(f"Prompt timestamps: {len(expected)}")
    print(f"Scene images: {len(actual)}")
    print(f"Duplicate prompt timestamps: {len(duplicate_prompts)}")
    print(f"Missing images: {len(missing)}")
    print(f"Extra timestamp images: {len(extra)}")
    print(f"Unexpected scene files: {len(unexpected)}")
    print("PASS" if passed else "FAIL")
    if not passed:
        raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check-range", "rename-range", "move", "migrate-windows", "verify"))
    parser.add_argument("project", type=Path)
    parser.add_argument("start", nargs="?")
    parser.add_argument("end", nargs="?")
    args = parser.parse_args()
    if args.command in {"check-range", "rename-range"}:
        if not args.start or not args.end:
            parser.error(f"{args.command} requires START and END")
        if seconds(args.start) > seconds(args.end):
            parser.error("START must be at or before END")
        if args.command == "check-range":
            raise SystemExit(0 if inspect(args.project, args.start, args.end) else 2)
        rename(args.project, args.start, args.end)
    elif args.command == "move":
        move(args.project)
    elif args.command == "migrate-windows":
        migrate_windows(args.project)
    else:
        verify(args.project)


if __name__ == "__main__":
    main()
