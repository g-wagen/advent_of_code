from aoc.helper import get_puzzle_input, print_solution
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

puzzle_input = get_puzzle_input(y=2022, d=10)
# with open('aoc_2022_10_inputsample2.txt', 'r') as f:
#     puzzle_input = f.read().splitlines()

x = 1
total_cycles = 0
thing = dict()
display = [[" " for x in range(40)] for x in range(6)]

for c, cycle in enumerate(puzzle_input):
    if "noop" in cycle:
        total_cycles += 1
        thing[total_cycles] = x
    if cycle.startswith("addx"):
        number = int(cycle.split()[1])
        total_cycles += 1
        thing[total_cycles] = x
        x += number
        total_cycles += 1
        thing[total_cycles] = x


sums = []

for k, v in thing.items():
    line = k // 40
    position = k % 40
    if abs(v - position) <= 1:
        display[line][position] = "#"

for x in display:
    print_solution(solution="".join(x), y=2022, d=10, part=2)
