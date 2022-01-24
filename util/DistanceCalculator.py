import math


def calculateDistanceFromCoordinates(lat_1, lng_1, lat_2, lng_2):
    R = 6378.137  # Radius of earth in KM
    dLat = lat_2 * math.pi / 180 - lat_1 * math.pi / 180
    dLon = lng_2 * math.pi / 180 - lng_1 * math.pi / 180
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat_1 * math.pi / 180) * math.cos(
        lat_2 * math.pi / 180) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d * 1000

print(calculateDistanceFromCoordinates(52.376122,4.819205, 52.347390,4.839684))
