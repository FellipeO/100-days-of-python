import requests
import datetime as dt
import os
import dotenv

dotenv.load_dotenv(".env")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")
google_sheet_endpoint = os.getenv("SHEET_ENDPOINT")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

query_input = input("Tell me which exercises you did: ")

parameters = {
    "query":query_input,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)

row_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

new_row = {
    "workout": {
        "date":dt.datetime.now().strftime("%d/%m/%Y"),
        "time":dt.datetime.now().strftime("%H:%M:%S"),
        "exercise":response.json()["exercises"][0]["name"].title(),
        "duration":response.json()["exercises"][0]["duration_min"],
        "calories":response.json()["exercises"][0]["nf_calories"],
    }
}
requests.post(google_sheet_endpoint, json=new_row, headers=row_headers)