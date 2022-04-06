from pickle import FALSE
import unittest
# unittest live cycle


class Live_Cycle(unittest.TestCase):
    def setUpClass(self) -> None:
        print("setUpClass will be call first one")

    @classmethod
    def setUp(self) -> None:
        # return super().setUp()
        print("tearDown before every test method")

    @classmethod
    def tearDown(self) -> None:
        # return super().tearDown()
        print("tearDown after every test method")

    @classmethod
    def tearDownClass(self) -> None:
        print("tearDownClass will be call last one")


if __name__ == "__main__":
    unittest.main()
