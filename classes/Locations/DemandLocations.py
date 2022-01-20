""" This file supports the retrieving of all the demand locations"""
from classes.Locations.LocationsHelper import LocationsHelper


class DemandLocations():
    def __init__(self):
        self._locations_helper = LocationsHelper('demand_locations.csv')

