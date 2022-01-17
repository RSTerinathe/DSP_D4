import datetime

from classes.RouteFinder.HereMaps.UrlBuilder import buildUrl
from classes.RouteFinder.RouteFinder import RouteFinder

import classes.RouteFinder.HereMaps.Routes as Routes
import requests

class HereMapsEmergencyRouteFinder(RouteFinder):
    """Uses the HereMaps API to calculate the route"""

    def __init__(self, api_key, timeout = 20):
        self._api_key = api_key
        self._timeout = timeout

    def calculateRoute(self, origin, destination):
        return 1

    def getEmergencyRoute(self, origin_lat, origin_lng, destination_lat, destination_lng):
        url = buildUrl(
            base_url=Routes.WAYPOINTS_BASE_URL,
            route=Routes.WAYPOINTS_CALCULATE_ROUTE,
            # Hardcoded for now since it is just a test
            parameters=
            {
                'apiKey' : self._api_key,
                'waypoint0': f"{origin_lat},{origin_lng}",
                'waypoint1': f"{destination_lat},{destination_lng}",
                'mode' : self.getModeParameters(),
                'departure':'2022-01-13T16:18:38',
                'alternatives':'0'
            }
        )
        response = requests.get(url)
        print(response.content)

    def getModeParameters(self, enableTraffic = False):
        mode =  ['fastest','emergency']
        if enableTraffic:
            mode.append('traffic:enabled')
        return mode

    def getDateTimeString(self):
        print(datetime.datetime.now())
