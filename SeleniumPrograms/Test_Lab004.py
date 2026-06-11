import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://www.osprey.com/")
    print(driver.page_source)