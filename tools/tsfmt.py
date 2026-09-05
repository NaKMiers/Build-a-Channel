"""Shared helpers for turning timed text into the transcript timestamp formats.

Two shapes, and the difference matters:

  [MM:SS.SSS]  transcribes/transcript.md, written by the transcript tools. Forced
               alignment returns real onsets to the millisecond, so the transcript
               keeps them. `[00:03.480]`.
  [M:SS]       prompts/image-prompts.md, and the scene image file names derived from
               it by swapping the colon for a hyphen. Never widened, because the file
               names on disk are built from it.

`to_mss` is the single definition of how the second is derived from the first: plain
truncation, so a project re-cut from its cached word timings reproduces byte-identical
[M:SS] values and its existing image prompts still line up.
"""

import json
import re
from pathlib import Path

# 00:01:02,500  |  00:01:02.500  |  1:02.5
TIME_RE = re.compile(
    r"(?:(?P<h>\d+):)?(?P<m>\d{1,2}):(?P<s>\d{1,2})(?:[,.](?P<ms>\d{1,3}))?"
)
TAG_RE = re.compile(r"</?[^>]+>")  # <i>, <c.colorE5E5E5>
BRACE_RE = re.compile(r"\{[^}]*\}")  # {\an8}
SENTENCE_END = ('.', '!', '?', '…', '"', "'", '”', '’')
CLAUSE_END = (',', ';', ':', '—', '–')

# A single capital plus a period is an initial, not the end of a sentence:
# "E. J. Masicampo", "E. Adamson Hoebel", "Robin B. Lee". Without this, the
# splitter breaks after "E." and the healer then keeps it, because a capitalized
# one-word token ending in "." looks exactly like a short complete sentence
# ("Not less."). The result is a transcript line reading "E." which becomes a
# scene image with nothing to draw.
INITIAL_RE = re.compile(r"^[A-Z][.!?]?[\"'”’]?$")


def ends_sentence(token):
    """True if this token really closes a sentence, ignoring personal initials."""
    return token.endswith(SENTENCE_END) and not INITIAL_RE.match(token)


def parse_timecode(text):
    """Parse a single timecode into seconds. Returns None if it isn't one."""
    m = TIME_RE.fullmatch(text.strip())
    if not m:
        return None
    ms = m.group("ms") or "0"
    return (
        int(m.group("h") or 0) * 3600
        + int(m.group("m")) * 60
        + int(m.group("s"))
        + int(ms.ljust(3, "0")) / 1000
    )


def parse_offset(text):
    """Parse an --offset value, accepting either M:SS or plain seconds."""
    value = parse_timecode(text)
    if value is not None:
        return value
    try:
        return float(text)
    except ValueError:
        return None


def clean(text):
    text = TAG_RE.sub("", text)
    text = BRACE_RE.sub("", text)
    return " ".join(text.split())


def dedupe(cues):
    """Drop rolling-caption repeats (YouTube VTT repeats each line as it scrolls)."""
    out = []
    for start, end, text in cues:
        if out and out[-1][2] == text:
            prev_start, prev_end, prev_text = out[-1]
            out[-1] = (prev_start, max(prev_end, end), prev_text)
            continue
        # A cue whose text merely extends the previous one is the same rolling line.
        if out and text.startswith(out[-1][2] + " "):
            prev_start, _, _ = out[-1]
            out[-1] = (prev_start, end, text)
            continue
        out.append((start, end, text))
    return out


