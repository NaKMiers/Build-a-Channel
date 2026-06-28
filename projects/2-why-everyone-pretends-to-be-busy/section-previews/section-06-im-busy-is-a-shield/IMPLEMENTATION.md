# Section 6 Implementation - "I'm Busy" Is A Shield

Composition: `Section06Shield` · 1920x1080 · 38.04s · port 1006

## Build summary
- 5 scenes on tracks 1/3/4/5/6, 5 cue groups on track 2 (one per scene), audio on track 10.
- Every scene base is a REAL people-free photo; shield / speech bubbles / chat built in CSS on top.
- Real-UI chat (1:1 scene B, group scene E) with the real Messenger icon; WIT in cue divs.
- GSAP: reveal/show/smash helpers; scene-internal elements (shield, bubbles, chat msgs, speech) revealed at word times; cue labels/WIT/stamps shown on their words.

## Scenes
1. **A - THE SHIELD** (0–8.30): base-office + scrim; CSS shield `I'M BUSY` (clip-path), two request bubbles bounce in (4.46 / 6.30), WIT deadpan behind. Shield smashes in on "shield" @3.52.
2. **B - chat reality** (8.26–15.38): base-desk-chat + floating `.screen`; Messenger 1:1 chat - "Quick question?"/"Got a sec?" incoming, "I'm busy 🙂" reply @11.10; captions STOP ASKING @9.08, (=NO IDEA, STAY CALM) @13.90; WIT facepalm @12.86.
3. **C - OVERLOADED** (15.34–20.12): base-overloaded (sticky-note wall); NOT ALWAYS DISHONEST @15.34, OVERLOADED stamp @18.56, THE SHIELD IS REAL @19.28; WIT sleeping-burned-out.
4. **D - what you can't say** (20.08–32.18): base-meeting (empty conference room); THE ONLY OK "NO" @20.28; struck speech bubble "I need quiet time to think" → TOO RELAXED @27.48; struck "This meeting could've been a message" → TOO DANGEROUS @31.70; WIT shocked @31.60.
5. **E - everyone nods** (32.14–38.04): base-desk-group + floating `.screen`; group chat bubbles (So busy / Swamped / Slammed / Same) stack @33.26–36.60; OR BOTH @37.54; WIT tiny-defeated.

## QA
- `hyperframes lint`: 0 errors (1 advisory `timeline_track_too_dense`, same as prior sections).
- `hyperframes validate`: 0 errors; contrast advisories are fixed-sample-time measurements of off-screen elements (same pattern as prior sections); visible labels use cream/red/green cards with dark text.
- `hyperframes snapshot --at 3.6,5,9.5,14,17,19.5,21,27.5,31.9,35,37.7`: all 5 scenes verified - shield + bubbles, 1:1 chat + reply + captions, sticky-note wall + OVERLOADED + burned-out WIT, meeting room + two struck bubbles + red stamps + shocked WIT, group chat full of "busy" + OR BOTH + defeated WIT.

## Fixes during build
- duplicate_media_discovery_risk (Messenger icon reused in B + E) → copied to `messenger-grp.png` for scene E.
- Removed the green "I'M BUSY ✓" speech bubble in D (revealed <0.3s before the cut; redundant with Scene E payoff).

## Notes
- Audio is 0.86 (pause-tuned), consistent with Sections 4–7.
- Sources: base-office/desk-chat/desk-group = CC0 StockSnap; base-overloaded = Wikimedia CC BY 3.0; base-meeting = rawpixel CC0; Messenger icon = Wikimedia. People-free, editorial real-UI.
- No MP4/WebM exported (not requested).
