from helper import get_puzzle_input, print_solution
import numpy as np
from string import ascii_lowercase
import networkx as nx


puzzle_input = get_puzzle_input(y=2022, d=13)
with open('aoc_2022_13_inputsample.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

data = [eval(p) for p in puzzle_input if p]
pairs = dict()

for i, d in enumerate(data):
    if i%2 == 0:
        pairs[i//2] = data[i:i+2]

def both_lists(left, right):
    return isinstance(left, list) and isinstance(right, list)

def both_ints(left, right):
    return isinstance(left, int) and isinstance(right, int)

def change_types(left, right):
    out = dict()
    if isinstance(left, int) and isinstance(right, list):
        out.update({'left': [left], 'right': right})
    elif isinstance(left, list) and isinstance(right, int):
        out.update({'left': left, 'right': [right]})
    return out

def types_mixed(left, right):
    return isinstance(left, int) and isinstance(right, list) or isinstance(left, list) and isinstance(right, int)



def compare(left, right):
    if both_lists(left, right):
        print('found lists!')
        for i, item in enumerate(left):
            compare(item, right[i])
    if both_ints(left, right):
        print(f'both are ints {left}, {right}')
        if left < right:
            return True
        elif left == right:
            pass
        elif left > right:
            return False
    if types_mixed(left, right):
        print('types mismatch, converting')
        new_left, new_right = change_types(left, right)
        compare(new_left, new_right)


compare(pairs[1][0], pairs[1][1])
#
#
# for i, pp in pairs.items():
#     left = pp[0]
#     right = pp[1]



