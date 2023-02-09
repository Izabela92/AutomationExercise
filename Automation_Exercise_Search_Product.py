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

#Click on 'Products' button
driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a"). click()

# Wait for the ads to be closed
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ns-nk2bx-e-16'))).click()
except:
    print("Close button not found")

# Verify that the user is navigated to the ALL PRODUCTS page
try:
    driver.find_element(By.CSS_SELECTOR, ".product-header").is_displayed()
    print("User is navigated to ALL PRODUCTS page successfully.")
except:
    print("User is not navigated to ALL PRODUCTS page.")

#Enter product name in search input and click search button
driver.find_element(By.XPATH, "//*[@id='search_product']").send_keys("Sleeveless Dress")
driver.find_element(By.XPATH, "/html/body/section[1]/div/button/i"). click()

#Verify 'SEARCHED PRODUCTS' is visible
try:
    driver.find_element(By.CSS_SELECTOR, ".title").is_displayed()
    print("The products list is visible.")
except:
    print("The products list is not visible.")

# Verify all the products related to search are visible
products = driver.find_elements(By.XPATH, "//div[@class='product']")
result = "Products found" if len(products) > 0 else "No products found"
print(result)

# Close the browser
driver.quit()