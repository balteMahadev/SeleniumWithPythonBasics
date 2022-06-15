import unittest


def setUpModule(self):
    print("setUpModule")


def tearDownModule(self):
    print("tearDownModule")
class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is Login test")

    @classmethod
    def tearDown(self):
        print("This is log out")

    @classmethod
    def setUpClass(cls):
        print("Opening the application")

    def test_search(self):
        print("This is search test")

    def test_advancesearch(self):
        print(" This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paid recharge test")

    @classmethod
    def tearDownClass(cls):
        print("Close the appllication")


if __name__ == 'main':
    unittest.main()