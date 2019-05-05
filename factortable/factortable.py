#!/usr/bin/python3

from .factorizer import Factorizer


def get_factor_string(n, factors):
    s = "{}: "

    for i in range(0, len(factors)):
        s += (", " if i > 0 else "")
        s += "{}"

    return s.format(n, *factors)


def main():
    limit = 100

    factorizer = Factorizer()

    for n in range(2, limit + 1):
        factors = factorizer.factor(n)

        s = get_factor_string(n, factors)

        print(s)

if __name__ == '__main__':
    main()
