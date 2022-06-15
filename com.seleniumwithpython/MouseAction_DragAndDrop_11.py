import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()

col_A = driver.find_element(By.XPATH, "//a[contains(text(),'BANK')]")
col_B = driver.find_element(By.XPATH, "//body[1]/section[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/ol[1]/li[1]")

actions = ActionChains(driver)
actions.drag_and_drop(col_A, col_B).perform()  # perform drag and drop action
# actions.click_and_hold(col_A).move_to_element(col_B).perform()