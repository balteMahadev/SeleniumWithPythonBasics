import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_advancesearch(self):
        print("This is test_advancesearch test")

    @unittest.skipIf(1==2,"false")
    def test_prepaidRecharge(self):
        print("This is test_prepaidRecharge test")

    def test_postpaidRecharge(self):
        print("This is test_postpaidRecharge test")

    def test_loginbyemail(self):
        print("This is test_loginbyemail test")

    def test_loginbytwitter(self):
        print("This is test_loginbytwitter test")

if __name__ == '__main__':
    unittest.main()

