import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


def input_text(input):
    # Locating elements
    driver.find_element(By.XPATH, f"//button[text()='{input}']").click()
    time.sleep(5)


input_text('Add Element')
input_text('Delete')

# close the browser
driver.quit()
