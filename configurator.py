import math


cities = ["NYC"]
cityLinesArray = {"NYC":['1', '2', '3', '4', '5', '5X', '6', '6X', '7', '7X', 'A', 'B', 'C', 'D', 'E', 'F', 'FX', 'FS', 'G', 'GS', 'H', 'J', 'L', 'M', 'N', 'Q', 'R', 'SI', 'W', "Z"]}
longNames = {"NYC":['1', '2', '3', '4', '5', '5 Express', '6', '6 Express', '7', '7 Express', 'A', 'B', 'C', 'D', 'E', 'F', 'F Express', 'Frank Shuttle', 'G', '42nd Shuttle', 'Rockaway Shuttle', 'J', 'L', 'M', 'N', 'Q', 'R', 'SIR', 'W', "Z"]}
cityStopArray = {"NYC":{
	'1':
		["Van Cortlandt Park-242 St","238 St","231 St","Marble Hill-225 St","215 St","207 St","Dyckman St","191 St","181 St","168 St-Washington Hts","157 St","145 St","137 St-City College","125 St","116 St-Columbia University","Cathedral Pkwy (110 St)","103 St","96 St","86 St","79 St","72 St","66 St-Lincoln Center","59 St-Columbus Circle","50 St","Times Sq-42 St","34 St-Penn Station","28 St","23 St","18 St","14 St","Christopher St-Stonewall","Houston St","Canal St","Franklin St","Chambers St","WTC Cortlandt","Rector St","South Ferry Loop","South Ferry"],
	'2':
		["Wakefield-241 St","Nereid Av","233 St","225 St","219 St","Gun Hill Rd","Burke Av","Allerton Av","Pelham Pkwy","Bronx Park East","E 180 St","West Farms Sq-E Tremont Av","174 St","Freeman St","Simpson St","Intervale Av","Prospect Av","Jackson Av","3 Av-149 St","149 St-Grand Concourse","135 St","125 St","116 St","Central Park North (110 St)","96 St","72 St","Times Sq-42 St","34 St-Penn Station","14 St","Chambers St","Park Place","Fulton St","Wall St","Clark St","Borough Hall","Hoyt St","Nevins St","Atlantic Av-Barclays Ctr","Bergen St","Grand Army Plaza","Eastern Pkwy-Brooklyn Museum","Franklin Av-Medgar Evers College","President St-Medgar Evers College","Sterling St","Winthrop St","Church Av","Beverly Rd","Newkirk Av-Little Haiti","Flatbush Av-Brooklyn College"],
	'3':
		["Harlem-148 St","145 St","135 St","125 St","116 St","Central Park North (110 St)","96 St","72 St","Times Sq-42 St","34 St-Penn Station","14 St","Chambers St","Park Place","Fulton St","Wall St","Clark St","Borough Hall","Hoyt St","Nevins St","Atlantic Av-Barclays Ctr","Bergen St","Grand Army Plaza","Eastern Pkwy-Brooklyn Museum","Franklin Av-Medgar Evers College","Nostrand Av","Kingston Av","Crown Hts-Utica Av","Sutter Av-Rutland Rd","Saratoga Av","Rockaway Av","Junius St","Pennsylvania Av","Van Siclen Av","New Lots Av"],
	'4':
		["Woodlawn","Mosholu Pkwy","Bedford Park Blvd-Lehman College","Kingsbridge Rd","Fordham Rd","183 St","Burnside Av","176 St","Mt Eden Av","170 St","167 St","161 St-Yankee Stadium","149 St-Grand Concourse","138 St-Grand Concourse","125 St","86 St","59 St","Grand Central-42 St","14 St-Union Sq","Brooklyn Bridge-City Hall","Fulton St","Wall St","Bowling Green","Borough Hall","Nevins St","Atlantic Av-Barclays Ctr","Franklin Av-Medgar Evers College","Crown Heights-Utica Av"],
	'5':
		["Eastchester-Dyre Av","Baychester Av","Morris Park","E 180 St","West Farms Sq-E Tremont Av","174 St","Freeman St","Simpson St","Intervale Av","Prospect Av","Jackson Av","3 Av-149 St","149 St-Grand Concourse","138 St-Grand Concourse","125 St","86 St","59 St","Grand Central-42 St","14 St-Union Sq","Brooklyn Bridge-City Hall","Fulton St","Wall St","Bowling Green","Nereid Av","233 St","225 St","219 St","Gun Hill Rd","Burke Av","Allerton Av","Pelham Pkwy","Bronx Park East","Borough Hall","Nevins St","Atlantic Av-Barclays Ctr","Franklin Av-Medgar Evers College","President St-Medgar Evers College","Sterling St","Winthrop St","Church Av","Beverly Rd","Newkirk Av-Little Haiti","Flatbush Av-Brooklyn College"],
	'6':
		["Pelham Bay Park","Buhre Av","Middletown Rd","Westchester Sq-East Tremont Av","Zerega Av","Castle Hill Av","Parkchester","St Lawrence Av","Morrison Av-Soundview","Elder Av","Whitlock Av","Hunts Point Av","Longwood Av","E 149 St","E 143 St-Mary's St","Cypress Av","Brook Av","3 Av-138 St","125 St","116 St","110 St","103 St","96 St","86 St","77 St","68 St-Hunter College","59 St","51 St","Grand Central-42 St","33 St","28 St","23 St","14 St-Union Sq","Astor Pl","Bleeker St","Spring St","Canal St","Brooklyn Bridge-City Hall"],
	'6X':
		["Pelham Bay Park","Buhre Av","Middletown Rd","Westchester Sq-East Tremont Av","Zerega Av","Castle Hill Av","Parkchester","Hunts Point Av","3 Av-138 St","125 St","116 St","110 St","103 St","96 St","86 St","77 St","68 St-Hunter College","59 St","51 St","Grand Central-42 St","33 St","28 St","23 St","14 St-Union Sq","Astor Pl","Bleeker St","Spring St","Canal St","Brooklyn Bridge-City Hall"],
	'7':
		["Flushing-Main St","Mets-Willets Point","111 St","103 St-Corona Plaza","Junction Blvd","90 St-Elmhurst Av","82 St-Jackson Hts","74 St-Broadway","69 St","61 St-Woodside","52 St","46 St-Bliss St","40 St-Lowery St","33 St-Rawson St","Queensboro Plaza","Court Sq","Hunters Point Av","Vernon Blvd-Jackson Av","Grand Central-42 St","5 Av","Times Sq-42 St","34 St-Hudson Yards"],
	'7X':
		["Flushing-Main St","Mets-Willets Point","Junction Blvd","74 St-Broadway","69 St","61 St-Woodside","52 St","46 St-Bliss St","40 St-Lowery St","33 St-Rawson St","Queensboro Plaza","Court Sq","Hunters Point Av","Vernon Blvd-Jackson Av","Grand Central-42 St","5 Av","Times Sq-42 St","34 St-Hudson Yards"],
	'A':
		["Inwood-207 St","Dyckman St","190 St","181 St","175 St","168 St","145 St","125 St","59 St-Columbus Circle","42 St/Port Authority Bus Terminal","34 St-Penn Station","14 St","W 4 St-Washington Sq","Canal St","Chambers St","Fulton St","High St","Jay St-MetroTech","Hoyt-Schermerhorn","Nostrand Av","Utica Av","Broadway Junction","Euclid Av","Grant Av","80 St","88 St","Rockaway Blvd","104 St","111 St","Ozone Pk-Lefferts Boulevard","Aqueduct Racetrack","Aqueduct-North Conduit Av","Howard Beach-JFK Airport","Broad Channel","Beach 67 St","Beach 60 St","Beach 44 St","Beach 36 St","Beach 25 St","Far Rockaway-Mott Av","Broad Channel","Beach 90 St","Beach 98 St","Beach 105 St","Rockaway Park-Beach 116 St"],
	'B':
		["Bedford Park Blvd","Kingsbridge Rd","Fordham Rd","182-183 Sts","Tremont Av","174-175 Sts","170 St","167 St","161 St-Yankee Stadium","155 St","145 St","135 St","125 St","116 St","Cathedral Pkwy (110 St)","103 St","96 St","86 St","81 St-Museum of Natural History","72 St","59 St-Columbus Circle","7 Av","47-50 Sts-Rockefeller Ctr","42 St-Bryant Park","34 St-Herald Sq","W 4 St-Washington Sq","Broadway-Lafayette St","Grand St","DeKalb Av","Atlantic Av-Barclays Ctr","7 Av","Prospect Park","Church Av","Newkirk Plaza","Kings Hwy","Sheepshead Bay","Brighton Beach"],
	'C':
		["168 St","163 St-Amsterdam Av","155 St","145 St","135 St","125 St","116 St","Cathedral Pkwy (110 St)","103 St","96 St","86 St","81 St-Museum of Natural History","72 St","59 St-Columbus Circle","50 St","42 St/Port Authority Bus Terminal","34 St-Penn Station","23 St","14 St","W 4-Washington Sq","Spring St","Canal St","Chambers St","Fulton St","High St","Jay St-MetroTech","Hoyt-Schermerhorn","Lafayette Av","Clinton-Washington Avs","Franklin Av","Nostrand Av","Kingston-Throop Avs","Utica Av","Ralph Av","Rockaway Av","Broadway Junction","Liberty Av","Van Siclen Av","Shepherd Av","Euclid Av"],
	'D':
		["Norwood-205 St","Bedford Park Blvd","Kingsbridge Rd","Fordham Rd","182-183 Sts","Tremont Av","174-175 Sts","170 St","167 St","161 St-Yankee Stadium","155 St","145 St","125 St","59 St-Columbus Circle","7 Av","47-50 Sts-Rockefeller Ctr","42 St-Bryant Pk","34 St-Herald Sq","W 4 St-Washington Sq","Broadway-Lafayette St","Grand St","Atlantic Av-Barclays Ctr","36 St","9 Av","Fort Hamilton Pkwy","50 St","55 St","62 St","71 St","79 St","18 Av","20 Av","Bay Pkwy","25 Av","Bay-50 St","Coney Island-Stillwell Av"],
	'E':
		["Jamaica Center-Parsons/Archer","Sutphin Blvd-Archer Av-JFK Airport","Jamaica-Van Wyck","Briarwood","Kew Gardens-Union Tpke","75 Av","Forest Hills-71 Av","Jackson Hts-Roosevelt Av","Queens Plaza","Court Sq-23 St","Lexington Av/53 St","5 Av/53 St","7 Av","50 St","42 St/Port Authority Bus Terminal","34 St-Penn Station","23 St","14 St","W 4 St-Washington Sq","Spring St","Canal St","World Trade Center"],
	'F':
		["Jamaica-179 St","169 St","Parsons Blvd","Sutphin Blvd","Briarwood","Kew Gardens-Union Tpke","75 Av","Forest Hills-71 Av","Jackson Hts-Roosevelt Av","21 St-Queensbridge","Roosevelt Island","Lexington Av/63 St","57 St","47-50 Sts Rockefeller Ctr","42 St-Bryant Pk","34 St-Herald Sq","23 St","14 St","W 4 St-Washington Sq","Broadway-Lafayette St","2 Av","Delancey St-Essex St","East Broadway","York St","Jay St-MetroTech","Bergen St","Carroll St","Smith-9 Sts","4 Av-9 St","7 Av","15 St-Prospect Park","Fort Hamilton Pkwy","Church Av","Ditmas Av","18 Av","Avenue I","Bay Pkwy","Avenue N","Avenue P","Kings Hwy","Avenue U","Avenue X","Neptune Av","W 8 St-NY Aquarium","Coney Island-Stillwell Av"],
	'FX':
		[],
	'FS':
		["Franklin Av","Park Place","Botanic Garden","Prospect Park"],
	'G':
		["Court Sq","21 St","Greenpoint Av","Nassau Av","Metropolitan Av","Broadway","Flushing Av","Myrtle Willoughby Avs","Bedford-Nostrand Avs","Classon Av","Clinton-Washington Avs","Fulton St","Hoyt-Schermerhorn","Bergen St","Carroll St","Smith-9 Sts","4 Av-9 Sts","7 Av","15 St-Prospect Park","Fort Hamilton Pkwy","Church Av"],
	'GS':
		["Times Sq-42 St","Grand Central-42 St"],
	'H':
		["Broad Channel","Beach 90 St","Beach 98 St","Beach 105 St","Rockaway Park-Beach 116 St"], 
	'J':
		["Jamaica Center-Parsons/Archer","Sutphin Blvd-Archer Av-JFK Airport","121 St","111 St","104 St","Woodhaven Blvd","85 St-Forest Pkwy","75 St-Elderts Ln","Cypress Hills","Crescent St","Norwood Av","Cleveland St","Van Siclen Av","Alabama Av","Broadway Junction","Chauncey St","Halsey St","Gates Av","Kosciuszko St","Myrtle Av","Flushing Av","Lorimer St","Hewes St","Marcy Av","Delancey St-Essex St","Bowery","Canal St","Chambers St","Fulton St","Broad St"],
	'L':
		["8 Av","6 Av","14 St-Union Sq","3 Av","1 Av","Bedford Av","Lorimer St","Graham Av","Grand St","Montrose Av","Morgan Av","Jefferson St","DeKalb Av","Myrtle-Wyckoff Avs","Halsey St","Wilson Av","Bushwick Av-Aberdeen St","Broadway Junction","Atlantic Av","Sutter Av","Livonia Av","New Lots Av","East 105 St","Canarsie-Rockaway Pkwy"],
	'M':
		["Forest Hills-71 Av","67 Av","63 Dr-Rego Park","Woodhaven Blvd","Grand Av-Newtown","Elmhurst Av","Jackson Hts-Roosevelt Av","65 St","Northern Blvd","46 St","Steinway St","36 St","Queens Plaza","Court Sq-23 St","Lexington Av/53 St","5 Av/53 St","47-50 Sts-Rockefeller Ctr","42 St-Bryant Pk","34 St-Herald Sq","23 St","14 St","W 4 St-Washington Sq","Broadway-Lafayette St","Delancey St-Essex St","Marcy Av","Hewes St","Lorimer St","Flushing Av","Myrtle Av","Central Av","Knickerbocker Av","Myrtle-Wyckoff Avs","Seneca Av","Forest Av","Fresh Pond Rd","Middle Village-Metropolitan Av"],
	'N':
		["Astoria Ditmars Blvd","Astoria Blvd","30 Av","Broadway","36 Av","39 Av","Queensboro Plaza","Lexington Av/59 St","5 Av/59 St","57 St-7 Av","49 St","Times Sq-42 St","34 St-Herald Sq","14 St-Union Sq","Canal St","Atlantic Av-Barclays Ctr","36 St","59 St","8 Av","Fort Hamilton Pkwy","New Utrecht Av","18 Av","20 Av","Bay Pkwy","Kings Hwy","Avenue U","86 St","Coney Island-Stillwell Av"],
	'Q':
		["96 St","86 St","72 St","Lexington Av/63 St","57 St-7 Av","Times Sq-42 St","34 St-Herald Sq","14 St-Union Sq","Canal St","DeKalb Av","Atlantic Av-Barclays Ctr","7 Av","Prospect Park","Parkside Av","Church Av","Beverly Rd","Cortelyou Rd","Newkirk Plaza","Avenue H","Avenue J","Avenue M","Kings Hwy","Avenue U","Neck Rd","Sheepshead Bay","Brighton Beach","Ocean Pkwy","W 8 St-NY Aquarium","Coney Island-Stillwell Av"],
	'R':
		["Forest Hills-71 Av","67 Av","63 Dr-Rego Park","Woodhaven Blvd","Grand Av","Elmhurst Av","Jackson Hts-Roosevelt Av","65 St","Northern Blvd","46 St","Steinway St","36 St","Queens Plaza","Lexington Av/59 St","5 Av/59 St","57 St-7 Av","49 St","Times Square-42 St","34 St-Herald Square","28 St","23 St","14 St-Union Sq","8 St-NYU","Prince St","Canal St","City Hall","Cortlandt St","Rector St","Whitehall St-South Ferry","Court St","Jay St-MetroTech","DeKalb Av","Atlantic Av-Barclays Ctr","Union St","4 Av-9 St","Prospect Av","25 St","36 St","45 St","53 St","59 St","Bay Ridge Av","77 St","86 St","Bay Ridge-95 St"],
	'SI':
		["Tottenville","Arthur Kill","Richmond Valley","Pleasant Plains","Prince's Bay","Huguenot","Annadale","Eltingville","Great Kills","Bay Terrace","Oakwood Heights","New Dorp","Grant City","Jefferson Av","Dongan Hills","Old Town","Grasmere","Clifton","Stapleton","Tompkinsville","St George"],
	'W':
		["Astoria-Ditmars Blvd","Astoria Blvd","30 Av","Broadway","36 Av","39 Av","Queensboro Plaza","Lexington Av/59 St","5 Av/59 St","57-7 Av","49 St","Times Sq-42 St","34 St-Herald Sq","28 St","23 St","14 St-Union Sq","8 St-NYU","Prince St","Canal St","City Hall","Cortlandt St","Rector St","Whitehall St-South Ferry"],
	'Z':
		["Jamaica Center-Parsons/Archer","Sutphin Blvd-Archer Av-JFK Airport","121 St","104 St","Woodhaven Blvd","75 St-Elderts Ln","Crescent St","Norwood Av","Van Siclen Av","Alabama Av","Broadway Junction","Chauncey St","Gates Av","Myrtle Av","Marcy Av","Delancey St Essex St","Bowery","Canal St","Chambers St","Fulton St","Broad St"]
		
		}

}
def get_city():
	while True:
		try:
			cityNum = int(input("> "))
			if cityNum>=len(cities):
				print("Invalid input. City number must be a valid index.")
			else: 
				return cityNum
		except ValueError:
			print("Invalid input. Please enter a number.")

