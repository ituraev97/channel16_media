# CHANNEL 16 · MILITARY HARDWARE · m013 (TikTok only, Nov 12, 2026). Five vertical videos t1–t5, 62–75 s each.
# Exercises, tests and training only. Facts: sources.md. shot: (clip_id, start, cx)
G_HUR = 995774       # AC-130J live-fire training near Hurlburt Field, Fla., Dec 8, 2025 (horizontal parts only: 54-76 s, 114-121 s)
G_MEL = 826283       # AC-130J (17th SOS) live fire training over Melrose Air Force Range, N.M., Dec 8, 2021 (interior)
G_CAN = 875552       # AC-130J Ghostrider gunship B-roll, Cannon AFB, N.M., 2023: takeoff, landing, live-fire maneuvers
F_TRI = 946904       # F-35B (VMFA-211) deck landing qualifications aboard USS Tripoli (LHA 7), Steel Knight 24, Pacific, Dec 5, 2024
F_T22 = 840297       # VMFA-211 F-35B flight operations aboard USS Tripoli (LHA 7), Pacific, Apr 2022
T_RI = 1009153       # unarmed Trident II D5LE launch, USS Rhode Island (SSBN 740), DASO-29, off Cape Canaveral, May 9, 2019
T_CMP = 1009260      # Trident II D5 flight test compilation: DASO 25 (USS West Virginia, Jun 2, 2014), DASO 26 (USS Kentucky, Nov 7, 2015), DASO 27 (USS Maryland, Aug 31, 2016)
M_OJO = 948412       # Marines fire M777, ARTP 24.3, Ojojihara Maneuver Area, Japan, Dec 3, 2024
M_YAU = 941822       # Marines fire M777, ARTP 24.2, Yausubetsu Maneuver Area, Hokkaido, Japan, Sept 14, 2024
M_FUJ = 926221       # Marines fire M777, ARTP 24.1, Camp Fuji, Japan, May 16, 2024
L_ONS = 997888       # LCACs (ACU 4) land at Onslow Beach, TCAT 26.1, Camp Lejeune, N.C., Feb 27, 2026
L_UNI = 984580       # UNITAS 2025: Marines and multinational forces land at Onslow Beach on LCACs (ACU 4), Sept 26, 2025

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

LB_HUR = dict(label="NEAR HURLBURT FIELD, FLA. · LIVE-FIRE TRAINING · DEC 2025")
LB_CAN = dict(label="AC-130J GHOSTRIDER · AIR FORCE B-ROLL · MAR 2023")
LB_MEL = dict(label="MELROSE RANGE, N.M. · LIVE-FIRE TRAINING · DEC 2021")
LB_TRI = dict(label="USS TRIPOLI · EXERCISE STEEL KNIGHT 24 · DEC 2024")
LB_T22 = dict(label="USS TRIPOLI · FLIGHT OPERATIONS · APR 2022")
LB_RI = dict(label="USS RHODE ISLAND · UNARMED TEST · MAY 2019")
LB_WV = dict(label="USS WEST VIRGINIA · UNARMED TEST · JUNE 2014")
LB_KY = dict(label="USS KENTUCKY · UNARMED TEST · NOV 2015")
LB_OJO = dict(label="OJOJIHARA, JAPAN · MARINE LIVE FIRE · DEC 2024")
LB_YAU = dict(label="HOKKAIDO, JAPAN · MARINE LIVE FIRE · SEP 2024")
LB_FUJ = dict(label="CAMP FUJI, JAPAN · MARINE LIVE FIRE · MAY 2024")
LB_ONS = dict(label="ONSLOW BEACH, N.C. · AMPHIBIOUS TRAINING · FEB 2026")
LB_UNI = dict(label="ONSLOW BEACH, N.C. · EXERCISE UNITAS · SEP 2025")

