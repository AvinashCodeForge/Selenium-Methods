from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://the-internet.herokuapp.com/broken_images")  # Replace with your webpage

# Add an implicit wait to allow elements to load
driver.implicitly_wait(10)

# Find all image elements on the page
images = driver.find_elements(By.XPATH, "//div/img")

if len(images) == 0:
    print("No images found on the page.")
else:
    for img in images:
        try:
            # Wait until the image is fully loaded
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "img"))
            )

            # Check if the image has a non-zero natural width (indicating it's loaded)
            is_image_loaded = driver.execute_script(
                "return arguments[0].naturalWidth > 0;", img)

            if is_image_loaded:
                print(f"Image {img.get_attribute('src')} is loaded successfully.")
            else:
                print(f"Image {img.get_attribute('src')} is broken.")

        except Exception as e:
            print(f"Error checking image {img.get_attribute('src')}: {e}")

# Close the browser
driver.quit()
