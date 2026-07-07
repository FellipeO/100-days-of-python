import requests
import os
import dotenv

dotenv.load_dotenv(".env")

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("FLIGHT_KEY")
        self.endpoint = "https://app.100daysofpython.dev/v1/flights/search"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, stop):
        self.parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }
        if stop == "1":
            self.parameters["stops"] = "1"
        response = requests.get(self.endpoint, params=self.parameters)
        response.raise_for_status()
        return response.json()
