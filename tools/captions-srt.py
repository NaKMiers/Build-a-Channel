#!/usr/bin/env python3
"""Build, assemble, and verify SRT caption files from a forced-aligned words.json.

Three stages, mirroring how the captions skill runs:

  build      words.json -> outputs/captions/en.srt + blocks.json
             Blocks are cut on real word timings, so every subtitle starts on the
             first word's true onset and ends on the last word's true offset.

  assemble   blocks.json + <code>.json -> outputs/captions/<code>.srt
             The translated text is poured into the English timing spine. Timings
             are identical across every language by construction, never by luck.

  check      outputs/captions/*.srt -> pass or fail
             Sequence, timing, emptiness, duplicate, script-leak, and em dash scan
             of every language file against en.srt.

Usage:

  python3 tools/captions-srt.py build \\
      --words   projects/12-slug/transcribes/words.json \\
      --transcript projects/12-slug/transcribes/transcript.md \\
      --out     projects/12-slug/outputs/captions

  python3 tools/captions-srt.py assemble \\
      --blocks  projects/12-slug/outputs/captions/blocks.json \\
      --translation /tmp/vi.json \\
      --out     projects/12-slug/outputs/captions

  python3 tools/captions-srt.py check \\
      --dir     projects/12-slug/outputs/captions

No third-party dependencies. Python 3.8+.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import tsfmt

# Block cutting. Every value is a knob, but these are the calibrated defaults for
# this channel's narration pace. See references/memory.md before changing one.
MAX_DUR = 7.0        # hard ceiling on a subtitle, tested look-ahead (never after the fact)
MIN_DUR = 2.5        # a silence gap may not close a block shorter than this
SENTENCE_MIN = 2.0   # a sentence end may close a block once it runs this long
GAP = 0.5            # real silence between words that counts as a phrase break
MAX_CHARS = 96       # 2 readable lines of 48, tested look-ahead like the duration cap

# Timing polish, in milliseconds.
LEAD_OUT = 300       # hold the subtitle past the last word so it does not read as clipped
TAIL_GAP = 80        # blank frame between consecutive subtitles
MIN_DISPLAY = 1000   # floor on how briefly a subtitle may flash

# Languages this skill ships. The code is the SRT file stem and is the BCP-47 tag
# YouTube expects when the file is uploaded as a caption track.
LANGUAGES = [
    ("ar", "Arabic"),
    ("bn", "Bangla"),
    ("zh-Hans", "Chinese Simplified"),
    ("zh-Hant", "Chinese Traditional"),
    ("en", "English"),
    ("fil", "Filipino"),
    ("fr", "French"),
    ("de", "German"),
    ("hi", "Hindi"),
    ("id", "Indonesian"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("ko", "Korean"),
    ("ml", "Malayalam"),
    ("mr", "Marathi"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("pa", "Punjabi"),
    ("ru", "Russian"),
    ("es", "Spanish"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("th", "Thai"),
    ("tr", "Turkish"),
    ("vi", "Vietnamese"),
]
NAMES = dict(LANGUAGES)

# Languages written in a non-Latin script. A run of Latin letters inside one of these
# is an untranslated source word that every structural check passes over in silence.
NON_LATIN = {
    "ar", "bn", "zh-Hans", "zh-Hant", "hi", "ja", "ko",
    "ml", "mr", "pa", "ru", "ta", "te", "th",
}

EM_DASH = "\u2014"  # escaped, so this file stays ASCII per house rules
LATIN_RUN = re.compile(r"[A-Za-z]{3,}")
WORD_CHARS = re.compile(r"[^0-9a-z]+")

SRT_BLOCK = re.compile(
    r"(?P<seq>\d+)\s*\n"
    r"(?P<start>\d{2}:\d{2}:\d{2},\d{3}) --> (?P<end>\d{2}:\d{2}:\d{2},\d{3})\s*\n"
    r"(?P<text>.*?)(?:\n\s*\n|\s*$)",
    re.DOTALL,
)


def die(message):
    print("error: %s" % message, file=sys.stderr)
    raise SystemExit(1)


def ms_to_srt(ms):
    ms = int(round(ms))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1_000)
    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)


def srt_to_ms(stamp):
    hms, milli = stamp.split(",")
    h, m, s = (int(x) for x in hms.split(":"))
    return ((h * 60 + m) * 60 + s) * 1000 + int(milli)


def normalize(text):
    """Reduce text to comparable letters and digits, for the transcript cross-check."""
    return WORD_CHARS.sub("", text.lower())


# ---------------------------------------------------------------- build


def load_words(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        die("%s not found. Run /transcript first, it writes words.json." % path)
    except json.JSONDecodeError as exc:
        die("%s is not valid JSON: %s" % (path, exc))

    if not isinstance(data, list) or not data:
        die("%s must be a non-empty list of word objects." % path)

    words = []
    for i, item in enumerate(data):
        if not isinstance(item, dict) or not {"start", "end", "text"} <= set(item):
            die("%s entry %d is missing start, end, or text." % (path, i))
        text = str(item["text"]).strip()
        if not text:
            continue
        # Both cache shapes: "MM:SS.SSS" as written today, bare seconds in older files.
        try:
            start = tsfmt.seconds_of(item["start"])
            end = tsfmt.seconds_of(item["end"])
        except ValueError as exc:
            die("%s entry %d has an unreadable timing: %s" % (path, i, exc))
        words.append({"start": start, "end": end, "text": text})
    if not words:
        die("%s has no words with text." % path)

    for i in range(1, len(words)):
        if words[i]["start"] < words[i - 1]["start"]:
            die("%s is not sorted by start time at entry %d. Re-run /transcript."
                % (path, i))
    return words


def check_against_transcript(words, transcript_path):
    """The words.json must be the same recording the transcript was cut from.

    A stale words.json from a previous take aligns without error and produces
    captions that drift against the video with nothing to show for it.
    """
    raw = Path(transcript_path).read_text(encoding="utf-8")
    # Either transcript shape: [MM:SS.SSS] as written today, or the legacy [M:SS]
    # still sitting in projects 1 through 13.
    cues = re.findall(r"^\[\d+:\d{2}(?:\.\d{1,3})?\]\s*(.+)$", raw, re.MULTILINE)
    if not cues:
        die("%s has no timestamped cue lines. Run /transcript first." % transcript_path)

    left = normalize(" ".join(w["text"] for w in words))
    right = normalize(" ".join(cues))
    if left == right:
        return len(cues)

    limit = min(len(left), len(right))
    at = next((i for i in range(limit) if left[i] != right[i]), limit)
    die(
        "words.json and %s describe different audio (they diverge %d characters in).\n"
        "  words.json: ...%s\n"
        "  transcript: ...%s\n"
        "Re-run /transcript so both come from the same take."
        % (transcript_path, at, left[at:at + 60], right[at:at + 60])
    )


def ends_clause(token):
    """True if this token closes a clause, the second-best place to cut."""
    return token.endswith(tsfmt.CLAUSE_END)


def best_split(words, start, end, floor_frac):
    """Pick the most translatable cut point in words[start:end+1].

    A cap firing at whatever word happened to fit produces fragments like "Your
    mind never scores your", which Japanese, Korean, and Hindi cannot translate
    at all because they reorder the clause. Falling back to the last sentence or
    clause boundary keeps every block a unit a translator can work with. The
    floor stops the fallback from shrinking a block to almost nothing.
    """
    floor = start + int((end - start) * floor_frac)
    for test in (tsfmt.ends_sentence, ends_clause):
        for j in range(end, floor - 1, -1):
            if test(words[j]["text"]):
                return j
    return end


def cut_blocks(words, max_dur, min_dur, sentence_min, gap, max_chars,
               floor_frac=0.4):
    """Group words into subtitle blocks on real timings.

    A block closes on the first of: the duration cap, the character cap, a real
    silence once the block has run long enough, or a sentence end once the block
    has run long enough. The two caps are tested against what the block *would
    become* if the next word joined, never against what it already is. Testing a
    ceiling after the fact is not a ceiling, and it is how a 7 second cap once
    shipped 9.9 second subtitles.

    The two natural closers land on a boundary by definition. When a cap forces
    the close instead, the block rewinds to its last sentence or clause boundary
    and the leftover words open the next block.
    """
    blocks = []
    total = len(words)
    start = 0

    while start < total:
        end = start
        forced = False
        length = len(words[start]["text"])

        while end + 1 < total:
            nxt = words[end + 1]
            onset = words[start]["start"]
            run = words[end]["end"] - onset

            if nxt["end"] - onset > max_dur or length + 1 + len(nxt["text"]) > max_chars:
                forced = True
                break
            if nxt["start"] - words[end]["end"] >= gap and run >= min_dur:
                break
            if tsfmt.ends_sentence(words[end]["text"]) and run >= sentence_min:
                break

            length += 1 + len(nxt["text"])
            end += 1

        if forced and end > start:
            end = best_split(words, start, end, floor_frac)

        blocks.append(words[start:end + 1])
        start = end + 1

    return blocks


def time_blocks(blocks):
    """Assign display windows. Guarantees no overlap and no zero-length block."""
    starts = [int(round(b[0]["start"] * 1000)) for b in blocks]
    ends = [int(round(b[-1]["end"] * 1000)) for b in blocks]

    timed = []
    for i, block in enumerate(blocks):
        start = starts[i]
        spoken_end = ends[i]
        if i + 1 < len(blocks):
            ceiling = starts[i + 1] - TAIL_GAP
        else:
            ceiling = spoken_end + LEAD_OUT

        end = min(spoken_end + LEAD_OUT, ceiling)
        end = max(end, min(start + MIN_DISPLAY, ceiling))
        if end <= start:
            end = start + 1

        timed.append({
            "i": i + 1,
            "start_ms": start,
            "end_ms": end,
            "start": ms_to_srt(start),
            "end": ms_to_srt(end),
            "text": " ".join(w["text"] for w in block),
            "words": len(block),
        })
    return timed


def render_srt(entries):
    out = []
    for e in entries:
        out.append("%d\n%s --> %s\n%s\n" % (e["i"], e["start"], e["end"], e["text"]))
    return "\n".join(out)


def cmd_build(args):
    words = load_words(args.words)
    cues = check_against_transcript(words, args.transcript)

    blocks = cut_blocks(
        words, args.max_dur, args.min_dur, args.sentence_min, args.gap, args.max_chars
    )
    entries = time_blocks(blocks)

    over = [e for e in entries
            if (e["end_ms"] - e["start_ms"]) > (args.max_dur * 1000 + LEAD_OUT + 1)]
    if over:
        die("%d blocks exceed the %.1fs cap. This is a bug in cut_blocks, not input."
            % (len(over), args.max_dur))

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    srt_path = out_dir / "en.srt"
    srt_path.write_text(render_srt(entries), encoding="utf-8")

    blocks_path = out_dir / "blocks.json"
    blocks_path.write_text(
        json.dumps(
            {
                "words": str(args.words),
                "transcript": str(args.transcript),
                "count": len(entries),
                "settings": {
                    "max_dur": args.max_dur, "min_dur": args.min_dur,
                    "sentence_min": args.sentence_min, "gap": args.gap,
                    "max_chars": args.max_chars,
                },
                "blocks": entries,
            },
            ensure_ascii=False,
            indent=1,
        ) + "\n",
        encoding="utf-8",
    )

    durations = [(e["end_ms"] - e["start_ms"]) / 1000 for e in entries]
    chars = [len(e["text"]) for e in entries]
    unfinished = sum(1 for e in entries if not tsfmt.ends_sentence(e["text"].split()[-1]))
    total = entries[-1]["end_ms"] / 1000

    print("words        %d, from %s" % (len(words), args.words))
    print("transcript   %d cues, text matches words.json" % cues)
    print("blocks       %d" % len(entries))
    print("duration     mean %.1fs, min %.1fs, max %.1fs, total %d:%02d"
          % (sum(durations) / len(durations), min(durations), max(durations),
             int(total // 60), int(total % 60)))
    print("characters   mean %d, max %d" % (sum(chars) / len(chars), max(chars)))
    print("mid-sentence %d blocks (%.0f%%), split by the caps"
          % (unfinished, 100 * unfinished / len(entries)))
    print("wrote        %s" % srt_path)
    print("wrote        %s" % blocks_path)


# ---------------------------------------------------------------- assemble


def cmd_assemble(args):
    spine = json.loads(Path(args.blocks).read_text(encoding="utf-8"))
    entries = spine["blocks"]

    payload = json.loads(Path(args.translation).read_text(encoding="utf-8"))
    code = args.code or payload.get("code")
    if not code:
        die("%s has no \"code\" key and --code was not given." % args.translation)
    if code not in NAMES:
        die("%s is not a supported language code. Supported: %s"
            % (code, ", ".join(c for c, _ in LANGUAGES)))

    texts = payload.get("translations")
    if not isinstance(texts, list):
        die("%s has no \"translations\" array." % args.translation)
    if len(texts) != len(entries):
        die("%s has %d translations for %d blocks. Re-translate; do not pad or trim."
            % (args.translation, len(texts), len(entries)))

    cleaned = []
    for i, text in enumerate(texts):
        text = " ".join(str(text).split())
        if not text:
            die("%s translation %d is empty." % (args.translation, i + 1))
        if EM_DASH in text:
            die("%s translation %d contains an em dash, banned by house rules."
                % (args.translation, i + 1))
        cleaned.append(text)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / ("%s.srt" % code)
    path.write_text(
        render_srt([dict(e, text=t) for e, t in zip(entries, cleaned)]),
        encoding="utf-8",
    )
    print("wrote %s (%s, %d blocks)" % (path, NAMES[code], len(cleaned)))


# ---------------------------------------------------------------- check


def proper_nouns(blocks):
    """Latin words a non-Latin file is allowed to keep, derived from en.srt.

    Researcher names, study titles, and place names stay in Latin script inside a
    Japanese or Hindi subtitle, and that is correct. Everything else Latin in
    those files is an untranslated leak. The two are told apart by capitalisation
    in the English source: a capital that is not opening a sentence is a name.
    """
    allowed = set()
    opener = True  # runs across blocks: a block often continues the previous sentence
    for _, _, _, text in blocks:
        for token in text.split():
            word = token.strip(".,:;!?\"'()[]")
            if word and word[0].isupper() and not opener:
                allowed.add(word.lower())
                allowed.update(p.lower() for p in word.split("-") if p)
            opener = bool(word) and tsfmt.ends_sentence(token)
    return allowed


def parse_srt(path):
    raw = Path(path).read_text(encoding="utf-8")
    blocks = []
    for m in SRT_BLOCK.finditer(raw):
        blocks.append((
            int(m.group("seq")),
            srt_to_ms(m.group("start")),
            srt_to_ms(m.group("end")),
            m.group("text").strip(),
        ))
    return blocks


def cmd_check(args):
    directory = Path(args.dir)
    ref_path = directory / "en.srt"
    if not ref_path.exists():
        die("%s not found. Run the build stage first." % ref_path)

    ref = parse_srt(ref_path)
    allowed = proper_nouns(ref)
    allowed.update(w.strip().lower() for w in (args.allow or "").split(",") if w.strip())
    files = sorted(p for p in directory.glob("*.srt"))
    problems, lines = [], []

    for path in files:
        code = path.stem
        blocks = parse_srt(path)
        found = []

        if len(blocks) != len(ref):
            found.append("%d blocks, en.srt has %d" % (len(blocks), len(ref)))
        else:
            drift = sum(
                1 for a, b in zip(blocks, ref)
                if a[0] != b[0] or a[1] != b[1] or a[2] != b[2]
            )
            if drift:
                found.append("%d blocks disagree with en.srt on sequence or timing" % drift)

        for seq, start, end, text in blocks:
            if not text:
                found.append("block %d is empty" % seq)
                break
        for i in range(1, len(blocks)):
            if blocks[i][3] == blocks[i - 1][3]:
                found.append("block %d repeats block %d verbatim" % (blocks[i][0], blocks[i - 1][0]))
                break
        for seq, start, end, _ in blocks:
            if end <= start:
                found.append("block %d has a zero or negative duration" % seq)
                break
        for i in range(1, len(blocks)):
            if blocks[i][1] < blocks[i - 1][2]:
                found.append("block %d overlaps block %d" % (blocks[i][0], blocks[i - 1][0]))
                break

        if any(EM_DASH in b[3] for b in blocks):
            found.append("contains an em dash, banned by house rules")

        if code in NON_LATIN:
            leaks = []
            for seq, _, _, text in blocks:
                stray = [w for w in LATIN_RUN.findall(text) if w.lower() not in allowed]
                if stray:
                    leaks.append((seq, stray[0]))
            if leaks:
                found.append(
                    "%d blocks leak untranslated Latin text (block %d: %s)"
                    % (len(leaks), leaks[0][0], leaks[0][1])
                )

        status = "FAIL" if found else "ok"
        lines.append("%-9s %-4s %4d blocks  %s"
                     % (code, status, len(blocks), NAMES.get(code, "?")))
        for f in found:
            lines.append("            %s" % f)
            problems.append("%s: %s" % (code, f))

    missing = [c for c, _ in LANGUAGES if not (directory / ("%s.srt" % c)).exists()]

    print("\n".join(lines))
    if missing:
        print("\nnot written: %s" % ", ".join(missing))
    if problems:
        print("\n%d problem(s). Fix and re-check before reporting done." % len(problems))
        raise SystemExit(1)
    print("\n%d file(s) clean, all in sync with en.srt." % len(files))


# ---------------------------------------------------------------- cli


def main():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("build", help="words.json -> en.srt + blocks.json")
    a.add_argument("--words", required=True, help="transcribes/words.json")
    a.add_argument("--transcript", required=True, help="transcribes/transcript.md")
    a.add_argument("--out", required=True, help="outputs/captions")
    a.add_argument("--max-dur", type=float, default=MAX_DUR)
    a.add_argument("--min-dur", type=float, default=MIN_DUR)
    a.add_argument("--sentence-min", type=float, default=SENTENCE_MIN)
    a.add_argument("--gap", type=float, default=GAP)
    a.add_argument("--max-chars", type=int, default=MAX_CHARS)
    a.set_defaults(func=cmd_build)

    a = sub.add_parser("assemble", help="blocks.json + <code>.json -> <code>.srt")
    a.add_argument("--blocks", required=True, help="outputs/captions/blocks.json")
    a.add_argument("--translation", required=True, help="JSON with code + translations")
    a.add_argument("--out", required=True, help="outputs/captions")
    a.add_argument("--code", help="override the code in the translation file")
    a.set_defaults(func=cmd_assemble)

    a = sub.add_parser("check", help="verify every *.srt against en.srt")
    a.add_argument("--dir", required=True, help="outputs/captions")
    a.add_argument("--allow", help="extra Latin words a non-Latin file may keep, "
                                   "comma separated. Names capitalised mid-sentence "
                                   "in en.srt are allowed automatically.")
    a.set_defaults(func=cmd_check)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
