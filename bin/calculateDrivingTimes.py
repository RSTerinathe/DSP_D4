""" This script calculates the driving times from a set of locations where firetrucks can be located (parking spots + firestations) to a set of demand points."""
from configparser import ConfigParser
from classes.Locations.LocationsHelper import LocationsHelper
from classes.RouteFinder.HereMaps.HereMapsEmergencyRouteFinder import HereMapsEmergencyRouteFinder
from time import sleep

# Get the API key for the here maps api
config = ConfigParser()
config.read("./config/config.ini")
api_key = config['HERE_MAPS_KEY']['api_key']

routefinder = HereMapsEmergencyRouteFinder(api_key)
origin_locations = LocationsHelper('').getLocations()
demand_locations = LocationsHelper('demand_points.csv').getLocations()

#
print(f"Calculating the travelling time for {len(origin_locations) * len(demand_locations)} combinations")
i = 0
for demand_point in demand_locations:
    print (f"{i} out of {len(demand_locations)}.")
    for origin_point in origin_locations:
        print('.', end='')
        # Calculate travelling time between two points
        travelling_time = routefinder.getEmergencyRoute()
        # Write to file
        sleep(0.1)
    print('')
