import re
from math import lcm


from advent_of_code.helper import read_puzzle_input, print_solution

year = 2023
day = 8

puzzle_input = read_puzzle_input(input_path=f"aoc_{year}_{day:02d}_input.txt")

def y2023d8p1():
    instructions = [0 if x == "L" else 1 for x in puzzle_input[0]]
    data = {}
    re_pattern = re.compile(pattern=r"[=,()]")

    for line in puzzle_input[2:]:
        newline = re.sub(pattern=re_pattern, repl="", string=line).split()
        data[newline[0]] = newline[1:]

    current = "AAA"
    current_step = 0
    max_steps = 99999999
    instruction_index = 0

    while True:
        if current == "ZZZ" or current_step >= max_steps:
            break

        possibilities = data[current]
        current = possibilities[instructions[instruction_index]]
        instruction_index += 1

        if instruction_index == len(instructions):
            instruction_index = 0
        current_step += 1

    return current_step

def y2023d8p2():
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

    return lcm(*steps)


print_solution(solution=y2023d8p1, y=year, d=day, part=1)

print_solution(solution=y2023d8p2, y=year, d=day, part=2)
