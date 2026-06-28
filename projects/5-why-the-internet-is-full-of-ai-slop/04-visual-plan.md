# 04 Visual Plan (master)

Video: `Why The Internet Is Full Of Garbage Now`
Status: `master visual plan in progress`
Source skill: `visual-plan`
Source files: `02-script.md`, `03-voiceover.md`

## Video-Level Direction

- Audience: `A2-C1 English learners (interesting-English advantage)`
- Renderer: `HyperFrames (composited from pre-made assets)`
- Visual grammar: `real / real-looking base + mascot drawn on top; new scene ~per sentence; vary everything`
- Mascot character: `WIT - round bald white head, thick black outline, big rectangular glasses, dot eyes, flat white body. A real character with dry personality; big and high (1/3-1/2 frame), the soul of each scene. Poses ship on flat green #00B140 - chroma-key at render.`
- Tone on screen: `dry, savage-but-clean; edge aimed at the system/the feed, never the viewer; "garbage / slop / fake" carry the hook (strongest words kept out of the open)`
- Recurring motif: `the feed as a rising flood of grey sludge + WIT's glowing phone; the sludge is BORN in Section 1 (Scene 1.8) and should return at later beats (the spread, the payoff)`
- Scene-type rotation in use: `object-on-real-base / mascot-only focus / real-UI phone-or-card mockup / hero-evidence card / payoff-text`
- Pose library: `.agents/_shared/assets/wit/poses/` (palette; new poses may be invented)

## Section Index

| # | Section | Status | Duration | Scenes | Assets named | Section file |
|---:|---|---|---:|---:|---:|---|
| 1 | Hook: Is Any Of This Real? | planned | ~31.3s | 9 | 20 | `visual-plan/section-01-hook/section-01-hook-visual-plan.md` |
| 2 | It Has A Name: Slop | planned | ~36.7s | 8 | 14 | `visual-plan/section-02-it-has-a-name-slop/section-02-it-has-a-name-slop-visual-plan.md` |
| 3 | What Slop Actually Is | planned (v2 rebuild, generate-forward) | 40.7s | 9 | 10 generate + 8 browse + 9 poses | `visual-plan/section-03-what-slop-actually-is/section-03-what-slop-actually-is-visual-plan.md` |
| 4 | The Machine That Feeds Itself | planned (generate-forward) | 53.0s | 9 | 8 generate + 7 browse + 1 reuse (S3) + 9 poses | `visual-plan/section-04-the-machine-that-feeds-itself/section-04-the-machine-that-feeds-itself-visual-plan.md` |
| 5 | It Already Got Out | planned (generate-forward) | 53.7s | 7 | 6 generate + 4 browse + 2 reuse + 7 poses | `visual-plan/section-05-it-already-got-out/section-05-it-already-got-out-visual-plan.md` |
| 6 | It's Not AI's Fault (And Not A Plot) | planned (generate-forward) | 38.9s | 7 | 4 generate + 4 browse + 2 reuse + 7 poses | `visual-plan/section-06-its-not-ais-fault/section-06-its-not-ais-fault-visual-plan.md` |
| 7 | Payoff: Attention In, Garbage Out | planned (callback-heavy) | 43.4s | 7 | 1 generate + 2 browse + 5 reuse + 7 poses | `visual-plan/section-07-attention-in-garbage-out/section-07-attention-in-garbage-out-visual-plan.md` |
| 8 | Outro: Like, Share, Subscribe | planned (light outro) | 8.0s | 2 | 0 generate + 0 browse + 2 reuse + 2 poses | `visual-plan/section-08-outro-like-share-subscribe/section-08-outro-like-share-subscribe-visual-plan.md` |

## All Sections (scenes)

> Each section below is identical to its `visual-plan/section-XX-*/` file. Keep them in sync.

### Section 1: Hook: Is Any Of This Real?

Section goal: open a curiosity gap ("is any of this real?"), show the feed is full of fakes, name the
stakes, hand off to "why," and plant the sludge motif. Duration ~31.3s (audio 31.253s; scene times
ESTIMATED - no word-timings JSON yet). 9 scenes. Mascot arc: content scroll -> suspicious ->
calm/nostalgic -> deadpan -> cringe -> doubtful -> surprised -> drowning -> curious pivot.

#### Scene 1.1 - "Quick question. Pick up your phone, open any feed, and scroll for ten seconds."
- Time `0:00-0:05` (est). Role: cold-open instruction; establishes "your feed"; leads to the question.
- Layout: warm living-room real base; CSS feed phone floats center-right; giant WIT bottom-right holding phone; handwritten label upper-left.
- Base `couch-phone-evening-1.jpg` (browse). Mascot `holding_phone_pointing_smile.png` (right, ~1/2 frame, high), casual/absorbed scroll. Text `"scroll for 10 seconds"` upper-left on the cue.
- Show-as-you-say: base+WIT 0:00; feed slides up on "open any feed"; label on "scroll for ten seconds." SFX: soft scroll tick.