SHORTS = [
 dict(id="t1", hook="[30MM + 105MM]<br>GUNS ON A PLANE", title="The AC-130J gunship carries a 30mm and a 105mm cannon. This is live-fire training",
      lines=[
  ("Watch the barrel. This gun is firing out of the side of an airplane.", [(G_HUR, 114.40, .50), (G_HUR, 117.40, .50)], "tense", LB_HUR),
  ("The AC-130J Ghostrider. An Air Force gunship, built on a modified C-130J.", [(G_CAN, 0.50, .45), (G_CAN, 5.00, .45)], "punch", LB_CAN),
  ("It carries two cannons the crew can aim: a thirty-millimeter, and a one-hundred-five-millimeter.", [(G_MEL, 63.20, .45), (G_MEL, 68.20, .50)], "punch", LB_MEL),
  ("Plus precision-guided weapons, like Hellfire and Griffin missiles and the Small Diameter Bomb.", [(G_CAN, 32.00, .55), (G_CAN, 20.00, .50)], "calm"),
  ("Its main jobs, in the Air Force's words: close air support, air interdiction and armed reconnaissance.", [(G_HUR, 54.00, .50), (G_HUR, 57.50, .50)], "calm", LB_HUR),
  ("Inside, crew members handle the heavy rounds by hand.", [(G_HUR, 72.30, .50)], "tense", LB_HUR),
  ("Eight crew: two pilots, two combat systems officers, and four special mission aviators.", [(G_MEL, 296.00, .50), (G_MEL, 300.00, .50)], "calm"),
  ("Four Rolls-Royce turboprops, forty-seven hundred shaft horsepower each.", [(G_CAN, 11.00, .62), (G_CAN, 14.80, .55)], "drive", LB_CAN),
  ("Wingspan: almost one hundred thirty-three feet. Maximum takeoff weight: one hundred sixty-four thousand pounds.", [(G_CAN, 124.00, .50), (G_CAN, 127.50, .50)], "calm"),
  ("Range: about three thousand miles. With air refueling, the limit is the crew's duty day.", [(G_CAN, 130.80, .50), (G_CAN, 134.00, .50)], "calm"),
  ("And this is the gunship's own sensor view, during live-fire maneuvers.", [(G_CAN, 115.40, .50), (G_CAN, 78.40, .50)], "tense", LB_CAN),
  ("The Air Force calls it the fifth generation of gunship. It replaced the AC-130U and AC-130W.", [(G_HUR, 61.00, .45), (G_HUR, 68.20, .45)], "calm", LB_HUR),
  ("Deployed in July twenty nineteen. Unit cost: one hundred sixty-five million dollars.", [(G_CAN, 139.00, .50), (G_CAN, 100.20, .50)], "punch", LB_CAN),
  ("Which aircraft should we break down next? Follow for more.", [(G_CAN, 106.00, .50)], "punch", LB_CAN),
 ]),
 dict(id="t2", hook="[MACH 1.6]<br>AND IT CAN HOVER", title="The F-35B can hover and land straight down on a ship. Here's what that looks like",
      lines=[
  ("This fighter jet stops in midair, then lands straight down onto a ship.", [(F_TRI, 205.40, .55), (F_TRI, 208.60, .50)], "tense", LB_TRI),
  ("The F-35B: the Marine Corps' short takeoff, vertical landing version of the F-35.", [(F_TRI, 236.00, .50), (F_TRI, 240.00, .50)], "punch"),
  ("One Pratt and Whitney F135 engine also drives a LiftFan.", [(F_TRI, 244.00, .50)], "drive"),
  ("A swivel duct turns the engine's thrust downward. Roll ducts under the wings keep it steady.", [(F_TRI, 248.80, .50), (F_TRI, 253.00, .50)], "calm"),
  ("This is the amphibious assault ship USS Tripoli, during exercise Steel Knight, December twenty twenty-four.", [(F_TRI, 144.00, .45), (F_TRI, 150.00, .45)], "calm", LB_TRI),
  ("Marine F-35B pilots were flying deck landing qualifications.", [(F_TRI, 156.00, .45), (F_TRI, 161.00, .45)], "calm"),
  ("Britain's Royal Air Force, which also flies the F-35B, lists its top speed at Mach one point six.", [(F_TRI, 224.10, .50), (F_TRI, 182.00, .50)], "drive"),
  ("Ceiling: fifty thousand feet. Maximum takeoff weight: about sixty thousand pounds.", [(F_TRI, 228.60, .45), (F_TRI, 166.00, .45)], "calm"),
  ("It can also take off from a short deck.", [(F_TRI, 267.80, .50)], "drive"),
  ("In twenty fifteen, the Marine Corps declared its first F-35B squadron, VMFA-one-twenty-one, operational.", [(F_T22, 102.00, .50), (F_T22, 106.00, .50)], "calm", LB_T22),
  ("It was the first squadron in military history to go operational with any F-35.", [(F_T22, 110.00, .50), (F_T22, 114.00, .50)], "calm", LB_T22),
  ("The Marine Corps planned for the F-35 to replace three older aircraft: the Harrier, the Hornet, and the Prowler.", [(F_T22, 61.00, .50), (F_T22, 64.20, .50)], "calm", LB_T22),
  ("One more hover, over the deck of USS Tripoli.", [(F_TRI, 77.00, .50)], "tense", LB_TRI),
  ("Hover landing or catapult launch: which takes more skill? Follow for more.", [(F_TRI, 214.50, .50)], "punch"),
 ]),
 dict(id="t3", hook="[4,000] NAUTICAL MILES<br>FROM A SUBMARINE", title="A Trident II D5 missile launched from a Navy submarine: 4,000 nautical miles of range",
      lines=[
  ("It just broke the surface. A Trident Two D5 missile, launched from a U.S. Navy submarine.", [(T_RI, 1.00, .56), (T_RI, 5.80, .50)], "tense", LB_RI),
  ("This was an unarmed test, from USS Rhode Island, off Cape Canaveral, Florida, in May twenty nineteen.", [(T_RI, 10.90, .50), (T_RI, 17.40, .45)], "calm", LB_RI),
  ("Ohio-class submarines carry up to twenty of them.", [(T_RI, 20.30, .50)], "punch"),
  ("A three-stage, solid-fuel ballistic missile with inertial guidance.", [(T_RI, 25.30, .50)], "drive"),
  ("Its range, per the Navy: four thousand nautical miles. That's forty-six hundred statute miles.", [(T_RI, 30.55, .45), (T_RI, 34.60, .45)], "punch"),
  ("It's forty-four feet long, and weighs one hundred thirty thousand pounds.", [(T_RI, 38.00, .40)], "calm"),
  ("First deployed in nineteen ninety. Unit cost, per the Navy: thirty point nine million dollars.", [(T_RI, 41.70, .40), (T_CMP, 20.00, .50)], "calm"),
  ("These tests have a name: DASO, a Demonstration and Shakedown Operation.", [(T_CMP, 46.00, .52), (T_CMP, 51.00, .50)], "calm", LB_WV),
  ("They show a submarine and its crew are ready, before the boat deploys.", [(T_CMP, 54.00, .50), (T_CMP, 58.00, .50)], "calm"),
  ("This one is USS West Virginia, off Florida, in June twenty fourteen.", [(T_CMP, 61.50, .50), (T_CMP, 76.50, .50)], "calm", LB_WV),
  ("And this is USS Kentucky, off California, in November twenty fifteen. A night launch.", [(T_CMP, 119.50, .52), (T_CMP, 124.00, .50)], "tense", LB_KY),
  ("The Navy calls this missile the most survivable leg of the nuclear triad.", [(T_CMP, 128.50, .50)], "calm", LB_KY),
  ("Britain's Vanguard-class submarines carry it too. This launch was a U.S. Navy test.", [(T_CMP, 85.00, .45), (T_CMP, 88.50, .45)], "calm", LB_WV),
  ("Life-extended versions entered fleet service in twenty seventeen, and will go on the new Columbia-class submarines.", [(T_RI, 48.40, .55), (T_RI, 51.80, .50)], "calm", LB_RI),
  ("Which launch should we break down next? Follow for more.", [(T_RI, 57.10, .55)], "punch"),
 ]),
 dict(id="t4", hook="[155 MM]<br>BUILT TO BE LIGHT", title="The M777 howitzer: a 155mm gun so light that two fit in one C-130 (live-fire training)",
      lines=[
  ("Watch the barrel kick back. An M777 howitzer, firing in a Marine Corps live-fire exercise in Japan.", [(M_OJO, 275.60, .50), (M_OJO, 285.40, .50)], "tense", LB_OJO),
  ("A one-hundred-fifty-five-millimeter towed howitzer, built to be light.", [(M_YAU, 5.00, .45)], "punch", LB_YAU),
  ("The Australian Army, which also uses it, lists the weight at forty-one hundred kilograms. That's about nine thousand pounds.", [(M_YAU, 9.30, .45), (M_YAU, 13.00, .55)], "calm"),
  ("The U.S. Army says it's seven thousand pounds lighter than the M198 it replaced.", [(M_FUJ, 9.20, .50), (M_FUJ, 134.20, .40)], "calm", LB_FUJ),
  ("The U.S. Army says two of them fit on a single C-130.", [(M_FUJ, 100.00, .45)], "punch"),
  ("Range, per the Australian Army: twenty-four kilometers with conventional rounds, thirty with improved rounds.", [(M_YAU, 44.50, .45), (M_YAU, 47.50, .45)], "drive", LB_YAU),
  ("Rate of fire: two rounds a minute sustained, five a minute rapid.", [(M_YAU, 50.50, .45), (M_YAU, 53.50, .45)], "drive"),
  ("These are its one-hundred-fifty-five-millimeter rounds.", [(M_FUJ, 54.20, .45)], "calm", LB_FUJ),
  ("The Army and the Marine Corps developed it together. BAE Systems builds it.", [(M_FUJ, 31.60, .45), (M_FUJ, 38.10, .45)], "calm"),
  ("Marines first fired it as a fielded gun in the California desert in May two thousand five: more than eleven hundred fifty rounds in a week.", [(M_OJO, 15.00, .50), (M_OJO, 20.50, .50)], "calm", LB_OJO),
  ("Here, Marines fire it at Camp Fuji, Japan, in May twenty twenty-four.", [(M_FUJ, 64.10, .50)], "tense", LB_FUJ),
  ("And at Ojojihara, Japan, in December.", [(M_OJO, 290.00, .50), (M_OJO, 300.00, .50)], "tense", LB_OJO),
  ("One more round.", [(M_YAU, 61.20, .55)], "punch", LB_YAU),
  ("Twenty-four kilometers of range, from a gun two of which fit in one plane.", [(M_OJO, 304.90, .45), (M_OJO, 308.00, .45)], "punch", LB_OJO),
  ("Towed gun or self-propelled: which would you rather crew? Follow for more.", [(M_OJO, 342.50, .45)], "punch"),
 ]),
 dict(id="t5", hook="[60 TONS]<br>ON A CUSHION OF AIR", title="This Navy hovercraft carries 60 tons and drives straight up onto the beach",
      lines=[
  ("This boat doesn't stop at the waterline. It drives right up onto the beach.", [(L_ONS, 37.20, .45), (L_ONS, 45.00, .55)], "tense", LB_ONS),
  ("The Navy's LCAC: Landing Craft, Air Cushion. A hovercraft.", [(L_ONS, 49.80, .50)], "punch"),
  ("It carries sixty tons, seventy-five in overload. That's enough for an M1 tank.", [(L_ONS, 61.00, .50), (L_ONS, 66.00, .50)], "punch"),
  ("Speed: more than forty knots, fully loaded.", [(L_ONS, 81.00, .55)], "drive"),
  ("Four gas turbines: two to push it, two to lift it. Sixteen thousand horsepower.", [(L_ONS, 91.10, .40), (L_ONS, 98.00, .55)], "drive"),
  ("The Navy says an air cushion craft can reach more than seventy percent of the world's coastline. Conventional landing craft: about fifteen percent.", [(L_UNI, 102.00, .55), (L_UNI, 107.60, .55)], "calm", LB_UNI),
  ("A crew of five.", [(L_UNI, 113.00, .60)], "punch"),
  ("Almost ninety-two feet long, and just over forty-eight feet wide.", [(L_UNI, 117.60, .45), (L_UNI, 121.00, .50)], "calm"),
  ("It launches from the well decks of amphibious ships, and comes ashore from there.", [(L_UNI, 132.70, .40), (L_UNI, 140.30, .50)], "calm"),
  ("Here, Marines and multinational forces land at Onslow Beach, North Carolina, for exercise UNITAS twenty twenty-five.", [(L_UNI, 196.50, .45), (L_UNI, 200.30, .45)], "calm", LB_UNI),
  ("UNITAS has run every year since nineteen sixty. It's the world's longest-running annual multinational maritime exercise.", [(L_UNI, 212.90, .45), (L_UNI, 219.60, .45)], "calm"),
  ("Then the vehicles roll off.", [(L_UNI, 181.20, .40)], "tense"),
  ("The first LCAC was delivered in nineteen eighty-four. Ninety-one were built.", [(L_UNI, 312.20, .45), (L_UNI, 318.50, .45)], "calm", LB_UNI),
  ("And it moves out again.", [(L_UNI, 326.00, .45)], "slow"),
  ("Hovercraft or helicopter: which is the better way onto a beach? Follow for more.", [(L_UNI, 330.00, .45)], "punch", LB_UNI),
 ]),
]
YSHORTS = []

