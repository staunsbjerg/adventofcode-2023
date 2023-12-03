#!/usr/bin/env python3

import sys
import operator


literals = [(str(name), pos + 1) 
            for pos, name in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])]

digits = [(str(x), x) for x in range(1, 10)]

ALL_PATTERNS = digits + literals
REVERSE_PATTERNS = digits + [(name[::-1], value) for name, value in literals]

def numbers():
    for puzzle_line in puzzle_input():
        yield first_digit(puzzle_line) * 10 + last_digit(puzzle_line)

def puzzle_input():
    for line in sys.stdin.readlines():
        yield line.strip()


def first_digit(input: str, patterns=ALL_PATTERNS) -> int:
    matches = [(pos, value) 
               for pattern, value in patterns 
               if (pos := input.find(pattern)) >= 0]
    return min(matches, key=operator.itemgetter(0))[1]


def last_digit(input: str) -> int:
    return first_digit(input[::-1], patterns=REVERSE_PATTERNS)


print(sum(numbers()))