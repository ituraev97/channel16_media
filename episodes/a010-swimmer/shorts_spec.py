# Shorts for ANATOMY 010 (The Rescue Swimmer). TikTok s1–s5: 62–75 s each (Creator Rewards needs > 1 min), one rescue each, own narration.
# YouTube Shorts y1–y3 (YSHORTS): 15–30 s cuts that open on the single most dramatic moment, built with PLATFORM=youtube.
# Facts: sources.md. shot: (clip_id, start, cx) — cx = horizontal centre of the 9:16 crop inside the active picture (0..1)
SAND = 909520        # Sandpiper, Columbia River bar, Feb 3, 2023 (vertical phone video from the Jayhawk)
SANDM = 872430       # same rescue, motor lifeboat view 0–7.1 s
SANDV = "872430v"    # same rescue, vertical part 14.9–26.6 (wave from the helicopter, alternate edit) — used only as the hook flash-forward
SANDQ = "872430q"    # same rescue, 4:3 parts: swimmer lowered 7.2–10.6; swimmer + survivor hoisted / cabin 26.7–39.5
AHRS = 1006811       # Advanced Helicopter Rescue School, Astoria, TRAINING footage, Feb 2026
GALV = 993525        # Sea Ray taking on water near Galveston, Jan 17, 2026 (swimmer camera)
STURG = 971965       # 3 rescued from a capsized 16-ft boat, Sturgeon Bay, Mich., July 28, 2025
SARG = 976930        # 3 helped from a capsized 17-ft boat onto a Station Freeport boat, off Sargent, Texas, Sep 13, 2025 (vertical)
NAHMA = 970021       # AST2 Ryan Watkins, medical emergency on a 16-ft boat near Nahma, Mich., July 13, 2025

AHRS_L = dict(label="RESCUE SCHOOL, ASTORIA · TRAINING, 2026")
CAB_L = dict(label="JAYHAWK CAMERAS · DURING THE RESCUE")

