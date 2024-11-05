from itertools import product

# Lists of airports and airlines
# airports300 = [
#     "Hartsfield-Jackson Atlanta International Airport (ATL)", "Beijing Capital International Airport (PEK)",
#     "Los Angeles International Airport (LAX)", "Dubai International Airport (DXB)", "Tokyo Haneda Airport (HND)",
#     "Chicago O'Hare International Airport (ORD)", "London Heathrow Airport (LHR)", "Hong Kong International Airport (HKG)",
#     "Shanghai Pudong International Airport (PVG)", "Charles de Gaulle Airport (CDG)", "Dallas/Fort Worth International Airport (DFW)",
#     "Guangzhou Baiyun International Airport (CAN)", "Amsterdam Airport Schiphol (AMS)", "Frankfurt Airport (FRA)",
#     "Istanbul Airport (IST)", "Singapore Changi Airport (SIN)", "Incheon International Airport (ICN)",
#     "Denver International Airport (DEN)", "Soekarno–Hatta International Airport (CGK)", "Suvarnabhumi Airport (BKK)",
#     "Kuala Lumpur International Airport (KUL)", "San Francisco International Airport (SFO)",
#     "Indira Gandhi International Airport (DEL)", "Seattle-Tacoma International Airport (SEA)", "McCarran International Airport (LAS)",
#     "Toronto Pearson International Airport (YYZ)", "Miami International Airport (MIA)", "Orlando International Airport (MCO)",
#     "Barcelona-El Prat Airport (BCN)", "Mexico City International Airport (MEX)", "Shanghai Hongqiao International Airport (SHA)",
#     "Chengdu Shuangliu International Airport (CTU)", "Narita International Airport (NRT)", "London Gatwick Airport (LGW)",
#     "Madrid-Barajas Adolfo Suárez Airport (MAD)", "Sydney Kingsford Smith Airport (SYD)", "Munich Airport (MUC)",
#     "Taiwan Taoyuan International Airport (TPE)", "Leonardo da Vinci–Fiumicino Airport (FCO)",
#     "Moscow Sheremetyevo International Airport (SVO)", "Houston George Bush Intercontinental Airport (IAH)",
#     "Newark Liberty International Airport (EWR)", "Chhatrapati Shivaji Maharaj International Airport (BOM)",
#     "São Paulo/Guarulhos–Governador André Franco Montoro International Airport (GRU)", "Bangkok Don Mueang International Airport (DMK)",
#     "Vancouver International Airport (YVR)", "Tan Son Nhat International Airport (SGN)", "Brussels Airport (BRU)",
#     "Johannesburg OR Tambo International Airport (JNB)", "Detroit Metropolitan Wayne County Airport (DTW)",
#     "Boston Logan International Airport (BOS)", "Philadelphia International Airport (PHL)",
#     "Minneapolis-Saint Paul International Airport (MSP)", "Singapore Changi Airport (SIN)", 
#     "Istanbul Sabiha Gökçen International Airport (SAW)", "Dubai Al Maktoum International Airport (DWC)",
#     "Rome Ciampino–G. B. Pastine International Airport (CIA)", "Vienna International Airport (VIE)", "Zurich Airport (ZRH)",
#     "Doha Hamad International Airport (DOH)", "Dublin Airport (DUB)", "Lisbon Humberto Delgado Airport (LIS)",
#     "Kansai International Airport (KIX)", "Osaka International Airport (ITM)", "Cape Town International Airport (CPT)",
#     "Bucharest Henri Coandă International Airport (OTP)", "Athens International Airport (ATH)",
#     "Budapest Ferenc Liszt International Airport (BUD)", "Prague Václav Havel Airport (PRG)", "Warsaw Chopin Airport (WAW)",
#     "Manchester Airport (MAN)", "Birmingham Airport (BHX)", "Edinburgh Airport (EDI)", "Nice Côte d'Azur Airport (NCE)",
#     "Helsinki-Vantaa Airport (HEL)", "Stockholm Arlanda Airport (ARN)", "Copenhagen Airport (CPH)",
#     "Oslo Gardermoen Airport (OSL)", "Doha Hamad International Airport (DOH)", "Hamad International Airport (DOH)",
#     "Abu Dhabi International Airport (AUH)", "Riyadh King Khalid International Airport (RUH)", "Jeddah King Abdulaziz International Airport (JED)",
#     "Muscat International Airport (MCT)", "Kuwait International Airport (KWI)", "Bahrain International Airport (BAH)",
#     "Cairo International Airport (CAI)", "Casablanca Mohammed V International Airport (CMN)", "Johannesburg Lanseria International Airport (HLA)",
#     "Durban King Shaka International Airport (DUR)", "Lagos Murtala Muhammed International Airport (LOS)",
#     "Nairobi Jomo Kenyatta International Airport (NBO)", "Addis Ababa Bole International Airport (ADD)",
#     "Algiers Houari Boumediene Airport (ALG)", "Accra Kotoka International Airport (ACC)", "Dakar Blaise Diagne International Airport (DSS)",
#     "Lusaka Kenneth Kaunda International Airport (LUN)", "Dar es Salaam Julius Nyerere International Airport (DAR)",
#     "Harare Robert Gabriel Mugabe International Airport (HRE)", "Cape Town International Airport (CPT)",
#     "Gaborone Sir Seretse Khama International Airport (GBE)", "Windhoek Hosea Kutako International Airport (WDH)",
#     "Antananarivo Ivato International Airport (TNR)", "Maputo Maputo International Airport (MPM)", "Luanda Quatro de Fevereiro Airport (LAD)",
#     "Port Louis Sir Seewoosagur Ramgoolam International Airport (MRU)", "Seychelles International Airport (SEZ)",
#     "Reykjavik Keflavik International Airport (KEF)", "Luxembourg Findel Airport (LUX)", "Hamburg Airport (HAM)",
#     "Berlin Brandenburg Airport (BER)", "Dusseldorf Airport (DUS)", "Stuttgart Airport (STR)", "Cologne Bonn Airport (CGN)",
#     "Hannover Airport (HAJ)", "Malaga-Costa del Sol Airport (AGP)", "Palma de Mallorca Airport (PMI)", "Ibiza Airport (IBZ)",
#     "Milan Malpensa Airport (MXP)", "Milan Linate Airport (LIN)", "Rome Ciampino–G. B. Pastine International Airport (CIA)",
#     "Venice Marco Polo Airport (VCE)", "Naples International Airport (NAP)", "Athens Eleftherios Venizelos Airport (ATH)",
#     "Thessaloniki Airport (SKG)", "Sofia Airport (SOF)", "Bucharest Henri Coandă International Airport (OTP)",
#     "Zagreb Franjo Tuđman Airport (ZAG)", "Belgrade Nikola Tesla Airport (BEG)", "Sarajevo International Airport (SJJ)",
#     "Ljubljana Jože Pučnik Airport (LJU)", "Skopje International Airport (SKP)", "Tirana International Airport Nënë Tereza (TIA)",
#     "Podgorica Airport (TGD)", "Pristina International Airport (PRN)", "Moscow Domodedovo Airport (DME)", "Moscow Vnukovo Airport (VKO)",
#     "Saint Petersburg Pulkovo Airport (LED)", "Sochi International Airport (AER)", "Kiev Boryspil International Airport (KBP)",
#     "Lviv Danylo Halytskyi International Airport (LWO)", "Minsk National Airport (MSQ)", "Yerevan Zvartnots International Airport (EVN)",
#     "Tbilisi International Airport (TBS)", "Baku Heydar Aliyev International Airport (GYD)", "Almaty International Airport (ALA)",
#     "Astana Nursultan Nazarbayev International Airport (NQZ)", "Tashkent International Airport (TAS)", "Ashgabat International Airport (ASB)",
#     "Dushanbe International Airport (DYU)", "Bishkek Manas International Airport (FRU)", "New Delhi Indira Gandhi International Airport (DEL)",
#     "Mumbai Chhatrapati Shivaji Maharaj International Airport (BOM)", "Bangalore Kempegowda International Airport (BLR)",
#     "Hyderabad Rajiv Gandhi International Airport (HYD)", "Chennai International Airport (MAA)", "Kolkata Netaji Subhas Chandra Bose International Airport (CCU)",
#     "Pune Lohegaon Airport (PNQ)", "Jaipur International Airport (JAI)", "Goa Dabolim Airport (GOI)", "Ahmedabad Sardar Vallabhbhai Patel International Airport (AMD)",
#     "Lucknow Chaudhary Charan Singh International Airport (LKO)", "Cochin International Airport (COK)", "Thiruvananthapuram International Airport (TRV)",
#     "Visakhapatnam International Airport (VTZ)", "Bhubaneswar Biju Patnaik International Airport (BBI)", "Guwahati Lokpriya Gopinath Bordoloi International Airport (GAU)",
#     "Srinagar Sheikh ul-Alam International Airport (SXR)", "Amritsar Sri Guru Ram Dass Jee International Airport (ATQ)",
#     "Leh Kushok Bakula Rimpochee Airport (IXL)", "Port Blair Veer Savarkar International Airport (IXZ)", "Male Velana International Airport (MLE)",
#     "Colombo Bandaranaike International Airport (CMB)", "Kathmandu Tribhuvan International Airport (KTM)", "Thimphu Paro International Airport (PBH)",
#     "Dhaka Hazrat Shahjalal International Airport (DAC)", "Chittagong Shah Amanat International Airport (CGP)", "Yangon International Airport (RGN)",
#     "Mandalay International Airport (MDL)", "Hanoi Noi Bai International Airport (HAN)", "Ho Chi Minh City Tan Son Nhat International Airport (SGN)",
#     "Phnom Penh International Airport (PNH)", "Siem Reap International Airport (REP)", "Bangkok Suvarnabhumi Airport (BKK)",
#     "Bangkok Don Mueang International Airport (DMK)", "Chiang Mai International Airport (CNX)", "Kuala Lumpur International Airport (KUL)",
#     "Penang International Airport (PEN)", "Kota Kinabalu International Airport (BKI)", "Jakarta Soekarno–Hatta International Airport (CGK)",
#     "Bali Ngurah Rai International Airport (DPS)", "Surabaya Juanda International Airport (SUB)", "Singapore Changi Airport (SIN)",
#     "Brunei International Airport (BWN)", "Manila Ninoy Aquino International Airport (MNL)", "Cebu Mactan-Cebu International Airport (CEB)",
#     "Davao Francisco Bangoy International Airport (DVO)", "Hong Kong International Airport (HKG)", "Macau International Airport (MFM)",
#     "Taipei Taiwan Taoyuan International Airport (TPE)", "Taipei Songshan Airport (TSA)", "Kaohsiung International Airport (KHH)",
#     "Seoul Incheon International Airport (ICN)", "Busan Gimhae International Airport (PUS)", "Jeju International Airport (CJU)",
#     "Tokyo Narita International Airport (NRT)", "Tokyo Haneda Airport (HND)", "Osaka Kansai International Airport (KIX)",
#     "Nagoya Chubu Centrair International Airport (NGO)", "Sapporo New Chitose Airport (CTS)", "Fukuoka Airport (FUK)",
#     "Okinawa Naha Airport (OKA)", "Sydney Kingsford Smith Airport (SYD)", "Melbourne Tullamarine Airport (MEL)",
#     "Brisbane Airport (BNE)", "Perth Airport (PER)", "Adelaide Airport (ADL)", "Auckland Airport (AKL)",
#     "Christchurch International Airport (CHC)", "Wellington Airport (WLG)", "Nadi International Airport (NAN)",
#     "Port Moresby Jacksons International Airport (POM)", "Honiara International Airport (HIR)", "Apia Faleolo International Airport (APW)",
#     "Suva Nausori International Airport (SUV)", "Pago Pago International Airport (PPG)", "Noumea La Tontouta International Airport (NOU)",
#     "Tahiti Faa'a International Airport (PPT)", "Bora Bora Airport (BOB)"
# ]

