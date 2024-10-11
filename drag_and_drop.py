import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://the-internet.herokuapp.com/drag_and_drop')


# common locator for drag and drop

def dragAndDrop(input):
    # Locating element
    return driver.find_element(By.XPATH, f"//header[text()='{input}']")


# Mouse Action Right-click on the element
mouseActions = ActionChains(driver)
mouseActions.drag_and_drop(dragAndDrop('A'), dragAndDrop('B')).perform()

# short wait
time.sleep(10)

# close the browser
driver.quit()
