import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "SENDER EMAIL HERE"
PASSWORD = "PASSWORD HERE"

now = dt.datetime.now()
df = pandas.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

letters = ["letter_1", "letter_2", "letter_3"]

for person in birthdays:
    if person["month"] == now.month and person["day"] == now.day:
        with open(f"letter_templates/{random.choice(letters)}.txt", "r") as file:
            email_content = file.read()
            email_content = email_content.replace("[NAME]", person["name"])
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()

                connection.login(user=MY_EMAIL, password=PASSWORD)

                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=person["email"],
                                    msg=f"Subject: Happy Birthday!\n\n{email_content}")