# airports = [
#     # India
#     "Indira Gandhi International Airport (DEL)",
#     "Chhatrapati Shivaji Maharaj International Airport (BOM)",
#     "Kempegowda International Airport (BLR)",
#     "Netaji Subhas Chandra Bose International Airport (CCU)",
#     "Rajiv Gandhi International Airport (HYD)",
#     "Chennai International Airport (MAA)",
#     "Sardar Vallabhbhai Patel International Airport (AMD)",
#     "Pune Airport (PNQ)",
#     "Goa International Airport (GOI)",
#     "Jaipur International Airport (JAI)",
#     "Cochin International Airport (COK)",
#     "Lokpriya Gopinath Bordoloi International Airport (GAU)",
#     "Mangalore International Airport (IXE)",
#     "Biju Patnaik International Airport (BBI)",
#     "Trivandrum International Airport (TRV)",
#     "Surat Airport (STV)",
#     "Visakhapatnam Airport (VTZ)",
#     "Bagdogra Airport (IXB)",
#     "Devi Ahilya Bai Holkar Airport (IDR)",
#     "Sri Guru Ram Dass Jee International Airport (ATQ)",

#     # USA
#     "Hartsfield-Jackson Atlanta International Airport (ATL)",
#     "Los Angeles International Airport (LAX)",
#     "Chicago O'Hare International Airport (ORD)",
#     "Dallas/Fort Worth International Airport (DFW)",
#     "Denver International Airport (DEN)",
#     "John F. Kennedy International Airport (JFK)",
#     "San Francisco International Airport (SFO)",
#     "Seattle-Tacoma International Airport (SEA)",
#     "Orlando International Airport (MCO)",
#     "Miami International Airport (MIA)",
#     "Phoenix Sky Harbor International Airport (PHX)",
#     "Charlotte Douglas International Airport (CLT)",
#     "Newark Liberty International Airport (EWR)",
#     "George Bush Intercontinental Airport (IAH)",
#     "Las Vegas McCarran International Airport (LAS)",
#     "Boston Logan International Airport (BOS)",
#     "Minneapolis-Saint Paul International Airport (MSP)",
#     "Detroit Metropolitan Wayne County Airport (DTW)",
#     "Philadelphia International Airport (PHL)",
#     "Salt Lake City International Airport (SLC)",

