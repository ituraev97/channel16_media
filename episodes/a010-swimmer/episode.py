# CHANNEL 16 · ANATOMY OF A RESCUE 010 — The Rescue Swimmer (what a Coast Guard rescue swimmer does, from the jump to the hoist, 6 real cases)
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (location/date lower third), kind (narration direction: calm|punch|tense|slow|drive|question)
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

SAND = 909520       # Sandpiper capsized by a breaking wave, ~6 mi W of the Columbia River mouth, Feb 3, 2023 — vertical phone video from the AHRS Jayhawk (PO1 Kyle Turcotte)
SANDM = 872430      # same rescue, multi-unit compilation (PO2 Michael Clark): 0–7.1 s motor lifeboat view (full frame)
SANDQ = "872430q"   # same file, 4:3 parts: 7.2–10.6 swimmer lowered; 26.7–39.5 swimmer + survivor hoisted, cabin
JUMP = 1028863      # Air Station Borinquen rescue swimmer deploys from an MH-60T, TRAINING near Mona Island, P.R., Nov 5, 2026 (cabin + swimmer camera; PO3 Jessica Walker)
STURG = 971965      # Air Station Traverse City MH-60 rescues 3 from a capsized 16-ft boat, Sturgeon Bay, Mich., July 28, 2025 (courtesy)
NAHMA = 970021      # Air Station Traverse City MH-60 deploys AST2 Ryan Watkins, vessel operator with a medical emergency near Nahma, Mich., July 13, 2025 (courtesy)
SARG = 976930       # Air Station Houston swimmer helps 3 boaters from a capsized vessel onto a Station Freeport boat, off Sargent, Texas, Sep 13, 2025 (vertical, courtesy)
GALV = 993525       # Air Station Houston MH-65 swimmer + pump, 40-ft Sea Ray with 7 aboard taking on water near Galveston, Jan 17, 2026 (swimmer camera, courtesy)
PJ = 987403         # AHRS rescue swimmers train in surf with Air Force PJs at Fort Stevens, Ore., Nov 19, 2025 (PO? Thomas Molloy) — black helicopters are Air Force HH-60s
AHRS = 1006811      # Advanced Helicopter Rescue School, Astoria, Ore., Feb 2026 (Coast Guard Video Production Team: PO2 Ryan Schultz, PO2 Jose Hernandez, Erik Villa Rodriguez)

COL = [[-124.75, 46.62], [-123.55, 45.95]]      # Columbia River mouth
ASTORIA = [-123.83, 46.19]; CAPED = [-124.05, 46.28]; SANDP = [-124.20, 46.25]
MI = [[-87.4, 46.35], [-84.2, 44.55]]           # northern Lake Michigan
STURGEON = [-84.98, 45.71]; PELLSTON = [-84.79, 45.57]; STIGNACE = [-84.73, 45.87]; TRAVERSE = [-85.58, 44.74]; NAHMA_LL = [-86.66, 45.84]

