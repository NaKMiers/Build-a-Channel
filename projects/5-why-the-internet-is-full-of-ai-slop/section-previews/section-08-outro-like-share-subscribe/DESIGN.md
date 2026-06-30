# Section 8 Design - Outro: Like, Share, Subscribe (v2 gamified CTA)

- Composition: `Section08Outro`, 1920x1080, 7.957s.
- Big idea: a LOUD, gamified end-card. Instead of static buttons, the screen shows a fake YouTube video
  page and a mouse cursor that flies in and actually CLICKS the like and subscribe buttons - they boing,
  flip to "Liked" / "Subscribed", the bell rings, and confetti pops. It is deliberately over-the-top and
  superficial-fun: a direct, playful "do the thing" call to the viewer.
- Single continuous scene (no hard cut) so the YouTube card stays on screen the whole time and holds its
  liked + subscribed state into the sign-off.
- Choreography is pinned to the real word timings: the cursor clicks LIKE on "like the video" (2.24),
  SHARE on "share it" (3.14), and SUBSCRIBE on "subscribe" (5.22). A gold glow ring pulses on the
  subscribe button in the gap before the click to pull the eye.
- The card is a parody YouTube UI built in CSS/SVG (no screen-grab): red play-logo + "WhyTube" wordmark,
  a video thumbnail with our "WHY IT WORKS" title card and a realistic "5:00" duration, the channel row
  (the REAL WIT channel avatar, "Why It Works", a non-numeric channel line), the red SUBSCRIBE button,
  and a LIKE / SHARE action row. On click the buttons cross-fade between states (red SUBSCRIBE -> grey
  SUBSCRIBED + bell; white LIKE -> blue Liked).
- Honest, not inflated: the channel is small, so there is NO fake subscriber count. The line reads
  "Subscribe for more" and flips to "Welcome to the channel!" on subscribe, with a floating green
  "Thanks!" and a humble like tick (247 -> 248) - celebratory without claiming numbers it does not have.
- Mascot: cheerful enthusiastic-point WIT presenting the card during the CTA, cross-fading to a calm
  peace-sign WIT for the sign-off. On the far left, clear of the card.
- Motion: this is the one section where loud kinetic motion is the point - the cursor moves, the buttons
  boing/wiggle, confetti bursts. Everything settles by the "see you in the next one." sign-off so the
  outro still lands calm.
- Type: PatrickHand handwritten captions ("if this helped...", "see you in the next one.") + Segoe UI
  black for the card UI, button labels, and the WHY IT WORKS wordmark.
- Colors: YouTube red for the logo + SUBSCRIBE, `--ytblue` for the Liked state, `--green` for the toast
  and "+1", `--gold` for the avatar / glow ring / wordmark, `--cream` for the handwritten captions.
- Icons (filled thumbs-up / share-arrow / notification bell) and the cursor are inline SVG, not emoji -
  color emoji do not render in the snapshot Chromium.
- Safety: parody UI with our own branding (WhyTube, Why It Works) - no real YouTube screen-grab, no real
  channel, no real person; nothing else to flag.
