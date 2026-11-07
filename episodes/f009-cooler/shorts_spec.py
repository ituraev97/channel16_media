# Shorts for STORM FILES 009. TikTok s1–s5: 62–75 s each (Creator Rewards needs > 1 min), one rescue each, own narration.
# YouTube Shorts y1–y3 (YSHORTS): 15–30 s cuts that open on the single most dramatic moment, built with PLATFORM=youtube.
# Facts: sources_shorts.md. shot: (clip_id, start, cx) — cx = horizontal centre of the 9:16 crop inside the active picture (0..1)
COOLER, PILOTS, MSTAGE, MOBILE = "939855d", 939934, 939360, 939646
CAT = 1014541 
CATF = "1014541g"  # first 70.5 s of 1014541 (HC-130 FLIR + swimmer), cropped to 4:3, duplicate frames removed + motion-interpolated
         # Alakai, 35-ft catamaran, 23 mi off Kauai, July 12, 2026 (night, 4:3)
ROCK = 973969          # four girls on a rock in Lake Superior, Aug 17, 2025 (night)
AETOS = "966645s"      # cargo ship Aetos, appendicitis, 185 mi off San Francisco, June 10, 2025 (square-pixel copy)
BLISS = "1028902s"     # Norwegian Bliss, east of Oregon Inlet, Nov 2, 2026 (square-pixel copy, 24p)

