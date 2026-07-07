import requests
import smtplib
from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_PASS = os.getenv("GOOGLE_PASS")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, data, destination_iata, receiver):
        if data.stops == 0:
            msg_body = f"Flight Deals\n\nLow price alert! Only {data.price} GBP to fly from LHR to {destination_iata}."
        else:
            msg_body = (f"Flight Deals\n\nLow price alert! Only {data.price} GBP to fly from LHR to {destination_iata}"
                        f" with {data.stops} in between.")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=GOOGLE_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=receiver,
                                msg=msg_body)

# TWILIO_SID = os.getenv("TWILIO_SID")
# TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
# TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
# TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")
#
# class NotificationManager:
#     #This class is responsible for sending notifications with the deal flight details.
#     def send_message(self, data, destination_iata):
#         client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#         message = client.messages.create(
#             body=f"Low price alert! Only £{data.price} to fly from LHR to {destination_iata} "
#                  f"on {data.out_date} until {data.return_date}",
#             from_=TWILIO_VIRTUAL_NUMBER,
#             to=TWILIO_VERIFIED_NUMBER,
#         )
#         print(message.status)

