import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://the-internet.herokuapp.com/context_menu')

# Locating element
right_click = driver.find_element(By.ID, "hot-spot")

# Mouse Action Right-click on the element
mouseActions = ActionChains(driver)
mouseActions.context_click(right_click).perform()

# short wait
time.sleep(2)

# close the browser
driver.quit()
