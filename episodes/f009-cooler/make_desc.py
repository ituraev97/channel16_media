#!/usr/bin/env python3
"""Builds youtube_description.txt from timing.json (chapters) for STORM FILES 009."""
import json, os, importlib.util
EP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json"))
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
ch = [("0:00", "On a cooler")]
for i, (txt, shots, o) in enumerate(E.LINES):
    if shots[0][0] == "g:chapter":
        ch.append((fmt(T["starts"][i]), shots[0][2]["t"].title()))
summary = ("A Coast Guard rescue from Hurricane Milton: a fishing captain rode out the storm in the open Gulf of Mexico holding on to a cooler, and an Air Station Miami helicopter crew found him about 30 miles off Longboat Key, Florida, on Oct. 10, 2024. "
           "Using real U.S. Coast Guard footage, we tell the whole story of two hurricanes in two weeks: Hurricane Helene and the Gulfport rescue, "
           "the Capt. Dave's first rescue on Monday, why the captain went back out on landfall day, the lost radio contact, the search, the rescue swimmer, and what the Coast Guard said kept him alive: a life jacket, an EPIRB and a cooler.")
src = [
 ("U.S. Coast Guard release, Oct. 10, 2024 (Longboat Key rescue)", "https://www.news.uscg.mil/Press-Releases/Article/3933279/"),
 ("NPR/GPB, Oct. 11, 2024 (pilots' account)", "https://www.gpb.org/news/2024/10/11/we-were-ecstatic-coast-guard-rescues-man-clinging-cooler-in-open-water"),
 ("U.S. Coast Guard release, Oct. 9, 2024 (Milton preparations)", "https://www.news.uscg.mil/Press-Releases/Article/3931638/"),
 ("U.S. Coast Guard release, Oct. 1, 2024 (Helene response)", "https://www.news.uscg.mil/Press-Releases/Article/3921895/"),
 ("NOAA NESDIS (Helene landfall)", "https://www.nesdis.noaa.gov/news/hurricane-helene-makes-landfall-florida"),
 ("NHC Milton report via WFLA", "https://www.yahoo.com/news/milton-one-most-powerful-atlantic-144202438.html"),
 ("WWSB/ABC7 Sarasota (Milton landfall)", "https://www.mysuncoast.com/2024/10/10/hurricane-milton-makes-landfall-siesta-key/"),
 ("WUSF (Helene storm surge records)", "https://wusf.org/weather/2024-10-02/early-readings-show-the-tampa-bay-region-sustained-record-storm-surge"),
 ("FOX Weather", "https://www.foxweather.com/extreme-weather/florida-gulf-of-mexico-cooler-coast-guard-rescue-milton"),
 ("NOAA SARSAT (EPIRB)", "https://www.sarsat.noaa.gov/"),
 ("DVIDS videos", "https://www.dvidshub.net/video/939855 · /939934 · /938233 · /940566 · /939360 · /939646 · /939530 · /939937 · /940014 · /940869 · /938595 · /938294 · /937908 · /938016 · /939451 · /939658"),
]
out = [summary, "", "Chapters:"] + [f"{a} {b}" for a, b in ch] + ["", "Sources:"] + [f"• {a} — {b}" for a, b in src] + [
 "",
 "Footage: U.S. Coast Guard via DVIDS (public domain) — Air Station Miami, Air Station Clearwater, Seventh District, Coast Guard Video Production Team "
 "(PO3 Nicholas Strasburg, PO3 Santiago Gomez, PO1 Riley Perkofski, PO3 Vincent Moreno, PO2 Ryan Pierce, PO2 Jose Hernandez, PO2 Ian Gray; courtesy videos).",
 "Appearance of U.S. government visual information does not imply or constitute endorsement.",
 "CHANNEL 16 is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard.",
 "", "#coastguard #rescue #hurricanemilton"]
TAGS = ["coast guard rescue", "hurricane milton", "man on cooler", "man clinging to cooler", "hurricane rescue", "helicopter rescue at sea", "rescue swimmer",
        "epirb", "air station miami", "air station clearwater", "hurricane helene", "longboat key", "search and rescue", "real rescue footage", "storm files"]
open(f"{EP}/youtube_description.txt", "w").write(f"TITLE: {E.META['title']}\n\n" + "\n".join(out) + "\n\nTAGS: " + ", ".join(TAGS) + "\n")
print("\n".join(out)); print(len("\n".join(out)), "chars")
