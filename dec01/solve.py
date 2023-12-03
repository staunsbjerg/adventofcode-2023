#!/usr/bin/env python3

import sys


def numbers():
    for puzze_line in puzzle_input():
        yield first_digit(puzze_line) + last_digit(puzze_line) * 10

def puzzle_input():
    for line in sys.stdin.readlines():
        yield line


def first_digit(input: str) -> int:
    for c in input:
        try:
            return int(c)
        except ValueError:
            continue
    raise "no digits in " + input

def last_digit(input: str) -> int:
    return first_digit(input[::-1])


print(sum(numbers()))