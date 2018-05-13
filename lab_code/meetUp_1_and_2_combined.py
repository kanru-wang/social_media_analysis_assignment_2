# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:36:00 2018

@author: Kevin
"""

from __future__ import unicode_literals

import requests
#import json
import time
import codecs
import sys
import pandas as pd

from geopy.geocoders import Nominatim

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

cities = ["Sydney","Melbourne", "Perth", "Adelaide", "Brisbane"]

api_key= "1e3c223b136a3967b576525b167f"
radius = 50.0 #add the radius in miles
topic = "Python" #add your choice of topic here

geolocator = Nominatim(timeout=3) #create object


def get_results(params):
    # Test it here https://secure.meetup.com/meetup_api/console/?path=/2/groups
    request = requests.get("http://api.meetup.com/2/groups",params=params)
    data = request.json()
	
    return data

city,country,rating,name,members,category = [],[],[],[],[],[]

# Get your key here https://secure.meetup.com/meetup_api/key/
for city_name in cities:
    per_page = 200
    results_we_got = per_page
    offset = 0
    location = geolocator.geocode(city_name)
    while (results_we_got == per_page):
        # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
        response=get_results({"sign":"true",
                              "lon": location.longitude,
                              "lat": location.latitude,
                              "radius": radius,
                              "topic": topic,
                              "key": api_key, 
                              "page": per_page, 
                              "offset": offset })
        time.sleep(1)
        offset += 1
        results_we_got = response['meta']['count']
        for group in response['results']:
            if "category" in group:
                category.append(group['category']['name'])
            city.append(group['city'])
            country.append(group['country'])
            rating.append(group['rating'])
            name.append(group['name'])
            members.append(group['members']) 

    time.sleep(1)
 
df = pd.DataFrame([city,country,rating,name,members,category]).T
df.columns=['city','country','rating','name','members','category']
df.sort_values(['members','rating'], ascending=[False, False])


