import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
fNameBox = driver.find_element(By.XPATH,"//input[@id='firstName']")
print(fNameBox.is_displayed()) #return true if it displayed else false
print(fNameBox.is_enabled()) #return true if it enabled else false
fNameBox.send_keys("Mahadev")

lNameBox = driver.find_element(By.XPATH,"//input[@id='lastName']")
print(lNameBox.is_displayed()) #return true if it displayed else false
print(lNameBox.is_enabled()) #return true if it enabled else false
lNameBox.send_keys("Balte")

EmailBox = driver.find_element(By.XPATH,"//input[@id='userEmail']")
print(EmailBox.is_displayed()) #return true if it displayed else false
print(EmailBox.is_enabled()) #return true if it enabled else false
EmailBox.send_keys("baltemahadev633@gmail.com")

GenderButton = driver.find_element(By.XPATH,"//label[normalize-space()='Male']")
GenderButton.click()



# driver.quit()

