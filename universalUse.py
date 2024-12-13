import time

def printIcon(icon,stationName,date,arrivalTime,departureTime,destination,heading,colorcode):
        g = 31 #89x24 assumed size, TODO: improve sizing 
        if len(stationName) > g:
                stationName = stationName[0:31]
        bar = "═"*(g+1)
        print("\033[2J╔═════════════════════════════════════════════════╦" + bar + "╗")
        dataArray = ["Station Name:".ljust(g),stationName.ljust(g),bar,"Date:".ljust(g),date.ljust(g),bar,"Arrival Time:".ljust(g),arrivalTime.ljust(g),bar,"Departure Time:".ljust(g),departureTime.ljust(g).ljust(g),bar,"Destination:".ljust(g),destination.ljust(g),bar,"Heading:".ljust(g),heading.ljust(g),bar,"".ljust(g),"".ljust(g),"".ljust(g),"","","","","","","","","","","","","","","",""]
        i=0
        y = [" ║"," ║"," ╠"," ║"," ║"," ╠"," ║"," ║"," ╠"," ║"," ║"," ╠"," ║"," ║"," ╠"," ║"," ║"," ╠"," ║"," ║"," ║"]
        u = [" ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ "," ║"]
        for x in icon:
                print("║" + colorcode + x + "\x1b[0m" + y[i] + dataArray[i]+ u[i])
                i = i+1
        print("╚═════════════════════════════════════════════════╩" + bar + "╝")
        time.sleep(2.5)

