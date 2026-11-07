# CHANNEL 16 · STORM FILES 009 — Two storms, one cooler (Hurricanes Helene and Milton, Florida's Gulf coast, Sept.–Oct. 2024)
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

HSTAGE = 937908    # Air Station Clearwater stages in West Palm Beach before Helene, Sept 25, 2024 (PO3 Santiago Gomez)
MAYPORT = 938016   # Station Mayport prepares for Helene, Sept 25, 2024 (PO3 Vincent Moreno)
GULFPORT = 938233  # Air Station Clearwater hoists a man from the water near Gulfport, Sept 27, 2024 (vertical hoist camera)
HRESP = 938595     # Air Station Clearwater aircrews launch from West Palm Beach, Sept 25-27, 2024 (PO3 Santiago Gomez)
HASSESS = 938294   # Air Station Clearwater overflight of Helene damage, Sept 27, 2024
PREM = 939530      # Air Station Miami overflight of Tampa Bay before Milton (PO3 Nicholas Strasburg)
MSTAGE = 939360    # Air Station Clearwater moves aircraft to ATC Mobile, Oct 7, 2024 (PO3 Santiago Gomez)
VENT = 939451      # Cutter Venturous relocates, 7-8 ft seas, Oct 7, 2024
RESOL = 939658     # Cutter Resolute relocates toward Pensacola, Oct 8, 2024 (vertical)
MOBILE = 939646    # Clearwater + ATC Mobile prepare aircraft in Mobile, Oct 8, 2024 (PO1 Riley Perkofski)
COOLER = "939855d"   # Air Station Miami rescues the man clinging to a cooler ~30 mi off Longboat Key (courtesy video)
PILOTS = 939934    # Lt. Ian Logan and Lt. Landon Klopfenstein, Air Station Miami, interview (PO3 Nicholas Strasburg)
POSTM = 939937     # Air Station Miami airplane crews fly the west coast after Milton, Oct 10, 2024
CUTTERS = 940014   # HC-144 over cutters Thetis, Resolute, Pablo Valent off Tampa Bay, Oct 11, 2024 (PO2 Ryan Pierce)
DAMAGE = 940566    # Coast Guard property damage after Helene and Milton (PO2 Jose Hernandez, PO2 Ian Gray) - 24p
ATON = 940869      # Aids to Navigation Teams after Milton, Oct 16, 2024 (vertical)

GULF = [[-89.0, 31.4], [-79.8, 24.4]]              # eastern Gulf + Florida
BAY = [[-83.55, 28.25], [-82.2, 26.95]]            # Tampa Bay to Venice, with the Gulf
PERRY = [-83.58, 30.12]; TAMPA = [-82.46, 27.95]; STPETE = [-82.64, 27.77]; CLEARWATER = [-82.69, 27.91]; SIESTA = [-82.55, 27.27]
LONGBOAT = [-82.66, 27.41]; JOHNSPASS = [-82.78, 27.78]; GULFPORT_LL = [-82.71, 27.74]; MOBILE_LL = [-88.13, 30.69]; MIAMI = [-80.28, 25.91]
OFF_JP = [-83.12, 27.78]       # ~20 mi west of John's Pass (illustrative)
OFF_LBK = [-83.18, 27.36]      # ~30 mi off Longboat Key (illustrative)
WPB = [-80.05, 26.68]; MAYPORT_LL = [-81.40, 30.39]; VENICE = [-82.45, 27.10]

