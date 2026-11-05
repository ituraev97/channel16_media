# CHANNEL 16 · ANATOMY OF A RESCUE 007 — Medevac at Sea (how a Coast Guard medical evacuation from a ship works, 6 real cases)
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (location/date lower third), kind (narration direction: calm|punch|tense|slow|drive|question)
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

CHIPOL = 984907   # Air Station Barbers Point MH-65 hoists the master of the Hong Kong-flagged cargo ship Chipol Donghai, 57 mi off Oahu, Oct 8, 2025 (night hoist camera)
STILL = 1010820   # Air Station Clearwater helicopter crew, 56-year-old from a fishing vessel 92 mi off Brunswick, Ga., June 12, 2026 (vertical phone video)
SOL = 1003800     # Air Station Barbers Point MH-65, Celebrity Solstice passenger 58 mi off Oahu, Apr 23, 2026 (night hoist camera)
SOLI = 1006503    # same mission, with crew interviews (PO3 Avery Tibbets)
VIKING = 998677   # Air Station Barbers Point MH-65 refuels on USCGC Harriet Lane, then hoists a 37-year-old from the cargo ship Viking Emerald ~100 mi off Kauai, Mar 3, 2026 (CPO Corinne Zilnicki, PO2 Tyler Robertson)
LUM = 1015431     # Air Station Humboldt Bay MH-65, 51-year-old woman from the Carnival Luminosa 45 mi off Humboldt Bay, July 16, 2026
SAIL = 986213     # Air Station Astoria MH-60, mariner from a sailing vessel via a Station Tillamook Bay 47-ft motor lifeboat, 19 mi SW of Tillamook Bay, Nov 5, 2025 (Lt. Christopher Butters)

HI = [[-162.6, 23.4], [-155.6, 18.0]]           # Hawaiian Islands
HIW = [[-162.6, 23.6], [-146.3, 12.2]]          # Hawaii + ocean to the southeast
NPAC = [[-171.0, 46.5], [-145.0, 17.0]]         # North Pacific, Oahu -> 1,500 mi north
OAHU = [-157.98, 21.47]; BARBERS = [-158.07, 21.30]; HONOLULU = [-157.86, 21.31]; KAUAI = [-159.53, 22.06]
CHIPOL_FAR = [-158.0, 43.0]; CHIPOL_NEAR = [-158.0, 22.30]
SOL_FAR = [-161.0, 18.45]; SOL_NEAR = [-158.70, 20.75]
VIK = [-161.05, 22.70]
HILO = [-155.07, 19.72]; OG_FAR = [-149.6, 13.2]; OG_NEAR = [-153.9, 18.9]
GA = [[-83.0, 33.3], [-76.8, 30.2]]             # Georgia / South Carolina coast
BRUNSWICK = [-81.49, 31.15]; SSI = [-81.39, 31.25]; CHARLESTON = [-79.93, 32.78]; STILL_P = [-79.92, 31.10]; SAVANNAH = [-81.10, 32.08]
NCAL = [[-126.6, 41.7], [-122.4, 38.9]]         # Humboldt Bay -> Fort Bragg
EUREKA = [-124.16, 40.80]; FORTBRAGG = [-123.80, 39.45]; LUM_P = [-125.10, 40.75]
ORE = [[-125.6, 46.45], [-122.9, 44.95]]        # Tillamook Bay / Astoria
TILLAMOOK = [-123.94, 45.56]; ASTORIA = [-123.88, 46.16]; SAIL_P = [-124.22, 45.35]

