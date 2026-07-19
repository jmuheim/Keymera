#!/usr/bin/env python3
"""Second-opinion audio analysis for committed takes (ear first, algorithm second).

Usage:
    .venv/bin/python tools/analyze_take.py <audio-file> [--bpm 62] [--chords D,F,C,G]

Reports duration, tempo hypotheses, onset timing tightness, per-bar chroma
(approximate root guess), and a global key estimate. Chord/root detection is
approximate — treat as a second opinion, never ground truth.
"""
import argparse
import numpy as np
import librosa

PC = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path')
    ap.add_argument('--bpm', type=float, default=62.0, help='target BPM (for bar-count guess)')
    ap.add_argument('--chords', default='D,F,C,G', help='expected chord roots, comma-separated')
    args = ap.parse_args()
    expected = [c.strip() for c in args.chords.split(',') if c.strip()]

    y, sr = librosa.load(args.path, mono=True, sr=None)
    dur = librosa.get_duration(y=y, sr=sr)
    print(f"file          : {args.path.split('/')[-1]}")
    print(f"sample rate   : {sr} Hz")
    print(f"duration      : {dur:.2f} s")

    # --- Tempo ---
    tempo = float(np.atleast_1d(librosa.beat.beat_track(y=y, sr=sr)[0])[0])
    print("\n== TEMPO ==")
    print(f"librosa tempo estimate : {tempo:.1f} BPM")
    print("implied BPM if the take is exactly N bars of 4/4:")
    for nbars in (4, 8, 12, 16):
        print(f"  {nbars:2d} bars -> {nbars * 4 / dur * 60:6.1f} BPM   (bar length {dur / nbars:.2f} s)")

    # --- Onsets / timing tightness ---
    print("\n== ONSETS (strum attacks) ==")
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, units='time', backtrack=True)
    print(f"detected onsets: {len(onsets)}")
    print("times (s): " + ", ".join(f"{t:.2f}" for t in onsets))
    if len(onsets) >= 2:
        iois = np.diff(onsets)
        print("inter-onset intervals (s): " + ", ".join(f"{d:.2f}" for d in iois))
        print(f"IOI mean {iois.mean():.2f}s, std {iois.std():.3f}s  "
              f"(std/mean = {iois.std() / iois.mean() * 100:.1f}% -> lower = tighter)")

    # --- Per-bar chroma -> likely root (bar count closest to target BPM) ---
    print("\n== CHORD / ROOT (chroma, second opinion only) ==")
    nbars = min((4, 8, 12, 16), key=lambda n: abs((n * 4 / dur * 60) - args.bpm))
    print(f"assuming {nbars} bars (implied {nbars * 4 / dur * 60:.1f} BPM, closest to target {args.bpm:.0f})")
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    frames = chroma.shape[1]
    for b in range(nbars):
        lo, hi = int(frames * b / nbars), int(frames * (b + 1) / nbars)
        seg = chroma[:, lo:hi].mean(axis=1)
        top = np.argsort(seg)[::-1][:3]
        exp = expected[b % len(expected)] if expected else '?'
        print(f"  bar {b + 1} (slot {b % len(expected) + 1 if expected else b + 1}, expected {exp}): "
              f"top -> {', '.join(f'{PC[t]}({seg[t]:.2f})' for t in top)}")

    # --- Global key (Krumhansl-Schmuckler) ---
    print("\n== KEY (global) ==")
    maj = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
    minr = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
    cmean = chroma.mean(axis=1)

    def best(profile):
        cors = [np.corrcoef(np.roll(profile, k), cmean)[0, 1] for k in range(12)]
        k = int(np.argmax(cors))
        return PC[k], cors[k]

    mk, mc = best(maj)
    nk, nc = best(minr)
    print(f"best major: {mk} major (r={mc:.2f})")
    print(f"best minor: {nk} minor (r={nc:.2f})")


if __name__ == '__main__':
    main()
