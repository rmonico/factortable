import unittest
from . import factortable
from . import factorizer
from . import primegenerator


class FactorTableTests(unittest.TestCase):

    def test_get_factor_string(self):
        self.assertEqual(factortable.get_factor_string(6, [1, 1]), '6: 1, 1')


class FactorizerTests(unittest.TestCase):

    def test_factorizer_factor(self):
        self.assertEqual(factorizer.Factorizer().factor(6), [1, 1])


class PrimeGeneratorTests(unittest.TestCase):

    def test_prime_generation(self):
        generator = primegenerator.PrimeGenerator()

        self.assertEqual(generator.__next__(), 2)
        self.assertEqual(generator.__next__(), 3)
        self.assertEqual(generator.__next__(), 5)
        self.assertEqual(generator.__next__(), 7)
        self.assertEqual(generator.__next__(), 11)
        self.assertEqual(generator.__next__(), 13)
        self.assertEqual(generator.__next__(), 17)
        self.assertEqual(generator.__next__(), 19)
        self.assertEqual(generator.__next__(), 23)

    def test_reset(self):
        generator = primegenerator.PrimeGenerator()

        generator.__next__()
        generator.__next__()

        generator.reset()

        self.assertEqual(generator.__next__(), 2)


if __name__ == '__main__':
    unittest.main()
