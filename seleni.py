import os
import time
from selenium import webdriver

os.environ["PATH"] += r"/home/rahul/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
# driver.get("https://www.linkedin.com/feed/")

time.sleep(30)

driver.quit()
