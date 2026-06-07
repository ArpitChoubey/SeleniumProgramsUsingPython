import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.osprey.com/customer/account/create/")

    first_name = driver.find_element(By.XPATH, "//input[@id='firstname']")
    first_name.Send_keys("Arpit")

    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "arpit").key_up(Keys.SHIFT).perform()

    time.sleep(10)
    driver.close()
