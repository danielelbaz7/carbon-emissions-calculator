import json
from dataclasses import dataclass

@dataclass
class Response:
    id: str
    carbon_lb: int
    carbon_kg: int

def parse_response(response):
    parsed = json.loads(response)
    response = Response(
        id=parsed["data"]["id"],
        carbon_lb=parsed["data"]["attributes"]["carbon_lb"],
        carbon_kg=parsed["data"]["attributes"]["carbon_kg"],
    )
    return response