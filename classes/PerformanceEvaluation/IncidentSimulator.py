import pandas as pd

class IncidentSimulator():
    def __init__(self, seed, size=10):
        self.__seed = seed

    def getIncidents(self):
        incidents = pd.read_csv('./data/simulated_incidents.csv')
        return incidents
