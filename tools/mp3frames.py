"""MPEG audio frame parsing: tag stripping and true duration, with no dependencies.

Shared by `combine-audio.py`, which concatenates narration parts, and
`audio-to-timestamps.py`, which needs each part's real length to place the later
parts on the combined timeline.

Duration comes from summing actual frame headers rather than dividing file size by a
nominal bitrate, so VBR recordings and parts encoded at different bitrates are both
measured correctly. ffmpeg is not required and neither is any pip package.
"""

import sys

# MPEG 1/2/2.5 frame tables, indexed by the bits in the 4-byte frame header.
BITRATES = {
    # (table_version, layer): bitrate in kbps per bitrate_index
    (1, 1): [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448],
    (1, 2): [0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384],
    (1, 3): [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320],
    (2, 1): [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256],
    (2, 2): [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],
    (2, 3): [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],
}
SAMPLE_RATES = {1: [44100, 48000, 32000], 2: [22050, 24000, 16000],
                25: [11025, 12000, 8000]}
SAMPLES_PER_FRAME = {(1, 1): 384, (1, 2): 1152, (1, 3): 1152,
                     (2, 1): 384, (2, 2): 1152, (2, 3): 576}


def strip_tags(data):
    """Return (leading_id3v2_tag, audio_bytes), with ID3v1 and APE trailers removed."""
    start = 0
    if data[:3] == b"ID3" and len(data) > 10:
        size = 0
        for byte in data[6:10]:  # syncsafe integer, 7 bits per byte
            size = (size << 7) | (byte & 0x7F)
        start = 10 + size
        if data[5] & 0x10:  # footer present
            start += 10

    end = len(data)
    if data[end - 128:end - 125] == b"TAG":
        end -= 128
    if data[end - 32:end - 24] == b"APETAGEX":
        end -= int.from_bytes(data[end - 20:end - 16], "little")

    return data[:start], data[start:end]


