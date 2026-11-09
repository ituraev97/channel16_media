#!/usr/bin/env python3
"""Little Hushaby lullaby synthesizer (numpy, no samples, no third-party audio).
Builds a stereo WAV from a plan JSON:
  {"seconds": 720, "key_shifts": [...], "passes": [{"tune":"brahms","inst":"musicbox","shift":0,"tempo":74}, ...],
   "pad": true, "noise": {"kind":"none|pink|brown|womb|shush|rain", "db": -34}, "seed": 1, "lufs": -18}
Instruments: musicbox, celesta, harp, piano. Tunes: see TUNES (public domain melodies only).
usage: synth.py plan.json out.wav
"""
import json, sys, math
import numpy as np
from scipy.signal import fftconvolve, butter, sosfilt

SR = 44100

# ---- public-domain melodies: (midi note or None for rest, beats); chords: list of (chord root name, beats)
C4 = 60
N = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
def m(s, oct=4):
    """'G4 1.5' style tokens -> list of (midi, beats)."""
    out = []
    for tok in s.split(","):
        tok = tok.strip()
        if not tok: continue
        n, b = tok.split()
        if n == "r": out.append((None, float(b))); continue
        name, o = n[:-1], int(n[-1])
        acc = 1 if "#" in name else (-1 if name.endswith("b") and len(name) > 1 else 0)
        out.append((12 * (o + 1) + N[name[0]] + acc, float(b)))
    return out

CHORD = {"C": [0, 4, 7], "F": [5, 9, 12], "G": [7, 11, 14], "G7": [7, 11, 14, 17], "Am": [9, 12, 16], "Dm": [2, 5, 9], "Em": [4, 7, 11]}

TUNES = {
    # Brahms, Wiegenlied Op. 49 No. 4 (1868) — public domain. 3/4, pickup of 1 beat (two eighths).
    "brahms": dict(meter=3, pickup=1.0, mel=m("""E4 .5, E4 .5,
        G4 1.5, E4 .5, E4 1, G4 2, E4 .5, G4 .5, C5 1, B4 1.5, A4 .5, A4 1, G4 1, D4 .5, E4 .5,
        F4 1, D4 1, D4 .5, E4 .5, F4 2, D4 .5, F4 .5, B4 .5, A4 .5, G4 1, B4 1, C5 2, C4 .5, C4 .5,
        C5 2, A4 .5, F4 .5, G4 2, E4 .5, C4 .5, F4 1, G4 1, A4 1, G4 2, C4 .5, C4 .5,
        C5 2, A4 .5, F4 .5, G4 2, E4 .5, C4 .5, F4 1, E4 1, D4 1, C4 3"""),
        chords=[("C", 3), ("C", 3), ("G", 3), ("G", 3), ("G7", 3), ("G7", 3), ("G", 3), ("C", 3),
                ("F", 3), ("C", 3), ("F", 3), ("C", 3), ("F", 3), ("C", 3), ("G7", 3), ("C", 3)]),
    # Twinkle, Twinkle, Little Star (melody 1761, words 1806) — public domain. 4/4.
    "twinkle": dict(meter=4, pickup=0.0, mel=m("""C4 1, C4 1, G4 1, G4 1, A4 1, A4 1, G4 2, F4 1, F4 1, E4 1, E4 1, D4 1, D4 1, C4 2,
        G4 1, G4 1, F4 1, F4 1, E4 1, E4 1, D4 2, G4 1, G4 1, F4 1, F4 1, E4 1, E4 1, D4 2,
        C4 1, C4 1, G4 1, G4 1, A4 1, A4 1, G4 2, F4 1, F4 1, E4 1, E4 1, D4 1, D4 1, C4 2"""),
        chords=[("C", 4), ("F", 2), ("C", 2), ("F", 2), ("C", 2), ("G", 2), ("C", 2),
                ("C", 2), ("F", 2), ("C", 2), ("G", 2), ("C", 2), ("F", 2), ("C", 2), ("G", 2),
                ("C", 4), ("F", 2), ("C", 2), ("F", 2), ("C", 2), ("G", 2), ("C", 2)]),
}

def env_adsr(n, a, d_tau):
    t = np.arange(n) / SR
    e = np.exp(-t / d_tau)
    na = max(1, int(a * SR)); e[:na] *= np.linspace(0, 1, na)
    return e

