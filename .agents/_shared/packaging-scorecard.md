# Packaging Scorecard

Classification: `Core`

Scope: `CHANNEL_WIDE`

Purpose:
decide whether a future `Why It Works` title-thumbnail pair is strong enough before scripting or production.

This is a reusable gate. It does not score any existing video by itself.

## Pass Threshold

Score out of `100`.

```text
85-100: Strong. Ready for scripting or mockup testing.
75-84: Usable, but improve one weak area first.
60-74: Not ready. Iterate the title-thumbnail pair.
0-59: Reject. Start again from the contradiction.
```

Hard fail rules override the score.

## Score Table

| Area | Points | What To Check |
| --- | ---: | --- |
| 1-second clarity | 15 | A stranger can identify the broad topic or situation quickly. |
| Curiosity gap | 20 | The viewer still has a question after understanding the image. |
| Visual contradiction | 15 | The image shows something normal behaving in a suspicious, unfair, or weird way. |
| WIT emotion | 10 | WIT has one obvious emotion that fits the topic. |
| Title strength | 15 | The title is specific, simple, and system-focused. |
| Title-thumbnail contrast | 10 | The title and thumbnail support each other without repeating the same words. |
| First 10 seconds promise | 10 | The hook can pay off the thumbnail immediately. |
| Learner-friendly clarity | 5 | The title and label are clear for intermediate English learners. |

Total: `100`

## Detailed Rubric

### 1. 1-Second Clarity - 15

Score high if:

- one dominant object is obvious
- the label is readable at mobile size
- WIT does not block the main object
- the scene has a clear foreground and background

Score low if:

- the viewer must inspect details to understand the image
- the thumbnail has multiple equal objects
- the text is too small or too long
- the image looks like a presentation slide

### 2. Curiosity Gap - 20

Score high if:

- the image creates a question
- the normal object feels suspicious
- the viewer can sense a hidden cost, trap, downgrade, or unfair rule
- the title makes the larger explanation feel worth clicking

Score low if:

- the image fully explains itself
- the title gives away the entire point
- the concept is merely `topic + icon + label`

### 3. Visual Contradiction - 15

Score high if:

- the contradiction is visible without reading the title
- the object appears to lie, leak, trap, shrink, charge, or pressure
- the image makes a normal system feel weird

Score low if:

- the contradiction only exists in the script idea
- the image shows a clean symbol instead of a situation
- the concept uses a generic lock, warning sign, or money icon with no twist

### 4. WIT Emotion - 10

Score high if:

- WIT reads as suspicious, betrayed, trapped, panicked, confused, or defeated
- the emotion is clear at small size
- WIT reacts to the object, not away from it
- the pose supports the click question

Score low if:

- WIT is neutral
- WIT looks like a presenter
- WIT emotion conflicts with the title
- WIT is too small to read

### 5. Title Strength - 15

Score high if:

- the title names a hidden system
- the wording is simple but not generic
- the title sounds like `Why It Works`, not generic advice content
- the title creates a clear promise the video can deliver

Score low if:

- the title sounds like a blog article
- the title is vague advice
- the title uses jargon before common words
- the title needs the thumbnail to make sense

### 6. Title-Thumbnail Contrast - 10

Score high if:

- the title explains the logic while the thumbnail shows the weird situation
- the thumbnail label is not just a shorter version of the title
- each part adds new information

Score low if:

- title and thumbnail repeat the same phrase
- both title and thumbnail explain the same point
- one element becomes unnecessary

### 7. First 10 Seconds Promise - 10

Score high if:

- the hook can immediately show the thumbnail contradiction
- the first line answers why the thumbnail looked weird
- the opening uses the same object, motif, or emotional situation

Score low if:

- the hook starts with a definition
- the thumbnail promise appears late
- the package is more exciting than the actual opening

### 8. Learner-Friendly Clarity - 5

Score high if:

- the title uses common words
- the thumbnail label is short and concrete
- the concept works without advanced cultural knowledge

Score low if:

- the title depends on dense idiom or slang
- the label is abstract
- the joke hides the meaning

## Hard Fails

A package fails even with a high score if:

- it makes a fake claim
- it uses rage bait
- it copies a specific creator's thumbnail too closely
- it depends on copyrighted brand logos without a clear safe-use reason
- the thumbnail text is unreadable on mobile
- WIT is neutral or decorative only
- the first `10` seconds cannot pay off the promise

## Review Checklist

Use this checklist after scoring:

```text
[ ] One dominant object
[ ] One visible contradiction
[ ] One clear WIT emotion
[ ] One label, 1-3 words
[ ] Title and label do not repeat each other
[ ] Topic clear in 1 second
[ ] Question remains after 1 second
[ ] Hook can pay off the image by second 10
[ ] Mobile-size test passes
[ ] No fake claim, rage bait, logo clutter, or copied design
```

## Decision Note Template

For future per-video packaging, record the score like this:

```text
Packaging score: __ / 100

Pass status:
Strong / Usable after fixes / Not ready / Reject

Strongest part:
_____

Weakest part:
_____

Required fix before scripting:
_____
```

