# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Launch the browser
driver = webdriver.Firefox()

# Navigate to the URL
driver.get("http://automationexercise.com")

# Verify the home page is visible successfully
assert "Automation Exercise" in driver.title

#Click on 'Test Cases' button
driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a"). click()

#Verify user is navigated to test cases page successfully
try:
    driver.find_element(By.CSS_SELECTOR, ".title > b:nth-child(1)").is_displayed()
    print("User is navigated to Test Cases page successfully.")
except:
    print("User is not navigated to Test Cases page.")

time.sleep(10)
# Close the browser
driver.quit()