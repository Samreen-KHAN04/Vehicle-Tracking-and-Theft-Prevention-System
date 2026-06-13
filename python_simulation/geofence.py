from geopy.distance import geodesic

HOME_LOCATION = (17.3850, 78.4867)
SAFE_RADIUS = 500

def check_geofence(lat, lon):

    current = (lat, lon)

    distance = geodesic(
        HOME_LOCATION,
        current
    ).meters

    return distance <= SAFE_RADIUS