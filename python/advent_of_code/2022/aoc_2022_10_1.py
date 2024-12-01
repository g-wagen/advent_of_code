from advent_of_code.helper import get_puzzle_input, print_solution
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

puzzle_input = get_puzzle_input(y=2022, d=10)
with open("aoc_2022_10_inputsample2.txt", "r") as f:
    puzzle_input = f.read().splitlines()

x = 1
total_cycles = 0
thing = dict()

for c, cycle in enumerate(puzzle_input, 1):
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
    k = k + 1
    if k in [20, 60, 100, 140, 180, 220]:
        print(f"cycle: {k}: {k * v}")
        sums.append(k * v)

print_solution(sum(sums), y=2022, d=10, part=1)
