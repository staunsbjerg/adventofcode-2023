#!/usr/bin/env python3

import sys
from collections import defaultdict
from operator import itemgetter
from functools import reduce, cache
import re

@cache
def games():
    return list(map(parse_game, sys.stdin.readlines()))

def parse_game(line: str):

    def zero():
        return 0
    
    def cube_draw(a_dict, match):
        a_dict[match.group(2)] = int(match.group(1))
        return a_dict
    
    def game_number_and_rounds():
        return re.compile(r"Game (\d+):(.*)$").match(line).group(1, 2)

    def round_to_dict(round):
        return reduce(
            cube_draw,
            re.compile(r"(\b\d+\b) (\b[a-z]+\b)").finditer(round), 
            defaultdict(zero))

    game_no, rounds = game_number_and_rounds()    
    return int(game_no), [round_to_dict(round) for round in rounds.split(";")]


def possible_games():
    for game_no, rounds in games():
        if all(is_possible(round) for round in rounds):
            yield game_no

def is_possible(round):
    return round["red"] <= 12 and round["green"] <= 13 and round["blue"] <= 14

def power_of_minimum_games():
    def mul(x, y):
        return x * y
    for _, rounds in games():
        yield reduce(mul, [max(map(itemgetter(color), rounds)) 
                           for color in ("red", "green", "blue")])
        

print(sum(possible_games()))
print(sum(power_of_minimum_games()))