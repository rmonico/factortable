#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


from .factorizer import Factorizer

# TODO: implmement print_sorted_by_factor_count


def main():
    global args
    global table

    args = parse_command_line()

    factorizer = Factorizer()

    table = []

    for n in range(2, args.limit + 1):
        factors = factorizer.factor(n)

        table.append(factors)

    if args.sort_key == "n":
        print_sorted_by_n()
    else:
        print_sorted_by_factor_count()


def parse_command_line():
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--sort-key", choices=["n", "factor_count"], default="n")
    parser.add_argument("-l", "--limit", type=int, default=101, help="Limit to generate factor table")

    return parser.parse_args()


def get_factor_string(n, factors):
    s = "{}: "

    for i in range(0, len(factors)):
        s += (", " if i > 0 else "")
        s += "{}"

    return s.format(n, *factors)


def print_sorted_by_n():
    global table

    for n in range(len(table)):
        s = get_factor_string(n + 2, table[n])

        print(s)


def print_sorted_by_factor_count():
    global table

    table.sort(key=lambda n: len(n))

    for i in range(len(table[-1]), 1):
        table.sort(key=lambda n: n[i])

    print("TODO")

if __name__ == '__main__':
    main()
