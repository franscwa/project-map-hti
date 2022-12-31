#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import geojson

import folium

print(type([34.343,35.3535]))

# Load the GeoJSON file
with open('haiti.geojson') as mapData:
     geojson_data = mapData.read()

# Create a Map instance
m = folium.Map(location=[18.9712, 72.2852], zoom_start=10)

# Add the GeoJSON data to the map
folium.GeoJson(geojson_data).add_to(m)

html = """
<form method="post" style="background-color: rgba(0, 0, 0, 0.5); position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1;">
  <label for="location" style="color: white;">Location:</label><br>
  <input type="text" id="location" name="location" style="color: white; background-color: transparent;"><br>
  <br>
  <label for="title" style="color: white;">Title:</label><br>
  <input type="text" id="title" name="title" style="color: white; background-color: transparent;"><br>
  <br>
  <label for="description" style="color: white;">Description:</label><br>
  <input type="text" id="description" name="description" style="color: white; background-color: transparent;"><br>
  <br>
  <input type="submit" value="Submit" style="color: white; background-color: transparent; border: 1px solid white;">
</form> 
"""
folium.Html(html, script=True).add_to(m)

#this is where the user puts in the location

#convert to lat/long
#builder? for list of folium markers,
#list.add(folium.Marker())

# for f in list, make the add the markers to map




# Display the map
