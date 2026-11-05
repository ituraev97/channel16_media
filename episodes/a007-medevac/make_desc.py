#!/usr/bin/env python3
"""Builds youtube_description.txt from timing.json (chapters) for ANATOMY OF A RESCUE 007."""
import json, os, importlib.util
EP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json"))
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
ch = [("0:00", "1,500 miles from help")]
for i, (txt, shots, o) in enumerate(E.LINES):
    if shots[0][0] == "g:chapter":
        ch.append((fmt(T["starts"][i]), shots[0][2]["t"].title()))
summary = ("How do you get a seriously ill person off a ship far out at sea? Using real U.S. Coast Guard footage, we break down how a medical evacuation works, step by step, through six real cases: "
           "a fishing boat 92 miles off Georgia, the cruise ship Celebrity Solstice off Oahu at night with a Navy helicopter watching over, a Dolphin crew that refuels on the cutter Harriet Lane before hoisting a man from the cargo ship Viking Emerald off Kauai, "
           "a passenger with stroke symptoms on the Carnival Luminosa off Humboldt Bay, a mariner hoisted from a motor lifeboat in heavy seas off Oregon, "
           "and the master of the cargo ship Chipol Donghai, who fell ill about 1,500 miles north of Oahu. "
           "Who decides to launch, why a flight surgeon is involved, and why a ship sometimes heads toward the helicopter.")
src = [
 ("Chipol Donghai medevac (U.S. Coast Guard)", "https://www.news.uscg.mil/Press-Releases/Article/4323393/coast-guard-medevacs-master-from-hong-kong-flagged-cargo-ship-offshore-oahu/"),
 ("Still Fishing medevac, 92 miles off Brunswick (U.S. Coast Guard)", "https://www.news.uscg.mil/Press-Releases/Article/4516331/coast-guard-medevacs-man-from-fishing-vessel-92-miles-offshore-brunswick/"),
 ("Celebrity Solstice medevac off Oahu (U.S. Coast Guard)", "https://www.news.uscg.mil/Press-Releases/Article/4470788/coast-guard-medevacs-cruise-ship-passenger-offshore-oahu/"),
 ("Celebrity Solstice medevac (Hawaii News Now)", "https://www.hawaiinewsnow.com/2026/04/25/coast-guard-medevacs-man-off-cruise-ship-offshore-oahu/"),
 ("Ocean Gladiator medevac (Honolulu Star-Advertiser)", "https://www.staradvertiser.com/2026/10/09/breaking-news/crew-member-55-medevaced-from-cargo-ship-off-hawaii-island/"),
 ("Carnival Luminosa medevac (U.S. Coast Guard)", "https://www.news.uscg.mil/Press-Releases/Article/4549640/coast-guard-medevacs-cruise-ship-passenger-offshore-humboldt-bay/"),
 ("Carnival Luminosa medevac (KRCR)", "https://krcrtv.com/north-coast-news/eureka-local-news/woman-rescued-from-cruise-ship-off-humboldt-bay-after-suspected-stroke"),
 ("Queen Elizabeth medevac (U.S. Coast Guard)", "https://www.news.uscg.mil/Press-Releases/Article/4476336/coast-guard-medevacs-cruise-ship-passenger-southwest-of-shelter-cove/"),
 ("Moving target: How do you medevac embarked patients? (Juneau Empire, 2019)", "https://www.juneauempire.com/news/moving-target-how-do-you-medevac-embarked-patients"),
 ("MH-65 Dolphin (U.S. Coast Guard)", "https://www.uscg.mil/Assets/Article/1822743/mh-65-short-range-recovery-helicopter"),
 ("47-foot Motor Life Boat (U.S. Coast Guard)", "https://www.uscg.mil/Assets/Article/1825014/47-foot-motor-life-boat/"),
 ("DVIDS videos", "https://www.dvidshub.net/video/984907 · /1010820 · /1003800 · /1006503 · /998677 · /1015431 · /986213 · /1025953"),
]
out = [summary, "", "Chapters:"] + [f"{a} {b}" for a, b in ch] + ["", "Sources:"] + [f"• {a} — {b}" for a, b in src] + [
 "",
 "Footage: U.S. Coast Guard via DVIDS (public domain) — Air Station Barbers Point (PO3 Avery Tibbets; CPO Corinne Zilnicki and PO2 Tyler Robertson), Air Station Clearwater, Air Station Humboldt Bay, Air Station Astoria (Lt. Christopher Butters), Coast Guard Oceania District, Coast Guard Southeast, Coast Guard Southwest, Coast Guard Northwest.",
 "Appearance of U.S. government visual information does not imply or constitute endorsement.",
 "CHANNEL 16 is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard.",
 "", "#coastguard #rescue #searchandrescue"]
TAGS = ["coast guard rescue", "coast guard medevac", "medevac at sea", "cruise ship medevac", "helicopter hoist", "mh-65 dolphin", "mh-60 jayhawk",
        "flight surgeon", "air station barbers point", "air station humboldt bay", "air station astoria", "motor lifeboat", "rescue swimmer",
        "real rescue footage", "anatomy of a rescue", "channel 16", "search and rescue", "cargo ship medevac"]
open(f"{EP}/youtube_description.txt", "w").write(f"TITLE: {E.META['title']}\n\n" + "\n".join(out) + "\n\nTAGS: " + ", ".join(TAGS) + "\n")
print("\n".join(out)); print(len("\n".join(out)), "chars")
