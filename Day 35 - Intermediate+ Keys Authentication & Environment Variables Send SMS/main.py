import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(".env.py")
weather_api_key = os.getenv("OW_API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
parameters = {
    "lat":"-16.814839",
    "lon":"-49.255829",
    "appid":weather_api_key,
    "cnt":"4"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Vai chover hoje, use um guarda-chuva",
        from_="FROM_NUMBER",
        to="TO_NUMBER",
    )
    print(message.status)

