import random

def generate_coordinates():
    latitude = 17.3850 + random.uniform(-0.005, 0.005)
    longitude = 78.4867 + random.uniform(-0.005, 0.005)

    return latitude, longitude