def split_by_pause(
    words, pause=0.30, split_sentences=True, max_chars=0, max_dur=0, min_words=3
):
    """Group word-level timings into lines the way a listener would hear them.

    Breaks wherever the speaker actually paused, and after every sentence, so a
    short sentence stays its own line instead of being glued to its neighbour.
    Anything still over max_chars or max_dur is then split at its widest internal
    pause, which keeps one line from holding more video than one image can carry.

    words: [(start, end, text)] with real per-word timings.
    """
    lines = []
    buf = []

    def flush():
        if buf:
            lines.append((buf[0][0], buf[-1][1], " ".join(w[2] for w in buf)))
            buf.clear()

    for i, word in enumerate(words):
        buf.append(word)
        if i + 1 >= len(words):
            break
        gap = words[i + 1][0] - word[1]
        if gap >= pause or (split_sentences and ends_sentence(word[2])):
            flush()
    flush()

    if max_chars > 0 or max_dur > 0:
        lines = [
            part
            for line in lines
            for part in _split_long(line, words, max_chars, max_dur)
        ]
    return _heal_fragments(lines, min_words)


def _heal_fragments(lines, min_words):
    """Fold stray fragments back into their neighbour.

    A dramatic pause mid-phrase ("Just watch ... it.") would otherwise leave a
    one-word line with nothing to draw. A short *complete* sentence ("The lull.")
    is left alone — that one earns its own frame.
    """
    if min_words <= 1:
        return lines

    pending = list(lines)
    out = []
    i = 0
    while i < len(pending):
        start, end, text = pending[i]
        runt = len(text.split()) < min_words
        complete = ends_sentence(text)
        continuation = not text[:1].isupper()

        # A line ending in an initial belongs to the name that follows it, however
        # long the line already is. The narrator's small pause in "E. Adamson" or
        # "E. J. Masicampo" would otherwise leave the initial stranded at the end of
        # the previous line, or alone on its own.
        tokens = text.split()
        if tokens and INITIAL_RE.match(tokens[-1]) and i + 1 < len(pending):
            _, next_end, next_text = pending[i + 1]
            pending[i + 1] = (start, next_end, f"{text} {next_text}")
            i += 1
            continue

        if runt and continuation and out:
            # Tail of the sentence above it — belongs to the line before.
            prev_start, _, prev_text = out[-1]
            out[-1] = (prev_start, end, f"{prev_text} {text}")
        elif runt and not complete and i + 1 < len(pending):
            # Head of the sentence below it — carry it forward instead.
            _, next_end, next_text = pending[i + 1]
            pending[i + 1] = (start, next_end, f"{text} {next_text}")
        elif runt and continuation and i + 1 < len(pending):
            _, next_end, next_text = pending[i + 1]
            pending[i + 1] = (start, next_end, f"{text} {next_text}")
        else:
            # Either long enough, or a short sentence that earns its own frame.
            out.append((start, end, text))
        i += 1

    return out


def _split_long(line, words, max_chars, max_dur):
    """Break an over-long line at its widest internal pause, then re-check."""
    start, end, text = line
    too_wide = max_chars > 0 and len(text) > max_chars
    too_slow = max_dur > 0 and (end - start) > max_dur
    if not (too_wide or too_slow):
        return [line]

    inside = [w for w in words if start <= w[0] and w[1] <= end]
    if len(inside) < 2:
        return [line]

    # Prefer a clause boundary, then the longest silence, and keep the cut near
    # the middle so splitting never leaves a two-word orphan line.
    middle = (len(inside) - 1) / 2

    def score(i):
        gap = inside[i + 1][0] - inside[i][1]
        clause = 0.5 if inside[i][2].endswith(CLAUSE_END) else 0
        off_centre = abs(i - middle) / max(middle, 1)
        return gap + clause - off_centre * 0.4

    cut = max(range(len(inside) - 1), key=score)
    left = inside[: cut + 1]
    right = inside[cut + 1 :]
    if not left or not right:
        return [line]

    halves = [
        (left[0][0], left[-1][1], " ".join(w[2] for w in left)),
        (right[0][0], right[-1][1], " ".join(w[2] for w in right)),
    ]
    return [
        part
        for half in halves
        for part in _split_long(half, words, max_chars, max_dur)
    ]


