def printIcon(icon,stationName,date,arrivalTime,departureTime,destination):
        g = max(len(stationName),len(date),len(arrivalTime),len(destination),16)
        bar = "═"*(g+1)
        print("╔═══════════════════════════════════════════════════╦═" + bar + "╗")
        dataArray = ["Station Name:"'hi'.ljust(g),stationName.ljust(g),bar,"Date:".ljust(g),date.ljust(g),bar,"Arrival Time:".ljust(g),arrivalTime.ljust(g),bar,"Departure Time:".ljust(g),departureTime.ljust(g).ljust(g),bar,"Destination:".ljust(g),destination.ljust(g),bar,"".ljust(g),"".ljust(g),bar,"".ljust(g),"".ljust(g),"".ljust(g),"","","","","","","","","","","","","","","",""]
        i=0
        y = [" ║ "," ║ "," ╠═"," ║ "," ║ "," ╠═"," ║ "," ║ "," ╠═"," ║ "," ║ "," ╠═"," ║ "," ║ "," ╠═"," ║ "," ║ "," ╠═"," ║ "," ║ "," ║ "]
        u = [" ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ ","╣"," ║ "," ║ "," ║"]
        for x in icon:
                print("║" + x + y[i] + dataArray[i]+ u[i])
                i = i+1
        print("╚═══════════════════════════════════════════════════╩═" + bar + "╝")


