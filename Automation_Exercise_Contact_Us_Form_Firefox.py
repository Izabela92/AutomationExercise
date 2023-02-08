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

# Click on 'Contact Us' button
driver.get("https://automationexercise.com/contact_us")


# Enter name, email, subject, and message
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("John Doe")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("johndoe@example.com")
driver.find_element(By.XPATH, "//input[@name='subject']").send_keys("Automation Test")
driver.find_element(By.XPATH, "//textarea[@name='message']").send_keys("Test message")

# Upload file
driver.find_element(By.XPATH, "//input[@type='file']").send_keys("C:\\Users\\izawr\\PycharmProjects\\pythonProject2\\Contact_Us_Form.txt")

# Click 'Submit' button
driver.find_element(By.NAME, 'submit').click()

# Click OK button
driver.switch_to.alert.accept()

# Verify success message 'Success! Your details have been submitted successfully.' is visible
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[2]")


# Click 'Home' button and verify that landed to home page successfully
driver.get("https://automationexercise.com/")
assert "Automation Exercise" in driver.title

# Close the browser
driver.close()
