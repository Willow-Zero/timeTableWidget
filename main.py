from google.transit import gtfs_realtime_pb2
import requests
import gtfs_kit as gk
import pandas as pd
import folium
import datetime




def getNextStopTime(stops,line,feed):
	now = datetime.datetime.now()
	currenttime=now.strftime("%H:%M:%S")
	currentdate = now.strftime("%Y%m%d")
	next = "00:00:00"
	stopentries = [y for y in gk.stops.build_stop_timetable(feed,x,[currentdate]).values if y[0] == line]
	stopnext=[]
	for z in stopentries:
		for z in stopentries:
			if int(z[7].split(":")[0]) > int(currenttime.split(":")[0]):
				stopnext = z
				break
	return(stopnext)




stops=["Astor Pl"]
line="6"



response = requests.get('http://web.mta.info/developers/data/nyct/subway/google_transit.zip')

with open("NYC67.zip", mode="wb") as file:
	file.write(response.content)
path = 'NYC67.zip'

feed = (gk.read_feed(path, dist_units='km'))
pd.set_option('display.max_rows', 99999)
pd.set_option('display.max_columns', 99999)
pd.set_option('display.width', 99999)

#print(gk.list_feed(path))
stopids = [x[0] for x in feed.get_stops().values if x[1] in stops]

#print(feed.get_stops().values[0][1])
#print(feed.get_routes())
#print(gk.routes.routes_to_geojson(feed, ["6","H"]))
#print(gk.stop_times.get_stop_times(feed,"20240212").values)
#print(gk.stops.build_stop_timetable(feed,"636N",[currentdate]).values[7])
#print(currentdate)

#for x in stopids:
#	print(getNextStopTime(x,line,feed))
#print(next)
#print(stopentries)


feedrt = gtfs_realtime_pb2.FeedMessage()
responsert = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs', headers={'x-api-key':'nHWpwh63jqaJMyYbpQ9rx6nSTMTGtGWu24F1mB8p'})
feedrt.ParseFromString(responsert.content)
print(feedrt.entity[0].trip_update)



