import requests
from bs4 import BeautifulSoup
import os
import smtplib
import dotenv

dotenv.load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_PASS = os.getenv("GOOGLE_PASS")
PRODUCT_URL = os.getenv("PRODUCT_URL")

response = requests.get(url=PRODUCT_URL,
                        headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0",
                                 "Accept-Language":"en-US,en;q=0.9"})
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

price = float(f"{soup.find(name="span", class_="a-price-whole").text}{soup.find(name="span", class_="a-price-fraction").text}")
if price < 450:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()

        connection.login(user=MY_EMAIL, password=GOOGLE_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Nintendo Switch 2 System"
                                f"is now ${price:.2f}\nhttps://a.co/d/0dNOl9nL".encode("utf-8"))
