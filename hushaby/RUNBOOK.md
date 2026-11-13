# Little Hushaby — RUNBOOK

Channel: **Little Hushaby** (YouTube channel ID `UClIEnu6kMrh0x-iZKceoq8Q`, target handle `@littlehushaby`; formerly CHANNEL16). It is a kids channel: channel-level "made for kids" is ON and every upload is `madeForKids: true`. YouTube only, with no TikTok, because TikTok is 13+.
Metricool brand blogId **7743228**, timezone America/New_York. This brand also holds the paused CHANNEL 16 TikTok, so never post to tiktok from here.
Project bible: Projects doc `claude/little-hushaby-bible.md` (rules, brand, money). This file covers how to build.

## 1. Setup (fresh container)
```
cd /home/claude/channel16_media/hushaby
npm i @fontsource/fredoka @fontsource/nunito          # fonts (embedded as base64 into every render)
ln -sfn "$(npm root -g)/playwright" node_modules/playwright   # Playwright is preinstalled globally
python3 -c "import numpy, scipy"                     # synth needs numpy + scipy only
```
Work in `/home/claude/channel16_media/hushaby`. Never commit `node_modules/`, `frames/`, `episodes/*/out/`, wav or mp4 files to main.

## 2. Files
- `art.mjs`: palette `PAL` (night, dusk, winter, ocean), colours `C`, the mascots (`bunny`, `bear`, `kitten`, drawn in a 220x150 box with the head on the left and asleep), `bowlMoon`, `sky`, `hills`, `cloud`, `wordmark`.
- `scene.mjs`: seamless animated loop to PNG frames. Every motion completes a whole number of cycles per loop, so the loop can repeat for hours without a jump. `loop` must be a multiple of 6 s (the "z" cycle). Options: char, pal, seed, snow, caption (Shorts), layout wide or tall.
- `synth.py`: the lullaby synthesizer, pure numpy. The instruments are musicbox, celesta, harp and piano. Tunes live in `TUNES`. It adds a pad, reverb and optional noise (pink, brown, womb, shush, rain, white) and normalises to the target LUFS.
- `longsynth.py`: memory-safe renderer for long plans (build.py uses it when seconds > 1200). The container has ~7 GB RAM and synth.py runs out of memory at 60 min; longsynth renders ~5-min segments with one shared reverb and overlap-adds them (no seams), streams the noise with stateful filters (RMS calibrated to synth.noise) and measures loudness in blocks.
- `thumb.mjs`: 1280x720 thumbnail with l1, l2, badge, char and pal.
- `build.py episodes/<id> [long|short|all]` writes `out/long.mp4`, `out/short.mp4` and `out/thumb.jpg`.
- `brandkit.mjs` renders the avatar, banner and watermark into `brand/`.

## 3. Formats (weekday = ET publish date)
| Day | Long video | Sound |
|---|---|---|
| Mon, Wed, Fri | Lullaby, 10–15 min (2 melodies, alternating instruments and keys, gently slowing) | music box, celesta, harp, piano; no noise |
| Tue, Thu, Sat | Sleep, 60 min | 1–2 melodies, slow tempo 56–64, plus noise: Tue `womb` −30 dB, Thu `shush` −32 dB, Sat `rain` or `pink` −30 dB |
| Sun | Lullaby medley, 20–30 min | 3+ melodies if available |

- Plus **one YouTube Short every day**: one melody pass, 35–50 s, vertical 1080x1920, caption = the song name in 1–2 lines, using a different character, palette or melody than the day before.
- Vary every video: character, palette, seed, keys (`shifts`), instrument order, tempo curve. No two uploads may share the same audio. YouTube demonetises repetitive, mass-produced content, and kids content has extra quality rules: calm, complete and honest.
- Size limit: GitHub raw files must stay ≤ 95 MB. A 60-min sleep video uses `"crf": 26` and `"abr": "96k"` in episode.json long (build.py reads both; e002 = 78.9 MB). Check the size before pushing; if it is too big, raise crf by 2 and/or lower audio to 80k.

## 4. Melodies: public domain only
Present: `brahms` (Wiegenlied Op. 49 No. 4, 1868), `twinkle` (traditional) `allnight` (All Through the Night / Ar Hyd y Nos, Welsh trad., Jones 1784; added 10.11.2026, sources in e002) and `frere` (Frère Jacques / Are You Sleeping, French trad. round, 8 bars ≈ 27 s at 72 bpm; checked against Boutet de Monvel/Widor 1883; added 11.11.2026, sources in e003). Original: `moonboat` ("Moon Boat Lullaby", our own 16-bar 3/4 melody in C; added 12.11.2026 in e004; always title it as an original lullaby) and `raindrop` ("Raindrop Lullaby", our own 16-bar 4/4 melody in C; added 13.11.2026 in e005; always title it as an original lullaby). 13.11.2026: Commons API + upload.wikimedia.org again HTTP 429 for the Rock-a-bye Baby score, so the 6th tune is an original; next PD candidate to try: `File:Rock-a-bye Baby and Lillibulero.png` on Commons.
Score access from the cloud: en.wikipedia.org, IMSLP, Mutopia and tunearch are blocked by the proxy; Wikimedia Commons file pages and `upload.wikimedia.org/.../thumb/.../1280px-<file>` thumbnails work (use a custom User-Agent, wait a few seconds between requests), then Read the image. 12.11.2026: upload.wikimedia.org answered HTTP 429 (robot policy) to plain curl, so no PD score could be opened; do not try to work around it — add an original melody that day instead.
Add new tunes only if all three hold:
- the melody was published before 1929 (folk or traditional, or a composer who died before 1956);
- you are certain of every note; check against a public-domain score you actually opened, such as Mutopia, IMSLP or Wikisource, and note the URL in `sources.md`;
- it has chords per bar.

