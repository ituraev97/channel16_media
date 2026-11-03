#!/usr/bin/env python3
"""Builds youtube_description.txt from timing.json (chapters) for THE CALL 005."""
import json, os, importlib.util
EP = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", f"{EP}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json"))
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
ch = [("0:00", "Five people in a life raft")]
for i, (txt, shots, o) in enumerate(E.LINES):
    if shots[0][0] == "g:chapter":
        ch.append((fmt(T["starts"][i]), shots[0][2]["t"].title()))
    if shots[0][0] == "g:steps" and shots[0][2].get("title") == "WHAT GOT EVERYONE HOME":
        ch.append((fmt(T["starts"][i]), "What Got Everyone Home"))
summary = ("November 6, 2025. A sailing catamaran called Magic Bus is filling with water about 260 nautical miles (roughly 300 statute miles) off Cape Hatteras, North Carolina, and the five people aboard have abandoned ship into a life raft. "
           "That far out, the rescue pushes the limits of a Coast Guard helicopter's range. Using real U.S. Coast Guard footage and U.S. Navy photos, we follow the call step by step: a Hercules that finds the raft, a Jayhawk crew from Air Station Elizabeth City, "
           "and the aircraft carrier USS George H.W. Bush, which refuels the helicopter on the way out and again on the way home. "
           "Then, less than two months later, the same air station answers another call off Hatteras: two people, a dog and a cat, and an EPIRB that put their position in front of watchstanders within minutes.")
src = [
 ("Magic Bus rescue (U.S. Coast Guard)", "https://www.news.uscg.mil/Press-Releases/Article/4328992/coast-guard-rescues-5-people-from-sinking-sailboat-off-cape-hatteras/"),
 ("Carrier assists long-range rescue (Maritime Executive)", "https://www.maritime-executive.com/article/carrier-uss-george-w-bush-assists-long-range-rescue-off-cape-hatteras"),
 ("Refueling out and back, the cutter (WorkBoat)", "https://www.workboat.com/coastal-inland-waterways/coast-guard-rescues-sailors-260-miles-off-cape-hatteras"),
 ("Five rescued off Cape Hatteras (WTKR)", "https://www.wtkr.com/news/in-the-community/outer-banks/five-rescued-from-sailboat-sinking-off-cape-hatteras-uscg"),
 ("Navy carrier helps Coast Guard (gCaptain)", "https://gcaptain.com/navy-carrier-helps-coast-guard-save-five-sailors-far-offshore-cape-hatteras/"),
 ("The aircrew's view of the boat (Fox News)", "https://www.foxnews.com/us/coast-guard-swoops-save-stranded-sailors-sinking-boat-hundreds-miles-off-coast"),
 ("Final trip for the Magic Bus (Scuttlebutt Sailing News)", "https://www.sailingscuttlebutt.com/2025/11/07/final-trip-for-the-magic-bus/"),
 ("Review of the Magic Bus incident report (S/V Sabado)", "https://svsabado.com/offshore-nightmare-decisions-that-saved-the-crew/"),
 ("U.S. Navy photos aboard USS George H.W. Bush, Nov. 6, 2025 (DVIDS)", "https://www.dvidshub.net/image/9381777"),
 ("Graveyard of the Atlantic (National Park Service)", "https://www.nps.gov/caha/learn/historyculture/shipwrecks.htm"),
 ("MH-60T fact sheet (U.S. Coast Guard Acquisitions)", "https://www.dcms.uscg.mil/Portals/10/CG-9/Acquisition%20PDFs/Factsheets/MH-60T.pdf"),
 ("Aviation Survival Technician training", "https://gocoastguard.com/careers/enlisted/ast"),
 ("How a 406 MHz beacon alert works (NOAA SARSAT)", "https://www.sarsat.noaa.gov/sys-diag.html"),
 ("Two people, a cat and a dog (WTKR)", "https://www.wtkr.com/news/in-the-community/outer-banks/coast-guard-saves-two-people-cat-and-dog-65-miles-offshore-of-cape-hatteras"),
 ("A rescue to remember (Coast Guard Mutual Assistance)", "https://mycgma.org/coast-guard-rescue-two-mariners-dog-cat-cape-hatteras/"),
 ("The unbothered cat (The Charlotte Observer, via Stars and Stripes)", "https://www.stripes.com/branches/coast_guard/2025-12-31/cat-aloof-reaction-coast-guard-rescue-nc-20258789.html"),
]
out = [summary, "", "Chapters:"] + [f"{a} {b}" for a, b in ch] + ["", "Sources:"] + [f"• {a} — {b}" for a, b in src] + [
 "",
 "Footage: U.S. Coast Guard via DVIDS (public domain) — Air Station Elizabeth City (PO3 Matt Thieme, PO3 Christine Bills), Coast Guard East.",
 "Photos: U.S. Navy via DVIDS (public domain) — MC3 Jayden Brown, MC2 Pierce Luck, USS George H.W. Bush (CVN 77).",
 "Appearance of U.S. government visual information does not imply or constitute endorsement.",
 "CHANNEL 16 is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard.",
 "", "#coastguard #rescue #searchandrescue"]
TAGS = ["coast guard rescue", "coast guard helicopter rescue", "cape hatteras", "graveyard of the atlantic", "magic bus catamaran", "life raft rescue",
        "uss george h.w. bush", "aircraft carrier", "mh-60 jayhawk", "hc-130 hercules", "air station elizabeth city", "rescue swimmer", "epirb",
        "pet rescue", "real rescue footage", "channel 16", "the call", "search and rescue"]
open(f"{EP}/youtube_description.txt", "w").write(f"TITLE: {E.META['title']}\n\n" + "\n".join(out) + "\n\nTAGS: " + ", ".join(TAGS) + "\n")
print("\n".join(out)); print(len("\n".join(out)), "chars")
