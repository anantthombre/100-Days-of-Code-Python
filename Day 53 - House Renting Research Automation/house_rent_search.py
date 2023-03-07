from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.zillow.com/")

time.sleep(30)

rent_button = driver.find_element(By.LINK_TEXT, "Rent")
# print(rent_button.tag_name)
rent_button.click()


# while(True):
#     pass
