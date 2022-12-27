# 27-12-2022 extract upcoming events from the python website and stores them in a dictionary
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
# get events titles
events_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li a")

# get events dates
events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li time")

# create a dictionary to store events and event dates
events_dict = {}
number = 0
for index in range(len(events_dates)):
    events_dict[number] = {
        'time': events_dates[index].text,
        'name':events_titles[index].text
    }
    number += 1
print(events_dict)

driver.quit()