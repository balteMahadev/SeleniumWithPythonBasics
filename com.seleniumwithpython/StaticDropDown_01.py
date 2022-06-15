import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


separator = os.sep
driver = webdriver.Chrome(executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()

dropDownElement = driver.find_element(By.XPATH,"(//select)[1]")
drp = Select(dropDownElement)

#Select by visible text
# drp.select_by_visible_text("American Samoa")

#select by index value
# drp.select_by_index(1)

#select by value
drp.select_by_value("ALB")

#print number of options are avalible
print(len(drp.options))

#Capture all the options and print them in console
all_options = drp.options
for option in all_options:
    print(option.text)