import os
import time
import dotenv

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

dotenv.load_dotenv(".env")
TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/fKCWYFgGYUki7Hkh4G7DXmrAMqrIp_Yi"
EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASS")

#Keep Chrome open after program finishes executing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)

driver.find_element(By.CSS_SELECTOR, "button[class^='btn-tindog-login']").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn-facebark").click()

time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
#Login
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(EMAIL)

password_field = driver.find_element(By.ID, "pass")
password_field.send_keys(PASS)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[class='btn-secondary']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

while True:
    time.sleep(2)
    try:
        driver.find_element(By.CLASS_NAME, "btn-like").click()
    except ElementClickInterceptedException:
        driver.find_element(By.CLASS_NAME, "match-popup-link").click()





