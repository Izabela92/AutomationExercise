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

# Verify that the products list is visible
try:
    driver.find_element(By.CSS_SELECTOR, "#product_list").is_displayed()
    print("The products list is visible.")
except:
    print("The products list is not visible.")

# Wait for the ads to be closed
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ns-nk2bx-e-16'))).click()
except:
    print("Close button not found")

# Click on the 'View Product' button of the first product
driver.find_element(By.CSS_SELECTOR, 'div.col-sm-4:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()

# Verify that the user is landed on the product detail page
try:
    driver.find_element(By.CSS_SELECTOR, ".product-name").is_displayed()
    print("User is landed to product detail page.")
except:
    print("User is not landed to product detail page.")

# Verify that the product details are visible: product name, category, price, availability, condition, brand
try:
    driver.find_element(By.CSS_SELECTOR, ".product-name").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".product-category").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".product-price").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".product-availability").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".product-condition").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".product-brand").is_displayed()
    print("Product details are visible: product name, category, price, availability, condition, brand")
except:
    print("Product details are not visible: product name, category, price, availability, condition, brand")

# Close the browser window
driver.quit()