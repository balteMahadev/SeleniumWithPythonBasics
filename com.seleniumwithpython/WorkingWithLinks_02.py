import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,"a")

#How many links present in a page
print("Number of links present in a page",len(links))

#Print all links text present in a web page
for link in links:
    print(link.text)

#Clicking on the link by using link text
# driver.find_element(By.LINK_TEXT,"EXCEL BASICS").click()

#Clicking on the link by using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"ACC").click()


