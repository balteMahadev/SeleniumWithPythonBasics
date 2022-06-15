import os
import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        separator = os.sep
        self.driver = webdriver.Chrome(
            executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
        self.driver.get("http://www.google.com/")
        print("Title of the page is", self.driver.title)

    def test_Bing(self):
        separator = os.sep
        self.driver = webdriver.Chrome(
            executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
        self.driver.get("http://bing.com")
        print("Title of the page is ", self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
