import requests

API_KEY = "4QA5DNM2FPBA52IT "

def upload_data(lat, lon, status, alert):

    payload = {
        "api_key": API_KEY,
        "field1": lat,
        "field2": lon,
        "field3": 1 if status == "SAFE" else 0,
        "field4": 1 if alert == "THEFT_ALERT" else 0
    }

    response = requests.post(
        "https://api.thingspeak.com/update",
        data=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)