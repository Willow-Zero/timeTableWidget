from google.transit import gtfs_realtime_pb2
import requests
import gtfs_kit as gk
import pandas as pd
import datetime
import config as c
import iconDict
import universalUse as uu
from sec import MTA_API_KEY




def getNextStopTime(stops,line,feed):
	now = datetime.datetime.now()
	currenttime=now.strftime("%H:%M:%S")
	currentdate = now.strftime("%Y%m%d")
	next = "00:00:00"
	stopentries = [y for y in gk.stops.build_stop_timetable(feed,stops,[currentdate]).values if y[0] == line]
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




def main():
        stopDict = c.NYC
        staticURL='http://web.mta.info/developers/data/nyct/subway/google_transit.zip'

        response = requests.get(staticURL)

        with open("NYC67.zip", mode="wb") as file:
	        file.write(response.content)
        path = 'NYC67.zip'

        feed = (gk.read_feed(path, dist_units='km'))
        pd.set_option('display.max_rows', 99999)
        pd.set_option('display.max_columns', 99999)
        pd.set_option('display.width', 99999)

        # print(gk.list_feed(path))
        stopids = []
        stopNameToID = []
        for key in stopDict:
                stopids = [x[0] for x in feed.get_stops().values if x[1] in stopDict[key]]
                # print(feed.get_stops().values)
                stopNameToID = [x[1] for x in feed.get_stops().values if x[1] in stopDict[key]]
                nextstoptimes=[]
                for x in stopids:
	                nextstoptimes.append(list(getNextStopTime(x,key,feed)))
                i=0
                for x in nextstoptimes:
                        if x != []:
                                heading = ""
                                if (x[6][-1] == 'N'):
                                        heading = "Uptown"
                                elif (x[6][-1] == 'S'):
                                        heading = "Downtown"
                                uu.printIcon(iconDict.Lines["NYC"][x[0]],stopNameToID[i],x[10],x[7],x[8],x[3],heading)
                                i = i+1

        feedrt = gtfs_realtime_pb2.FeedMessage()
        responsert = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs', headers={'x-api-key':MTA_API_KEY})
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

        # ([5])

