# Transcript Memory

## Current profile

`--pause 0.24 --max-dur 3.2 --min-words 2`

This profile normally yields 22 to 32 cues per minute. Always save the word cache so cue
density can be changed without another API call.

## Durable lessons

- Combine multi-part audio first and use measured offsets.
- Align each part to the matching script segment, then merge word caches.
- Compare part-level words per second before paying for alignment.
- Duplicate timestamps need an explicit downstream filename remap.
- The final cue should land close to the true audio duration.

## Detecting a degenerate alignment

Forced alignment can return HTTP 200 and still be unusable. It anchors the words it finds,
then pins every remaining word to the end of the file. The last cue still lands at the true
duration, so the Step 3 duration check passes and the transcript still looks plausible.

Check the saved cache before trusting any transcript:

```bash
python3 - <<'EOF'
import json,statistics
ws=json.load(open("<words.json>"))
d=[w["end"]-w["start"] for w in ws]
tiny=sum(1 for x in d if x<=0.002)
print(f"median {statistics.median(d):.3f}s  max {max(d):.1f}s  near-zero {tiny}/{len(ws)}")
EOF
```

Healthy narration has a median word duration near 0.2 to 0.4s and few near-zero words. A
median of 0.001s, a single word spanning tens or hundreds of seconds, or more than about a
tenth of words at or under 2ms means the alignment failed. Bucketing word starts per 30s
shows it plainly: a failed run stacks most of the words in the final bucket.

Project 2 failed this way on both parts, with 80 percent of part-1 words at or under 2ms
and 890 of 895 part-2 words pinned past 5:00, despite a lossless script split whose parts
matched the measured durations to within 3 percent words per second. A verified split does
not prove the audio matches the script.

## Known tool bug

Degenerate word timings make `tsfmt.py _split_long` recurse until `RecursionError`, because
no internal cut can bring a cue under `--max-dur`. The crash happens after the API call, so
the credits are already spent, and `--save-json` has written the cache. Re-cut from that
cache rather than re-calling. The tool should reject degenerate input with a clear message
instead of recursing.

## Quota

ElevenLabs refuses with HTTP 401 and `quota_exceeded`, naming credits remaining and
credits required. Roughly 346 credits covered one 5-minute part, so budget about 700 for a
two-part 10-minute episode. Check the balance before splitting the script.

## Root cause of project 2's failure: swapped part files, not bad alignment

The degenerate alignment above was a symptom, not the disease. Project 2's `part-1.mp3`
and `part-2.mp3` were saved in the wrong chronological order relative to their names, so
every `--script` passed to `audio-to-timestamps.py` was aligned against the wrong half of
the narration. The proportional word-count split (matched to each part's measured
duration) still produced a plausible-looking near-3-percent words-per-second spread, which
is why the mismatch was not visible from the numbers alone. Forced alignment quietly does
its best on the front of a mismatched file, then collapses for everything after the point
where the supplied text and the actual speech diverge.

Detecting this needs actual content, not just duration math. Once both alignments failed
identically twice in a row (ruling out a transient service issue), the fix was to get an
independent transcript of each raw file and read where its content actually falls in the
script:

```bash
curl -s -X POST "https://api.elevenlabs.io/v1/speech-to-text" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -F "model_id=scribe_v1" -F "file=@part-N.mp3" \
  -o stt_full_part-N.json
python3 -c "import json; print(json.load(open('stt_full_part-N.json'))['text'])"
```

This is a paid diagnostic (each call transcribes a whole part), so use it only after a
deterministic failure, not as a first resort. Once the true content of each file is known,
locate the exact word count in the script where the recording actually breaks (search for
the sentence the STT transcript ends or begins on), and re-split the script there instead
of trusting the proportional estimate. Project 2's real break was 5 sentences later than
the duration-based estimate: 885 and 860 words rather than 850 and 895, which brought the
two parts from a 3 percent words-per-second spread down to 0.65 percent and let both parts
align cleanly with a healthy median word duration near 0.2s and zero near-zero words.

If the swap is confirmed, rename the files on disk into their true order and rebuild
`full.mp3` and `offsets.json` before re-aligning, so the final transcript timestamps and
the editor's timeline agree.

## A repeated identical failure is a real signal, not bad luck

When a forced-alignment run degenerates (see above), re-running it with nothing changed
and getting the exact same word-for-word degenerate output twice means the failure is
deterministic given that audio and that script text. Do not spend a third paid call
retrying the identical inputs. Something about the pairing is wrong, most likely a content
mismatch (wrong file, wrong order, or stale script draft), and the fix is to find that
mismatch, not to hope for a different result from the same API call.
