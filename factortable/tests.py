import unittest
from . import factortable
from . import factorizer


class FactorTableTests(unittest.TestCase):

    def test_get_factor_string(self):
        self.assertEqual(factortable.get_factor_string(6, [1, 1]), '6: 1, 1')


class FactorizerTests(unittest.TestCase):

    def test_factorizer_factor(self):
        self.assertEqual(factorizer.Factorizer().factor(6), [1, 1])

if __name__ == '__main__':
    unittest.main()
