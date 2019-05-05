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

        self.assertEqual(generator.next(), 2)
        self.assertEqual(generator.next(), 3)
        self.assertEqual(generator.next(), 5)
        self.assertEqual(generator.next(), 7)
        self.assertEqual(generator.next(), 11)
        self.assertEqual(generator.next(), 13)
        self.assertEqual(generator.next(), 17)
        self.assertEqual(generator.next(), 19)
        self.assertEqual(generator.next(), 23)

    def test_reset(self):
        generator = primegenerator.PrimeGenerator()

        generator.next()
        generator.next()

        generator.reset()

        self.assertEqual(generator.next(), 2)


if __name__ == '__main__':
    unittest.main()