LINES = [
 # ---------------- COLD OPEN (Sandpiper, Columbia River) ----------------
 ("February third, twenty twenty-three. About six miles off the mouth of the Columbia River, a thirty-five-foot boat is taking on water, in twenty-foot seas.",
  [C(SAND, 0.3), C(SAND, 4.7)], dict(tag=("OFF THE COLUMBIA RIVER BAR", "FEB 3, 2023"), kind="tense")),
 ("At ten that morning, the Coast Guard had heard a mayday on channel sixteen. Just the mayday. No other details. Watchstanders estimated his position by triangulating the radio signal.",
  [G("callcard", kicker="COAST GUARD SECTOR COLUMBIA RIVER · FEB 3, 2023", title="SANDPIPER",
     rows=[["10:00 A.M.", "MAYDAY · VHF CHANNEL 16"], ["DETAILS", "NONE GIVEN"], ["POSITION", "ESTIMATED BY RADIO TRIANGULATION"], ["ABOARD", "ONE MARINER"]])], dict(kind="calm")),
 ("By about ten forty, a Jayhawk crew is overhead. Their rescue swimmer goes down the cable, into the sea.",
  [C(SANDQ, 7.4), C(SAND, 9.1)], dict(kind="tense")),
 ("A lifeboat crew from Station Cape Disappointment is coming. So are crews from the National Motor Lifeboat School, who were training nearby. But only the helicopter can put a swimmer in the water, right next to the boat.",
  [C(SANDM, 0.05), C(SANDM, 3.5), C(SAND, 12.3)], dict(kind="drive")),
 ("He swims toward the boat.",
  [C(SAND, 16.2)], dict(kind="calm")),
 ("And then, this.",
  [C(SAND, 21.6)], dict(kind="punch")),
 ("A breaking wave rolls the boat over, and throws the man into the water.",
  [C(SAND, 23.6), C(SAND, 26.6)], dict(kind="tense")),
 ("The swimmer is already in the water. He reaches him, and they go up the cable, together.",
  [C(SAND, 30.0), C(SANDQ, 27.0), C(SANDQ, 30.4)], dict(kind="drive")),
 ("So what does a Coast Guard rescue swimmer actually do, when everything goes wrong at once?",
  [C(SANDQ, 34.3)], dict(kind="question")),
 ("This is the anatomy of the job, in five real rescues. The jump, the swim, the hoist, the swimmer who stays behind, and the school where they train for the worst.",
  [G("title", title="Rescue<br><span style=\"color:#FF5B14\">swimmer</span>", sub="ANATOMY OF A RESCUE · 010", size=240)], dict(kind="slow", gap=2.6)),

 # ---------------- I. THE JOB ----------------
 ("First, who they are.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="I", t="THE JOB")], dict(kind="calm")),
 ("In the Coast Guard, rescue swimmers are aviation survival technicians. A-S-Ts. They fly on Coast Guard helicopters, into sea rescues, floods, and cliff rescues.",
  [C(AHRS, 334.0), C(AHRS, 305.3), C(AHRS, 262.4)], dict(tag=("ASTORIA, OREGON", "TRAINING · FEB 2026"), kind="calm")),
 ("They're usually assigned to Coast Guard air stations. Between rescues, they also maintain aviation survival equipment.",
  [C(AHRS, 250.1), C(AHRS, 132.9)], dict(kind="calm")),
 ("They're also emergency medical technicians. The rating course takes twenty-two weeks: seven weeks of E-M-T training, ten weeks of rescue swimmer training, and five weeks on life-support equipment.",
  [G("steps", kicker="AVIATION SURVIVAL TECHNICIAN", title="22 WEEKS TO THE RATING",
     items=[["EMT", "7 weeks · national registry"], ["Swimmer", "10 weeks · rescue swimmer course"], ["Life support", "5 weeks · equipment"], ["Air station", "Assigned to a crew"]], active=1,
     footer="SOURCE: GOCOASTGUARD.COM")], dict(kind="calm")),
 ("And it's hard to get through. In twenty twenty-two, a class finished rescue swimmer training with three out of four students passing. The Coast Guard called that a historically high success rate.",
  [G("stat", a="75%", b="FINISHED RESCUE SWIMMER TRAINING", c="ONE CLASS, 2022 · A \"HISTORICALLY HIGH\" RATE · SOURCE: U.S. COAST GUARD")], dict(kind="drive")),
 ("That year, the commanding officer of Training Center Petaluma, where the class trained after a facilities problem closed the pool in Elizabeth City, North Carolina, put the stakes this way:",
  [G("quote", q="The Coast Guard has a critical shortage of aviation survival technicians throughout the enterprise.", w="CAPT. MATTHEW CHONG · TRAINING CENTER PETALUMA · AUG. 2022")], dict(kind="slow", gap=0.8)),
 ("The Coast Guard's own careers page puts it plainly:",
  [G("quote", q="AST tasks require the highest degree of physical fitness.", w="U.S. COAST GUARD · GOCOASTGUARD.COM")], dict(kind="slow", gap=1.2)),

 # ---------------- II. THE JUMP (Borinquen, training) ----------------
 ("Every rescue starts the same way. The swimmer has to get into the water.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="II", t="THE JUMP")], dict(kind="calm")),
 ("This is training near Mona Island, Puerto Rico, on November fifth, twenty twenty-six. The helicopter is a Jayhawk from Air Station Borinken. Then, the swimmer\'s own camera.",
  [C(JUMP, 1.0), C(JUMP, 5.0)], dict(tag=("NEAR MONA ISLAND, PUERTO RICO", "TRAINING · NOV 5, 2026"), kind="calm")),
 ("Fins first. Out the door.",
  [C(JUMP, 7.4)], dict(kind="punch")),
 ("Then, the water.",
  [C(JUMP, 13.45)], dict(kind="slow")),
 ("From the surface, he signals the crew above. And the hoist hook comes down to him.",
  [C(JUMP, 16.0), C(JUMP, 23.0), C(JUMP, 35.0)], dict(kind="calm")),
 ("He clips in, and rides the cable back up to the door.",
  [C(JUMP, 42.0), C(JUMP, 55.0)], dict(kind="drive")),
 ("Look at the sea below him. The rotor wash pushes the water out in rings, around the swimmer on the cable.",
  [C(JUMP, 63.0), C(JUMP, 66.5)], dict(kind="slow")),
 ("The Jayhawk's powered rescue hoist raises and lowers rescue swimmers, survivors, and rescue equipment. Training, and the real thing.",
  [C(JUMP, 72.5), C(JUMP, 78.0), C(JUMP, 84.0)], dict(kind="calm", gap=0.8)),

 # ---------------- III. THE SWIM (Sturgeon Bay) ----------------
 ("Once he's in the water, the swimmer works for the people who can't get out on their own.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="III", t="THE SWIM")], dict(kind="calm")),
 ("July twenty-eighth, twenty twenty-five. One twenty-seven in the afternoon. The Coast Guard gets a report: a sixteen-foot boat has capsized in Sturgeon Bay, Michigan, on Lake Michigan.",
  [G("callcard", kicker="COAST GUARD SECTOR NORTHERN GREAT LAKES · JULY 28, 2025", title="CAPSIZED · 16-FT BOAT",
     rows=[["MON 13:27", "REPORT OF A CAPSIZED VESSEL"], ["WHERE", "STURGEON BAY, MICH. · LAKE MICHIGAN"], ["IN THE WATER", "THREE PEOPLE"], ["LIFE JACKETS", "ALL THREE WEARING THEM"]])], dict(kind="tense")),
 ("The sector puts out an urgent marine information broadcast, launches a small boat from Station Saint Ignace, and diverts a Jayhawk crew from Air Station Traverse City.",
  [G("steps", kicker="SECTOR NORTHERN GREAT LAKES · JULY 28, 2025", title="THE RESPONSE",
     items=[["Broadcast", "Urgent marine information"], ["Boat", "Station St. Ignace"], ["Jayhawk", "Air Station Traverse City"], ["EMS", "Waiting at Pellston"]], active=2,
     footer="SOURCE: U.S. COAST GUARD")], dict(kind="drive")),
 ("The swimmer goes down first.",
  [C(STURG, 0.4), C(STURG, 3.4)], dict(tag=("STURGEON BAY, MICHIGAN", "JULY 28, 2025"), kind="tense")),
 ("Through the helicopter's camera: three people, holding on to their overturned boat.",
  [C(STURG, 7.9), C(STURG, 12.0)], dict(kind="calm")),
 ("Then the rescue basket goes down. And comes back up, with a survivor inside.",
  [C(STURG, 17.4), C(STURG, 32.0)], dict(kind="drive")),
 ("In the cabin, the crew pulls each one aboard.",
  [C(STURG, 38.0), C(STURG, 50.0)], dict(kind="calm")),
 ("Three times. And last, the swimmer himself.",
  [C(STURG, 72.4), C(STURG, 79.0)], dict(kind="drive")),
 ("Down on the lake, the Station Saint Ignace boat crew checked the scene. No pollution, no debris, no hazard to other boats.",
  [C(STURG, 22.6)], dict(kind="calm")),
 ("All three were flown to Pellston Airport, where emergency medical services were waiting. Afterward, the air station said this:",
  [C(STURG, 84.0), C(STURG, 91.0)], dict(kind="calm")),
 ("Thanks to the survivors for wearing life jackets, which made locating and rescuing them far more efficient, the crews were able to save three lives today.",
  [G("quote", q="Thanks to the survivors for wearing life jackets—which made locating and rescuing them far more efficient…", w="LT. J.G. NICHOLAS BETTS · AIR STATION TRAVERSE CITY")], dict(kind="slow", gap=1.0)),

 # ---------------- IV. THE HOIST (Nahma) ----------------
 ("Fifteen days earlier, the same air station got a different kind of call.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="IV", t="THE HOIST")], dict(kind="calm")),
 ("July thirteenth, twenty twenty-five. Near Nahma, on Michigan's Upper Peninsula, a boat's operator is having a medical emergency.",
  [G("callcard", kicker="AIR STATION TRAVERSE CITY · JULY 13, 2025", title="MEDICAL EMERGENCY",
     rows=[["WHERE", "NEAR NAHMA, MICH. · LAKE MICHIGAN"], ["BOAT", "16-FT PLEASURE CRAFT, AT ANCHOR"], ["PATIENT", "THE OPERATOR"], ["SENT", "MH-60 JAYHAWK · RESCUE SWIMMER"]])], dict(kind="calm")),
 ("A Traverse City Jayhawk deploys its swimmer, Petty Officer Second Class Ryan Watkins.",
  [C(NAHMA, 8.0), C(NAHMA, 9.8)], dict(tag=("NEAR NAHMA, MICHIGAN", "JULY 13, 2025"), kind="drive")),
 ("From the cabin door, he becomes a speck on the lake.",
  [C(NAHMA, 12.5), C(NAHMA, 19.0)], dict(kind="slow")),
 ("Below him, the boat drifts on the open water.",
  [C(NAHMA, 33.0), C(NAHMA, 45.0), C(NAHMA, 55.0)], dict(kind="calm")),
 ("Then the cable comes back up. Two people on one hook. The swimmer, and the survivor.",
  [C(NAHMA, 76.0), C(NAHMA, 79.0)], dict(kind="tense")),
 ("Into the helicopter. The survivor was flown to a nearby airport, where emergency medical services were waiting.",
  [C(NAHMA, 89.5), C(NAHMA, 93.5)], dict(kind="calm", gap=0.8)),

 # ---------------- V. STAYING BEHIND (Sargent + Galveston) ----------------
 ("But the swimmer doesn't always come back up with the survivors.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="V", t="STAYING BEHIND")], dict(kind="calm")),
 ("September thirteenth, twenty twenty-five, off Sargent, Texas. A seventeen-foot boat has capsized, with two adults and an adolescent aboard.",
  [C(SARG, 1.3), C(SARG, 7.45)], dict(tag=("OFF SARGENT, TEXAS", "SEPT 13, 2025"), kind="calm")),
 ("The report reaches Sector Houston-Galveston at eleven-oh-three that Saturday morning. Watchstanders broadcast an urgent marine information alert, and launch two crews: a helicopter, and a boat.",
  [G("callcard", kicker="SECTOR HOUSTON-GALVESTON · SEPT 13, 2025", title="CAPSIZED · 17-FT BOAT",
     rows=[["SAT 11:03", "REPORT OF A CAPSIZED BOAT"], ["ABOARD", "TWO ADULTS, ONE ADOLESCENT"], ["AIR", "MH-65 · AIR STATION HOUSTON"], ["SEA", "29-FT BOAT · STATION FREEPORT"]])], dict(kind="calm")),
 ("The crews find all three sitting on the overturned hull. A Dolphin from Air Station Houston lowers its swimmer.",
  [C(SARG, 12.0), C(SARG, 16.5)], dict(kind="tense")),
 ("A twenty-nine-foot boat from Station Freeport is on scene too. So the swimmer helps the three of them onto the Coast Guard boat.",
  [C(SARG, 36.0), C(SARG, 44.0), C(SARG, 52.0)], dict(kind="drive")),
 ("No hoist this time. All three were taken to Bridge Bait Marina in Freeport. No injuries were reported.",
  [C(SARG, 90.0), C(SARG, 143.3)], dict(kind="calm", gap=0.6)),
 ("And sometimes, the swimmer's job is to save the boat.",
  [C(GALV, 3.0)], dict(kind="punch")),
 ("January seventeenth, twenty twenty-six, near Galveston. A forty-foot Sea Ray, with seven people aboard, is taking on water. This is the swimmer's camera.",
  [G("callcard", kicker="AIR STATION HOUSTON · JAN 17, 2026", title="40-FT SEA RAY",
     rows=[["WHERE", "NEAR GALVESTON, TEXAS"], ["ABOARD", "SEVEN PEOPLE"], ["PROBLEM", "TAKING ON WATER"], ["SENT", "MH-65 DOLPHIN · SWIMMER · PUMP"]]), C(GALV, 8.0)], dict(kind="tense")),
 ("He rides the hoist down, under the Dolphin.",
  [C(GALV, 16.5), C(GALV, 21.0)], dict(tag=("NEAR GALVESTON, TEXAS", "JAN 17, 2026"), kind="drive")),
 ("And onto the boat.",
  [C(GALV, 26.5)], dict(kind="calm")),
 ("Then the helicopter sends down a second piece of help, on the same cable. A pump.",
  [C(GALV, 40.3), C(GALV, 44.5)], dict(kind="tense")),
 ("The swimmer hauls it in, and they start dewatering the boat.",
  [C(GALV, 50.6), C(GALV, 55.0)], dict(kind="drive")),
 ("A boat crew from Station Galveston arrives. And the Sea Ray, with all seven aboard, is escorted safely into port.",
  [C(GALV, 71.5), C(GALV, 79.0), C(GALV, 93.0)], dict(kind="calm", gap=0.8)),

 # ---------------- VI. THE SCHOOL (AHRS) ----------------
 ("Remember the swimmer at the start, off the Columbia River?",
  [G("chapter", case="ANATOMY OF A RESCUE", n="VI", t="THE SCHOOL")], dict(kind="question")),
 ("His name is Branch Walton, Aviation Survival Technician Third Class. That day, he and his crew were students, at the Coast Guard's Advanced Helicopter Rescue School in Astoria, Oregon.",
  [C(AHRS, 99.1), C(AHRS, 122.3), C(AHRS, 168.9)], dict(tag=("ASTORIA, OREGON", "AHRS TRAINING · FEB 2026"), kind="calm")),
 ("Their rescue was his first life saved. The mariner was taken to Air Station Astoria, and was stable when he was handed over to emergency medical personnel.",
  [G("stat", a="STABLE", b="AT AIR STATION ASTORIA", c="MINOR INJURIES · HANDED TO EMERGENCY MEDICAL PERSONNEL · SOURCE: U.S. COAST GUARD")], dict(kind="calm")),
 ("Hours later, the class graduated.",
  [G("stat", a="1ST", b="LIFE SAVED · HOURS BEFORE GRADUATION", c="AST3 BRANCH WALTON · FEB 3, 2023 · SOURCE: U.S. COAST GUARD")], dict(kind="punch")),
 ("The school sits at the mouth of the Columbia, in waters known as the Graveyard of the Pacific. Trainees there describe the waves, consistently ten to fifteen feet, as some of the biggest swells in the country.",
  [G("map", map=dict(bounds=COL, rings=[dict(ll=SANDP, r=36, n=3, d=0.3)],
     cities=[dict(ll=SANDP, name="SANDPIPER", sub="~6 MI W OF THE RIVER MOUTH", d=0.3, color="#FF5B14", anchor="end", dy=-40),
             dict(ll=ASTORIA, name="ASTORIA", sub="AIR STATION · AHRS", d=0.6, size=28, dy=40), dict(ll=CAPED, name="STATION CAPE DISAPPOINTMENT", d=0.8, size=24, anchor="start", dy=-40)]),
     kicker="\"THE GRAVEYARD OF THE PACIFIC\"", title="THE COLUMBIA RIVER BAR", footer="POSITION ILLUSTRATIVE")], dict(kind="calm")),
 ("They train in heavy surf. On cliffs, rappelling from a hovering helicopter. And inside sea caves, where currents and seas build up around the swimmer.",
  [C(AHRS, 337.6), C(AHRS, 367.0), C(AHRS, 208.0), C(AHRS, 214.2)], dict(kind="drive")),
 ("The school also trains with other services. In November twenty twenty-five, its rescue swimmers worked the surf at Fort Stevens State Park, alongside Air Force pararescue jumpers.",
  [C(PJ, 16.3), C(PJ, 20.3), C(PJ, 25.0)], dict(tag=("FORT STEVENS STATE PARK, ORE.", "TRAINING · NOV 19, 2025"), kind="calm")),
 ("Rescue swimmers founded the school about thirty years ago. Each class has about sixteen students: eight rescue swimmers, four flight mechanics, and four pilots. Swimmers must attend within three years of finishing their A-School, and come back at regular intervals.",
  [G("stat", a="16", b="STUDENTS PER CLASS", c="8 RESCUE SWIMMERS · 4 FLIGHT MECHANICS · 4 PILOTS · SOURCE: U.S. COAST GUARD, MAY 2026")], dict(kind="calm")),
 ("An instructor there, Lieutenant Commander Danielle Benedetto, describes the daily work:",
  [C(AHRS, 37.9), C(AHRS, 225.9)], dict(kind="calm")),
 ("Each day, you have to learn how to analyze the hazards, mitigate those risks, and work as a team to get the mission done.",
  [G("quote", q="Each day, you have to learn how to analyze the hazards, mitigate those risks, and work as a team to get the mission done.", w="LT. CMDR. DANIELLE BENEDETTO · INSTRUCTOR · ADVANCED HELICOPTER RESCUE SCHOOL")], dict(kind="slow", gap=1.0)),

 # ---------------- WHAT IT TAKES ----------------
 ("So, five rescues, and one more call. What did they have in common?",
  [G("steps", kicker="FIVE RESCUES · ONE CALL", title="WHAT THE SWIMMER NEEDED",
     items=[["A call", "Mayday on channel 16"], ["Life jackets", "Easier to find"], ["Stay with it", "On the hull"], ["A crew", "Trained for it"]])], dict(kind="question")),
 ("First, someone called for help. Off the Columbia River, a mayday with no position was still enough to find him.",
  [C(SAND, 1.5)], dict(kind="calm")),
 ("And in September twenty twenty-six, a kayaker capsized near Parker Reef, in Washington's San Juan Islands. He kept his radio working in the water, and called a mayday on channel sixteen. A boat crew from Station Bellingham pulled him out.",
  [G("callcard", kicker="SECTOR PUGET SOUND · SEPT. 2026", title="CAPSIZED KAYAKER",
     rows=[["CALL", "\"MAYDAY, THIS IS A CAPSIZED KAYAKER…\""], ["RADIO", "VHF CHANNEL 16"], ["WATER", "54°F · DRY SUIT · LIFE JACKET"], ["RESCUE", "45-FT BOAT · STATION BELLINGHAM"]], footer="SOURCE: MYNORTHWEST / U.S. COAST GUARD")], dict(kind="calm")),
 ("As the Coast Guard's duty officer put it:",
  [G("quote", q="In cold water, every single second counts.", w="LT. ALLISON RUTH · COMMAND DUTY OFFICER · SECTOR PUGET SOUND")], dict(kind="slow", gap=0.8)),
 ("Second, life jackets. On Lake Michigan, the Coast Guard said they made three people easier to find, and to rescue.",
  [C(STURG, 59.0), C(STURG, 63.0)], dict(kind="calm")),
 ("Third, staying with the boat. Off Sargent, the crews found all three sitting on their overturned hull.",
  [C(SARG, 62.0)], dict(kind="calm")),
 ("And last, a crew that had trained for the worst day of someone else's life. Then, a swimmer went into the water first.",
  [C(AHRS, 374.2), C(AHRS, 399.5)], dict(kind="slow", gap=0.8)),
 ("Next time, on Channel Sixteen: another real rescue, from the first call to the hoist. Stay safe out there.",
  [G("end", stamp="ALWAYS READY")], dict(kind="calm", gap=2.4)),
]

DISPLAY = [
 ("February third, twenty twenty-three", "February 3, 2023"), ("six miles", "6 miles"), ("thirty-five-foot", "35-foot"), ("twenty-foot", "20-foot"),
 ("channel sixteen", "Channel 16"), ("Saint Ignace", "St. Ignace"), ("A-S-Ts", "ASTs"), ("twenty-two weeks", "22 weeks"), ("seven weeks", "7 weeks"), ("E-M-T", "EMT"),
 ("ten weeks", "10 weeks"), ("five weeks", "5 weeks"), ("twenty twenty-two", "2022"), ("November fifth, twenty twenty-six", "November 5, 2026"), ("Borinken", "Borinquen"),
 ("July twenty-eighth, twenty twenty-five", "July 28, 2025"), ("One twenty-seven", "1:27"), ("sixteen-foot", "16-foot"),
 ("July thirteenth, twenty twenty-five", "July 13, 2025"), ("September thirteenth, twenty twenty-five", "September 13, 2025"), ("seventeen-foot", "17-foot"),
 ("twenty-nine-foot", "29-foot"), ("January seventeenth, twenty twenty-six", "January 17, 2026"), ("forty-foot", "40-foot"),
 ("ten to fifteen feet", "10 to 15 feet"), ("eleven-oh-three", "11:03"), ("thirty years", "30 years"), ("November twenty twenty-five", "November 2025"), ("ten forty", "10:40"), ("September twenty twenty-six", "September 2026"), ("sixteen students", "16 students"), ("Channel Sixteen", "Channel 16"),
]

META = dict(
    case="ANATOMY OF A RESCUE · 010", label="CH 16 · 156.800 MHz",
    title="What a Coast Guard Rescue Swimmer Actually Does, in 5 Real Rescues",
    voice="am_eric",
    credit=("Footage: U.S. Coast Guard via DVIDS (public domain). Appearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NCHANNEL 16 is an independent channel, not affiliated with the U.S. Coast Guard."),
)
