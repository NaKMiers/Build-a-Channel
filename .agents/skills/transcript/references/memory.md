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
