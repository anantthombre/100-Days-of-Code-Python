from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options


# from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser = webdriver.Safari()

# makes the browser wait if it can't find an element


browser.get("https://www.zillow.com/")
browser.maximize_window()
# driver.get("https://www.zillow.com/")
browser.implicitly_wait(10)
# time.sleep(30)

rent_button = browser.find_element(By.LINK_TEXT, "Rent")
# print(rent_button.tag_name)
rent_button.click()

browser.implicitly_wait(10)

price_button = browser.find_element(By.CSS_SELECTOR, "#price button")
print(price_button.tag_name)
print(price_button.text)
price_button.click()

browser.implicitly_wait(10)

max_rent = "3000"
max_input = browser.find_element(By.XPATH, '//*[@id="price-form"]/div/fieldset/div/div[2]/div/div/div/input')
max_input.send_keys(max_rent)
max_rent_apply_button = browser.find_element(By.XPATH, '//*[@id="price"]/div/footer/div/div/button')
max_rent_apply_button.click()
bed_bath_button = browser.find_element(By.XPATH, '//button[text()="Beds & Baths"]')
bed_bath_button.click()

time.sleep(15)

# while(True):
#     pass