def voice(inst, midi, dur, vel, rnd):
    f = 440 * 2 ** ((midi - 69) / 12)
    if inst == "musicbox":
        L = 3.2; parts = [(1, 1, 1.4), (2.0, .18, .5), (3.01, .08, .25), (5.43, .12, .12), (8.9, .05, .06)]; a = .002
    elif inst == "celesta":
        L = 2.6; parts = [(1, 1, 1.1), (2, .35, .45), (3, .12, .25), (4, .06, .15)]; a = .003
    elif inst == "harp":
        L = 3.4; parts = [(k, 1 / k ** 1.8, 1.6 / k ** .7) for k in range(1, 9)]; a = .004
    else:  # soft piano
        L = 4.0; parts = [(k * (1 + .0004 * k * k), 1 / k ** 1.6, 2.2 / k ** .8) for k in range(1, 8)]; a = .006
    n = int((max(dur, 0) + L) * SR)
    t = np.arange(n) / SR
    det = 1 + (rnd.random() - .5) * .0016
    y = np.zeros(n)
    for ratio, amp, tau in parts:
        fr = f * ratio * det
        if fr > 15000: continue
        y += amp * np.sin(2 * np.pi * fr * t + rnd.random() * 6.28) * np.exp(-t / tau)
    na = int(a * SR); y[:na] *= np.linspace(0, 1, na)
    # soft release so long tails never click
    y[-int(.3 * SR):] *= np.linspace(1, 0, int(.3 * SR))
    if inst == "piano":  # mellow low-pass
        y = sosfilt(butter(2, 2600, fs=SR, output="sos"), y)
    return vel * y / max(1e-9, np.max(np.abs(y)))

def pad_chord(notes, dur):
    n = int((dur + 1.5) * SR); t = np.arange(n) / SR; y = np.zeros(n)
    for k, nt in enumerate(notes):
        f = 440 * 2 ** ((nt - 69) / 12)
        for d in (-.12, .12):
            y += np.sin(2 * np.pi * f * (1 + d / 100) * t) + .25 * np.sin(4 * np.pi * f * t)
    e = np.minimum(1, t / 1.2) * np.minimum(1, np.maximum(0, (dur + 1.5 - t)) / 1.5)
    return y * e / (len(notes) * 2.5)

def noise(kind, n, rnd):
    w = rnd.standard_normal(n)
    if kind == "white": return w * .3
    spec = np.fft.rfft(w); fr = np.fft.rfftfreq(n, 1 / SR); fr[0] = 1
    if kind in ("pink", "rain"): spec /= np.sqrt(fr)
    else: spec /= fr  # brown, womb, shush base
    y = np.fft.irfft(spec, n); y /= np.max(np.abs(y)) + 1e-9
    if kind == "womb":  # low rumble with a slow 60 bpm pulse
        y = sosfilt(butter(2, 400, fs=SR, output="sos"), y)
        t = np.arange(n) / SR; y *= .65 + .35 * (np.sin(2 * np.pi * 1.0 * t) ** 8)
    if kind == "shush":  # band-limited 'shhh' swelling every ~5 s
        y = sosfilt(butter(2, [1800, 7000], btype="band", fs=SR, output="sos"), w)
        t = np.arange(n) / SR; y *= (.25 + .75 * np.sin(np.pi * t / 5.0) ** 2); y /= np.max(np.abs(y)) + 1e-9
    if kind == "rain":
        y = sosfilt(butter(2, 5000, fs=SR, output="sos"), y); y /= np.max(np.abs(y)) + 1e-9
    return y

def reverb_ir(seconds, rnd):
    n = int(seconds * SR); t = np.arange(n) / SR
    ir = np.stack([rnd.standard_normal(n), rnd.standard_normal(n)]) * np.exp(-t / (seconds / 5.5))
    ir = sosfilt(butter(1, 5500, fs=SR, output="sos"), ir)
    ir[:, :int(.012 * SR)] = 0
    return ir / np.sqrt((ir ** 2).sum(axis=1, keepdims=True))

def lufs_approx(x):
    # K-weighting approximation: high-shelf + high-pass, gated mean square over 400 ms blocks
    hp = butter(2, 60, btype="high", fs=SR, output="sos")
    y = sosfilt(hp, x, axis=-1)
    blk = int(.4 * SR); nb = y.shape[-1] // blk
    if nb == 0: return -70
    ms = (y[:, :nb * blk].reshape(2, nb, blk) ** 2).mean(axis=2).sum(axis=0)
    l = -0.691 + 10 * np.log10(ms + 1e-12)
    g = ms[l > -70]
    if len(g) == 0: return -70
    rel = -0.691 + 10 * np.log10(g.mean()) - 10
    g2 = ms[(l > -70) & (l > rel)]
    return -0.691 + 10 * np.log10(g2.mean())

