from aoc.helper import choose_puzzle_input, print_solution
import re
from math import lcm

year = 2023
day = 8

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_2_input_sample.txt",
)
instructions = [0 if x == "L" else 1 for x in puzzle_input[0]]
data = {}
re_pattern = re.compile(pattern=r"[=,()]")

for line in puzzle_input[2:]:
    newline = re.sub(pattern=re_pattern, repl="", string=line).split()
    data[newline[0]] = newline[1:]


start_nodes = [x for x in data if x.endswith("A")]
steps = [0] * len(start_nodes)
instruction_index = 0

for i, s in enumerate(start_nodes):
    current = s
    current_step = steps[i]

    while True:
        if current.endswith("Z"):
            break

        possibilities = data[current]
        next_nodes = possibilities[instructions[instruction_index]]

        current = next_nodes
        instruction_index += 1

        if instruction_index == len(instructions):
            instruction_index = 0

        current_step += 1

    steps[i] = current_step

print_solution(solution=lcm(*steps), y=year, d=day, part=2)
