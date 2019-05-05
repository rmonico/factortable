from . import primegenerator


class Factorizer(object):

    def __init__(self):
        self.prime_generator = primegenerator.PrimeGenerator()

    def factor(self, n):
        factors = []

        self.prime_generator.reset()

        for prime in self.prime_generator:
            factors.append(0)

            while (n % prime == 0):
                factors[-1] += 1
                n = n // prime

            if n == 1:
                return factors
