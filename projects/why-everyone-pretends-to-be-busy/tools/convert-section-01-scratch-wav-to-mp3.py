from pathlib import Path
import wave

import lameenc


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRATCH_AUDIO_DIR = PROJECT_ROOT / "voiceover" / "section-01-hook" / "scratch-audio"


def convert_wav_to_mp3(wav_path: Path) -> Path:
    mp3_path = wav_path.with_suffix(".mp3")

    with wave.open(str(wav_path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()
        sample_width = wav_file.getsampwidth()
        frames = wav_file.readframes(wav_file.getnframes())

    if sample_width != 2:
        raise ValueError(f"{wav_path.name} is {sample_width * 8}-bit audio; expected 16-bit PCM")

    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)

    mp3_data = encoder.encode(frames) + encoder.flush()
    mp3_path.write_bytes(mp3_data)
    wav_path.unlink()
    return mp3_path


def main() -> None:
    wav_files = sorted(SCRATCH_AUDIO_DIR.glob("section-01-hook-*.wav"))
    if not wav_files:
        raise FileNotFoundError(f"No scratch WAV files found in {SCRATCH_AUDIO_DIR}")

    for wav_path in wav_files:
        mp3_path = convert_wav_to_mp3(wav_path)
        print(mp3_path)


if __name__ == "__main__":
    main()
