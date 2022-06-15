import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
inputBoxes = driver.find_elements(By.XPATH,"//input[@type='text']")
print(len(inputBoxes))
# First way to find elements
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Mahadev")
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Balte")

# Second way to find elemets
driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("baltemahadev633@gmail.com")
driver.find_element_by_css_selector("#userNumber").send_keys("7259279633")
