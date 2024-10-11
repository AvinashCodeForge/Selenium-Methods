import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://the-internet.herokuapp.com/dropdown')

drop_down = driver.find_element(By.ID, "dropdown")
select = Select(drop_down)
select.select_by_visible_text('Option 1')

# short wait
time.sleep(5)

# close the browser
driver.quit()
