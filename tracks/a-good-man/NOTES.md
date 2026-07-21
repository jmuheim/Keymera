# A Good Man (Stringscapes) — phase 1 reference

## My transcription (ear first, before any analysis)

- Tempo (guessed BPM): around 50
- Key: don't know how to do that
- Chords / progression: seems to be D F C G, but I'm not sure whether a non-standard tuning is used, as the D seems to have more bass than usual
- Layers I hear (list, in order of entry):
    - Simple, repeating strum+picking: each chord is strummed once, then picked with a simple, more or less repeating pattern
- Song form / arc: don't know what that means

## Verified (Claude analysis)

- Tempo: **~62 BPM** (measured). One chord per bar → loop is a clean **4-bar cycle (~15s)**.
- Key: home is **D** (song starts and ends on D). Note-finder's "G major" is just the relative — same white notes. Feel: **D Dorian / D-minor modal**.
- Chords: **D → F → C → G**, repeating — confirms the ear-first guess. Voicings are mostly **power-chord / sus** shapes (D5, Gsus4, Gsus2, some Dm), not clean triads → that's the open/ambient sound.
- Tuning: real energy at **72.7 Hz (D2)**, below standard low E (82 Hz) → low string detuned to D (**Drop D / DADGAD**). Whole track ~20 cents flat (A≈435 Hz). Confirms the ear-guess that the D carried unusual bass.
- Song form / arc: intro → establish D–F–C–G loop → develop → **quiet dip ~5:20** → **rebuild to peak ~7:30–8:00** → resolve home on D and thin out.
- Notes on discrepancies: only real miss was tempo (guessed 50, actual ~62 — sparse music feels slower than it clocks). Chords, tonal center, and the drop-D bass were all confirmed by ear first.

## My loop layout in Loopy Pro

| Tile | Content | Bars | Notes |
|------|---------|------|-------|
| 1 | Guitar bed — D → F → C → G, one strum per bar, let ring | 4 | ~62 BPM, standard tuning, thumb-wrapped F |
| 2 | Sparse lead line over the bed — played by ear, not tabbed | 4 | Reference: `2026-07-21_lead-over-bed.mp3` |
| 3 | *(open — later layer)* | | |
| 4 | *(open — later layer)* | | |

## Takes

See `audio/` — naming: YYYY-MM-DD_short-description.mp3

- `2026-07-19_bed-loop-d-f-c-g.mp3` — first recorded loop: the 4-bar D–F–C–G guitar bed. Solid first pass.
- `2026-07-19_lead-idea-sketch.mp3` — solo sketch of the lead line (2-bar phrase, no bed underneath).
- `2026-07-21_lead-over-bed.mp3` — the lead recorded over the bed (issue #8 deliverable).

## Lessons learned

- Reproduction plan: **standard tuning** (Drop D parked — new technique), **relaxed slow tempo**, 4-bar **D–F–C–G** loop, one chord per bar. Goal is chords + atmosphere, not a 1:1 copy.
- Ear beat the algorithm: chords, tonal center (D), and the detuned low D were all correctly heard before analysis. Only tempo was off (feels slower than it clocks).
- Voicing choice (2026-07-19): **F played thumb-wrapped** (low-E fretted with the thumb, high E muted) gives a strong low-F root that fits the ambient bass. In standard tuning the **D chord's root sits higher** (open D string, ~D3) than F/C/G — exactly why the original used Drop D. Kept as a gentle "lift" home for now; Drop D stays parked.
