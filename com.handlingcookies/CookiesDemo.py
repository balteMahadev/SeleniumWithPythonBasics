import os

from selenium import webdriver

separator = os.sep
driver = webdriver.Chrome(
    executable_path=os.getcwd() + separator + "drivers" + separator + "chromedriver" + separator + "chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

#  Capture all the cookies created by browser

cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies have been created
print(cookies)  # printing all the cookies in the form of key value pair

# Adding new cookie to the browser
cookies = {'name': 'My cookie', 'value': '123456'}
driver.add_cookie(cookies)

cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after adding new cookie
print(cookies)  # print all the cookie pairs

# deleting the cookie

driver.delete_cookie('My cookie')
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after deleting the cookie
print(cookies)  # print all the cookie pairs

# deleting all the cookies from the browser
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after deleting the cookie
print(cookies)

