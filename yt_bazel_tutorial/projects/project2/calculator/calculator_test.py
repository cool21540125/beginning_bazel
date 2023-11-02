import unittest
from projects.project2.calculator.calculator import Calculator


class TestSum(unittest.TestCase):
    def test_sum(self):
        cc = Calculator()
        self.assertEqual(cc.add(1, 2), 3)

    def test_sum2(self):
        cc = Calculator()
        self.assertEqual(cc.add(51, 49), 100)


if __name__ == "__main__":
    unittest.main()
