from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/at-tawlib/Softwares/chromedriver_linux64/ChromeService"
# using the path is deprecated use a Service object instead
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# go to a website
# driver.get("https://www.amazon.com/")

# get find element by class
# driver.get("https://www.amazon.com/Corsair-Optical-Mechanical-Gaming-Keyboard-Hyper-Polling/dp/B0B9RLFYHW/ref=sr_1_1_sspa?keywords=gaming%2Bkeyboard&pd_rd_r=d14dd4d6-6f8c-46ee-8da4-d0982c6c08dc&pd_rd_w=PDKGW&pd_rd_wg=b44WP&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=38HY2W70SFD5A1E5WCJH&qid=1672133661&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTExNRzFTRDc5SkxVJmVuY3J5cHRlZElkPUEwOTA3NTE0M1RaNFRWVjJNNVFZNyZlbmNyeXB0ZWRBZElkPUExMDIwMzI3MldEQVFVUVZDME5KRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)
#
# # find element by Id
# price_by_id = driver.find_element("id", "corePrice_feature_div")
# print(price_by_id.text)

driver.get("https://www.python.org/")
# get element by name (search_bar)
search_bar = driver.find_element(By.NAME, "q")
print(search_bar)
print(search_bar.tag_name)

# image
python_logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(python_logo.size)

# by css Selector
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

# by xpath (locating html elements with a path structure)
# to copy xPATH, right click on the element in the inspection panel => copy => copy as xpath
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
driver.quit()