LINES = [
 # ---------------- COLD OPEN (Chipol Donghai) ----------------
 ("October, twenty twenty-five. Late on a Sunday night, an email reaches the Coast Guard's rescue center in Honolulu.",
  [G("stat", a="SUNDAY", b="LATE NIGHT · AN EMAIL FROM THE NORTH PACIFIC", c="TO THE JOINT RESCUE COORDINATION CENTER, HONOLULU · OCTOBER 2025")], dict(kind="calm")),
 ("It comes from a six-hundred-sixteen-foot cargo ship, the Chipol Donghai. The ship's master, the man in command, has severe chest pains.",
  [G("callcard", kicker="JOINT RESCUE COORDINATION CENTER HONOLULU", title="CHIPOL DONGHAI",
     rows=[["SUNDAY", "~11 P.M. · EMAIL FROM THE SHIP"], ["VESSEL", "616-FT CARGO SHIP · HONG KONG FLAG"], ["PATIENT", "THE MASTER · SEVERE CHEST PAINS"], ["POSITION", "~1,500 MI NORTH OF OAHU"]])], dict(kind="tense")),
 ("And the ship is about fifteen hundred miles north of Oahu. Far too far for a rescue helicopter.",
  [G("map", map=dict(bounds=NPAC, rings=[dict(ll=CHIPOL_FAR, r=40, n=3, d=0.3)],
     cities=[dict(ll=CHIPOL_FAR, name="CHIPOL DONGHAI", sub="~1,500 MI N OF OAHU · POSITION ILLUSTRATIVE", d=0.3, color="#FF5B14"), dict(ll=OAHU, name="OAHU", d=0.7, size=30)]),
     kicker="NORTH PACIFIC · OCTOBER 2025", title="1,500 MILES OUT")], dict(kind="slow")),
 ("Three days later, on Wednesday night, at eight fifty-three, a Coast Guard helicopter is hovering over that ship's deck.",
  [C(CHIPOL, 2), C(CHIPOL, 10), C(CHIPOL, 22)], dict(tag=("57 MI OFF OAHU, HAWAII", "OCT 8, 2025"), kind="drive")),
 ("So how does a man fifteen hundred miles out at sea end up in a hospital in Honolulu?",
  [C(CHIPOL, 27.5), C(CHIPOL, 46)], dict(kind="question", gap=0.6)),
 ("This is how a medical evacuation at sea works. Six real cases: a fishing boat, two cruise ships, a cargo ship, a sailboat in heavy seas, and the Chipol Donghai.",
  [G("title", title="Medevac<br><span style=\"color:#FF5B14\">at sea</span>", sub="ANATOMY OF A RESCUE · 007", size=240)], dict(kind="slow", gap=2.6)),

 # ---------------- I. THE DOCTOR (Still Fishing) ----------------
 ("It starts with a call. And, before anyone takes off, a doctor.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="I", t="THE DOCTOR")], dict(kind="calm")),
 ("June twelfth, twenty twenty-six. The Still Fishing, a forty-four-foot fishing boat, is about ninety-two miles off Brunswick, Georgia. A fifty-six-year-old man aboard is sick.",
  [G("map", map=dict(bounds=GA, rings=[dict(ll=STILL_P, r=40, n=3, d=0.3)],
     cities=[dict(ll=STILL_P, name="STILL FISHING", sub="~92 MI OFF BRUNSWICK", d=0.3, color="#FF5B14", dy=-60),
             dict(ll=BRUNSWICK, name="BRUNSWICK", d=0.6, size=28, anchor="end", dy=40), dict(ll=CHARLESTON, name="SECTOR CHARLESTON", d=0.8, size=28, anchor="end")]),
     kicker="JUNE 12, 2026", title="OFF THE GEORGIA COAST", footer="POSITION ILLUSTRATIVE")], dict(kind="calm")),
 ("The boat's operator reports it to the Coast Guard. The man has gastrointestinal symptoms.",
  [G("callcard", kicker="COAST GUARD SECTOR CHARLESTON · JUNE 12, 2026", title="STILL FISHING",
     rows=[["VESSEL", "44-FT FISHING BOAT"], ["POSITION", "~92 MI OFF BRUNSWICK, GA."], ["PATIENT", "56-YEAR-OLD MAN"], ["REPORT", "GASTROINTESTINAL SYMPTOMS"]])], dict(kind="calm")),
 ("Here's the part most people never see. The watchstanders don't decide on their own whether a sick mariner needs a helicopter. They consult the duty flight surgeon.",
  [C(STILL, 3.3), C(STILL, 8.15), C(STILL, 47.7)], dict(tag=("92 MI OFF BRUNSWICK, GEORGIA", "JUNE 12, 2026"), kind="drive")),
 ("On a cruise ship, the ship's own doctors make the first call. Then the flight surgeon talks with them, works out the patient's condition, and how fast they need a higher level of care.",
  [G("steps", kicker="HOW A MEDEVAC IS DECIDED", title="FROM THE SHIP TO THE HELICOPTER",
     items=[["Ship", "The ship's doctor makes the first call"], ["Surgeon", "Flight surgeon assesses, recommends"], ["Coordinator", "Mission coordinator decides"], ["Aircrew", "Launches"]], active=1,
     footer="SOURCE: JUNEAU EMPIRE, 2019 · U.S. COAST GUARD")], dict(kind="calm")),
 ("The flight surgeon recommends. The final call to launch belongs to the search and rescue mission coordinator.",
  [C(STILL, 11.4), C(STILL, 26.5)], dict(kind="calm")),
 ("And the decision matters. As a senior Coast Guard medical officer put it:",
  [G("quote", q="Hoisting someone off the deck is a very risky operation.", w="CAPT. J. RUSSELL BOWMAN · SENIOR COAST GUARD MEDICAL OFFICER · JUNEAU EMPIRE, 2019")], dict(kind="slow", gap=1.6)),
 ("For the Still Fishing, the flight surgeon recommends a medevac. And because the boat is so far offshore, the job goes to an MH-60 Jayhawk from Air Station Clearwater.",
  [G("stat", a="92 MI", b="OFFSHORE · SO THE JAYHAWK GOES", c="MH-60 JAYHAWK · AIR STATION CLEARWATER · DUE TO THE DISTANCE OFFSHORE · SOURCE: USCG")], dict(kind="drive")),
 ("The rescue swimmer goes into the water, and swims to the boat.",
  [C(STILL, 17.0), C(STILL, 20.0)], dict(kind="tense")),
 ("The man is hoisted aboard, and flown to St. Simons Island Airport, where emergency medical services take over.",
  [C(STILL, 56.3), C(STILL, 51.3)], dict(kind="calm", gap=0.8)),

 # ---------------- II. THE DISTANCE (Celebrity Solstice) ----------------
 ("But what if the ship is too far away for any helicopter?",
  [G("chapter", case="ANATOMY OF A RESCUE", n="II", t="THE DISTANCE")], dict(kind="question")),
 ("In Hawaii, these medevacs are flown by the MH-65 Dolphin. The Coast Guard calls it a short-range recovery helicopter. It can stay in the air for about three hours.",
  [G("stat", a="3 HRS", b="MH-65 DOLPHIN · ENDURANCE", c="THE COAST GUARD'S SHORT-RANGE RECOVERY HELICOPTER · SOURCE: USCG")], dict(kind="calm")),
 ("So often, the answer is to bring the patient closer.",
  [C(SOLI, 19), C(SOLI, 24)], dict(kind="punch")),
 ("April twenty-second, twenty twenty-six. Three nineteen in the afternoon. The cruise ship Celebrity Solstice is two hundred seventy-six miles southwest of Oahu. A seventy-eight-year-old passenger has a serious medical condition.",
  [G("callcard", kicker="JOINT RESCUE COORDINATION CENTER HONOLULU · APRIL 22, 2026", title="CELEBRITY SOLSTICE",
     rows=[["WED 15:19", "MEDEVAC REQUEST"], ["POSITION", "276 MI SW OF OAHU"], ["PATIENT", "78-YEAR-OLD PASSENGER"], ["DOCTOR", "FLIGHT SURGEON RECOMMENDS A MEDEVAC"]])], dict(kind="calm")),
 ("The flight surgeon recommends a medevac. The watchstanders stay in regular contact with the ship's crew. And the ship heads toward Oahu.",
  [G("map", map=dict(bounds=HI, arcs=[dict(**{"from": SOL_FAR, "to": SOL_NEAR}, d=0.5, dur=1.4, bend=0.08, color="#FF5B14")],
     rings=[dict(ll=SOL_NEAR, r=36, n=3, d=1.6)],
     cities=[dict(ll=SOL_FAR, name="276 MI SW", sub="POSITION ILLUSTRATIVE", d=0.3, color="#FF5B14", anchor="end", dy=40), dict(ll=SOL_NEAR, name="58 MI OFF OAHU", d=1.7, color="#FFC93C", anchor="end", dy=-50),
             dict(ll=BARBERS, name="AIR STATION BARBERS POINT", d=0.8, size=26, dy=40), dict(ll=KAUAI, name="KAUAI", d=0.9, size=26)]),
     kicker="APRIL 22–23, 2026", title="THE SHIP COMES TO THE HELICOPTER")], dict(kind="drive")),
 ("On Thursday, in the dark, about fifty-eight miles off Oahu, a Dolphin from Air Station Barbers Point is over the ship.",
  [C(SOL, 1), C(SOL, 6)], dict(tag=("58 MI OFF OAHU, HAWAII", "APR 23, 2026"), kind="drive")),
 ("The rescue swimmer goes down to the deck.",
  [C(SOL, 12), C(SOL, 16)], dict(kind="tense")),
 ("Distance offshore and darkness both make a hoist harder. So overhead, a Navy MH-60 Seahawk from Helicopter Maritime Strike Squadron Thirty-Seven provides communications, and aerial overwatch.",
  [C(SOLI, 42.5), C(SOL, 22), C(SOL, 31)], dict(kind="calm")),
 ("The Coast Guard's duty officer credited the Navy crew.",
  [G("quote", q="…helped us minimize that risk and safely complete our mission.", w="LT. TAYLOR GIBBONS · COMMAND DUTY OFFICER · COAST GUARD OCEANIA DISTRICT")], dict(kind="slow", gap=1.0)),
 ("The patient goes up in a litter.",
  [C(SOL, 46), C(SOL, 54)], dict(kind="tense")),
 ("Then the swimmer.",
  [C(SOL, 106), C(SOL, 110)], dict(kind="punch")),
 ("He was flown to Queen's Medical Center in Honolulu, reported stable.",
  [C(SOL, 86), C(SOL, 95)], dict(kind="calm", gap=0.8)),
 ("It's not the only time. In October, twenty twenty-six, a fifty-five-year-old crew member on the cargo ship Ocean Gladiator needed a medevac about five hundred forty miles southeast of Hawaii island. The request came in on a Tuesday morning. By Wednesday morning, the ship was about eighty-six miles out, and a Dolphin crew hoisted him and flew him to Hilo International Airport, for further medical care.",
  [G("map", map=dict(bounds=HIW, arcs=[dict(**{"from": OG_FAR, "to": OG_NEAR}, d=0.5, dur=1.4, bend=-0.06, color="#FF5B14")],
     rings=[dict(ll=OG_NEAR, r=36, n=3, d=1.6)],
     cities=[dict(ll=OG_FAR, name="TUE 07:50 · ~540 MI SE", sub="POSITION ILLUSTRATIVE", d=0.3, color="#FF5B14", anchor="end", dy=-50), dict(ll=OG_NEAR, name="WED 08:35 · ~86 MI OUT", d=1.7, color="#FFC93C", anchor="end", dy=50),
             dict(ll=HILO, name="HILO", d=0.8, size=28, anchor="end", dy=-30), dict(ll=OAHU, name="OAHU", d=0.9, size=26)]),
     kicker="OCEAN GLADIATOR · OCTOBER 2026", title="SAME PLAYBOOK")], dict(kind="calm")),

 # ---------------- III. THE FUEL (Viking Emerald) ----------------
 ("And when the helicopter has to go farther, it can stop for fuel. At sea.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="III", t="THE FUEL")], dict(kind="calm")),
 ("March third, twenty twenty-six. A five-hundred-forty-seven-foot cargo ship, the Viking Emerald, is about a hundred miles off Kauai. A thirty-seven-year-old man aboard has severe abdominal pain.",
  [G("map", map=dict(bounds=HI, rings=[dict(ll=VIK, r=40, n=3, d=0.3)],
     cities=[dict(ll=VIK, name="VIKING EMERALD", sub="~100 MI OFF KAUAI", d=0.3, color="#FF5B14", dy=-50), dict(ll=KAUAI, name="KAUAI", d=0.6, size=28),
             dict(ll=BARBERS, name="AIR STATION BARBERS POINT", d=0.8, size=26, dy=40)]),
     kicker="MARCH 3, 2026", title="OFF KAUAI", footer="POSITION ILLUSTRATIVE")], dict(kind="calm")),
 ("A Dolphin crew from Barbers Point heads out. But first, it takes on fuel aboard the Coast Guard cutter Harriet Lane.",
  [C(VIKING, 0.3), C(VIKING, 13)], dict(tag=("OFF KAUAI, HAWAII", "MAR 3, 2026"), kind="drive")),
 ("A medium endurance cutter, with a flight deck, out at sea.",
  [C(VIKING, 19.5), C(VIKING, 7)], dict(kind="calm")),
 ("Then it's on to the ship. A roll-on, roll-off cargo carrier, under way.",
  [C(VIKING, 28), C(VIKING, 36)], dict(kind="drive")),
 ("The swimmer goes down first.",
  [C(VIKING, 57), C(VIKING, 64)], dict(kind="tense")),
 ("On a deck this big, he's a tiny figure.",
  [C(VIKING, 72), C(VIKING, 77)], dict(kind="slow")),
 ("Then the hoist goes back down. And the man goes up.",
  [C(VIKING, 83), C(VIKING, 115), C(VIKING, 121.2)], dict(kind="drive")),
 ("Last, the swimmer, hanging below the Dolphin over the open Pacific.",
  [C(VIKING, 153.0), C(VIKING, 155.5)], dict(kind="calm", gap=0.8)),

 # ---------------- IV. THE DECK (Carnival Luminosa) ----------------
 ("A cruise ship gives the crew a different kind of deck.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="IV", t="THE DECK")], dict(kind="calm")),
 ("July sixteenth, twenty twenty-six. Five ten in the evening. A crew member on the cruise ship Carnival Luminosa asks Coast Guard Sector Humboldt Bay for a medevac. A fifty-one-year-old passenger is showing symptoms of a stroke.",
  [G("callcard", kicker="COAST GUARD SECTOR HUMBOLDT BAY · JULY 16, 2026", title="CARNIVAL LUMINOSA",
     rows=[["THU 17:10", "MEDEVAC REQUEST FROM THE SHIP"], ["POSITION", "~45 MI OFF HUMBOLDT BAY"], ["PATIENT", "51-YEAR-OLD PASSENGER"], ["SYMPTOMS", "OF A STROKE"]])], dict(kind="tense")),
 ("The ship is about forty-five miles offshore. A Dolphin crew from Air Station Humboldt Bay flies out. Local news reported waves up to ten feet, and forty-mile-an-hour winds.",
  [G("map", map=dict(bounds=NCAL, arcs=[dict(**{"from": EUREKA, "to": LUM_P}, d=0.5, dur=1.1, bend=0.1), dict(**{"from": LUM_P, "to": FORTBRAGG}, d=1.7, dur=1.1, bend=0.12, color="#FF5B14")],
     rings=[dict(ll=LUM_P, r=36, n=3, d=0.3)],
     cities=[dict(ll=LUM_P, name="CARNIVAL LUMINOSA", sub="~45 MI OFFSHORE", d=0.3, color="#FF5B14", anchor="end", dy=70), dict(ll=EUREKA, name="AIR STATION HUMBOLDT BAY", d=0.6, size=26, anchor="start", dy=-30),
             dict(ll=FORTBRAGG, name="FORT BRAGG", sub="MENDOCINO COAST HOSPITAL", d=1.9, size=28, anchor="end", dy=40)]),
     kicker="JULY 16, 2026 · WAVES TO 10 FT · 40-MPH WINDS (KRCR)", title="OFF HUMBOLDT BAY", footer="SHIP POSITION ILLUSTRATIVE")], dict(kind="drive")),
 ("This is the view from the cabin door.",
  [C(LUM, 6), C(LUM, 13)], dict(tag=("45 MI OFF HUMBOLDT BAY, CALIF.", "JULY 16, 2026"), kind="calm")),
 ("The ship has a marked spot on its deck for the hoist.",
  [C(LUM, 17.5), C(LUM, 21)], dict(kind="calm")),
 ("First down: a trail line, so the people on deck can guide what comes next.",
  [C(LUM, 24), C(LUM, 27.6)], dict(kind="calm")),
 ("Then the litter.",
  [C(LUM, 29.6)], dict(kind="punch")),
 ("The rescue swimmer and the ship's crew strap her in.",
  [C(LUM, 37.8), C(LUM, 40)], dict(kind="calm")),
 ("And she's hoisted up to the cabin door.",
  [C(LUM, 63), C(LUM, 66.5)], dict(kind="drive")),
 ("She was flown to Mendocino Coast Hospital in Fort Bragg, reported in stable condition. And for the co-pilot, Lieutenant junior grade Nathan O'Brien, it was the first life he had saved as an aviator.",
  [C(LUM, 68.6), C(LUM, 75.0)], dict(kind="calm", gap=0.8)),
 ("Same air station, about eleven weeks earlier. Eight forty-seven on a Saturday morning in May, a crew member on the Queen Elizabeth reported a forty-five-year-old passenger with a serious medical condition, about forty-five miles southwest of Shelter Cove. This time, the Coast Guard says, a duty flight surgeon recommended the medevac. And again, a Dolphin from Humboldt Bay made the hoist.",
  [G("callcard", kicker="COAST GUARD SECTOR HUMBOLDT BAY · MAY 2, 2026", title="QUEEN ELIZABETH",
     rows=[["SAT 08:47", "MEDEVAC REQUEST FROM THE SHIP"], ["POSITION", "~45 MI SW OF SHELTER COVE"], ["PATIENT", "45-YEAR-OLD PASSENGER"], ["HOIST", "MH-65 DOLPHIN → ST. JOSEPH HOSPITAL, EUREKA"]])], dict(kind="calm")),

 # ---------------- V. THE SMALL BOAT (Tillamook Bay) ----------------
 ("Sometimes the hoist doesn't happen from the patient's own boat.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="V", t="THE SMALL BOAT")], dict(kind="calm")),
 ("November fifth, twenty twenty-five. Heavy seas, about nineteen miles southwest of Tillamook Bay, Oregon. A mariner on a sailboat needs a higher level of medical care.",
  [G("map", map=dict(bounds=ORE, rings=[dict(ll=SAIL_P, r=36, n=3, d=0.3)],
     cities=[dict(ll=SAIL_P, name="SAILBOAT", sub="~19 MI SW OF TILLAMOOK BAY", d=0.3, color="#FF5B14", anchor="end", dy=60), dict(ll=TILLAMOOK, name="STATION TILLAMOOK BAY", d=0.6, size=26, anchor="start", dy=-20),
             dict(ll=ASTORIA, name="AIR STATION ASTORIA", d=0.8, size=26)]),
     kicker="NOVEMBER 5, 2025 · HEAVY SEAS", title="OFF THE OREGON COAST", footer="POSITION ILLUSTRATIVE")], dict(kind="calm")),
 ("Here, the Coast Guard did it in two steps. First, a forty-seven-foot motor lifeboat from Station Tillamook Bay takes the mariner off the sailboat.",
  [G("steps", kicker="TWO STEPS · NOV 5, 2025", title="SAILBOAT → LIFEBOAT → HELICOPTER",
     items=[["Boat", "47-ft motor lifeboat takes the mariner off the sailboat"], ["Hoist", "A Jayhawk hoists from the lifeboat"], ["Fly", "To a higher level of care"]], active=0,
     footer="SOURCE: U.S. COAST GUARD VIA DVIDS")], dict(kind="calm")),
 ("The forty-seven-foot motor lifeboat is built for high seas, surf, and heavy weather. It can work in seas up to thirty feet. And if a wave knocks it over, it rights itself in thirty seconds.",
  [G("stat", a="30 FT", b="SEAS · 47-FT MOTOR LIFEBOAT", c="OR 20-FT SURF IN 50-KNOT WINDS · SELF-RIGHTS IN 30 SECONDS · SOURCE: USCG")], dict(kind="calm")),
 ("Then a Jayhawk from Air Station Astoria hoists the patient, from the lifeboat.",
  [C(SAIL, 1), C(SAIL, 9)], dict(tag=("19 MI SW OF TILLAMOOK BAY, ORE.", "NOV 5, 2025"), kind="drive")),
 ("Look at that water.",
  [C(SAIL, 17)], dict(kind="slow")),
 ("With a trail line from the lifeboat steadying it, the rescue basket comes up, with the mariner inside.",
  [C(SAIL, 24.5), C(SAIL, 29), C(SAIL, 34)], dict(kind="tense")),
 ("And into the helicopter.",
  [C(SAIL, 39.5)], dict(kind="drive")),
 ("Inside, the crew gets the patient settled, for the flight to a higher level of care.",
  [C(SAIL, 49), C(SAIL, 57)], dict(kind="calm", gap=0.8)),
 ("And sometimes a boat can do the whole job. Near Juneau, Alaska, in August twenty nineteen, the Coast Guard twice asked a cruise ship to come close enough for a small response boat to pick the patient up, and bring them to a harbor where fire and rescue crews took over.",
  [G("steps", kicker="JUNEAU, ALASKA · AUGUST 2019", title="WHEN THE SHIP CAN COME CLOSE",
     items=[["Close", "The ship comes in toward shore"], ["Boat", "A 45-ft response boat picks up the patient"], ["Harbor", "Fire and rescue takes over"]], active=1,
     footer="SOURCE: JUNEAU EMPIRE · U.S. COAST GUARD STATION JUNEAU")], dict(kind="calm", gap=0.8)),

 # ---------------- VI. THE LONG WAY IN (Chipol Donghai) ----------------
 ("Which brings us back to the Chipol Donghai.",
  [G("chapter", case="ANATOMY OF A RESCUE", n="VI", t="THE LONG WAY IN")], dict(kind="slow")),
 ("Fifteen hundred miles out, no helicopter could get there. So for days, the ship headed toward Oahu, while the watchstanders in Honolulu kept in regular contact with its crew.",
  [G("map", map=dict(bounds=NPAC, arcs=[dict(**{"from": CHIPOL_FAR, "to": CHIPOL_NEAR}, d=0.3, dur=1.2, bend=0.03, color="#FF5B14")],
     rings=[dict(ll=CHIPOL_NEAR, r=30, n=3, d=1.5, color="#FFC93C")],
     cities=[dict(ll=CHIPOL_FAR, name="SUNDAY · ~1,500 MI N", sub="POSITION ILLUSTRATIVE", d=0.3, color="#FF5B14"), dict(ll=CHIPOL_NEAR, name="WEDNESDAY · ~57 MI OFF OAHU", d=1.6, color="#FFC93C", anchor="end", dy=-40),
             dict(ll=OAHU, name="OAHU", d=0.6, size=28, dy=40)]),
     kicker="OCTOBER 2025", title="THE LONG WAY IN")], dict(kind="calm")),
 ("Then the master's condition got worse. The duty flight surgeon recommended a medevac.",
  [G("callcard", kicker="JOINT RESCUE COORDINATION CENTER HONOLULU · OCTOBER 2025", title="CHIPOL DONGHAI",
     rows=[["SUNDAY", "EMAIL · ~1,500 MI NORTH OF OAHU"], ["TRANSIT", "SHIP HEADS FOR OAHU · REGULAR CONTACT"], ["WORSENS", "FLIGHT SURGEON: MEDEVAC"], ["WED 20:53", "HOIST · ~57 MI OFF OAHU"]])], dict(kind="tense")),
 ("At eight fifty-three on Wednesday night, about fifty-seven miles off Oahu, a Dolphin from Barbers Point is over the ship.",
  [C(CHIPOL, 34), C(CHIPOL, 40)], dict(tag=("57 MI OFF OAHU, HAWAII", "OCT 8, 2025"), kind="drive")),
 ("The crew brings the master up, and into the cabin.",
  [C(CHIPOL, 55), C(CHIPOL, 64)], dict(kind="tense")),
 ("He was flown to Queen's Medical Center in Honolulu, in stable condition.",
  [C(CHIPOL, 74), C(CHIPOL, 78)], dict(kind="calm")),
 ("The search and rescue mission coordinator said the Pacific's vast distances require days of sustained communication and coordination. And he put the mission in one sentence.",
  [G("quote", q="The Coast Guard's priority is the preservation of life at sea…", w="CMDR. PRESTON HIEB · SEARCH AND RESCUE MISSION COORDINATOR · COAST GUARD OCEANIA DISTRICT")], dict(kind="slow", gap=1.0)),

 # ---------------- VII. WHAT MAKES IT WORK ----------------
 ("So what do these six medevacs have in common?",
  [G("chapter", case="ANATOMY OF A RESCUE", n="VII", t="WHAT MAKES IT WORK")], dict(kind="question")),
 ("Look closely, and four things keep coming up.",
  [G("steps", kicker="WHAT THESE SIX MEDEVACS HAVE IN COMMON", title="FOUR THINGS THAT GET A PATIENT OFF A SHIP",
     items=[["Call early", "Days out, not hours"], ["A doctor", "The flight surgeon weighs the risk"], ["Meet halfway", "The ship heads toward help"], ["Right tool", "Jayhawk, cutter, lifeboat"]])], dict(kind="calm")),
 ("One: call early. The Chipol Donghai reached out when it was still days from Oahu.",
  [C(CHIPOL, 15.5), C(CHIPOL, 50)], dict(kind="drive")),
 ("Two: a doctor in the loop. In most of these cases, a duty flight surgeon recommended the medevac before anyone took off.",
  [C(LUM, 44.5), C(SOL, 60)], dict(kind="calm")),
 ("Three: meet halfway. The Solstice and the Chipol Donghai both headed toward Oahu, closer to the helicopters.",
  [C(SOL, 40), C(CHIPOL, 59.6)], dict(kind="calm")),
 ("And four: the right tool for the distance. A Jayhawk for a boat far off Georgia. A cutter's flight deck off Kauai. A motor lifeboat, in heavy seas off Oregon.",
  [C(VIKING, 8.8), C(VIKING, 16.2), C(SAIL, 19.5)], dict(kind="drive")),
 ("In each of the six rescues in this video, the patient was hoisted aboard a helicopter, and flown toward a higher level of care.",
  [C(LUM, 57.8), C(VIKING, 126)], dict(kind="punch", gap=0.8)),
 ("Next time on Channel Sixteen, another call, minute by minute. Stay safe out there.",
  [G("end", stamp="MEDEVAC AT SEA")], dict(kind="calm", gap=2.4)),
]

DISPLAY = [
 ("October, twenty twenty-five", "October 2025"), ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"),
 ("six-hundred-sixteen-foot", "616-foot"), ("fifteen hundred miles", "1,500 miles"), ("Fifteen hundred miles", "1,500 miles"), ("eight fifty-three", "8:53"),
 ("June twelfth", "June 12"), ("forty-four-foot", "44-foot"), ("ninety-two miles", "92 miles"), ("fifty-six-year-old", "56-year-old"),
 ("MH-sixty", "MH-60"), ("MH-sixty-five", "MH-65"), ("three hours", "3 hours"),
 ("April twenty-second", "April 22"), ("Three nineteen", "3:19"), ("two hundred seventy-six miles", "276 miles"), ("seventy-eight-year-old", "78-year-old"),
 ("fifty-eight miles", "58 miles"), ("Squadron Thirty-Seven", "Squadron 37"),
 ("March third", "March 3"), ("five-hundred-forty-seven-foot", "547-foot"), ("a hundred miles", "100 miles"), ("thirty-seven-year-old", "37-year-old"),
 ("July sixteenth", "July 16"), ("Five ten", "5:10"), ("fifty-one-year-old", "51-year-old"), ("forty-five miles", "45 miles"), ("ten feet", "10 feet"), ("forty-mile-an-hour", "40-mph"), ("August twenty nineteen", "August 2019"), ("Three days later", "Three days later"),
 ("November fifth", "November 5"), ("fifty-five-year-old", "55-year-old"), ("five hundred forty miles", "540 miles"), ("eighty-six miles", "86 miles"), ("Eight forty-seven", "8:47"), ("forty-five-year-old", "45-year-old"), ("thirty feet", "30 feet"), ("thirty seconds", "30 seconds"), ("nineteen miles", "19 miles"), ("forty-seven-foot", "47-foot"),
 ("fifty-seven miles", "57 miles"), ("Channel Sixteen", "Channel 16"),
]

META = dict(
    case="ANATOMY OF A RESCUE · 007", label="CH 16 · 156.800 MHz",
    title="Medevac at Sea: How the Coast Guard Gets a Patient Off a Ship, in 6 Real Rescues",
    voice="am_eric",
    credit=("Footage: U.S. Coast Guard via DVIDS (public domain). Appearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NCHANNEL 16 is an independent channel, not affiliated with the U.S. Coast Guard."),
)
