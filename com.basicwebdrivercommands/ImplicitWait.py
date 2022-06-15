import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://demoqa.com/login")
driver.maximize_window()

# implicit wait
driver.implicitly_wait(10)

assert "ToolsQA" in driver.title

driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("Mahadev")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Mahadev@633")
driver.find_element(By.XPATH,"//button[@id='login']").click()
