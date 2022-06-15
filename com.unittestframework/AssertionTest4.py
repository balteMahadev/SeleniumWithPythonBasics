import os
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        list = {"python", "selenium", "java"}

        # assertIn
        self.assertIn("python", list)

        # assertNotIn
        self.assertNotIn("C++",list)


if __name__ == '__main__':
    unittest.main()