LINES = [
 # ---------------- COLD OPEN ----------------
 ("October tenth, twenty twenty-four. About thirty miles off Longboat Key, Florida, in the Gulf of Mexico.",
  [C(COOLER, 0.4), C(COOLER, 3.4)], dict(tag=("30 MILES OFF LONGBOAT KEY, FLA.", "OCT 10, 2024"), kind="calm")),
 ("Hurricane Milton came ashore the night before.",
  [C(COOLER, 7.0)], dict(kind="punch")),
 ("Down there, a man in a life jacket is holding on to a large cooler. He has been out here through the hurricane, and through the night.",
  [C(COOLER, 10.0), C(COOLER, 13.2)], dict(kind="tense")),
 ("A Coast Guard helicopter crew from Air Station Miami has just found him.",
  [C(COOLER, 16.4), C(COOLER, 19.4)], dict(kind="drive")),
 ("The Coast Guard's estimate of what he lived through: winds of seventy-five to ninety miles an hour, and seas of twenty to twenty-five feet, for hours, including overnight.",
  [G("stat", a="20–25 FT", b="ESTIMATED SEAS HE ENDURED", c="WINDS 75–90 MPH · INCLUDING OVERNIGHT · SOURCE: U.S. COAST GUARD SECTOR ST. PETERSBURG")], dict(kind="tense")),
 ("He survived, the Coast Guard said, because of three things. A life jacket. An emergency beacon. And a cooler.",
  [G("cards3", kicker="U.S. COAST GUARD · OCT. 10, 2024", title="WHY HE SURVIVED",
     cards=[dict(h="1", t="A life jacket"), dict(h="2", t="An emergency beacon (EPIRB)"), dict(h="3", t="A cooler")],
     footer="SOURCE: U.S. COAST GUARD SECTOR ST. PETERSBURG")], dict(kind="slow")),
 ("This is the story of two hurricanes in two weeks, and the fishing captain who went back out.",
  [G("title", title="Two storms.<br><span style=\"color:#FF5B14\">One cooler.</span>", sub="STORM FILES · 009", size=220)], dict(kind="slow", gap=2.6)),

 # ---------------- I. HELENE ----------------
 ("It starts two weeks earlier, with a different storm.",
  [G("chapter", case="STORM FILES", n="I", t="HELENE")], dict(kind="calm")),
 ("September twenty-fifth. As Hurricane Helene approached, Air Station Clearwater's crews staged their aircraft in West Palm Beach, on the other side of Florida.",
  [C(HSTAGE, 0.2), C(HSTAGE, 3.3), C(HSTAGE, 9.9)], dict(tag=("WEST PALM BEACH, FLA.", "SEPT 25, 2024"), kind="calm")),
 ("On the Atlantic side, at Station Mayport, crews stacked sandbags against the doors, and secured their boats.",
  [C(MAYPORT, 0.3), C(MAYPORT, 3.5), C(MAYPORT, 17.5)], dict(tag=("STATION MAYPORT, FLA.", "SEPT 25, 2024"), kind="calm")),
 ("Helene came ashore far to the north, in Florida's Big Bend near Perry, at eleven ten on the night of September twenty-sixth. A Category four, with winds of one hundred forty miles an hour.",
  [G("map", map=dict(bounds=GULF, rings=[dict(ll=PERRY, r=45, n=3, d=0.3, color="#FF5B14")],
     cities=[dict(ll=PERRY, name="PERRY", sub="LANDFALL · 11:10 P.M. EDT", d=0.4, color="#FF5B14"), dict(ll=TAMPA, name="TAMPA BAY", d=0.9, anchor="end"),
             dict(ll=MOBILE_LL, name="MOBILE", d=1.1, size=28), dict(ll=MIAMI, name="MIAMI", d=1.2, size=28, anchor="end")]),
     kicker="SEPTEMBER 26, 2024", title="HELENE · CATEGORY 4 · 140 MPH", footer="SOURCE: NOAA NESDIS")], dict(kind="drive")),
 ("But on its way past, it pushed the Gulf into Tampa Bay. Every working tide gauge from Clearwater to Venice logged a record.",
  [G("stat", a="RECORD", b="EVERY REPORTING TIDE GAUGE, CLEARWATER TO VENICE", c="WUSF ANALYSIS OF NOAA AND USGS DATA")], dict(kind="tense")),
 ("From West Palm Beach, Clearwater's Jayhawk helicopters and C-27 Spartan planes launched on search and rescue cases and overflights, by day and by night.",
  [C(HRESP, 18.6), C(HRESP, 30.9), C(HRESP, 54.2), C(HRESP, 64.3)], dict(tag=("AIR STATION CLEARWATER CREWS", "SEPT 25–27, 2024"), kind="drive")),
 ("The day after landfall, a Clearwater helicopter crew flew the coast to see the damage.",
  [C(HASSESS, 1.0), C(HASSESS, 19.0), C(HASSESS, 28.5)], dict(tag=("FLORIDA'S WEST COAST", "SEPT 27, 2024"), kind="calm")),
 ("Near the Gulfport municipal marina, the same air station had a man in the water.",
  [C(GULFPORT, 0.4), C(GULFPORT, 4.2)], dict(tag=("GULFPORT, FLA.", "SEPT 27, 2024"), kind="tense")),
 ("The thirty-two-foot sailboat he was aboard had become disabled, and he had tried to swim ashore.",
  [C(GULFPORT, 7.0)], dict(kind="tense")),
 ("The rescue swimmer went down on the cable. Then the basket came up, with the man inside.",
  [C(GULFPORT, 11.2), C(GULFPORT, 19.6)], dict(kind="drive")),
 ("He was flown to Albert Whitted Airport in St. Petersburg, with no reported medical concerns.",
  [C(GULFPORT, 24.8), C(GULFPORT, 28.0)], dict(kind="calm")),
 ("The Coast Guard's count for Helene: twenty-one lives saved or assisted, and five pets, from Florida to western North Carolina.",
  [G("cards3", kicker="U.S. COAST GUARD · HURRICANE HELENE", title="THE COUNT",
     cards=[dict(h="21", t="Lives saved or assisted"), dict(h="5", t="Pets rescued"), dict(h="12", t="Ports in the response")],
     footer="SOURCE: U.S. COAST GUARD NEWS RELEASE, OCT. 1, 2024")], dict(kind="calm")),
 ("And before that coast had finished cleaning up, another storm was coming.",
  [C(PREM, 42.0), C(PREM, 45.2)], dict(kind="slow", gap=0.8)),

 # ---------------- II. MILTON ----------------
 ("Its name was Milton.",
  [G("chapter", case="STORM FILES", n="II", t="MILTON")], dict(kind="punch")),
 ("In the Gulf, Milton became one of the most powerful Atlantic hurricanes on record. The National Hurricane Center estimates its peak winds at one hundred seventy-eight miles an hour.",
  [G("stat", a="178 MPH", b="MILTON'S ESTIMATED PEAK WINDS", c="895 MB · TIED FOR 4TH-LOWEST ATLANTIC PRESSURE ON RECORD · NHC FINAL REPORT VIA WFLA")], dict(kind="drive")),
 ("And it was headed for the same coast Helene had just flooded.",
  [C(PREM, 30.2), C(PREM, 33.0)], dict(tag=("TAMPA BAY, FLA.", "BEFORE MILTON"), kind="tense")),
 ("Before Milton arrived, an Air Station Miami aircrew flew over Tampa Bay to look at the coast, which was still recovering from Helene.",
  [C(PREM, 6.2), C(PREM, 12.0), C(PREM, 17.0)], dict(tag=("TAMPA BAY, FLA.", "AIR STATION MIAMI AIRCREW"), kind="calm")),
 ("On Monday, October seventh, Air Station Clearwater began moving its planes and helicopters out of the storm's way, to the Coast Guard's Aviation Training Center in Mobile, Alabama.",
  [C(MSTAGE, 15.3), C(MSTAGE, 46.9), C(MSTAGE, 124.0)], dict(tag=("AIR STATION CLEARWATER, FLA.", "OCT 7, 2024"), kind="drive")),
 ("Cutters relocated too. The Venturous rode through seven- to eight-foot seas, six hundred miles northeast of the storm.",
  [C(VENT, 2.0), C(VENT, 30.0), C(RESOL, 20.5)], dict(kind="calm")),
 ("That same Monday, at about twelve forty in the afternoon, a call came in to Sector St. Petersburg.",
  [G("callcard", kicker="SECTOR ST. PETERSBURG · MONDAY, OCT. 7", title="12:40 P.M.",
     rows=[["VESSEL", "FISHING VESSEL CAPT. DAVE"], ["ABOARD", "CAPTAIN + 1 CREW MEMBER"], ["STATUS", "DISABLED"], ["POSITION", "ABOUT 20 MI OFF JOHN'S PASS"]],
     footer="SOURCE: U.S. COAST GUARD NEWS RELEASE, OCT. 10, 2024")], dict(kind="calm")),
 ("The captain of a fishing boat, the Capt. Dave, reported that he and a crew member were disabled, about twenty miles off John's Pass.",
  [G("callcard", kicker="SECTOR ST. PETERSBURG · MONDAY, OCT. 7", title="12:40 P.M.",
     rows=[["VESSEL", "FISHING VESSEL CAPT. DAVE"], ["ABOARD", "CAPTAIN + 1 CREW MEMBER"], ["STATUS", "DISABLED"], ["POSITION", "ABOUT 20 MI OFF JOHN'S PASS"]],
     footer="SOURCE: U.S. COAST GUARD NEWS RELEASE, OCT. 10, 2024")], dict(kind="tense")),
 ("A boat crew from Station Sand Key and an Air Station Clearwater helicopter went out. The helicopter crew hoisted both of them, and brought them back to the air station in good condition.",
  [G("map", map=dict(bounds=BAY, rings=[dict(ll=OFF_JP, r=40, n=3, d=0.3, color="#FF5B14")],
     cities=[dict(ll=OFF_JP, name="CAPT. DAVE", sub="POSITION APPROX.", d=0.4, color="#FF5B14", anchor="end"), dict(ll=JOHNSPASS, name="JOHN'S PASS", d=0.8),
             dict(ll=CLEARWATER, name="AIR STATION CLEARWATER", d=1.0, size=28), dict(ll=LONGBOAT, name="LONGBOAT KEY", d=1.2, size=28)]),
     kicker="MONDAY, OCTOBER 7, 2024", title="THE FIRST RESCUE", footer="SOURCE: U.S. COAST GUARD")], dict(kind="drive")),
 ("The boat was left adrift, and salvage was being arranged.",
  [G("map", map=dict(bounds=BAY, rings=[dict(ll=OFF_JP, r=40, n=3, d=0.3, color="#8DA2AE")],
     cities=[dict(ll=OFF_JP, name="CAPT. DAVE", sub="LEFT ADRIFT", d=0.4, color="#8DA2AE", anchor="end"), dict(ll=JOHNSPASS, name="JOHN'S PASS", d=0.8),
             dict(ll=CLEARWATER, name="AIR STATION CLEARWATER", d=1.0, size=28), dict(ll=LONGBOAT, name="LONGBOAT KEY", d=1.2, size=28)]),
     kicker="MONDAY, OCTOBER 7, 2024", title="NO ONE ABOARD", footer="POSITION APPROXIMATE · SOURCE: U.S. COAST GUARD")], dict(kind="punch", gap=0.8)),

 # ---------------- III. BACK OUT ----------------
 ("Two days later, on the day Milton was due to make landfall, the captain went back.",
  [G("chapter", case="STORM FILES", n="III", t="BACK OUT")], dict(kind="calm")),
 ("Wednesday, October ninth. At about noon, the boat's owner called the Coast Guard. The captain had gone back out at about three that morning, to make repairs. And he hadn't checked in.",
  [G("timeline", kicker="WEDNESDAY, OCTOBER 9, 2024", title="LANDFALL DAY",
     events=[dict(y="3 A.M.", t="Captain goes back out to the boat"), dict(y="≈ NOON", t="Owner reports: no check-in"), dict(y="6:45 P.M.", t="Communication lost"), dict(y="≈ 8:30 P.M.", t="Milton makes landfall")],
     footer="SOURCES: U.S. COAST GUARD · WWSB/ABC7 SARASOTA")], dict(kind="tense")),
 ("Watchstanders reached him by radio. His rudder was fouled with a line. The boat was disabled again, on his way back to port.",
  [G("callcard", kicker="SECTOR ST. PETERSBURG · WED., OCT. 9", title="RADIO CONTACT",
     rows=[["CAUSE", "RUDDER FOULED WITH A LINE"], ["STATUS", "DISABLED AGAIN"], ["SEAS", "6–8 FT"], ["WIND", "ABOUT 30 MPH · WORSENING"]],
     footer="SOURCE: U.S. COAST GUARD NEWS RELEASE, OCT. 10, 2024")], dict(kind="calm")),
 ("Out there, the seas were already six to eight feet, with winds around thirty miles an hour, and getting worse as the storm came closer.",
  [G("cards3", kicker="WEDNESDAY AFTERNOON", title="CONDITIONS AT THE BOAT",
     cards=[dict(h="6–8 FT", t="Seas"), dict(h="≈30 MPH", t="Winds"), dict(h="WORSE", t="As Milton approached")],
     footer="SOURCE: U.S. COAST GUARD")], dict(kind="tense")),
 ("The Coast Guard told him two things. Put on a life jacket. And stay with the boat's emergency beacon, its EPIRB.",
  [G("steps", kicker="U.S. COAST GUARD · WEDNESDAY, OCT. 9", title="TWO INSTRUCTIONS",
     items=[["Life jacket", "Put it on"], ["EPIRB", "Stay with the emergency beacon"]], active=1,
     footer="SOURCE: U.S. COAST GUARD NEWS RELEASE")], dict(kind="slow")),
 ("An EPIRB is a distress beacon. Switched on, it sends a distress signal to satellites, so rescuers know someone is in trouble.",
  [G("steps", kicker="EMERGENCY POSITION-INDICATING RADIO BEACON", title="THE EPIRB",
     items=[["Switch on", "Manually or automatically"], ["Transmit", "A distress signal, via satellite"]], active=1,
     footer="SOURCE: NOAA SARSAT")], dict(kind="calm")),
 ("By then, Clearwater's helicopters were in Mobile, Alabama, out of the storm's path.",
  [C(MOBILE, 5.4), C(MOBILE, 28.3)], dict(tag=("MOBILE, ALA.", "OCT 8, 2024"), kind="calm")),
 ("There, crews from Clearwater and the Aviation Training Center worked on the aircraft, so they would be ready to help once Milton had passed.",
  [C(MOBILE, 13.5), C(MOBILE, 36.9), C(MOBILE, 45.0)], dict(kind="calm")),
 ("Across the region, the Coast Guard had twenty-seven aircraft and thirty cutters ready to respond. And its message to everyone else was three words. Stay off the water.",
  [G("cards3", kicker="U.S. COAST GUARD · OCT. 9, 2024", title="READY FOR MILTON",
     cards=[dict(h="27", t="Aircraft, 17 on immediate standby"), dict(h="30", t="Cutters, 10 underway"), dict(h="3 WORDS", t="\"Stay off the water.\"")],
     footer="SOURCE: U.S. COAST GUARD NEWS RELEASE, OCT. 9, 2024")], dict(kind="calm")),
 ("At about six forty-five that evening, the Coast Guard lost communication with the captain.",
  [G("timeline", kicker="WEDNESDAY, OCTOBER 9, 2024", title="LANDFALL DAY",
     events=[dict(y="3 A.M.", t="Captain goes back out to the boat"), dict(y="≈ NOON", t="Owner reports: no check-in"), dict(y="6:45 P.M.", t="Communication lost"), dict(y="≈ 8:30 P.M.", t="Milton makes landfall")],
     footer="SOURCES: U.S. COAST GUARD · WWSB/ABC7 SARASOTA")], dict(kind="punch")),
 ("Less than two hours later, Milton made landfall near Siesta Key, as a Category three hurricane.",
  [G("map", map=dict(bounds=BAY, rings=[dict(ll=SIESTA, r=45, n=3, d=0.3, color="#FF5B14")],
     cities=[dict(ll=SIESTA, name="SIESTA KEY", sub="LANDFALL · ≈8:30 P.M.", d=0.4, color="#FF5B14"), dict(ll=LONGBOAT, name="LONGBOAT KEY", d=0.8),
             dict(ll=TAMPA, name="TAMPA", d=1.0, size=28), dict(ll=STPETE, name="ST. PETERSBURG", d=1.1, size=28, anchor="end")]),
     kicker="WEDNESDAY, OCTOBER 9, 2024", title="MILTON · CATEGORY 3", footer="SOURCE: WWSB/ABC7 SARASOTA · NHC")], dict(kind="drive")),
 ("Milton spawned forty-five known tornadoes on land. Near St. Petersburg, more than twenty inches of rain fell. From Venice south to Boca Grande, the surge reached six to nine feet.",
  [G("cards3", kicker="HURRICANE MILTON · NHC FINAL REPORT", title="THE STORM",
     cards=[dict(h="45", t="Known tornadoes on land"), dict(h="20+ IN", t="Rain near St. Petersburg"), dict(h="6–9 FT", t="Surge, Venice to Boca Grande")],
     footer="SOURCE: NHC FINAL REPORT VIA WFLA")], dict(kind="tense")),
 ("Helene and Milton made landfall in Florida just thirteen days apart. And the storms hit the Coast Guard's own facilities, too.",
  [C(DAMAGE, 54.2), C(DAMAGE, 57.3), C(DAMAGE, 60.2)], dict(kind="calm")),
 ("And somewhere out in the Gulf, the captain was riding it out. He would be found about seventeen hours after landfall.",
  [G("stat", a="≈17 HRS", b="FROM MILTON'S LANDFALL TO THE RESCUE", c="SOURCE: NPR, OCT. 11, 2024")], dict(kind="slow", gap=0.8)),

 # ---------------- IV. THE SEARCH ----------------
 ("Thursday morning, the search started again.",
  [G("chapter", case="STORM FILES", n="IV", t="THE SEARCH")], dict(kind="calm")),
 ("Clearwater's aircrews were in Mobile, out of the storm. At about five thirty in the morning, a crew from Air Station Miami launched to look for the missing captain.",
  [G("map", map=dict(bounds=GULF, arcs=[dict(**{"from": MIAMI, "to": OFF_LBK}, d=0.5, dur=1.2, bend=-0.18)],
     rings=[dict(ll=OFF_LBK, r=35, n=3, d=1.5, color="#FF5B14")],
     cities=[dict(ll=MIAMI, name="AIR STATION MIAMI", sub="LAUNCH ≈5:30 A.M.", d=0.3, anchor="end"), dict(ll=OFF_LBK, name="SEARCH AREA", sub="APPROX.", d=1.5, color="#FF5B14", anchor="end"),
             dict(ll=MOBILE_LL, name="MOBILE", sub="CLEARWATER'S AIRCRAFT", d=0.9, size=28)]),
     kicker="THURSDAY, OCTOBER 10, 2024", title="THE SEARCH", footer="SOURCE: U.S. COAST GUARD")], dict(kind="drive")),
 ("Two of its pilots, Lieutenant Landon Klopfenstein and Lieutenant Ian Logan, later described the search to NPR.",
  [C(PILOTS, 8.0), C(PILOTS, 96.0)], dict(tag=("PILOTS LOGAN AND KLOPFENSTEIN", "AIR STATION MIAMI"), kind="calm")),
 ("They searched with his description and a search pattern. Logan put it this way: it's a lot of math that determines where we're gonna go and search, because we have limited resources, limited fuel.",
  [G("quote", q="It's a lot of math that determines where we're gonna go and search because we have limited resources, limited fuel.", w="LT. IAN LOGAN · AIR STATION MIAMI · VIA NPR")], dict(kind="calm")),
 ("Another helicopter was flying the same pattern. And the crew was told to head back toward the coast.",
  [C(PILOTS, 150.0), C(PILOTS, 186.0)], dict(kind="tense")),
 ("Then their direction-finding equipment picked up an alert. A signal, coming in bursts about once a minute. They decided to follow it.",
  [G("callcard", kicker="AIR STATION MIAMI HELICOPTER · THURSDAY", title="SIGNAL",
     rows=[["SIGNAL", "UNIDENTIFIED · DIRECTION-FINDING ALERT"], ["RECEIVED BY", "DIRECTION-FINDING EQUIPMENT"], ["PATTERN", "BURSTS, ABOUT ONCE A MINUTE"], ["ACTION", "FOLLOW THE BEARING LINES"]],
     footer="SOURCE: NPR, OCT. 11, 2024")], dict(kind="tense")),
 ("One of the pilots remembered the moment. As we were trucking that way, our swimmer noticed some debris, or an object, about two o'clock on the aircraft.",
  [G("quote", q="As we were trucking that way, our swimmer noticed some debris or an object about 2 o'clock on the aircraft.", w="AIR STATION MIAMI PILOT · VIA NPR")], dict(kind="calm")),
 ("They turned toward it, following the bearing lines.",
  [C(PILOTS, 222.0)], dict(kind="drive")),
 ("Then they saw arms, raised in the air. A man, holding on to a large cooler. This Coast Guard video picks up moments later, filmed from another aircraft.",
  [C(COOLER, 22.0), C(COOLER, 25.4)], dict(kind="tense")),
 ("It was about one thirty in the afternoon, roughly thirty miles off Longboat Key.",
  [G("map", map=dict(bounds=BAY, rings=[dict(ll=OFF_LBK, r=40, n=3, d=0.3, color="#FF5B14")],
     cities=[dict(ll=OFF_LBK, name="FOUND", sub="≈30 MI OFF LONGBOAT KEY · APPROX.", d=0.4, color="#FF5B14"), dict(ll=LONGBOAT, name="LONGBOAT KEY", d=0.8),
             dict(ll=SIESTA, name="SIESTA KEY", d=1.0, size=28), dict(ll=TAMPA, name="TAMPA", d=1.2, size=28)]),
     kicker="THURSDAY, OCTOBER 10, 2024 · ≈1:30 P.M.", title="FOUND", footer="POSITION ILLUSTRATIVE · SOURCE: U.S. COAST GUARD")], dict(kind="calm")),
 ("The swimmer was lowered into the water beside him. Then, off camera, the captain was hoisted aboard.",
  [C(COOLER, 28.4), C(COOLER, 34.6)], dict(kind="drive")),
 ("Klopfenstein called it a miracle. We couldn't believe it, honestly, he said, that he was OK.",
  [G("quote", q="We couldn't believe it, honestly, that he was OK.", w="LT. LANDON KLOPFENSTEIN · AIR STATION MIAMI · VIA NPR")], dict(kind="slow")),
 ("He was flown to Tampa General Hospital.",
  [C(COOLER, 39.6)], dict(kind="calm")),
 ("Lieutenant Commander Dana Grady, who leads Sector St. Petersburg's command center, put it simply. This man survived in a nightmare scenario, for even the most experienced mariner.",
  [G("quote", q="This man survived in a nightmare scenario for even the most experienced mariner.", w="LT. CMDR. DANA GRADY · SECTOR ST. PETERSBURG")], dict(kind="slow", gap=0.8)),

 # ---------------- V. AFTER ----------------
 ("Milton was gone. The work wasn't.",
  [G("chapter", case="STORM FILES", n="V", t="AFTER")], dict(kind="punch")),
 ("On October tenth, Air Station Miami's airplane crews flew Florida's west coast, looking for people in distress, and assessing the damage.",
  [C(POSTM, 1.0), C(POSTM, 46.0), C(POSTM, 65.0)], dict(tag=("FLORIDA'S WEST COAST", "OCT 10, 2024"), kind="calm")),
 ("The next day, three cutters, the Thetis, the Resolute and the Pablo Valent, patrolled off Tampa Bay, to cover offshore search and rescue for Sector St. Petersburg and Air Station Clearwater. Both had been impacted by Helene and Milton.",
  [C(CUTTERS, 1.0), C(CUTTERS, 10.0), C(CUTTERS, 19.0)], dict(tag=("OFF TAMPA BAY, FLA.", "OCT 11, 2024"), kind="calm")),
 ("At Air Station Clearwater, the district commander, Rear Admiral Douglas Schofield, talked about what the two storms had done to the Coast Guard's own property. Then the aircrews went back to work.",
  [C(DAMAGE, 69.0), C(DAMAGE, 92.5), C(DAMAGE, 97.0)], dict(tag=("AIR STATION CLEARWATER, FLA.", "OCT. 2024"), kind="calm")),
 ("Along that coast there are more than thirteen hundred aids to navigation, from Fort Myers to Cedar Key. Teams from six Coast Guard units joined forces to check them, and repair the critical ones.",
  [C(ATON, 2.0), C(ATON, 18.0)], dict(tag=("FLORIDA'S GULF COAST", "OCT 16, 2024"), kind="calm")),
 ("Across both storms, in two weeks, the Coast Guard counted thirty-seven lives saved or assisted, and eight pets rescued.",
  [G("stat", a="37", b="LIVES SAVED OR ASSISTED · HELENE AND MILTON", c="AND 8 PETS · IN TWO WEEKS · SOURCE: U.S. COAST GUARD VIA DVIDS")], dict(kind="drive")),
 ("So what kept one fishing captain alive through a major hurricane, in open water?",
  [G("steps", kicker="HURRICANE MILTON", title="WHAT THE COAST GUARD CREDITS",
     items=[["Life jacket", "He was wearing it"], ["EPIRB", "The Coast Guard credited it"], ["A cooler", "Something that floats"], ["Lesson", "Stay off the water"]])], dict(kind="question")),
 ("First: the life jacket. He was still wearing it when the crew found him.",
  [C(PILOTS, 300.0)], dict(kind="calm")),
 ("Second: the beacon. The Coast Guard counted it among the reasons he survived. Klopfenstein's summary: survival equipment is priceless.",
  [G("quote", q="Survival equipment is priceless.", w="LT. LANDON KLOPFENSTEIN · AIR STATION MIAMI · VIA NPR")], dict(kind="calm")),
 ("Third: something that floats. He held on to that cooler.",
  [C(COOLER, 31.6)], dict(kind="calm")),
 ("And fourth, the Coast Guard's message to every mariner as Milton approached. Stay off the water.",
  [G("quote", q="Stay off the water.", w="REAR ADM. DOUGLAS SCHOFIELD · SEVENTH DISTRICT · OCT. 9, 2024")], dict(kind="punch")),
 ("The search itself began with one phone call. The boat's owner noticed that the captain hadn't checked in, and called the Coast Guard. Always tell someone your plan.",
  [C(PILOTS, 340.0)], dict(kind="calm")),
 ("Both men you saw rescued from the water in this video survived.",
  [C(GULFPORT, 31.6), C(POSTM, 75.0)], dict(kind="slow", gap=0.8)),
 ("Next time, on Channel Sixteen: the anatomy of another rescue. Stay safe out there.",
  [G("end", stamp="FOUND AFTER THE STORM")], dict(kind="calm", gap=2.4)),
]

