import pandas as pd
""" This helper helps to load Locations from a file """
class LocationsHelper():
    def __init__(self, file_location, data_path = './data/'):
        self._data_path = data_path
        self._file_location = file_location
        self._locations = None

    def loadLocationsFromCsv(self):
        return pd.read_csv(self._data_path+self._file_location)

    def getLocations(self):
        if not self._locations:
            self._locations = self.loadLocationsFromCsv()
        return self._locations