#     # Europe
#     "London Heathrow Airport (LHR)",
#     "Paris Charles de Gaulle Airport (CDG)",
#     "Amsterdam Airport Schiphol (AMS)",
#     "Frankfurt Airport (FRA)",
#     "Madrid-Barajas Adolfo Suárez Airport (MAD)",
#     "Barcelona-El Prat Airport (BCN)",
#     "Munich Airport (MUC)",
#     "Rome Leonardo da Vinci–Fiumicino Airport (FCO)",
#     "Zurich Airport (ZRH)",
#     "Vienna International Airport (VIE)",
#     "Istanbul Airport (IST)",
#     "Copenhagen Airport (CPH)",
#     "Oslo Gardermoen Airport (OSL)",
#     "Stockholm Arlanda Airport (ARN)",
#     "Dublin Airport (DUB)",
#     "Brussels Airport (BRU)",
#     "Lisbon Humberto Delgado Airport (LIS)",
#     "Athens International Airport (ATH)",
#     "Warsaw Chopin Airport (WAW)",
#     "Prague Václav Havel Airport (PRG)",

#     # Russia
#     "Moscow Sheremetyevo International Airport (SVO)",
#     "Moscow Domodedovo Airport (DME)",
#     "Saint Petersburg Pulkovo Airport (LED)",
#     "Kazan International Airport (KZN)",
#     "Novosibirsk Tolmachevo Airport (OVB)",
#     "Yekaterinburg Koltsovo Airport (SVX)",
#     "Sochi International Airport (AER)",
#     "Vladivostok International Airport (VVO)",
#     "Rostov-on-Don Platov International Airport (ROV)",
#     "Ufa International Airport (UFA)",
#     "Krasnoyarsk International Airport (KJA)",
#     "Samara Kurumoch International Airport (KUF)",
#     "Irkutsk International Airport (IKT)",
#     "Kaliningrad Khrabrovo Airport (KGD)",
#     "Omsk Tsentralny Airport (OMS)",

