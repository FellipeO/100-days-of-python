import os
import dotenv
import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

dotenv.load_dotenv(".env")
FORM = os.getenv("FORM_LINK")
URL = "https://appbrewery.github.io/Zillow-Clone/"
header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0"}

response = requests.get(URL, headers=header)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

links = [link.get("href") for link in soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")]
prices = [re.split(r'[^0-9$,]', price.text)[0] for price in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
addresses = [" ".join(address.text.replace("|", "").split()) for address in soup.find_all(name="address")]

#Keep Chrome open after program finishes executing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM)
time.sleep(1)
for i in range(len(addresses)):
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(addresses[i])
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(prices[i])
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(links[i])
    driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
    time.sleep(1)
