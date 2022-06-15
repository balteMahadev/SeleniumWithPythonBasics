import os
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        separator = os.sep
        driver = webdriver.Chrome(
            executable_path=os.getcwd() + separator + "drivers" + separator + "chromeDriver" + separator + "chromedriver.exe")

        # assertIsNone
        apple = None
        self.assertIsNone(apple)

        # assertIsNotNone
        self.assertIsNotNone(driver)


if __name__ == '__main__':
    unittest.main()
