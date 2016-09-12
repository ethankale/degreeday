#!/usr/bin/python3

import urllib.request
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Olympia station ID
station = "GHCND:USW00024227"

# Build the URL
token   = config["NOAA"]["token"]
baseurl = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?"
#options = "datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01"
options = "datasetid=GHCND&datatypeid=TMAX,TMIN&startdate=2016-01-01&enddate=2016-09-11&limit=750&stationid=" + station
url     = baseurl + options

# Stream & print the data
request = urllib.request.Request(url)
request.add_header("token", token)

with urllib.request.urlopen(request) as stream:
    streamStr = stream.readall().decode("utf-8") 
    data = json.loads(streamStr)
    
    maxTemps = {}
    minTemps = {}
    
    #max = data["results"][5]["value"]
    
    for result in data["results"]:
        if result["datatype"] == "TMAX":
            maxTemps[result["date"]] = result["value"] * 0.1
        if result["datatype"] == "TMIN":
            minTemps[result["date"]] = result["value"] * 0.1
    
    f = open("d:/Projects/degreeday/apiOutput.txt", "w")
    f.write(str(data) + "\r\n")
    f.write(str(len(maxTemps)))
    f.write(str(maxTemps) + "\r\n" )
    f.write(str(len(minTemps)))
    f.write(str(minTemps) + "\r\n" )
    
    f.close()
    
    