#     # Other
#     "Dubai International Airport (DXB)",
#     "Beijing Capital International Airport (PEK)",
#     "Tokyo Haneda Airport (HND)",
#     "Singapore Changi Airport (SIN)",
#     "Hong Kong International Airport (HKG)",
#     "Doha Hamad International Airport (DOH)",
#     "Seoul Incheon International Airport (ICN)",
#     "Sydney Kingsford Smith Airport (SYD)",
#     "Toronto Pearson International Airport (YYZ)",
#     "Mexico City International Airport (MEX)",
#     "Guangzhou Baiyun International Airport (CAN)",
#     "Shanghai Pudong International Airport (PVG)",
#     "Kuala Lumpur International Airport (KUL)",
#     "Bangkok Suvarnabhumi Airport (BKK)",
#     "Cape Town International Airport (CPT)",
#     "Johannesburg OR Tambo International Airport (JNB)",
#     "Istanbul Sabiha Gökçen International Airport (SAW)",
#     "Buenos Aires Ministro Pistarini International Airport (EZE)",
#     "Auckland Airport (AKL)",
#     "São Paulo/Guarulhos–Governador André Franco Montoro International Airport (GRU)"
# ]

# airlines = [
#     "American Airlines",
#     "Delta Air Lines",
#     "United Airlines",
#     "Southwest Airlines",
#     "Ryanair",
#     "China Southern Airlines",
#     "Lufthansa",
#     "Air France",
#     "Turkish Airlines",
#     "Emirates",
#     "Qatar Airways",
#     "British Airways",
#     "Air China",
#     "Japan Airlines",
#     "Singapore Airlines",
#     "Cathay Pacific",
#     "Korean Air",
#     "Aeroflot",
#     "Etihad Airways",
#     "LATAM Airlines",
#     "Qantas",
#     "EasyJet",
#     "Alaska Airlines",
#     "Vueling Airlines",
#     "Hainan Airlines",
#     "JetBlue Airways",
#     "IndiGo",
#     "Thai Airways",
#     "Garuda Indonesia",
#     "Vietnam Airlines",
#     "SAS Scandinavian Airlines",
#     "Finnair",
#     "KLM Royal Dutch Airlines",
#     "Iberia",
#     "Spirit Airlines",
#     "Wizz Air",
#     "Air India",
#     "Avianca",
#     "Saudi Arabian Airlines",
#     "EgyptAir",
#     "TAP Air Portugal",
#     "Air Canada",
#     "Aegean Airlines",
#     "Malaysia Airlines",
#     "Asiana Airlines",
#     "All Nippon Airways (ANA)",
#     "Swiss International Air Lines",
#     "LOT Polish Airlines",
#     "Philippine Airlines",
#     "Brussels Airlines",
#     "Air New Zealand",
#     "Royal Air Maroc",
#     "Vietnam Airlines",
#     "Azul Brazilian Airlines",
#     "Norwegian Air Shuttle",
#     "RwandAir",
#     "Oman Air",
#     "Cebu Pacific",
#     "Pegasus Airlines",
#     "TUI Airways",
#     "Scoot",
#     "South African Airways",
#     "Kenya Airways",
#     "El Al Israel Airlines",
#     "Virgin Atlantic",
#     "Vistara",
#     "Middle East Airlines",
#     "Frontier Airlines",
#     "Sun Country Airlines",
#     "Aer Lingus",
#     "Air Mauritius",
#     "Air Serbia",
#     "Jet2.com",
#     "S7 Airlines",
#     "Hawaiian Airlines",
#     "AirBaltic",
#     "LATAM Airlines",
#     "Air Astana",
#     "Uzbekistan Airways",
#     "Bangkok Airways",
#     "SriLankan Airlines",
#     "Copa Airlines",
#     "Azores Airlines",
#     "Fiji Airways",
#     "Azerbaijan Airlines",
#     "Royal Jordanian",
#     "PAL Express",
#     "Flydubai",
#     "Bamboo Airways",
#     "WestJet",
#     "Jetstar Airways",
#     "Jazeera Airways",
#     "Widerøe",
#     "Air Tanzania",
#     "Tunisair",
#     "Icelandair"
#     # ... Continue adding to the list if needed.
# ]

