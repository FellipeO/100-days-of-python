import smtplib

import requests
from datetime import datetime

MY_LAT = -16.791175 # Your latitude
MY_LONG = -49.250336 # Your longitude

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5):
        return True
    else:
        return False

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + UTC_OFFSET
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + UTC_OFFSET
    current_hour = datetime.now().hour
    print(sunrise)
    print(sunset)
    if sunrise >= current_hour or sunset >= current_hour:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

MY_EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
UTC_OFFSET = -3 #Your timezone as an offset

if is_iss_close() and is_dark():
    print("email sent")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject: Iss Visible\n\nLook up")



