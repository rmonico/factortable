class PrimeGenerator(object):

    def __init__(self):
        self.i = 0
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def next(self):
        next = self.primes[self.i]
        self.i += 1

        return next