#from itertools import product

# # List of 150 major airports organized by region
# airports_india = [
#     "Indira Gandhi International Airport (DEL)",
#     "Chhatrapati Shivaji Maharaj International Airport (BOM)",
#     "Kempegowda International Airport (BLR)",
#     "Netaji Subhas Chandra Bose International Airport (CCU)",
#     "Rajiv Gandhi International Airport (HYD)",
#     "Chennai International Airport (MAA)",
#     "Sardar Vallabhbhai Patel International Airport (AMD)",
#     "Pune Airport (PNQ)",
#     "Goa International Airport (GOI)",
#     "Jaipur International Airport (JAI)",
#     "Cochin International Airport (COK)",
#     "Lokpriya Gopinath Bordoloi International Airport (GAU)",
#     "Mangalore International Airport (IXE)",
#     "Biju Patnaik International Airport (BBI)",
#     "Trivandrum International Airport (TRV)",
#     "Surat Airport (STV)",
#     "Visakhapatnam Airport (VTZ)",
#     "Bagdogra Airport (IXB)",
#     "Devi Ahilya Bai Holkar Airport (IDR)",
#     "Sri Guru Ram Dass Jee International Airport (ATQ)"
# ]

# airports_usa = [
#     "Hartsfield-Jackson Atlanta International Airport (ATL)",
#     "Los Angeles International Airport (LAX)",
#     "Chicago O'Hare International Airport (ORD)",
#     "Dallas/Fort Worth International Airport (DFW)",
#     "Denver International Airport (DEN)",
#     "John F. Kennedy International Airport (JFK)",
#     "San Francisco International Airport (SFO)",
#     "Seattle-Tacoma International Airport (SEA)",
#     "Orlando International Airport (MCO)",
#     "Miami International Airport (MIA)",
#     "Phoenix Sky Harbor International Airport (PHX)",
#     "Charlotte Douglas International Airport (CLT)",
#     "Newark Liberty International Airport (EWR)",
#     "George Bush Intercontinental Airport (IAH)",
#     "Las Vegas McCarran International Airport (LAS)",
#     "Boston Logan International Airport (BOS)",
#     "Minneapolis-Saint Paul International Airport (MSP)",
#     "Detroit Metropolitan Wayne County Airport (DTW)",
#     "Philadelphia International Airport (PHL)",
#     "Salt Lake City International Airport (SLC)"
# ]

