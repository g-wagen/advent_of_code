from helper import choose_puzzle_input, print_solution
import math


puzzle_input = choose_puzzle_input(
    y=2022,
    d=9,
    # sample_input_path="aoc_2022_09_inputsample.txt",
)

head_positions = [[1, 1]]

for line in puzzle_input:
    x, y = head_positions[-1]
    direction, amount = line.split(" ")
    for i in range(int(amount)):
        if direction == "U":
            y += 1
        elif direction == "R":
            x += 1
        elif direction == "D":
            y -= 1
        elif direction == "L":
            x -= 1
        head_positions.append([x, y])


tail_positions = [[1, 1]]

for p, pos in enumerate(head_positions):
    tail_x, tail_y = tail_positions[-1]
    head_x, head_y = pos

    direction_x = head_x - tail_x
    direction_y = head_y - tail_y

    try:
        if direction_x > 0:
            norm_direction_x = direction_x / direction_x
        else:
            norm_direction_x = -direction_x / direction_x
    except ZeroDivisionError:
        norm_direction_x = 0
    try:
        if direction_y > 0:
            norm_direction_y = direction_y / direction_y
        else:
            norm_direction_y = -direction_y / direction_y
    except ZeroDivisionError:
        norm_direction_y = 0

    distance = math.dist([tail_x, tail_y], [head_x, head_y])

    if distance >= 2:
        tail_x += norm_direction_x
        tail_y += norm_direction_y
        tail_positions.append([tail_x, tail_y])


unique_positions = []
for tp in tail_positions:
    if tp not in unique_positions:
        unique_positions.append(tp)

print_solution(solution=len(unique_positions), y=2022, d=9, part=1)