def merge(cues, min_dur, max_chars):
    """Combine short cues into longer lines, preferring sentence boundaries."""
    if min_dur <= 0 and max_chars <= 0:
        return cues

    out = []
    buf_start = buf_end = None
    buf_text = ""

    def flush():
        nonlocal buf_start, buf_end, buf_text
        if buf_text:
            out.append((buf_start, buf_end, buf_text))
        buf_start = buf_end = None
        buf_text = ""

    for start, end, text in cues:
        if buf_text:
            long_enough = (buf_end - buf_start) >= min_dur
            complete = ends_sentence(buf_text)
            too_long = max_chars > 0 and len(buf_text) + 1 + len(text) > max_chars
            # Running out of room mid-sentence: take the last clause boundary
            # instead of letting max_chars cut between two words.
            nearly_full = (
                max_chars > 0
                and len(buf_text) >= max_chars * 0.7
                and buf_text.endswith(CLAUSE_END)
            )
            if too_long or nearly_full or (long_enough and complete):
                flush()

        if not buf_text:
            buf_start, buf_end, buf_text = start, end, text
        else:
            buf_end = end
            buf_text = f"{buf_text} {text}"

    flush()
    return out


# A leading transcript stamp in either shape: [0:03], [00:03], [00:03.480].
STAMP_RE = re.compile(r"\[(\d+):(\d{2})(?:\.(\d{1,3}))?\]")


def mark(seconds):
    """MM:SS.SSS with no brackets: the shape a timestamp takes inside a JSON data file.

    words.json carries these instead of bare float seconds, so the cache can be read by
    eye against the transcript and the audio. Counting in whole milliseconds rather than
    formatting a float means a value a hair under the minute can never render as the
    impossible 00:60.000.
    """
    total = max(0, round(float(seconds) * 1000))
    minutes, rest = divmod(total, 60_000)
    return f"{minutes:02d}:{rest // 1000:02d}.{rest % 1000:03d}"


def seconds_of(value):
    """Read one timing out of a JSON data file, in either shape.

    Accepts the "MM:SS.SSS" string written today and the bare float seconds every
    words.json carried before it, so an old cache still merges without conversion.
    """
    if isinstance(value, bool):
        raise ValueError(f"not a timing: {value!r}")
    if isinstance(value, (int, float)):
        return float(value)
    parsed = parse_offset(str(value))
    if parsed is None:
        raise ValueError(f"not a timing: {value!r}")
    return parsed


def load_words(path):
    """Read a words.json cache into [(start, end, text)] with seconds as floats.

    The one place that knows both cache shapes, so a diagnostic snippet does not have to
    remember which one it is looking at. Validation beyond the timings is the caller's
    job; captions-srt.py keeps its own loader because it reports per-entry errors.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [(seconds_of(w["start"]), seconds_of(w["end"]), w["text"]) for w in data]


def stamp(seconds, pad=False, ms=False):
    """Format seconds as a transcript stamp.

    ms=True gives [MM:SS.SSS], the transcript format. Otherwise [M:SS], or [MM:SS]
    when pad is set. Hours roll into minutes either way.
    """
    if ms:
        return f"[{mark(seconds)}]"
    seconds = max(0, int(seconds))
    minutes, secs = divmod(seconds, 60)
    return f"[{minutes:02d}:{secs:02d}]" if pad else f"[{minutes}:{secs:02d}]"


def to_mss(text):
    """Truncate a [MM:SS.SSS] stamp to the [M:SS] form image prompts use.

    Milliseconds are dropped, not rounded, and the minute loses its pad: [00:03.480]
    becomes [0:03]. A stamp already in [M:SS] form comes back unchanged, so the same
    call works on a legacy whole-second transcript. Anything that is not a stamp is
    returned as-is.
    """
    m = STAMP_RE.fullmatch(text.strip())
    if not m:
        return text
    return f"[{int(m.group(1))}:{m.group(2)}]"


def render(cues, pad=False, ms=False):
    return "".join(f"{stamp(start, pad, ms)} {text}\n" for start, _, text in cues)