# airports_europe = [
#     "London Heathrow Airport (LHR)",
#     "Paris Charles de Gaulle Airport (CDG)",
#     "Amsterdam Airport Schiphol (AMS)",
#     "Frankfurt Airport (FRA)",
#     "Madrid-Barajas Adolfo Suárez Airport (MAD)",
#     "Barcelona-El Prat Airport (BCN)",
#     "Munich Airport (MUC)",
#     "Rome Leonardo da Vinci–Fiumicino Airport (FCO)",
#     "Zurich Airport (ZRH)",
#     "Vienna International Airport (VIE)",
#     "Istanbul Airport (IST)",
#     "Copenhagen Airport (CPH)",
#     "Oslo Gardermoen Airport (OSL)",
#     "Stockholm Arlanda Airport (ARN)",
#     "Dublin Airport (DUB)",
#     "Brussels Airport (BRU)",
#     "Lisbon Humberto Delgado Airport (LIS)",
#     "Athens International Airport (ATH)",
#     "Warsaw Chopin Airport (WAW)",
#     "Prague Václav Havel Airport (PRG)"
# ]

# airports_russia = [
#     "Moscow Sheremetyevo International Airport (SVO)",
#     "Moscow Domodedovo Airport (DME)",
#     "Saint Petersburg Pulkovo Airport (LED)",
#     "Kazan International Airport (KZN)",
#     "Novosibirsk Tolmachevo Airport (OVB)",
#     "Yekaterinburg Koltsovo Airport (SVX)",
#     "Sochi International Airport (AER)",
#     "Vladivostok International Airport (VVO)",
#     "Rostov-on-Don Platov International Airport (ROV)",
#     "Ufa International Airport (UFA)",
#     "Krasnoyarsk International Airport (KJA)",
#     "Samara Kurumoch International Airport (KUF)",
#     "Irkutsk International Airport (IKT)",
#     "Kaliningrad Khrabrovo Airport (KGD)",
#     "Omsk Tsentralny Airport (OMS)"
# ]

