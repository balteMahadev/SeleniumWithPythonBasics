import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" +separator + "chromedriver.exe")

driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
driver.maximize_window()
product = driver.find_element(By.XPATH,"//button[@id='product-menu-toggle']")
automationPart = driver.find_element(By.XPATH,"//a[@aria-label='Automate']//div[@class='dropdown-link-text'][normalize-space()='Selenium testing at scale']")

actions = ActionChains(driver)
actions.move_to_element(product).move_to_element(automationPart).click().perform()

developers = driver.find_element(By.XPATH,"//button[@id='developers-menu-toggle']")
events = driver.find_element(By.XPATH,"//a[contains(text(),'Events')]")

actions.move_to_element(developers).move_to_element(events).click().perform()