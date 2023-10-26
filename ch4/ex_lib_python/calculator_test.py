import unittest
from ch4.ex_lib_python.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
