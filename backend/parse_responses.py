import json
from dataclasses import dataclass

@dataclass
class Response:
    id: str
    carbon_lb: int
    carbon_kg: int
    def __init__(self, response):
        parsed = json.loads(response)
        self.id = parsed["data"]["id"]
        self.carbon_lb = parsed["data"]["attributes"]["carbon_lb"]
        self.carbon_kg = parsed["data"]["attributes"]["carbon_kg"]