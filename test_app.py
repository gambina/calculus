import unittest
from unittest import result
import app


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = app.add(4, 5)
        self.assertEqual(result, 9)
