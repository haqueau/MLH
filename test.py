from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver
service = Service('/Users/auyonhaque/Downloads/chrome-mac-arm64/Google Chrome for Testing.app')  # Replace with the correct path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# LinkedIn credentials
linkedin_username = 'your_email@example.com'
linkedin_password = 'your_password'

try:
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Enter username
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(linkedin_username)

    # Enter password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(linkedin_password)

    # Submit login form
    password_field.send_keys(Keys.RETURN)

    # Wait for login to complete
    time.sleep(5)  # Adjust sleep time as necessary for your internet speed

    # Navigate to the job post page
    jobPost = "https://www.linkedin.com/jobs/view/3971216047/"  # Update with the correct job post URL
    driver.get(jobPost)

    # Wait for the page to load
    time.sleep(5)  # Adjust sleep time as necessary for your internet speed

    # Extract job position
    position_tag = driver.find_element(By.CLASS_NAME, "t-24.t-bold.inline")
    position = position_tag.text if position_tag else "Job position not found"
    print("Position: ", position)

    # Extract company name
    company_tag = driver.find_element(By.CLASS_NAME, "job-details-job-unified-top-card__company-name")
    companyName = company_tag.text if company_tag else "Company name not found"
    print("Company Name: ", companyName)

finally:
    # Close the WebDriver
    driver.quit()