def render(plan):
    rnd = np.random.default_rng(plan.get("seed", 1))
    total = float(plan["seconds"]); n = int((total + 6) * SR)
    dry = np.zeros((2, n)); padbus = np.zeros((2, n))
    t0 = plan.get("intro", 5.0)
    if t0 > 0:  # soft pad on the tonic before the first melody
        sh0 = plan["passes"][0].get("shift", 0)
        pc = pad_chord([60 + sh0, 64 + sh0, 67 + sh0], t0 + .5)
        e = min(n, len(pc)); padbus[0, :e] += pc[:e] * .5; padbus[1, :e] += pc[:e] * .5
    for p in plan["passes"]:
        tune = TUNES[p["tune"]]; sh = p.get("shift", 0); bpm = p.get("tempo", 72); spb = 60 / bpm
        inst = p["inst"]; oct_up = p.get("octave", 12 if inst in ("musicbox", "celesta") else 0)
        vel0 = p.get("vel", .8); pan = p.get("pan", 0.0)
        # melody
        tt = t0
        for i, (nt, b) in enumerate(tune["mel"]):
            dur = b * spb
            if nt is not None:
                hum = (rnd.random() - .5) * .018
                v = voice(inst, nt + sh + oct_up, dur, vel0 * (.86 + .14 * rnd.random()), rnd)
                s = int(max(0, tt + hum) * SR); e = min(n, s + len(v))
                dry[0, s:e] += v[:e - s] * (1 - pan) * .5 * 2 ** .5
                dry[1, s:e] += v[:e - s] * (1 + pan) * .5 * 2 ** .5
            tt += dur
        mel_end = tt
        # accompaniment: soft arpeggio (harp/celesta below melody) + pad
        tc = t0 + tune["pickup"] * spb
        acc_inst = p.get("acc", "harp")
        for name, b in tune["chords"]:
            notes = [48 + sh + x for x in CHORD[name]]
            if p.get("arp", True):
                step = 1.0 if tune["meter"] == 3 else 2.0
                k = 0; tb = 0.0
                while tb < b - 1e-6:
                    nt = notes[k % len(notes)] if k % 2 == 0 else notes[(k + 1) % len(notes)] + 0
                    v = voice(acc_inst, nt, step * spb, .32 * (.9 + .1 * rnd.random()), rnd)
                    s = int((tc + tb * spb) * SR); e = min(n, s + len(v))
                    dry[0, s:e] += v[:e - s] * .55; dry[1, s:e] += v[:e - s] * .45
                    tb += step; k += 1
            if plan.get("pad", True):
                pc = pad_chord([nt + 12 for nt in notes[:3]], b * spb)
                s = int(tc * SR); e = min(n, s + len(pc))
                padbus[0, s:e] += pc[:e - s] * .5; padbus[1, s:e] += pc[:e - s] * .5
            tc += b * spb
        t0 = max(mel_end, tc) + p.get("gap", 2.5)
        if t0 > total - 4: break
    # reverb
    ir = reverb_ir(3.2, rnd)
    wet = np.stack([fftconvolve(dry[0], ir[0])[:n], fftconvolve(dry[1], ir[1])[:n]])
    mix = dry * .62 + wet * .55 + padbus * plan.get("pad_level", .16)
    nz = plan.get("noise", {"kind": "none"})
    if nz.get("kind", "none") != "none":
        y = noise(nz["kind"], n, rnd)
        mix += np.stack([y, np.roll(y, 731)]) * (10 ** (nz.get("db", -34) / 20)) * 4
    mix = mix[:, :int(total * SR)]
    # fades
    fi = int(3 * SR); fo = int(plan.get("fade_out", 12) * SR)
    mix[:, :fi] *= np.linspace(0, 1, fi); mix[:, -fo:] *= np.linspace(1, 0, fo) ** 1.5
    # loudness
    tgt = plan.get("lufs", -18); cur = lufs_approx(mix)
    mix *= 10 ** ((tgt - cur) / 20)
    pk = np.max(np.abs(mix))
    if pk > .89: mix *= .89 / pk
    return mix

if __name__ == "__main__":
    plan = json.load(open(sys.argv[1]))
    out = render(plan)
    from scipy.io import wavfile
    wavfile.write(sys.argv[2], SR, (out.T * 32767).astype(np.int16))
    print(f"wrote {sys.argv[2]}: {out.shape[1] / SR:.1f} s, approx {lufs_approx(out):.1f} LUFS, peak {np.max(np.abs(out)):.2f}")
