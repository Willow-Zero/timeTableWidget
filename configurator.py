


NYCLines = ['1', '2', '3', '4', '5', '5X', '6', '6X', '7', '7X', 'A', 'B', 'C', 'D', 'E', 'F', 'FX', 'FS', 'G', 'GS', 'H', 'J', 'L', 'M', 'N', 'Q', 'R', 'SI', 'W', "Z"]
NYCStops={
	'1':
		["Van Cortlandt Park-242 St","238 St","231 St","Marble Hill-225 St","215 St","207 St","Dyckman St","191 St","181 St","168 St-Washington Hts","157 St","145 St","137 St-City College","125 St","116 St-Columbia University","Cathedral Pkwy (110 St)","103 St","96 St","86 St","79 St","72 St","66 St-Lincoln Center","59 St-Columbus Circle","50 St","Times Sq-42 St","34 St-Penn Station","28 St","23 St","18 St","14 St","Christopher St-Stonewall","Houston St","Canal St","Franklin St","Chambers St","WTC Cortlandt","Rector St","South Ferry Loop","South Ferry"],
	'2':
		["Wakefield-241 St","Nereid Av","233 St","225 St","219 St","Gun Hill Rd","Burke Av","Allerton Av","Pelham Pkwy","Bronx Park East","E 180 St","West Farms Sq-E Tremont Av","174 St","Freeman St","Simpson St","Intervale Av","Prospect Av","Jackson Av","3 Av-149 St","149 St-Grand Concourse","135 St","125 St","116 St","Central Park North (110 St)","96 St","72 St","Times Sq-42 St","34 St-Penn Station","14 St","Chambers St","Park Place","Fulton St","Wall St","Clark St","Borough Hall","Hoyt St","Nevins St","Atlantic Av-Barclays Ctr","Bergen St","Grand Army Plaza","Eastern Pkwy-Brooklyn Museum","Franklin Av-Medgar Evers College","President St-Medgar Evers College","Sterling St","Winthrop St","Church Av","Beverly Rd","Newkirk Av-Little Haiti","Flatbush Av-Brooklyn College"],
	'3':
		["Harlem-148 St","145 St","135 St","125 St","116 St","Central Park North (110 St)","96 St","72 St","Times Sq-42 St","34 St-Penn Station","14 St","Chambers St","Park Place","Fulton St","Wall St","Clark St","Borough Hall","Hoyt St","Nevins St","Atlantic Av-Barclays Ctr","Bergen St","Grand Army Plaza","Eastern Pkwy-Brooklyn Museum","Franklin Av-Medgar Evers College","Nostrand Av","Kingston Av","Crown Hts-Utica Av","Sutter Av-Rutland Rd","Saratoga Av","Rockaway Av","Junius St","Pennsylvania Av","Van Siclen Av","New Lots Av"],
	'4':
		["Woodlawn","Mosholu Pkwy","Bedford Park Blvd-Lehman College","Kingsbridge Rd","Fordham Rd","183 St","Burnside Av","176 St","Mt Eden Av","170 St","167 St","161 St-Yankee Stadium","149 St-Grand Concourse","138 St-Grand Concourse","125 St","86 St","59 St","Grand Central-42 St","14 St-Union Sq","Brooklyn Bridge-City Hall","Fulton St","Wall St","Bowling Green","Borough Hall","Nevins St","Atlantic Av-Barclays Ctr","Franklin Av-Medgar Evers College","Crown Heights-Utica Av"],
	'5':
		["Nereid Av","233 St","225 St","219 St","Gun Hill Rd","Burke Av","Allerton Av","Pelham Pkwy","Bronx Park East","Atlantic Av-Barclays Ctr","Bergen St","Grand Army Plaza","Eastern Pkwy-Brooklyn Museum","Franklin Av-Medgar Evers College","Nostrand Av","Kingston Av","Crown Hts-Utica Av","Sutter Av-Rutland Rd","Saratoga Av","Rockaway Av","Junius St","Pennsylvania Av","Van Siclen Av","New Lots Av"],
	'6':
		["Pelham Bay Park","Buhre Av","Middletown Rd","Westchester Sq-E Tremont Av","Zerega Av","Castle Hill Av","Parkchester","St Lawrence Av","Morrison Av-Soundview","Elder Av","Whitlock Av","Hunts Point Av","Longwood Av","E 149 St","E 143 St-St Mary's St","Cypress Av","Brook Av","3 Av-138 St","125 St","116 St","110 St","103 St","96 St","86 St","77 St","68 St-Hunter College","59 St","51 St","Grand Central-42 St","33 St","28 St","23 St","14 St-Union Sq","Astor Pl","Bleecker St","Spring St","Canal St","Brooklyn Bridge-City Hall"],
	'6X':
		["Pelham Bay Park","Buhre Av","Middletown Rd","Westchester Sq-E Tremont Av","Zerega Av","Castle Hill Av","Parkchester","Hunts Point Av","3 Av-138 St","125 St","116 St","110 St","103 St","96 St","86 St","77 St","68 St-Hunter College","59 St","51 St","Grand Central-42 St","33 St","28 St","23 St","14 St-Union Sq","Astor Pl","Bleecker St","Spring St","Canal St","Brooklyn Bridge-City Hall"],
	'7':
		["Flushing-Main St","Mets-Willets Point","111 St","103 St-Corona Plaza","Junction Blvd","90 St-Elmhurst Av","82 St-Jackson Hts","74 St-Broadway","69 St","61 St-Woodside","52 St","46 St-Bliss St","40 St-Lowery St","33 St-Rawson St","Queensboro Plaza","Court Sq","Hunters Point Av","Vernon Blvd-Jackson Av","Grand Central-42 St","5 Av","Times Sq-42 St","34 St-Hudson Yards"],
	'7X':
		["Flushing-Main St","Mets-Willets Point","Junction Blvd","74 St-Broadway","69 St","61 St-Woodside","52 St","46 St-Bliss St","40 St-Lowery St","33 St-Rawson St","Queensboro Plaza","Court Sq","Hunters Point Av","Vernon Blvd-Jackson Av","Grand Central-42 St","5 Av","Times Sq-42 St","34 St-Hudson Yards"],
	'A':
		["Inwood-207 St","Dyckman St","190 St","181 St","175 St","168 St","163 St-Amsterdam Av","155 St","145 St","135 St","125 St","116 St","Cathedral Pkwy (110 St)","103 St","96 St","86 St","81 St-Museum of Natural History","72 St","59 St-Columbus Circle","50 St","42 St-Port Authority Bus Terminal","34 St-Penn Station","23 St","14 St","W 4 St-Wash Sq","Spring St","Canal St","Chambers St","Fulton St","High St","Jay St-MetroTech","Hoyt-Schermerhorn Sts","Lafayette Av","Clinton-Washington Avs","Franklin Av","Nostrand Av","Kingston-Throop Avs","Utica Av","Ralph Av","Rockaway Av","Broadway Junction","Liberty Av","Van Siclen Av","Shepherd Av","Euclid Av","Grant Av","80 St","88 St","Rockaway Blvd","104 St","111 St","Ozone Park-Lefferts Blvd","Aqueduct Racetrack","Aqueduct-N Conduit Av","Howard Beach-JFK Airport","Broad Channel","Beach 67 St","Beach 60 St","Beach 44 St","Beach 36 St","Beach 25 St","Far Rockaway-Mott Av","Beach 90 St","Beach 98 St","Beach 105 St","Rockaway Park-Beach 116 St"],
	'B':
		["Bedford Park Blvd","Kingsbridge Rd","Fordham Rd","182-183 Sts","Tremont Av","174-175 Sts","170 St","167 St","161 St-Yankee Stadium","155 St","145 St","135 St","125 St","116 St","Cathedral Pkwy (110 St)","103 St","96 St","86 St","81 St-Museum of Natural History","72 St","59 St-Columbus Circle","7 Av","47-50 Sts-Rockefeller Ctr","42 St-Bryant Pk","34 St-Herald Sq","W 4 St-Wash Sq","Broadway-Lafayette St","Grand St","DeKalb Av","Atlantic Av-Barclays Ctr","7 Av","Prospect Park","Church Av","Newkirk Plaza","Kings Hwy","Sheepshead Bay","Brighton Beach"],
	'C':
		["168 St","163 St-Amsterdam Av","155 St","145 St","135 St","125 St","116 St","Cathedral Pkwy (110 St)","103 St","96 St","86 St","81 St-Museum of Natural History","72 St","59 St-Columbus Circle","50 St","42 St-Port Authority Bus Terminal","34 St-Penn Station","23 St","14 St","W 4 St-Wash Sq","Spring St","Canal St","Chambers St","Fulton St","High St","Jay St-MetroTech","Hoyt-Schermerhorn Sts","Lafayette Av","Clinton-Washington Avs","Franklin Av","Nostrand Av","Kingston-Throop Avs","Utica Av","Ralph Av","Rockaway Av","Broadway Junction","Liberty Av","Van Siclen Av","Shepherd Av","Euclid Av"],
	'D':
		["Norwood-205 St","Bedford Park Blvd","Kingsbridge Rd","Fordham Rd","182-183 Sts","Tremont Av","174-175 Sts","170 St","167 St","161 St-Yankee Stadium","155 St","145 St","125 St","59 St-Columbus Circle","7 Av","47-50 Sts-Rockefeller Ctr","42 St-Bryant Pk","34 St-Herald Sq","W 4 St-Wash Sq","Broadway-Lafayette St","Grand St","DeKalb Av","Atlantic Av-Barclays Ctr","Union St","4 Av-9 St","Prospect Av","25 St","36 St","9 Av","Fort Hamilton Pkwy","50 St","55 St","62 St","71 St","79 St","18 Av","20 Av","Bay Pkwy","25 Av","Bay 50 St","Coney Island-Stillwell Av"],
	'E':
		["Jamaica-179 St","169 St","Parsons Blvd","Sutphin Blvd","","","","","","","","","","","","","","","","","","","",""],
	'F':
		[],
	'FX':
		[],
	'FS':
		[],
	'G':
		[],
	'GS':
		[],
	'H':
		["Broad Channel","Beach 90 St","Beach 98 St","Beach 105 St","Rockaway Park-Beach 116 St"],
	'J':
		[],
	'L':
		[],
	'M':
		[],
	'N':
		[],
	'Q':
		[],
	'R':
		[],
	'SI':
		["Tottenville","Arthur Kill","Richmond Valley","Pleasant Plains","Prince's Bay","Huguenot","Annadale","Eltingville","Great Kills","Bay Terrace","Oakwood Heights","New Dorp","Grant City","Jefferson Av","Dongan Hills","Old Town","Grasmere","Clifton","Stapleton","Tompkinsville","St George"],
	'W':
		[],
	'Z':
		[]}
