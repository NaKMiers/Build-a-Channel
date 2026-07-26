#!/usr/bin/env python3
"""Turn narration audio into a [M:SS] transcript, ready to paste into Stage 4.

Two engines:

  align  (default, needs ELEVENLABS_API_KEY)
         Forced alignment: you supply the audio AND the exact script it was read
         from, and the API returns the timing of every word. The words come from
         your script, so the text is never wrong. Billed at the speech-to-text
         rate (~$0.08 for a 12-minute video).

  groq   (needs GROQ_API_KEY)
         Plain transcription with whisper-large-v3-turbo (~$0.04 per hour of
         audio, so under a cent per video). No script needed, but the text is
         whatever the model heard, so wording and punctuation can drift.

Lines are cut where the narrator actually paused and after every sentence, so a
short sentence stays its own line and nothing is glued to its neighbour. Anything
still holding more than --max-dur seconds of video is split at its widest internal
pause. On a 12-minute script this lands around 230 lines of ~3s each.

Multiple audio files are treated as consecutive parts of one recording, so
part 2 continues where part 1 ended. With --engine align, pass one --script per
audio file, in the same order.

Examples:
    audio-to-timestamps.py voice.mp3 --script script_why_you_fear_the_dark.txt -o t.txt
    audio-to-timestamps.py part-1.mp3 part-2.mp3 --script s1.txt --script s2.txt
    audio-to-timestamps.py part-1.mp3 part-2.mp3 part-3.mp3 --engine groq -o t.txt
"""

import argparse
import json
import mimetypes
import os
import statistics
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

import tsfmt

ALIGN_URL = "https://api.elevenlabs.io/v1/forced-alignment"
GROQ_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_MODEL = "whisper-large-v3-turbo"
GROQ_SIZE_LIMIT = 25 * 1024 * 1024  # free-tier upload cap


def load_dotenv():
    """Read KEY=value pairs from the nearest .env, without overriding the shell."""
    for folder in (Path.cwd(), *Path(__file__).resolve().parents):
        path = folder / ".env"
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip().removeprefix("export ").strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("\"'")
            if key and value:
                os.environ.setdefault(key, value)
        return path
    return None


def api_key(*names):
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    sys.exit(
        f"error: no API key found. Set {names[0]} in your shell or in a .env file "
        f"next to this repo.\n       Accepted names: {', '.join(names)}"
    )


def encode_multipart(fields, files):
    """Build a multipart/form-data body. fields: {name: str}. files: [(name, Path)]."""
    boundary = uuid.uuid4().hex
    sep = f"--{boundary}".encode()
    body = bytearray()

    for name, value in fields.items():
        body += sep + b"\r\n"
        body += f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode()
        body += str(value).encode() + b"\r\n"

    for name, path in files:
        ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        body += sep + b"\r\n"
        body += (
            f'Content-Disposition: form-data; name="{name}"; '
            f'filename="{path.name}"\r\n'
        ).encode()
        body += f"Content-Type: {ctype}\r\n\r\n".encode()
        body += path.read_bytes() + b"\r\n"

    body += f"--{boundary}--\r\n".encode()
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def post(url, headers, body, content_type, timeout):
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", content_type)
    for key, value in headers.items():
        req.add_header(key, value)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace").strip()
        sys.exit(f"error: {url} returned {e.code}\n{detail}")
    except urllib.error.URLError as e:
        sys.exit(f"error: could not reach {url}: {e.reason}")


def align(audio, script, timeout):
    """Forced-align one audio file against its script. Returns word cues."""
    text = " ".join(script.read_text(encoding="utf-8").split())
    if not text:
        sys.exit(f"error: {script} is empty")

    body, ctype = encode_multipart({"text": text}, [("file", audio)])
    data = post(
        ALIGN_URL,
        {
            "xi-api-key": api_key(
                "ELEVENLABS_API_KEY",
                "ELEVENLAB_API_KEY",  # common typo, accepted so it just works
                "ELEVEN_API_KEY",
                "XI_API_KEY",
            )
        },
        body,
        ctype,
        timeout,
    )

    words = data.get("words") or []
    if not words:
        sys.exit(f"error: alignment returned no words for {audio}")

    cues = []
    for w in words:
        token = tsfmt.clean(w.get("text", ""))
        if token:
            cues.append((float(w["start"]), float(w["end"]), token))
    return cues


def transcribe(audio, timeout):
    """Transcribe one audio file with Groq. Returns word or segment cues."""
    if audio.stat().st_size > GROQ_SIZE_LIMIT:
        print(
            f"warning: {audio.name} is over Groq's 25MB free-tier upload limit; "
            "split it or use --engine align",
            file=sys.stderr,
        )

    body, ctype = encode_multipart(
        {
            "model": GROQ_MODEL,
            "response_format": "verbose_json",
            "timestamp_granularities[]": "word",
        },
        [("file", audio)],
    )
    data = post(
        GROQ_URL,
        {"Authorization": f"Bearer {api_key('GROQ_API_KEY')}"},
        body,
        ctype,
        timeout,
    )

    def to_cues(units, key):
        out = []
        for u in units:
            token = tsfmt.clean(u.get(key, ""))
            if token:
                out.append((float(u["start"]), float(u["end"]), token))
        return out

    words = to_cues(data.get("words") or [], "word")
    segments = to_cues(data.get("segments") or [], "text")

    # Whisper's word timestamps sometimes come back stripped of punctuation, which
    # would defeat sentence splitting. Fall back to segments when that happens.
    if words and any(w[2].endswith(tsfmt.SENTENCE_END) for w in words):
        return words
    if segments:
        return segments
    if words:
        return words
    sys.exit(f"error: transcription returned nothing for {audio}")


