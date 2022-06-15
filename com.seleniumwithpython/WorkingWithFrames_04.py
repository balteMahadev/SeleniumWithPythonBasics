import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

#Switching to first frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium.chrome").click()
time.sleep(3)

#switching to default frame
driver.switch_to.default_content()

#switching to second frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"ChromeOptions").click()
time.sleep(3)

#switching to default frame
driver.switch_to.default_content()

#Switching to third frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//div[@class='topNav']//a[normalize-space()='Deprecated']").click()

