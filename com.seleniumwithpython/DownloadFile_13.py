import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" +separator + "chromedriver.exe")

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# Download a text file

driver.find_element(By.ID, "textbox").send_keys("testing download test file")
driver.find_element(By.XPATH, "//button[@id='createTxt']").click()
driver.find_element(By.XPATH, "//a[@id='link-to-download']").click()

# Download pdf file
driver.find_element(By.XPATH,"//textarea[@id='pdfbox']").send_keys("pdf file")
driver.find_element(By.XPATH,"//button[@id='createPdf']").click()
driver.find_element(By.XPATH,"//a[@id='pdf-link-to-download']").click()
