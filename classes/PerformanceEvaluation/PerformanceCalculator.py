from configparser import ConfigParser
import util.DistanceCalculator as DC
from classes.PerformanceEvaluation.IncidentSimulator import IncidentSimulator
import statistics
from classes.RouteFinder.HereMaps.HereMapsEmergencyRouteFinder import HereMapsEmergencyRouteFinder


class PerformanceCalculator():
    def __init__(self, routefinder, seed = 0):
        self.__seed = seed
        self.routefinder = routefinder
        self.incident_simulator = IncidentSimulator(seed)

    def calculatePerformance(self, placement_a, placement_b):
        incidents = self.incident_simulator.getIncidents()
        times_a = []
        times_b = []
        for index, incident in incidents.iterrows():
            lat, lng = self._findClosestLocation(incident.lat, incident.lng, placement_a)
            time = self.routefinder.getEmergencyRoute(lat, lng, incident.lat, incident.lng)
            times_a.append(time)
        print(f"Mean time a: {statistics.mean(times_a)}")
        print(f"Mean time b: {statistics.mean(times_b)}")

    def _findClosestLocation(self, lat, lng, parkingspots):
        closest_coords = (None,None)
        min_distance = 100000
        for index, parkingspot in parkingspots.iterrows():
            distance = DC.calculateDistanceFromCoordinates(lat, lng, parkingspot.latitude, parkingspot.longitude)
            if distance < min_distance:
                min_distance = distance
                closest_coords = (parkingspot.latitude, parkingspot.longitude)
        print(closest_coords)
        return closest_coords
