from flask import Flask, render_template, request, Blueprint
from flask_cors import CORS

import json
import os

import parse_responses

import requests
import dotenv
import jsonify

app = Flask(__name__)
CORS(app)

import API_Management

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


dotenv.load_dotenv()

CI_KEY = os.getenv("CARBON_INTERFACE_API_KEY")

CI_URL = "https://www.carboninterface.com/api/v1/estimates"
MAKES_URL = "https://www.carboninterface.com/api/v1/vehicle_makes"

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
    departure = request.args.get('curloc', "").strip()
    destination = request.args.get('desloc', "").strip()

    if not departure and not destination:
        return {"error": "Missing or invalid parameters"}, 400


    data = {
        "type": "flight",
        "passengers": 160,
        "legs": [
            {"departure_airport": departure, "destination_airport": destination}
        ]
    }


    response = requests.post(CI_URL, headers=HEADERS, json=data)


    print(f"Request Payload: {data}, API Response Status: {response.status_code}, Response: {response.text}")
    print('Hello!')
    if response.status_code == 201:
        res_json = response.json()
        carbon_lb = res_json["data"]["attributes"]["carbon_lb"]
        carbon_kg = res_json["data"]["attributes"]["carbon_kg"]

        carbon_data_lbs["flights"].append({"emissions": carbon_lb})
        carbon_data_kg["flights"].append({"emissions": carbon_kg})

    return ("", response.status_code)


@app.route("/get-makes", methods=["GET"])
def get_makes():
    response = requests.get(MAKES_URL, headers=HEADERS)
    if(response.status_code == 200):
        all_makes_names = [item["data"]["attributes"]["name"] for item in response.json()]
        all_makes_ids = [item["data"]["id"] for item in response.json()]
        makes_data = {
            "names": all_makes_names,
            "ids": all_makes_ids
        }
        return json.dumps(makes_data)
    return None

@app.route("/get-total-emissions", methods=["GET"])
def get_total_emissions():
    total_emissions_kg = 0
    total_emissions_lb = 0

    for num in carbon_data_kg["flights"]:
        total_emissions_kg += num["emissions"]
    for num in carbon_data_lbs["flights"]:
        total_emissions_lb += num["emissions"]

    return json.dumps({"kg": total_emissions_kg, "lb": total_emissions_lb})



if __name__ == '__main__':
    app.run(debug=True)