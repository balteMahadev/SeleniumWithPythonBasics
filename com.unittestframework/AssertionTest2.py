import os
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        separator = os.sep
        driver = webdriver.Chrome(
            executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")
        driver.get("http://www.google.com/")
        titleOfWebPage = driver.title

        # assert True
        # self.assertTrue(titleOfWebPage == "Google", "Web Page title not matched")

        # assertNotEqual
        self.assertFalse(titleOfWebPage == "Google", "Web Page title  matched")



if __name__ == '__main__':
    unittest.main()