#### Scene 1.2 - "Now be honest: how much of that was actually made by a human?"
- Time `0:05-0:09.5` (est). Role: the curiosity gap snaps shut; mascot-only focus.
- Layout: near-empty dark phone-glow base; GIANT WIT centered, side-eye; big question top-center; `% HUMAN?` dial lower-right (subtitle-safe).
- Base `dark-room-phone-glow-1.jpg` (browse). Mascot `skeptical_side_eye_doubtful.png` (center, ~1/2 frame). Text `"how much is REAL?"` top-center on "be honest"; `% human?` dial on "made by a human."

#### Scene 1.3 - "Three years ago, the answer was easy. All of it."
- Time `0:09.5-0:13.5` (est). Role: calm nostalgic "before."
- Layout: warm older-laptop desk base; WIT left relaxed; `3 YEARS AGO` tag top-left; green `100% HUMAN` stamp center-right.
- Base `cozy-laptop-desk-1.jpg` (browse). Mascot `ok_hand_sign_content_closeup.png` (left). Text `"3 years ago"`, green stamp `"100% HUMAN"` impact on "All of it."

#### Scene 1.4 - "Today? Good luck."
- Time `0:13.5-0:16` (est). Role: hard turn; deadpan closeup; the joke is the flatness.
- Layout: cool phone-on-table base (soft blur); WIT center closeup deadpan (safe crop); `today...` upper-left then `good luck.` lower-right.
- Base `phone-on-table-screen-on-1.jpg` (browse). Mascot `deadpan_unimpressed_half_lidded.png` (center closeup). SFX: dry bonk/silence.

#### Scene 1.5 - "Because somewhere in that feed there is a photo of a shrimp shaped like Jesus,"
- Time `0:16-0:20` (est). Role: first fake; iconic absurd hero.
- Layout: living-room base; CSS phone post left-center showing Shrimp Jesus with absurd fake engagement; WIT right cringing; caption lower-center.
- Base `social-scroll-livingroom-1.jpg` (browse). Hero `shrimp-jesus.jpg` (browse, Commons; verify license). Mascot `cringe_uneasy_drool.png` (right). Text `"...a shrimp. as Jesus."` on "shaped like Jesus."

#### Scene 1.6 - "a news story about an event that never happened,"
- Time `0:20-0:23` (est). Role: second fake; real-UI fake-news card; WIT flips left.
- Layout: blurred newsroom base; fake news card center-right; red `DIDN'T HAPPEN` cross-out; WIT left doubtful.
- Base `newsroom-blur-1.jpg` (browse). Card `fake-news-card.png` (generate; or render-CSS real-UI). Mascot `pondering_skeptical_hand_on_chin.png` (left). Red markup on "never happened."

#### Scene 1.7 - "and a hit song by a band that does not exist."
- Time `0:23-0:26.5` (est). Role: third fake; real-UI music-app card; WIT flips right.
- Layout: blurred music base; dark artist card center with "1,000,000+ monthly listeners"; `0 REAL MEMBERS` tag; WIT right surprised.
- Base `music-studio-blur-1.jpg` (browse). Card `fake-band-card.png` (generate; or render-CSS real-UI). Mascot `mildly_surprised_hand_at_chin.png` (right). Text `"0 REAL MEMBERS"` on "does not exist."

#### Scene 1.8 - "The internet is filling up with garbage. Cheap, fake, mass-produced garbage. And the strange part is, nobody told it to."
- Time `0:26.5-0:30` (est). Role: motif birth + thesis; the sludge floods; giant WIT drowning.
- Layout: murky grey-sludge base rising from bottom; slop bits bob in it; GIANT WIT center sinking (swim pose, head/arms above the line); huge `GARBAGE` top; `cheap. fake. mass-produced.` chips one-per-word; `nobody told it to.` lower.
- Base `grey-sludge-flood-1.jpg` (browse). Mascot `swimming_underwater_goggles_cap.png` (center, ~1/2 frame). Reuse `shrimp-jesus.jpg`; add `ai-extra-fingers-hand.png` (browse Commons; verify license). SFX: low watery flood swell.

