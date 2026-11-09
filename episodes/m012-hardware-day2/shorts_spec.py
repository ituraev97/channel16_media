# CHANNEL 16 · MILITARY HARDWARE · m012 (TikTok only, Nov 11, 2026). Five vertical videos w1–w5, 62–75 s each.
# Exercises, tests and training only. Facts: sources.md. shot: (clip_id, start, cx)
MK_LC = 582965       # USS Lake Champlain (CG 57) fires forward MK 45 5-inch gun, live fire event, Pacific, Jan 31, 2018
MK_MU = 1006389      # USS Mustin (DDG 89) fires Mark 45 5-inch gun on the fo'c'sle, live-fire exercise, Western Pacific, Apr 16, 2026
F_GR = 735120        # USS Gerald R. Ford (CVN 78), EA-18G Growler (VX-23) lands, Aircraft Compatibility Testing (EMALS/AAG), Atlantic, Jan 19, 2020
F_C2 = 735016        # Ford, C-2A Greyhound (VX-20) lands, Aircraft Compatibility Testing, Jan 17, 2020
F_C2B = 735045       # Ford, C-2A Greyhound (VX-20), Aircraft Compatibility Testing, Jan 17, 2020
AB_FS = 499722       # aerial drone: M1A2 Abrams crews, 1st ABCT 3rd ID, Table VI Gunnery, Fort Stewart, Ga., Dec 8, 2016
AB_GR = 427494       # 1-64 Armor, 1st ABCT 3rd ID fire M1A2 SEPv2 Abrams, Exercise Combined Resolve V, Grafenwoehr, Germany, Oct 8, 2015 (slate 0–2 s)
SM_SH = 857966       # USS Shoup (DDG 86) launches SM-2 Block IIIA, Live Fire With a Purpose, Pacific, Sept 18, 2022
SM_PO = 883984       # USS Porter (DDG 78) launches SM-2, live-fire exercise, Formidable Shield 2023, May 20, 2023
B_A = 943838         # two B-52H (20th EBS) take off from RAF Fairford, Bomber Task Force 25-1, training sortie, Nov 13, 2024
B_B = 945517         # B-52H (20th EBS) taxis/takes off at RAF Fairford for Exercise APEX Buccaneer, Dec 3, 2024

HUD = "CH 16 · HARDWARE"
CREDIT = "Footage: U.S. DoD via DVIDS · not affiliated with the U.S. military"
CTA = "FOLLOW · CHANNEL 16"

L_LC = dict(label="USS LAKE CHAMPLAIN · LIVE FIRE · JAN 2018")
L_MU = dict(label="USS MUSTIN · LIVE-FIRE EXERCISE · APR 2026")
L_F = dict(label="USS GERALD R. FORD · COMPATIBILITY TESTING · JAN 2020")
L_FS = dict(label="FORT STEWART, GA · GUNNERY TRAINING · DEC 2016")
L_GR = dict(label="GRAFENWOEHR, GERMANY · EXERCISE · OCT 2015")
L_SH = dict(label="USS SHOUP · LIVE-FIRE EXERCISE · SEP 2022")
L_PO = dict(label="USS PORTER · FORMIDABLE SHIELD EXERCISE · MAY 2023")
L_BA = dict(label="RAF FAIRFORD · BOMBER TASK FORCE TRAINING · NOV 2024")
L_BB = dict(label="RAF FAIRFORD · EXERCISE APEX BUCCANEER · DEC 2024")

