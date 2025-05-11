import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
USERNAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

# Selenium Chrome Setup
options = Options()
options.add_argument("--remote-debugging-pipe")

# Disable automation bar
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


# Use Service with default chromedriver and options
service = Service()
driver = webdriver.Chrome(service=service, options=options)

try:
    # === Step 1: Open the login page ===
    driver.get("https://inkasure.easyhrworld.com")
    time.sleep(2)

    # === Step 2: Fill in login form ===
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "btnSignin").click() 
    time.sleep(2)

    # === Step 3: Go to attendance page ===
    driver.get("https://inkasure.easyhrworld.com/attendance") 
    time.sleep(5)
    
    # === Step 4: Click Clock In ===
    driver.find_element(By.ID, "btnCheckIn").click()
    print("Clock-in button clicked.")
    time.sleep(2)

    input("Press Enter to exit and close Chrome...")

except Exception as e:
    print(f"Error: {e}")