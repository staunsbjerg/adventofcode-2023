#!/usr/bin/env python3

from math import prod
import re


def is_symbol(c):
    return c not in '01234566789.'

schematic = open('input.txt', 'r').readlines()

parts = {(row, col): []
         for row in range(140)
         for col in range(140)
         if is_symbol(schematic[row][col])}

def edges(row, number_match):
    return {(r, c)
            for r in (row-1, row, row+1)
            for c in range(number_match.start()-1, number_match.end()+1)}

def adjacent_parts(row, number_match):
    return edges(row, number_match) & parts.keys()
    

for row, line in enumerate(schematic):
    for number in re.finditer(r'\d+', line):
        for coord in adjacent_parts(row, number):
            parts[coord].append(int(number.group()))

print(sum(sum(part_numbers)
          for part_numbers in parts.values()))

print(sum(prod(part_numbers)
          for part_numbers in parts.values() 
          if len(part_numbers) == 2))