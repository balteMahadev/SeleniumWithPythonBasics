import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.current_window_handle) #CDwindow-956FD0EBAAA398617B6D8A6E3639BE0E window id

driver.find_element(By.XPATH,"(//button[@class='btn btn-info'][normalize-space()='click'])[1]").click()
handles = driver.window_handles #returns all the handle values of opened windows
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.current_window_handle)
    if driver.title == "Frames & windows":
        driver.close()




# driver.quit()