SHORTS = [
 dict(id="s1", hook="WATCH THE<br>[WAVE]", title="A wave flipped his boat, and the Coast Guard swimmer was already in the water",
      lines=[
  ("Watch the wave behind this boat. A Coast Guard rescue swimmer is already in the water.", [(SANDV, 15.50, .5), (SANDV, 18.30, .5)], "tense", dict(label="FEB 3, 2023 · MOMENTS LATER")),
  ("This is off the Columbia River, February third, twenty twenty-three. But first, how it started.", [(SANDM, 0.20, .30)], "slow"),
  ("Ten a.m.: a mayday on channel sixteen, from the thirty-five-foot Sandpiper. Nothing else.", [(SAND, 0.2, .5), (SAND, 2.75, .5)], "tense"),
  ("Watchstanders estimated his position by triangulating the radio signal.", [(SAND, 5.3, .5)], "calm"),
  ("A Jayhawk crew from the Advanced Helicopter Rescue School is overhead. Their swimmer, a student, goes down the cable.", [(SANDQ, 7.30, .5), (SAND, 9.8, .5)], "drive"),
  ("Twenty-foot seas. He swims for the boat.", [(SAND, 12.9, .5), (SAND, 14.5, .5)], "calm"),
  ("The boat is taking on water, rolling in the swells.", [(SAND, 16.1, .5), (SAND, 17.6, .5)], "tense"),
  ("Then it breaks, right on top of the boat.", [(SAND, 21.60, .5)], "punch"),
  ("It rolls the boat over, and throws the man into the sea.", [(SAND, 24.60, .5), (SAND, 27.40, .5)], "tense"),
  ("The swimmer was already in the water. He reaches him.", [(SAND, 30.30, .5)], "drive"),
  ("Then the cable takes them both up, together.", [(SANDQ, 26.80, .45)], "drive"),
  ("Into the helicopter. The man was flown to Air Station Astoria, stable, with minor injuries.", [(SANDQ, 29.4, .5), (SANDQ, 34.25, .5)], "calm"),
  ("The swimmer was Branch Walton, Aviation Survival Technician Third Class. It was his first life saved.", [(AHRS, 99.1, .5), (AHRS, 82.2, .5)], "calm", AHRS_L),
  ("Hours later, he and his classmates graduated from the school. Follow for more real rescues.", [(AHRS, 122.3, .5), (AHRS, 168.9, .5)], "punch", AHRS_L),
 ]),
 dict(id="s2", hook="A PUMP ON<br>[THE CABLE]", title="Swimmer's camera: a Coast Guard rescue swimmer rides the cable down to a flooding boat",
      lines=[
  ("A Coast Guard rescue swimmer's own camera. And that's a pump, coming down his cable to a flooding boat.", [(GALV, 40.4, .5), (GALV, 43.5, .5)], "tense"),
  ("January seventeenth, twenty twenty-six, near Galveston, Texas. A forty-foot Sea Ray, with seven people aboard, is taking on water.", [(GALV, 26.3, .5), (GALV, 30.3, .5)], "calm"),
  ("An M-H sixty-five Dolphin crew from Air Station Houston flies out.", [(GALV, 2.6, .5)], "drive"),
  ("At the door, the swimmer hooks up to the hoist.", [(GALV, 6.7, .5)], "calm"),
  ("Then he's out, and going down, under the helicopter.", [(GALV, 12.0, .5), (GALV, 15.0, .5)], "drive"),
  ("He rides the cable down, with the Dolphin right above him.", [(GALV, 18.0, .5), (GALV, 21.4, .5)], "tense"),
  ("On deck, he looks back up at the helicopter.", [(GALV, 34.3, .5)], "calm"),
  ("The boat needs more than a swimmer. So the helicopter lowers a second load, on the same cable.", [(GALV, 37.3, .5), (GALV, 46.6, .5)], "tense"),
  ("He hauls in the line, and gets the pump aboard.", [(GALV, 50.6, .5)], "drive"),
  ("Then they start dewatering the boat.", [(GALV, 54.0, .5)], "calm"),
  ("Rescue swimmers train twenty-two weeks to earn their rating, seven of them as E-M-Ts.", [(GALV, 56.3, .5)], "calm"),
  ("The boat gets under way, with the swimmer still aboard.", [(GALV, 61.2, .5), (GALV, 65.4, .5)], "calm"),
  ("This swimmer was sent down to help save a boat.", [(GALV, 67.4, .5)], "slow"),
  ("A Coast Guard boat crew from Station Galveston comes out to meet them.", [(GALV, 71.6, .5), (GALV, 75.4, .5), (GALV, 79.2, .5)], "drive"),
  ("They escort the Sea Ray, and the seven people aboard, safely into port.", [(GALV, 83.4, .5), (GALV, 88.0, .5)], "calm"),
  ("This time, the job was keeping their boat afloat. Follow for more real rescues.", [(GALV, 101.5, .5)], "punch"),
 ]),
 dict(id="s3", hook="WEARING<br>[LIFE JACKETS]", title="Why the Coast Guard thanked three boaters who clung to a capsized boat on Lake Michigan",
      lines=[
  ("Three people in Lake Michigan, holding on to an overturned boat. Why did the Coast Guard thank them afterward?", [(STURG, 9.2, .5), (STURG, 12.5, .5)], "question"),
  ("July twenty-eighth, twenty twenty-five. One twenty-seven on a Monday afternoon. A sixteen-foot boat has capsized in Sturgeon Bay, Michigan.", [(STURG, 90.30, .5), (STURG, 94.70, .5)], "calm", CAB_L),
  ("Coast Guard Sector Northern Great Lakes sends out an urgent marine information broadcast.", [(STURG, 85.30, .5)], "calm", CAB_L),
  ("It launches a small boat from Station Saint Ignace, and diverts a Jayhawk crew from Air Station Traverse City.", [(STURG, 99.50, .5), (STURG, 37.80, .5)], "drive", CAB_L),
  ("Over the lake, the swimmer goes down first.", [(STURG, 0.5, .5)], "tense"),
  ("He swims to them.", [(STURG, 22.6, .5)], "calm"),
  ("Then the rescue basket goes down.", [(STURG, 17.50, .5)], "drive"),
  ("The swimmer works the water below.", [(STURG, 26.0, .5)], "calm"),
  ("And the basket comes back up, with a survivor inside.", [(STURG, 31.30, .5), (STURG, 34.00, .5)], "drive"),
  ("One at a time, the crew brings each of them into the cabin.", [(STURG, 41.00, .5), (STURG, 47.00, .5)], "calm"),
  ("Last, the swimmer comes up on the cable.", [(STURG, 72.40, .5)], "drive"),
  ("The boat crew checks the scene. No pollution, no debris, no hazard to other boats.", [(STURG, 56.00, .5), (STURG, 61.00, .5)], "calm", CAB_L),
  ("All three were flown to Pellston Airport, where emergency medical services were waiting.", [(STURG, 82.70, .5), (STURG, 80.10, .5)], "calm"),
  ("And the air station thanked them for wearing life jackets. It made finding and rescuing them far more efficient. Follow for more real rescues.", [(STURG, 63.7, .5), (STURG, 50.6, .5)], "punch"),
 ]),
 dict(id="s4", hook="SITTING ON<br>[THE HULL]", title="Sitting on an upside-down boat off Texas, until a Coast Guard swimmer came for them",
      lines=[
  ("Three people, sitting on an upside-down boat off the Texas coast. Watch who comes for them.", [(SARG, 9.0, .5), (SARG, 12.0, .5)], "question"),
  ("September thirteenth, twenty twenty-five. A Saturday. At eleven-oh-three, Coast Guard Sector Houston-Galveston gets the report.", [(SARG, 1.3, .5), (SARG, 15.0, .5)], "calm"),
  ("A seventeen-foot boat has capsized off Sargent, Texas, with two adults and an adolescent aboard.", [(SARG, 19.0, .5)], "tense"),
  ("Watchstanders put out an urgent marine information broadcast, and launch two crews.", [(SARG, 24.5, .5), (SARG, 27.0, .5)], "drive"),
  ("From Air Station Houston, an M-H sixty-five Dolphin. This video was shot from that helicopter.", [(SARG, 29.8, .5), (SARG, 32.8, .5)], "calm"),
  ("And from Station Freeport, a twenty-nine-foot response boat.", [(SARG, 35.8, .5)], "drive"),
  ("The crews find all three on the hull. The helicopter lowers its rescue swimmer.", [(SARG, 39.0, .5), (SARG, 41.5, .5)], "tense"),
  ("In the water, he helps them onto the Coast Guard boat, one by one.", [(SARG, 44.0, .5), (SARG, 45.8, .5)], "drive"),
  ("No hoist needed this time. The swimmer's job was in the water.", [(SARG, 52.0, .5), (SARG, 55.4, .5)], "calm"),
  ("Back on the hull, the next one waits.", [(SARG, 66.0, .5)], "slow"),
  ("Then the boat moves in again.", [(SARG, 88.0, .5)], "drive"),
  ("All three were taken to Bridge Bait Marina, in Freeport. No injuries were reported.", [(SARG, 130.0, .5), (SARG, 134.0, .5)], "calm"),
  ("Before: three people on an upside-down boat. After: a Coast Guard boat crew, and a swimmer, getting all three off it. Follow for more real rescues.", [(SARG, 140.0, .5), (SARG, 145.4, .5)], "punch"),
 ]),
 dict(id="s5", hook="TWO PEOPLE<br>[ONE HOOK]", title="The swimmer and the boater he went down for, on one hoist hook",
      lines=[
  ("Two people on one hoist hook: a Coast Guard rescue swimmer, and the boater he went down for.", [(NAHMA, 76.00, .27), (NAHMA, 78.80, .27)], "tense"),
  ("July thirteenth, twenty twenty-five. Lake Michigan, near Nahma, on Michigan's Upper Peninsula.", [(NAHMA, 32.20, .27), (NAHMA, 35.60, .27)], "calm"),
  ("A sixteen-foot boat sits at anchor. The operator is having a medical emergency.", [(NAHMA, 39.00, .27)], "tense"),
  ("Station Sturgeon Bay photographed the boat that day: a small pleasure craft, anchored on the lake.", [(NAHMA, 44.30, .27)], "calm"),
  ("A Jayhawk crew from Air Station Traverse City answers.", [(NAHMA, 49.70, .27), (NAHMA, 51.40, .27)], "drive"),
  ("They deploy their swimmer, Petty Officer Second Class Ryan Watkins, an aviation survival technician.", [(NAHMA, 7.90, .27), (NAHMA, 11.90, .27)], "calm"),
  ("From the cabin door, he's a speck on the lake.", [(NAHMA, 14.90, .27), (NAHMA, 16.40, .27)], "slow"),
  ("Below him, the boat swings at anchor.", [(NAHMA, 24.20, .27)], "calm"),
  ("Rescue swimmers are also emergency medical technicians.", [(NAHMA, 53.10, .27), (NAHMA, 55.60, .27)], "calm"),
  ("Their course takes twenty-two weeks. Seven of E-M-T training, ten as rescue swimmers, five on survival equipment.", [(NAHMA, 1.20, .5)], "calm", dict(label="HELICOPTER CAMERA · NEAR NAHMA")),
  ("Up in the cabin, the crew watches, and waits.", [(NAHMA, 59.20, .27), (NAHMA, 63.40, .27)], "slow"),
  ("Then the hook goes down again.", [(NAHMA, 70.00, .27)], "drive"),
  ("And it comes back up with two people on it.", [(NAHMA, 81.60, .27)], "tense"),
  ("Into the helicopter.", [(NAHMA, 89.20, .27)], "calm"),
  ("The boater was flown to a nearby airport, where emergency medical services were waiting.", [(NAHMA, 92.20, .27), (NAHMA, 95.60, .27)], "calm"),
  ("One swimmer, one hook, one life. Follow for more real rescues.", [(NAHMA, 85.60, .27), (NAHMA, 17.90, .27)], "punch"),
 ]),
]

