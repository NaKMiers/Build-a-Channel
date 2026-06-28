# Section 1 Visual Plan - Hook: Is Any Of This Real?

Video: `Why The Internet Is Full Of Garbage Now`
Section: `Section 1: Hook: Is Any Of This Real?`
Status: `draft visual plan for approval`

## Video-Level Direction (for context - keep identical to master)

- Audience: A2-C1 English learners (interesting-English advantage).
- Renderer: HyperFrames (composited from pre-made assets).
- Visual grammar: real / real-looking base + mascot drawn on top; a new scene roughly per sentence; vary everything (base, WIT side/scale/pose, idea-device).
- Mascot: WIT - round bald white head, thick black outline, big rectangular glasses, dot eyes, flat white body. Big and high (1/3-1/2 frame), a real character with personality; the soul of each scene. Poses ship on flat green #00B140 - chroma-key at render.
- Tone on screen: dry, savage-but-clean; edge aimed at the system/the feed, never the viewer. Keep the strongest words out of the hook; "garbage / slop / fake" carry it.
- Recurring motif: the feed as a rising flood of grey sludge; WIT's glowing phone; the sludge is BORN in this section (Scene 1.8) and returns across the video.
- Scene-type rotation in use: object-on-real-base / mascot-only focus / real-UI phone mockup / hero-evidence card / payoff-text.
- Pose library: `.agents/_shared/assets/wit/poses/` (palette; new poses may be invented).

## Section Overview

- Section goal: open a curiosity gap ("is any of this real?"), show the feed is full of fakes, name the stakes, and hand off to "why." Plant the sludge motif.
- Duration: `~31.3s` (section audio `section-01-hook-david23-am_eric-0.80.mp3`, 31.253s). No word-timings JSON yet, so scene times are ESTIMATED from audio length + tts-input pacing; re-pin to word timings if generated later.
- Scene count: `9`
- Scene-type rotation: 1.1 real-UI phone / 1.2 mascot-focus / 1.3 calm object / 1.4 deadpan closeup / 1.5 hero-evidence (Shrimp Jesus) / 1.6 hero-evidence (fake news) / 1.7 hero-evidence (fake band) / 1.8 motif birth (sludge, giant WIT) / 1.9 mascot-only button.
- Mascot arc in this section: content scroll -> suspicious -> calm/nostalgic -> deadpan -> cringe -> doubtful -> surprised -> drowning -> curious pivot.

## Scenes

### Scene 1.1 - "Quick question. Pick up your phone, open any feed, and scroll for ten seconds."

- **Local time:** `0:00-0:05` (estimated)
- **Role:** Cold open as a direct instruction to the viewer (curiosity-gap setup). Establishes "your feed" as the subject. Leads into the gut-punch question in 1.2.
- **Composition / layout:** Warm living-room real photo fills the frame (lamp glow, evening). A CSS phone mockup floats center-right (~50-78% width, drop-shadow, slight tilt) showing a normal-looking scrolling feed (generic cards, no real brands). WIT enters bottom-right (~58-100% x), giant, holding/looking at a phone. Thin handwritten label upper-left.
- **Elements:**
  - *Base (full frame):* `couch-phone-evening-1.jpg` - a cozy real living room at night, sofa + warm lamp, no faces (hands ok). Bright (~0.8), soft bokeh, reads instantly as "at home, relaxed."
  - *Center-right phone (CSS .screen):* a clean feed mockup - 3-4 neutral content cards scrolling; no real logos; soft blue-white screen glow.
  - *WIT bottom-right:* see Mascot.
  - *Upper-left label:* handwritten.
