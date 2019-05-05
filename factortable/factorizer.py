class Factorizer(object):

    def __init__(self):
        self.prime_table = [2, 3, 5]

    def factor(self, n):
        factors = []

        for i in range(0, len(self.prime_table)):
            prime = self.prime_table[i]
            factors.append(0)

            while (n % prime == 0) and (n > 1):
                factors[i] += 1
                n = n // prime

            if n == 1:
                break

        return factors