#### Scene 1.9 - "Let's find out why."
- Time `0:30-0:31.3` (est). Role: button/pivot; mascot-only focus; energy reset.
- Layout: settled darker grade of the sludge base (continuity); WIT center pointing up curious; big `WHY?`.
- Base `grey-sludge-flood-1.jpg` (reuse, settled grade). Mascot `pointing_up_curious_open_mouth.png` (center). Text `"WHY?"` on "why." SFX: upward whoosh into Section 2.

Section 1 asset list: see `visual-plan/section-01-hook/section-01-hook-visual-plan.md` (Section Asset
Summary) - 12 image assets (8 real bases incl. 1 reused, 2 Commons AI-slop images, 2 generate cards)
+ 9 library poses. Full per-scene detail (composition %, elements, emotion, linkage, sound, color,
asset table) lives in the section file and is the source of truth; this master block is its synced summary.

### Section 2: It Has A Name: Slop

Section goal: NAME the phenomenon ("slop", Word of the Year), then reframe - not "AI is evil", not a
master plan; it's cheap content + pay-for-attention. End on the flood "still rising." Duration ~36.7s
(scene times ESTIMATED; render will pin to word timings). 8 scenes. Mascot arc: announcing -> disgusted
-> proud -> dismissive -> deadpan -> skeptical -> teaching -> uneasy. Full detail in the section file.

- 2.1 `0:00-4.6` "...we call it slop." - sludge motif base (reuse, darker) + WIT presenting (right); "SLOP" stamp smash on "slop".
- 2.2 `4.6-9.2` "...grey mush you pour into a pig trough." - `pig-trough-slop-1.jpg` + WIT disgust (left); "grey mush" arrow.
- 2.3 `9.2-15.2` "...Word of the Year in 2025." - `dictionary-open-1.jpg` + CSS dictionary entry + gold WotY badge; WIT proud (right).
- 2.4 `15.2-20.8` "...AI is evil and the robots are coming." - `toy-robot-1.jpg` + "AI = EVIL ROBOTS" red cross-out; WIT waving off (center).
- 2.5 `20.8-23.0` "That's a different video." - sludge (reuse, very dark) mascot-only deadpan closeup; caption.
- 2.6 `23.0-28.6` "...not because of some master plan." - `corkboard-redstring-1.jpg` conspiracy board + "A MASTER PLAN" red cross-out; WIT skeptical (left).
- 2.7 `28.6-34.8` "...pays you for attention, not for quality." - `coins-pile-1.jpg` + CSS `ATTENTION=PAID` vs greyed `QUALITY`; WIT teaching (right).
- 2.8 `34.8-36.7` "So a flood started. And it is still rising." - sludge motif (reuse), rising overlay + giant WIT uneasy (center); "STILL RISING" smash.

Section 2 assets: 5 new browse photos (pig-trough, dictionary, toy-robot, corkboard-redstring, coins-pile)
+ reuse `grey-sludge-flood-1.jpg` (motif) + 8 library poses; dictionary card / WotY badge / ATTENTION-vs-QUALITY
/ crossed-cliché labels are render-CSS. Full per-scene detail in the section file (source of truth).

### Section 3: What Slop Actually Is (v2 REBUILD - generate-forward, no sludge)

REBUILT 2026-06-28 (owner-directed): v1 over-reused the sludge and leaned on browsed/old photos. v2 is
wild + GENERATE-FORWARD with a bespoke surreal hero per scene; the section's new motif is THE SLOP
MACHINE (a content-grinder), NOT the sludge. Timing pinned to REAL word-timings. 9 scenes. Mascot arc:
announcer -> sarcastic awe -> horror -> baffled -> howling laugh -> flattened -> blasted -> smug -> deadpan.

- 3.1 `0-2.96` "...three things." - factory base + GEN `slop-machine` (brain in, grey slop out); WIT announcing (right); "3 THINGS".
- 3.2 `2.96-6.80` "...looks fine." - studio + GEN `ai-influencer-perfect` (flawless plastic); WIT mock-awe (left); "1. LOOKS FINE".
- 3.3 `6.80-9.80` "...falls apart. six fingers." - studio (reuse) + GEN `ai-influencer-melting` (same shot glitching, 6 fingers) + red circle; WIT horror (right).
- 3.4 `9.80-11.10` "gibberish." - night storefront + GEN `gibberish-melting-sign`; WIT baffled (left).
- 3.5 `11.10-17.48` "...'Coca-Coola.'" - holiday street + GEN `coca-coola-ad-fail` (parody, no real logo) + red circle; WIT howling (right).
- 3.6 `17.48-25.94` "...costs you everything." - server room + GEN `cost-crush-pile` (clocks/eyes/hearts avalanche) CRUSHING WIT (`lying_down_fainted_dead`, center); time/attention/trust labels.
- 3.7 `25.94-33.22` "...made by the thousand... fire hose." - pipes + GEN `slop-firehose` + GEN `slop-clone` (tiled) + "10,000+"; WIT blasted (center-right).
- 3.8 `33.22-37.26` "...That is slop." - factory callback + reuse `slop-machine` + GEN `certified-slop-stamp`; WIT smug (right).
- 3.9 `37.26-40.704` "a machine pretending to be a person, at full volume." - dark stage + GEN `robot-human-mask` (robot in human mask screaming into a mic) + volume-MAX; WIT deadpan (bottom-left).