- **Mascot:** pose `holding_phone_pointing_smile.png`; placement right, scale ~1/2 frame, anchored high (head+torso in frame, only legs cropped), facing slightly left toward the floating phone; expression content/absorbed (he doesn't suspect a thing yet).
- **On-screen text:** `"scroll for 10 seconds"` - handwritten cream/white, upper-left ~6-30% x / 12-22% y, slight tilt, hard-shows on "scroll for ten seconds."
- **Emotion:** familiar, easy, everyday - lull the viewer before the trap.
- **Insight / joke:** this is you, right now, doing the most normal thing in the world.
- **Linkage / eye path:** WIT (right) looks left into the phone -> phone -> label. Eye lands on the feed.
- **Show-as-you-say:** base + WIT from 0:00; phone feed slides up on "open any feed" (~0:02); `scroll for 10 seconds` hard-shows on "scroll for ten seconds" (~0:04).
- **Sound:** soft phone scroll/tick SFX under narration on "scroll"; duck immediately.
- **Color / contrast:** warm room vs cool phone glow; label pops warm-on-dark.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `couch-phone-evening-1.jpg` | browse-real-photo | cozy real living room at night, sofa + warm lamp, no faces, full-HD, CC0 | base, full frame, ~0.8 bright | new |
| `holding_phone_pointing_smile.png` | pose | WIT calmly holding/looking at a phone, content | right, ~1/2 frame, high anchor | reuse (library) |

(The center-right feed phone is a render CSS `.screen` mockup - neutral cards, no real brands - not a stored asset.)

### Scene 1.2 - "Now be honest: how much of that was actually made by a human?"

- **Local time:** `0:05-0:09.5` (estimated)
- **Role:** The curiosity gap snaps shut - the question that powers the whole video. Mascot-only focus beat to make the viewer actually think.
- **Composition / layout:** Near-empty frame: a dark room with a single phone glow real base, heavily simplified. WIT centered and GIANT (~1/2 frame), turned to the viewer. One big handwritten question floats top-center; a small "% human?" gauge sits lower-right.
- **Elements:**
  - *Base (full frame):* `dark-room-phone-glow-1.jpg` - a phone glowing in a dark room, face-free, moody; the only light source.
  - *WIT center:* see Mascot.
  - *Question text (top-center):* handwritten.
  - *Gauge (lower-right, subtitle-safe):* a small hand-drawn dial labeled `% HUMAN?` with the needle wobbling.
- **Mascot:** pose `skeptical_side_eye_doubtful.png`; placement center, scale ~1/2 frame, high anchor, facing viewer with a side-eye; expression "wait... how much of this is real?"
- **On-screen text:** `"how much is REAL?"` - big handwritten white, top-center ~30-70% x / 10-22% y, slight tilt; hard-shows on "be honest." Small `"% human?"` on the dial, appears on "made by a human."
- **Emotion:** dawning suspicion; the comfortable feeling from 1.1 curdles.
- **Insight / joke:** you've never actually asked this question - and you don't know the answer.
- **Linkage / eye path:** big question (top) -> WIT's side-eye (center) -> wobbling gauge (lower-right).
- **Show-as-you-say:** WIT + base from 0:05; `how much is REAL?` hard-shows on "be honest" (~0:06.5); dial + `% human?` on "made by a human" (~0:08.5), needle wobbles (small impact).
- **Sound:** a tiny record-scratch/uh-oh tick on "be honest"; gauge wobble blip.
- **Color / contrast:** near-black base, white text, WIT bright; high contrast = the question dominates.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `dark-room-phone-glow-1.jpg` | browse-real-photo | a phone glowing in a dark room, face-free, moody, full-HD, CC0 | base, full frame | new |
| `skeptical_side_eye_doubtful.png` | pose | WIT side-eye, doubtful | center, ~1/2 frame, high anchor | reuse (library) |

(The `% HUMAN?` dial is a render CSS/hand-drawn overlay, not a stored asset.)

### Scene 1.3 - "Three years ago, the answer was easy. All of it."

- **Local time:** `0:09.5-0:13.5` (estimated)
- **Role:** Establish the "before" - a calm, nostalgic baseline so the "today" turn lands hard. Distinct calm base.
- **Composition / layout:** A warm, clean desk real photo (older laptop vibe) fills frame. A big handwritten date tag `3 YEARS AGO` top-left; a green `100% HUMAN` stamp slaps on center-right over the desk. WIT left, relaxed.
- **Elements:**
  - *Base (full frame):* `cozy-laptop-desk-1.jpg` - a warm, tidy desk with an older-style laptop, no faces, full-HD; reads "the calmer, older internet."
  - *WIT left:* see Mascot.
  - *Date tag (top-left):* handwritten.
  - *Stamp (center-right):* green rubber-stamp style `100% HUMAN`.
- **Mascot:** pose `ok_hand_sign_content_closeup.png`; placement left, scale ~1/3-1/2 frame, high anchor, facing right; expression relaxed/approving ("back then, fine").
- **On-screen text:** `"3 years ago"` handwritten cream top-left; `"100% HUMAN"` green stamp center-right, tilts in on "all of it."
- **Emotion:** warm nostalgia, calm - the last safe moment.
- **Insight / joke:** there really was a time the answer was obvious.
- **Linkage / eye path:** date tag (top-left) -> WIT's OK sign (left) -> green stamp (right).
- **Show-as-you-say:** base + WIT from 0:09.5; `3 years ago` on "three years ago"; `100% HUMAN` stamp impact on "All of it" (~0:12.5).
- **Sound:** soft warm chime; a light stamp thud on the green stamp.
- **Color / contrast:** warm wood tones; green stamp pops as the "good/safe" color (sets up red later).

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `cozy-laptop-desk-1.jpg` | browse-real-photo | warm tidy desk with an older-style laptop, no faces, full-HD, CC0 | base, full frame, ~0.82 bright | new |
| `ok_hand_sign_content_closeup.png` | pose | WIT relaxed, OK hand sign | left, ~1/3-1/2 frame, high anchor | reuse (library) |

### Scene 1.4 - "Today? Good luck."

- **Local time:** `0:13.5-0:16` (estimated)
- **Role:** The hard turn. Deadpan closeup. Tiny, dry, fast - the joke is the flatness.
- **Composition / layout:** Tight on WIT, centered closeup (~1/2-2/3 frame), deadpan. Base is a phone-on-table real photo, screen on, slightly cold grade. Two handwritten words appear: `today...` then `good luck.`
- **Elements:**
  - *Base (full frame, soft-blurred):* `phone-on-table-screen-on-1.jpg` - a phone face-up on a table, screen glowing, no faces, full-HD; cool grade to contrast 1.3's warmth.
  - *WIT center closeup:* see Mascot.
  - *Two-word text:* handwritten.
- **Mascot:** pose `deadpan_unimpressed_half_lidded.png`; placement center, closeup scale ~1/2-2/3 frame (head + glasses dominant, safe crop - no cut through face), facing viewer; expression the channel's signature flat deadpan.
- **On-screen text:** `"today..."` handwritten upper-left (on "Today?"); `"good luck."` handwritten lower-right, subtitle-safe, drops in deadpan on "Good luck."
- **Emotion:** dry comedy; resignation.
- **Insight / joke:** the entire shift from "easy" to "impossible" delivered in two words and a flat face.
- **Linkage / eye path:** `today...` (upper-left) -> WIT deadpan (center) -> `good luck.` (lower-right).
- **Show-as-you-say:** cut to WIT closeup on "Today?"; `today...` hard-shows; beat; `good luck.` hard-shows on "Good luck."
- **Sound:** a single dry "bonk"/silence; let the deadpan breathe.
- **Color / contrast:** cool, desaturated; WIT bright against it.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `phone-on-table-screen-on-1.jpg` | browse-real-photo | phone face-up on a table, screen glowing, no faces, full-HD, CC0, cool grade | base, full frame, soft blur | new |
| `deadpan_unimpressed_half_lidded.png` | pose | WIT flat deadpan, half-lidded | center closeup, ~1/2-2/3 frame, safe crop | reuse (library) |

### Scene 1.5 - "Because somewhere in that feed there is a photo of a shrimp shaped like Jesus,"

- **Local time:** `0:16-0:20` (estimated)
- **Role:** First of three fast "fakes." The iconic, absurd hero image. Cut to evidence.
- **Composition / layout:** A CSS phone mockup left-center floats over a real living-room base, showing the Shrimp Jesus image as a feed post (with fake like/share counts). WIT right, cringing. Tiny handwritten caption under the post.
- **Elements:**
  - *Base (full frame):* `social-scroll-livingroom-1.jpg` - a real, softly-lit living room / sofa scene (distinct from 1.1), no faces; the "still scrolling" context.
  - *Phone post (left-center):* CSS `.screen` feed card containing `shrimp-jesus.jpg` with absurd fake engagement (e.g. "AMEN 47K", thousands of shares).
  - *WIT right:* see Mascot.
  - *Caption:* handwritten under the phone.
- **Mascot:** pose `cringe_uneasy_drool.png`; placement right, scale ~1/2 frame, high anchor, facing left at the phone; expression secondhand-cringe horror.
- **On-screen text:** `"...a shrimp. as Jesus."` handwritten lower-center, subtitle-safe, lands on "shaped like Jesus."
- **Emotion:** absurd disbelief; the funny-disturbing first proof.
- **Insight / joke:** this genuinely exists and genuinely farms millions of likes.
- **Linkage / eye path:** phone post (left) -> caption (center) -> WIT cringe (right).
- **Show-as-you-say:** cut on "Because somewhere in that feed"; `shrimp-jesus.jpg` post slides up on "a photo of a shrimp"; caption + fake like-counter ticks up on "shaped like Jesus."
- **Sound:** a wet/absurd "ding" like a notification, slightly off.
- **Color / contrast:** the uncanny image pops; WIT's white reads against the warm room.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `social-scroll-livingroom-1.jpg` | browse-real-photo | softly-lit real living room/sofa, no faces, full-HD, CC0 (distinct from 1.1) | base, full frame | new |
| `shrimp-jesus.jpg` | browse-real-photo | the iconic Facebook AI-slop "Shrimp Jesus" image (Wikimedia Commons: "Facebook AI slop, Shrimp Jesus") - verify license on file page | inside phone post, left-center | new |
| `cringe_uneasy_drool.png` | pose | WIT cringing, uneasy | right, ~1/2 frame, high anchor | reuse (library) |

### Scene 1.6 - "a news story about an event that never happened,"

- **Local time:** `0:20-0:23` (estimated)
- **Role:** Second fake. Real-UI fake-news card (owner-loved real-UI illustration). Quick cut, new layout (WIT flips to left).
- **Composition / layout:** A fake news/article card floats center-right over a blurred newsroom real base. Big fake headline; a red handwritten cross-out / "DIDN'T HAPPEN" scribble slaps over it. WIT left, doubtful.
- **Elements:**
  - *Base (full frame):* `newsroom-blur-1.jpg` - a blurred press/newsroom or news-website vibe, no faces, full-HD; signals "news."
  - *News card (center-right, CSS):* `fake-news-card.png` - a clean generic news-article card with a plausible-but-vague AI headline (e.g. "Crowds Gather For Parade That Was Never Scheduled") + a too-perfect AI thumbnail; no real outlet branding.
  - *Red markup:* handwritten `DIDN'T HAPPEN` cross-out over the headline.
  - *WIT left:* see Mascot.
- **Mascot:** pose `pondering_skeptical_hand_on_chin.png`; placement left, scale ~1/2 frame, high anchor, facing right; expression "hmm, that didn't happen."
- **On-screen text:** card headline (in-asset); red `DIDN'T HAPPEN` hand-scribble center-right on "never happened."
- **Emotion:** quiet doubt turning to "wait, that's fake."
- **Insight / joke:** the news itself is now invented to farm clicks.
- **Linkage / eye path:** WIT (left) -> news card (center-right) -> red cross-out.
- **Show-as-you-say:** cut on "a news story"; card slides in; red `DIDN'T HAPPEN` impact-scribbles on "never happened."
- **Sound:** a paper/print swoosh; a marker-scribble SFX on the cross-out.
- **Color / contrast:** clean white card vs blurred base; red markup is the only red so far - it pops.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `newsroom-blur-1.jpg` | browse-real-photo | blurred newsroom / news-website vibe, no faces, full-HD, CC0 | base, full frame | new |
| `fake-news-card.png` | generate | isolated clean generic news-article card (vague AI headline about an event that never happened + a too-perfect AI thumbnail), transparent bg, NO real outlet branding | center-right, float w/ shadow | new |
| `pondering_skeptical_hand_on_chin.png` | pose | WIT pondering, skeptical, hand on chin | left, ~1/2 frame, high anchor | reuse (library) |

(Render may instead build the news card in CSS as real-UI; if so, `fake-news-card.png` is unused. Keep the filename reserved.)

### Scene 1.7 - "and a hit song by a band that does not exist."

- **Local time:** `0:23-0:26.5` (estimated)
- **Role:** Third fake. Real-UI music-app card. WIT flips back to right; new device.
- **Composition / layout:** A Spotify-style "now playing" / artist card floats center over a blurred concert/studio real base. Big monthly-listeners number; a handwritten `0 REAL MEMBERS` tag. WIT right, mildly surprised.
- **Elements:**
  - *Base (full frame):* `music-studio-blur-1.jpg` - a blurred concert stage / music studio vibe, no faces, full-HD; signals "music."
  - *Music card (center, CSS):* `fake-band-card.png` - a clean generic music-app artist card: invented band name, a too-smooth AI promo photo, "1,000,000+ monthly listeners," play bar; no real Spotify branding (generic green-free neutral or clearly-generic).
  - *Tag:* handwritten `0 REAL MEMBERS`.
  - *WIT right:* see Mascot.
- **Mascot:** pose `mildly_surprised_hand_at_chin.png`; placement right, scale ~1/2 frame, high anchor, facing left; expression "huh - a million fans, zero people."
- **On-screen text:** card text (in-asset); handwritten `0 REAL MEMBERS` lower-center (subtitle-safe) on "does not exist"; optional small `1,000,000+ listeners` callout pulses on "hit song."
- **Emotion:** the absurdity compounds - now even music is fake and winning.
- **Insight / joke:** a band with a million fans and no humans.
- **Linkage / eye path:** music card (center) -> listeners number -> WIT (right) -> `0 REAL MEMBERS`.
- **Show-as-you-say:** cut on "and a hit song"; card in; listeners counter ticks up on "hit song"; `0 REAL MEMBERS` hard-shows on "does not exist."
- **Sound:** a short music sting that cuts off abruptly (the "fake" gag).
- **Color / contrast:** card pops; WIT bright; keep palette distinct from 1.6's white news card (use a dark music-app card).

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `music-studio-blur-1.jpg` | browse-real-photo | blurred concert stage / music studio, no faces, full-HD, CC0 | base, full frame | new |
| `fake-band-card.png` | generate | isolated clean generic music-app artist card (invented band, too-smooth AI promo photo, "1,000,000+ monthly listeners," play bar), transparent bg, NO real Spotify branding | center, float w/ shadow | new |
| `mildly_surprised_hand_at_chin.png` | pose | WIT mildly surprised, hand at chin | right, ~1/2 frame, high anchor | reuse (library) |

(Render may instead build the artist card in CSS as real-UI; if so, `fake-band-card.png` is unused. Keep the filename reserved.)

### Scene 1.8 - "The internet is filling up with garbage. Cheap, fake, mass-produced garbage. And the strange part is, nobody told it to."

- **Local time:** `0:26.5-0:30` (estimated)
- **Role:** Motif birth + thesis. The grey sludge floods the frame; the three fakes dissolve into it. Giant WIT drowning. Biggest emotional beat of the section.
- **Composition / layout:** A murky grey-sludge real texture base rises from the bottom like a flood. Small slop thumbnails (shrimp, fake hand, fake card) bob in the sludge. WIT center, GIANT, sinking (swim pose) with only head/arms above the "waterline." Big handwritten `GARBAGE` across the top; small `nobody told it to.` lower.
- **Elements:**
  - *Base (full frame):* `grey-sludge-flood-1.jpg` - a murky grey/green water or sludge texture, no faces, full-HD; the literal "garbage flood."
  - *Floating slop bits:* small instances of `shrimp-jesus.jpg`, `ai-extra-fingers-hand.png`, and the fake cards, half-sunk, low opacity.
  - *WIT center:* see Mascot (drowning).
  - *Big word:* handwritten `GARBAGE`.
- **Mascot:** pose `swimming_underwater_goggles_cap.png`; placement center, GIANT (~1/2 frame), anchored so head + goggles + arms are above the sludge line (safe crop - no face cut), facing viewer; expression overwhelmed/sinking. This literally plays the "drowning in slop" motif.
- **On-screen text:** `"GARBAGE"` huge handwritten across top ~20-80% x / 8-24% y, lands on "garbage"; small `"cheap. fake. mass-produced."` staccato chips appear one-per-word; `"nobody told it to."` lower-center (subtitle-safe) on the last line.
- **Emotion:** dread + dark comedy; the scale finally hits.
- **Insight / joke:** the flood has no author - it just rises.
- **Linkage / eye path:** `GARBAGE` (top) -> WIT sinking (center) -> floating slop bits -> `nobody told it to.`
- **Show-as-you-say:** sludge rises on "filling up with garbage"; `GARBAGE` smash on "garbage"; three chips `cheap. / fake. / mass-produced.` pop one per word; slop bits bob in; `nobody told it to.` hard-shows on the last clause.
- **Sound:** a low watery rising "gloop"/flood swell; muffled as WIT sinks; duck under voice.
- **Color / contrast:** muddy grey-green sludge vs WIT white + bold dark `GARBAGE` - the ugliest frame on purpose.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `grey-sludge-flood-1.jpg` | browse-real-photo | murky grey/green water or sludge texture, no faces, full-HD, CC0 | base, full frame, rises from bottom | new |
| `swimming_underwater_goggles_cap.png` | pose | WIT swimming/underwater (plays "drowning in slop") | center, ~1/2 frame, head+arms above sludge line | reuse (library) |
| `shrimp-jesus.jpg` | reuse | the Shrimp Jesus image, half-sunk small | floating, low opacity | reuse (1.5) |
| `ai-extra-fingers-hand.png` | browse-real-photo | AI-generated hand with extra/wrong fingers (Wikimedia Commons "AI generated hand") - verify license | floating slop bit, small | new |

### Scene 1.9 - "Let's find out why."

- **Local time:** `0:30-0:31.3` (estimated)
- **Role:** Button / pivot to the body. Mascot-only focus beat. Resets energy from the sludge to curiosity.
- **Composition / layout:** The sludge recedes to a calm dark base (reuse `grey-sludge-flood-1.jpg` graded darker/clearer as deliberate continuity). WIT center, smaller-than-1.8 but still big, pointing up curiously. One big handwritten `WHY?`.
- **Elements:**
  - *Base (full frame):* `grey-sludge-flood-1.jpg` (reuse, graded darker/settled) - the flood has calmed; continuity into the explanation.
  - *WIT center:* see Mascot.
  - *Big word:* handwritten `WHY?`.
- **Mascot:** pose `pointing_up_curious_open_mouth.png`; placement center, scale ~1/3-1/2 frame, high anchor, facing viewer/up; expression curious "but why?"
- **On-screen text:** `"WHY?"` big handwritten center-top, lands on "why."
- **Emotion:** curiosity rekindled - the viewer wants the answer now.
- **Insight / joke:** transition promise; the rest of the video pays this off.
- **Linkage / eye path:** WIT points up -> `WHY?`.
- **Show-as-you-say:** quick cut on "Let's find out"; `WHY?` pops on "why."
- **Sound:** a small upward "whoosh"/page-turn into Section 2.
- **Color / contrast:** calmer dark base, bright WIT, bold `WHY?` - clean palette reset.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `grey-sludge-flood-1.jpg` | reuse | settled/darker grade of the sludge base (deliberate continuity from 1.8) | base, full frame | reuse (1.8) |
| `pointing_up_curious_open_mouth.png` | pose | WIT pointing up, curious | center, ~1/3-1/2 frame, high anchor | reuse (library) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `couch-phone-evening-1.jpg` | browse-real-photo | 1.1 | - | warm living room base |
| `dark-room-phone-glow-1.jpg` | browse-real-photo | 1.2 | - | moody phone-glow base |
| `cozy-laptop-desk-1.jpg` | browse-real-photo | 1.3 | - | "3 years ago" calm base |
| `phone-on-table-screen-on-1.jpg` | browse-real-photo | 1.4 | - | cool deadpan base |
| `social-scroll-livingroom-1.jpg` | browse-real-photo | 1.5 | - | living room (distinct from 1.1) |
| `shrimp-jesus.jpg` | browse-real-photo | 1.5 | 1.8 | Commons AI-slop hero; verify license |
| `newsroom-blur-1.jpg` | browse-real-photo | 1.6 | - | news base |
| `fake-news-card.png` | generate | 1.6 | - | isolated card; or render-CSS real-UI |
| `music-studio-blur-1.jpg` | browse-real-photo | 1.7 | - | music base |
| `fake-band-card.png` | generate | 1.7 | - | isolated card; or render-CSS real-UI |
| `grey-sludge-flood-1.jpg` | browse-real-photo | 1.8 | 1.9 | the garbage-flood motif base |
| `ai-extra-fingers-hand.png` | browse-real-photo | 1.8 | - | Commons "AI generated hand"; verify license |
| `holding_phone_pointing_smile.png` | pose | 1.1 | - | library |
| `skeptical_side_eye_doubtful.png` | pose | 1.2 | - | library |
| `ok_hand_sign_content_closeup.png` | pose | 1.3 | - | library |
| `deadpan_unimpressed_half_lidded.png` | pose | 1.4 | - | library |
| `cringe_uneasy_drool.png` | pose | 1.5 | - | library |
| `pondering_skeptical_hand_on_chin.png` | pose | 1.6 | - | library |
| `mildly_surprised_hand_at_chin.png` | pose | 1.7 | - | library |
| `swimming_underwater_goggles_cap.png` | pose | 1.8 | - | library; plays "drowning in slop" |
| `pointing_up_curious_open_mouth.png` | pose | 1.9 | - | library |

## Approval Checks

- each scene picturable from text alone: yes
- ~one scene per sentence, scene-types varied: yes (9 scenes, rotated types)
- every scene has a real/real-looking base: yes (no bare gradients)
- mascot big/high with a specific pose+expression per scene: yes (varied side/scale/pose each scene)
- show-as-you-say timeline present per scene: yes (timing estimated - no word-timings JSON yet)
- every asset has type + description + filename + layout: yes
- repeated subjects reuse the same filename: yes (shrimp-jesus, grey-sludge-flood reused)
- public figures handled as caricature/parody, punching up: n/a (no public figures in this section)
- no image-generation prompts written here: correct (descriptions only)
- in sync with master `04-visual-plan.md`: yes
