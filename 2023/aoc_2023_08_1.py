from helper import choose_puzzle_input, print_solution
import re

year = 2023
day = 8

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_1_input_sample2.txt",
)
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


print_solution(solution=current_step, y=year, d=day, part=1)
