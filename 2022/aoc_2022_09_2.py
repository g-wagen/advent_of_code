from helper import choose_puzzle_input, print_solution
import math


puzzle_input = choose_puzzle_input(
    y=2022,
    d=9,
    # sample_input_path="aoc_2022_09_2_inputsample.txt",
)

head_positions = [[1, 1]]

one_positions = [[1, 1]]
two_positions = [[1, 1]]
three_positions = [[1, 1]]
four_positions = [[1, 1]]
five_positions = [[1, 1]]
six_positions = [[1, 1]]
seven_positions = [[1, 1]]
eight_positions = [[1, 1]]
nine_positions = [[1, 1]]


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

for head_p in head_positions:
    one_x, one_y = one_positions[-1]
    one_positions.append(
        knot_movement(
            parent_x=head_p[0], parent_y=head_p[1], self_x=one_x, self_y=one_y
        )
    )

for one_p in one_positions:
    two_x, two_y = two_positions[-1]
    two_positions.append(
        knot_movement(parent_x=one_p[0], parent_y=one_p[1], self_x=two_x, self_y=two_y)
    )

for two_p in two_positions:
    three_x, three_y = three_positions[-1]
    three_positions.append(
        knot_movement(
            parent_x=two_p[0], parent_y=two_p[1], self_x=three_x, self_y=three_y
        )
    )

for three_p in three_positions:
    four_x, four_y = four_positions[-1]
    four_positions.append(
        knot_movement(
            parent_x=three_p[0], parent_y=three_p[1], self_x=four_x, self_y=four_y
        )
    )

for four_p in four_positions:
    five_x, five_y = five_positions[-1]
    five_positions.append(
        knot_movement(
            parent_x=four_p[0], parent_y=four_p[1], self_x=five_x, self_y=five_y
        )
    )

for five_p in five_positions:
    six_x, six_y = six_positions[-1]
    six_positions.append(
        knot_movement(
            parent_x=five_p[0], parent_y=five_p[1], self_x=six_x, self_y=six_y
        )
    )

for six_p in six_positions:
    seven_x, seven_y = seven_positions[-1]
    seven_positions.append(
        knot_movement(
            parent_x=six_p[0], parent_y=six_p[1], self_x=seven_x, self_y=seven_y
        )
    )

for seven_p in seven_positions:
    eight_x, eight_y = eight_positions[-1]
    eight_positions.append(
        knot_movement(
            parent_x=seven_p[0], parent_y=seven_p[1], self_x=eight_x, self_y=eight_y
        )
    )

for eight_p in eight_positions:
    nine_x, nine_y = nine_positions[-1]
    nine_positions.append(
        knot_movement(
            parent_x=eight_p[0], parent_y=eight_p[1], self_x=nine_x, self_y=nine_y
        )
    )


unique_positions = []
for two_p in nine_positions:
    if two_p not in unique_positions:
        unique_positions.append(two_p)

print_solution(solution=len(unique_positions), y=2022, d=9, part=2)
