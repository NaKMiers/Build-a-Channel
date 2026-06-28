# 03 Voiceover

Video: `Vì sao giá vàng tăng điên cuồng?`

Status: `section voiceover generated (All sections)`

Source skill: `voiceover`

Source file:

- `02-script.md`

> Experiment note: Vietnamese video. The default channel voice (Kokoro `am_eric`) has NO Vietnamese
> support, so this project uses **edge-tts** (Microsoft Edge TTS). The default English `David23 /
> am_eric` voice is unchanged for the rest of the channel.

## Voice Direction

- Default final voice (channel, English): `David23 / am_eric / 0.84 / en-us` (NOT usable for Vietnamese)
- Current generation voice (this VN experiment): `vi-VN-NamMinhNeural` (young male, VN equivalent of David23)
- Engine: `edge-tts 7.2.8` (Microsoft Edge TTS - free, no API key, needs internet)
- Rate: `normal` · Language: `vi-VN`
- Tone: deadpan + cà khịa, kiểu Vui Vẻ; brisk pace
- Voice status: `owner-approved voice (Nam); rate normal - adjustable (--rate=-8%) if clarity needs it`
- Markup: `[pause]/[beat]/[deadpan]/[slower]` are stripped before TTS (edge-tts would read them aloud); marked source stays in `02-script.md`.

## Section Voiceover Index

|   # | Section | Status | Voice | Rate | Duration | Audio file | Notes |
| --: | ------- | ------ | ----- | ---- | -------: | ---------- | ----- |
| 1 | Hook: cục kim loại không làm gì | generated | vi-VN-NamMinhNeural | normal | 29.35s | `voiceover/section-01-hook/scratch-audio/section-01-hook-nam-minh.mp3` | |
| 2 | Vàng = phong vũ biểu nỗi sợ | generated | vi-VN-NamMinhNeural | normal | 31.54s | `voiceover/section-02-phong-vu-bieu-noi-so/scratch-audio/section-02-phong-vu-bieu-noi-so-nam-minh.mp3` | |
| 3 | Lãi suất & đồng đô | generated | vi-VN-NamMinhNeural | normal | 42.65s | `voiceover/section-03-lai-suat-dong-do/scratch-audio/section-03-lai-suat-dong-do-nam-minh.mp3` | |
| 4 | Lạm phát & bất ổn | generated | vi-VN-NamMinhNeural | normal | 38.18s | `voiceover/section-04-lam-phat-bat-on/scratch-audio/section-04-lam-phat-bat-on-nam-minh.mp3` | |
| 5 | NHTW & đám đông | generated | vi-VN-NamMinhNeural | normal | 49.22s | `voiceover/section-05-nhtw-dam-dong/scratch-audio/section-05-nhtw-dam-dong-nam-minh.mp3` | |
| 6 | Payoff: mua sự an tâm | generated | vi-VN-NamMinhNeural | normal | 41.09s | `voiceover/section-06-payoff-an-tam/scratch-audio/section-06-payoff-an-tam-nam-minh.mp3` | có câu miễn trừ đầu tư |
| 7 | Outro | generated | vi-VN-NamMinhNeural | normal | 16.20s | `voiceover/section-07-outro/scratch-audio/section-07-outro-nam-minh.mp3` | |

Total spoken audio: `~248.2s` (~4:08).

## Section Details

Each section folder contains: `*-script.txt` (clean text fed to TTS), `tts-inputs/*.txt`,
`scratch-audio/*-nam-minh.mp3`, `scratch-results.json`, `README.md`.

Regenerate any section:

```bash
python -m edge_tts --voice vi-VN-NamMinhNeural \
  --file voiceover/<section>/tts-inputs/<section>.txt \
  --write-media voiceover/<section>/scratch-audio/<section>-nam-minh.mp3
# slower for clarity: add --rate=-8%
```

## Stale / Regeneration Notes

- Brand-new project; `04-visual-plan.md` and later are still empty stubs → nothing real to mark stale.
- Total runtime came in ~4:08 vs the script's ~5:10 estimate (NamMinh is brisk). If the owner wants a
  calmer pace, regenerate all sections with `--rate=-8%` (would lengthen ~10%).
- If the script (`02-script.md`) changes, regenerate the affected section(s) and update this index.

## Next Step Boundary

Next workflow step: `Visual plan` (the rebuilt skill - master plan + synced sections, per-sentence
scenes, ASSET lists). Then `visual-implement`, then `render`. Do not continue into those until asked.
