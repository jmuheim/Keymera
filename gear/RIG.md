# RIG.md — Frozen hardware & control architecture

Changes to this file only via rig-change PR (justification ≤3 sentences).

## Core principle: widgets over hardware

All musical actions are bound to **Loopy Pro virtual widgets**. Physical controllers are MIDI-learned / key-bound to widgets, never to actions directly. Workflows must work identically across all profiles.

```
[Akai pads/knobs] ──MIDI──┐
[Numpad keys] ──HID keys──┼──> [Widget layout] ──> [Loopy Pro actions]
[BT500S switches] ──BLE───┘
```

## Shared components (always in the backpack)

- iPhone 15 Pro — Loopy Pro host, powers USB chain
- UGM192 USB3 interface — input 1: mic, input 2: guitar/instrument
- AirTurn BT500S-2 — Bluetooth MIDI foot controller (hands-free)

## Profile A — Full rig (🚧 in build — not yet available)

- Custom electric guitar (**Thomann DIY starter kit**, build in progress — see `build/`) with mounted **Akai MPK Mini 3** (keys, drum pads, endless knobs)
- MIDI instruments: organs, drum kits, custom one-shots (guitar-body hits as kicks)

## Profile B — Acoustic / light (✅ ACTIVE — starting rig for phase 1+)

- **Taylor GS Mini** with ES2 preamp → UGM192 instrument input
- **Numpad** (USB HID keyboard) → Loopy Pro key bindings on the same widgets
- ⚠️ TODO: 5-min test that numpad works alongside UGM192 in the USB setup

## Constraints

- No car; public transport only → everything lightweight, backpack-sized, battery/bus-powered.

## Foot controller mapping (starter — do not expand until stage need proven)

| Switch | Press | Double-press | Hold |
|--------|-------|--------------|------|
| 1 | Record/overdub/play selected tile | — | Clear tile |
| 2 | Select next tile | — | Mute/unmute group |

Note: BLE MIDI has small latency/jitter → always use quantized recording; don't use foot switches for timed musical triggering.

## Widget layout v1 (phase 1 scope — max 6 widgets)

1–4. Loop tiles ×4
5. Record/overdub (bound to: Akai pad, numpad key, BT500S switch 1)
6. Mute all (bound to: Akai pad, numpad key, BT500S switch 2 hold)

Layout grows only when the current phase demands it.
