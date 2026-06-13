import csv
import os

FILE = "data/vehicle_log.csv"

def log_data(
        timestamp,
        lat,
        lon,
        status,
        alert):

    file_exists = os.path.isfile(FILE)

    with open(FILE,
              "a",
              newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Latitude",
                "Longitude",
                "Status",
                "Alert"
            ])

        writer.writerow([
            timestamp,
            lat,
            lon,
            status,
            alert
        ])