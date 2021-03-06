import datetime

from classes.RouteFinder.HereMaps.UrlBuilder import buildUrl
from classes.RouteFinder.RouteFinder import RouteFinder

import classes.RouteFinder.HereMaps.HereApiRoutes as Routes
import requests

class HereMapsEmergencyRouteFinder(RouteFinder):
    """Uses the HereMaps API to calculate the route"""

    def __init__(self, api_key, timeout = 20):
        self._api_key = api_key
        self._timeout = timeout

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
                'mode' : self._getModeParameters(),
                'departure': self._getDepartureTime(),
                'alternatives':'0'
            }
        )
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)
            return 100000
        json_response = response.json()
        return json_response["response"]['route'][0]['summary']['travelTime']

    def _getModeParameters(self, enableTraffic = False):
        mode =  ['fastest','emergency']
        if enableTraffic:
            mode.append('traffic:enabled')
        return mode

    def _getDepartureTime(self):
        return '2022-01-13T16:18:38'
