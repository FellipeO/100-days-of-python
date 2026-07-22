from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Keep Chrome open after program finishes executing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(5)
driver.find_element(By.ID, value="langSelect-EN").click()
time.sleep(5)
cookie = driver.find_element(By.ID, value="bigCookie")
current_cookies = driver.find_element(By.ID, value="cookies").text.split()[0]
print(current_cookies)
wait_time = 5
timeout = time.time() + wait_time
five_min = time.time() + 60 * 5
while True:
    cookie.click()

    if time.time() > timeout:
        cookie_count = int(driver.find_element(By.ID, value="cookies").text.replace(",","").split()[0])
        products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
        best_product = None

        for product in reversed(products):
           if "enabled" in product.get_attribute("class"):
               best_product = product
               break

        if best_product:
            best_product.click()

        timeout = time.time() + wait_time

    if time.time() > five_min:
        print(driver.find_element(By.ID, value="cookies").text)
        break