def parse_frame(data, pos):
    """Decode the frame header at pos. Returns (frame_len, samples, rate) or None."""
    if pos + 4 > len(data):
        return None
    h = data[pos:pos + 4]
    if h[0] != 0xFF or (h[1] & 0xE0) != 0xE0:
        return None

    version = {0: 25, 2: 2, 3: 1}.get((h[1] >> 3) & 0x03)
    layer = 4 - ((h[1] >> 1) & 0x03)
    bitrate_index = (h[2] >> 4) & 0x0F
    rate_index = (h[2] >> 2) & 0x03
    padding = (h[2] >> 1) & 0x01

    if version is None or layer == 4 or bitrate_index in (0, 15) or rate_index == 3:
        return None

    table_version = 1 if version == 1 else 2
    bitrate = BITRATES[(table_version, layer)][bitrate_index] * 1000
    rate = SAMPLE_RATES[version][rate_index]
    samples = SAMPLES_PER_FRAME[(table_version, layer)]

    if layer == 1:
        length = (12 * bitrate // rate + padding) * 4
    else:
        length = samples // 8 * bitrate // rate + padding

    return (length, samples, rate) if length > 4 else None


def scan(audio, name="audio"):
    """Walk every frame of stripped audio bytes.

    Returns (offsets, samples, rate, bitrates): the byte offset of each frame, the
    total sample count, the sample rate, and a {kbps: frame_count} histogram. The
    histogram is how a mixed-bitrate concatenation is detected, and the offsets are
    what a Xing seek table is built from.
    """
    offsets, samples, rate, resyncs, bitrates = [], 0, None, 0, {}
    pos = 0
    while pos < len(audio):
        frame = parse_frame(audio, pos)
        if frame is None:
            pos += 1
            resyncs += 1
            continue
        length, frame_samples, frame_rate = frame
        rate = rate or frame_rate
        offsets.append(pos)
        samples += frame_samples
        kbps = round(length * 8 * frame_rate / frame_samples / 1000)
        bitrates[kbps] = bitrates.get(kbps, 0) + 1
        pos += length

    if not offsets:
        sys.exit(f"error: no MPEG audio frames found in {name}")
    if resyncs > 4096:
        print(f"warning: {name} needed {resyncs} resync bytes, it may be damaged",
              file=sys.stderr)
    return offsets, samples, rate, bitrates


def measure(audio, name="audio"):
    """Walk every frame of stripped audio bytes. Returns (seconds, frames, rate)."""
    offsets, samples, rate, _ = scan(audio, name)
    return samples / rate, len(offsets), rate


def side_info_size(header):
    """Bytes of side info after a frame header, which is where a Xing tag starts."""
    version = {0: 25, 2: 2, 3: 1}.get((header[1] >> 3) & 0x03)
    mono = ((header[3] >> 6) & 0x03) == 3
    if version == 1:
        return 17 if mono else 32
    return 9 if mono else 17


def build_toc(offsets, total_bytes):
    """Xing's 100-entry seek table: percent of duration to 1/256ths of the stream."""
    toc = bytearray(100)
    count = len(offsets)
    for i in range(100):
        frame = min(count - 1, i * count // 100)
        toc[i] = min(255, offsets[frame] * 256 // total_bytes)
    return bytes(toc)


def write_vbr_header(audio, name="audio"):
    """Give a stream an accurate Xing header, so players report the real duration.

    Concatenating parts encoded at different bitrates produces a variable-bitrate
    stream. Without a Xing header a player reads the *first* frame's bitrate and
    extrapolates it across the whole file, so a 256 kbps part followed by 128 kbps
    parts reports roughly two thirds of the true length, and every seek lands in the
    wrong place. Worse, if the first part carried a LAME `Info` header of its own,
    that header survives the concatenation and now describes only the first part.

    This rewrites that header in place when one exists, or synthesises a header frame
    and prepends it when none does. Declares the true frame count, the true byte
    count, and a seek table built from real frame offsets. Returns new audio bytes.
    """
    offsets, _, _, _ = scan(audio, name)

    first = audio[offsets[0]:offsets[0] + 4]
    frame_length = parse_frame(audio, offsets[0])[0]
    tag_at = offsets[0] + 4 + side_info_size(first)
    existing = audio[tag_at:tag_at + 4] in (b"Xing", b"Info")

    if existing:
        # The first frame is already a dedicated header frame, so it holds no audio
        # and is not counted among the frames the tag describes.
        audio_frames = offsets[1:]
        header_frame = bytearray(audio[offsets[0]:offsets[0] + frame_length])
        body = audio[offsets[0] + frame_length:]
        tag_offset = 4 + side_info_size(first)
    else:
        # Clone the first frame's format into a fresh silent frame to carry the tag.
        audio_frames = offsets
        header_frame = bytearray(first + b"\x00" * (frame_length - 4))
        body = audio[offsets[0]:]
        tag_offset = 4 + side_info_size(first)

    total_bytes = len(header_frame) + len(body)
    shift = len(header_frame) if not existing else 0
    toc = build_toc([o + shift - offsets[0] for o in audio_frames], total_bytes)

    payload = (
        b"Xing"                                     # Xing, not Info: this is VBR now
        + (0x0007).to_bytes(4, "big")               # FRAMES | BYTES | TOC
        + len(audio_frames).to_bytes(4, "big")
        + total_bytes.to_bytes(4, "big")
        + toc
    )
    if tag_offset + len(payload) > len(header_frame):
        print(f"warning: {name}'s first frame is too small for a seek table, "
              "leaving the duration header alone", file=sys.stderr)
        return audio
    header_frame[tag_offset:tag_offset + len(payload)] = payload

    return bytes(header_frame) + body


def reported_duration(audio):
    """The duration a player will show, which is not always the true one.

    Reads a Xing or Info header the way a decoder does, and falls back to the same
    extrapolation a decoder falls back to: first frame's bitrate across the whole
    stream. Comparing this against the frame-counted duration is what catches a
    concatenation whose header lies about its length.
    """
    pos = 0
    while pos < len(audio) and parse_frame(audio, pos) is None:
        pos += 1
    frame = parse_frame(audio, pos)
    if frame is None:
        return None
    length, samples_per_frame, rate = frame

    tag_at = pos + 4 + side_info_size(audio[pos:pos + 4])
    if audio[tag_at:tag_at + 4] in (b"Xing", b"Info"):
        flags = int.from_bytes(audio[tag_at + 4:tag_at + 8], "big")
        if flags & 0x0001:
            frames = int.from_bytes(audio[tag_at + 8:tag_at + 12], "big")
            if frames:
                return frames * samples_per_frame / rate

    bitrate = length * 8 * rate / samples_per_frame
    return len(audio) * 8 / bitrate


def duration(path):
    """True duration of an MP3 file in seconds. Returns None for other formats."""
    if path.suffix.lower() not in (".mp3", ".mp2"):
        return None
    _, audio = strip_tags(path.read_bytes())
    try:
        seconds, _, _ = measure(audio, path.name)
    except SystemExit:
        return None
    return seconds


def fmt(seconds):
    """Human duration, for progress lines."""
    return f"{int(seconds // 60)}m{seconds % 60:04.1f}s"
