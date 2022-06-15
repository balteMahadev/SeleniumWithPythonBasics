from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

separator = os.sep
driver = webdriver.Chrome(
    executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator+"chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath(
    "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
time.sleep(5)

# driver.close() # close currently focussed browser

# driver.quit() # closes all the browers
