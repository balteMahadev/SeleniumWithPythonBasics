import os
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):

        # assertGreater
        self.assertGreater(100,10)

        # assertGreaterEqual
        self.assertGreaterEqual(100,100)

        # assertLess
        self.assertLess(10,100)

        # assertLessEqual
        self.assertLessEqual(100, 100)



if __name__ == '__main__':
    unittest.main()
