from configparser import ConfigParser

import pandas as pd

from classes.PerformanceEvaluation.PerformanceCalculator import PerformanceCalculator
from classes.RouteFinder.HereMaps.HereMapsEmergencyRouteFinder import HereMapsEmergencyRouteFinder

# Loading keys from config file
config = ConfigParser()
config.read("./config/config.ini")

#
api_key = config['HERE_MAPS_KEY']['api_key']
routefinder = HereMapsEmergencyRouteFinder(api_key)
# routefinder.getEmergencyRoute(52.3778525, 4.8311525, 52.3579215, 4.8685845)
pc = PerformanceCalculator(routefinder)
fire_stations = pd.read_csv('./data/firestations_updated.csv')
fire_stations_with_trucks = pd.read_csv('./data/firestations_4_4_evening.csv')
pc.calculatePerformance(fire_stations,fire_stations_with_trucks)
# print(datetime.datetime.now().utcnow())
