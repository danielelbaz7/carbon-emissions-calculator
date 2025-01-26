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

keys = ["flights", "drive", "electricity"]
carbon_data_lbs = dict.fromkeys(keys, [])
carbon_data_kg = dict.fromkeys(keys, [])

for key in keys:
    carbon_data_lbs[key] = [0]
    carbon_data_kg[key] = [0]

@app.route("/process-flight-data", methods=["POST"])
def get_flight_data():
    departure = request.args.get('curloc', "").strip()
    destination = request.args.get('desloc', "").strip()

    if not departure or not destination:
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
    if(response.status_code == 201):
        response_values = parse_responses.Response(response.json())
        carbon_data_lbs["flights"].append(response_values.carbon_lb/160)
        carbon_data_kg["flights"].append(response_values.carbon_kg/160)
        return "Created", 201

    return "Failed", response.status_code

@app.route("/process-car-data", methods=["POST"])
def get_car_data():
    model = request.args.get('deslocCar', "").strip()
    distance = request.args.get('milDriv', "").strip()
    data = {
        "type": "vehicle",
        "distance_unit": "mi",
        "distance_value": distance,
        "vehicle_model_id": model,
    }
    response = requests.post(CI_URL, headers=HEADERS, json=data)
    print(f"Request Payload: {data}, API Response Status: {response.status_code}, Response: {response.text}")
    if(response.status_code == 201):
        response_values = parse_responses.Response(response.json())
        carbon_data_lbs["vehicles"][0] = response_values.carbon_lb
        carbon_data_kg["vehicles"][0] = response_values.carbon_kg
        return "Created", 201
    return "Failed", response.status_code

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

@app.route("/get-models", methods=["POST"])
def get_models():
    make = request.args.get('make', "").strip()
    response = requests.get(f"{MAKES_URL}/{make}/vehicle_models", headers=HEADERS)
    if response.status_code == 200:
        all_models_names = [item["data"]["attributes"]["name"] for item in response.json()]
        all_models_ids = [item["data"]["id"] for item in response.json()]
        models_data = {
            "names": all_models_names,
            "ids": all_models_ids
        }
        return json.dumps(models_data)
    return None

@app.route("/get-total-emissions", methods=["GET"])
def get_total_emissions():
    total_emissions_kg = 0
    total_emissions_lb = 0

    for num in carbon_data_kg["flights"]:
        total_emissions_kg += num
    for num in carbon_data_lbs["flights"]:
        total_emissions_lb += num

    total_emissions_kg += carbon_data_kg["drive"][0] + carbon_data_kg["electricity"][0]
    total_emissions_lb += carbon_data_lbs["drive"][0] + carbon_data_lbs["electricity"][0]

    return json.dumps({"kg": total_emissions_kg, "lb": total_emissions_lb})



if __name__ == '__main__':
    app.run(debug=True)