import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" +separator + "chromedriver.exe")

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

# Scroll down the page by pixel

# driver.execute_script("window.scrollBy(0,1000)","")

# Scroll down the page till element found

# flag = driver.find_element(By.XPATH, "//img[@src='/img/flags/small/tn_in-flag.gif']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

