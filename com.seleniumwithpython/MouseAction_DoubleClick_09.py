import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

doubleClickButton = driver.find_element(By.XPATH, "//button[contains(text(),'Copy Text')]")
actions = ActionChains(driver)

actions.double_click(doubleClickButton).perform()  # double-click on the element
