import requests
import os
import dotenv

dotenv.load_dotenv(".env")
TOKEN = os.getenv("SHEET_TOKEN")
row_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:
    def __init__(self):
        self.prices_endpoint = os.getenv("PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("USERS_ENDPOINT")


    def read_data(self):
        return requests.get(self.prices_endpoint, headers=row_headers).json()

    def get_customer_emails(self):
        return requests.get(self.users_endpoint, headers=row_headers).json()


    def update_sheet(self, price, destination):
        data = requests.get(self.prices_endpoint, headers=row_headers).json()
        rows = data.get("prices", [])
        change_row_id = None
        parameters = {
            "price":{
                "lowestPrice": f"{price}"
            }
        }
        for row in rows:
            if row["iataCode"] == destination:
                change_row_id = row.get("id")
        requests.put(f"{self.prices_endpoint}/{change_row_id}", headers=row_headers, json=parameters)