SHORTS = [
 dict(id="s1", hook="ON A COOLER<br>[IN A HURRICANE]", title="He rode out Hurricane Milton holding on to a cooler. This is how the Coast Guard found him",
      lines=[
  ("He rode out a hurricane in the open Gulf, holding on to a cooler. How did the Coast Guard find him?", [(COOLER, 3.40, .39), (COOLER, 6.60, .39)], "question", dict(label="OCT 10 · FILMED FROM ANOTHER AIRCRAFT")),
  ("This is his rescue, the day after Hurricane Milton. It starts three days earlier.", [(COOLER, 9.80, .5)], "slow", dict(label="OCT 10 · FILMED FROM ANOTHER AIRCRAFT")),
  ("October seventh, twenty twenty-four. As Coast Guard aircraft move out of Milton's path, his fishing boat, the Capt. Dave, is disabled twenty miles off John's Pass, Florida.", [(MSTAGE, 46.90, .5), (MSTAGE, 57.10, .5)], "calm", dict(label="CLEARWATER CREWS MOVE AIRCRAFT TO MOBILE · OCT 7, 2024")),
  ("A Coast Guard helicopter hoists him and a crew member. The boat is left adrift.", [(MSTAGE, 30.10, .5), (MSTAGE, 33.10, .5)], "drive", dict(label="CLEARWATER CREWS MOVE AIRCRAFT TO MOBILE · OCT 7, 2024")),
  ("Wednesday, landfall day, he goes back out at three a.m. to make repairs.", [(MOBILE, 2.80, .5)], "tense", dict(label="COAST GUARD AIRCRAFT WAIT IN MOBILE · OCT 8")),
  ("A line fouls his rudder. He's disabled again.", [(MOBILE, 28.70, .5)], "tense", dict(label="COAST GUARD AIRCRAFT WAIT IN MOBILE · OCT 8")),
  ("The Coast Guard tells him: wear a life jacket, stay with your emergency beacon.", [(MOBILE, 45.00, .5)], "calm", dict(label="COAST GUARD AIRCRAFT WAIT IN MOBILE · OCT 8")),
  ("At six forty-five that evening, they lose contact. Less than two hours later, Milton makes landfall.", [(PILOTS, 20.00, .22), (PILOTS, 100.00, .78)], "punch", dict(label="AIR STATION MIAMI PILOTS")),
  ("Thursday, these two Air Station Miami pilots search. Their direction finder picks up a signal, and they follow it.", [(PILOTS, 160.00, .22), (PILOTS, 220.00, .78)], "tense", dict(label="PILOTS LOGAN AND KLOPFENSTEIN")),
  ("Their swimmer spots something in the water. Then they see arms, raised. A man, holding on to a cooler.", [(COOLER, 15.30, .5), (COOLER, 18.50, .5)], "tense", dict(label="MOMENTS LATER · FILMED FROM ANOTHER AIRCRAFT")),
  ("Thirty miles off Longboat Key, about seventeen hours after landfall, the swimmer reaches him.", [(COOLER, 21.70, .5), (COOLER, 24.10, .5)], "drive", dict(label="OCT 10 · FILMED FROM ANOTHER AIRCRAFT")),
  ("Then he was hoisted aboard, and flown to Tampa General Hospital.", [(COOLER, 26.50, .5), (COOLER, 37.00, .5)], "calm", dict(label="OCT 10 · HOIST NOT SHOWN")),
  ("A life jacket, a beacon, and a cooler saved him, the Coast Guard said. Follow for more real rescues.", [(COOLER, 30.40, .5), (PILOTS, 300.00, .22)], "punch"),
 ]),
 dict(id="s2", hook="THEN IT<br>[SANK]", title="His catamaran was flooding 23 miles off Kauai, and he talked to the Coast Guard by text",
      lines=[
  ("His catamaran is flooding twenty-three miles off Kauai, and it might sink. What do you do?", [(CATF, 28.00, .5), (CATF, 46.80, .5)], "question"),
  ("This is Coast Guard video from that night: the Hercules, then the helicopter. But first, the call.", [(CATF, 0.40, .5)], "slow"),
  ("Sunday, July twelfth, twenty twenty-six. A thirty-five-foot catamaran, the Alakai, is sailing from Oahu to Kauai.", [(CATF, 31.00, .5), (CATF, 43.30, .5)], "calm"),
  ("Its steering fails, and it's taking on water.", [(CATF, 52.60, .5)], "tense"),
  ("At six in the evening, Coast Guard Sector Honolulu gets the report. Watchstanders talk to the owner by text message.", [(CAT, 130.00, .5), (CAT, 135.00, .5)], "calm"),
  ("They launch a Dolphin helicopter and a Hercules plane from Air Station Barbers Point, and a response boat from Station Kauai.", [(CAT, 110.00, .5), (CAT, 114.00, .5)], "drive"),
  ("The helicopter gets there. Its rescue swimmer goes into the water.", [(CATF, 34.60, .5), (CATF, 36.10, .5), (CATF, 37.70, .5)], "tense"),
  ("In the dark, the hoist camera looks straight down at the waves.", [(CAT, 120.00, .5), (CAT, 124.00, .5)], "calm"),
  ("The swimmer gets the man ready. Then the basket comes up, with him inside.", [(CAT, 170.00, .5), (CAT, 173.20, .5)], "drive"),
  ("The video doesn't show it, but shortly after the hoist, the catamaran sank.", [(CATF, 57.80, .5)], "punch", dict(label="THE CATAMARAN · FROM THE HC-130, THAT NIGHT")),
  ("The man is flown to Lihue Airport. Paramedics check him, and release him with no medical concerns.", [(CAT, 193.00, .5), (CAT, 198.00, .5)], "calm"),
  ("Down with it went thirty to forty gallons of diesel. The cause is under investigation.", [(CAT, 140.00, .5), (CAT, 146.00, .5)], "calm"),
  ("The Coast Guard's advice: carry the proper safety equipment, and wear a life jacket. It can significantly reduce the risk of drowning. Follow for more real rescues.", [(CAT, 202.10, .5), (CAT, 150.00, .5)], "punch"),
 ]),
 dict(id="s3", hook="LOST THEIR<br>[PADDLES]", title="Four girls lost their paddles on Lake Superior and got stuck on a rock into the night",
      lines=[
  ("Four girls, stuck on a rock in Lake Superior, in their swimsuits, after dark. How do you get them off?", [(ROCK, 30.00, .5), (ROCK, 33.20, .5)], "question"),
  ("This is the helicopter's infrared camera. But first, how they got there.", [(ROCK, 0.30, .5)], "slow"),
  ("August, twenty twenty-five. Four girls, ages eight to fourteen, are paddleboarding near Black Beach, in Silver Bay, Minnesota.", [(ROCK, 5.40, .5), (ROCK, 9.10, .5)], "calm"),
  ("On a small island off the beach, they lose their paddles. The waves are too big to get back.", [(ROCK, 12.80, .5)], "tense"),
  ("At about eight o'clock that Saturday night, a parent calls nine-one-one.", [(ROCK, 18.00, .5)], "calm", dict(label="COAST GUARD HOIST CAMERA · LATER THAT NIGHT")),
  ("Lake County deputies take a boat out, find the girls, and tell them to stay put.", [(ROCK, 21.70, .5), (ROCK, 23.90, .5)], "calm", dict(label="COAST GUARD HOIST CAMERA · LATER THAT NIGHT")),
  ("From a bigger island nearby, rescuers pass them blankets and food on a rope.", [(ROCK, 36.40, .5)], "calm", dict(label="COAST GUARD HOIST CAMERA · LATER THAT NIGHT")),
  ("But the water is still too rough. So the county asks the Coast Guard for a helicopter.", [(ROCK, 66.20, .5), (ROCK, 40.50, .5)], "tense", dict(label="COAST GUARD HOIST CAMERA · LATER THAT NIGHT")),
  ("A Jayhawk crew from Air Station Traverse City answers.", [(ROCK, 43.10, .5)], "drive"),
  ("In the middle of the night, the crew lowers a basket to the rock.", [(ROCK, 46.40, .5), (ROCK, 48.10, .5)], "calm"),
  ("One by one, all four girls are hoisted up into the helicopter.", [(ROCK, 49.80, .5), (ROCK, 52.40, .5)], "drive"),
  ("For one crew member, Petty Officer Lorenzo Giambanco, it's his first rescue.", [(ROCK, 57.80, .5)], "calm"),
  ("The girls are flown to a field nearby, where paramedics and their parents are waiting.", [(ROCK, 64.00, .5), (ROCK, 72.00, .5)], "calm"),
  ("Deputies told them to stay put, and they did. Follow for more real rescues.", [(ROCK, 54.20, .5), (ROCK, 83.40, .5)], "punch"),
 ]),
 dict(id="s4", hook="820 MILES<br>[OFFSHORE]", title="Appendicitis 820 miles out at sea: how the Coast Guard reached him at 185",
      lines=[
  ("Appendicitis, on a cargo ship eight hundred twenty miles offshore. How do you get him to a hospital?", [(AETOS, 41.80, .5), (AETOS, 45.20, .5)], "question"),
  ("This is the Coast Guard helicopter that came for him. But it took two days.", [(AETOS, 13.40, .5)], "slow"),
  ("June, twenty twenty-five. A Sunday, about ten in the morning.", [(AETOS, 0.40, .5)], "calm"),
  ("The captain of the cargo ship Aetos calls the Coast Guard. A forty-year-old crew member has symptoms of appendicitis.", [(AETOS, 6.70, .5), (AETOS, 10.10, .5)], "tense"),
  ("The ship is about eight hundred twenty miles offshore.", [(AETOS, 19.30, .5)], "punch"),
  ("Watchstanders advise the captain to meet a helicopter at a rendezvous point, much closer to the coast.", [(AETOS, 22.70, .5)], "calm"),
  ("A Jayhawk crew from Air Station Ventura refuels in San Francisco.", [(AETOS, 50.70, .5), (AETOS, 53.00, .5)], "drive"),
  ("Tuesday, about five in the evening, they head out to sea.", [(AETOS, 28.60, .5)], "calm"),
  ("By seven, they're over the Aetos, a hundred eighty-five miles offshore.", [(AETOS, 32.90, .5)], "drive"),
  ("On deck, the rescue swimmer gets the patient ready.", [(AETOS, 36.60, .5), (AETOS, 38.40, .5)], "tense"),
  ("Then the basket comes up from the deck, with the patient inside.", [(AETOS, 56.30, .5)], "drive"),
  ("Into the cabin.", [(AETOS, 71.10, .5)], "calm"),
  ("The crew flies him to San Francisco International Airport.", [(AETOS, 62.20, .5)], "calm"),
  ("At about nine that night, he's handed to waiting paramedics. Two days, and hundreds of miles, after the first call. Follow for more real rescues.", [(AETOS, 72.60, .5), (AETOS, 65.60, .5)], "punch"),
 ]),
 dict(id="s5", hook="THE NURSE<br>[WENT UP TOO]", title="A cruise passenger needs a hospital, and the ship's nurse goes up the cable with her",
      lines=[
  ("A cruise ship off North Carolina. A passenger needs a hospital, and the ship's nurse goes with her, up the cable.", [(BLISS, 138.50, .0), (BLISS, 142.50, .5)], "question"),
  ("This is the hoist camera on a Coast Guard helicopter. Here's how it happened.", [(BLISS, 0.50, .5)], "slow"),
  ("November second, twenty twenty-six. The cruise ship Norwegian Bliss is about thirty-two miles off Oregon Inlet, on North Carolina's Outer Banks.", [(BLISS, 5.70, .5), (BLISS, 10.10, .5)], "calm"),
  ("A sixty-three-year-old passenger needs medical attention, and the ship calls for help.", [(BLISS, 14.50, .5)], "tense"),
  ("An aircrew from Air Station Elizabeth City flies out to meet the ship.", [(BLISS, 19.20, .5), (BLISS, 21.20, .5)], "drive"),
  ("First, the rescue swimmer goes down the cable to the deck.", [(BLISS, 25.00, .5), (BLISS, 29.00, .5)], "calm"),
  ("He works with the crew below to get the patient into a rescue litter.", [(BLISS, 33.00, .5), (BLISS, 37.00, .5)], "calm"),
  ("Then the litter comes up, with the swimmer guiding it.", [(BLISS, 47.00, .5), (BLISS, 55.00, .5)], "drive"),
  ("Up to the door, and into the helicopter.", [(BLISS, 63.00, .5)], "calm"),
  ("Then the cable goes back down, for the onboard nurse.", [(BLISS, 104.00, .5), (BLISS, 108.00, .5)], "calm"),
  ("The nurse comes up with the swimmer, the two of them on one cable.", [(BLISS, 146.50, .5), (BLISS, 150.50, .5)], "tense"),
  ("Then the helicopter pulls away from the ship, and heads for Virginia.", [(BLISS, 161.50, .5), (BLISS, 166.00, .5)], "calm"),
  ("They fly to Sentara Norfolk General Hospital, in Virginia. A local station reported she was in stable condition.", [(BLISS, 172.00, .5), (BLISS, 176.50, .5)], "calm"),
  ("Far from shore, help still comes. Follow for more real rescues.", [(BLISS, 181.00, .5), (BLISS, 124.00, .5)], "punch"),
 ]),
]

