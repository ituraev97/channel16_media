# m015 QA (2026-11-12)
- Durations: t1 74.0 s, t2 73.4 s, t3 74.5 s, t4 70.7 s, t5 74.2 s; loudness −14.1…−14.2 LUFS.
- motion_check: 0 issues on all five. The check was run with extra "cuts" at genuine muzzle blasts / missile impacts (954992 120.68 and 136.42, 864039 104.34, 1017152 9.11 and 54.45 → 1017152c 4.75, 475606 launch flash 5.17/5.64), which are real one-frame brightness jumps in the footage, not judder. These are NOT in clips.json (short16 would treat them as cuts).
- 1017152 repeats every 4th frame on its deck cameras → de-duplicated sub-clips 1017152a/b/c (mpdecimate + minterpolate) used instead.
- Fact-check: independent agent, 15 findings, all applied before the final build.
- 0.5 s frames: t1 THAAD launch, t2 Paladin muzzle blast, t3 B-1B underside with afterburners, t4 Harpoon impact fireball at Peleliu's hull, t5 CV-22 nose with refuel probe.
