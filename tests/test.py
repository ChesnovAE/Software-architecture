import unittest
from tst_fnc import pipska

class TestGame(unittest.TestCase):
    def test_func(self):
        self.assertEqual(pipska(), 1)