f1 = True
while f1:
	print("These are the supported metro systems. Please enter the number corresponding to the system you would like to configure stops for.\n")
	for x in range(int(math.ceil(len(cities)/3))):
		if ((x+2))<len(cities):
			print(str(x) + ": " + cities[x].ljust(20) + " | " + str(x+1) + cities[x*2].ljust(20) + " | " + str(x+2) + cities[x*3] )
		elif (x+1)<len(cities):
			print(str(x) + ": " + cities[x].ljust(20) + " | " + str(x+1) + cities[x*2].ljust(20) )
		else:
			print(str(x) + ": " + cities[x].ljust(20))
		citNum = get_city()
		f2 = True
		while f2:
			print("These are the lines. Please enter the number corresponding to the system you would like to configure stops for.\n")
			numOfLines = len(cityLinesArray.get(cities[citNum]))
			for x in range(int(math.ceil(numOfLines/3))):
				if ((x+(int(numOfLines/3))+(int(numOfLines/3))))<numOfLines:
					print(str(x) + ": " + longNames.get(cities[citNum])[x].ljust(20) + " | " + str(x+(int(numOfLines/3))) + ": " + longNames.get(cities[citNum])[x+(int(numOfLines/3))].ljust(20) + " | " + str(x+(int(numOfLines/3))+(int(numOfLines/3))) + ": " + longNames.get(cities[citNum])[x+(int(numOfLines/3))+(int(numOfLines/3))] )
				elif (x+(int(numOfLines/3)))<numOfLines:
					print(str(x) + ": " + longNames.get(cities[citNum])[x].ljust(20) + " | " + str(x+(int(numOfLines/3))) + ": " + longNames.get(cities[citNum])[x+(int(numOfLines/3))].ljust(20) )
				else:
					print(str(x) + ": " + longNames.get(cities[citNum])[x].ljust(20))

			d2 = input("Would you like to configure another line? (Y/N) ")
			if d2.upper() == "Y":
				f2 = True
			else:
				f2 = False
	d1 = input("Would you like to configure another metro? (Y/N)")
	if d1.upper() == "Y":
		f1 = True
	else:
		f1 = False