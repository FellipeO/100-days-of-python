import os
import dotenv
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

dotenv.load_dotenv(".env")
MY_USERNAME = os.getenv("MY_USERNAME")
PASSWORD = os.getenv("PASSWORD")
SIMILAR_ACCOUNT = "chefsteps"

BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
LOGIN_URL = f"{BASE_URL}/login"

#Keep Chrome open after program finishes executing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)
        username_field = self.driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(MY_USERNAME)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(PASSWORD)

        self.driver.find_element(By.CLASS_NAME, "naan-btn-primary").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='popup-save-login']/div/div[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='popup-notifications']/div/button[2]").click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}")
        self.driver.find_element(By.CLASS_NAME, "naan-followers-link").click()
        popup = self.driver.find_element(By.CLASS_NAME, "followers-scroll")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(1)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, "naan-follower-row")
        for button in follow_buttons:
            time.sleep(1)
            try:
                button.find_element(By.CLASS_NAME, "naan-follow-btn").click()
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, "/html/body/div[6]/div/button[2]").click()


follower = InstaFollower ()
follower.login()
follower.find_followers()
follower.follow()