# YouTube Shorts (15–30 s): open on the most dramatic shot, one-line hook, payoff line + CTA. Windows may reuse the TikTok cut's footage (separate video).
YSHORTS = [
 dict(id="y1", hook="ON A COOLER<br>[IN A HURRICANE]", title="He rode out a hurricane holding on to a cooler",
      lines=[
  ("He rode out Hurricane Milton in the open Gulf, holding on to a cooler.", [(COOLER, 3.40, .39), (COOLER, 6.60, .39)], "tense", dict(label="OCT 10 · FILMED FROM ANOTHER AIRCRAFT")),
  ("A Coast Guard crew found him about thirty miles off Longboat Key, the day after landfall.", [(COOLER, 16.40, .5), (COOLER, 19.60, .5)], "drive", dict(label="OCT 10 · FILMED FROM ANOTHER AIRCRAFT")),
  ("A life jacket, a beacon, and a cooler saved him. Full story on our channel.", [(COOLER, 22.80, .5), (COOLER, 26.30, .5)], "punch", dict(label="OCT 10 · FILMED FROM ANOTHER AIRCRAFT")),
 ]),
 dict(id="y2", hook="THEN IT<br>[SANK]", title="His catamaran sank right after this rescue",
      lines=[
  ("Twenty-three miles off Kauai, his catamaran is flooding, and he's texting with the Coast Guard.", [(CAT, 170.00, .5), (CATF, 46.80, .5)], "tense"),
  ("A rescue swimmer goes into the water. The basket lifts the man out.", [(CATF, 34.40, .5), (CAT, 173.20, .5)], "drive"),
  ("Shortly after, the boat sinks. Paramedics release him with no medical concerns. Follow for more real rescues.", [(CATF, 57.80, .5), (CAT, 193.00, .5)], "punch"),
 ]),
 dict(id="y3", hook="LOST THEIR<br>[PADDLES]", title="Four girls lost their paddles on Lake Superior",
      lines=[
  ("Four girls lost their paddles, and got stuck on a rock in Lake Superior, in their swimsuits, after dark.", [(ROCK, 30.00, .5), (ROCK, 3.40, .5)], "tense"),
  ("A Coast Guard Jayhawk lowers a basket, and hoists them up, one by one.", [(ROCK, 44.00, .5), (ROCK, 48.40, .5)], "drive"),
  ("All four were flown to a field where their parents were waiting. Follow for more real rescues.", [(ROCK, 64.00, .5), (ROCK, 54.30, .5)], "punch"),
 ]),
]

DISPLAY = [
 ("October seventh, twenty twenty-four", "October 7, 2024"), ("twenty miles", "20 miles"), ("six- to eight-foot", "6- to 8-foot"), ("six forty-five", "6:45"),
 ("thirty miles", "30 miles"), ("seventeen hours", "17 hours"), ("twenty-three miles", "23 miles"), ("July twelfth, twenty twenty-six", "July 12, 2026"),
 ("thirty-five-foot", "35-foot"), ("thirty to forty gallons", "30 to 40 gallons"), ("three to four gallons", "3 to 4 gallons"), ("twenty twenty-five", "2025"),
 ("eight to fourteen", "8 to 14"), ("nine-one-one", "911"), ("eight hundred twenty miles", "820 miles"), ("forty-year-old", "40-year-old"),
 ("a hundred eighty-five miles", "185 miles"), ("November second, twenty twenty-six", "November 2, 2026"), ("thirty-two miles", "32 miles"),
 ("sixty-three-year-old", "63-year-old"), ("Twenty-three miles", "23 miles"), ("three a.m.", "3 a.m."),
]
CTA = "FOLLOW FOR MORE REAL RESCUES"
YCTA = "FULL STORY ON OUR CHANNEL"
