# scene-images - memory

Validate before any rename. A mismatched count, non-contiguous numbered sequence, existing timestamp file, or root-level collision means no rename occurs.

Never use directory listing order. Map `1_2k.jpg` through `N_2k.jpg` to prompt timestamps in order only after the range check passes.

Move only timestamp-named JPG files. Refuse to move when a range has another entry, two folders have the same name, or `scenes/` already has that name.

The completed `scenes/` folder must have exactly one timestamp-named JPG per `image-prompts.md` timestamp, with no extras or duplicate timestamps.
