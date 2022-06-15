import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
driver.maximize_window()

all_Rows = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
print(len(all_Rows))

all_Columns = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[1]/th")
print(len(all_Columns))

for r in range(2, len(all_Rows) + 1):
    for c in range(1, len(all_Columns) + 1):
        values = driver.find_element(By.XPATH,
                                     "//table[@id='customers']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(values, end='    ')
    print()
