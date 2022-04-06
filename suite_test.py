import unittest
import number as def_number


class number_test_case(unittest.TestCase):
    # fun must start with test_ => to make .main() run it
    def test_add_number(self):
        result1 = def_number.add_numbers()
        result2 = def_number.add_numbers(10, 20)
        result3 = def_number.add_numbers(10, 20, 30)
        self.assertEqual("empty args", result1)  # true
        self.assertEqual(30, result2)  # true
        self.assertEqual(60, result3)  # true
        self.assertEqual(150, def_number.add_numbers(100, 200))  # false

    def test_compare_numbers(self):
        self.assertNotEqual(150, def_number.compare_numbers(
            150, 200))  # true => 100 != 200

    def test_boolean_equality_numbers(self):
        self.assertTrue(def_number.compare_numbers(10, 10))
        self.assertTrue(def_number.compare_numbers(10, 50),"firstnumber not equal second number")  # will failed

    def test_insert(self):
        name = "mohamed"
        container = "hello this is mohamed Alabasy from unit test lab 01"
        self.assertIn(name, container,f"the {name} doesn't exist in {container}")  # true


my_suite = unittest.TestSuite()
my_suite.addTest(unittest.makeSuite(number_test_case))

runner = unittest.TextTestRunner()
runner.run(my_suite)
