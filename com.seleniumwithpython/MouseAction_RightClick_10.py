import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

rightClickButton = driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
copyButton = driver.find_element(By.XPATH,"//span[contains(text(),'Copy')]")

actions = ActionChains(driver)
actions.context_click(rightClickButton).move_to_element(copyButton).click().perform()
driver.switch_to.alert.accept()

