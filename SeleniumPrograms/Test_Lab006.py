from selenium import webdriver



def test_sample():


    driver = webdriver.Chrome()
    driver.get("https://www.osprey.com/")
    driver.forward()
    driver.back()
    driver.refresh()