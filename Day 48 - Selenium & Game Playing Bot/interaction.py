from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
#article_count.click()

# wikipedia = driver.find_element(By.LINK_TEXT, "Wikipedia")
# wikipedia.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.find_element(By.NAME, "fName").send_keys("Abcd")
driver.find_element(By.NAME, "lName").send_keys("Efgh")
driver.find_element(By.NAME, "email").send_keys("ijkl@mnop.qrs")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(10)
