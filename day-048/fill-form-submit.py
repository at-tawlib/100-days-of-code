# 27-12-22 Fill form with details, then click submit

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://id.heroku.com/login")

# go to form to enter login details
email = driver.find_element(By.NAME, "email")
email.send_keys("abc@gmail.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("123445")

# click the login button
login = driver.find_element(By.NAME, "commit")
login.click()

while True:
    pass