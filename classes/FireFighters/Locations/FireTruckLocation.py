class FireTruckLocation():
    def __init__(self, X, Y, name=""):
        self._X = X
        self._Y = Y
        self._name = name

    def getCoordinatesAsString(self):
        return f"{self._X},{self._Y}"

    def getCoordinates(self):
        return self._X, self._Y
