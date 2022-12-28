import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config

TWITTER_EMAIL = config('TWITTER_EMAIL')
TWITTER_PASSWORD = config('TWITTER_PASSWORD')

class InternetSpeedTwitterBot:

    def __init__(self):
          self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          self.up = 0
          self.down = 0

    def get_internet_speed(self):
        """Uses selenium to get the current internet speed and set the up and down values"""
        time.sleep(3)  # delay for 3 seconds
        self.driver.get("https://www.speedtest.net/")
        # click on the go button to start
        go_btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_btn.click()

        time.sleep(60)  # delay for 1 minute
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(self.down)
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(self.up)

    def tweet_at_provider(self):
        """open twitter and post a text"""
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        # click login
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(5)
        # enter email address
        self.driver.find_element(By.NAME, 'text').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
        time.sleep(3)
        # enter password
        self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(10)
        # post message
        enter_tweet = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span > br")
        enter_tweet.send_keys(f"My upload speed is {self.up} and my download speed is {self.down}")
        tweet = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
        tweet.click()
        time.sleep(10)
        self.driver.quit()