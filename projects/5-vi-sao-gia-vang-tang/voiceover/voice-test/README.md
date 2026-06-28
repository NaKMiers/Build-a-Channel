# Vietnamese Voice Test - `5-vi-sao-gia-vang-tang` (Experiment)

The channel's default TTS is **Kokoro** (via HyperFrames `tts`), whose languages are
en-us/en-gb/es/fr/hi/it/pt-br/ja/zh - **no Vietnamese**. So this Vietnamese experiment uses a
different engine for voiceover.

## Chosen engine: Microsoft Edge TTS (`edge-tts`)

- Free, no API key; needs internet (Microsoft speech endpoint reachable from this box).
- Installed: `edge-tts 7.2.8` (via `python -m pip install edge-tts`; Python 3.12/3.14 available).
- High-quality Vietnamese neural voices.

## Voice options tested (samples in this folder)

| File | Voice ID | Gender | Note |
|---|---|---|---|
| `test-nam-minh.mp3` | `vi-VN-NamMinhNeural` | male | recommended - VN equivalent of the channel's young-male narrator (David23) |
| `test-hoai-my.mp3` | `vi-VN-HoaiMyNeural` | female | alternative |

Test line (from script Section 1 hook): *"Vàng không trả lãi. Không trả cổ tức. Không nhắn tin chúc
bạn ngủ ngon. Vậy mà cứ vài tháng, cả nước lại lao đi mua nó như sắp hết hàng."* (~11s each)

## Generate command

```bash
python -m edge_tts --voice vi-VN-NamMinhNeural --text "<text>" --write-media out.mp3
# slower for clarity if needed: add --rate=-8%   (or -5%, -10%)
# pitch tweak if wanted:          add --pitch=-2Hz
```

## Status

Chosen channel-VN voice: `PENDING owner pick` (NamMinh male recommended).
Once picked, `voiceover` for this project uses edge-tts with that voice instead of Kokoro/am_eric.
This is **experiment tooling only** - it does NOT change the default English `David23 / am_eric` voice.
