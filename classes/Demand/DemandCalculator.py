import numpy as np
import pandas as pd

class DemandCalculator():
    def __init__(self, incident_data, demand_points):
        self.incident_data = incident_data
        self.demand_points = demand_points

    def getTotalDemand(self):
        demand_points = self.demand_points['Wijkcode'].unique()
        print(demand_points)
        cpy = self.demand_points.copy()
        cpy = cpy.drop(columns=['OBJECTNUMMER', 'Stadsdeelcode','Oppervlakte_m2','WijkID','WKT_LNG_LAT','WKT_LAT_LNG'])
        cpy['demand'] = np.nan
        i = 0
        for demand_point in demand_points:
            if sum(self.incident_data['code'].str.contains(demand_point)):
                indexes = cpy[cpy['Wijkcode'] == demand_point]
                total_incidents = self.incident_data[self.incident_data['code'] == demand_point]['count'].sum()
                cpy.loc[cpy.Wijkcode == demand_point, 'demand'] = self.getScaledDemand(total_incidents)
            else:
                cpy.loc[cpy.Wijkcode == demand_point, 'demand'] = 1


        print(cpy)
        print(cpy['demand'].max())
        return cpy

    def getDemandForTimeOfDay(self, time_of_day):
        demand_points = self.demand_points['Wijkcode'].unique()
        print(demand_points)
        cpy = self.demand_points.copy()
        cpy = cpy.drop(columns=['OBJECTNUMMER', 'Stadsdeelcode','Oppervlakte_m2','WijkID','WKT_LNG_LAT','WKT_LAT_LNG'])
        cpy['demand'] = np.nan
        i = 0
        for demand_point in demand_points:
            if sum(self.incident_data['code'].str.contains(demand_point)):
                total_incidents = self.incident_data[np.bitwise_and(self.incident_data['dagdeel'] == time_of_day, self.incident_data['code'] == demand_point)]['count'].sum()
                cpy.loc[cpy.Wijkcode == demand_point, 'demand'] = self.getScaledDemand(total_incidents, 5)
            else:
                cpy.loc[cpy.Wijkcode == demand_point, 'demand'] = 1


        print(cpy)
        print(cpy['demand'].max())
        return cpy


    def getScaledDemand(self, nr, divide=1):
        if nr < (200/ divide):
            return 1
        if nr < (500/ divide):
            return 2
        if nr < (1000/ divide):
            return 3
        return 4