# airports_other = [
#     "Dubai International Airport (DXB)",
#     "Beijing Capital International Airport (PEK)",
#     "Tokyo Haneda Airport (HND)",
#     "Singapore Changi Airport (SIN)",
#     "Hong Kong International Airport (HKG)",
#     "Doha Hamad International Airport (DOH)",
#     "Seoul Incheon International Airport (ICN)",
#     "Sydney Kingsford Smith Airport (SYD)",
#     "Toronto Pearson International Airport (YYZ)",
#     "Mexico City International Airport (MEX)",
#     "Guangzhou Baiyun International Airport (CAN)",
#     "Shanghai Pudong International Airport (PVG)",
#     "Kuala Lumpur International Airport (KUL)",
#     "Bangkok Suvarnabhumi Airport (BKK)",
#     "Cape Town International Airport (CPT)",
#     "Johannesburg OR Tambo International Airport (JNB)",
#     "Istanbul Sabiha Gökçen International Airport (SAW)",
#     "Buenos Aires Ministro Pistarini International Airport (EZE)",
#     "Auckland Airport (AKL)",
#     "São Paulo/Guarulhos–Governador André Franco Montoro International Airport (GRU)"
# ]

# # Region-specific airlines
# airlines_india = ["IndiGo", "Air India", "Vistara", "SpiceJet", "Go First"]
# airlines_usa = ["American Airlines", "Delta Air Lines", "United Airlines", "Southwest Airlines", "JetBlue Airways"]
# airlines_europe = ["Lufthansa", "Air France", "British Airways", "Ryanair", "KLM Royal Dutch Airlines"]
# airlines_russia = ["Aeroflot", "S7 Airlines", "Ural Airlines", "Rossiya Airlines"]
# airlines_other = ["Emirates", "Qatar Airways", "Singapore Airlines", "Cathay Pacific", "Air New Zealand"]


# with open("flights.txt", "w") as file:
#     # Generate and write combinations for each region
#     for airports, airlines, region_name in [
#         (airports_india, airlines_india, "India"),
#         (airports_usa, airlines_usa, "USA"),
#         (airports_europe, airlines_europe, "Europe"),
#         (airports_russia, airlines_russia, "Russia"),
#         (airports_other, airlines_other, "Other")
#     ]:
#         combinations = [[airport1, airport2, airline] for airport1, airport2, airline in product(airports, airports, airlines) if airport1 != airport2]
#         for combination in combinations:
#             file.write(f"{combination}\n")

# print("All combinations written to flights.txt")


import itertools

