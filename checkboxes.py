import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://the-internet.herokuapp.com/checkboxes')

# Locating elements
checkboxes = driver.find_elements(By.XPATH, "//form[@id='checkboxes']//input")
for checkbox in checkboxes:
    checkbox.click()

# short wait
time.sleep(2)

# close the browser
driver.quit()
