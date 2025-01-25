import json
import os

from backend.CO2_Calculator import app
import parse_responses

from flask import Flask, request
import dotenv
import requests

from backend.parse_responses import parse_response

dotenv.load_dotenv()

CI_KEY = os.getenv("CARBON_INTERFACE_API_KEY")

CI_URL = "https://www.carboninterface.com/api/v1/estimates"

HEADERS = {
    "Authorization": f"Bearer {CI_KEY}",
    "Content-Type": "application/json"
}

keys = ["flights"]
carbon_data_lbs = dict.fromkeys(keys, [])
carbon_data_kg = dict.fromkeys(keys, [])

for key in keys:
    carbon_data_lbs[key] = []
    carbon_data_kg[key] = []

@app.route("/process-flight-data", methods=["POST"])
def get_flight_data():
    departure = request.form.get("curloc")
    destination = request.form.get("desloc")

    data = {
        "type": "flight",
        "passengers": 160,
        "legs": [
            {"departure_airport": departure, "destination_airport": destination}
        ]
    }

    response = requests.post(CI_URL, headers=HEADERS, json=data)
    if(response.status_code == 200):
        response_values = parse_response(response.json())
        carbon_data_lbs["flights"].append(response_values.carbon_lb)
        carbon_data_kg["flights"].append(response_values.carbon_kg)

    return response.status_code



