class FireTruckLocation():
    def __init__(self, lat, lng, name=""):
        self._lat = lat
        self._lng = lng
        self._name = name

    def getCoordinatesAsString(self):
        return f"{self._X},{self._Y}"

    def getLat(self):
        return self._lat

    def getLng(self):
        return self._lng
