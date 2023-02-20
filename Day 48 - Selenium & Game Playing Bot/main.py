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

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# print([event_time.text for event_time in event_times])
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# print([event_name.text for event_name in event_names])

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)