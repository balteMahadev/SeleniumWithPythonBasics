import os

from selenium import webdriver

separator = os.sep
driver = webdriver.Chrome(
    executable_path=os.getcwd() + separator + "drivers" + separator + "chromedriver" + separator + "chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window() 
file = os.getcwd() + separator + "ScreenShots\homePage2.jpg"
# driver.save_screenshot(file)
driver.get_screenshot_as_file(file)