def main():
    p = argparse.ArgumentParser(
        description="Turn narration audio into [M:SS] transcript lines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples:")[1],
    )
    p.add_argument(
        "audio",
        nargs="*",
        type=Path,
        help="audio files, in order (omit only with --from-json)",
    )
    p.add_argument(
        "--script",
        action="append",
        default=[],
        type=Path,
        metavar="TXT",
        help="the exact script the audio was read from; repeat once per audio file",
    )
    p.add_argument(
        "--engine",
        choices=("align", "groq"),
        help="default: align when --script is given, groq otherwise",
    )
    p.add_argument("-o", "--output", type=Path, help="write here instead of stdout")
    p.add_argument(
        "--pause",
        type=float,
        default=0.30,
        metavar="SEC",
        help="start a new line wherever the narrator paused this long "
        "(default: 0.30; lower = more, shorter lines)",
    )
    p.add_argument(
        "--no-split-sentences",
        action="store_true",
        help="allow one line to run across a sentence boundary",
    )
    p.add_argument(
        "--max-dur",
        type=float,
        default=4.5,
        metavar="SEC",
        help="split any line holding more than this much video, at its widest "
        "internal pause (default: 4.5; 0 = never split)",
    )
    p.add_argument(
        "--min-words",
        type=int,
        default=3,
        metavar="N",
        help="fold fragments shorter than this into a neighbour, so a dramatic "
        "pause never leaves a one-word line (default: 3)",
    )
    p.add_argument(
        "--max-chars",
        type=int,
        default=0,
        metavar="N",
        help="also split lines longer than this many characters (default: 0 = off)",
    )
    p.add_argument(
        "--min-dur",
        type=float,
        default=0,
        metavar="SEC",
        help="AFTER splitting, glue lines back together until each spans this "
        "long. Use only to cut the number of images you pay for (default: 0 = off)",
    )
    p.add_argument(
        "--pad",
        action="store_true",
        help="zero-pad minutes: [00:05] instead of [0:05]",
    )
    p.add_argument(
        "--timeout",
        type=int,
        default=900,
        metavar="SEC",
        help="per-request timeout (default: 900)",
    )
    p.add_argument(
        "--save-json",
        type=Path,
        metavar="PATH",
        help="also write the raw word timings here",
    )
    p.add_argument(
        "--from-json",
        type=Path,
        metavar="PATH",
        help="re-chunk word timings saved earlier by --save-json, with no API call "
        "and no cost. Use this to retune the line splitting.",
    )
    args = p.parse_args()

    if not args.audio and not args.from_json:
        p.error("give at least one audio file, or --from-json to re-chunk saved timings")

    if args.from_json:
        cues = [
            (float(w["start"]), float(w["end"]), w["text"])
            for w in json.loads(args.from_json.read_text(encoding="utf-8"))
        ]
        return emit(args, cues)

    env_file = load_dotenv()
    if env_file:
        print(f"loaded {env_file}", file=sys.stderr)

    engine = args.engine or ("align" if args.script else "groq")

    for path in [*args.audio, *args.script]:
        if not path.is_file():
            sys.exit(f"error: no such file: {path}")

    if engine == "align":
        if len(args.script) != len(args.audio):
            sys.exit(
                f"error: --engine align needs one --script per audio file "
                f"(got {len(args.audio)} audio, {len(args.script)} script). "
                "Align the whole narration in one call, or split the script to match "
                "the audio parts."
            )
    elif args.script:
        print(
            "warning: --script is ignored with --engine groq (transcription "
            "produces its own text)",
            file=sys.stderr,
        )

    cues = []
    running_end = 0.0
    for i, audio in enumerate(args.audio):
        label = f"[{i + 1}/{len(args.audio)}] {audio.name}"
        print(f"{label}: {engine}...", file=sys.stderr)

        part = align(audio, args.script[i], args.timeout) if engine == "align" \
            else transcribe(audio, args.timeout)

        cues.extend((s + running_end, e + running_end, t) for s, e, t in part)
        running_end = cues[-1][1]

    if args.save_json:
        args.save_json.write_text(
            json.dumps(
                [{"start": s, "end": e, "text": t} for s, e, t in cues],
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    return emit(args, cues)


def emit(args, cues):
    """Chunk word timings into lines and write them out."""
    if not cues:
        sys.exit("error: no word timings to work with")

    lines = tsfmt.split_by_pause(
        cues,
        pause=args.pause,
        split_sentences=not args.no_split_sentences,
        max_chars=args.max_chars,
        max_dur=args.max_dur,
        min_words=args.min_words,
    )
    if args.min_dur > 0:
        lines = tsfmt.merge(lines, args.min_dur, args.max_chars)

    body = tsfmt.render(lines, args.pad)

    total = cues[-1][1]
    durations = [e - s for s, e, _ in lines]
    summary = (
        f"{len(lines)} lines from {len(cues)} words, "
        f"{int(total // 60)}m{int(total % 60):02d}s, "
        f"median {statistics.median(durations):.1f}s/line, "
        f"median {statistics.median(len(t) for _, _, t in lines):.0f} chars/line"
    )

    if args.output:
        args.output.write_text(body, encoding="utf-8")
        print(f"{summary} -> {args.output}", file=sys.stderr)
    else:
        print(summary, file=sys.stderr)
        sys.stdout.write(body)


if __name__ == "__main__":
    main()
