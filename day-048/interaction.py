# 27-12-22 Interacts with wikipedia webpage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# click article counts
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
# article_count.click()

# find element by link text portal and click on it
community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# community_portal.click()

# find element by name of search bar, enter a text and search
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

while True:
    pass