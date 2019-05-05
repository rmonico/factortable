class PrimeGenerator(object):

    _first_prime = 2
    _known_primes = [_first_prime, _first_prime + 1]

    def __init__(self):
        self.reset()

    def next(self):
        if self.i == len(PrimeGenerator._known_primes):
            PrimeGenerator._known_primes.append(self._calculate_next_prime())

        next = PrimeGenerator._known_primes[self.i]
        self.i += 1

        return next

    def _calculate_next_prime(self):
        n = PrimeGenerator._known_primes[-1] + PrimeGenerator._first_prime

        while not self._is_prime(n):
            n += PrimeGenerator._first_prime

        return n

    def _is_prime(self, n):
        for prime in PrimeGenerator._known_primes:
            if n % prime == 0:
                return False

        return True

    def reset(self):
        self.i = 0
