import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" +separator + "chromedriver.exe")
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"(//button[@id='alertButton'])[1]").click()
time.sleep(5)
print(driver.switch_to.alert.text)

#switch to alert.accept
driver.switch_to.alert.accept()

driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
time.sleep(5)
print(driver.switch_to.alert.text)
#switch to alert.dismiss
driver.switch_to.alert.dismiss()