SHORTS = [
 dict(id="w1", hook="[5-INCH] GUN<br>13 NAUTICAL MILES", title="The Navy's 5-inch gun reaches about 13 nautical miles. Here it is firing at sea",
      lines=[
  ("This is the five-inch gun on a U.S. Navy cruiser. Watch the muzzle.", [(MK_LC, 5.10, .62), (MK_LC, 28.10, .62)], "tense", L_LC),
  ("The Mark forty-five. A fully automatic naval gun mount.", [(MK_LC, 8.50, .45)], "punch"),
  ("It's built to hit ships, aircraft, and targets ashore.", [(MK_LC, 13.20, .45)], "calm"),
  ("The Navy lists its rate of fire at sixteen to twenty rounds a minute.", [(MK_LC, 40.60, .45)], "drive"),
  ("Its range: about thirteen nautical miles with conventional rounds. That's almost fifteen statute miles.", [(MK_LC, 44.50, .45), (MK_LC, 48.50, .45)], "punch"),
  ("Its crew works from below deck: a mount captain, an operator, and four ammunition handlers.", [(MK_LC, 17.00, .45), (MK_LC, 21.00, .45)], "calm"),
  ("Destroyers carry six hundred rounds for it. Cruisers carry twelve hundred.", [(MK_LC, 32.00, .45)], "calm"),
  ("The first version went to sea in nineteen seventy-one, as a lighter, easier-to-maintain replacement for the Mark forty-two.", [(MK_LC, 36.70, .45), (MK_LC, 54.00, .45)], "calm"),
  ("The newer Mod four adds a longer, sixty-two-caliber barrel, to improve shore bombardment.", [(MK_LC, 0.20, .45), (MK_LC, 24.40, .45)], "calm"),
  ("This is the destroyer USS Mustin, firing hers in the Western Pacific in April twenty twenty-six.", [(MK_MU, 1.00, .42), (MK_MU, 8.50, .35)], "tense", L_MU),
  ("It's installed on the Navy's Arleigh Burke-class destroyers and Ticonderoga-class cruisers.", [(MK_MU, 12.00, .40)], "calm"),
  ("One more round, from the Mustin's forecastle.", [(MK_MU, 19.50, .55)], "drive", L_MU),
  ("Sixteen to twenty rounds a minute, out to about thirteen nautical miles.", [(MK_MU, 24.00, .55)], "punch"),
  ("Five-inch gun or Gatling gun: which would you want on your ship? Follow for more.", [(MK_MU, 29.00, .55)], "punch"),
 ]),
 dict(id="w2", hook="[~100,000] TONS<br>NO STEAM CATAPULT", title="USS Gerald R. Ford launches jets electromagnetically. Here's what that looks like",
      lines=[
  ("This jet is leaving USS Gerald R. Ford, launched by an electromagnetic catapult, not steam.", [(F_GR, 76.30, .55)], "tense", L_F),
  ("The Navy calls it the first new shipboard launching technology on its carriers in sixty years.", [(F_GR, 83.30, .50)], "punch"),
  ("It does the same job as a steam catapult, with entirely different technology.", [(F_GR, 62.00, .50)], "calm"),
  ("The Navy says it gives smoother acceleration and more accurate end speed.", [(F_GR, 67.00, .50)], "calm"),
  ("Now the landing. Watch this jet catch a wire.", [(F_GR, 102.50, .45)], "tense"),
  ("That's the Advanced Arresting Gear: software-controlled, with energy absorbers and digital controls.", [(F_GR, 106.50, .45), (F_GR, 110.00, .45)], "drive"),
  ("This EA-18G Growler, from test squadron VX-23, landed during compatibility testing in January twenty twenty.", [(F_GR, 113.00, .45)], "calm", L_F),
  ("The ship itself: one thousand ninety-two feet long, about one hundred thousand tons fully loaded.", [(F_C2B, 29.00, .50), (F_C2B, 31.90, .50)], "punch"),
  ("Two nuclear reactors. About four thousand five hundred fifty people aboard.", [(F_C2, 10.00, .55)], "calm"),
  ("And room for more than seventy-five aircraft.", [(F_C2, 23.00, .50)], "calm"),
  ("Here, a C-2A Greyhound from test squadron VX-20 comes aboard, January twenty twenty.", [(F_C2B, 17.30, .45)], "calm", L_F),
  ("Ford was commissioned on July twenty-second, twenty seventeen. Six days later came its first arrested landing and catapult launch.", [(F_C2, 30.00, .55), (F_C2B, 0.50, .45)], "calm", L_F),
  ("By June twenty twenty-two: ten thousand launches and recoveries.", [(F_GR, 46.00, .50)], "drive"),
  ("Steam or electric: which would you trust with your jet? Follow for more.", [(F_C2B, 35.20, .45)], "punch"),
 ]),
 dict(id="w3", hook="[120 MM]<br>MAIN GUN", title="The M1A2 Abrams: a 120mm cannon and a 1,500-horsepower gas turbine (gunnery training)",
      lines=[
  ("Watch the muzzle flash. An M1A2 Abrams, firing on a training range in Georgia.", [(AB_FS, 58.50, .55), (AB_FS, 61.60, .58)], "tense", L_FS),
  ("Its main weapon: a one-hundred-twenty-millimeter cannon.", [(AB_GR, 40.00, .45)], "punch", L_GR),
  ("The Australian Army, which also fields the M1A2, lists a crew of four: commander, gunner, loader and driver.", [(AB_GR, 96.00, .45), (AB_GR, 30.00, .45)], "calm"),
  ("And instead of a diesel, a gas turbine engine, rated at fifteen hundred shaft horsepower.", [(AB_GR, 22.00, .45)], "drive"),
  ("In Australia's figures: more than sixty kilometers an hour, cross-country more than forty.", [(AB_GR, 62.00, .45), (AB_GR, 68.00, .45)], "drive"),
  ("And a range of more than four hundred kilometers.", [(AB_GR, 74.00, .45)], "calm"),
  ("This is gunnery training at Fort Stewart, Georgia: tank crews of the 3rd Infantry Division, December twenty sixteen.", [(AB_FS, 37.00, .55), (AB_FS, 45.00, .55)], "calm", L_FS),
  ("This view is from a drone, high above the range.", [(AB_FS, 65.00, .55)], "slow"),
  ("Another round goes downrange.", [(AB_FS, 71.60, .68)], "punch"),
  ("And this is Grafenwoehr, Germany, October twenty fifteen: Exercise Combined Resolve Five.", [(AB_GR, 113.00, .45), (AB_GR, 157.00, .40)], "calm", L_GR),
  ("Combined Resolve Five was designed to train the Army's regionally aligned force for Europe, with multinational training at all echelons.", [(AB_GR, 183.00, .45)], "calm"),
  ("Soldiers of the 1st Battalion, 64th Armor Regiment, firing M1A2 SEP version two tanks.", [(AB_GR, 160.50, .40)], "drive"),
  ("Watch the smoke leave the barrel.", [(AB_GR, 125.60, .40)], "tense"),
  ("A hundred-twenty-millimeter gun, a turbine engine, four crew.", [(AB_FS, 84.00, .68)], "punch"),
  ("Which tank should we break down next? Follow for more.", [(AB_FS, 101.70, .55)], "punch"),
 ]),
 dict(id="w4", hook="[UP TO 90] NAUTICAL MILES<br>FROM THE DECK", title="A Navy destroyer fires an SM-2 missile straight out of its deck (live-fire exercise)",
      lines=[
  ("Straight up out of the deck. An SM-2 missile, leaving a U.S. Navy destroyer.", [(SM_SH, 27.20, .50), (SM_SH, 30.20, .50)], "tense", L_SH),
  ("The Standard Missile Two. The Navy calls it its primary surface-to-air air defense weapon.", [(SM_SH, 34.90, .50)], "punch"),
  ("It's fired from the Mark forty-one vertical launcher, as part of the Aegis weapon system.", [(SM_SH, 5.00, .50)], "calm"),
  ("You'll find it on Ticonderoga-class cruisers and Arleigh Burke-class destroyers.", [(SM_SH, 12.00, .50)], "calm"),
  ("The medium-range version is fifteen and a half feet long, and weighs about fifteen hundred fifty-eight pounds.", [(SM_SH, 41.00, .50)], "calm"),
  ("Its range: up to ninety nautical miles.", [(SM_SH, 47.00, .50)], "punch"),
  ("A dual-thrust, solid-fuel rocket, and semi-active radar homing.", [(SM_SH, 52.00, .50)], "drive"),
  ("The medium-range SM-2 first deployed in nineteen eighty-one.", [(SM_SH, 58.00, .50)], "calm"),
  ("This launch, from USS Shoup in the Pacific, was a Block Three-A, in September twenty twenty-two.", [(SM_SH, 64.00, .50), (SM_SH, 70.00, .50)], "calm", L_SH),
  ("A Navy data team was aboard, recording the launch for analysis.", [(SM_SH, 100.00, .50)], "calm"),
  ("And this is USS Porter, firing one during exercise Formidable Shield, May twenty twenty-three.", [(SM_PO, 5.50, .62), (SM_PO, 9.00, .60)], "tense", L_PO),
  ("Formidable Shield is a live-fire exercise against subsonic, supersonic and ballistic targets, held every two years.", [(SM_PO, 26.00, .40), (SM_PO, 30.00, .40)], "drive"),
  ("The medium-range version: up to ninety nautical miles.", [(SM_PO, 54.00, .45)], "punch"),
  ("Would you want to be on deck for that? Follow for more.", [(SM_SH, 118.00, .50)], "punch"),
 ]),
 dict(id="w5", hook="[1961]<br>AND STILL FLYING", title="The B-52H: first delivered in 1961, eight engines, and still flying (training takeoff)",
      lines=[
  ("Eight engines. A B-52H Stratofortress, lifting off from RAF Fairford, England.", [(B_A, 56.00, .50), (B_A, 38.50, .55)], "tense", L_BA),
  ("The first of one hundred and two B-52Hs was delivered in May nineteen sixty-one.", [(B_A, 60.00, .50)], "punch"),
  ("The Air Force says B-52s have been the backbone of its strategic bomber force for more than sixty years.", [(B_A, 27.00, .60)], "calm"),
  ("A crew of five: aircraft commander, pilot, radar navigator, navigator, and electronic warfare officer.", [(B_B, 37.10, .40), (B_B, 45.00, .40)], "calm", L_BB),
  ("The wingspan: one hundred eighty-five feet.", [(B_B, 50.50, .45)], "punch"),
  ("The length: one hundred fifty-nine feet.", [(B_B, 58.00, .45)], "calm"),
  ("It can carry about seventy thousand pounds of mixed ordnance: bombs, mines and missiles.", [(B_B, 63.00, .40)], "drive"),
  ("Listed speed: six hundred fifty miles an hour.", [(B_B, 68.00, .40)], "drive"),
  ("Range: eight thousand eight hundred miles. Ceiling: fifty thousand feet.", [(B_B, 72.00, .40)], "calm"),
  ("Power comes from eight Pratt and Whitney turbofan engines.", [(B_B, 117.50, .45)], "punch"),
  ("This one is leaving for Exercise APEX Buccaneer, a Norwegian-led training exercise in the High North, December twenty twenty-four.", [(B_B, 174.00, .50), (B_B, 180.00, .50)], "calm", L_BB),
  ("In twenty nineteen, the Air Force listed fifty-eight in the active force and eighteen in the reserve.", [(B_A, 45.00, .50)], "calm"),
  ("Delivered from nineteen sixty-one, and still flying.", [(B_A, 52.50, .50)], "punch"),
  ("What should we break down next? Follow for more.", [(B_B, 186.00, .50)], "punch"),
 ]),
]
YSHORTS = []