Good candidates: Rock-a-bye Baby (1886), Hush Little Baby (trad.), All Through the Night (Ar Hyd y Nos, trad.), Golden Slumbers (trad.), Sleep Baby Sleep (trad.), Schubert Wiegenlied D 498, Mozart/Flies Wiegenlied, Are You Sleeping (Frère Jacques). Original melodies are also allowed: write them as simple 8–16 bar phrases in the pentatonic or major scale with I–IV–V chords, and title them honestly ("Original Lullaby").
Never use modern songs or other channels' arrangements, and never use characters from shows (Cocomelon, Disney, Bluey, etc.).

## 5. Build and QA
1. Write `episodes/eNNN-<slug>/episode.json` (see e001). build.py sizes the number of long passes from each tune's real length (11.11.2026), so short tunes never leave silence at the end. Use an odd-length `insts` list (e.g. 5) with 2 tunes so each tune rotates through every instrument. Long: seconds, tunes, insts, shifts, tempo [start, end], noise, scene, thumb. Short: tune, inst, tempo, seconds, caption, scene.
2. `nohup python3 build.py episodes/eNNN-<slug> > build.log 2>&1 &`, then wait. A 12-min episode takes about 4 min; a 60-min one about 12 min.
3. QA (all mandatory):
   - `ffprobe` the duration: long within ±10 s of the plan, Short 30–58 s.
   - `ffmpeg -i out/long.mp4 -af ebur128 -f null -`: integrated loudness −20…−16 LUFS (Short −17…−15), true peak ≤ −1 dBFS.
   - Contact sheet: one frame every 60 s plus the first and last frame. Read it. Nothing clipped, the character is drawn correctly, no white or black frames.
   - Seam check: frame 0 and frame N−1 of the loop must be nearly identical. Mean abs diff < 2 in a 192x108 grey comparison.
   - Listen-proxy: plot a spectrogram of the first 30 s. Melody notes must be visible, with no clicks (vertical full-band lines) and no silence gaps over 4 s except the end fade.
   - Look at `thumb.jpg`: text readable at 320x180.
4. If anything fails, fix it and rebuild that part (`build.py <dir> long` or `short`).

## 6. Hosting
Orphan branch per ET weekday: `hushaby-<mon..sun>`, containing only `long.mp4`, `short.mp4` and `thumb.jpg`. Force-push it, then check every `https://raw.githubusercontent.com/ituraev97/channel16_media/hushaby-<day>/<file>` returns HTTP 200. Never put video on main.

## 7. Metricool (blogId 7743228, timezone America/New_York, autoPublish true)
- **Long video at 17:00 ET:** providers `[{"network":"youtube"}]`; youtubeData `{title, type "video", privacy "public", madeForKids true, category "MUSIC", tags, isAiGeneratedContent false}`; videoThumbnailUrl = the thumb URL. If the post is rejected because of the thumbnail, retry once without it.
- **Short at 12:00 ET:** providers `[{"network":"youtube"}]`; youtubeData `{title, type "short", privacy "public", madeForKids true, category "MUSIC", tags}`.
- **Titles** (≤ 100 chars) name the real melody first, then the format and the benefit, with no false promises:
  - "Brahms Lullaby & Twinkle Twinkle Little Star 🌙 Music Box Lullaby for Babies to Go to Sleep"
  - "1 Hour Baby Sleep Music 🌙 Brahms Lullaby + Womb Sounds"
  - Shorts: "Twinkle Twinkle Little Star 🌙 Music Box Lullaby #shorts"
- **Description:**
  - Line 1–2: what it is, with the main keywords.
  - "♪ Melodies:" with public-domain credits.
  - "Arrangement, sound and animation: Little Hushaby."
  - A gentle tip ("Lower the screen brightness at bedtime").
  - 3 hashtags: #lullaby #babysleep #musicbox
- **Tags:** 10–15 researched keywords.
- After scheduling, verify both posts with getScheduledPosts.

## 8. Commit
On main, commit `hushaby/episodes/eNNN-*/episode.json`, the plans, `sources.md`, `research/*.md` and any code changes. Run `git fetch` and rebase first, and end the message with the session attribution lines.
