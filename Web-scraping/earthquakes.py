import requests
import json

website = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")

if website.ok:
    earthquakes_dict = website.json()
    for i in earthquakes_dict["features"]:
        if i["properties"]["felt"] != None and i["properties"]["felt"] != 0:
            quake_ratio = i["properties"]["mag"]
            quake_place = i["properties"]["place"].capitalize()
            people_felt = i["properties"]["felt"]
            print("%1.2f. %s. %s people felt earthquake." % (quake_ratio, quake_place, people_felt))
else:
    print("Website error has appeard")
        
        