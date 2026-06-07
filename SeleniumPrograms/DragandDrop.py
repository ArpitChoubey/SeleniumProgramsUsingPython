from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_drag():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    drag_elem= driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")

    action = ActionChains(driver)

    action.click_and_hold(on_element=drag_elem).perform()

    time.sleep(10)
    driver.quit()