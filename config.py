# This is the config file for TimeTableWidget. The format is as follows
# CITY={"lineName":["exampleStop","exampleStop2"]}
#  note that these need to be the exact stop names in the apis, unless ive futzed with the way the program interprets things
#  ill try to provide a list of the valid stop names for each service i implement
#  if you give no stops (the dict is empty) nothing will be done. 
#  also at the end there's the scroll mode config stuff, ill comment on that when i get to it
#  also there are of course some other config options, ill comment on those when they show up
#  please, enjoy my crappy widget

# NYC rail services
#  services:
#  FS = Franklin Ave Shuttle
#  GS = 42nd St Shuttle
#  H = Rockaway Park Shuttle
#  SI = SIR
#      1, 2, 3, 4, 5, 5X, 6, 6X, 7, 7X, A, B, C, D, E, F, FX, FS, G, GS, H, J, L, M, N, Q, R, SI, W, Z
#     
NYC = {"M":["Broadway-Lafayette St"],"J":["Gates Av"]}
# PATH lines (order is:Newark-World Trade, Hoboken-World Trade,Journal Square-33rd, Hoboken-33rd)
PATHNWKWTCStops=[]
PATHHOBWTCStops=[]
PATHJSQ33Stops=[]
PATHHOB33Stops=[]
# Metro-North(MN) Lines
MNPVLStops=[] # Pascack Valley Line      
MNPJLStops=[] # Port Jervis Line
MNHaLStops=[] # Harlem Line      
MNHuLStops=[] # Hudson Line
MNNHLStops=[] # New Haven Line 
# LIRR
LIRRMLStops=[] # Mail Line
LIRRABStops=[] # Atlantic Branch   
LIRRMBStops=[] # Montauk Branch
LIRRBBStops=[] # Babylon Branch   
LIRRBPBStops=[] # Belmont Park Branch 
LIRRCBStops=[] # Central Branch   
LIRRCTZStops=[] # City Terminal Zone   
LIRRFRBStops=[] # Far Rockaway Branch   
LIRRHBStops=[] # Hempstead Branch   
LIRRLBBStops=[] # Long Beach Branch   
LIRROBBStops=[] # Oyster Bay Branch   
LIRRPJBStops=[] # Port Jefferson Branch   
LIRRPWBStops=[] # Port Washington Branch   
LIRRRkBStops=[] # Ronkonkoma Branch   
LIRRWHBStops=[] # West Hempstead Branch
 



