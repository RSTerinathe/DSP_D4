""" This script calculates the driving times from a set of locations where firetrucks can be located (parking spots + firestations) to a set of demand points."""
import pandas as pd
import csv
from configparser import ConfigParser
from classes.RouteFinder.HereMaps.HereMapsEmergencyRouteFinder import HereMapsEmergencyRouteFinder
from time import sleep
from util.DistanceCalculator import calculateDistanceFromCoordinates

# Get the API key for the here maps api
config = ConfigParser()
config.read("../config/config.ini")
api_key = config['HERE_MAPS_KEY']['api_key']

routefinder = HereMapsEmergencyRouteFinder(api_key)
origin_locations = pd.read_csv('../data/parkingspots_revised.csv')
# demand_locations = pd.read_csv('../data/buurten_information.csv')
# origin_locations = pd.read_csv('../data/firestations_updated.csv')
demand_locations = pd.read_csv('../data/wijken.csv')
print(f"Calculating the travelling time for {len(origin_locations) * len(demand_locations)} combinations")
i = 0

csv_file = open('../data/travelling_times_firestations2.csv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter =',')
csv_writer.writerow(['origin_coords', 'demand_coords', 'travel_time', 'wijkcode', 'wijknaam'])
nr = 0
for demand_point in demand_locations.iterrows():
    j = 0
    print (f"{i} out of {len(demand_locations)}.")
    demand_lat = demand_point[1]['LAT']
    demand_lng = demand_point[1]['LNG']
    wijkcode = demand_point[1]['Wijkcode']
    wijknaam = demand_point[1]['Wijknaam']
    for origin in origin_locations.iterrows():
        print('.', end='')
        origin_lat = origin[1]['latitude']
        origin_lng = origin[1]['longitude']

        # If the straight line distance is less than 3.5 km then we calculate the travel time
        if calculateDistanceFromCoordinates(origin_lat, origin_lng, demand_lat, demand_lng) < 3600:
            # Calculate travelling time between two points
            travelling_time = routefinder.getEmergencyRoute(origin_lat, origin_lng, demand_lat, demand_lng)
            sleep(0.1)
        else:
            travelling_time= 99999
        csv_writer.writerow([f"{ str(origin_lat) + '_' + str(origin_lng)}", f"{str(demand_lat) + '_' + str(demand_lng)}", travelling_time, wijkcode, wijknaam])
    i+= 1
    print('')