YSHORTS = [
 dict(id="y1", hook="WATCH THE<br>[WAVE]", title="A wave flipped his boat. The swimmer was already there",
      lines=[
  ("Watch the wave. A Coast Guard rescue swimmer is already in the water, off the Columbia River.", [(SANDV, 16.00, .5), (SAND, 22.40, .5)], "tense"),
  ("It rolls the boat over, and throws the man into the sea. The swimmer reaches him.", [(SAND, 25.40, .5), (SAND, 28.00, .5), (SAND, 31.00, .5)], "drive"),
  ("They go up the cable together. It was the swimmer's first life saved. Full story on our channel.", [(SANDQ, 29.4, .45), (SANDQ, 34.25, .5)], "punch"),
 ]),
 dict(id="y2", hook="A PUMP ON<br>[THE CABLE]", title="A rescue swimmer rides the cable onto a flooding boat",
      lines=[
  ("A Coast Guard rescue swimmer's own camera, and a pump coming down his cable, to a flooding boat near Galveston.", [(GALV, 40.4, .5), (GALV, 43.5, .5)], "tense"),
  ("Seven people aboard. He rode the hoist down first. Then he hauled the pump onto the deck.", [(GALV, 18.0, .5), (GALV, 21.4, .5), (GALV, 47.0, .5)], "drive"),
  ("They dewater the boat, and it's escorted into port. Full story on our channel.", [(GALV, 54.0, .5), (GALV, 75.4, .5)], "punch"),
 ]),
 dict(id="y3", hook="WEARING<br>[LIFE JACKETS]", title="They wore life jackets. Watch the rescue basket",
      lines=[
  ("Three people in Lake Michigan, holding on to their capsized boat.", [(STURG, 9.2, .5), (STURG, 12.4, .5)], "tense"),
  ("A Coast Guard swimmer goes down, and the basket brings them up, one at a time.", [(STURG, 0.50, .5), (STURG, 17.50, .5), (STURG, 31.40, .5)], "drive"),
  ("The Coast Guard thanked all three for wearing life jackets. It made them easier to find. Full story on our channel.", [(STURG, 73.00, .5), (STURG, 45.00, .5)], "punch"),
 ]),
]

DISPLAY = [
 ("February third, twenty twenty-three", "February 3, 2023"), ("thirty-five-foot", "35-foot"), ("channel sixteen", "Channel 16"), ("Twenty-foot", "20-foot"),
 ("January seventeenth, twenty twenty-six", "January 17, 2026"), ("forty-foot", "40-foot"), ("twenty-two weeks", "22 weeks"), ("E-M-Ts", "EMTs"), ("E-M-T", "EMT"),
 ("July twenty-eighth, twenty twenty-five", "July 28, 2025"), ("One twenty-seven", "1:27"), ("sixteen-foot", "16-foot"),
 ("September thirteenth, twenty twenty-five", "September 13, 2025"), ("eleven-oh-three", "11:03"), ("seventeen-foot", "17-foot"), ("twenty-nine-foot", "29-foot"),
 ("July thirteenth, twenty twenty-five", "July 13, 2025"), ("Saint Ignace", "St. Ignace"), ("M-H sixty-five", "MH-65"),
]
CTA = "FOLLOW FOR MORE REAL RESCUES"
YCTA = "FULL STORY ON OUR CHANNEL"
