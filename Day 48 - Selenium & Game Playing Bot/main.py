from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chrome_driver_path = "../chromedriver_mac_arm64/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.amazon.in/Instant-Pot-Duo-Multi-Functional-Pressure/dp/B01NBKTPTS")

# while(True):
#     pass

# driver.close()

# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)