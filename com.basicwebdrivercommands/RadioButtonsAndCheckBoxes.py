import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
driver.maximize_window()

# Verify Radio button is selected or not
Excel = driver.find_element(By.XPATH,"//input[@value='Photoshop']")
print(Excel.is_selected())

# Click the radio button box
Excel.click()
print(Excel.is_selected())

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
ele1 = driver.find_element(By.XPATH,"//label[normalize-space()='Sports']")
print(ele1.text)
ele1.click()
ele2 = driver.find_element(By.XPATH,"//label[normalize-space()='Reading']")
ele2.click()
print(ele2.text)

