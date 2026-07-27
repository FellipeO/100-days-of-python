from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import os
import dotenv
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

def login ():
    email_field = driver.find_element(By.ID, value="email-input")
    email_field.clear()
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field = driver.find_element(By.ID, value="password-input")
    password_field.clear()
    password_field.send_keys(ACCOUNT_PASSWORD)
    driver.find_element(By.ID, value="submit-button").click()
    try:
        WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.ID, "schedule-link")))
    except TimeoutException:
        raise Exception


def book_class(class_):
    class_.click()
    WebDriverWait(driver, 2).until(lambda d: class_.text == "Booked")


def retry(func, retries=7, description=None):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(4)


# Add your credentials at the top of your script
dotenv.load_dotenv(".env")
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

#Keep Chrome open after program finishes executing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

driver.find_element(By.ID, value="login-button").click()

WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.ID, "email-input")))
retry(login)

#Classes Objects
classes = driver.find_elements(By.CSS_SELECTOR, value="div[class^='ClassCard_cardHeader']")
classes_six = [class_ for class_ in classes if "Time: 6:00 PM" in class_.text]

#Counters
classes_booked = 0
classes_waitlisted = 0
already_booked = 0
total_processed = 0

detailed_list = []

day = None
for class_ in classes_six:
    try:
        day = class_.find_element(By.XPATH, "./ancestor::div[contains(@id, 'tue')]")
    except NoSuchElementException:
        pass
    try:
        day = class_.find_element(By.XPATH, "./ancestor::div[contains(@id, 'thu')]")
    except NoSuchElementException:
        pass
    if day:
        class_text = class_.find_element(By.CSS_SELECTOR, value="h3[id^='class-name-']").text
        day_text = day.find_element(By.TAG_NAME, value="h2").text
        if class_.find_element(By.CSS_SELECTOR, value="button[id^='book-button']").text == "Booked":
            print(f"Already booked: {class_text} on {day_text} ")
            detailed_list.append(f"[Already Booked] {class_text} on {day_text}")
            already_booked += 1
        elif class_.find_element(By.CSS_SELECTOR, value="button[id^='book-button']").text == "Waitlisted":
            print(f"Already on waitlist: {class_text} on {day_text}")
            detailed_list.append(f"[Already Waitlisted] {class_text} on {day_text}")
            already_booked += 1
        elif class_.find_element(By.CSS_SELECTOR, value="button[id^='book-button']").text == "Join Waitlist":
            retry(lambda: book_class(class_.find_element(By.CSS_SELECTOR, value="button[id^='book-button']")))
            print(f"Joined waitlist: {class_text} on {day_text}")
            detailed_list.append(f"[New Waitlist] {class_text} on {day_text}")
            classes_waitlisted += 1
            time.sleep(0.5)
        else:
            retry(lambda: book_class(class_.find_element(By.CSS_SELECTOR, value="button[id^='book-button']")))
            print(f"Booked {class_text} on {day_text}")
            detailed_list.append(f"[New Booking] {class_text} on {day_text}")
            classes_booked += 1
            time.sleep(0.5)
    day = None

total_processed = classes_booked + classes_waitlisted + already_booked
print(f"\n--- BOOKING SUMMARY ---\nClasses booked: {classes_booked}\nWaitlists joined: {classes_waitlisted}"
      f"\nAlready booked/waitlisted: {already_booked}\nTotal classes processed: {total_processed}")

total_verified = 0
driver.find_element(By.ID, "my-bookings-link").click()
verify_classes = driver.find_elements(By.CSS_SELECTOR, value="div[id^='booking-card-booking']")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
for class_ in verify_classes:
    print(f"Verified: {class_.find_element(By.CSS_SELECTOR, value="h3[id^='booking-class-name-booking']").text}")
    total_verified += 1

print(f"\n--- VERIFICATION RESULTS ---\nExpected: {total_processed}\nFound: {total_verified}")
if total_verified != total_processed:
    print(f"\nMismatch: Missing {total_processed - total_verified } bookings")
