#!/usr/bin/env python3

def tickets():
    return open("input.txt", 'r').readlines()

def winners(row):
    _, ticket = row.split(":")
    winners, yours = ticket.split(r'|')
    winning_numbers = set(winners.split())
    my_numbers = set(yours.split())
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

def part1_score():
    return [score_of_winners(ticket)
            for ticket in tickets()]

def part2_score():
    scores = [1] * len(tickets())
    for r, ticket in enumerate(tickets()):
        w = winners(ticket)
        if w:
            for c in range(r + 1, min([r +1 + len(w), len(scores)])):
                scores[c] += scores[r]
    return scores


print (sum(part1_score()), sum(part2_score()))
