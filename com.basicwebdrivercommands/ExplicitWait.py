import os
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://www.expedia.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Flights']").click() #clicks on flight button
time.sleep(2)  # this is for python
Leaving_from = driver.find_element(By.ID,"location-field-leg1-origin").send_keys("SFO")
Leaving_from.click()
wait = WebDriverWait(driver,10)
time.sleep(6)
driver.find_element(By.XPATH,"//button[@aria-label='Going to']").click()
wait.until(EC.element_to_be_clickable)

