from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


URL = "https://www.zillow.com/cambridge-ma/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A42.41439899528081%2C%22east%22%3A-70.99376714990234%2C%22south%22%3A42.342372110434106%2C%22west%22%3A-71.23065985009765%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22mp%22%3A%7B%22max%22%3A4000%7D%2C%22price%22%3A%7B%22max%22%3A768293%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3934%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
response = requests.get(URL, headers=header)
zillow_cambridge_ma_webpage = response.text

soup = BeautifulSoup(zillow_cambridge_ma_webpage, "html.parser")
prices = soup.select("div.StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 bqsBln span")

print(prices)

