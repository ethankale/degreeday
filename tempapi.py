#!/usr/bin/python3

import urllib.request
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Build the URL
token   = config["NOAA"]["token"]
baseurl = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?"
options = "datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01"
url     = baseurl + options

# Stream & print the data
request = urllib.request.Request(url)
request.add_header("token", token)

with urllib.request.urlopen(request) as stream:
    streamStr = stream.readall().decode("utf-8") 
    data = json.loads(streamStr)
    
    max = data["results"][5]["value"]
    
    f = open("d:/Projects/degreeday/apiOutput.txt", "w")
    f.write("Max Temperature (tenths of a degree C): " + str(max) )