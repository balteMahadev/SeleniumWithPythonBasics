import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()