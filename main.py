import datetime

from classes.RouteFinder.HereMaps.HereMapsEmergencyRouteFinder import HereMapsEmergencyRouteFinder
from configparser import ConfigParser

# Loading keys from config file
config = ConfigParser()
config.read("./config/config.ini")

#
api_key = config['HERE_MAPS_KEY']['api_key']
routefinder = HereMapsEmergencyRouteFinder(api_key)
routefinder.getEmergencyRoute('x', 'y')
# print(datetime.datetime.now().utcnow())