# Define the list of airports and airlines
major_airports = [
    # India
    "Indira Gandhi International Airport (DEL)",
    #"Chhatrapati Shivaji Maharaj International Airport (BOM)",
    #"Kempegowda International Airport (BLR)",
    #"Netaji Subhas Chandra Bose International Airport (CCU)",
    "Chennai International Airport (MAA)",
    #"Rajiv Gandhi International Airport (HYD)",
    #"Cochin International Airport (COK)",
    #"Sardar Vallabhbhai Patel International Airport (AMD)",
    "Pune International Airport (PNQ)",
    "Goa International Airport (GOI)",
    #"Jaipur International Airport (JAI)",
    #"Lucknow Airport (LKO)",
    "Trivandrum International Airport (TRV)",
    #"Bagdogra Airport (IXB)",
    "Mangaluru International Airport (IXE)",
    "Visakhapatnam Airport (VTZ)",
    #"Sri Guru Ram Dass Jee International Airport (ATQ)",
    #"Devi Ahilya Bai Holkar Airport (IDR)",
    #"Biju Patnaik International Airport (BBI)",
    #"Lal Bahadur Shastri International Airport (VNS)",
    
    # USA
    "Boston Logan International Airport (BOS)",
    #"Hartsfield-Jackson Atlanta International Airport (ATL)",
    "Los Angeles International Airport (LAX)",
    #"O'Hare International Airport (ORD)",
    #"Dallas/Fort Worth International Airport (DFW)",
    #"Denver International Airport (DEN)",
    "John F. Kennedy International Airport (JFK)",
    #"San Francisco International Airport (SFO)",
    #"Seattle-Tacoma International Airport (SEA)",
    #"Miami International Airport (MIA)",
    #"Orlando International Airport (MCO)",
    #"Charlotte Douglas International Airport (CLT)",
    "Philadelphia International Airport (PHL)",
    #"Phoenix Sky Harbor International Airport (PHX)",
    #"Houston George Bush Intercontinental Airport (IAH)",
    
    # Europe
    "London Heathrow Airport (LHR)",
    "Paris Charles de Gaulle Airport (CDG)",
    #"Amsterdam Airport Schiphol (AMS)",
    "Frankfurt Airport (FRA)",
    #"Madrid-Barajas Adolfo Suárez Airport (MAD)",
    "Barcelona-El Prat Airport (BCN)",
    #"Zurich Airport (ZRH)",
    #"Munich Airport (MUC)",
    #"Brussels Airport (BRU)",
    "Copenhagen Airport (CPH)",
    
    # Russia
    #"Sheremetyevo International Airport (SVO)",
    "Domodedovo International Airport (DME)",
    #"Pulkovo Airport (LED)",
    
    # Other Regions
    "Tokyo Haneda Airport (HND)",  # Japan
    "Dubai International Airport (DXB)"  # UAE
]

major_airlines = [
    "Air India",
    "American Airlines",
    #"Lufthansa",
    "Emirates",
    "British Airways",
    "Qatar Airways",
    #"Delta Air Lines",
    #"Air France",
    #"Turkish Airlines",
    #"Singapore Airlines"
]

# Generate combinations of airports and airlines
combinations = []
for airport1, airport2 in itertools.combinations(major_airports, 2):
    for airline in major_airlines:
        combinations.append([airport1, airport2, airline])
        

# Output the combinations:
    
with open('flights2.txt', 'w+') as file:
    for combo in combinations:
        file.write(f"{combo}\n")
        print(combo)
    
    
print("Major airports written to major_airports.txt")



import pymysql
import random
import ast

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database = "airwaysms2_0"
                    )

cur = con.cursor()

def get_price(departure, arrival, airline):
    # Price ranges for domestic and international flights in INR
    domestic_price_range = (1000, 5000)  # For domestic flights
    international_price_range = (10000, 50000)  # For international flights

    # Simple logic to categorize flights
    if "India" in departure and "India" in arrival:
        # Domestic flight
        return random.randint(*domestic_price_range)
    else:
        # International flight
        return random.randint(*international_price_range)

# Read flights from the file and insert them into the database
with open("flights2.txt", "r") as infile:
    for line in infile:
        # Convert the string representation of the list to an actual list
        flight_data = ast.literal_eval(line.strip())
        if len(flight_data) == 3:
            departure, arrival, airline = flight_data
            
            # Get the price based on departure and arrival
            price = get_price(departure, arrival, airline)
            
            # Insert data into the flights table
            cur.execute("""
                INSERT INTO flights (F_Departure, F_Ariaval, F_Airline, F_price)
                VALUES (%s, %s, %s, %s)
            """, (departure, arrival, airline, price))
        
            con.commit()
        