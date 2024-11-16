from google.transit import gtfs_realtime_pb2
import requests
import gtfs_kit as gk
import pandas as pd
import folium
import datetime
import config as c
import iconDict
import universalUse as uu



stopDict = c.NYC
staticURL='http://web.mta.info/developers/data/nyct/subway/google_transit.zip'





def getNextStopTime(stops,line,feed):
	now = datetime.datetime.now()
	currenttime=now.strftime("%H:%M:%S")
	currentdate = now.strftime("%Y%m%d")
	next = "00:00:00"
	stopentries = [y for y in gk.stops.build_stop_timetable(feed,x,[currentdate]).values if y[0] == line]
	stopnext=[]
	for z in stopentries:
		for z in stopentries:
			if int(z[7].split(":")[0]) == int(currenttime.split(":")[0]):
			        if int(z[7].split(":")[1]) == int(currenttime.split(":")[1]):
			                if int(z[7].split(":")[2]) >= int(currenttime.split(":")[2]):
                                                stopnext = z
                                                break
			        if int(z[7].split(":")[1]) > int(currenttime.split(":")[1]):
                                        stopnext = z
                                        break
			if int(z[7].split(":")[0]) > int(currenttime.split(":")[0]):
				stopnext = z
				break
	return(stopnext)



response = requests.get(staticURL)

with open("NYC67.zip", mode="wb") as file:
	file.write(response.content)
path = 'NYC67.zip'

feed = (gk.read_feed(path, dist_units='km'))
pd.set_option('display.max_rows', 99999)
pd.set_option('display.max_columns', 99999)
pd.set_option('display.width', 99999)

#print(gk.list_feed(path))
stopids = []
stopNameToID = []
for key in stopDict:
        stopids = [x[0] for x in feed.get_stops().values if x[1] in stopDict[key]]
        stopNameToID = [x[1] for x in feed.get_stops().values if x[1] in stopDict[key]]
        nextstoptimes=[]
        for x in stopids:
	        nextstoptimes.append(list(getNextStopTime(x,key,feed)))
        i=0
        for x in nextstoptimes:
                if x != []:
                        uu.printIcon(iconDict.Lines["NYC"][x[0]],stopNameToID[i],x[10],x[7],x[8],x[3])
                        i = i+1

#print(stopNameToID)

#for x in feed.get_stops().values:
#    print(x)
#print(feed.get_stops().values[0][1])
#print(feed.get_routes())
#print(gk.routes.routes_to_geojson(feed, ["5X"]))
#print(gk.stop_times.get_stop_times(feed,"20241115").values)
#print(gk.stops.build_stop_timetable(feed,"636N",[currentdate]).values[7])
#print(currentdate)
#print(nextstoptimes)
        #print(x[3])
#print(next)
#print(stopentries)

feedrt = gtfs_realtime_pb2.FeedMessage()
responsert = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs', headers={'x-api-key':'nHWpwh63jqaJMyYbpQ9rx6nSTMTGtGWu24F1mB8p'})
feedrt.ParseFromString(responsert.content)
for x in feedrt.entity:
      #  print(x.trip_update.stop_time_update[0].stop_id)
        try:
                if x.trip_update.stop_time_update[0].stop_id in stopids:
                   #     print(x.trip_update.trip.start_date)
                        for z in x.trip_update.stop_time_update:
                                if z.stop_id in stopids:
                                        pass
                     #                   print(z.arrival)
                       #                 print(datetime.datetime.fromtimestamp(z.arrival.time))
        except:
                pass
#        else:
#                print(x.trip_update.trip.trip_id)
        
#([5])

