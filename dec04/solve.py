#!/usr/bin/env python3
from math import prod


def tickets():
    return open("input.txt", 'r').readlines()

def winners(row):
    _, ticket = row.split(":")
    winners, yours = ticket.split(r'|')
    winning_numbers = set(winners.split())
    my_numbers = set(yours.split())
    #print (my_numbers, winning_numbers, my_numbers & winning_numbers)
    return my_numbers & winning_numbers


def score(winning_numbers):
    count = len(winning_numbers)
    match count:
        case 0:
            return count
        case 1:
            return count
        case _:
            return pow(2, (count -1))

def score_of_winners(ticket):
    return score(winners(ticket))

print (sum([score_of_winners(ticket) 
            for ticket in tickets()]))

#for ticket in tickets():
#    w = winners(ticket)
#    print(score(w), w)


#print(sum([score(winning_numbers) 
#      for ticket in tickets() 
#      for winning_numbers in winners(ticket)]))