Section 3 assets: 10 GENERATE heroes (slop-machine, ai-influencer-perfect/melting, gibberish-melting-sign,
coca-coola-ad-fail, cost-crush-pile, slop-firehose, slop-clone, certified-slop-stamp, robot-human-mask) +
8 FRESH browse bases + 9 library poses. NO sludge. CSS: "3 THINGS", marks, red circles, checks, counters,
maker/cost labels, volume meter. Full detail in the section file.

### Section 4: The Machine That Feeds Itself (generate-forward, the mechanism core)

Section goal: explain the incentive chain step by step (the heart of the video) - 5 steps that each land
separately so a learner follows by ear. Duration 53.0s (audio 52.971s; scene times ESTIMATED - NO
word-timings JSON yet, render must generate them and re-pin). 9 scenes. NEW section motif = THE
SELF-FEEDING ENGINE (a circular machine: prompt in -> slop out -> coins -> a return pipe loops the money
back), a deliberate callback to S3's slop-machine; teased dormant (4.1), roars shut as the loop closes
(4.8), labeled in the verdict (4.9). A CSS loop-ring HUD gains one node per Step and completes at 4.8.
Mascot arc: sly setup -> "the old way" -> scheming-cheap -> smug platform boss -> lecturing the thesis
-> manic flood -> disgusted at the blind algorithm -> dismayed as the loop closes -> dry verdict.

- 4.1 `0-6.5` "...follow the money - slowly... the whole video." - `dark-machine-hall-1.jpg` + GEN `slop-engine-loop` (dormant/dark) + GEN `money-trail-coins`; WIT sly (`smug_sly_smirk_leaning`, left); "FOLLOW THE MONEY".
- 4.2 `6.5-12.0` "Step one... used to be expensive... writer, camera, musician, time." - `vintage-film-set-1.jpg` + GEN `old-creation-cost-pile` (camera+typewriter+guitar+hourglass+$$$); WIT presenting (right); "STEP 1 / used to be EXPENSIVE".
- 4.3 `12.0-16.5` "Now... a prompt and ten seconds... almost zero." - `clean-bright-desk-1.jpg` + GEN `prompt-box-instant`; CSS `$$$ -> $0` counter; WIT scheming (`sly_scheming_twiddling_fingers`, left).
- 4.4 `16.5-24.0` "Step two... pays you for engagement - clicks, likes, time spent." - `casino-slot-machines-1.jpg` + GEN `engagement-slot-machine` (like/click/clock reels); WIT as platform boss (`boss_suit_sunglasses_sparkle`, right); chips clicks/likes/time.
- 4.5 `24.0-27.5` "[slower] It rewards attention, not quality." - PIVOT; `dark-spotlight-stage-1.jpg` + GEN `attention-quality-scale` (attention crashes down, quality flies up); WIT lecturing (`lecturing_finger_raised_eyes_closed`, center); kinetic "ATTENTION, not quality".
- 4.6 `27.5-36.5` "Step three... flood the zone - post a thousand cheap things, hope a few go viral." - `wall-of-screens-grid-1.jpg` + GEN `flood-the-zone-cannon` + reuse `slop-clone` (tiled barrage) + one gold `VIRAL`; WIT manic (`manic_gleeful_googly_eyes`, center-right).
- 4.7 `36.5-43.0` "Step four... can't tell slop from real... serves the slop anyway." - `cctv-control-room-1.jpg` + GEN `blindfold-sorter-robot` stamping `SERVE` on real + slop alike; WIT disgusted (`annoyed_disgusted_open_frown`, left); `CAN'T TELL`.
- 4.8 `43.0-48.5` "Step five... pays for more slop. [beat] The machine feeds itself." - `dark-machine-hall-1.jpg` (reuse, lit) + reuse `slop-engine-loop` (roaring, return loop closes); WIT dismayed (`shocked_sweating_dismayed`, right); loop-ring completes; "THE MACHINE FEEDS ITSELF".
- 4.9 `48.5-52.971` "...the whole engine. Cheap to make, paid by attention, impossible to filter. Of course it floods." - reuse engine (labeled "THE WHOLE ENGINE") + CSS grey sludge overflow (tie-back to the S1-S2 flood + setup for S5); 3 staccato stamps; WIT dry (`deadpan_unimpressed_half_lidded`, center-left).

