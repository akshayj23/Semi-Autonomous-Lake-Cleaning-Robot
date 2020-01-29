from neo6 import GpsNeo6
gps=GpsNeo6(port="/dev/ttyAMA0",debit=9600,diff=2)    
while True:
    gps.traite()
    print(gps) # print all info
    latstr=str(gps.latitude)
    lonstr=str(gps.longitude)
    print(gps.latitude,gps.longitude)
    print(latstr,lonstr)
