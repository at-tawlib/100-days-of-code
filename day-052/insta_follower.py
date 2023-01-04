# 04-01-23 Instagram follower bot with Selenium
import time
from decouple import config

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")

class InstaFollower:

    def __init__(self):
        """Create selenium driver on initialization"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        """Open instagram and login to account"""
        self.driver.get("https://www.instagram.com/")
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

    def find_followers(self):
        """Go to football page and open on the following"""
        self.driver.get("https://www.instagram.com/football.newz/")
        # click on following link
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a/div').click()

        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            # time.sleep(2)


    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div div button")
        # count = 0
        for button in follow_buttons:
            try:
                print(button.text)
                # code is not efficient
                #self.driver.execute_script("arguments[0].click();", button)
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                cancel_button.click()


insta = InstaFollower()
insta.login()
time.sleep(10)
insta.find_followers()
time.sleep(10)
insta.follow()
