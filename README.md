# CHANNEL 16 — media & pipeline

Real U.S. Coast Guard rescues, explained. Independent channel, not affiliated with or endorsed by the U.S. Coast Guard.

- `pipeline/` — production scripts (narration, graphics, edit, score/SFX mix, encode, Shorts, thumbnails, QA).
- `episodes/` — episode scripts (`episode.py`), Shorts specs, sources, thumbnail configs, descriptions. No video files on `main`.
- `brand/` — avatar, banner, watermark, palette, lower-third reference.
- `clips.json` — per-clip active picture area (`box`) and detected internal cuts (`cuts`).
- `drop-mon` … `drop-sun` — rotating upload slots: one day's video files per branch (orphan commit, force-pushed) so Metricool can fetch them by public raw URL.
- `RUNBOOK.md` — step-by-step for a production run.

Footage: public-domain U.S. government video via DVIDS. Appearance of U.S. government visual information does not imply or constitute endorsement.