DISPLAY = [("Mark forty-five", "Mk 45"), ("Mark forty-two", "Mk 42"), ("Mark forty-one", "Mk 41"), ("five-inch", "5-inch"), ("Five-inch", "5-inch"),
           ("sixteen to twenty", "16 to 20"), ("Sixteen to twenty", "16 to 20"), ("thirteen nautical", "13 nautical"), ("fifteen statute", "15 statute"),
           ("six hundred rounds", "600 rounds"), ("twelve hundred", "1,200"), ("nineteen seventy-one", "1971"), ("Mod four", "Mod 4"),
           ("sixty-two-caliber", "62-caliber"), ("twenty twenty-six", "2026"), ("sixty years", "60 years"), ("EA-18G", "EA-18G"),
           ("VX-23", "VX-23"), ("VX-20", "VX-20"), ("twenty twenty-two", "2022"), ("twenty twenty-three", "2023"), ("twenty twenty-four", "2024"),
           ("twenty twenty", "2020"), ("one thousand ninety-two", "1,092"), ("one hundred thousand", "100,000"), ("four thousand five hundred fifty", "4,550"),
           ("seventy-five", "75"), ("July twenty-second, twenty seventeen", "July 22, 2017"), ("ten thousand", "10,000"),
           ("one-hundred-twenty-millimeter", "120mm"), ("hundred-twenty-millimeter", "120mm"), ("fifteen hundred shaft", "1,500 shaft"),
           ("sixty kilometers an hour", "60 km/h"), ("sixty kilometers", "60 km"), ("more than forty", "more than 40"), ("four hundred kilometers", "400 km"), ("twenty sixteen", "2016"),
           ("twenty fifteen", "2015"), ("Combined Resolve Five", "Combined Resolve V"), ("SEP version two", "SEPv2"), ("1st Battalion, 64th", "1st Battalion, 64th"),
           ("Standard Missile Two", "Standard Missile-2"), ("fifteen and a half feet", "15.5 feet"), ("fifteen hundred fifty-eight", "1,558"),
           ("ninety nautical", "90 nautical"), ("nineteen eighty-one", "1981"), ("Block Three-A", "Block IIIA"),
           ("one hundred and two", "102"), ("nineteen sixty-one", "1961"), ("sixty years", "60 years"), ("one hundred eighty-five", "185"),
           ("one hundred fifty-nine", "159"), ("seventy thousand", "70,000"), ("six hundred fifty", "650"), ("eight thousand eight hundred", "8,800"),
           ("fifty thousand", "50,000"), ("twenty nineteen", "2019"), ("fifty-eight", "58"), ("eighteen", "18")]
