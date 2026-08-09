# HumanPrice Cast Identity

Read this file before building a cast or character reference prompt.

## Cast size and roles

Use 2 to 6 cast entries per video. Every cast member must perform a narrative job such
as participant, worker, seller, platform, expert, partner, or social observer.

Do not invent characters merely to increase variety. Institutions may be represented by
a human operator, a building, or a system object when that is clearer.

## Recurring protagonist

`@YOU` is HumanPrice's recurring audience surrogate. Use the reference image at
`brand/PROTAGONIST.jpeg` when it exists. If it does not exist, the cast skill must write
the full creation prompt below and clearly instruct the user to generate and save that
asset before generating scene images.

Identity lock for `@YOU`:

- neutral adult with a large round warm-cream head and bold charcoal outline;
- two charcoal dot eyes, mobile brows, and a simple expressive mouth;
- short asymmetrical charcoal hair with one recognizable forward swoop;
- olive overshirt `#6F7D3C`, terracotta undershirt `#C86B3C`, charcoal trousers;
- simplified hands with readable splayed fingers;
- curious, financially alert, and human, never smug or childish;
- no fixed ethnicity and no exaggerated gender coding.

The face, hair silhouette, outfit colors, and body proportions must remain unchanged
across all projects.

## Supporting characters

Differentiate supporting characters through silhouette, age range, hair, clothing shape,
and one story-relevant prop. Avoid stereotypes. A job or economic role is not a costume.

Each character entry needs:

- stable handle in `@UPPER_SNAKE_CASE`;
- narrative role and relationship to `@YOU`;
- full identity block;
- front, three-quarter, side, and back views;
- six expressions relevant to the script;
- three gesture or action poses;
- one scale lineup instruction when multiple characters share frames.

## Reference sheet constraints

- One neutral background and one consistent scale.
- Full body visible in turnaround views.
- No speech bubbles, captions, labels, logos, watermarks, or decorative text.
- No duplicate limbs, cropped hands, hidden feet, or outfit changes.
- Do not combine unrelated characters on one sheet unless it is a scale lineup.

Append the exact style and generation strings from `visual-style.md` to every prompt.
