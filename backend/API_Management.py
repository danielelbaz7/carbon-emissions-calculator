from backend.CO2_Calculator import app
import requests

keys = ["flights"]
carbon_data_kg = dict.fromkeys(keys, [])
carbon_data_lbs = dict.fromkeys(keys, [])

for key in keys:
    carbon_data_kg[key] = []
    carbon_data_kg[key] = []

@app.route("/process-flight-data", methods=["POST"])
def get_flight_data():
    departure = request.form.get("curloc")