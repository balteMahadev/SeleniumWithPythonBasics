import os
import ExcelUtils

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(
    executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()

excel_file_path = os.getcwd() + separator + "ExcelFiles" + separator + "Login" + separator + "logintests.xlsx"
rows = ExcelUtils.getRowCount(excel_file_path, "Sheet1")

for r in range(2, rows + 1):
    userName = ExcelUtils.readData(excel_file_path, "Sheet1", r, 1)
    password = ExcelUtils.readData(excel_file_path, "Sheet1", r, 2)
    driver.find_element(By.NAME, "userName").send_keys(userName)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    if driver.title == "Login: Mercury Tours":
        print("test is passed")
        ExcelUtils.writeData(excel_file_path, "Sheet1", r, 3, "test passed")
        driver.back()
    else:
        print("test failed")
        ExcelUtils.writeData(excel_file_path, "Sheet1", r, 3, "test failed")
