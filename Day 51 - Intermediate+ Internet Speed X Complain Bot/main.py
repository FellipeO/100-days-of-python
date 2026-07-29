import os
import dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

dotenv.load_dotenv(".env")
PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = os.getenv("Y_EMAIL")
Y_PASSWORD = os.getenv("Y_PASSWORD")
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

#Keep Chrome open after program finishes executing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, "from-ookla-go-green").click()
        WebDriverWait(self.driver,120).until(ec.presence_of_element_located((By.CLASS_NAME, "my-1")))
        self.up = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3").text
        self.down = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3").text
        print(f"Up: {self.up}\nDown: {self.down}")


    def tweet_at_provider(self):
        if float(self.up) < PROMISED_UP or float(self.down) < PROMISED_DOWN:
            self.driver.get("https://app.100daysofpython.dev/services/y")
            self.driver.find_element(By.CLASS_NAME, "y-login-link").click()

            email_field = self.driver.find_element(By.ID, "email")
            email_field.clear()
            email_field.send_keys(Y_EMAIL)

            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(Y_PASSWORD)

            self.driver.find_element(By.CLASS_NAME, "y-btn-primary").click()

            tweet_box = self.driver.find_element(By.ID, "tweet-compose")
            tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up"
                                f" when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            self.driver.find_element(By.ID, "post-btn").click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