DISPLAY = [("thirty-millimeter", "30mm"), ("one-hundred-five-millimeter", "105mm"), ("forty-seven hundred", "4,700"),
           ("one hundred thirty-three", "133"), ("one hundred sixty-four thousand", "164,000"), ("three thousand", "3,000"),
           ("twenty nineteen", "2019"), ("one hundred sixty-five million dollars", "$165 million"), ("twenty twenty-four", "2024"), ("thirty-seven", "37"),
           ("Pratt and Whitney", "Pratt & Whitney"), ("Mach one point six", "Mach 1.6"), ("fifty thousand", "50,000"), ("sixty thousand", "60,000"),
           ("July thirty-first, twenty fifteen", "July 31, 2015"), ("VMFA-one-twenty-one", "VMFA-121"),
           ("Trident Two D5", "Trident II D5"), ("up to twenty", "up to 20"), ("four thousand nautical", "4,000 nautical"), ("forty-six hundred", "4,600"),
           ("forty-four feet", "44 feet"), ("one hundred thirty thousand", "130,000"), ("nineteen ninety", "1990"), ("thirty point nine million dollars", "$30.9 million"),
           ("twenty fourteen", "2014"), ("twenty fifteen", "2015"), ("twenty seventeen", "2017"),
           ("one-hundred-fifty-five-millimeter", "155mm"), ("forty-one hundred kilograms", "4,100 kg"), ("nine thousand", "9,000"), ("seven thousand", "7,000"),
           ("twenty-four kilometers", "24 km"), ("Twenty-four kilometers", "24 km"), ("thirty with", "30 with"), ("two rounds", "2 rounds"), ("five a minute", "5 a minute"),
           ("two thousand five", "2005"), ("eleven hundred fifty", "1,150"),
           ("sixty tons", "60 tons"), ("seventy-five", "75"), ("forty knots", "40 knots"), ("Four gas", "4 gas"), ("Sixteen thousand", "16,000"),
           ("seventy percent", "70%"), ("fifteen percent", "15%"), ("ninety-two feet", "92 feet"), ("forty-eight feet", "48 feet"),
           ("twenty twenty-five", "2025"), ("nineteen sixty", "1960"), ("nineteen eighty-four", "1984"), ("Ninety-one", "91"), ("twenty twenty-six", "2026")]
