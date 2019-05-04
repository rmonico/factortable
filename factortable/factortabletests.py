import unittest
from factortable import get_factor_string


class FactorTableTests(unittest.TestCase):

    def test_get_factor_string(self):
        self.assertEqual(get_factor_string(6, [1, 1]), '6: 1, 1')


if __name__ == '__main__':
    unittest.main()
