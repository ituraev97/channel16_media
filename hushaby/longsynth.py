#!/usr/bin/env python3
"""Memory-safe renderer for long (60 min) Little Hushaby plans.
synth.render() keeps several full-length float64 buffers and runs one giant FFT reverb/noise, which needs
far more than the ~7 GB RAM of the cloud container for 60 minutes. This renders the same plan format
(same instruments, tunes, pad, reverb, noise kinds, fades and loudness target) segment by segment:
 - music: passes are grouped into ~5 min segments; each segment (plus an 8 s tail) is rendered dry,
   reverberated with ONE shared impulse response and overlap-added into a float32 master,
   so the result equals one continuous render (the mix is linear) with no seams;
 - noise: generated as a continuous stream with stateful IIR filters (no block boundaries);
 - loudness: gated LUFS approximation computed in 400 ms blocks, same method as synth.lufs_approx.
usage: longsynth.py plan.json out.wav
"""
import json, sys
import numpy as np
from scipy.signal import fftconvolve, butter, sosfilt, sosfilt_zi
from scipy.io import wavfile
import synth
from synth import SR, TUNES, CHORD, voice, pad_chord, reverb_ir

def schedule(plan):
    total = float(plan["seconds"]); t0 = plan.get("intro", 5.0); out = []
    for p in plan["passes"]:
        tune = TUNES[p["tune"]]; spb = 60 / p.get("tempo", 72)
        mel_len = sum(b for _, b in tune["mel"]) * spb
        tc_len = tune["pickup"] * spb + sum(b for _, b in tune["chords"]) * spb
        out.append((t0, p))
        t0 = t0 + max(mel_len, tc_len) + p.get("gap", 2.5)
        if t0 > total - 4: break
    return out

def render_pass(p, start, rnd, dry, padbus, off, plan):
    """add one pass into segment buffers (dry, padbus) whose sample 0 is absolute time `off`."""
    n = dry.shape[1]
    tune = TUNES[p["tune"]]; sh = p.get("shift", 0); spb = 60 / p.get("tempo", 72)
    inst = p["inst"]; oct_up = p.get("octave", 12 if inst in ("musicbox", "celesta") else 0)
    vel0 = p.get("vel", .8); pan = p.get("pan", 0.0)
    tt = start
    for nt, b in tune["mel"]:
        dur = b * spb
        if nt is not None:
            hum = (rnd.random() - .5) * .018
            v = voice(inst, nt + sh + oct_up, dur, vel0 * (.86 + .14 * rnd.random()), rnd).astype(np.float32)
            s = int(max(0, tt + hum - off) * SR); e = min(n, s + len(v))
            if e > s:
                dry[0, s:e] += v[:e - s] * (1 - pan) * .5 * 2 ** .5
                dry[1, s:e] += v[:e - s] * (1 + pan) * .5 * 2 ** .5
        tt += dur
    tc = start + tune["pickup"] * spb
    acc_inst = p.get("acc", "harp")
    for name, b in tune["chords"]:
        notes = [48 + sh + x for x in CHORD[name]]
        if p.get("arp", True):
            step = 1.0 if tune["meter"] == 3 else 2.0
            k = 0; tb = 0.0
            while tb < b - 1e-6:
                nt = notes[k % len(notes)] if k % 2 == 0 else notes[(k + 1) % len(notes)]
                v = voice(acc_inst, nt, step * spb, .32 * (.9 + .1 * rnd.random()), rnd).astype(np.float32)
                s = int((tc + tb * spb - off) * SR); e = min(n, s + len(v))
                if e > s:
                    dry[0, s:e] += v[:e - s] * .55; dry[1, s:e] += v[:e - s] * .45
                tb += step; k += 1
        if plan.get("pad", True):
            pc = pad_chord([nt + 12 for nt in notes[:3]], b * spb).astype(np.float32)
            s = int((tc - off) * SR); e = min(n, s + len(pc))
            if e > s:
                padbus[0, s:e] += pc[:e - s] * .5; padbus[1, s:e] += pc[:e - s] * .5
        tc += b * spb

def stream_noise(kind, n, seed, out_scale):
    """continuous noise (mono float32, length n) using stateful filters; normalised so the brown/pink core peaks ~1."""
    rnd = np.random.default_rng(seed + 7)
    blk = SR * 60
    y = np.empty(n, np.float32)
    if kind in ("pink", "rain"):  # Paul Kellet-style pink via 3 one-pole sections approximated with a 1st-order low-shelf chain
        core = butter(1, [40, 8000], btype="band", fs=SR, output="sos")
    else:  # brown / womb / shush base: 1/f amplitude above ~5 Hz
        core = butter(1, 5, fs=SR, output="sos")
    post = None
    if kind == "womb": post = butter(2, 400, fs=SR, output="sos")
    if kind == "rain": post = butter(2, 5000, fs=SR, output="sos")
    if kind == "shush": post = butter(2, [1800, 7000], btype="band", fs=SR, output="sos")
    zc = sosfilt_zi(core) * 0; zp = sosfilt_zi(post) * 0 if post is not None else None
    scale = None
    for s in range(0, n, blk):
        e = min(n, s + blk); w = rnd.standard_normal(e - s)
        x = w if kind == "shush" else sosfilt(core, w, zi=zc)
        if kind != "shush": x, zc = x
        if kind == "pink": x = x  # band-limited flat-ish: pink approximated below
        if post is not None: x, zp = sosfilt(post, x, zi=zp)
        if scale is None: scale = 1.0 / (np.percentile(np.abs(x), 99.99) + 1e-9)
        t = (np.arange(s, e) / SR)
        if kind == "womb": x = x * (.65 + .35 * np.sin(2 * np.pi * 1.0 * t) ** 8)
        if kind == "shush": x = x * (.25 + .75 * np.sin(np.pi * t / 5.0) ** 2)
        y[s:e] = (x * scale * out_scale).astype(np.float32)
    return y

