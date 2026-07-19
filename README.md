# One Man Band 🎸🎹🥁

A personal project to become a skilled live-looping one man band using **Loopy Pro** on iPhone, a custom electric guitar with an attached **Akai MPK Mini 3**, and a **UGM192** audio interface (mic + guitar).

This repo treats the musical journey like a software project: phased milestones, definitions of done, PR-based reviews, and an audio journal to track progress.

## Vision

**Long-term goal:** Perform ambient/downbeat live sets with improvised journeys — slow atmospheric parts building into punchier sections (tribal progressive trance, melodic techno) and back down. Full freedom to improvise; the audience goes on a ride with ups and downs.

**Reference for phase 1:** Stringscapes-style western ambient — slow, sparse, repetitive layered guitar with atmosphere.

## Rig (frozen — see `gear/RIG.md`)

- Custom electric guitar with mounted Akai MPK Mini 3 (drum pads, endless knobs, keys)
- UGM192 USB3 interface: input 1 = mic, input 2 = guitar
- iPhone 15 Pro running Loopy Pro (powers interface + Akai)
- MIDI instruments: organs, drum kits, custom one-shots (e.g. guitar-body hits as kicks)

Changes to the rig or app setup only happen via PR (see workflow below). This is the anti-rabbit-hole mechanism.

## Roadmap

| Phase | Goal | Definition of Done |
|-------|------|--------------------|
| 1 | Reproduce one Stringscapes-style song with stock Loopy Pro tools (guitar + voice only) | Played live, hands only, 3 clean runs in a row; recording committed |
| 2 | Arrangement control: unbuild/rebuild the same song with mutes, fades, groups | 5-minute version with a clear arc, no dead air |
| 3 | MIDI layer: one drum kit + one keys instrument via Akai | Ambient piece that morphs into downbeat and back |
| 4 | Journey set: chain 2–3 pieces with improvised transitions | 15+ min continuous set, recorded, self-reviewed |
| 5+ | Punchier genres, stage prep, first live performance | TBD when phase 4 ships |

Only the current phase is "in sprint." Everything else goes to the idea parking lot.

## Repo structure

```
.
├── README.md
├── CLAUDE.md              # Coaching instructions for Claude / Claude Code
├── gear/
│   └── RIG.md             # Frozen hardware + app config, MIDI mappings
├── tracks/
│   └── <track-name>/
│       ├── NOTES.md       # Chords, structure, loop layout, tempo, lessons learned
│       └── audio/         # Takes: YYYY-MM-DD_take-NN.m4a
├── journal/
│   └── YYYY-MM-DD.md      # Practice log entries
├── ideas/
│   └── PARKING_LOT.md     # Every shiny idea goes here instead of derailing the sprint
├── setlists/
│   └── <set-name>.md      # Ordered pieces, energy arc, transition notes
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
```

## Workflow

### Branches & Pull Requests

- `main` holds only **validated progress**: reviewed increments, approved rig changes, committed takes.
- Each **increment** gets a short-lived branch (`agm-transcription`, `agm-loop-layout`, …) — not one branch per phase. A phase spans several such branches and is tracked as a **GitHub milestone**.
- Rig/app changes (new AUv3, remapped knob, new Loopy Pro layout) get their own branch + PR with a written justification. If you can't justify it in 3 sentences, it goes to the parking lot instead.
- **Merging a PR ships one increment.** The review (by you + Claude) checks that increment's scope, listens to any attached take, and captures lessons learned. A **phase** is done only when its milestone's Definition of Done is met — the final performance PR closes it.

### Practice journal

After each session, add `journal/YYYY-MM-DD.md`:

```markdown
## Session YYYY-MM-DD (45 min)
**Worked on:** phase 1, loop timing on layer 2
**Win:** first clean 4-bar overdub without count-in
**Struggle:** melody comes in late; reverb tail masks the downbeat
**Next session:** metronome only in headphones, not in the loop
**Rabbit holes resisted:** almost bought a shimmer reverb AUv3 → parked
```

### Audio

- Commit short takes (< ~10 MB) directly; use **Git LFS** for longer recordings (`git lfs track "*.m4a" "*.wav"`).
- Naming: `YYYY-MM-DD_take-NN.m4a` inside the track's `audio/` folder.
- Tag releases when a piece is performable: `git tag track/dusty-trails-v1`.

### Issues as backlog

- Song ideas, gear ideas, and "I should learn X" thoughts go to `ideas/PARKING_LOT.md` first — don't open an issue for every stray idea.
- Promote a parked idea to an **issue** only when it's real, actionable work (labeled: `song-idea`, `technique`, `gear`, `loopy-pro`, `phase-N`).
- Sprint = issues assigned to the current phase milestone. Everything else waits.

## Rules of the road

1. **One new tool per phase.** No AUv3 shopping mid-phase.
2. **Finish before you optimize.** Ship the milestone, then improve.
3. **Park, don't chase.** Shiny ideas go to `ideas/PARKING_LOT.md` or an issue within 60 seconds.
4. **Play days are sacred.** One session per week is free experimentation, no goals, no guilt — findings can become issues afterwards.
5. **Record everything reviewable.** If it's not committed, it didn't happen.
