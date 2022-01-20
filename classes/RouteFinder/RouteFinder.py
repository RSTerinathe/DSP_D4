class RouteFinder():
    """
    Finds a route and the corresponding information from waypoint A to B for an Emergency vehicle.
    This class kind of functions as an abstract class, any new RouteFinder should be implemented with the functions in this class.
    """
    def getEmergencyRoute(self, origin_lat, origin_lng, destination_lat, destination_lng):
        raise NotImplementedError("This function has not yet been implemented")