Section 4 assets: 8 GENERATE heroes (slop-engine-loop, money-trail-coins, old-creation-cost-pile,
prompt-box-instant, engagement-slot-machine, attention-quality-scale, flood-the-zone-cannon,
blindfold-sorter-robot) + 7 FRESH browse bases (dark-machine-hall reused only at the engine beats
4.1/4.8/4.9) + reuse `slop-clone.png` (S3) + 9 library poses. CSS: STEP chips, loop-ring HUD, $$$->$0
counter, engagement chips, struck GOOD/QUALITY, "ATTENTION not quality", VIRAL card, 1-vs-1000,
CAN'T TELL + ✓SERVED, loop labels, "THE MACHINE FEEDS ITSELF", verdict stamps, sludge overflow. NO crutch
base. Full per-scene detail in the section file (source of truth).

### Section 5: It Already Got Out (generate-forward; the flood motif RETURNS and peaks)

Section goal: show the slop spread is wide and already in serious places - music, books (deadly), kids'
videos, your job - then land the dry "it's everywhere" payoff. Duration 53.7s (audio 53.739s; scene times
ESTIMATED - NO word-timings JSON yet, render must generate + re-pin). 7 scenes. The GREY-SLUDGE FLOOD
returns here as planned (born S1.8): a rising water-line climbs scene by scene; WIT goes from alarmed to
fully drowning at the payoff, holding ONE real photo above the surface. Each domain still gets its own
distinct vivid base + generated hero. Mascot arc: alarmed -> skeptical -> panic -> disgusted -> cringe ->
burnt-out -> drowning.

- 5.1 `0-4.5` "...it got out." - reuse `social-scroll-livingroom-1.jpg` + GEN `slop-bursting-phone` (sludge gushing from a phone); WIT alarmed (`worried_uneasy_wide_eyes`, right); rising sludge line starts.
- 5.2 `4.5-15.5` "Velvet Sundown... 1M listeners... not a single member real." - `music-stage-lights-1.jpg` + GEN `ai-band-uncanny`; CSS music-app card + red `0 REAL MEMBERS`; WIT skeptical (right).
- 5.3 `15.5-26` "AI mushroom guides... can actually kill you." - `forest-floor-mushrooms-1.jpg` + GEN `mushroom-guide-book` + red DANGER skull; WIT panic (`panic_hands_on_cheeks_scream`, left). Real safety warning, played straight.
- 5.4 `26-34.5` "~40% of kids' videos looked like AI slop. 40 out of 100." - `living-room-tv-1.jpg` + CSS kid-thumbnail grid (~40% stamped SLOP) + giant `40%`; WIT disgusted (`annoyed_disgusted_open_frown`, left).
- 5.5 `34.5-39.5` "six-legged horses... teach the alphabet." - reuse `living-room-tv-1.jpg` + GEN `six-legged-horse-cartoon` + red `6 LEGS?!`; WIT cringe (`cringe_uneasy_drool`, right).
- 5.6 `39.5-49.5` "...you got workslopped... ~2 hours to clean up." - `office-desk-inbox-1.jpg` + GEN `workslop-document` + `WORKSLOPPED` stamp + `~2 HOURS`; WIT burnt-out (`exhausted_dead_inside_eye_bags`, right).
- 5.7 `49.5-53.739` "congratulations... your feed, music, kid's tablet, inbox." - reuse `grey-sludge-flood-1.jpg` (motif peak) + WIT drowning (`swimming_underwater_goggles_cap`, center) holding GEN `real-photo-lifeline`; 4 bobbing domain icons.

Section 5 assets: 6 GENERATE (slop-bursting-phone, ai-band-uncanny, mushroom-guide-book,
six-legged-horse-cartoon, workslop-document, real-photo-lifeline) + 4 fresh browse (music-stage-lights,
forest-floor-mushrooms, living-room-tv, office-desk-inbox) + reuse `social-scroll-livingroom-1.jpg` (S1) +
reuse `grey-sludge-flood-1.jpg` (the flood return) + 7 library poses. CSS: rising sludge line, listeners
card + `0 REAL MEMBERS`, DANGER skull, kid-grid + `SLOP` + `40%`, `6 LEGS?!`, `WORKSLOPPED` + `~2 HOURS`,
4 domain icons + `congratulations.`. Full detail in the section file (source of truth).

### Section 6: It's Not AI's Fault (And Not A Plot) (the honest turn; calmer)

