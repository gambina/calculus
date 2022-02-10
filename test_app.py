import unittest
from unittest import result
import app


class TestCalc(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown\n')

    def test_add(self):
        print('test_add')
        self.assertEqual(app.add(4, 5), 9)
        self.assertEqual(app.add(-1, 1), 0)
        self.assertEqual(app.add(-1, -3), -4)

    def test_substraction(self):
        print('test_substraction')
        self.assertEqual(app.substraction(4, 5), -1)
        self.assertEqual(app.substraction(-1, 1), -2)
        self.assertEqual(app.substraction(-1, -3), 2)

    def test_multiply(self):
        print('test_multiply')
        self.assertEqual(app.multiply(4, 5), 20)
        self.assertEqual(app.multiply(-1, 1), -1)
        self.assertEqual(app.multiply(-1, -3), 3)

    def test_divide(self):
        print('test_divide')
        self.assertEqual(app.divide(10, 5), 2)
        self.assertEqual(app.divide(-5, 1), -5)
        self.assertEqual(app.divide(-6, -3), 2)

        with self.assertRaises(ValueError):
            app.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
