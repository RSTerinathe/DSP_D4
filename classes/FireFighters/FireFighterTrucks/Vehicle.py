class Vehicle():
    """
    Parameters:
        weight in kg
        height in cm
        length in cm
    """
    def __init__(self, weight=None, height=None, length=None, isTruck=False):
        self._weight = weight
        self._height = height
        self._length = length
        self._isTruck = isTruck

    def getWeight(self):
        return self._weight

    def getHeight(self):
        return self._height

    def getLength(self):
        return self._length

    def isTruck(self):
        return self._isTruck
