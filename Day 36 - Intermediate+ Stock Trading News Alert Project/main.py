from twilio.rest.bulkexports.v1.export import day

import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
import datetime as dt


yesterday = str(dt.date.today() - dt.timedelta(days=1))
previous_day = str(dt.date.today() - dt.timedelta(days=4))

load_dotenv(".env")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API = os.getenv("AV_API")
NEWS_API = os.getenv("NEWS_API")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")

parameters_av = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":AV_API,
}

parameters_news = {
    "apiKey":NEWS_API,
    "q":COMPANY_NAME,
    "searchIn":"title,description",
    "from":"2026-06-29",

}

message_content = ""
response = requests.get("https://www.alphavantage.co/query", params=parameters_av)
response.raise_for_status()
yesterday_close = float(response.json()["Time Series (Daily)"][yesterday]["4. close"])
previous_day_close = float(response.json()["Time Series (Daily)"][previous_day]["4. close"])

if yesterday_close < previous_day_close * 0.95 or yesterday_close > previous_day_close * 1.05:
    percentage = ((yesterday_close - previous_day_close) / previous_day_close) * 100
    news_response = requests.get("https://newsapi.org/v2/everything", params=parameters_news)
    news_response.raise_for_status()

    if percentage > 0:
        message_content = f"{STOCK}: 🔺{percentage:.2f}%\n"
    else:
        message_content = f"{STOCK}: 🔻{percentage *-1:.2f}\n%"
    for i in range(3):
        message_content += f"Headline: {news_response.json()["articles"][i]["title"]}\n"
        message_content += f"Brief: {news_response.json()["articles"][i]["description"]}\n\n"
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body=message_content,
        from_="[FROM_NUMBER]",
        to="[TO_NUMBER]",
    )
    print(message.status)

