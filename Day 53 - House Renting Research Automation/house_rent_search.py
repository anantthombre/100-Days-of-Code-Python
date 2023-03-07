from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options


# from webdriver_manager.chrome import ChromeDriverManager
# import time

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

# time.sleep(15)

while(True):
    pass
