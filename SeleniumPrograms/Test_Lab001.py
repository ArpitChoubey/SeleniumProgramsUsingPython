from selenium import webdriver



def test_sample():


    driver = webdriver.Chrome()
    driver.get("https://www.osprey.com/")
    assert driver.current_url == "https://www.osprey.com/"

    driver.quit()