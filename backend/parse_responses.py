import json
from dataclasses import dataclass

@dataclass
class Response:
    id: str
    carbon_lb: int
    carbon_kg: int
    def __init__(self, response):
        try:
            self.id = response.get("data", {}).get("id", "")
            self.carbon_lb = response.get("data", {}).get("attributes", {}).get("carbon_lb", 0)
            self.carbon_kg = response.get("data", {}).get("attributes", {}).get("carbon_kg", 0)
        except Exception as e:
            print(f"Error parsing response: {e}")
            self.id = ""
            self.carbon_lb = 0
            self.carbon_kg = 0
