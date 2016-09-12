#!/usr/bin/python3

# http://www.ncdc.noaa.gov/cdo-web/webservices/v2#stations

import urllib.request
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Build the URL
token   = config["NOAA"]["token"]
baseurl = "http://www.ncdc.noaa.gov/cdo-web/api/v2/stations?"
#options = "datasetid=GHCND&startdate=2016-01-01&datacategoryid=TMAX,TMIN&locationid=ST:WA"
options = "datasetid=GHCND&startdate=2016-01-01&datacategoryid=TEMP&extent=46,-123,48,-122"
url     = baseurl + options

# Stream & print the data
request = urllib.request.Request(url)
request.add_header("token", token)

f = open("d:/Projects/degreeday/apiOutput.txt", "w")

try:
    with urllib.request.urlopen(request) as stream:
        streamStr = stream.readall().decode("utf-8") 
        data = json.loads(streamStr)
        
        f.write(str(data) + "\r\n")
        
except urllib.error.URLError as e:
        f.write(e.read).decode("utf8", 'ignore')

f.close()