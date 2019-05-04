#!/usr/bin/python3


def get_factor_string(n, factors):
    s = "{}: "

    for i in range(0, len(factors)):
        s += (", " if i > 0 else "")
        s += "{}"

    return s.format(n, *factors)


def main():
    factor_string = get_factor_string(6, [1, 1])

    print(factor_string)

    # limit = 100

    # factorizer = Factorizer()

    # for n in range(2, limit + 1):
    #     factors = factorizer.factor(n)

    #     print_factors(n, factors)

if __name__ == '__main__':
    main()