DISPLAY = [
 ("October tenth, twenty twenty-four", "October 10, 2024"), ("thirty miles", "30 miles"), ("seventy-five to ninety miles an hour", "75 to 90 miles an hour"),
 ("twenty to twenty-five feet", "20 to 25 feet"), ("September twenty-fifth", "September 25"), ("eleven ten", "11:10"), ("September twenty-sixth", "September 26"),
 ("Category four", "Category 4"), ("one hundred forty miles an hour", "140 miles an hour"), ("thirty-two-foot", "32-foot"), ("twenty-one", "21"),
 ("five pets", "five pets"), ("one hundred seventy-eight miles an hour", "178 miles an hour"), ("October seventh", "October 7"), ("seven- to eight-foot", "7- to 8-foot"),
 ("six hundred miles", "600 miles"), ("twelve forty", "12:40"), ("twenty miles", "20 miles"), ("October ninth", "October 9"), ("six to eight feet", "6 to 8 feet"),
 ("thirty miles an hour", "30 miles an hour"), ("twenty-seven aircraft", "27 aircraft"), ("thirty cutters", "30 cutters"), ("six forty-five", "6:45"),
 ("Category three", "Category 3"), ("forty-five", "45"), ("twenty inches", "20 inches"), ("six to nine feet", "6 to 9 feet"), ("five thirty", "5:30"),
 ("one thirty", "1:30"), ("thirteen days", "13 days"), ("seventeen hours", "17 hours"), ("thirteen hundred", "1,300"), ("thirty-seven", "37"), ("Channel Sixteen", "Channel 16"),
]

META = dict(
    case="STORM FILES · 009", label="CH 16 · 156.800 MHz",
    title="He Rode Out Hurricane Milton on a Cooler. The Coast Guard Found Him",
    voice="am_eric",
    plate="Footage: U.S. Coast Guard via DVIDS · Independent channel, not affiliated with the USCG",
    credit=("Footage: U.S. Coast Guard via DVIDS (public domain). Appearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NCHANNEL 16 is an independent channel, not affiliated with the U.S. Coast Guard."),
    imgs=dict(),
)
