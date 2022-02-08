import pandas as pd

import util.DistanceCalculator as DC
from classes.PerformanceEvaluation.IncidentSimulator import IncidentSimulator
import statistics
from time import sleep

class PerformanceCalculator():
    def __init__(self, routefinder, seed = 0):
        self.__seed = seed
        self.routefinder = routefinder
        self.incident_simulator = IncidentSimulator(seed)

    def calculatePerformance(self, placement_a, placement_b):
        incidents = self.incident_simulator.getIncidents()
        times_a = []
        times_b = []
        i = 0
        diff = 0
        for index, incident in incidents.iterrows():
            print(incident.Adres)
            lat, lng = self._findClosestLocation(incident.lat, incident.lng, placement_a)
            time = self.routefinder.getEmergencyRoute(lat, lng, incident.lat, incident.lng)
            times_a.append(time)
            sleep(0.5)
            lat2, lng2 = self._findClosestLocation(incident.lat, incident.lng, placement_b)
            if lat2 == lat and lng2 == lng:
                time2 = time
            else:
                time2 = self.routefinder.getEmergencyRoute(lat2, lng2, incident.lat, incident.lng)
                sleep(0.5)
                if (time2 >= time):
                    time2 = time
                else:
                    i += 1
                    diff += (time - time2)
            times_b.append(time2)
            print(f"A: {time}, B: {time2}")
        print(f"Mean time a: {statistics.mean(times_a)}")
        print(f"Mean time b: {statistics.mean(times_b)}")
        print(f"Cases of improvement: {i}, average difference: {diff/i}")
        print(len(times_a))

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
