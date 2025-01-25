import json
from dataclasses import dataclass

@dataclass
class Response:
    id: str
    carbon_lb: int

def parse_response(response):
    parsed = json.loads(response)
    electric = Response(
        id=parsed["data"]["id"],
        carbon_lb=parsed["data"]["attributes"]["carbon_lb"],
    )
    return electric