import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame("frame-one1434677811")
driver.find_element(By.ID,"RESULT_FileUpload-10").send_keys("D://Sample.png")

