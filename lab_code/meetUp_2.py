# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:36:00 2018

@author: Kevin
"""
# SOURCED FROM HERE: https://www.analyticsvidhya.com/blog/2015/08/data-scientist-meetup-hack/

import urllib
import json
import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

geolocator = Nominatim(timeout=3) #create object

places = ["san fransisco", "california", "boston ", "new york" , 
          "pennsylvania", "colorado", "seattle", "washington","los angeles", 
          "san diego", "houston", "austin", "kansas", "delhi", "chennai", 
          "bangalore", "mumbai" , "Sydney","Melbourne", "Perth", "Adelaide", 
          "Brisbane", "Launceston", "Newcastle" , "beijing", "shanghai", 
          "Suzhou", "Shenzhen","Guangzhou","Dongguan", "Taipei", "Chengdu", 
          "Hong Kong"]
urls = [] #url lists
radius = 50.0 #add the radius in miles
data_format = "json"
topic = "Python" #add your choice of topic here
sig_id = "190292775" # initialize with your sign id, check sample signed key
sig = "2710fcf81491da3db8f647f2460a591338947bfb" # initialize with your sign, check sample signed key

for place in places: 
    location = geolocator.geocode(place)
    urls.append("https://api.meetup.com/2/groups?offset=0&format=" + 
                data_format + "&lon=" + str(location.longitude) + 
                "&topic=" + topic + "&photo-host=public&page=500&radius=" + 
                str(radius)+"&fields=&lat=" + str(location.latitude) + 
                "&order=id&desc=false&sig_id=" +sig_id + "&sig=" + sig)

city,country,rating,name,members = [],[],[],[],[]

for url in urls:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    data=data["results"] #accessed data of results key only
 
for i in data :
    city.append(i['city'])
    country.append(i['country'])
    rating.append(i['rating'])
    name.append(i['name'])
    members.append(i['members']) 
 
df = pd.DataFrame([city,country,rating,name,members]).T
df.columns=['city','country','rating','name','members']
df.sort(['members','rating'], ascending=[False, False])




