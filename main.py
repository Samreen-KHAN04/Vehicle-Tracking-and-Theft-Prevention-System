import time
from datetime import datetime

from python_simulation.gps_simulator import generate_coordinates
from python_simulation.geofence import check_geofence
from python_simulation.theft_detector import detect_theft
from python_simulation.logger import log_data
from dashboard.thingspeak_upload import upload_data
for i in range(20):

    lat, lon = generate_coordinates()

    inside = check_geofence(
        lat,
        lon
    )

    theft = detect_theft(
        inside
    )

    status = (
        "SAFE"
        if inside
        else "OUTSIDE_ZONE"
    )

    alert = (
        "THEFT_ALERT"
        if theft
        else "NO_ALERT"
    )

    maps_link = (
        f"https://maps.google.com/?q={lat},{lon}"
    )

    print("\n--------------------")
    print("Latitude:", lat)
    print("Longitude:", lon)
    print("Status:", status)
    print("Alert:", alert)
    print("Map:", maps_link)

    log_data(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    round(lat, 6),
    round(lon, 6),
    status,
    alert
    )

    upload_data(
        lat,
        lon,
        status,
        alert
    )
    time.sleep(2)