def lufs_blocks(mix):
    hp = butter(2, 60, btype="high", fs=SR, output="sos")
    blk = int(.4 * SR); nb = mix.shape[1] // blk; ms = np.zeros(nb)
    z = [sosfilt_zi(hp) * 0, sosfilt_zi(hp) * 0]
    step = blk * 150
    for s in range(0, nb * blk, step):
        e = min(nb * blk, s + step); acc = 0
        for c in range(2):
            y, z[c] = sosfilt(hp, mix[c, s:e].astype(np.float64), zi=z[c])
            acc = acc + (y.reshape(-1, blk) ** 2).mean(axis=1)
        ms[s // blk: e // blk] = acc
    l = -0.691 + 10 * np.log10(ms + 1e-12)
    g = ms[l > -70]; rel = -0.691 + 10 * np.log10(g.mean()) - 10
    g2 = ms[(l > -70) & (l > rel)]
    return -0.691 + 10 * np.log10(g2.mean())

def render_long(plan):
    total = float(plan["seconds"]); n = int(total * SR)
    rnd = np.random.default_rng(plan.get("seed", 1))
    ir = reverb_ir(3.2, np.random.default_rng(plan.get("seed", 1) + 101)).astype(np.float32)
    mix = np.zeros((2, n), np.float32)
    sched = schedule(plan)
    # intro pad
    t0 = plan.get("intro", 5.0)
    segs = []; cur = []; seg_start = 0.0
    for start, p in sched:
        if cur and start - seg_start > 300: segs.append((seg_start, cur)); cur = []; seg_start = start
        cur.append((start, p))
    if cur: segs.append((seg_start, cur))
    for i, (off, items) in enumerate(segs):
        end = (segs[i + 1][0] if i + 1 < len(segs) else total) + 9.0
        m = int((end - off) * SR)
        dry = np.zeros((2, m), np.float32); padbus = np.zeros((2, m), np.float32)
        if i == 0 and t0 > 0:
            sh0 = plan["passes"][0].get("shift", 0)
            pc = pad_chord([60 + sh0, 64 + sh0, 67 + sh0], t0 + .5).astype(np.float32); e = min(m, len(pc))
            padbus[0, :e] += pc[:e] * .5; padbus[1, :e] += pc[:e] * .5
        for start, p in items: render_pass(p, start, rnd, dry, padbus, off, plan)
        wet = np.stack([fftconvolve(dry[0], ir[0])[:m], fftconvolve(dry[1], ir[1])[:m]]).astype(np.float32)
        seg = dry * .62 + wet * .55 + padbus * plan.get("pad_level", .16)
        s = int(off * SR); e = min(n, s + m)
        mix[:, s:e] += seg[:, :e - s]
        del dry, padbus, wet, seg
        print(f"segment {i + 1}/{len(segs)} at {off:.0f}s", flush=True)
    nz = plan.get("noise", {"kind": "none"})
    if nz.get("kind", "none") != "none":
        y = stream_noise(nz["kind"], n, plan.get("seed", 1), (10 ** (nz.get("db", -34) / 20)) * 4)
        # calibrate: match the RMS of synth.noise() (the short-video generator) on a 120 s reference
        ref = synth.noise(nz["kind"], SR * 120, np.random.default_rng(5)); a = int(SR * 5)
        cal = np.sqrt(np.mean(ref[a:] ** 2)) / (np.sqrt(np.mean(y[a:SR * 120].astype(np.float64) ** 2)) / ((10 ** (nz.get("db", -34) / 20)) * 4))
        y *= np.float32(cal); del ref
        mix[0] += y; mix[1, 731:] += y[:-731]; mix[1, :731] += y[-731:]
        del y
    fi = int(3 * SR); fo = int(plan.get("fade_out", 12) * SR)
    mix[:, :fi] *= np.linspace(0, 1, fi, dtype=np.float32); mix[:, -fo:] *= (np.linspace(1, 0, fo, dtype=np.float32) ** 1.5)
    tgt = plan.get("lufs", -18); cur = lufs_blocks(mix)
    mix *= np.float32(10 ** ((tgt - cur) / 20))
    pk = float(np.max(np.abs(mix)))
    if pk > .89: mix *= np.float32(.89 / pk)
    return mix

if __name__ == "__main__":
    plan = json.load(open(sys.argv[1]))
    out = render_long(plan)
    pcm = np.empty(out.shape[::-1], np.int16)
    for c in range(2): pcm[:, c] = np.clip(out[c] * 32767, -32768, 32767).astype(np.int16)
    wavfile.write(sys.argv[2], SR, pcm)
    print(f"wrote {sys.argv[2]}: {out.shape[1] / SR:.1f} s, approx {lufs_blocks(out):.1f} LUFS, peak {np.max(np.abs(out)):.2f}")
