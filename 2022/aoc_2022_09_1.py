from helper import choose_puzzle_input, print_solution
import math


puzzle_input = choose_puzzle_input(
    y=2022,
    d=9,
    # sample_input_path="aoc_2022_09_1_inputsample.txt",
)

head_positions = [[1, 1]]
tail_positions = [[1, 1]]


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

        tail_x, tail_y = tail_positions[-1]

        tail_positions.append(
            knot_movement(
                parent_x=head_x, parent_y=head_y, self_x=tail_x, self_y=tail_y
            )
        )


unique_positions = []
for tp in tail_positions:
    if tp not in unique_positions:
        unique_positions.append(tp)

print_solution(solution=len(unique_positions), y=2022, d=9, part=1)
