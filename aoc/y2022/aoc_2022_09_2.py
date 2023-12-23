from aoc.helper import choose_puzzle_input, print_solution
import math


puzzle_input = choose_puzzle_input(
    y=2022,
    d=9,
    # sample_input_path="aoc_2022_09_2_inputsample.txt",
)


def signed_normalize(dir):
    try:
        if dir > 0:
            norm_dir = dir / dir
        else:
            norm_dir = -dir / dir
    except ZeroDivisionError:
        norm_dir = 0

    return norm_dir


def knot_movement(parent_x: int, parent_y: int, self_x: int, self_y: int):
    distance = math.dist([self_x, self_y], [parent_x, parent_y])

    if distance >= 2:
        self_x += signed_normalize(parent_x - self_x)
        self_y += signed_normalize(parent_y - self_y)

    return [self_x, self_y]


head_positions = [[1, 1]]
for line in puzzle_input:
    head_x, head_y = head_positions[-1]
    direction, amount = line.split(" ")

    # Move the head
    for i in range(int(amount)):
        if direction == "U":
            head_y += 1
        elif direction == "R":
            head_x += 1
        elif direction == "D":
            head_y -= 1
        elif direction == "L":
            head_x -= 1
        head_positions.append([head_x, head_y])


def move_rope(move_sequence: list, knots: int = 9):
    knot_positions = [move_sequence]

    for k in range(knots):
        calculate_positions = [[1, 1]]
        for parent in knot_positions[k]:
            x, y = calculate_positions[-1]
            calculate_positions.append(
                knot_movement(
                    parent_x=parent[0], parent_y=parent[1], self_x=x, self_y=y
                )
            )
        knot_positions.append(calculate_positions)

    return knot_positions[-1]


tail_positions = move_rope(move_sequence=head_positions, knots=9)


unique_positions = []
for tail_pos in tail_positions:
    if tail_pos not in unique_positions:
        unique_positions.append(tail_pos)

print_solution(solution=len(unique_positions), y=2022, d=9, part=2)