Section goal: the fair turn. Not all AI is slop (a doctor's scan, an artist's tool); slop = low effort x
high volume, not the tool. Reject the conspiracy ("dead internet theory") - "it's dumber than that."
Real cause: nobody's in charge, no villain; the money rewards it. Dry payoff: "you cannot arrest an
incentive." Duration 38.9s (audio 38.933s; scene times ESTIMATED - render must generate word-timings +
re-pin). 7 scenes, calmer/balanced. Mascot arc: careful -> doctor -> distinction -> skeptical -> dry reject
-> shrug -> calm point at the culprit.

- 6.1 `0-4` "let me be fair..." - `courtroom-1.jpg` + CSS level scale; WIT careful (`hand_on_cheek_pondering_eyes_closed`, left; substituted - the planned `talking_hand_at_chin_eyes_closed` is in pose.md but not on disk); "let's be fair".
- 6.2 `4-12` "a doctor's scan - not slop. an artist's tool - not slop." - `clinic-scan-room-1.jpg` + WIT as doctor (`doctor_coat_stethoscope_listening`, center-right) + GEN `artist-easel`; green `NOT SLOP` checks.
- 6.3 `12-16.5` "low effort + high volume. not the tool." - `workbench-tools-1.jpg` + CSS `SLOP = LOW EFFORT x HIGH VOLUME`; WIT (`pointing_up_curious_open_mouth`, right).
- 6.4 `16.5-26` "dead internet theory... govt bots control your mind." - reuse `corkboard-redstring-1.jpg` (S2 conspiracy board) + GEN `tinfoil-hat` + CSS `DEAD INTERNET THEORY`/red string; WIT skeptical (`pondering_skeptical_hand_on_chin`, left).
- 6.5 `26-29` "Relax. It's dumber than that." - reuse corkboard (crossed out, big red `X`); WIT deadpan (`unimpressed_smirk_closeup`, center closeup).
- 6.6 `29-35` "nobody's in charge... the money rewards it." - `empty-boardroom-1.jpg` + GEN `empty-villain-throne` (unpressed button) + glowing `$`; WIT shrug (`shrug_both_hands_up_smile`, left).
- 6.7 `35-38.933` "you cannot arrest an incentive." - reuse `dark-spotlight-stage-1.jpg` (S4.5) + GEN `uncuffable-incentive` (gold `$` shrugging off handcuffs); WIT calm point (`proud_explaining_hand_on_chest_hand_on_hip`, center-left).

Section 6 assets: 4 GENERATE (artist-easel, tinfoil-hat, empty-villain-throne, uncuffable-incentive) + 4
fresh browse (courtroom, clinic-scan-room, workbench-tools, empty-boardroom) + reuse
`corkboard-redstring-1.jpg` (S2) + reuse `dark-spotlight-stage-1.jpg` (S4) + 7 library poses. The calmer
"argument" section leans on real bases + CSS graphics + a few key props. CSS: level scale, green
`NOT SLOP` checks, `SLOP = LOW EFFORT x HIGH VOLUME`, `DEAD INTERNET THEORY` + red string, big red `X` +
"it's dumber than that.", `NOBODY IS IN CHARGE`/`NO VILLAIN` + `$`, `YOU CANNOT ARREST AN INCENTIVE`. Full
detail in the section file.

### Section 7: Payoff: Attention In, Garbage Out (the calm payoff; callback-heavy recap)

Section goal: land the insight calmly and hand the viewer the tells. Recap (works as built -> pays for
attention -> slop wins), state "Attention in. Garbage out.", reframe ("not broken - working perfectly -
that's the problem"), give the tells (six fingers / too-perfect photo / too-good story), empower (can't stop
the flood, but stop being fooled; pay attention on purpose -> you win), sign off "keep your eyes open."
Duration 43.4s (audio 43.413s; scene times ESTIMATED - render must generate word-timings + re-pin). 7
scenes, calmer than the S5 flood. Deliberately CALLBACK-heavy (it's a recap): the S4 engine winds down; the
tells reuse earlier slop artifacts. Mascot arc: asking -> calm answer -> takeaway -> dry irony -> presenting
the tells -> empowering -> calm direct sign-off (eyes open).

- 7.1 `0-4` "why is the internet full of garbage now?" - reuse `dark-machine-hall-1.jpg` + reuse `slop-engine-loop` (winding down); WIT asking (`pointing_up_curious_open_mouth`, left); `WHY?` (S1.9 callback).
- 7.2 `4-15` "not evil, not a conspiracy... pays for attention... slop wins." - reuse `dark-spotlight-stage-1.jpg` (S4 stage) + GEN `slop-wins-trophy` (slop on a podium w/ an ATTENTION trophy); struck `AI IS EVIL`/`CONSPIRACY`; WIT calm (`eyes_closed_talking_open_palm`, right). (Base swapped from a real award-podium - clean people-free podium photos were all real athletes.)
- 7.3 `15-18` "Attention in. Garbage out." - reuse engine (simplified in->out board) + big kinetic `ATTENTION IN.` / `GARBAGE OUT.`; WIT (`lecturing_finger_raised_eyes_closed`, center-left).
- 7.4 `18-24` "not broken... doing its job perfectly. that's the problem." - reuse engine (humming) + struck `BROKEN` + green `WORKING PERFECTLY ✓`; WIT deadpan (right).
- 7.5 `24-34` "now you know the tells: six fingers / too perfect / too good to be true." - `evidence-desk-1.jpg` + reuse `ai-extra-fingers-hand` (S1) + reuse `ai-influencer-perfect` (S3) + CSS headline; `THE TELLS` checklist; WIT presenting (`presenting_screen_announcing_open_mouth`, left).
- 7.6 `34-41` "can't stop the flood, but stop being fooled... pay attention on purpose -> you win." - `bright-window-calm-1.jpg` + receding sludge; WIT calm/clear-eyed (`proud_explaining_hand_on_chest_hand_on_hip`, center); glasses glint.
- 7.7 `41-43.413` "we'll keep explaining the weird machine. you keep your eyes open." - reuse `bright-window-calm-1.jpg` + tiny reuse `slop-engine-loop` tag; WIT calm-direct (`pointing_at_viewer_serious_accusing`, center); big `keep your eyes open.`

Section 7 assets: 1 GENERATE (slop-wins-trophy) + 2 fresh browse (evidence-desk, bright-window-calm) +
reuse `dark-spotlight-stage-1.jpg` (S4 stage, 7.2) + reuse `dark-machine-hall-1.jpg` + `slop-engine-loop.png` (S4 engine recap) +
`ai-extra-fingers-hand.png` (S1) + `ai-influencer-perfect.png` (S3) + 7 library poses. As a recap, it is
intentionally callback-heavy. CSS: `WHY?`, struck `AI IS EVIL`/`CONSPIRACY` + `slop wins`, big
`ATTENTION IN.`/`GARBAGE OUT.`, struck `BROKEN` + green `WORKING PERFECTLY ✓`, `THE TELLS` checklist,
empowerment text + glasses glint, `keep your eyes open.`. Full detail in the section file.

### Section 8: Outro: Like, Share, Subscribe (short outro end-card; added 2026-06-29)

Section goal: a short, straightforward like/share/subscribe close + a calm "see you next time" sign-off,
continuing the calm S7 mood. Duration 7.957s (scene times ESTIMATED - no word-timings yet). 2 scenes,
intentionally LIGHT (no new generate/browse assets). Mascot arc: warm offering -> chill sign-off.

- 8.1 `0-6.0` "That's it... like / share / subscribe..." - reuse `bright-window-calm-1.jpg` (S7 base) + tiny reuse `slop-engine-loop` corner callback; WIT warm (`cheerful_presenting_fullbody`, center-left); CSS `LIKE`/`SHARE`/`SUBSCRIBE` buttons pop one per word.
- 8.2 `6.0-7.957` "See you in the next one." - reuse `bright-window-calm-1.jpg` (continuation); WIT chill sign-off (`peace_sign_calm_open_mouth`, center); CSS `"see you in the next one"` + optional `Why It Works` wordmark.

Section 8 assets: 0 generate + 0 new browse. Reuse `bright-window-calm-1.jpg` (S7, both scenes - justified
continuity) + tiny `slop-engine-loop.png` (S4 callback) + 2 library poses (`cheerful_presenting_fullbody`,
`peace_sign_calm_open_mouth`). Render-CSS: the LIKE/SHARE/SUBSCRIBE buttons (thumb/arrow/bell, NOT emoji
glyphs), `"if this helped..."`, `"see you in the next one"`, optional `Why It Works` wordmark. Full detail
in the section file.

## Cross-Section Continuity

- Reused assets (filename -> scenes): `shrimp-jesus.jpg` -> 1.5, 1.8; `ai-extra-fingers-hand.png` -> 1.8; `grey-sludge-flood-1.jpg` -> 1.8, 1.9, 2.1, 2.5, 2.8 (the flood motif in S1-S2 ONLY; deliberately NOT used in S3 after the overuse note). S3 v2 has its own motif `slop-machine.png` -> 3.1, 3.8; `studio-backdrop-1.jpg` -> 3.2, 3.3; `factory-interior-1.jpg` -> 3.1, 3.8. S4 motif `slop-engine-loop.png` -> 4.1, 4.8, 4.9 and `dark-machine-hall-1.jpg` -> 4.1, 4.8, 4.9 (within-section engine callback: dormant -> roaring -> labeled). Cross-section: `slop-clone.png` (S3 3.7) -> 4.6 (the identical "fake post", kept consistent). The S4 verdict (4.9) ends with a grey sludge overflow that ties back to the S1-S2 flood motif and sets up Section 5.
- S5 reuse: `grey-sludge-flood-1.jpg` returns (the flood motif's planned comeback) as a rising line 5.1-5.6 and the full peak at 5.7; `social-scroll-livingroom-1.jpg` (S1) -> 5.1; `living-room-tv-1.jpg` -> 5.4, 5.5.
- S6 reuse: `corkboard-redstring-1.jpg` (S2 conspiracy board) -> 6.4, 6.5; `dark-spotlight-stage-1.jpg` (S4.5) -> 6.7.
- S7 reuse (callback-heavy recap): `slop-engine-loop.png` + `dark-machine-hall-1.jpg` (S4 engine) -> 7.1, 7.3, 7.4, 7.7; the tells reuse `ai-extra-fingers-hand.png` (S1) + `ai-influencer-perfect.png` (S3) -> 7.5; `bright-window-calm-1.jpg` -> 7.6, 7.7. `WHY?` echoes S1.9.
- S8 reuse (light outro): `bright-window-calm-1.jpg` (S7) -> 8.1, 8.2 (continues the calm close); tiny `slop-engine-loop.png` (S4) corner callback -> 8.1. The like/share/subscribe buttons are render-CSS.
- Motif discipline (owner-directed 2026-06-28): do NOT reuse one base across many sections as a crutch. Each section earns its own bold imagery; the flood/sludge stays an S1-S2 device, not a universal background.
- Recurring motif / callback scenes: the grey-sludge flood (born 1.8) should return for Section 5 ("It
  Already Got Out") and the Section 7 payoff; WIT's glowing phone recurs through the feed scenes.
- Mascot emotional arc across the video (planned): hook = suspicion -> drowning -> curiosity; body should
  build to unimpressed-at-the-machine (S4), drowning again (S5), pointing-at-the-culprit (S6), tired-but-clear (S7).

## Stale / Regeneration Notes

- All 8 sections are now planned (Sections 5-7 planned 2026-06-28 generate-forward; Section 8 outro added 2026-06-29 after the owner added a like/share/subscribe CTA to the script).
- Sections 5, 6, 7 now NEED `visual-implement` (create the generate heroes + source the fresh browse bases; reuse the cross-section assets noted in Cross-Section Continuity), then `render`. No S5/6/7 downstream exists yet, so nothing is stale - they are not-yet-built. All three have ESTIMATED scene times (no `section-0X-word-timings.json`); render must generate word-timings and re-pin every cue. New browse bases to source: S5 (music-stage-lights, forest-floor-mushrooms, living-room-tv, office-desk-inbox); S6 (courtroom, clinic-scan-room, workbench-tools, empty-boardroom); S7 (award-podium, evidence-desk, bright-window-calm).
- Section 4 (planned 2026-06-28, generate-forward): now NEEDS `visual-implement section 4` (create the 8 generate heroes + source the 7 fresh browse bases; reuse `slop-clone.png`), then `render section 4`. No S4 downstream exists yet, so nothing is stale - it is simply not-yet-built. S4 scene times are ESTIMATED (no `section-04-word-timings.json`); render must generate word-timings and re-pin every cue.
- STALE (S3 v2 rebuild 2026-06-28): the existing Section 3 render (`section-previews/section-03-what-slop-actually-is/`) is now STALE - rerun `visual-implement section 3` then `render section 3`. The S3 v1 browse assets `gallery-wall-1.jpg`, `ai-face-does-not-exist.png`, `hourglass-time-1.jpg`, `holiday-bokeh-red-1.jpg` are now ORPHANED (v2 does not use them); remove only on explicit request.
- Section 2 downstream not yet created: its new assets (`assets/`) and its render (`section-previews/section-02-*/`). Run `visual-implement section 2` then `render section 2`.
- Downstream for Section 1 (not yet created): implemented assets in `assets/`, `05-production-board.md`,
  `section-previews/section-01-hook/`, `hyperframes/`, `renders/`, `06-review.md`, `07-upload.md`,
  `08-self-learning.md`. None exist yet, so nothing is stale.

## Next Step Boundary

Next workflow step: `visual-implement` (creates the assets named here for each planned section), then `render`. Section 4's assets are already implemented; Sections 5, 6, 7 are newly planned and need `visual-implement` next.
